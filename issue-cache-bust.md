## Issue 标题
[Performance] 静态资源缓存失效问题 — 部署后需手动清理缓存

## 问题描述

### 现象
每次合并分支并部署到 GitHub Pages 后，用户在其他设备或浏览器访问网站，看到的仍是旧版本页面。必须手动清理浏览器缓存（强制刷新 `Ctrl+F5` / 清除站点数据）才能看到最新内容。

### 影响范围
- **所有用户**：每次更新后都会遇到
- **移动端用户**：尤其明显（缓存清理路径更深）
- **深度缓存**：Service Worker、CDN 缓存可能导致长时间显示旧内容

### 根本原因
GitHub Pages 默认识应 Cache-Control: max-age=31536000（1年），静态资源（CSS/JS/图片）被浏览器长期缓存。当文件内容更新后，URL 不变，浏览器不会主动重新请求。

## 解决方案

### 方案：Query String 版本化（推荐）

在所有静态资源的 URL 后面添加版本查询参数，格式：
```
https://guoxue.8023laozhanshi.cc/assets/css/ds-design-system.css?v=20250606
```

当文件内容更新时，更新 `v=` 值，浏览器认为是新资源，绕过缓存。

#### 实施步骤

1. **创建构建脚本 `scripts/cache-bust.js`**
   - 读取 HTML 文件
   - 扫描 `<link href="...">` 和 `<script src="...">` 引用
   - 自动更新 `v=` 参数为当前时间戳或 Git commit SHA
   - 输出更新后的 HTML（或直接替换源文件）

2. **修改 `index.html` 等 HTML 文件**
   - 将静态资源 URL 改为带 `v=` 参数的格式：
   ```html
   <link rel="stylesheet" href="assets/css/ds-design-system.css?v=20250606">
   ```

3. **CI/CD 集成（可选）**
   - 在 GitHub Actions 中，每次 push 到 main 分支自动执行版本化脚本

#### 脚本示例逻辑

```javascript
// scripts/cache-bust.js
const fs = require('fs');
const path = require('path');

// 读取 Git commit hash 作为版本号
const version = require('child_process')
  .execSync('git rev-parse --short HEAD')
  .toString().trim();

// 扫描 HTML 文件中的静态资源引用
function updateVersionInHTML(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');
  html = html.replace(/href="(assets\/[^"]+)\?v=[^"]*"/g, 'href="$1?v=' + version + '"');
  html = html.replace(/src="(assets\/[^"]+)\?v=[^"]*"/g, 'src="$1?v=' + version + '"');
  // 处理无 v 参数的引用（首次）
  html = html.replace(/href="(assets\/[^"]+)"/g, 'href="$1?v=' + version + '"');
  html = html.replace(/src="(assets\/[^"]+)"/g, 'src="$1?v=' + version + '"');
  fs.writeFileSync(filePath, html);
  console.log('Updated:', filePath);
}

// 遍历所有 HTML 文件
['index.html', 'about.html', ...].forEach(updateVersionInHTML);
```

#### GitHub Actions 集成

```yaml
# .github/workflows/deploy.yml
- name: Cache bust static assets
  run: node scripts/cache-bust.js
- name: Deploy to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
```

## 受影响文件

| 文件 | 变更 |
|------|------|
| `index.html` | 静态资源 URL 添加 `v=` 参数 |
| `about.html` | 同上 |
| `lessons/*.html` | 同上 |
| `assets/css/*.css` | 无需修改（通过 HTML 的 v 参数控制） |
| `assets/js/*.js` | 无需修改 |
| `scripts/cache-bust.js` | 新建版本化脚本 |
| `.github/workflows/deploy.yml` | 部署时自动执行版本化 |

## 替代方案（备选）

### 方案 B：Service Worker 精确缓存
- 注册 Service Worker 拦截请求
- 使用 `cache.put()` 并设置短缓存期
- 优点：离线可用，精确控制
- 缺点：实现复杂，与 GitHub Pages 部署流程集成困难

### 方案 C：Meta 标签禁止缓存
```html
<meta http-equiv="Cache-control" content="no-cache">
<meta http-equiv="Pragma" content="no-cache">
```
⚠️ 不推荐：CDN 和浏览器常忽略 HTML meta 标签

## 验收标准

- [ ] HTML 文件中的 `<link>` 和 `<script src>` 引用全部带 `v=` 参数
- [ ] 每次部署后，所有设备打开网站自动获取最新版本（无需手动刷新）
- [ ] 本地开发环境不受影响（可选：开发模式下跳过版本化）
- [ ] CI/CD 自动化（可选：GitHub Actions 集成）

## 优先级

P2 - 用户体验问题，不影响核心功能但影响更新感知

## 标签

`performance`, `cache`, `deployment`, `enhancement`