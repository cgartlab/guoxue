const express = require('express');
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
const pool = require('../db');

const router = express.Router();

const WECHAT_APP_ID = process.env.WECHAT_APP_ID;
const WECHAT_APP_SECRET = process.env.WECHAT_APP_SECRET;
const JWT_SECRET = process.env.CASDOOR_JWT_SECRET;
const CALLBACK_URL = process.env.CALLBACK_URL || 'https://guoxue.8023laozhanshi.cc/callback.html';

if (!WECHAT_APP_ID || !WECHAT_APP_SECRET) {
  throw new Error('WECHAT_APP_ID and WECHAT_APP_SECRET must be set in environment variables');
}

function randomString(len) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~';
  const array = new Uint8Array(len);
  crypto.getRandomValues(array);
  let result = '';
  for (let i = 0; i < len; i++) {
    result += chars[array[i] % chars.length];
  }
  return result;
}

router.get('/login', async (req, res) => {
  try {
    const state = randomString(32);
    const redirectBack = req.query.redirect || '/';
    const stateValue = `${state}:${redirectBack}`;

    await pool.query(
      'INSERT INTO oauth_states (state, redirect_back) VALUES ($1, $2) ON CONFLICT (state) DO UPDATE SET redirect_back = $2',
      [state, redirectBack]
    );

    const wechatAuthUrl = new URL('https://open.weixin.qq.com/connect/oauth2/authorize');
    wechatAuthUrl.searchParams.set('appid', WECHAT_APP_ID);
    wechatAuthUrl.searchParams.set('redirect_uri', `${CALLBACK_URL.replace('/callback.html', '')}/api/auth/wechat/callback`);
    wechatAuthUrl.searchParams.set('response_type', 'code');
    wechatAuthUrl.searchParams.set('scope', 'snsapi_base');
    wechatAuthUrl.searchParams.set('state', state);

    res.redirect(wechatAuthUrl.toString() + '#wechat_redirect');
  } catch (err) {
    console.error('[WeChat] Login error:', err);
    res.status(500).json({ error: 'Failed to initiate WeChat login' });
  }
});

router.get('/callback', async (req, res) => {
  try {
    const { code, state } = req.query;

    if (!code || !state) {
      return res.redirect(`${CALLBACK_URL}?error=no_code_or_state`);
    }

    const stateResult = await pool.query(
      'SELECT redirect_back FROM oauth_states WHERE state = $1',
      [state]
    );

    if (!stateResult.rows.length) {
      return res.redirect(`${CALLBACK_URL}?error=invalid_state`);
    }

    const redirectBack = stateResult.rows[0].redirect_back;
    await pool.query('DELETE FROM oauth_states WHERE state = $1', [state]);

    const tokenUrl = new URL('https://api.weixin.qq.com/sns/oauth2/access_token');
    tokenUrl.searchParams.set('appid', WECHAT_APP_ID);
    tokenUrl.searchParams.set('secret', WECHAT_APP_SECRET);
    tokenUrl.searchParams.set('code', code);
    tokenUrl.searchParams.set('grant_type', 'authorization_code');

    const tokenResponse = await fetch(tokenUrl.toString());
    const tokenData = await tokenResponse.json();

    if (tokenData.errcode) {
      console.error('[WeChat] Token exchange error:', tokenData);
      return res.redirect(`${CALLBACK_URL}?error=wechat_token_failed&msg=${tokenData.errmsg}`);
    }

    const { openid, unionid } = tokenData;

    let userResult = await pool.query(
      'SELECT id, casdoor_sub, username, full_name, email FROM users WHERE casdoor_sub = $1',
      [`wechat_${openid}`]
    );

    if (!userResult.rows.length) {
      userResult = await pool.query(
        `INSERT INTO users (casdoor_sub, username, full_name, email)
         VALUES ($1, $2, $3, $4)
         RETURNING id, casdoor_sub, username, full_name, email`,
        [`wechat_${openid}`, `wechat_${openid}`, `微信用户_${openid.slice(-8)}`, `wechat_${openid}@wechat.guoxue`]
      );
    }

    const user = userResult.rows[0];

    await pool.query(
      `INSERT INTO wechat_users (user_id, openid, unionid)
       VALUES ($1, $2, $3)
       ON CONFLICT (openid) DO UPDATE SET unionid = COALESCE($3, wechat_users.unionid), updated_at = NOW()`,
      [user.id, openid, unionid || null]
    );

    const payload = {
      sub: user.casdoor_sub,
      name: user.full_name || user.username,
      email: user.email || '',
    };

    const token = jwt.sign(payload, JWT_SECRET, { expiresIn: '7d' });

    res.redirect(`${CALLBACK_URL}?token=${token}&redirect=${encodeURIComponent(redirectBack)}`);
  } catch (err) {
    console.error('[WeChat] Callback error:', err);
    res.redirect(`${CALLBACK_URL}?error=callback_failed`);
  }
});

module.exports = router;