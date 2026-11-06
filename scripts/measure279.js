const { chromium } = require('playwright-core');
const path = require('path');

const files = [
  ['278', 'lessons/278-si-ma-niu-wen-ren/index.html'],
  ['279', 'lessons/279-si-ma-niu-wen-jun-zi/index.html'],
];

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const p = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await p.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  await p.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));

  for (const [label, rel] of files) {
    const url = 'file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/');
    await p.goto(url, { waitUntil: 'domcontentloaded' });
    await p.waitForTimeout(600);
    const data = await p.evaluate(() => {
      const out = {};
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      [3, 5, 6].forEach((i) => {
        slides.forEach((x) => x.classList.remove('active'));
        slides[i].classList.add('active');
        out[i] = Array.from(slides[i].querySelectorAll('p')).map((e) => Math.round(e.getBoundingClientRect().height));
      });
      return out;
    });
    console.log(label, JSON.stringify(data));
  }
  await browser.close();
})();
