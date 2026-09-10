# AGENTS.md

## 项目定位

「国学课堂」——面向小学生的中华传统文化在线课件站。**纯静态 HTML/CSS/JS，零构建**，部署于 **GitHub Pages**；学习记录/登录为可选的自建后端（`api/`），与静态站分离。

- 线上域名：`https://guoxue.8023laozhanshi.cc`（DNS：CNAME → `cgartlab.github.io`，灰云直连 GitHub Pages）
- 课程规模：46 门课（《论语》学而 / 为政 / 八佾 系列 + 三字经/拓展版），样式全部统一为**第一课扁平标准**
- 未来架构：`feature/astro-unocss-refactor` 分支仅含 Astro+UnoCSS 重构设计稿（`docs/refactor-astro-unocss.md`），未实施，与当前线上无关

## Quick Start

- `npm install` — 安装 Playwright（测试用）
- `npx playwright test` — 运行 e2e 测试（**NOT** `npm test`，该脚本是坏的）
- `python3 -m http.server 8000` — 本地预览
- `node scripts/cache-bust.js` — 给所有 HTML 的资源引用加 `?v=<git-hash>`（CI 部署时自动执行，源码勿手写）

## 架构速览

| 模块 | 文件 | 职责 |
|---|---|---|
| 首页渲染 | `assets/js/homepage.js` | 侧栏抽屉导航、门类折叠、搜索过滤、课程卡片、封面统计 |
| 课程目录 | `assets/js/lessons-manifest.js` | `GUOXUE_LESSONS`（46 门课：id/title/path/icon/subject/tier/featured…） |
| 学科门类 | `assets/data/categories.js` | `GUOXUE_CATEGORIES`（12 类：经史子集/蒙学/书法…） |
| 课程引擎 | `assets/js/slide-engine.js` | 讲义/测验/答疑导航、键盘/触屏/全屏、进度条、测验渲染判分、localStorage 进度 |
| 设计系统 | `assets/css/ds-design-system.css` | OKLCH 令牌、8px 网格、暗色模式、打印；`ds-*` 组件 + 课程扁平样式 |
| 登录 | `assets/js/auth.js` / `auth-email.js` | Casdoor OAuth2 PKCE / 邮箱验证码登录 |
| 学习数据 | `assets/js/api-client.js` | 自建 API 客户端（`window.SUPABASE` 兼容接口）：用户/进度/笔记/书签/成绩 |
| 后端 | `api/`（Express+JWT+Postgres） | `/api/*` REST；**独立部署，不上 GitHub Pages** |
| 顶栏 | `assets/js/navbar.js` | 仅 `dashboard.html` / `notes.html` 使用；首页用自带抽屉，课程页用 `ds-toolbar` |

> Supabase（`supabase-client.js` / `auth-supabase-patch.js` / `supabase/` SQL）已废弃，由 `api-client.js` + 自建 API 取代，`assets/js` 中已无相关文件。

## 课程样式规范（第一课标准，必须遵守）

**唯一模板**：`lessons/_template.html`；**样式标杆**：`lessons/01-lunyu`（及同为章节课的扁平范本 `08-junzi-bu-zhong`）。

- **封面**：`.slide.cover-slide` = `cover-ornament` ×2 + `h2.ds-display` 标题 + `cover-subtitle` + `cover-desc` + `cover-seal` 印章
- **讲义/答疑页**：`span.ds-badge.ds-badge--accent`（讲义/答疑解惑）+ `h2` 标题；内容用 `h3`/`p`/`ul`/`ol` + `ds-highlight`（字词/关键）、`ds-quote`（金句）、`ds-caption`（短提示，CSS 自动加 💡）
- 内容语义映射（由卡片式迁移而来，新增内容照此写）：
  - 原文 → 短句用 `ds-quote`；出处/篇章行 → 独立小字段落
  - 通译 → 普通段落 `<p><strong>通译：</strong>…</p>`
  - 字词卡 → `<p><span class="ds-highlight">字（音）</span>：释义</p>`（可多行 `<br>` 合并）
  - 长提示/要点/对比 → 普通段落或 `ul`（保留 `<strong>` 标签，不要色块）
  - FAQ → `<h3>❓ 问题</h3>` + `<p>答案</p>`
- **编号**：所有 slide 用 `data-page="0,1,2…"` 连续编号；`data-section="lecture|quiz|review"`
- **tabs 无 emoji**：讲义 / 测验 / 答疑解惑（第一课标准；课程 09-44 曾带 📖✏️💬，PR #101 已统一）
- **测验**：页内 `<script>window.GUOXUE_QUIZ_OVERRIDE = [...]</script>` 由引擎渲染到空容器 `id="quiz-0…9"`；测验前有"测验说明"页；得分页 `id="quiz-score"`；**禁止内联测验 HTML**
- **结束页**：`.slide.end-slide` = ornament + `ds-display` + `end-quote` + `cover-seal`

**❌ 禁止**（PR #101 已清理，勿复用）：`slide-card` 系列、`original-text`、`translation-box`、`tip-box`、`sentence-block`、`core-grid`、`app-grid`、`data-index`、内联 `font-size/line-height`、手写 `?v=`。

## 添加一门新课

1. `cp lessons/_template.html lessons/XX-name/index.html`
2. 编辑：`<title>` → 封面（title/subtitle/desc/seal）→ 讲义 slides（`data-page` 连续、扁平样式）→ `window.GUOXUE_QUIZ_OVERRIDE`（10 题）→ 测验说明页 → 答疑 slides → 结束页
3. 在 `assets/js/lessons-manifest.js` 追加条目（`subject` 必须匹配 `GUOXUE_CATEGORIES` 已有 key；新门类先加 categories）
4. 本地预览：`python3 -m http.server 8000`；回归：`npx playwright test`
5. 提交并推送 `main` → GitHub Actions 自动部署（cache-bust → GitHub Pages）

## 测试

- 唯一有效命令 `npx playwright test`；`playwright.config.js`：workers=1、CI 重试 2、首次失败开 trace
- `tests/homepage.spec.js`：桌面 1440×900 / 平板 768×1024 / 移动 375×812；测试内起本地服务，端口 **7890**（硬编码）
- 单测：`npx playwright test tests/homepage.spec.js -g "test name"`

## 部署与域名

- Push `main` → `.github/workflows/deploy.yml`：checkout → Node 20 → `node scripts/cache-bust.js` → upload artifact → Pages deploy
- 仓库根 `CNAME` = `guoxue.8023laozhanshi.cc`；DNS 为 CNAME → `cgartlab.github.io`（灰云，勿改回 Cloudflare Tunnel 或本地 nginx）
- `.nojekyll` 必须保留（否则 `_template.html` 无法访问）
- 浏览器缓存：`Ctrl+F5`；资源版本由 CI 的 `?v=` 处理

## 登录/云功能状态（2026-09）

- 域名已切回 GitHub Pages（此前 DNS 曾走 Cloudflare Tunnel 到本地 nginx，已删除该 CNAME）
- **GitHub Pages 无法反代 `/casdoor` 与 `/api`** → 当前登录（Casdoor/邮箱码）、dashboard、notes、进度/成绩云同步**不可用**；课程浏览、测验、本地进度（localStorage）**正常**
- 恢复方案（需要时）：Casdoor/API 部署到独立子域（如 `casdoor.8023laozhanshi.cc` / `api.8023laozhanshi.cc`），并修改前端 3 处硬编码：
  - `assets/js/auth.js`：`CONFIG.serverUrl`
  - `assets/js/auth-email.js`：`API_BASE`
  - `assets/js/api-client.js`：`API_BASE`
  - 另需同步 Casdoor 回调地址与后端 CORS
- 后端代码在 `api/`（Express，:3000），本地 docker/主机 111 上另有 Casdoor（:8000）与数据库

## 代码规范

- 分支：`dev-xxx` / `feature/xxx` / `fix/xxx`；提交用 Conventional Commits；PR 合入 `main`（有 Argus 门禁）
- Casdoor SMTP 配置在 Casdoor 管理后台（`casdoor.8023laozhanshi.cc`），不在仓库内
