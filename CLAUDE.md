# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workspace Overview

**guoxue** (国学课堂) — 面向小学生的中华传统文化在线课件站。纯静态 HTML/CSS/JS，零构建，部署于 **GitHub Pages**；46 门课已统一为第一课扁平样式。

- 线上域名：`https://guoxue.8023laozhanshi.cc`（DNS: CNAME → `cgartlab.github.io`，灰云直连）
- 后端（Casdoor + Express API）独立部署，当前域名下不可用（详见 AGENTS.md）
- 未来架构：`feature/astro-unocss-refactor` 分支仅含设计稿（`docs/refactor-astro-unocss.md`），未实施

---

## Dev Commands

```bash
npm install                    # 安装 Playwright
npx playwright test            # e2e 测试（仅有效命令，NOT npm test）
python3 -m http.server 8000    # 本地预览
node scripts/cache-bust.js     # 给资源加 ?v=<hash>（CI 自动执行）
```

### Deployment
Push to `main` → GitHub Actions 自动部署（`.github/workflows/deploy.yml`）：
cache-bust → upload artifact → GitHub Pages。

```bash
git add . && git commit -m "feat: ..." && git push
```

---

## 课程样式规范（第一课标准）

> 全部 46 门课已统一（PR #101），后续新增/修改必须遵守。

- **模板**：`lessons/_template.html`；**标杆**：`lessons/01-lunyu` / `08-junzi-bu-zhong`
- **封面**：`.slide.cover-slide` = `cover-ornament`×2 + `h2.ds-display` + `cover-subtitle` + `cover-desc` + `cover-seal`
- **讲义/答疑**：`ds-badge` + `h2`；正文 `p/ul/ol` + `ds-highlight`（字词）/ `ds-quote`（金句）/ `ds-caption`（短提示）
- **测验**：`window.GUOXUE_QUIZ_OVERRIDE` 引擎渲染到 `id="quiz-0…9"` 空容器 + 测验说明页 + `quiz-score`；禁止内联
- **编号**：`data-page="0,1,2…"` 连续；`data-section="lecture|quiz|review"`
- **tabs 无 emoji**：讲义 / 测验 / 答疑解惑
- **❌ 禁止**：`slide-card`、`original-text`、`tip-box`、`translation-box`、`data-index`、手写 `?v=`、内联 `font-size`/`line-height`

---

## Architecture

### Design System
- **Single source of truth**: `assets/css/ds-design-system.css` — OKLCH 色彩、8px 网格、暗色模式、打印样式
- **颜色**：ink-green theme（`--ds-accent: oklch(52% 0.08 115)`）
- **间距**：`--ds-space-1` ~ `--ds-space-20`
- **字体**：`Noto Serif SC` / `Noto Sans SC`
- **响应式断点**：1100px / 768px / 480px / 374px

### Slide Engine
- `assets/js/slide-engine.js`：讲义/测验/答疑导航、键盘/触屏/全屏、进度条、localStorage
- 自动探测 `data-section`；自定义测验 `window.GUOXUE_QUIZ_OVERRIDE`；自定义课程 ID `window.GUOXUE_COURSE_ID`

### 首页
- `assets/js/homepage.js`：侧栏抽屉、门类折叠、搜索过滤、课程卡片渲染
- `assets/js/lessons-manifest.js`：46 门课目录数据
- `assets/data/categories.js`：12 门类数据

### 认证（当前不可用）
- `assets/js/auth.js` / `auth-email.js`：Casdoor OAuth2 / 邮箱验证码
- `assets/js/api-client.js`：自建 API（`window.SUPABASE` 兼容接口）
- `api/`：Express + JWT + Postgres（独立部署）

---

## Key Files

| 文件 | 用途 |
|---|---|
| `assets/css/ds-design-system.css` | 设计系统 — 全局样式改动在这里 |
| `assets/js/slide-engine.js` | 课程引擎 — 除非加核心功能否则勿改 |
| `assets/js/lessons-manifest.js` | 课程目录 — 加课改这里 |
| `lessons/_template.html` | 空白课程模板 — 复制新建 |
| `index.html` | 首页 |
| `AGENTS.md` | 完整项目规范（样式标准、部署、后端状态） |

---

## 46 门课概览

- **蒙学**（`mengxue`）：论语·学而 15 门 + 论语·为政 17 门 + 论语·八佾 12 门 + 三字经 1 门 + 混合版 1 门
- 课程编号 `01-lunyu` ~ `44-ji-ru-zai` + `01-lunyu-mixed`

---

## 关键约定

- 课程 HTML：`lessons/XX-name/index.html`，相对路径 `../../assets/…`
- favicon：`assets/img/favicon.svg` — 缺少会 404
- `?v=` 由 CI 的 `cache-bust.js` 自动添加，源码不要手写
- 分支：`dev-xxx` / `feature/xxx` / `fix/xxx`；Conventional Commits；PR 合入 `main`
