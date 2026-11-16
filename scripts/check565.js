const { chromium } = require('playwright-core');
const path = require('path');

const CHROME = 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe';
const TARGETS = [
  ['565', 'lessons/565-jian-qiao-yu/index.html'],
  ['564', 'lessons/564-fan-chu-yan/index.html'],
];

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, args: ['--no-proxy-server'] });
  for (const [name, rel] of TARGETS) {
    const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    await page.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
    await page.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
    const url = 'file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/');
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);
    const res = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((sl, i) => {
        slides.forEach((x) => x.classList.remove('active'));
        sl.classList.add('active');
        const over = sl.scrollHeight - sl.clientHeight;
        const wide = sl.scrollWidth - sl.clientWidth;
        out.push({ i, sec: sl.dataset.section, over, wide });
      });
      return out;
    });
    const bad = res.filter((r) => r.over > 2 || r.wide > 2);
    console.log(`[${name}] slides=${res.length} 溢出页=${bad.length}`);
    bad.forEach((b) => console.log(`   page ${b.i} (${b.sec}) 纵向+${b.over}px 横向+${b.wide}px`));
    await page.close();
  }
  await browser.close();
})();
