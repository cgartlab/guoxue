const { chromium } = require('playwright-core');
const path = require('path');

const targets = [
  ['516', 'lessons/516-zi-xi-nong/index.html'],
  ['517', 'lessons/517-xia-you-yu/index.html'],
];

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.route('**/*', (route) => {
    const u = route.request().url();
    if (u.startsWith('file://')) return route.continue();
    return route.abort();
  });
  page.setDefaultTimeout(5000);

  const all = {};
  for (const [label, rel] of targets) {
    const url = 'file:///' + path.resolve(__dirname, '..', rel).replace(/\\/g, '/');
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);
    const rows = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((el, i) => {
        slides.forEach((s) => s.classList.remove('active'));
        el.classList.add('active');
        out.push({ i, page: el.getAttribute('data-page'), overflow: el.scrollHeight - el.clientHeight });
      });
      return out;
    });
    all[label] = rows;
    const bad = rows.filter(r => r.overflow > 2);
    console.log(`\n=== ${label} === 共 ${rows.length} 页`);
    console.log('逐页:', rows.map(r => `p${r.page}:${r.overflow}`).join(' '));
    console.log('溢出页(>2):', bad.length ? bad.map(r => `p${r.page}(+${r.overflow})`).join(' ') : '无');
  }

  const a = all['516'], b = all['517'];
  console.log('\n=== 516 vs 517 逐页溢出差 ===');
  let maxdiff = 0;
  for (let i = 0; i < a.length; i++) {
    const d = b[i].overflow - a[i].overflow;
    if (d !== 0) { console.log(`p${a[i].page}: 516=${a[i].overflow} 517=${b[i].overflow} diff=${d}`); maxdiff = Math.max(maxdiff, Math.abs(d)); }
  }
  console.log(maxdiff === 0 ? '完全一致 ✓ (所有页溢出差为0)' : `最大差异=${maxdiff}px ✗`);
  await browser.close();
})();
