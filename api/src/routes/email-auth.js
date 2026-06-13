'use strict';

const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const tls = require('tls');
const pool = require('../db');

const router = express.Router();

const SMTP_HOST = process.env.SMTP_HOST || 'smtp.qq.com';
const SMTP_PORT = parseInt(process.env.SMTP_PORT || '465', 10);
const SMTP_USER = process.env.SMTP_USER || 'cgartlab@qq.com';
const SMTP_PASS = process.env.SMTP_PASS || 'xuttpgidcjgbdffh';
const JWT_SECRET = process.env.CASDOOR_JWT_SECRET || 'guoxue-supabase-shared-secret-2026';
const CASDOOR_URL = process.env.CASDOOR_URL || 'https://casdoor.8023laozhanshi.cc';

const EMAIL_HTML_TEMPLATE = `<div style="max-width:560px;margin:24px auto;background:#fff;border-radius:12px;padding:24px 32px;font-family:sans-serif"><h2 style="margin:0;font-size:18px;color:#333">国学课堂</h2><hr style="border:none;border-top:1px solid #eee"><p style="margin:16px 0;font-size:15px;color:#333">您好，</p><p style="margin:0 0 16px;font-size:15px;color:#333">您的邮箱验证码为：</p><div style="text-align:center;margin:24px 0"><span style="display:inline-block;padding:10px 36px;font-size:30px;font-weight:bold;letter-spacing:10px;color:#1677ff;background:#f0f5ff;border-radius:8px">%s</span></div><p style="margin:0;font-size:13px;color:#888">验证码有效期为 <strong>5 分钟</strong>，请勿泄露给他人。</p><hr style="border:none;border-top:1px solid #eee"><p style="margin:16px 0 0;font-size:11px;color:#bbb;text-align:center">此邮件由系统自动发送，请勿回复</p></div>`;

function randomCode() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

function buildSmtpClient() {
  let socket = null;
  let connected = false;
  const commandQueue = [];
  let currentResolver = null;
  let currentRejecter = null;

  function sendCommand(cmd) {
    return new Promise((resolve, reject) => {
      if (!connected) {
        reject(new Error('Not connected'));
        return;
      }
      const line = cmd + '\r\n';
      socket.write(line, 'utf8', (err) => {
        if (err) reject(err);
        else resolve();
      });
    });
  }

  function readResponse() {
    return new Promise((resolve, reject) => {
      const chunks = [];
      socket.once('data', (chunk) => {
        chunks.push(chunk.toString());
        const response = chunks.join('');
        const lines = response.split('\r\n');
        const lastLine = lines[lines.length - 1];
        if (lastLine.startsWith('354') || lastLine.startsWith('250') || lastLine.startsWith('235') || lastLine.startsWith('220') || lastLine.startsWith('221')) {
          resolve(lastLine);
        } else {
          reject(new Error('SMTP response: ' + lastLine));
        }
      });
      socket.once('error', reject);
    });
  }

  return {
    connect() {
      return new Promise((resolve, reject) => {
        socket = tls.connect(SMTP_PORT, SMTP_HOST, { rejectUnauthorized: false }, () => {
          connected = true;
          resolve();
        });
        socket.setEncoding('utf8');
        socket.on('data', (chunk) => {
          const lines = chunk.split('\r\n');
          for (const line of lines) {
            if (line.startsWith('235 ') || line.startsWith('250 ') || line.startsWith('354 ') || line.startsWith('220 ') || line.startsWith('221 ')) {
              // ready
            }
          }
        });
        socket.on('error', reject);
        socket.on('close', () => { connected = false; });

        socket.once('data', () => {});
        setTimeout(() => reject(new Error('SMTP connect timeout')), 10000);
      });
    },

    sendEmail(to, subject, html) {
      return new Promise(async (resolve, reject) => {
        try {
          const code = Buffer.from(`${SMTP_USER}:${SMTP_PASS}`).toString('base64');

          await sendCommand('EHLO localhost');
          await readResponse();

          await sendCommand('AUTH LOGIN');
          await readResponse();

          await sendCommand(Buffer.from(SMTP_USER).toString('base64'));
          await readResponse();

          await sendCommand(Buffer.from(SMTP_PASS).toString('base64'));
          await readResponse();

          await sendCommand(`MAIL FROM:<${SMTP_USER}>`);
          await readResponse();

          await sendCommand(`RCPT TO:<${to}>`);
          await readResponse();

          await sendCommand('DATA');
          await readResponse();

          const fromHeader = `From: 国学课堂 <${SMTP_USER}>\r\n`;
          const toHeader = `To: ${to}\r\n`;
          const subjectHeader = `Subject: ${subject}\r\n`;
          const mimeHeaders = `MIME-Version: 1.0\r\nContent-Type: text/html; charset=UTF-8\r\n`;
          const emailContent = fromHeader + toHeader + subjectHeader + mimeHeaders + '\r\n' + html;
          const dotStuffed = emailContent.replace(/\n\./g, '\n..');
          await sendCommand(dotStuffed + '\r\n.');
          await readResponse();

          await sendCommand('QUIT');
          await readResponse();

          socket.end();
          resolve();
        } catch (err) {
          socket.end();
          reject(err);
        }
      });
    }
  };
}

async function sendEmailCode(to, code) {
  const client = buildSmtpClient();
  await client.connect();
  const html = EMAIL_HTML_TEMPLATE.replace('%s', code);
  await client.sendEmail(to, '国学课堂 邮箱验证码', html);
}

function signJwt(payload) {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '24h' });
}

router.post('/send-code', async (req, res) => {
  try {
    const { email, purpose } = req.body;
    if (!email || !purpose) {
      return res.status(400).json({ error: 'email and purpose are required' });
    }
    if (!['login', 'register'].includes(purpose)) {
      return res.status(400).json({ error: 'invalid purpose' });
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({ error: 'invalid email format' });
    }

    const existing = await pool.query(
      `SELECT id FROM email_verification_codes
       WHERE email = $1 AND purpose = $2 AND used_at IS NULL AND expires_at > NOW()
       ORDER BY created_at DESC LIMIT 1`,
      [email, purpose]
    );
    if (existing.rows.length > 0) {
      const age = (Date.now() - existing.rows[0].created_at.getTime()) / 1000;
      if (age < 60) {
        return res.status(429).json({ error: 'please wait before requesting another code' });
      }
    }

    const code = randomCode();
    const codeHash = crypto.createHash('bcrypt').syncBcrypt ? crypto.createHash('sha256').update(code).digest('hex') : code;

    await pool.query(
      `UPDATE email_verification_codes SET used_at = NOW() WHERE email = $1 AND purpose = $2 AND used_at IS NULL`,
      [email, purpose]
    );
    await pool.query(
      `INSERT INTO email_verification_codes (email, code_hash, purpose, expires_at)
       VALUES ($1, $2, $3, NOW() + INTERVAL '5 minutes')`,
      [email, codeHash, purpose]
    );

    try {
      await sendEmailCode(email, code);
    } catch (mailErr) {
      console.error('[EmailAuth] send-email error:', mailErr);
    }

    res.json({ success: true });
  } catch (err) {
    console.error('[EmailAuth] send-code error:', err);
    res.status(500).json({ error: 'internal error' });
  }
});

router.post('/verify-login', async (req, res) => {
  try {
    const { email, code } = req.body;
    if (!email || !code) {
      return res.status(400).json({ error: 'email and code are required' });
    }

    const record = await pool.query(
      `SELECT * FROM email_verification_codes
       WHERE email = $1 AND purpose = 'login' AND used_at IS NULL AND expires_at > NOW()
       ORDER BY created_at DESC LIMIT 1`,
      [email]
    );
    if (!record.rows.length) {
      return res.status(400).json({ error: 'invalid or expired code' });
    }

    const storedHash = record.rows[0].code_hash;
    const inputHash = crypto.createHash('sha256').update(code).digest('hex');
    if (storedHash !== inputHash) {
      return res.status(400).json({ error: 'invalid code' });
    }

    await pool.query(
      `UPDATE email_verification_codes SET used_at = NOW() WHERE id = $1`,
      [record.rows[0].id]
    );

    const userResult = await pool.query(
      `SELECT id, casdoor_sub, username, full_name, email FROM users WHERE email = $1`,
      [email]
    );
    if (!userResult.rows.length) {
      return res.status(400).json({ error: '该邮箱未注册，请先注册' });
    }

    const user = userResult.rows[0];
    const token = signJwt({ sub: user.casdoor_sub, name: user.full_name || user.username, email: user.email });

    res.json({ token, user: { id: user.id, username: user.username, email: user.email } });
  } catch (err) {
    console.error('[EmailAuth] verify-login error:', err);
    res.status(500).json({ error: 'internal error' });
  }
});

router.post('/register', async (req, res) => {
  try {
    const { email, code, password, username } = req.body;
    if (!email || !code || !password || !username) {
      return res.status(400).json({ error: 'email, code, password, username are all required' });
    }
    const usernameRegex = /^[a-zA-Z0-9_]{3,30}$/;
    if (!usernameRegex.test(username)) {
      return res.status(400).json({ error: 'username must be 3-30 characters, letters/digits/underscore only' });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: 'password must be at least 6 characters' });
    }

    const record = await pool.query(
      `SELECT * FROM email_verification_codes
       WHERE email = $1 AND purpose = 'register' AND used_at IS NULL AND expires_at > NOW()
       ORDER BY created_at DESC LIMIT 1`,
      [email]
    );
    if (!record.rows.length) {
      return res.status(400).json({ error: 'invalid or expired code' });
    }

    const storedHash = record.rows[0].code_hash;
    const inputHash = crypto.createHash('sha256').update(code).digest('hex');
    if (storedHash !== inputHash) {
      return res.status(400).json({ error: 'invalid code' });
    }

    const existing = await pool.query(
      `SELECT id FROM users WHERE email = $1 OR username = $2`,
      [email, username]
    );
    if (existing.rows.length > 0) {
      return res.status(400).json({ error: '该邮箱或用户名已被注册' });
    }

    await pool.query(
      `UPDATE email_verification_codes SET used_at = NOW() WHERE id = $1`,
      [record.rows[0].id]
    );

    const casdoorPayload = {
      name: username,
      password: password,
      email: email,
      owner: 'built-in',
      organization: 'built-in',
      display_name: username,
    };

    const casdoorRes = await fetch(`${CASDOOR_URL}/api/add-user`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(casdoorPayload),
    });

    if (!casdoorRes.ok) {
      const errText = await casdoorRes.text();
      console.error('[EmailAuth] Casdoor add-user error:', errText);
      return res.status(500).json({ error: '注册失败，请稍后重试' });
    }

    const casdoorSub = `email_${Buffer.from(email).toString('hex').slice(0, 16)}`;

    const userResult = await pool.query(
      `INSERT INTO users (casdoor_sub, username, full_name, email)
       VALUES ($1, $2, $3, $4)
       RETURNING id, casdoor_sub, username, full_name, email`,
      [casdoorSub, username, username, email]
    );
    const user = userResult.rows[0];
    const token = signJwt({ sub: user.casdoor_sub, name: user.full_name, email: user.email });

    res.json({ token, user: { id: user.id, username: user.username, email: user.email } });
  } catch (err) {
    console.error('[EmailAuth] register error:', err);
    res.status(500).json({ error: 'internal error' });
  }
});

module.exports = router;
