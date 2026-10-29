const { chromium } = require('playwright-core');
const path = require('path');

const targets = [
  ['122', 'lessons/122-yan-yuan-ji-lu-shi/index.html'],
  ['123', 'lessons/123-shi-shi-zhi-yi/index.html'],
  ['124', 'lessons/124-yong-ye-ke-shi-nan-mian/index.html'],
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

  for (const [label, rel] of targets) {
    const url = 'file:///' + path.resolve(__dirname, '..', rel).replace(/\\/g, '/');
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);

    // 逐页强制 active 后测量自身滚动高度（与引擎状态解耦，只量版面）
    const rows = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((el, i) => {
        slides.forEach((s) => s.classList.remove('active'));
        el.classList.add('active');
        const cs = getComputedStyle(el);
        out.push({
          i,
          page: el.getAttribute('data-page'),
          sec: el.getAttribute('data-section'),
          overflow: el.scrollHeight - el.clientHeight,
          scrollH: el.scrollHeight,
          clientH: el.clientHeight,
          display: cs.display,
        });
      });
      return out;
    });

    const bad = rows.filter((r) => r.overflow > 2);
    console.log(`\n=== ${label} ===  共 ${rows.length} 页`);
    console.log('尺寸样例:', `clientH=${rows[1].clientH} display=${rows[1].display}`);
    console.log('溢出页:', bad.length ? bad.map((r) => `p${r.page}(+${r.overflow})`).join(' ') : '无');
    console.log('逐页:', rows.map((r) => `p${r.page}:${r.overflow}`).join(' '));
  }

  await browser.close();
})();
