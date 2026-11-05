const { chromium } = require('playwright-core');
const path = require('path');

(async () => {
  const b = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  await p.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  await p.addInitScript(() => localStorage.setItem('guoxue_unlocked', '1'));
  const abs = path.resolve(__dirname, '../lessons/254-hui-fei-zhu-wo/index.html');
  const url = 'file:///' + abs.split(path.sep).join('/');
  await p.goto(url, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(900);
  for (const i of [0, 1, 3, 5, 7, 20, 22]) {
    await p.evaluate((n) => {
      const s = document.querySelectorAll('.slide-container > .slide');
      s.forEach((x) => x.classList.remove('active'));
      s[n].classList.add('active');
    }, i);
    await p.waitForTimeout(250);
    await p.screenshot({ path: `C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/test-results/l254-${i}.png` });
  }
  await b.close();
  console.log('shots ok');
})();
