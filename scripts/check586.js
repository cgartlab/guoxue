const { chromium } = require('playwright-core');
const path = require('path');

const CHROME = 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe';
const CUR = '586';
const PREV = '585';
const TARGETS = [
  [CUR, 'lessons/586-lie-dian-ji/index.html'],
  [PREV, 'lessons/585-fang-shi-qing/index.html'],
];

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, args: ['--no-proxy-server'] });
  const all = {};
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
        out.push({ i, sec: sl.dataset.section, over: sl.scrollHeight - sl.clientHeight, wide: sl.scrollWidth - sl.clientWidth });
      });
      return out;
    });
    all[name] = res;
    const bad = res.filter((r) => r.over > 2 || r.wide > 2);
    console.log(`[${name}] slides=${res.length} 溢出页=${bad.length}`);
    bad.forEach((b) => console.log(`   page ${b.i} (${b.sec}) 纵向+${b.over}px 横向+${b.wide}px`));
    await page.close();
  }
  const a = all[CUR], b = all[PREV];
  console.log(`\n逐页对照 (${CUR} vs ${PREV}):`);
  let worse = 0;
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    const x = a[i] || {}, y = b[i] || {};
    const d = (x.over || 0) - (y.over || 0);
    if (d > 2) worse++;
    console.log(`  p${i}: ${CUR}=${x.over}  ${PREV}=${y.over}  diff=${d > 0 ? '+' + d : d}`);
  }
  console.log('比对照课更差的页数:', worse);
  await browser.close();
})();
