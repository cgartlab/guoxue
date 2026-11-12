const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');
const targets = [
  ['430', 'lessons/430-yang-huo-yu-jian-kong-zi/index.html'],
  ['431', 'lessons/431-xing-xiang-jin-xi-xiang-yuan/index.html'],
];
(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.route('**/*', (r) => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  await page.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  for (const [id, rel] of targets) {
    await page.goto('file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/'), { waitUntil: 'load' });
    await page.waitForTimeout(800);
    const data = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      slides.forEach((s) => s.classList.remove('active'));
      const s = slides[22];
      s.classList.add('active');
      const kids = Array.from(s.children).map((k) => ({ tag: k.tagName, h: Math.round(k.getBoundingClientRect().height), t: (k.textContent || '').trim().slice(0, 16) }));
      return { overflow: s.scrollHeight - s.clientHeight, client: s.clientHeight, scroll: s.scrollHeight, kids };
    });
    console.log('=== ' + id + ' === overflow ' + data.overflow + ' (client ' + data.client + ' scroll ' + data.scroll + ')');
    data.kids.forEach((k, i) => console.log('  ' + i + ' ' + k.tag + ' h=' + k.h + '  ' + k.t));
  }
  await browser.close();
})();
