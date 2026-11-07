const { chromium } = require('playwright-core');
const path = require('path');

const targets = [
  ['284', 'lessons/284-bai-xing-zu/index.html'],
  ['285', 'lessons/285-qi-jing-gong-wen-zheng/index.html'],
  ['286', 'lessons/286-pian-yan-zhe-yu/index.html'],
  ['292', 'lessons/292-gou-zi-zhi-bu-yu/index.html'],
  ['293', 'lessons/293-zi-wei-zheng-yan-yong-sha/index.html'],
  ['294', 'lessons/294-zi-zhang-wen-da/index.html'],
  ['295', 'lessons/295-chong-de-xiu-te-bian-huo/index.html'],
  ['296', 'lessons/296-ai-ren-zhi-ren/index.html'],
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
