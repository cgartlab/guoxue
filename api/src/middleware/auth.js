const jwt = require('jsonwebtoken');

const JWT_SECRET = process.env.CASDOOR_JWT_SECRET;
if (!JWT_SECRET) {
  console.error('[Auth] ❌ CASDOOR_JWT_SECRET not set');
  process.exit(1);
}

function verifyToken(req, res, next) {
  const auth = req.headers.authorization;
  if (!auth || !auth.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Missing Bearer token' });
  }

  const token = auth.slice(7);
  jwt.verify(token, JWT_SECRET, { algorithms: ['HS256'] }, (err, decoded) => {
    if (err) {
      console.warn('[Auth] Invalid JWT:', err.message);
      return res.status(401).json({ error: 'Invalid or expired token' });
    }
    req.user = decoded; // { sub, name, email, ... }
    next();
  });
}

module.exports = { verifyToken };
