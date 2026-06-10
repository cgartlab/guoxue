# 导航栏 EDIC 设计系统对齐 + 统一菜单 + 对齐修复

## 变更概要
基于 EDIC Design System 重构全局导航栏，统一所有页面菜单风格，修复内容对齐问题，添加暗色模式支持。

## 涉及文件
- `assets/css/ds-design-system.css` — 添加暗色模式令牌、EDIC 导航栏类、暗色导航栏样式
- `assets/js/navbar-component.js` — 改用 EDIC 类名结构、统一菜单、简化逻辑
- `assets/js/homepage.js` — 适配新的类名

## 具体变更

### 1. 统一导航栏菜单
- 所有页面（首页/about/课件页）使用同一菜单：**品牌 + 关于本站**
- 课件页不再有"首页"、"课程"、"门类"等快捷入口，统一遵循首页风格
- 当前页自动高亮（关于本站 → `ds-navbar-link--active` 高亮，首页无多余链接）

### 2. EDIC 类名体系
- `ds-navbar-inner` → 内层容器（max-width: 1200px），对齐页面内容
- `ds-navbar-brand` → 品牌链接（国学课堂），衬线字体 + 加粗
- `ds-navbar-links` → 菜单列表
- `ds-navbar-link` / `ds-navbar-link--active` → 菜单项

### 3. 对齐修复
- `ds-navbar-inner max-width: 1200px` → 与 `home-wrapper` 一致
- 导航栏品牌文字与左侧边栏 / 主要内容区域左对齐

### 4. 暗色模式
- 添加完整的 `[data-theme="dark"]` 色板（EDIC 规范）
- 暗色下使用暖灰 `oklch(15% 0.008 75)` 代替纯黑
- 导航栏适配暗色背景 + 半透明模糊效果
- 跟随系统 `@media (prefers-color-scheme: dark)` 自动切换

## 预览
- PR #51 fix/homepage-ui
- 本地预览: http://192.168.31.131:3000 (无缓存模式)
- 线上预览前确认 PR 合并
