const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  await page.addInitScript(() => localStorage.setItem('guoxue_unlocked', '1'));
  const url = 'file:///' + path.resolve(__dirname, '..', 'lessons/464-zun-xian-er-rong-zhong/index.html').split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1000);
  const out = path.resolve(__dirname, '..', 'shots464');
  require('fs').mkdirSync(out, { recursive: true });
  for (const p of [0, 1, 2, 5, 7, 9, 20, 21, 22, 23]) {
    await page.evaluate((n) => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      slides.forEach((s) => s.classList.remove('active'));
      slides[n].classList.add('active');
    }, p);
    await page.waitForTimeout(350);
    await page.screenshot({ path: path.join(out, `p${String(p + 1).padStart(2, '0')}.png`) });
  }
  console.log('shots -> ' + out);
  await browser.close();
})();
