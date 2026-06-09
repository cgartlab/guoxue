# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: homepage.spec.js >> Desktop (1440x900) >> top nav menu shows pure text (no emoji)
- Location: tests/homepage.spec.js:77:3

# Error details

```
Error: expect(locator).toHaveCount(expected) failed

Locator:  locator('.ds-navbar__menu .ds-btn-nav--ghost')
Expected: 3
Received: 0
Timeout:  5000ms

Call log:
  - Expect "toHaveCount" with timeout 5000ms
  - waiting for locator('.ds-navbar__menu .ds-btn-nav--ghost')
    14 × locator resolved to 0 elements
       - unexpected value "0"

```

# Test source

```ts
  1   | // tests/homepage.spec.js
  2   | // Playwright E2E tests for homepage v2.1 (drawer sidebar + series cover + collapsed categories)
  3   | // Run: npx playwright test tests/homepage.spec.js --workers=1
  4   | 
  5   | const { test, expect } = require('@playwright/test');
  6   | const path = require('path');
  7   | const http = require('http');
  8   | const fs = require('fs');
  9   | 
  10  | const PROJECT_ROOT = path.resolve(__dirname, '..');
  11  | const INDEX_PATH = path.join(PROJECT_ROOT, 'index.html');
  12  | const PORT = 7890;
  13  | 
  14  | let server;
  15  | 
  16  | test.beforeAll(() => {
  17  |   const mime = {
  18  |     '.html': 'text/html',
  19  |     '.css': 'text/css',
  20  |     '.js': 'application/javascript',
  21  |     '.svg': 'image/svg+xml',
  22  |     '.png': 'image/png',
  23  |     '.ico': 'image/x-icon'
  24  |   };
  25  |   server = http.createServer((req, res) => {
  26  |     const url = new URL(req.url, `http://localhost:${PORT}`);
  27  |     let filePath = path.join(PROJECT_ROOT, url.pathname);
  28  |     if (url.pathname === '/') filePath = INDEX_PATH;
  29  |     const ext = path.extname(filePath);
  30  |     const contentType = mime[ext] || 'application/octet-stream';
  31  |     fs.readFile(filePath, (err, data) => {
  32  |       if (err) {
  33  |         res.writeHead(404);
  34  |         res.end('Not found');
  35  |       } else {
  36  |         res.writeHead(200, { 'Content-Type': contentType });
  37  |         res.end(data);
  38  |       }
  39  |     });
  40  |   });
  41  |   server.listen(PORT);
  42  | });
  43  | 
  44  | test.afterAll(() => {
  45  |   server && server.close();
  46  | });
  47  | 
  48  | // ===== 桌面端测试 (1440x900) =====
  49  | test.describe('Desktop (1440x900)', () => {
  50  |   test.use({ viewport: { width: 1440, height: 900 } });
  51  | 
  52  |   test('two-column layout with series cover renders', async ({ page }) => {
  53  |     await page.goto(`http://localhost:${PORT}/`);
  54  | 
  55  |     // Sidebar visible (default expanded on desktop)
  56  |     const sidebar = page.locator('.home-sidebar');
  57  |     await expect(sidebar).toBeVisible();
  58  | 
  59  |     // Main content visible
  60  |     const mainContent = page.locator('.home-content');
  61  |     await expect(mainContent).toBeVisible();
  62  | 
  63  |     // No right aside (removed)
  64  |     const aside = page.locator('.home-aside');
  65  |     await expect(aside).toHaveCount(0);
  66  | 
  67  |     // Series cover visible
  68  |     const seriesCover = page.locator('.series-cover');
  69  |     await expect(seriesCover).toBeVisible();
  70  |     await expect(seriesCover.locator('.series-cover__title')).toContainText('系列课程总览');
  71  | 
  72  |     // Stats visible
  73  |     const stats = page.locator('.series-stat__value');
  74  |     await expect(stats).toHaveCount(3); // 已上线 / 筹备中 / 门类
  75  |   });
  76  | 
  77  |   test('top nav menu shows pure text (no emoji)', async ({ page }) => {
  78  |     await page.goto(`http://localhost:${PORT}/`);
  79  | 
  80  |     // 主菜单项(首页/课程/门类)
  81  |     const menuLinks = page.locator('.ds-navbar__menu .ds-btn-nav--ghost');
> 82  |     await expect(menuLinks).toHaveCount(3);
      |                             ^ Error: expect(locator).toHaveCount(expected) failed
  83  | 
  84  |     // 品牌链接
  85  |     const brand = page.locator('.ds-btn-nav--brand');
  86  |     await expect(brand).toHaveText('国学课堂');
  87  | 
  88  |     // 菜单切换按钮(桌面端可见,文字"菜单")
  89  |     const menuToggle = page.locator('#menu-toggle .ds-btn-nav__text');
  90  |     await expect(menuToggle).toHaveText('菜单');
  91  | 
  92  |     // 抽屉切换按钮(桌面端可见,文字"目录")
  93  |     const drawerToggle = page.locator('#drawer-toggle .ds-btn-nav__text');
  94  |     await expect(drawerToggle).toHaveText('目录');
  95  |   });
  96  | 
  97  |   test('sidebar renders 12 collapsible categories (default collapsed)', async ({ page }) => {
  98  |     await page.goto(`http://localhost:${PORT}/`);
  99  | 
  100 |     const groups = page.locator('.home-sidebar__group');
  101 |     await expect(groups).toHaveCount(12);
  102 | 
  103 |     // Category headers visible
  104 |     const headers = page.locator('.home-sidebar__category-header');
  105 |     await expect(headers).toHaveCount(12);
  106 | 
  107 |     // Sub navs should be hidden by default
  108 |     const subNavs = page.locator('.home-sidebar__nav:not(.home-sidebar__nav--all)');
  109 |     for (let i = 0; i < await subNavs.count(); i++) {
  110 |       const nav = subNavs.nth(i);
  111 |       const isHidden = await nav.evaluate(el => el.hasAttribute('hidden'));
  112 |       expect(isHidden).toBe(true);
  113 |     }
  114 | 
  115 |     // "全部课程" reset link visible
  116 |     const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
  117 |     await expect(allLink).toBeVisible();
  118 |     await expect(allLink).toContainText('全部课程');
  119 |   });
  120 | 
  121 |   test('search box renders with L2 styling', async ({ page }) => {
  122 |     await page.goto(`http://localhost:${PORT}/`);
  123 | 
  124 |     const searchInput = page.locator('#sidebar-search');
  125 |     await expect(searchInput).toBeVisible();
  126 |     await expect(searchInput).toHaveAttribute('placeholder', '搜索课程…');
  127 |   });
  128 | 
  129 |   test('lesson cards render correctly', async ({ page }) => {
  130 |     await page.goto(`http://localhost:${PORT}/`);
  131 | 
  132 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  133 |     await expect(cards).toHaveCount(6);
  134 | 
  135 |     const firstCard = cards.first();
  136 |     await expect(firstCard.locator('.lesson-title')).toContainText('论语');
  137 |   });
  138 | 
  139 |   test('series cover stats show correct counts', async ({ page }) => {
  140 |     await page.goto(`http://localhost:${PORT}/`);
  141 | 
  142 |     const values = page.locator('.series-stat__value');
  143 |     const vals = await values.allTextContents();
  144 |     // 6 ready lessons, 0 coming lessons, 12 categories
  145 |     expect(vals[0]).toBe('6'); // 已上线
  146 |     expect(vals[1]).toBe('0'); // 筹备中
  147 |     expect(vals[2]).toBe('12'); // 门类
  148 |   });
  149 | });
  150 | 
  151 | // ===== 平板测试 (768x1024) =====
  152 | test.describe('Tablet (768x1024)', () => {
  153 |   test.use({ viewport: { width: 768, height: 1024 } });
  154 | 
  155 |   test('sidebar visible, cards in 2 columns', async ({ page }) => {
  156 |     await page.goto(`http://localhost:${PORT}/`);
  157 | 
  158 |     const sidebar = page.locator('.home-sidebar');
  159 |     await expect(sidebar).toBeVisible();
  160 | 
  161 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  162 |     await expect(cards).toHaveCount(6);
  163 |   });
  164 | });
  165 | 
  166 | // ===== 移动端测试 (375x812) =====
  167 | test.describe('Mobile (375x812)', () => {
  168 |   test.use({ viewport: { width: 375, height: 812 } });
  169 | 
  170 |   test('top nav collapses to text menu button', async ({ page }) => {
  171 |     await page.goto(`http://localhost:${PORT}/`);
  172 | 
  173 |     const toggle = page.locator('#menu-toggle');
  174 |     await expect(toggle).toBeVisible();
  175 |     // 移动端只显示图标(无文字)
  176 |     const menuToggleText = page.locator('#menu-toggle .ds-btn-nav__text');
  177 |     const isVisible = await menuToggleText.isVisible();
  178 |     expect(isVisible).toBe(false);
  179 | 
  180 |     const menu = page.locator('#primary-menu');
  181 |     const hasOpenClass = await menu.evaluate(el => el.classList.contains('is-open'));
  182 |     expect(hasOpenClass).toBe(false);
```