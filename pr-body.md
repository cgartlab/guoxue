## 相关 Issue
Closes #31

## 变更概览
实现了全站导航栏统一化改造，采用分层导航架构。

### 改动的 6 个文件

| 文件 | 说明 |
|------|------|
| `about.html` | 导航与首页完全统一（品牌+抽屉+主菜单+菜单+关于，引用navbar.js） |
| `assets/css/ds-design-system.css` | 新增 ds-navbar--global / ds-toolbar / ds-toolbar__right 样式，响应式适配 |
| `lessons/01-lunyu/index.html` | 分层导航：全局导航层 + 课程工具栏 |
| `lessons/01-lunyu-mixed/index.html` | 同上 |
| `lessons/02-sanzijing/index.html` | 同上 |
| `lessons/02-xueer/index.html` | 同上 |

### 架构说明

**全局导航层（所有页面一致）：** 品牌 Logo + 首页/课程/门类 + 关于本站

**功能层（仅课件页）：** 返回目录 + 讲义/测验/答疑标签 + 翻页控制 + 全屏按钮

### 验收
- [x] 所有页面顶部全局导航视觉一致
- [x] 课件页有独立的功能工具栏
- [x] 移动端导航紧凑排列，按钮可触控
- [x] 返回逻辑统一为 "返回目录"
- [x] 响应式布局适配（320px-1920px）
- [x] 全局导航 z-index 100，工具栏 z-index 99，层次清晰
