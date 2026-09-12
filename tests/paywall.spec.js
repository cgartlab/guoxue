// tests/paywall.spec.js
// Playwright E2E tests for paywall v2 (面包多支付 + 订单号验单解锁)
// Strategy:
//   - 本地静态服务器端口 7891(独立于 homepage.spec.js 的 7890)
//   - 通过 page.addInitScript 设置 window.GUOXUE_REDEEM_API 指向同源 /api/redeem
//     (模拟部署后指向真实 Worker 的姿势),再用 page.route() 拦截该请求,
//     模拟 Worker 返回,绝不连接真实面包多接口。
//   - 付费课样例: lessons/06-zengzi-sansheng (学而门类,非免费课)
//     免费课样例: lessons/01-lunyu
// Run: npx playwright test tests/paywall.spec.js --workers=1

const { test, expect } = require('@playwright/test');
const path = require('path');
const http = require('http');
const fs = require('fs');

const PROJECT_ROOT = path.resolve(__dirname, '..');
const PORT = 7891;
const BASE = `http://localhost:${PORT}`;
const PAID_LESSON = '/lessons/06-zengzi-sansheng/index.html';
const FREE_LESSON = '/lessons/01-lunyu/index.html';
const PRODUCT_URL = 'https://mbd.pub/o/bread/YZaVlJ5rag==';
const DEFAULT_API = 'https://pay.8023laozhanshi.cc/api/redeem';
const VALID_ORDER = 'abcd1234abcd1234abcd1234abcd1234';

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
    const url = new URL(req.url, `${BASE}`);
    let filePath = path.join(PROJECT_ROOT, url.pathname);
    if (url.pathname === '/') filePath = path.join(PROJECT_ROOT, 'index.html');
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

test.describe('付费墙 — 面包多解锁', () => {
  test.use({ viewport: { width: 1280, height: 800 } });

  test('付费课显示弹窗,含去面包多支付按钮且指向商品链接', async ({ page }) => {
    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });

    // 弹窗出现
    await expect(page.locator('.paywall-overlay--show')).toBeVisible();
    await expect(page.locator('.paywall-title')).toContainText('解锁全部国学课程');
    await expect(page.locator('.paywall-subtitle')).toContainText('一次付费，永久解锁');

    // 去面包多支付按钮:href 指向商品链接,文案含价格
    const payBtn = page.locator('#paywall-product-btn');
    await expect(payBtn).toBeVisible();
    await expect(payBtn).toHaveAttribute('href', PRODUCT_URL);
    await expect(payBtn).toHaveAttribute('target', '_blank');
    await expect(payBtn).toContainText('去面包多支付');
    await expect(payBtn).toContainText('¥9.90');

    // 订单号 / 邮箱输入框可见
    await expect(page.locator('#paywall-order-input')).toBeVisible();
    await expect(page.locator('#paywall-email-input')).toBeVisible();

    // CONFIG 与按钮一致
    const cfg = await page.evaluate(() => window.UNLOCK.CONFIG);
    expect(cfg.productUrl).toBe(PRODUCT_URL);
    expect(cfg.price).toBe('9.90');
  });

  test('redeemApi 默认指向已部署的 Worker(自定义域名)', async ({ page }) => {
    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });

    const redeemApi = await page.evaluate(() => window.UNLOCK.CONFIG.redeemApi);
    expect(redeemApi).toBe(DEFAULT_API);
  });

  test('免费课不弹窗,课程正常渲染(测验可渲染)', async ({ page }) => {
    await page.goto(`${BASE}${FREE_LESSON}`, { waitUntil: 'domcontentloaded' });

    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);
    await expect(page.locator('.slide-viewport')).toBeVisible();
    // quiz-0 位于第 13 页(初始只显示封面页),断言引擎已填充测验内容(attached 而非 visible)
    await expect(page.locator('#quiz-0 .quiz-option').first()).toBeAttached();
  });

  test('输入订单号解锁成功:提示解锁码、localStorage 记录、刷新后不再弹窗且测验可渲染', async ({ page }) => {
    let captured = null;
    await page.route('**/api/redeem', async (route) => {
      captured = JSON.parse(route.request().postData() || '{}');
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ ok: true, code: 'GX-TEST123' })
      });
    });
    await page.addInitScript(() => {
      window.GUOXUE_REDEEM_API = '/api/redeem';
    });

    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });
    await expect(page.locator('.paywall-overlay--show')).toBeVisible();

    await page.locator('#paywall-order-input').fill(VALID_ORDER);
    await page.locator('#paywall-email-input').fill('learner@example.com');
    await page.locator('#paywall-code-btn').click();

    // 请求体携带 order_id 与 email
    await expect.poll(() => captured).toBeTruthy();
    expect(captured.order_id).toBe(VALID_ORDER);
    expect(captured.email).toBe('learner@example.com');

    // 状态提示:解锁成功 + 解锁码
    await expect(page.locator('#paywall-status')).toContainText('解锁成功');
    await expect(page.locator('#paywall-status')).toContainText('GX-TEST123');

    // localStorage 已记录解锁标记与解锁码
    expect(await page.evaluate(() => localStorage.getItem('guoxue_unlocked'))).toBe('1');
    expect(await page.evaluate(() => localStorage.getItem('guoxue_unlock_code'))).toBe('GX-TEST123');

    // 稍后自动刷新:不再弹窗,课程内容(测验)已由引擎填充(quiz-0 非 active slide,断言 attached)
    await page.waitForTimeout(1800);
    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);
    await expect(page.locator('#quiz-0 .quiz-option').first()).toBeAttached();
  });

  test('订单未支付:显示"未支付"友好提示', async ({ page }) => {
    await page.route('**/api/redeem', async (route) => {
      await route.fulfill({
        status: 402,
        contentType: 'application/json',
        body: JSON.stringify({ ok: false, reason: 'not_paid' })
      });
    });
    await page.addInitScript(() => {
      window.GUOXUE_REDEEM_API = '/api/redeem';
    });

    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });
    await page.locator('#paywall-order-input').fill(VALID_ORDER);
    await page.locator('#paywall-code-btn').click();

    await expect(page.locator('#paywall-status')).toContainText('未支付');
    // 解锁按钮恢复可用
    await expect(page.locator('#paywall-code-btn')).toBeEnabled();
    // 未写入解锁标记
    expect(await page.evaluate(() => localStorage.getItem('guoxue_unlocked'))).toBeNull();
  });

  test('空订单号点击解锁:提示输入订单号', async ({ page }) => {
    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });

    await page.locator('#paywall-code-btn').click();
    await expect(page.locator('#paywall-status')).toContainText('请输入订单号');
    // 订单号格式提示保持错误配色
    await expect(page.locator('#paywall-status')).toHaveClass(/paywall-status--error/);
  });

  test('非法订单号格式(前端直接提示服务端 reason)', async ({ page }) => {
    await page.route('**/api/redeem', async (route) => {
      await route.fulfill({
        status: 400,
        contentType: 'application/json',
        body: JSON.stringify({ ok: false, reason: 'invalid_order_id' })
      });
    });
    await page.addInitScript(() => {
      window.GUOXUE_REDEEM_API = '/api/redeem';
    });

    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });
    await page.locator('#paywall-order-input').fill('not-a-hex');
    await page.locator('#paywall-code-btn').click();

    await expect(page.locator('#paywall-status')).toContainText('订单号格式不正确');
  });

  test('关闭按钮与点击遮罩均可关闭弹窗', async ({ page }) => {
    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });
    await expect(page.locator('.paywall-overlay--show')).toBeVisible();

    // 关闭按钮
    await page.locator('#paywall-close').click();
    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);

    // 再次打开,点遮罩关闭
    await page.evaluate(() => window.UNLOCK.showPaywall());
    await expect(page.locator('.paywall-overlay--show')).toBeVisible();
    await page.mouse.click(10, 10);
    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);
  });

  test('ESC 键可关闭弹窗', async ({ page }) => {
    await page.goto(`${BASE}${PAID_LESSON}`, { waitUntil: 'domcontentloaded' });
    await expect(page.locator('.paywall-overlay--show')).toBeVisible();

    await page.keyboard.press('Escape');
    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);
  });
});