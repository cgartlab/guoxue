# 📜 国学课堂

[![Argus-Flash Review](https://github.com/cgartlab/guoxue/actions/workflows/argus-review.yml/badge.svg)](https://github.com/cgartlab/guoxue/actions/workflows/argus-review.yml)

> 面向小学生的中华传统文化在线课件站 · GitHub Pages 部署

本仓库是「国学课堂」互动课件网站,适用于小学语文/国学课程,采用纯静态 HTML+CSS+JS(无构建步骤、无框架),通过 GitHub Pages 即可上线。

\---

## ✨ 当前内容

* 🏠 **首页**(index.html)— 课程目录、教师信息
* 📖 **《论语》国学问答**(01-lunyu)— 完整 26 页课件:讲义 10 页 + 测验 10 道 + 答疑 4 页
* 📚 **《论语》问答课件 · 混合版**(01-lunyu-mixed)— 同主题拓展版,内容更详尽
* 👩‍🏫 **关于本站**(about.html)— 教师寄语、教学理念
* 🎓 **空白课程模板**(`lessons/\_template.html`)— 复制即可新建一门课

\---

## 📁 目录结构

```
guoxue/
├── index.html                       ← 首页
├── about.html                       ← 关于页
├── README.md                        ← 本文件
├── .nojekyll                        ← GitHub Pages 配置(必须)
├── assets/                          ← 共享资源
│   ├── css/
│   │   └── ds-design-system.css    ← 全站设计系统(OKLCH 配色)
│   └── js/
│       ├── lessons-manifest.js      ← 课程目录清单(添加新课要改这里)
│       └── slide-engine.js          ← 课件引擎(切页/答题/全屏/触屏)
└── lessons/                         ← 所有课程放这里
    ├── \_template.html               ← 空白课程模板
    ├── 01-lunyu/
    │   └── index.html               ← 《论语》课
    └── 01-lunyu-mixed/
        └── index.html               ← 《论语》混合版
```

\---

## 🚀 三步法:添加一门新课

> 假设你想加一门《弟子规》课程,编号 02。

### 步骤 1 · 复制模板

打开 `lessons/` 文件夹,把 `\_template.html` 复制为 `02-dizigui/index.html`。

```
lessons/
├── \_template.html         (不动)
├── 01-lunyu/index.html    (已有)
└── 02-dizigui/index.html  (新)
```

### 步骤 2 · 编辑新课程内容

用任意文本编辑器(记事本、VS Code、Sublime 都行)打开 `lessons/02-dizigui/index.html`:

|找什么|改成什么|
|-|-|
|`<title>新课程标题 · 国学课堂</title>`|改为《弟子规》全篇精讲|
|封面页 `.cover-slide` 块|改标题、副标题、简介、印章文字|
|讲义区 `<div class="slide" data-page="1" ...>`|复制/删除/调整讲义幻灯片|
|`window.GUOXUE\_QUIZ\_OVERRIDE = \[ ... ]`|替换为本课的题目(格式见下)|
|答疑区 `<div class="slide" data-page="8" ...>`|填写本课答疑内容|

**题目格式**(在 `window.GUOXUE\_QUIZ\_OVERRIDE` 数组里):

```javascript
{
  q: '题目文本(支持中文标点)',
  opts: \['A 选项', 'B 选项', 'C 选项'],
  ans: 0,   // 0=A, 1=B, 2=C
  exp: '答案解析,会显示在选项下方'
}
```

### 步骤 3 · 注册到课程目录

打开 `assets/js/lessons-manifest.js`,在 `GUOXUE\_LESSONS` 数组中追加:

```javascript
{
    id: '02-dizigui',
    title: '《弟子规》全篇精讲',
    subtitle: '童蒙养正 · 循序致善',
    path: 'lessons/02-dizigui/index.html',
    icon: '🌱',
    grade: '小学低年级',
    description: '从"首孝悌"到"泛爱众",在朗朗书声中养成好习惯。',
    status: 'ready'   // 'ready' 已上线; 'coming' 即将上线(显示为灰色)
}
```

保存,刷新首页 — 新课程卡就出现了。

\---

## 🖥️ 本地预览(不上线也能看效果)

### 方式 A · Python(推荐,系统自带)

在项目根目录打开终端,运行:

```bash
python -m http.server 8000
```

然后浏览器打开 `http://localhost:8000/` 即可。

### 方式 B · VS Code Live Server 插件

1. 安装 [VS Code](https://code.visualstudio.com/) + `Live Server` 扩展
2. 右键 `index.html` → `Open with Live Server`

### 方式 C · 直接双击 `index.html`

> ⚠️ 部分浏览器对 `file://` 协议下的 JS 有限制,推荐用方式 A 或 B。

\---

## 🌐 部署到 GitHub Pages

### 一次性设置(5 分钟)

1. **注册 GitHub 账号**(若没有):[https://github.com](https://github.com)
2. **新建仓库**:

   * 名称填 `guoxue`(或你喜欢的名字,后面 URL 会用到)
   * 类型选 `Public`
   * **不要**勾选 "Add a README file"(我们已有 README)
3. **推送代码**:

```bash
   cd D:\\2-Area\\github-repos\\guoxue
   git init
   git add .
   git commit -m "feat: 初始化国学课堂网站"
   git branch -M main
   git remote add origin https://github.com/你的用户名/guoxue.git
   git push -u origin main
   ```

4. **开启 Pages**:

   * 进入仓库 → `Settings` → 左侧 `Pages`
   * `Source` 选 `Deploy from a branch`
   * `Branch` 选 `main` / `(root)`
   * 点 `Save`
5. **等 1-2 分钟**,访问 `https://你的用户名.github.io/guoxue/` 即可

### 以后更新内容

```bash
git add .
git commit -m "feat: 新增《弟子规》课程"
git push
```

推送后,GitHub Pages 会在 1-2 分钟内自动重新部署。

\---

## ❓ 常见问题

### Q1: 首页打开后图片不显示?

A: 课件中部分图片来自外链 CDN(redocn、sohucs、kzbwg),偶尔可能失效。
解决方案:把这些图片下载到 `assets/img/` 文件夹,在 HTML 里改用相对路径。

### Q2: 修改 `manifest.js` 后首页没变化?

A: 浏览器会缓存 JS 文件,试试 `Ctrl + F5` 强制刷新。
也可以打开 DevTools(F12)→ Network 勾选 `Disable cache`。

### Q3: 想改全站配色?

A: 编辑 `assets/css/ds-design-system.css` 顶部的 `:root` 变量。

* `--ds-accent`:主色(默认墨绿)
* `--ds-color-bg`:背景色
* 改完所有页面同步生效。

### Q4: 想增加题目数量?

A: 在 `lessons/XX-xxx/index.html` 里:

1. 复制 `<div class="slide" data-page="N" data-section="quiz" id="quiz-X"></div>` 块,递增编号
2. 在 `window.GUOXUE\_QUIZ\_OVERRIDE` 数组里追加新题

### Q5: 移动端能用吗?

A: ✅ 完全支持。设计系统已内置 `@media (max-width: 768px)` 响应式规则。
课程页支持触屏滑动翻页,首页布局自动单列。

### Q6: 想打印讲义发给学生?

A: 浏览器按 `Ctrl + P`,选择"仅当前页 / 另存为 PDF"。
当前样式已优化 A4 打印效果。

\---

## 🛠 设计系统说明

本项目使用 **CGArtLab Design System**:

* **配色**:OKLCH 色彩空间,墨绿主调(色相 115),护眼、适合长时间阅读
* **字体**:中文优先 Noto Serif SC / Noto Sans SC,系统衬线/无衬线字体兜底
* **间距**:8px 基准的 4/8/12/16/20/24/32/40/48/64 阶梯
* **圆角**:4/8/12/16 px 四档
* **动效**:150-500ms 渐变,尊重 `prefers-reduced-motion` 设置

如需自定义,主要改 `:root` 变量即可,无需修改具体组件样式。

\---

## 🤝 给老师的几点建议

1. **从模板开始,不要从零写** — `\_template.html` 已包含所有必要结构
2. **先讲义后测验** — 测验题目要忠实于讲义内容
3. **配图用 `.slide-image--portrait` 包裹** — 自动浮在文字右侧
4. **金句用 `.ds-quote` 包裹** — 视觉突出,学生容易记住
5. **每节课 5-10 分钟** — 小学生注意力有限,别塞太多

\---

## 📜 许可

课件内容(经史子集原文与讲解)为公共文化遗产,可自由使用。
代码部分采用 MIT 协议,欢迎改编、二次创作。

\---

> 💌 如有问题,可在仓库的 `Issues` 页面提问,或联系 \[你的邮箱]

