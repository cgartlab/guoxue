const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.addInitScript(() => {
    try {
      localStorage.setItem('guoxue_unlocked', '1');
      localStorage.setItem('guoxue_unlock_code', 'SCREENSHOT-LOCAL');
    } catch (e) {}
  });
  await page.route('**/*', (r) => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  const url = 'file:///' + path.resolve(__dirname, '../lessons/419-yi-zhe-san-you/index.html').split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(800);
  for (const n of [0, 1, 2, 5, 7, 20, 22]) {
    await page.evaluate((n) => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      slides.forEach((s) => s.classList.remove('active'));
      slides[n].classList.add('active');
    }, n);
    await page.waitForTimeout(220);
    await page.screenshot({ path: `shots/419-p${String(n).padStart(2,'0')}.png` });
  }
  await browser.close();
  console.log('done');
})();
