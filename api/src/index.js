require('dotenv').config();
const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const pool = require('./db');
const { verifyToken } = require('./middleware/auth');

const app = express();
app.set('trust proxy', 1);
const PORT = process.env.PORT || 3000;

// ─── 中间件 ───────────────────────────────────────────────
app.use(cors({ origin: process.env.CORS_ORIGIN || '*' }));
app.use(express.json({ limit: '100kb' }));
app.use(rateLimit({ windowMs: 15 * 60 * 1000, max: 200 }));

// ─── 公开路由 ─────────────────────────────────────────────
app.get('/api/health', (_req, res) => res.json({ ok: true, time: new Date().toISOString() }));

// ─── 微信 OAuth 路由（公开，不需要 JWT）───────────────────
const wechatRouter = require('./routes/wechat');
app.use('/api/auth/wechat', wechatRouter);

// ─── 邮箱登录注册路由（公开，不需要 JWT）─────────────────
const emailAuthRouter = require('./routes/email-auth');
app.use('/api/auth/email', emailAuthRouter);

// ─── 数据库初始化 ─────────────────────────────────────────
async function initDb() {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS wechat_users (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        openid TEXT UNIQUE NOT NULL,
        unionid TEXT,
        nickname TEXT,
        avatar_url TEXT,
        created_at TIMESTAMPTZ DEFAULT NOW(),
        updated_at TIMESTAMPTZ DEFAULT NOW()
      );
    `);
    await pool.query(`
      CREATE TABLE IF NOT EXISTS oauth_states (
        state TEXT PRIMARY KEY,
        redirect_back TEXT NOT NULL DEFAULT '/',
        created_at TIMESTAMPTZ DEFAULT NOW()
      );
    `);
    await pool.query(`
      CREATE INDEX IF NOT EXISTS idx_wechat_users_openid ON wechat_users(openid);
    `);
    await pool.query(`
      CREATE INDEX IF NOT EXISTS idx_oauth_states_created ON oauth_states(created_at);
    `);
    console.log('[DB] Tables initialized');
  } catch (err) {
    console.error('[DB] Init error:', err.message);
  }
}

// ─── 受保护路由 ──────────────────────────────────────────
// 所有 /api/* 路由都需要验证 JWT
app.use('/api', verifyToken);

// 用户同步（登录后自动调）
app.post('/api/users/sync', async (req, res, next) => {
  try {
    const { sub: casdoorSub, name, email } = req.user;
    const { rows } = await pool.query(
      `INSERT INTO users (casdoor_sub, username, full_name, email)
       VALUES ($1, $2, $3, $4)
       ON CONFLICT (casdoor_sub)
       DO UPDATE SET username = COALESCE($2, users.username),
                     full_name = COALESCE($3, users.full_name),
                     email = COALESCE($4, users.email),
                     updated_at = NOW()
       RETURNING id, casdoor_sub, username, full_name, email, avatar_url, user_type, created_at`,
      [casdoorSub, name || casdoorSub, name, email]
    );
    res.json(rows[0]);
  } catch (err) { next(err); }
});

// 获取当前用户信息
app.get('/api/users/me', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT id, casdoor_sub, username, full_name, email, avatar_url, user_type, created_at FROM users WHERE casdoor_sub = $1',
      [req.user.sub]
    );
    if (!rows.length) return res.status(404).json({ error: 'User not found. Call POST /api/users/sync first.' });
    res.json(rows[0]);
  } catch (err) { next(err); }
});

// ── 学习进度 ──
app.get('/api/progress', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT p.* FROM study_progress p JOIN users u ON u.id = p.user_id WHERE u.casdoor_sub = $1 ORDER BY p.updated_at DESC',
      [req.user.sub]
    );
    res.json(rows);
  } catch (err) { next(err); }
});

app.get('/api/progress/:courseId', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT p.* FROM study_progress p JOIN users u ON u.id = p.user_id WHERE u.casdoor_sub = $1 AND p.course_id = $2',
      [req.user.sub, req.params.courseId]
    );
    res.json(rows[0] || null);
  } catch (err) { next(err); }
});

app.post('/api/progress', async (req, res, next) => {
  try {
    const { courseId, currentPage, totalPages, quizAnswered, quizScore, completed } = req.body;
    const { rows } = await pool.query(
      `INSERT INTO study_progress (user_id, course_id, current_page, total_pages, quiz_answered, quiz_score, completed)
       VALUES ((SELECT id FROM users WHERE casdoor_sub = $1), $2, $3, $4, $5, $6, $7)
       ON CONFLICT (user_id, course_id)
       DO UPDATE SET current_page = $3, total_pages = $4, quiz_answered = $5, quiz_score = $6, completed = $7, updated_at = NOW()
       RETURNING *`,
      [req.user.sub, courseId, currentPage || 0, totalPages || 0, JSON.stringify(quizAnswered || {}), quizScore || 0, completed || false]
    );
    res.json(rows[0]);
  } catch (err) { next(err); }
});

// ── 笔记 ──
app.get('/api/notes', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT n.* FROM study_notes n JOIN users u ON u.id = n.user_id WHERE u.casdoor_sub = $1 ORDER BY n.is_pinned DESC, n.created_at DESC',
      [req.user.sub]
    );
    res.json(rows);
  } catch (err) { next(err); }
});

app.post('/api/notes', async (req, res, next) => {
  try {
    const { courseId, page, title, content, colorTag } = req.body;
    const { rows } = await pool.query(
      `INSERT INTO study_notes (user_id, course_id, page, title, content, color_tag)
       VALUES ((SELECT id FROM users WHERE casdoor_sub = $1), $2, $3, $4, $5, $6)
       RETURNING *`,
      [req.user.sub, courseId, page, title || '', content || '', colorTag || 'yellow']
    );
    res.json(rows[0]);
  } catch (err) { next(err); }
});

app.delete('/api/notes/:id', async (req, res, next) => {
  try {
    const { rowCount } = await pool.query(
      'DELETE FROM study_notes WHERE id = $1 AND user_id = (SELECT id FROM users WHERE casdoor_sub = $2)',
      [req.params.id, req.user.sub]
    );
    if (!rowCount) return res.status(404).json({ error: 'Not found' });
    res.json({ ok: true });
  } catch (err) { next(err); }
});

// ── 书签 ──
app.get('/api/bookmarks', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT b.* FROM bookmarks b JOIN users u ON u.id = b.user_id WHERE u.casdoor_sub = $1 ORDER BY b.created_at DESC',
      [req.user.sub]
    );
    res.json(rows);
  } catch (err) { next(err); }
});

app.post('/api/bookmarks', async (req, res, next) => {
  try {
    const { courseId, page, note } = req.body;
    const { rows } = await pool.query(
      `INSERT INTO bookmarks (user_id, course_id, page, note)
       VALUES ((SELECT id FROM users WHERE casdoor_sub = $1), $2, $3, $4)
       ON CONFLICT (user_id, course_id, page) DO UPDATE SET note = $4
       RETURNING *`,
      [req.user.sub, courseId, page, note || '']
    );
    res.json(rows[0]);
  } catch (err) { next(err); }
});

app.delete('/api/bookmarks/:id', async (req, res, next) => {
  try {
    const { rowCount } = await pool.query(
      'DELETE FROM bookmarks WHERE id = $1 AND user_id = (SELECT id FROM users WHERE casdoor_sub = $2)',
      [req.params.id, req.user.sub]
    );
    if (!rowCount) return res.status(404).json({ error: 'Not found' });
    res.json({ ok: true });
  } catch (err) { next(err); }
});

// ── 测验成绩 ──
app.get('/api/quiz-scores', async (req, res, next) => {
  try {
    const { rows } = await pool.query(
      'SELECT q.* FROM quiz_scores q JOIN users u ON u.id = q.user_id WHERE u.casdoor_sub = $1 ORDER BY q.completed_at DESC',
      [req.user.sub]
    );
    res.json(rows);
  } catch (err) { next(err); }
});

app.post('/api/quiz-scores', async (req, res, next) => {
  try {
    const { courseId, score, correctCount, totalQuestions, answers } = req.body;
    const { rows } = await pool.query(
      `INSERT INTO quiz_scores (user_id, course_id, score, correct_count, total_questions, answers)
       VALUES ((SELECT id FROM users WHERE casdoor_sub = $1), $2, $3, $4, $5, $6)
       RETURNING *`,
      [req.user.sub, courseId, score, correctCount || 0, totalQuestions || 0, JSON.stringify(answers || [])]
    );
    res.json(rows[0]);
  } catch (err) { next(err); }
});

// ─── 错误处理 ─────────────────────────────────────────────
app.use((err, _req, res, _next) => {
  console.error('[API] Error:', err.message);
  res.status(500).json({ error: 'Internal server error', detail: process.env.NODE_ENV === 'development' ? err.message : undefined });
});

// ─── 启动 ─────────────────────────────────────────────────
app.listen(PORT, async () => {
  await initDb();
  console.log(`🚀 Guoxue API running on port ${PORT}`);
  console.log(`   CORS origin: ${process.env.CORS_ORIGIN || '*'}`);
});