const { chromium } = require('playwright-core');
const path = require('path');
const fs = require('fs');

const pages = [0, 1, 2, 3, 5, 6, 20, 22, 23];
const rel = 'lessons/293-zi-wei-zheng-yan-yong-sha/index.html';

(async () => {
  const outDir = path.resolve(__dirname, '..', 'shots', '293');
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  await ctx.addInitScript(() => {
    try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {}
  });
  const page = await ctx.newPage();
  await page.route('**/*', (route) => {
    const u = route.request().url();
    if (u.startsWith('file://')) return route.continue();
    return route.abort();
  });

  const url = 'file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(700);

  for (const p of pages) {
    await page.evaluate((idx) => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      slides.forEach((s) => s.classList.remove('active'));
      slides[idx].classList.add('active');
    }, p);
    await page.waitForTimeout(250);
    const file = path.join(outDir, `p${String(p).padStart(2, '0')}.png`);
    await page.screenshot({ path: file });
    console.log('saved', file);
  }

  // 溢出读数（不 abort 资源时）
  const rows = await page.evaluate(() => {
    const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
    return slides.map((el) => {
      slides.forEach((s) => s.classList.remove('active'));
      el.classList.add('active');
      return { page: el.getAttribute('data-page'), over: el.scrollHeight - el.clientHeight };
    });
  });
  console.log('overflow:', rows.filter((r) => r.over > 2).map((r) => `p${r.page}(+${r.over})`).join(' ') || '无');

  await browser.close();
})();
