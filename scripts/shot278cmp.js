const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const p = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await p.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  await p.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));

  const url = 'file:///' + path.resolve(__dirname, '..', 'lessons/278-si-ma-niu-wen-ren/index.html').split(path.sep).join('/');
  await p.goto(url, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(800);

  for (const idx of [3, 5]) {
    await p.evaluate((i) => {
      const s = Array.from(document.querySelectorAll('.slide-container > .slide'));
      s.forEach((x) => x.classList.remove('active'));
      s[i].classList.add('active');
    }, idx);
    await p.waitForTimeout(200);
    await p.screenshot({ path: 'shots/278-p' + idx + '.png' });
  }
  await browser.close();
})();
