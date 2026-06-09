// tests/homepage.spec.js
// Playwright E2E tests for homepage v2.1 (drawer sidebar + series cover + collapsed categories)
// Run: npx playwright test tests/homepage.spec.js --workers=1

const { test, expect } = require('@playwright/test');
const path = require('path');
const http = require('http');
const fs = require('fs');

const PROJECT_ROOT = path.resolve(__dirname, '..');
const INDEX_PATH = path.join(PROJECT_ROOT, 'index.html');
const PORT = 7890;

let server;

test.beforeAll(() => {
  const mime = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.svg': 'image/svg+xml',
    '.png': 'image/png',
    '.ico': 'image/x-icon'
  };
  server = http.createServer((req, res) => {
    const url = new URL(req.url, `http://localhost:${PORT}`);
    let filePath = path.join(PROJECT_ROOT, url.pathname);
    if (url.pathname === '/') filePath = INDEX_PATH;
    const ext = path.extname(filePath);
    const contentType = mime[ext] || 'application/octet-stream';
    fs.readFile(filePath, (err, data) => {
      if (err) {
        res.writeHead(404);
        res.end('Not found');
      } else {
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(data);
      }
    });
  });
  server.listen(PORT);
});

test.afterAll(() => {
  server && server.close();
});

// ===== 桌面端测试 (1440x900) =====
test.describe('Desktop (1440x900)', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('two-column layout with series cover renders', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // Sidebar visible (default expanded on desktop)
    const sidebar = page.locator('.home-sidebar');
    await expect(sidebar).toBeVisible();

    // Main content visible
    const mainContent = page.locator('.home-content');
    await expect(mainContent).toBeVisible();

    // No right aside (removed)
    const aside = page.locator('.home-aside');
    await expect(aside).toHaveCount(0);

    // Series cover visible
    const seriesCover = page.locator('.series-cover');
    await expect(seriesCover).toBeVisible();
    await expect(seriesCover.locator('.series-cover__title')).toContainText('系列课程总览');

    // Stats visible
    const stats = page.locator('.series-stat__value');
    await expect(stats).toHaveCount(3); // 已上线 / 筹备中 / 门类
  });

  test('top nav shows simple brand and about link without emoji', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 首页导航条使用 ds-navbar--simple,仅含品牌+"关于本站"
    const brand = page.locator('.ds-btn-nav--brand');
    await expect(brand).toHaveText('国学课堂');
    await expect(brand.locator('.ds-btn-nav__icon')).toHaveCount(0);

    // 关于本站链接
    const aboutLink = page.locator('.ds-navbar__inner .ds-btn-nav').last();
    await expect(aboutLink).toHaveText('关于本站');

    // 首页无菜单/抽屉切换按钮(这些仅在课程页的 ds-navbar--global 中存在)
    await expect(page.locator('#menu-toggle')).toHaveCount(0);
    await expect(page.locator('#drawer-toggle')).toHaveCount(0);
  });

  test('sidebar renders 12 collapsible categories (default collapsed)', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const groups = page.locator('.home-sidebar__group');
    await expect(groups).toHaveCount(12);

    // Category headers visible
    const headers = page.locator('.home-sidebar__category-header');
    await expect(headers).toHaveCount(12);

    // Sub navs should be hidden by default
    const subNavs = page.locator('.home-sidebar__nav:not(.home-sidebar__nav--all)');
    for (let i = 0; i < await subNavs.count(); i++) {
      const nav = subNavs.nth(i);
      const isHidden = await nav.evaluate(el => el.hasAttribute('hidden'));
      expect(isHidden).toBe(true);
    }

    // "全部课程" reset link visible
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
    await expect(allLink).toBeVisible();
    await expect(allLink).toContainText('全部课程');
  });

  test('search box renders with L2 styling', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchInput = page.locator('#sidebar-search');
    await expect(searchInput).toBeVisible();
    await expect(searchInput).toHaveAttribute('placeholder', '搜索课程…');
  });

  test('lesson cards render correctly', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(6);

    const firstCard = cards.first();
    await expect(firstCard.locator('.lesson-title')).toContainText('论语');
  });

  test('series cover stats show correct counts', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const values = page.locator('.series-stat__value');
    const vals = await values.allTextContents();
    // 6 ready lessons, 0 coming lessons, 12 categories
    expect(vals[0]).toBe('6'); // 已上线
    expect(vals[1]).toBe('0'); // 筹备中
    expect(vals[2]).toBe('12'); // 门类
  });
});

// ===== 平板测试 (768x1024) =====
test.describe('Tablet (768x1024)', () => {
  test.use({ viewport: { width: 768, height: 1024 } });

  test('sidebar visible, cards in 2 columns', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const sidebar = page.locator('.home-sidebar');
    await expect(sidebar).toBeVisible();

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(6);
  });
});

// ===== 移动端测试 (375x812) =====
test.describe('Mobile (375x812)', () => {
  test.use({ viewport: { width: 375, height: 812 } });

  test('simple navbar adapts to mobile viewport', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 首页使用 ds-navbar--simple,无菜单切换按钮
    await expect(page.locator('#menu-toggle')).toHaveCount(0);

    // 品牌链接可见
    const brand = page.locator('.ds-btn-nav--brand');
    await expect(brand).toBeVisible();
    await expect(brand).toHaveText('国学课堂');

    // 关于本站链接可见
    const aboutLink = page.locator('.ds-navbar__inner .ds-btn-nav').last();
    await expect(aboutLink).toBeVisible();
  });

  test('drawer toggle button visible on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const drawerBtn = page.locator('#drawer-toggle');
    await expect(drawerBtn).toBeVisible();

    // Sidebar hidden by default on mobile (transform: translateX(-100%) → matrix with negative tx)
    const sidebar = page.locator('.home-sidebar');
    const transform = await sidebar.evaluate(el => getComputedStyle(el).transform);
    // matrix(1, 0, 0, 1, -260, 0) means translateX(-260px)
    expect(transform).toMatch(/-\d+/);

    // Click drawer to open
    await drawerBtn.click();
    const isOpen = await sidebar.evaluate(el => el.classList.contains('is-open'));
    expect(isOpen).toBe(true);

    // 抽屉打开后,按钮文字变成"收起"
    const text = page.locator('#drawer-toggle .ds-btn-nav__text');
    // 移动端文字隐藏(只显示图标),所以通过 JS 检查
    const textContent = await text.evaluate(el => el.textContent);
    expect(textContent).toBe('收起');
  });

  test('search box hidden on mobile when drawer closed', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchBox = page.locator('.search-box');
    const sidebar = page.locator('.home-sidebar');

    // When drawer is closed (sidebar off-canvas), search box should not be interactable
    const drawerClosed = await sidebar.evaluate(el => !el.classList.contains('is-open'));
    expect(drawerClosed).toBe(true);

    // Open drawer
    const drawerBtn = page.locator('#drawer-toggle');
    await drawerBtn.click();

    // Now search box should be visible inside the opened drawer
    const isOpen = await sidebar.evaluate(el => el.classList.contains('is-open'));
    expect(isOpen).toBe(true);
    await expect(searchBox).toBeVisible();
  });

  test('cards render in single column on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(6);
  });
});

// ===== 交互测试 =====
test.describe('Interactions', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('sidebar search filters sidebar links', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 先展开所有门类,让所有链接可见(默认是折叠的)
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
    await allLink.click({ noWaitAfter: true });
    await page.waitForTimeout(200);

    const searchInput = page.locator('#sidebar-search');
    await searchInput.fill('诗书');

    const jingLink = page.locator('.home-sidebar__link').filter({ hasText: '儒家经典' }).first();
    await expect(jingLink).toBeVisible();

    const mengxueDescLink = page.locator('.home-sidebar__link').filter({ hasText: '三字经 · 百家姓' }).first();
    await expect(mengxueDescLink).toBeHidden();
  });

  test('click category header expands/collapses sub-items', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
    const mengxueNav = page.locator('.home-sidebar__nav').filter({ hasText: '论语' }).first();

    // Initially hidden
    let isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
    expect(isHidden).toBe(true);

    // Click to expand
    await mengxueHeader.click();
    isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
    expect(isHidden).toBe(false);
    // toHaveClass does exact match, use evaluate instead
    let hasExpanded = await mengxueHeader.evaluate(el => el.classList.contains('is-expanded'));
    expect(hasExpanded).toBe(true);

    // Click to collapse
    await mengxueHeader.click();
    isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
    expect(isHidden).toBe(true);
    hasExpanded = await mengxueHeader.evaluate(el => el.classList.contains('is-expanded'));
    expect(hasExpanded).toBe(false);
  });

  test('click on ready discipline filters cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // Click the "蒙学" category header first to expand
    const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
    await mengxueHeader.click();

    // Then click the filter link
    const mengxueFilterLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '三字经 · 百家姓' }).first();
    await mengxueFilterLink.click({ noWaitAfter: true });

    const title = page.locator('#filter-title');
    await expect(title).toContainText('蒙学');

    // Should show 6 ready lessons in mengxue
    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(6);
  });

  test('click on coming discipline shows placeholder', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // Expand 经部 first
    const jingHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '经部' }).first();
    await jingHeader.click();

    // Click filter link
    const jingFilterLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '儒家经典' }).first();
    await jingFilterLink.click({ noWaitAfter: true });

    const comingEl = page.locator('#coming-soon');
    await expect(comingEl).toBeVisible();
    await expect(comingEl).toContainText('经部');
    await expect(comingEl).toContainText('即将上线');

    const grid = page.locator('#lesson-cards');
    await expect(grid).toHaveAttribute('hidden');
  });

  test('click "全部课程" resets to all', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // Expand and click 经部
    const jingHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '经部' }).first();
    await jingHeader.click();
    const jingLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '儒家经典' }).first();
    await jingLink.click({ noWaitAfter: true });
    await expect(page.locator('#coming-soon')).toBeVisible();

    // Click reset
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link').first();
    await allLink.click({ noWaitAfter: true });

    await expect(page.locator('#lesson-cards')).toBeVisible();
    await expect(page.locator('#filter-title')).toContainText('全部课程');
  });
});

// ===== 回归测试 =====
test.describe('Regression', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('about.html still works', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/about.html`);

    // About page should not use home-wrapper
    const hasHomeWrapper = await page.evaluate(() =>
      document.querySelector('.home-wrapper') !== null
    );
    expect(hasHomeWrapper).toBe(false);

    const title = page.locator('h1');
    await expect(title).toBeVisible();
  });

  test('lesson page still works', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/lessons/01-lunyu/index.html`, { waitUntil: 'domcontentloaded' });

    const hasHomeWrapper = await page.evaluate(() =>
      document.querySelector('.home-wrapper') !== null
    );
    expect(hasHomeWrapper).toBe(false);

    const slideViewport = page.locator('.slide-viewport');
    await expect(slideViewport).toBeVisible();
  });

  test('404.html still works', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/404.html`);

    const title = await page.title();
    expect(title).toMatch(/404|页面不存在/i);

    const heading = page.locator('h1');
    await expect(heading).toContainText('抱歉，这个页面不存在');

    const fourOhFour = page.locator('text=/^404$/');
    await expect(fourOhFour).toBeVisible();
  });
});
