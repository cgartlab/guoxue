# 国学课堂 · 技术架构规范

> **目标**：用最低的维护成本，实现稳定、可扩展的在线教育平台。  
> 本文档是全体开发者（包括 AI 协作者）的唯一技术权威来源。

---

## 1. 架构全景

```
┌──────────────────────────────────────────────────────────────┐
│                   浏览器 (Browser)                           │
│  ┌──────────────┐  ┌───────────────┐  ┌──────────────────┐  │
│  │  静态 HTML   │  │  JS 模块      │  │  CSS 设计系统    │  │
│  │  (GitHub     │  │  (7 个文件)   │  │  (ds-design-     │  │
│  │   Pages)     │  │               │  │   system.css)    │  │
│  └──────┬───────┘  └───────┬───────┘  └──────────────────┘  │
└─────────┼──────────────────┼──────────────────────────────────┘
          │                  │
          │  JWT Bearer      │  REST API
          ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│              guoxue.8023laozhanshi.cc  (后端)               │
│  /api/auth/email/*   — 邮件验证码登录/注册                  │
│  /api/users/me       — 获取当前用户                        │
│  /api/progress/*     — 学习进度                            │
│  /api/notes/*        — 学习笔记                            │
│  /api/bookmarks/*    — 书签                                │
│  /api/quiz-scores/*  — 测验成绩                            │
└─────────────────────────────────────────────────────────────┘
```

### 关键设计决策

| 决策 | 选择 | 原因 |
|------|------|------|
| 前端框架 | 无框架（原生 HTML/JS） | 零构建成本，任何人可直接编辑，GitHub Pages 直接部署 |
| 认证方式 | 邮件验证码 + JWT | 无需第三方账号，自主可控，适合目标用户群 |
| 数据后端 | 自建 REST API | 脱离 Supabase 限制，全数据在自己服务器 |
| CSS 方案 | 单文件设计系统（`ds-` 前缀） | 全局一致，无 CSS-in-JS 复杂度 |
| 部署 | GitHub Pages + 自定义域名 | 免费、稳定、CDN 加速 |

---

## 2. 项目文件结构

```
guoxue/
│
├── index.html              # 首页：课程目录、分类筛选
├── about.html              # 关于本站
├── callback.html           # OAuth/Token 回调处理页
├── dashboard.html          # 学生个人面板（需登录）
├── notes.html              # 笔记和书签（需登录）
├── 404.html                # 自定义 404 页
│
├── lessons/                  # 47 门课程，目录名 NN-slug（编号 01–47）
│   ├── _template.html      # ⭐ 新课程从这里复制
│   ├── 01-lunyu/index.html
│   ├── 03-sanzijing/index.html
│   ├── 47-wang-sun-jia-wen/index.html
│   └── ...（每门课一个目录）
│
├── assets/
│   ├── css/
│   │   └── ds-design-system.css   # 唯一全局样式表
│   ├── js/
│   │   ├── auth.js                # 认证状态管理、UI 更新
│   │   ├── auth-email.js          # 邮件登录弹窗 UI + API 调用
│   │   ├── api-client.js          # 后端 API 客户端（window.SUPABASE）
│   │   ├── homepage.js            # 首页：门类侧栏、课程卡片、移动端序号条
│   │   ├── lessons-manifest.js    # 课程列表数据（window.GUOXUE_LESSONS）
│   │   ├── navbar.js              # 顶栏导航（移动端抽屉）
│   │   └── slide-engine.js        # 课程幻灯片引擎
│   ├── data/
│   │   └── categories.js          # 门类数据（window.GUOXUE_CATEGORIES，5 大门类）
│   └── img/
│       └── favicon.svg
│
├── scripts/
│   └── cache-bust.js       # 资源 URL 版本号注入
│
├── supabase/               # 数据库 schema / RLS / 测试页
├── tests/                  # Playwright 端到端测试
│
├── .github/workflows/
│   ├── deploy.yml          # 自动部署到 GitHub Pages
│   └── argus-review.yml    # PR 自动审查
│
└── ARCHITECTURE.md         # 本文档
```

---

### 2.1 课程数据模型（`lessons-manifest.js`）

`window.GUOXUE_LESSONS` 数组,当前共 **47 项**,与 `lessons/` 下 47 个目录一一对应。

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 唯一标识,等于目录名(如 `01-lunyu`) |
| `num` | string | 两位课程序号 `01`–`47`,显示在卡片左上角 |
| `title` | string | 课程标题 |
| `subtitle` | string | 副标题 |
| `path` | string | 课程入口 HTML 相对路径 |
| `grade` | string | 适用年级 |
| `description` | string | 课程简介 |
| `status` | string | `ready` 已上线 / `coming` 即将上线 |
| `subject` | string | 所属门类 key,取自 `GUOXUE_CATEGORIES` |
| `tier` | string | `core` / `advanced` / `supplement` |
| `featured` | boolean | 是否标记为精选 |

> 部分课程另带可选的 `duration`(预计学习时长)字段。**已无 `icon` 字段**——课程一律以两位序号 `num` 呈现。

### 2.2 门类数据模型（`categories.js`）

`window.GUOXUE_CATEGORIES` 数组,当前共 **5 个门类,全部 `ready`**:

| key | label | num | 课程数 |
|-----|-------|-----|:---:|
| `daolun` | 导论 | `01` | 2 |
| `xueer` | 学而 | `02` | 14 |
| `weizheng` | 为政 | `03` | 17 |
| `bayi` | 八佾 | `04` | 13 |
| `mengxue` | 蒙学 | `05` | 1 |

字段:`key` / `label` / `num` / `description` / `status` / `order`(无 `icon` 字段;门类同样以序号呈现)。

### 2.3 课程模板与 slide-engine 版式

所有课程页统一为 slide-engine 版式(`lessons/_template.html` 为基准):

- 每张幻灯片:`<div class="slide" data-page="N" data-section="...">`,`data-page` 从 `0` 起连续编号
- `data-section` 取值:`lecture` | `quiz` | `review`
- 测验容器:`id="quiz-0"`、`id="quiz-1"` …(引擎依据 `window.GUOXUE_QUIZ_OVERRIDE` 自动渲染)
- 得分页:`id="quiz-score"`,内含 `correct-count` / `total-score` / `score-percent` / `retake-btn`
- 自定义课号:`window.GUOXUE_COURSE_ID`(用于 localStorage 进度键)
- 引擎文件:`assets/js/slide-engine.js`(切页 / 答题评分 / 全屏 / 键盘 / 触屏 / 进度持久化)

> 已废弃的旧结构(`data-index`、手写 `checkAnswer`、`.slide-card`)及其 CSS 均已移除。

### 2.4 首页响应式结构

`index.html` + `homepage.js` 构成首页的两栏布局,并针对移动端切换形态:

- **桌面端(≥768px)**:左侧 `aside.home-sidebar` 目录**默认展开**,按门类分组,组内列出课程「序号 标题」;右侧 `main.home-content` 为课程卡片网格与筛选栏。
- **移动端(<768px)**:隐藏左侧目录,顶部显示可横向滑动的 `.home-numstrip`,**按门类分组**(门类名 `.home-numstrip__label` + 组内课程序号 chip `.home-numstrip__chip`)。
- 首页**已移除**旧的抽屉开关 `#drawer-toggle` 与遮罩;`navbar.js` 的抽屉仅服务于其他带侧栏的页面。

---

## 3. JS 模块职责与依赖关系

### 依赖图

```
auth-email.js  ──────────────────────┐
      │ (定义 window.showLoginModal)  │
      ▼                               │
auth.js ──── (调用 showLoginModal) ──┘
      │ (定义 window.AUTH)
      ▼
api-client.js  (定义 window.SUPABASE, 依赖 localStorage 中的 token)
      │
      ▼
slide-engine.js / homepage.js / navbar.js
(各自独立，按需调用 AUTH.isLoggedIn() / window.SUPABASE)
```

### 加载顺序规范（所有页面必须遵守）

```html
<!-- 1. 数据（无依赖） -->
<script src="/assets/data/categories.js"></script>
<script src="/assets/js/lessons-manifest.js"></script>

<!-- 2. 认证（auth-email 必须在 auth 之前，因为 auth.js 依赖 showLoginModal） -->
<script src="/assets/js/auth-email.js" defer></script>
<script src="/assets/js/auth.js" defer></script>

<!-- 3. API 客户端（依赖 auth.js 中的 token） -->
<script src="/assets/js/api-client.js" defer></script>

<!-- 4. 页面功能（依赖以上所有） -->
<script src="/assets/js/navbar.js" defer></script>
<script src="/assets/js/homepage.js" defer></script>   <!-- 仅首页 -->
<script src="/assets/js/slide-engine.js" defer></script> <!-- 仅课程页 -->
```

> ⚠️ **注意**：`defer` 脚本按 DOM 顺序执行，不要用 `async`（会破坏依赖顺序）。

---

## 4. 认证系统

### 登录流程（邮件验证码）

```
用户点击「登录/注册」
      │
      ▼
auth.js: login()
  → 调用 window.showLoginModal()（由 auth-email.js 提供）
      │
      ▼
用户填写邮箱 → 点击「发送验证码」
  → POST /api/auth/email/send-code
      │
      ▼
用户填写 6 位验证码 → 点击「登录」
  → POST /api/auth/email/verify-login
  → 返回 { token, username }
      │
      ▼
auth-email.js: setAuthToken(token, username)
  → localStorage.casdoor_access_token = token
  → localStorage.casdoor_expires_at = token.exp × 1000  (或 +24h 兜底)
  → localStorage.guoxue_username = username
      │
      ▼
页面跳转回来源地址
      │
      ▼
auth.js: init() → updateAuthUI()
  → isLoggedIn() 返回 true → 显示用户名下拉菜单
```

### localStorage key 规范

| Key | 用途 | 设置方 | 清除方 |
|-----|------|--------|--------|
| `casdoor_access_token` | JWT Bearer Token | `auth-email.js` / `callback.html` | `auth.js logout()` |
| `casdoor_id_token` | ID Token（OIDC） | `auth.js handleCallback()` / `callback.html` | `auth.js logout()` |
| `casdoor_expires_at` | Token 过期时间戳（ms） | `auth-email.js` / `auth.js` | `auth.js logout()` |
| `casdoor_refresh_token` | Refresh Token | `auth.js handleCallback()` | `auth.js logout()` |
| `guoxue_token` | 等同 access_token（冗余） | `auth-email.js` | `auth.js logout()` |
| `guoxue_username` | 用户名（快速显示用） | `auth-email.js` / `callback.html` | `auth.js logout()` |
| `guoxue_email` | 邮箱 | `auth-email.js` | `auth.js logout()` |
| `casdoor_redirect_back` | 登录成功后跳转的 URL | `auth.js login()` | 跳转后立即删除 |

### ⚠️ 关键约束（勿违反）

1. **`casdoor_expires_at` 必须始终设置**  
   不论通过何种方式登录，都必须设置该值（最差兜底 `Date.now() + 86400000`）。  
   `isLoggedIn()` 和 `getAccessToken()` 在 `expiresAt=0` 时会出现严重 bug（详见下方修复记录）。

2. **`isLoggedIn()` 语义**  
   `expiresAt === 0` → 视为有效（无过期信息）  
   `expiresAt > 0 && Date.now() > expiresAt` → 已过期，清除 token  
   其他 → 有效

3. **`logout()` 会清除所有 token**  
   包括 `guoxue_token`、`guoxue_username`、`guoxue_email`，不只是 `casdoor_*`。

---

## 5. CSS 设计系统规范

### 命名规范（BEM-like，统一 `ds-` 前缀）

```css
/* 组件：ds-[component] */
.ds-navbar { }
.ds-btn-nav { }
.ds-lesson-card { }

/* 状态修饰符 */
.ds-btn-nav--brand { }     /* -- 双横线表示变体 */
.ds-lesson-card.active { } /* 直接 class 合并表示状态 */

/* 布局工具 */
.ds-container { }
.ds-card-grid { }

/* 变量（全部用 CSS 自定义属性） */
--ds-accent       /* 主强调色 */
--ds-color-fg     /* 正文色 */
--ds-space-4      /* 间距单位（4 = 1rem） */
--ds-radius-lg    /* 圆角 */
--ds-shadow-md    /* 阴影 */
```

### 禁止行为

- ❌ 在单个课程 HTML 中写大量内联 `<style>`（小范围覆盖 OK，但不能超过 20 行）
- ❌ 使用 `!important`（除非覆盖第三方组件）
- ❌ 在 `ds-design-system.css` 中写课程特定样式（应写在各课程 HTML 的 `<style>` 里）
- ❌ 重复定义相同选择器（合并到已有规则）

### 响应式断点

```css
/* 桌面优先 */
@media (max-width: 1023px) { /* 平板 */ }
@media (max-width: 767px)  { /* 手机横屏 */ }
@media (max-width: 479px)  { /* 手机竖屏 */ }
@media (max-width: 374px)  { /* 小屏手机 */ }
```

---

## 6. 新增课程 SOP（标准作业程序）

### 5 步添加新课程

```bash
# 步骤 1：复制模板（编号接在现有 47 门之后，即 48）
cp lessons/_template.html lessons/48-new-lesson/index.html

# 步骤 2：编辑内容（在文件中找标注的 【填写XXX】 位置）
# - 修改 <title>
# - 填写讲义幻灯片（data-section="lecture"）
# - 定义测验题目（window.GUOXUE_QUIZ_OVERRIDE）
# - 填写复习内容（data-section="review"）

# 步骤 3：注册到课程目录
# 打开 assets/js/lessons-manifest.js，在 GUOXUE_LESSONS 数组末尾追加：
# { id: '48-new-lesson', num: '48', title: '...', subject: 'xueer', status: 'ready', ... }
# subject 必须是 GUOXUE_CATEGORIES 中已有的 key（daolun/xueer/weizheng/bayi/mengxue）

# 步骤 4：（可选）将新课程 URL 追加到 sitemap.xml；资源版本号由 node scripts/cache-bust.js 统一处理

# 步骤 5：提交并推送到 main 分支
git add lessons/48-new-lesson/ assets/js/lessons-manifest.js
git commit -m "feat(lesson): add 48-new-lesson"
git push origin main
# → GitHub Actions 自动部署
```

---

## 7. API 客户端规范（api-client.js）

`window.SUPABASE` 是对后端 API 的封装，保持接口不变，方便后续迁移。

### 所有方法均返回 Promise，失败返回 null / false / []

```javascript
// 正确用法
const progress = await window.SUPABASE.getProgress('01-lunyu')
// progress: { currentPage, totalPages, quizScore, ... } 或 null

// 错误用法 ❌ — 不要假设 SUPABASE 存在
window.SUPABASE.getProgress(...)  // SUPABASE 可能未加载
```

### 防御性调用模板

```javascript
// 在页面脚本中调用 API 的正确姿势
if (AUTH.isLoggedIn() && window.SUPABASE) {
  const data = await window.SUPABASE.getProgress(courseId)
  if (data) renderProgress(data)
}
```

---

## 8. 已知技术债务

| 债务 | 风险 | 建议处理时间 |
|------|------|-------------|
| `callback.html` 同时处理三种登录流程（邮件/微信/Casdoor PKCE），逻辑混杂 | 低 | 下个迭代 |
| 课程页 `<script>` 标签里的 `v=9e67644` 版本参数需手动更新 | 低 | 接入 cache-bust 脚本自动化 |
| `ds-design-system.css` 超过 1990 行，部分规则仅某页面使用 | 低 | 按需拆分为多文件 |
| 无单元测试覆盖认证流程 | 中 | 添加 Playwright auth 测试 |

---

## 9. 架构演进路线（降低维护成本）

### 现状：零构建静态站（current）

优点：部署简单、任何人可改、无依赖更新问题  
缺点：HTML 页面间重复代码多、无类型检查、CSS 难以管理

### 近期改进（无需框架迁移）

1. **抽取公共 navbar/footer**  
   用 `fetch('/assets/components/navbar.html')` 注入到每个页面  
   统一维护一份导航栏 HTML

2. **自动化 cache-bust**  
   `scripts/cache-bust.js` 已存在，接入 GitHub Actions，推送时自动更新版本参数

3. **Lint 规范**  
   引入 ESLint（`eslint:recommended`）+ Stylelint，在 CI 中运行

### 中期演进（如团队扩大到 3+ 人）

迁移至 **[Astro](https://astro.build)**：

```
为什么是 Astro？
✅ 构建输出纯 HTML → 兼容 GitHub Pages
✅ 组件化解决 HTML 重复（navbar、footer、课程幻灯片）
✅ Markdown/MDX 支持 → 课程内容与代码分离
✅ 按需 JS（Islands Architecture）→ 首页零 JS
✅ TypeScript 支持
✅ 与现有 CSS 设计系统完全兼容（直接沿用 ds-design-system.css）
✅ 迁移成本低（HTML → .astro 文件，语法基本一致）
```

**迁移优先级**：
1. `lessons/_template.html` → Astro 组件（复用最高）
2. `index.html` + `homepage.js` → Astro 页面
3. 认证相关保持不变（Astro 客户端 islands）

---

## 10. 发布流程

```
本地开发
  │  git commit -m "feat/fix/chore: 描述"
  │  git push origin feature-branch
  ▼
Pull Request（目标分支：main）
  │  → GitHub Actions 运行 Playwright 测试
  │  → argus-flash[bot] 自动 review
  ▼
合并到 main
  │
  ▼
GitHub Actions: deploy.yml
  → 构建（目前：复制静态文件）
  → 部署到 GitHub Pages
  → 自动生效（~2 分钟）
```

### Commit 消息规范

```
feat(scope):   新功能
fix(scope):    Bug 修复
chore(scope):  工具/配置
docs(scope):   文档
style(scope):  CSS 样式
refactor(scope): 代码重构
test(scope):   测试
```

---

## 11. 紧急排障指南

### 登录失败

1. 打开浏览器 DevTools → Console
2. 检查 `localStorage.getItem('casdoor_access_token')` 是否为空
3. 检查 `localStorage.getItem('casdoor_expires_at')` 是否合理（大于 `Date.now()`）
4. 查看 Network 标签：`/api/auth/email/verify-login` 是否返回 200
5. 若 API 返回 5xx：检查后端服务是否在线 `https://guoxue.8023laozhanshi.cc/api/health`

### 课程页面空白 / 功能异常

1. 检查 `window.GUOXUE_LESSONS` 是否已定义（`lessons-manifest.js` 是否加载）
2. 检查 `window.AUTH` 是否已定义（`auth.js` 是否加载）
3. 检查 `data-section` 属性是否正确：`lecture` / `quiz` / `review`

### 样式错乱

1. 检查是否有 `!important` 冲突
2. 检查是否有两处相同选择器定义（运行 `grep -n "选择器" assets/css/ds-design-system.css`）

---

*最后更新：2026-09 | 维护者：cgartlab*
