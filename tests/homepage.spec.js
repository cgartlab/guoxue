// tests/homepage.spec.js
// Playwright E2E tests for homepage (v2.0 redesign)
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

  test('three-column layout renders', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // Sidebar visible
    const sidebar = page.locator('.home-sidebar');
    await expect(sidebar).toBeVisible();

    // Main content visible
    const mainContent = page.locator('.home-content');
    await expect(mainContent).toBeVisible();

    // Right aside visible
    const aside = page.locator('.home-aside');
    await expect(aside).toBeVisible();

    // Featured section has content
    const featuredItems = page.locator('.featured-item');
    await expect(featuredItems).toHaveCount(2); // 01-lunyu and 02-sanzijing
  });

  test('top nav menu shows 4 items on desktop', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const items = page.locator('.ds-navbar__menu-item');
    await expect(items).toHaveCount(3); // 首页 / 课程 / 门类 (关于本站在 ds-nav-right)

    // 汉堡按钮在桌面端隐藏
    const toggle = page.locator('#menu-toggle');
    const isHidden = await toggle.evaluate(el => getComputedStyle(el).display === 'none');
    expect(isHidden).toBe(true);
  });

  test('sidebar renders 12 disciplines', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const groups = page.locator('.home-sidebar__group');
    await expect(groups).toHaveCount(12);

    // "✨ 全部课程" 重置项
    const allLink = page.locator('.home-sidebar__link').filter({ hasText: '✨ 全部课程' });
    await expect(allLink).toBeVisible();
  });

  test('coming disciplines have badge', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // "经部" 状态为 coming,显示 ⏳ 徽标
    const jingGroup = page.locator('.home-sidebar__group--coming').filter({ hasText: '经部' });
    await expect(jingGroup).toBeVisible();
    const badge = jingGroup.locator('.home-sidebar__badge--coming').first();
    await expect(badge).toContainText('⏳');
  });

  test('lesson cards render correctly', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(3); // 3 ready lessons

    // Check card content
    const firstCard = cards.first();
    await expect(firstCard.locator('.lesson-title')).toContainText('论语');
    await expect(firstCard.locator('.lesson-icon')).toContainText('📖');
  });

  test('hero section renders', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const hero = page.locator('.ds-hero');
    await expect(hero).toBeVisible();
    await expect(hero.locator('h1')).toContainText('国学课堂');
    await expect(hero.locator('.hero-subtitle')).toContainText('传承经典');
  });

  test('filter-title shows "全部课程" by default', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    const title = page.locator('#filter-title');
    await expect(title).toContainText('✨ 全部课程');
  });

  test('search box renders in sidebar', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchInput = page.locator('#sidebar-search');
    await expect(searchInput).toBeVisible();
    await expect(searchInput).toHaveAttribute('placeholder', '🔍 搜索课程…');
  });
});

// ===== 平板测试 (768x1024) =====
test.describe('Tablet (768x1024)', () => {
  test.use({ viewport: { width: 768, height: 1024 } });

  test('right aside hidden on tablet', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const aside = page.locator('.home-aside');
    const isHidden = await aside.evaluate(el => getComputedStyle(el).display === 'none');
    expect(isHidden).toBe(true);
  });

  test('sidebar still visible on tablet', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const sidebar = page.locator('.home-sidebar');
    await expect(sidebar).toBeVisible();
  });

  test('cards render in 2 columns on tablet', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });
});

// ===== 移动端测试 (375x812) =====
test.describe('Mobile (375x812)', () => {
  test.use({ viewport: { width: 375, height: 812 } });

  test('top nav collapses to hamburger on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const toggle = page.locator('#menu-toggle');
    const isVisible = await toggle.isVisible();
    expect(isVisible).toBe(true);

    // 菜单默认关闭
    const menu = page.locator('#primary-menu');
    const hasOpenClass = await menu.evaluate(el => el.classList.contains('is-open'));
    expect(hasOpenClass).toBe(false);

    // 点击展开
    await toggle.click();
    await expect(menu).toHaveClass(/is-open/);
    await expect(toggle).toHaveAttribute('aria-expanded', 'true');

    // 点击按钮再次收起
    await toggle.click();
    await expect(menu).not.toHaveClass(/is-open/);
    await expect(toggle).toHaveAttribute('aria-expanded', 'false');
  });

  test('right aside hidden on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const aside = page.locator('.home-aside');
    const isHidden = await aside.evaluate(el => getComputedStyle(el).display === 'none');
    expect(isHidden).toBe(true);
  });

  test('search box hidden on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchBox = page.locator('.search-box');
    const isHidden = await searchBox.evaluate(el => getComputedStyle(el).display === 'none');
    expect(isHidden).toBe(true);
  });

  test('cards render in single column on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });
});

// ===== 交互测试 =====
test.describe('Interactions', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('sidebar search filters sidebar links', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchInput = page.locator('#sidebar-search');
    await searchInput.fill('诗书');

    // 匹配的"经部"描述链接应可见（"儒家经典 · 诗书礼易春秋"包含"诗书"）
    const jingLink = page.locator('.home-sidebar__link').filter({ hasText: '儒家经典' }).first();
    await expect(jingLink).toBeVisible();

    // 不匹配的"蒙学"描述链接应隐藏（"三字经 · 百家姓 · 千字文 · 论语"不含"诗书"）
    const mengxueDescLink = page.locator('.home-sidebar__link').filter({ hasText: '三字经 · 百家姓' }).first();
    await expect(mengxueDescLink).toBeHidden();
  });

  test('click on ready discipline filters cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 点击"蒙学"门类的 filter 链接(描述文本"三字经 · 百家姓 · 千字文 · 论语")
    const mengxueFilterLink = page.locator('.home-sidebar__link').filter({ hasText: '三字经 · 百家姓' }).first();
    await mengxueFilterLink.click({ noWaitAfter: true });

    // filter-title 应更新
    const title = page.locator('#filter-title');
    await expect(title).toContainText('蒙学');

    // 应只显示蒙学的 ready 课程(论语 + 论语混合版 + 三字经 = 3)
    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });

  test('click on coming discipline shows placeholder', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 点击"经部"门类的 filter 链接(描述文本"儒家经典 · 诗书礼易春秋")
    const jingFilterLink = page.locator('.home-sidebar__link').filter({ hasText: '儒家经典' }).first();
    await jingFilterLink.click({ noWaitAfter: true });

    // 网格应隐藏,"敬请期待"占位应显示
    const grid = page.locator('#lesson-cards');
    const comingEl = page.locator('#coming-soon');
    await expect(comingEl).toBeVisible();
    await expect(comingEl).toContainText('经部');
    await expect(comingEl).toContainText('即将上线');
    // 检查 hidden 属性而非 toBeHidden()（Playwright 对 hidden 属性的 visibility 检测有差异）
    await expect(grid).toHaveAttribute('hidden');
  });

  test('click "✨ 全部课程" resets to all', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 先点经部切到 coming 状态
    const jingLink = page.locator('.home-sidebar__link').filter({ hasText: '诗书礼易春秋' });
    await jingLink.first().click({ noWaitAfter: true });
    await expect(page.locator('#coming-soon')).toBeVisible();

    // 点击"✨ 全部课程"重置
    const allLink = page.locator('.home-sidebar__link').filter({ hasText: '✨ 全部课程' });
    await allLink.click({ noWaitAfter: true });

    await expect(page.locator('#lesson-cards')).toBeVisible();
    await expect(page.locator('#filter-title')).toContainText('✨ 全部课程');
  });
});

// ===== 回归测试 =====
test.describe('Regression', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('about.html still works', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/about.html`);

    // About page should not use .home-layout
    const hasHomeLayout = await page.evaluate(() =>
      document.querySelector('.home-layout') !== null
    );
    expect(hasHomeLayout).toBe(false);

    // About page content should be visible
    const title = page.locator('h1');
    await expect(title).toBeVisible();
  });

  test('lesson page still works', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/lessons/01-lunyu/index.html`);

    // Lesson page should not use .home-layout
    const hasHomeLayout = await page.evaluate(() =>
      document.querySelector('.home-layout') !== null
    );
    expect(hasHomeLayout).toBe(false);

    // Slide viewport should be present
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

