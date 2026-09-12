// tests/homepage.spec.js
// Playwright E2E tests for homepage v3 (static sidebar + series cover + mobile numstrip)
// Current structure facts:
//   - 52 lessons (num 01..52, all status:'ready') in lessons-manifest.js
//   - 5 categories (daolun/xueer/weizheng/bayi/mengxue, num 01..05, all ready)
//   - Sidebar rendered by homepage.js: 5 groups, collapsed sub-navs, filter + reset links
//   - Mobile (<768px): sidebar hidden, top numstrip visible (flat sorted chips, 52 in total)
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

    // Sidebar visible (default expanded on desktop, no off-canvas)
    await expect(page.locator('.home-sidebar')).toBeVisible();

    // Main content visible
    await expect(page.locator('.home-content')).toBeVisible();

    // Series cover visible
    const seriesCover = page.locator('.series-cover');
    await expect(seriesCover).toBeVisible();
    await expect(seriesCover.locator('.series-cover__title')).toContainText('系列课程总览');

    // No right aside
    await expect(page.locator('.home-aside')).toHaveCount(0);
  });

  test('top nav shows simple brand and about link without menu/drawer toggles', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 首页导航条使用 ds-navbar--simple,仅含品牌 + "关于本站"
    const brand = page.locator('.ds-btn-nav--brand');
    await expect(brand).toHaveText('国学课堂');

    const aboutLink = page.locator('.ds-navbar__inner a[href="about.html"]');
    await expect(aboutLink).toHaveText('关于本站');

    // 首页无菜单/抽屉切换按钮
    await expect(page.locator('#menu-toggle')).toHaveCount(0);
    await expect(page.locator('#drawer-toggle')).toHaveCount(0);
  });

  test('sidebar renders 5 ready categories (default collapsed)', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 5 category groups
    const groups = page.locator('.home-sidebar__group');
    await expect(groups).toHaveCount(5);

    // 5 category headers
    const headers = page.locator('.home-sidebar__category-header');
    await expect(headers).toHaveCount(5);

    // Header numbers 01..05 in order
    const iconTexts = await page.locator('.home-sidebar__category-icon').allTextContents();
    expect(iconTexts).toEqual(['01', '02', '03', '04', '05']);

    // Header labels in order: 导论/学而/为政/八佾/蒙学
    const labelTexts = await page.locator('.home-sidebar__category-label').allTextContents();
    expect(labelTexts).toEqual(['导论', '学而', '为政', '八佾', '蒙学']);

    // Sub-navs (non-all) hidden by default
    const subNavs = page.locator('.home-sidebar__nav:not(.home-sidebar__nav--all)');
    await expect(subNavs).toHaveCount(5);
    for (let i = 0; i < await subNavs.count(); i++) {
      const isHidden = await subNavs.nth(i).evaluate(el => el.hasAttribute('hidden'));
      expect(isHidden).toBe(true);
    }

    // Per-category filter links: 5
    await expect(page.locator('.home-sidebar__link--filter')).toHaveCount(5);

    // Course sub-links: 52 (one per ready lesson)
    await expect(page.locator('.home-sidebar__link--sub')).toHaveCount(52);

    // "全部课程" reset link visible
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
    await expect(allLink).toBeVisible();
    await expect(allLink).toContainText('全部课程');
  });

  test('search box renders with placeholder', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const searchInput = page.locator('#sidebar-search');
    await expect(searchInput).toBeVisible();
    await expect(searchInput).toHaveAttribute('placeholder', '搜索课程…');
  });

  test('lesson cards render correctly (52 ready lessons)', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(52);

    const firstCard = cards.first();
    await expect(firstCard.locator('.lesson-title')).toContainText('论语');
    await expect(firstCard.locator('.lesson-num')).toBeVisible();
    await expect(firstCard.locator('.lesson-num')).toHaveText('01');
  });

  test('series cover stats show correct counts (52/0/5)', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const values = page.locator('.series-stat__value');
    await expect(values).toHaveCount(3); // 已上线 / 筹备中 / 学科门类
    const vals = await values.allTextContents();
    expect(vals[0]).toBe('52'); // 已上线
    expect(vals[1]).toBe('0');  // 筹备中
    expect(vals[2]).toBe('5');  // 学科门类
  });
});

// ===== 平板测试 (768x1024) =====
test.describe('Tablet (768x1024)', () => {
  test.use({ viewport: { width: 768, height: 1024 } });

  test('sidebar visible, 52 lesson cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    await expect(page.locator('.home-sidebar')).toBeVisible();
    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(52);
  });
});

// ===== 移动端测试 (375x812) =====
test.describe('Mobile (375x812)', () => {
  test.use({ viewport: { width: 375, height: 812 } });

  test('sidebar hidden, numstrip visible with 52 chips and horizontal scroll', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // No menu/drawer toggles on homepage
    await expect(page.locator('#menu-toggle')).toHaveCount(0);
    await expect(page.locator('#drawer-toggle')).toHaveCount(0);

    // Sidebar hidden on mobile (<768px, display:none)
    await expect(page.locator('.home-sidebar')).toBeHidden();

    // 顶部序号条可见
    const numstrip = page.locator('#home-numstrip');
    await expect(numstrip).toBeVisible();

    // 按门类分组：5 组
    const groups = page.locator('.home-numstrip__group');
    await expect(groups).toHaveCount(5);

    // 门类标签顺序：导论/学而/为政/八佾/蒙学
    const labels = await page.locator('.home-numstrip__label').allTextContents();
    expect(labels).toEqual(['导论', '学而', '为政', '八佾', '蒙学']);

    // 组内 chip 数：导论=2、学而=14、为政=17、八佾=18、蒙学=1（合计 52）
    const expectedChipCounts = [2, 14, 17, 18, 1];
    for (let i = 0; i < expectedChipCounts.length; i++) {
      await expect(groups.nth(i).locator('.home-numstrip__chip')).toHaveCount(expectedChipCounts[i]);
    }

    // 全部 52 个序号 chip，按门类顺序排列
    const chips = page.locator('.home-numstrip__chip');
    await expect(chips).toHaveCount(52);
    // 首组「导论」首项 = 01；末组「蒙学」唯一项 = 03
    await expect(chips.first()).toHaveText('01');
    await expect(chips.last()).toHaveText('03');

    // 横向可滑动
    const overflowX = await numstrip.evaluate(el => getComputedStyle(el).overflowX);
    expect(['auto', 'scroll']).toContain(overflowX);

    // 第一个 chip 指向第 01 课
    await expect(chips.first()).toHaveAttribute('href', 'lessons/01-lunyu/index.html');
    await expect(chips.first()).toHaveAttribute('aria-label', /01/);
  });
});

// ===== 交互测试 =====
test.describe('Interactions', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('sidebar search filters sidebar links', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 先展开所有门类,让链接可以被命中
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
    await allLink.click({ noWaitAfter: true });

    const searchInput = page.locator('#sidebar-search');
    await searchInput.fill('三字经');

    // 命中: 蒙学门类描述行 + 《三字经》课程行
    const hit = page.locator('.home-sidebar__link').filter({ hasText: '三字经' }).first();
    await expect(hit).toBeVisible();

    // 未命中: 学而门类下的课程被隐藏
    const miss = page.locator('.home-sidebar__link').filter({ hasText: '温良恭俭让' }).first();
    await expect(miss).toBeHidden();
  });

  test('click category header expands/collapses sub-items', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    const xueerHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '学而' }).first();
    const xueerNav = page.locator('.home-sidebar__nav[data-subject-group="xueer"]');

    // Initially hidden
    expect(await xueerNav.evaluate(el => el.hasAttribute('hidden'))).toBe(true);

    // Click to expand
    await xueerHeader.click();
    expect(await xueerNav.evaluate(el => el.hasAttribute('hidden'))).toBe(false);
    expect(await xueerHeader.evaluate(el => el.classList.contains('is-expanded'))).toBe(true);

    // Click to collapse
    await xueerHeader.click();
    expect(await xueerNav.evaluate(el => el.hasAttribute('hidden'))).toBe(true);
    expect(await xueerHeader.evaluate(el => el.classList.contains('is-expanded'))).toBe(false);
  });

  test('click on ready category filters cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 展开 八佾 门类
    const bayiHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '八佾' }).first();
    await bayiHeader.click();

    // 点击门类描述行触发过滤
    const bayiFilter = page.locator('.home-sidebar__link--filter').filter({ hasText: '八佾' }).first();
    await bayiFilter.click({ noWaitAfter: true });

    await expect(page.locator('#filter-title')).toContainText('八佾');

    // 八佾门类已有 18 门 ready 课程
    const cards = page.locator('#lesson-cards .ds-lesson-card');
    await expect(cards).toHaveCount(18);
    await expect(page.locator('#lesson-cards')).toBeVisible();
  });

  test('click "全部课程" resets to all', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);

    // 先过滤到 蒙学(1 门)
    const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
    await mengxueHeader.click();
    const mengxueFilter = page.locator('.home-sidebar__link--filter').filter({ hasText: '蒙学' }).first();
    await mengxueFilter.click({ noWaitAfter: true });
    await expect(page.locator('#lesson-cards .ds-lesson-card')).toHaveCount(1);

    // 点「全部课程」重置
    const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
    await allLink.click({ noWaitAfter: true });

    await expect(page.locator('#lesson-cards .ds-lesson-card')).toHaveCount(52);
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
    await expect(title).toContainText('关于本站');
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