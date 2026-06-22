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

## 课程样式规范（必须遵守）

### 参考标准
- **唯一正确模板**：`lessons/_template.html` — 所有课件必须基于此模板创建
- **Pattern A 参考**：`lessons/09-wen-liang-gong-jian-rang/index.html` — 已修复的最新课件，直接参考其结构

### ✅ 必须使用的设计系统类

| 元素 | 正确类名 |
|------|---------|
| 封面容器 | `cover-slide` |
| 封面标题装饰线 | `cover-ornament`（成对使用） |
| 封面标题 | `h2`（不需要 class，继承 `.slide h2`） |
| 封面副标题 | `cover-subtitle` |
| 封面简介 | `cover-desc` |
| 封面印章 | `cover-seal` |
| 结束页 | `end-slide` |
| 结束页引言 | `end-quote` |
| 讲义/答疑页签 | `ds-badge ds-badge--accent` |
| 测验页签 | `ds-badge ds-badge--success` |
| 原文引用块 | `ds-quote` |
| 注释/提示框 | `ds-caption`（CSS 自动加 💡 前缀） |
| 网格布局 | `summary-grid` + `summary-card` |
| 卡片标题 | `card-label` |
| 卡片内容 | `card-value` |
| 导航栏分隔 | `<span class="flex-spacer">`（不用 `style="flex:1"`） |

### ❌ 严禁使用的模式

以下类名在 CSS 中**不存在**，使用会导致样式丢失：

| 错误类名 | 说明 |
|---------|------|
| `slide-card`、`slide-card--cover`、`slide-card__body` | 无 CSS，请用 `cover-slide` 或扁平 `.slide` |
| `sentence-block`、`quote-block`、`original-text`、`translation-box` | 无 CSS，请用 `ds-quote` |
| `tip-box`、`contrast-box` | 无 CSS，请用 `ds-caption` |
| `people-grid`、`core-grid`、`app-grid` | 无 CSS，请用 `summary-grid` |
| `lesson-title`、`lesson-subtitle`（课程内） | 首页卡片专用，课程内请用 `cover-subtitle` |
| `faq-item` | 无 CSS，可保留作语义钩子 |

### ❌ 严禁内联测验 HTML

所有课件测验必须使用引擎渲染，**禁止内联**：

```html
<!-- ✅ 正确：空容器，引擎自动填充 -->
<div class="slide" data-page="8" data-section="quiz" id="quiz-0"></div>

<!-- ❌ 错误：内联 HTML，破坏一致性 -->
<div class="quiz-option" onclick="checkAnswer(this)">...</div>
```

### ❌ 严禁源码中硬编码 `?v=` 哈希

`cache-bust.js` 在 CI 部署时自动为所有 HTML 中的 `href/src` 添加哈希，**不要手动添加**：

```html
<!-- ✅ 正确：无哈希，CI 自动添加 -->
<link rel="stylesheet" href="../../assets/css/ds-design-system.css">

<!-- ❌ 错误：手动哈希，部署时被覆盖，造成不一致 -->
<link rel="stylesheet" href="../../assets/css/ds-design-system.css?v=abc123">
```

### ⚙️ 必需的脚本配置

每个课件必须定义以下全局变量，**在 `slide-engine.js` 加载之前**定义：

```html
<script>
window.GUOXUE_COURSE_ID = 'course-slug';   // 必须：用于 localStorage 进度隔离
window.GUOXUE_QUIZ_OVERRIDE = [             // 必须：自定义测验题目
    { q: '题目', opts: ['A','B','C','D'], ans: 0, exp: '解析' },
    // ... 共10题
];
</script>
<script src="../../assets/js/slide-engine.js"></script>   <!-- 无 defer，同步加载 -->
<script src="../../assets/js/auth-email.js" defer></script>
<script src="../../assets/js/auth.js" defer></script>
<script src="../../assets/js/api-client.js" defer></script>
```

### 📐 页面结构规范

```html
<!-- 封面 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture">
    <div class="cover-ornament"></div>
    <h2>标题</h2>
    <div class="cover-ornament"></div>
    <p class="cover-subtitle">副标题</p>
    <p class="cover-desc">简介</p>
    <div class="cover-seal">印章</div>
</div>

<!-- 讲义页 -->
<div class="slide" data-page="1" data-section="lecture">
    <span class="ds-badge ds-badge--accent">讲义</span>
    <h2>标题</h2>
    <div class="ds-quote">引用内容</div>
    <div class="summary-grid">
        <div class="summary-card">
            <div class="card-label">标签</div>
            <div class="card-value">内容</div>
        </div>
    </div>
    <div class="ds-caption">提示说明</div>
</div>

<!-- 结束页 -->
<div class="slide end-slide" data-page="N" data-section="review">
    <div class="cover-ornament"></div>
    <h2>谢谢大家</h2>
    <div class="cover-ornament"></div>
    <div class="end-quote">"引言"</div>
    <div class="cover-seal">印章</div>
</div>
```

### 🔧 常见错误排查

| 症状 | 原因 | 修复 |
|------|------|------|
| 封面看起来不对 | 用了 `slide-card--cover` 而非 `cover-slide` | 改用 `cover-slide` 模式 |
| 引用块无样式 | 用了 `sentence-block` 等自定义类 | 改用 `ds-quote` |
| 网格无样式 | 用了 `core-grid` 等自定义类 | 改用 `summary-grid` |
| 导航栏偏移 | 用了 `style="flex:1"` | 改用 `class="flex-spacer"` |
| 测验点击无反应 | 内联了 `quiz-option` HTML | 改用空 `id="quiz-N"` 容器 |
| 样式与课件不一致 | 偏离了 Pattern A | 对照 `_template.html` 检查结构 |
