# AGENTS.md

## Quick Start
- `npm install` — install Playwright for testing
- `npx playwright test` — run e2e tests
- `python -m http.server 8000` — local preview

## Testing
- `npx playwright test` (NOT `npm test` — that command is broken)
- Tests: `tests/homepage.spec.js`
- Uses local HTTP server on port 7890 (auto-started by test harness)

## Deployment
- Push to `main` → GitHub Pages auto-deploys via `.github/workflows/deploy.yml`
- CI runs `node scripts/cache-bust.js` before deploy (adds `?v=<git-hash>` to assets)

## Static Asset Updates
- After modifying CSS/JS, run `node scripts/cache-bust.js` to update version params
- Or let CI handle it on push to main

## Architecture Notes
- **Zero-build deploy**: raw HTML/CSS/JS go directly to GitHub Pages
- **npm is for testing only** — not required for site functioning
- Design system: `assets/css/ds-design-system.css`
- Slide engine: `assets/js/slide-engine.js`
- Courses: `assets/js/lessons-manifest.js` + `assets/data/categories.js`
- Navbar: `assets/js/navbar.js` (drawer on desktop, collapsed on mobile)

## Adding a Course
1. `cp lessons/_template.html lessons/XX-name/index.html`
2. Edit content
3. Add entry to `assets/js/lessons-manifest.js`
4. If new subject, add entry to `assets/data/categories.js`

## Note
CLAUDE.md may be stale — it claims "no build system" but the repo now has npm/Playwright for testing.