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
  const slug = process.argv[2];
  const pages = (process.argv[3] || '2,3,4,5,6').split(',').map(Number);
  const abs = path.resolve(__dirname, '../lessons/' + slug + '/index.html');
  await p.goto('file:///' + abs.split(path.sep).join('/'), { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(600);
  const out = await p.evaluate((pages) => {
    const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
    const res = [];
    pages.forEach((i) => {
      slides.forEach((s) => s.classList.remove('active'));
      const el = slides[i];
      el.classList.add('active');
      const kids = Array.from(el.children).filter((c) => c.tagName === 'P' || c.tagName === 'H3');
      res.push({
        page: i,
        overflow: el.scrollHeight - el.clientHeight,
        kids: kids.map((c) => ({ tag: c.tagName, h: Math.round(c.getBoundingClientRect().height) })),
      });
    });
    return res;
  }, pages);
  out.forEach((r) => {
    console.log(`p${r.page} overflow=${r.overflow}  ` + r.kids.map((k) => `${k.tag}${k.h}`).join(' '));
  });
  await b.close();
})();
