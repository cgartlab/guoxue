# AGENTS.md

## Quick Start
- `npm install` — install Playwright for testing
- `npx playwright test` — run e2e tests (NOT `npm test` — that script is broken)
- `python -m http.server 8000` — local preview
- `node scripts/cache-bust.js` — add `?v=<git-hash>` to asset URLs in all HTML files

## Testing
- `npx playwright test` — only valid test command; `npm test` exits with error
- `playwright.config.js`: `workers: 1`, CI retries: 2, trace on first retry
- Test file: `tests/homepage.spec.js` — covers desktop (1440×900), tablet (768×1024), mobile (375×812)
- Test harness auto-starts a local HTTP server on **port 7890** (hardcoded in test file)
- Run a single test: `npx playwright test tests/homepage.spec.js -g "test name"`

## Deployment
- Push to `main` → GitHub Pages auto-deploys via `.github/workflows/deploy.yml`
- CI steps: checkout → setup Node 20 → `node scripts/cache-bust.js` → upload artifact → deploy
- Zero-build deploy: raw HTML/CSS/JS pushed directly; `.nojekyll` required (allows serving `_template.html`)

## Static Asset Versioning
- `scripts/cache-bust.js` appends `?v=<short-git-hash>` to all `href="assets/…"` and `src="assets/…"` references
- Scans: `index.html`, `about.html`, `404.html`, and all `lessons/**/*.html`
- Skip in dev: `NODE_ENV=development node scripts/cache-bust.js`

## Architecture
- **Static site**: raw HTML/CSS/JS, no build step, deployed to GitHub Pages
- **Design system**: `assets/css/ds-design-system.css` — OKLCH colors, 8px grid, dark mode, print styles
- **Slide engine**: `assets/js/slide-engine.js` — lecture/quiz/review navigation, keyboard + touch + swipe, localStorage progress
  - Custom quiz: set `window.GUOXUE_QUIZ_OVERRIDE` before engine loads
  - Custom course ID: set `window.GUOXUE_COURSE_ID` before engine loads
- **Course manifest**: `assets/js/lessons-manifest.js` (`GUOXUE_LESSONS` array) — fields: `id`, `title`, `subtitle`, `path`, `icon`, `grade`, `description`, `status`, `subject`, `tier`, `featured`
- **Categories**: `assets/data/categories.js` (`GUOXUE_CATEGORIES` array) — key, label, icon, description, status, order
- **Navbar**: `assets/js/navbar.js` — drawer on desktop, collapsed on mobile; homepage uses `ds-navbar--simple` (brand + about link only)
- **API server** (separate, not deployed to Pages): `api/` — Express + JWT + Postgres; `api/package.json`

## Supabase + Auth Integration
- Supabase client: `assets/js/supabase-client.js` — user sync, progress save, notes/bookmarks
- Auth patch: `assets/js/auth-supabase-patch.js` — syncs Casdoor login to Supabase users
- Dashboard: `dashboard.html` — study stats, progress, quiz scores
- Notes: `notes.html` — learning notes and bookmarks management
- DB setup: run `supabase/01-schema.sql` then `supabase/02-rls.sql` in Supabase SQL Editor
- Local-only operations always succeed; cloud ops may fail silently (no blocking)

## Adding a Course
1. `cp lessons/_template.html lessons/XX-name/index.html`
2. Edit: `<title>`, cover slide, lecture slides (sequential `data-page="0,1,2..."`), quiz (`window.GUOXUE_QUIZ_OVERRIDE`), review slides
3. Add entry to `assets/js/lessons-manifest.js` (include `subject` key matching a `GUOXUE_CATEGORIES` key)
4. If new subject, add entry to `assets/data/categories.js`
5. For browser cache: `Ctrl+F5` or DevTools → Network → Disable cache

## Casdoor Email (SMTP) Configuration
- Casdoor manages its own SMTP/email config via the admin web UI at `https://casdoor.8023laozhanshi.cc`
- Login with admin credentials (defaults are set during Casdoor deployment)
- **To configure**:
  1. Settings → Providers → Add → Email → SMTP
  2. Fill in SMTP server, port, username, password (QQ授权码), sender info
  3. Applications → `guoxue-classroom` → Set the email provider in `providers` array
  4. Ensure `enableCodeSignin: true` and `signupItems` includes Email with rule `Required`
- The configuration is stored in Casdoor's PostgreSQL database, **not** in `app.conf`
- After changing SMTP settings, test by registering a new user on the website
- For QQ邮箱: server `smtp.qq.com`, port `465` (SSL), use **授权码** not password
- SMTP credentials are NOT stored in this repo (they are secrets managed in Casdoor)

## Key Conventions
- Course HTML files: `lessons/XX-name/index.html`, relative asset paths use `../assets/…`
- Slide `data-section`: `lecture` | `quiz` | `review`
- Quiz containers: `id="quiz-0"`, `id="quiz-1"`, … (engine auto-renders from `GUOXUE_QUIZ_OVERRIDE`)
- Score page: `id="quiz-score"`
- Favicon: `assets/img/favicon.svg` — missing folder will 404 silently
