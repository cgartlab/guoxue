# LESSONS — guoxue

> 「国学课堂」小学生传统文化在线课件站（纯静态 HTML/CSS/JS，零构建，GitHub Pages 部署，69 门课，第一课扁平样式标准，Playwright e2e）。
> 本仓库从真实失误沉淀的「教训→规则」清单。**会话开始先全文阅读并遵循其中所有规则**；出现新失误按 §维护 追加。
> 权威依据：Anthropic Claude Code memory/best practices（<200 行、具体可验证、第二次犯同样错即写入）；社区 lessons.md 惯例（Boris Cherny，Anthropic）。
> 来源：本仓库 AGENTS.md 的课程样式规范 / 部署与域名 / 登录状态 + 已验证 fix 提交；预填为种子，后续由 Agent 在真实工作中增长。

## 维护
- **触发**：用户纠正 / Agent 自查到的失误 / 非显而易见的 gotcha。
- **格式**：`### <主题>` 下，每条 = 失误（具体场景）→ 规则（最小可执行指令），一行可验证。
- **只记项目特有、不可从代码推断的**；通用最佳实践不写；含糊措辞（"小心""注意"）删掉。
- **重复出现** → 升级进 `AGENTS.md` 硬规则；**月度审阅**裁剪过期项；目标 < 200 行。

## 课程样式（第一课标准）

### 从模板开始
- 失误：从零写课程 HTML，样式不统一 → 规则：唯一模板 `lessons/_template.html`，新课程 `cp lessons/_template.html lessons/XX-name/index.html`（见 AGENTS.md「课程样式规范」）

### 禁止已清理的旧样式
- 失误：复用 `slide-card`、`original-text`、`translation-box`、`tip-box`、`sentence-block`、`core-grid` 等旧 class → 规则：这些已由 PR #101 清理，勿复用（见 AGENTS.md「禁止」）

### tabs 无 emoji
- 失误：讲义/测验/答疑解惑 tabs 带 📖✏️💬 emoji → 规则：课程 09-44 曾带 emoji，PR #101 已统一为无 emoji，新增课程照第一课标准（见 AGENTS.md「课程样式规范」）

### 内联测验 HTML 禁止
- 失误：测验写成内联 HTML → 规则：测验用页内 `window.GUOXUE_QUIZ_OVERRIDE` 由引擎渲染到空容器 `id="quiz-0…9"`，禁止内联测验 HTML（见 AGENTS.md「课程样式规范」）

### data-page 连续编号
- 失误：slide 的 `data-page` 跳号或不连续 → 规则：所有 slide 用 `data-page="0,1,2…"` 连续编号，`data-section="lecture|quiz|review"`（见 AGENTS.md「课程样式规范」）

### 手写 ?v= 禁止
- 失误：源码手写 `?v=` 资源版本 → 规则：CI 部署时自动执行 `cache-bust.js` 注入，源码勿手写（见 AGENTS.md「禁止」）（commit 199be4d 修复正则贪婪导致的版本号叠加）

### manifest subject 必须匹配 categories
- 失误：新课程 `subject` 填了 `GUOXUE_CATEGORIES` 中不存在的 key，首页分类无此课程 → 规则：`subject` 必须匹配已有 key，新门类先加 categories（见 AGENTS.md「添加一门新课」）（commit a3c7e16 曾把 33-44 从 lunyu 重分配到 mengxue）

## 测试与构建

### 唯一有效命令 npx playwright test
- 失误：运行 `npm test`（该脚本是坏的） → 规则：唯一有效命令 `npx playwright test`，`npm test` 是坏的勿用（见 AGENTS.md「Quick Start」）

### 测试端口 7890 硬编码
- 失误：测试前先手动起本地服务 → 规则：测试会自动在 7890 端口起本地 HTTP 服务，无需另开预览服务（见 README「端到端测试」）

## 部署与域名

### CNAME 灰云直连
- 失误：把 DNS 改回 Cloudflare Tunnel 或本地 nginx → 规则：`guoxue.8023laozhanshi.cc` 的 DNS 是 CNAME → `cgartlab.github.io`（灰云直连），勿改回（见 AGENTS.md「部署与域名」）（commit e9113f4 修正 .org → .cc）

### .nojekyll 必须保留
- 失误：删除 `.nojekyll`，`_template.html` 无法访问 → 规则：`.nojekyll` 必须保留（见 AGENTS.md「部署与域名」）

### GitHub Pages 无法反代 /casdoor 与 /api
- 失误：误以为登录功能可用，或试图在 GitHub Pages 反代后端 → 规则：登录（Casdoor/邮箱码）、dashboard、notes、进度云同步当前不可用；恢复需部署独立子域并改前端 3 处硬编码（`auth.js` CONFIG.serverUrl、`auth-email.js` API_BASE、`api-client.js` API_BASE）（见 AGENTS.md「登录/云功能状态」）

## 测验与逻辑

### 正确答案固定第二位
- 失误：答案固定在第 2 个选项，学生可猜测 → 规则：每题渲染时随机打乱选项顺序（commit ab4230e）

### 免费课误判为付费
- 失误：`01/02/03/05` 等免费课缺 COURSE_ID 被误判为付费课 → 规则：免费课也必须补齐 COURSE_ID（commit bb4f05d）

## 相对路径与导航

### 非课程页面相对路径
- 失误：非课程页面的相对路径、标签切换与课程映射错误 → 规则：修复后注意页面间相对路径与导航一致性（commit aab5cac）

### 外部图片失效
- 失误：课件引用外链 CDN 图片（redocn/sohucs/kzbwg）偶尔失效 → 规则：下载到 `assets/img/` 用相对路径（见 README「常见问题 Q1」）

## 无障碍

### ruby lang 属性
- 失误：ruby 注音未加 `lang` 属性 → 规则：ruby 注解加 `lang="zh-Hans"`（commit eeada8f）

### token 覆盖 + skip links
- 失误：token 覆盖不完整、缺少 skip links → 规则：完整 token 覆盖 + skip links（commit b52b6d6）
