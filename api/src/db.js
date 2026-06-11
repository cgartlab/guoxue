const { Pool } = require('pg');

const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT || '5432'),
  database: process.env.DB_NAME || 'guoxue',
  user: process.env.DB_USER || 'guoxue',
  password: process.env.DB_PASSWORD,
});

pool.on('connect', () => console.log('[DB] ✅ Connected to PostgreSQL'));
pool.on('error', (err) => console.error('[DB] ❌', err.message));

module.exports = pool;
