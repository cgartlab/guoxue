# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace Overview

This is the **guoxue** (国学课堂) repository — a static HTML/CSS/JS website for Chinese traditional culture courses targeting elementary school students. Deployed to GitHub Pages.

---

## Dev Commands

No build system. Pure static files.

```bash
cd guoxue
# Preview locally with any static server:
python -m http.server 8000
# Or use VS Code Live Server extension
```

### Deployment
Push to `main` branch → GitHub Pages auto-deploys.

```bash
git add . && git commit -m "feat: ..." && git push
```

---

## Architecture

### Design System
- **Single source of truth**: `assets/css/ds-design-system.css` — all shared styles, tokens, and responsive rules live here
- **Color**: OKLCH color space, ink-green theme (`--ds-accent: oklch(52% 0.08 115)`)
- **Spacing**: 8px baseline grid (`--ds-space-1` through `--ds-space-20`)
- **Typography**: `Noto Serif SC` / `Noto Sans SC` for Chinese
- **Dark mode**: `@media (prefers-color-scheme: dark)` overrides in `:root`
- **Responsive breakpoints**: 1023px / 767px / 479px / 374px

### Slide Engine
- **File**: `assets/js/slide-engine.js` — shared course engine (no build step)
- **Features**: slide navigation, quiz rendering & scoring, section switching (lecture/quiz/review), keyboard/touch/swipe support, fullscreen, localStorage progress persistence
- **Auto-detects** `data-section` on slides — no hard-coded section boundaries
- **Custom quiz**: define `window.GUOXUE_QUIZ_OVERRIDE` in the HTML before importing `slide-engine.js`
- **Custom course ID**: define `window.GUOXUE_COURSE_ID` before importing for per-course localStorage keys

### Course Manifest
- **File**: `assets/js/lessons-manifest.js` — `GUOXUE_LESSONS` array (47 entries, `01`–`47`)
- Adding a new course: 1) copy `lessons/_template.html`, 2) edit content, 3) add entry to manifest, 4) refresh index.html
- Fields: `id`, `num` (two-digit display index `01`–`47`), `title`, `subtitle`, `path`, `grade`, `description`, `status` (`ready`/`coming`), `subject`, `tier` (`core`/`advanced`/`supplement`), `featured` (no `icon` field — courses show `num` instead)

### Categories
- **File**: `assets/data/categories.js` — `GUOXUE_CATEGORIES` array, 5 subjects (all `ready`): `daolun` 导论, `xueer` 学而, `weizheng` 为政, `bayi` 八佾, `mengxue` 蒙学
- Fields: `key`, `label`, `num`, `description`, `status`, `order`; a course's `subject` must match one of these `key`s

### Lesson Template
- **File**: `lessons/_template.html` — copy this to create new courses
- Structure: cover slide → lecture slides → quiz slides (auto-rendered) → review slides → end slide
- Key conventions:
  - Every slide has `data-page="N"` (continuous from 0)
  - Section via `data-section="lecture|quiz|review"`
  - Quiz containers must have `id="quiz-0"`, `id="quiz-1"`, etc.
  - Score page must have `id="quiz-score"` (with `correct-count` / `total-score` / `score-percent` / `retake-btn`)

### Page Structure
- `index.html` — course catalog (two-column layout on desktop: category sidebar + main content; on mobile the sidebar is replaced by a top horizontal `.home-numstrip` grouped by category, no drawer)
- `about.html` — about page with teaching philosophy and teacher intro
- `lessons/` — 47 self-contained slide decks

---

## Adding a New Course (3-Step Method)

1. **Copy template**: `cp lessons/_template.html lessons/XX-name/index.html` (next free number, currently `48`)
2. **Edit content**: title, slides, quiz questions (`window.GUOXUE_QUIZ_OVERRIDE`), review content
3. **Register**: add entry to `assets/js/lessons-manifest.js` with `num` and a `subject` matching a `GUOXUE_CATEGORIES` key, then refresh `index.html`

---

## Key Files to Know

| File | Purpose |
|------|---------|
| `assets/css/ds-design-system.css` | Design system — edit here for global style changes |
| `assets/js/slide-engine.js` | Slide engine — do NOT modify unless adding core features |
| `assets/js/lessons-manifest.js` | Course catalog — add new courses here |
| `lessons/_template.html` | Blank course template — copy for new lessons |
| `index.html` | Homepage — course directory |
| `about.html` | About page |

---

## Responsive & Accessibility

- Mobile-first with progressive enhancement
- Touch swipe navigation on course pages
- WCAG 2.5.5 touch targets (44px minimum on mobile)
- `prefers-reduced-motion` respected — animations disabled
- `prefers-color-scheme: dark` — full dark mode support
- Print-optimized styles for A4 handouts

---

## Cross-Repo Note

This repo (`guoxue/`) is one of three projects under `D:/2-Area/github-repos/`. The other two are:
- `cgartlab.github.io/` — Astro 6 static site (separate build system)
- `cgartlab-obsidian/` — Obsidian vault (not a software project)

When working on this repo, stay within `guoxue/` directory. Do not run `pnpm install` or other build commands here — this is a zero-build static site.
