const { chromium } = require('playwright-core');
const path = require('path');

const targets = [
  ['306', 'lessons/306-shan-ju-shi/index.html'],
  ['307', 'lessons/307-zi-shi-wei/index.html'],
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
    const url = 'file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/');
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);

    const rows = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((el, i) => {
        slides.forEach((s) => s.classList.remove('active'));
        el.classList.add('active');
        out.push({ page: el.getAttribute('data-page'), overflow: el.scrollHeight - el.clientHeight });
      });
      return out;
    });

    const bad = rows.filter((r) => r.overflow > 2);
    console.log(`=== ${label} === 共 ${rows.length} 页 | 溢出: ${bad.length ? bad.map((r) => `p${r.page}(+${r.overflow})`).join(' ') : '无'}`);
    console.log('逐页:', rows.map((r) => `p${r.page}:${r.overflow}`).join(' '));
  }

  await browser.close();
})();
