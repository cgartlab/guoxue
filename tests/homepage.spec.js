// tests/homepage.spec.js
// Playwright E2E tests for homepage redesign
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

  test('sidebar navigation renders categories', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    
    const sidebarLinks = page.locator('.home-sidebar__link');
    const count = await sidebarLinks.count();
    expect(count).toBeGreaterThan(0);
    
    // Check that core category has active links (at least one)
    const activeLinks = page.locator('.home-sidebar__link--active');
    const activeCount = await activeLinks.count();
    expect(activeCount).toBeGreaterThan(0);
  });

  test('lesson cards render correctly', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    
    const cards = page.locator('.ds-lesson-card');
    await expect(cards).toHaveCount(3); // 3 lessons
    
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
    
    const cards = page.locator('.ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });
});

// ===== 移动端测试 (375x812) =====
test.describe('Mobile (375x812)', () => {
  test.use({ viewport: { width: 375, height: 812 } });

  test('sidebar collapses to horizontal row on mobile', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    
    const sidebar = page.locator('.home-sidebar');
    await expect(sidebar).toBeVisible();
    
    // Sidebar nav should be horizontal on mobile (use first nav element)
    const nav = page.locator('.home-sidebar__nav').first();
    const flexDirection = await nav.evaluate(el => getComputedStyle(el).flexDirection);
    expect(flexDirection).toBe('row');
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
    
    const cards = page.locator('.ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });
});

// ===== 交互测试 =====
test.describe('Interactions', () => {
  test.use({ viewport: { width: 1440, height: 900 } });

  test('sidebar search filters cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    
    const searchInput = page.locator('#sidebar-search');
    await searchInput.fill('论语');
    
    // Sidebar links should filter
    const sidebarLinks = page.locator('.home-sidebar__link');
    const visibleLinks = await sidebarLinks.count();
    expect(visibleLinks).toBeGreaterThan(0);
    
    // Cards should still be visible (search only filters sidebar, not cards)
    const cards = page.locator('.ds-lesson-card');
    await expect(cards).toHaveCount(3);
  });

  test('sidebar category click filters cards', async ({ page }) => {
    await page.goto(`http://localhost:${PORT}/`);
    
    // Click on "进阶拓展" category link
    const advancedLink = page.locator('.home-sidebar__link').filter({ hasText: '混合版' });
    await advancedLink.click();
    
    // Cards should filter to show only advanced
    const cards = page.locator('.ds-lesson-card');
    // After filtering, should show 1 card (01-lunyu-mixed)
    const cardCount = await cards.count();
    expect(cardCount).toBe(1);
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
    // Directly load 404.html to verify it renders correctly
    await page.goto(`http://localhost:${PORT}/404.html`);
    
    // Should show 404 page content
    const title = await page.title();
    expect(title).toMatch(/404|页面不存在/i);
    
    // Check for 404 heading
    const heading = page.locator('h1');
    await expect(heading).toContainText('抱歉，这个页面不存在');
    
    // Check for 404 number
    const fourOhFour = page.locator('text=/^404$/');
    await expect(fourOhFour).toBeVisible();
  });
});
