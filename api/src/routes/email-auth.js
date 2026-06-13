'use strict';

const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const net = require('net');
const dns = require('dns');
const tls = require('tls');
const pool = require('../db');

const router = express.Router();

const SMTP_HOST = process.env.SMTP_HOST;
const SMTP_PORT = parseInt(process.env.SMTP_PORT || '587', 10);
const SMTP_SECURE = process.env.SMTP_SECURE !== 'false';
const SMTP_USER = process.env.SMTP_USER;
const SMTP_PASS = process.env.SMTP_PASS;
const JWT_SECRET = process.env.CASDOOR_JWT_SECRET;
const CASDOOR_URL = process.env.CASDOOR_URL || 'https://casdoor.8023laozhanshi.cc';

if (!SMTP_HOST || !SMTP_USER || !SMTP_PASS) {
  throw new Error('SMTP_HOST, SMTP_USER, and SMTP_PASS environment variables are required');
}
if (!JWT_SECRET) {
  throw new Error('CASDOOR_JWT_SECRET environment variable is required');
}

const EMAIL_HTML_TEMPLATE = `<div style="max-width:560px;margin:24px auto;background:#fff;border-radius:12px;padding:24px 32px;font-family:sans-serif"><h2 style="margin:0;font-size:18px;color:#333">国学课堂</h2><hr style="border:none;border-top:1px solid #eee"><p style="margin:16px 0;font-size:15px;color:#333">您好，</p><p style="margin:0 0 16px;font-size:15px;color:#333">您的邮箱验证码为：</p><div style="text-align:center;margin:24px 0"><span style="display:inline-block;padding:10px 36px;font-size:30px;font-weight:bold;letter-spacing:10px;color:#1677ff;background:#f0f5ff;border-radius:8px">%s</span></div><p style="margin:0;font-size:13px;color:#888">验证码有效期为 <strong>5 分钟</strong>，请勿泄露给他人。</p><hr style="border:none;border-top:1px solid #eee"><p style="margin:16px 0 0;font-size:11px;color:#bbb;text-align:center">此邮件由系统自动发送，请勿回复</p></div>`;

function randomCode() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

function buildSmtpClient() {
  let socket = null;

  function sendCommand(cmd, timeoutMs) {
    return new Promise((resolve, reject) => {
      timeoutMs = timeoutMs === undefined ? 10000 : timeoutMs;
      const timer = setTimeout(() => {
        reject(new Error('SMTP command timeout: ' + cmd.slice(0, 30)));
      }, timeoutMs);
      socket.write(cmd + '\r\n', 'utf8', (err) => {
        if (err) { clearTimeout(timer); reject(err); return; }
        const chunks = [];
        function onData(chunk) {
          chunks.push(chunk.toString());
          const response = chunks.join('');
          const lastLine = response.split('\r\n').filter(l => l).pop();
          const code = lastLine.split(' ')[0];
          if (code === '235' || code === '250' || code === '334' || code === '354' || code === '220' || code === '221') {
            clearTimeout(timer);
            socket.removeListener('data', onData);
            resolve(lastLine);
          } else if (code.startsWith('4') || code.startsWith('5')) {
            clearTimeout(timer);
            socket.removeListener('data', onData);
            reject(new Error('SMTP error: ' + lastLine));
          } else if (code.match(/^\d{3}$/)) {
            clearTimeout(timer);
            socket.removeListener('data', onData);
            reject(new Error('SMTP unexpected response: ' + lastLine));
          }
        }
        socket.on('data', onData);
        socket.once('error', (err) => { clearTimeout(timer); reject(err); });
      });
    });
  }

  return {
    connect() {
      return new Promise((resolve, reject) => {
        if (SMTP_SECURE && SMTP_PORT === 465) {
          socket = tls.connect({
            host: SMTP_HOST,
            port: SMTP_PORT,
            minVersion: 'TLSv1',
            rejectUnauthorized: false,
          }, () => { resolve(); });
          socket.setEncoding('utf8');
          socket.on('error', reject);
          socket.on('close', () => { socket = null; });
          setTimeout(() => reject(new Error('SMTP connect timeout')), 10000);
        } else {
          dns.resolve4(SMTP_HOST, (dnsErr, addrs) => {
            if (dnsErr) { reject(dnsErr); return; }
            socket = new net.Socket();
            socket.setEncoding('utf8');
            let bannerDone = false;
            let bannerTimer;
            function onBanner(chunk) {
              if (bannerDone) return;
              bannerDone = true;
              clearTimeout(bannerTimer);
              socket.removeListener('data', onBanner);
              resolve();
            }
            socket.on('data', onBanner);
            socket.on('error', reject);
            socket.on('close', () => { socket = null; });
            bannerTimer = setTimeout(() => {
              if (!bannerDone) reject(new Error('SMTP banner timeout'));
            }, 10000);
            socket.connect({ host: addrs[0], port: SMTP_PORT });
          });
        }
      });
    },

    sendEmail(to, subject, html) {
      return new Promise(async (resolve, reject) => {
        try {
          const banner = await sendCommand('EHLO localhost', 15000);
          if (SMTP_SECURE && SMTP_PORT === 587 && banner.includes('STARTTLS')) {
            await sendCommand('STARTTLS', 10000);
            const tlsSocket = tls.connect({
              socket: socket,
              host: SMTP_HOST,
              rejectUnauthorized: false,
            });
            socket = tlsSocket;
            socket.setEncoding('utf8');
            await new Promise((res, rej) => {
              tlsSocket.once('secureConnect', res);
              tlsSocket.once('error', rej);
              setTimeout(() => rej(new Error('TLS handshake timeout')), 10000);
            });
            await sendCommand('EHLO localhost', 15000);
          }
          await sendCommand('AUTH LOGIN', 10000);
          await sendCommand(Buffer.from(SMTP_USER).toString('base64'), 10000);
          await sendCommand(Buffer.from(SMTP_PASS).toString('base64'), 10000);
          await sendCommand(`MAIL FROM:<${SMTP_USER}>`, 10000);
          await sendCommand(`RCPT TO:<${to}>`, 10000);
          await sendCommand('DATA', 10000);
          const fromHeader = `From: 国学课堂 <${SMTP_USER}>\r\n`;
          const toHeader = `To: ${to}\r\n`;
          const subjectHeader = `Subject: ${subject}\r\n`;
          const mimeHeaders = `MIME-Version: 1.0\r\nContent-Type: text/html; charset=UTF-8\r\n`;
          const emailContent = fromHeader + toHeader + subjectHeader + mimeHeaders + '\r\n' + html;
          const dotStuffed = emailContent.replace(/\n\./g, '\n..');
          await sendCommand(dotStuffed + '\r\n.', 10000);
          await sendCommand('QUIT', 5000);
          socket.end();
          resolve();
        } catch (err) {
          if (socket && !socket.destroyed) socket.end();
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
    const codeHash = crypto.createHash('sha256').update(code).digest('hex');

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
      return res.status(500).json({ error: '邮件发送失败，请稍后重试' });
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
    const token = signJwt({ sub: user.casdoor_sub, name: user.username || user.full_name, email: user.email });

    res.json({ token, username: user.username || user.full_name });
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

    res.json({ token, username: user.username });
  } catch (err) {
    console.error('[EmailAuth] register error:', err);
    res.status(500).json({ error: 'internal error' });
  }
});

module.exports = router;
