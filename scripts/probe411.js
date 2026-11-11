const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');

const targets = [
  ['410', 'lessons/410-zhen-er-bu-liang/index.html'],
  ['411', 'lessons/411-jing-qi-shi-hou-qi-shi/index.html'],
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
    await page.waitForTimeout(900);

    const rows = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((el) => {
        slides.forEach((s) => s.classList.remove('active'));
        el.classList.add('active');
        out.push({ page: el.getAttribute('data-page'), overflow: el.scrollHeight - el.clientHeight });
      });
      return out;
    });

    const quizCount = await page.evaluate(() => document.querySelectorAll('.slide[id^="quiz-"]:not(#quiz-score)').length);
    const quizRendered = await page.evaluate(() => document.querySelectorAll('#quiz-0 .quiz-option, #quiz-0 button').length);
    const bad = rows.filter((r) => r.overflow > 2);
    console.log(`=== ${label} === 共 ${rows.length} 页 | quiz页 ${quizCount} | 首题选项 ${quizRendered} | 溢出: ${bad.length ? bad.map((r) => `p${r.page}(+${r.overflow})`).join(' ') : '无'}`);
  }

  await browser.close();
})();
