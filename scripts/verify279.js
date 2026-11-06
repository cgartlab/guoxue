const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });

  // ---- 首页（桌面）----
  const page = await browser.newPage({ viewport: { width: 1470, height: 910 } });
  await page.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  const home = 'file:///' + path.resolve(__dirname, '..', 'index.html').replace(/\\/g, '/');
  await page.goto(home, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1000);

  const cards = await page.locator('#lesson-cards .ds-lesson-card').count();
  const stats = await page.locator('.series-stat__value').allTextContents();
  const subs = await page.locator('.home-sidebar__link--sub').count();
  const lastCard = await page.locator('#lesson-cards .ds-lesson-card').last().innerText();
  console.log('首页卡片数:', cards, '| 统计:', stats.join('/'), '| 侧栏课程链接:', subs);
  console.log('最后一张卡:', lastCard.replace(/\n/g, ' | '));

  // ---- 移动端 chip ----
  const m = await browser.newPage({ viewport: { width: 375, height: 812 } });
  await m.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  await m.goto(home, { waitUntil: 'domcontentloaded' });
  await m.waitForTimeout(800);
  const groups = m.locator('.home-numstrip__group');
  const cnt = [];
  const n = await groups.count();
  for (let i = 0; i < n; i++) cnt.push(await groups.nth(i).locator('.home-numstrip__chip').count());
  console.log('分组数:', n, '| chip 数:', JSON.stringify(cnt), '| 合计:', cnt.reduce((a, b) => a + b, 0));

  // ---- 新课渲染 ----
  const p = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await p.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  await p.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  const url = 'file:///' + path.resolve(__dirname, '..', 'lessons/279-si-ma-niu-wen-jun-zi/index.html').replace(/\\/g, '/');
  await p.goto(url, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(1000);
  const title = await p.title();
  const indicator = await p.locator('#page-indicator').innerText();
  console.log('新课标题:', title);
  console.log('页码指示:', indicator);

  // 逐页截图关键页
  const shots = [0, 3, 5, 20, 22];
  for (const idx of shots) {
    await p.evaluate((i) => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      slides.forEach((s) => s.classList.remove('active'));
      slides[i].classList.add('active');
    }, idx);
    await p.waitForTimeout(250);
    await p.screenshot({ path: `shots/279-p${idx}.png` });
  }
  console.log('截图完成: shots/279-p*.png');

  await browser.close();
})();
