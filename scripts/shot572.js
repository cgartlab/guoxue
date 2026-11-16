const { chromium } = require('playwright-core');
const path = require('path');

const CHROME = 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe';
const REL = 'lessons/572-fan-shi-ren/index.html';

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, args: ['--no-proxy-server'] });
  const url = 'file:///' + path.resolve(__dirname, '..', REL).split(path.sep).join('/');

  // 桌面截图
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
  await page.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  await page.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(800);
  for (const i of [0, 1, 3, 4, 6, 7, 9]) {
    await page.evaluate((n) => {
      const s = document.querySelectorAll('.slide-container > .slide');
      s.forEach((x) => x.classList.remove('active'));
      s[n].classList.add('active');
    }, i);
    await page.waitForTimeout(250);
    await page.screenshot({ path: `scripts/s572-p${i}.png` });
  }
  await page.close();

  // 手机纵向溢出
  const m = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await m.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));
  await m.addInitScript(() => { try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {} });
  await m.goto(url, { waitUntil: 'domcontentloaded' });
  await m.waitForTimeout(800);
  const bad = await m.evaluate(() => {
    const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
    const out = [];
    slides.forEach((sl, i) => {
      slides.forEach((x) => x.classList.remove('active'));
      sl.classList.add('active');
      const over = sl.scrollHeight - sl.clientHeight;
      const wide = sl.scrollWidth - sl.clientWidth;
      if (over > 2 || wide > 2) out.push({ i, sec: sl.dataset.section, over, wide });
    });
    return out;
  });
  console.log('手机端溢出页:', JSON.stringify(bad));
  await m.evaluate(() => {
    const s = document.querySelectorAll('.slide-container > .slide');
    s.forEach((x) => x.classList.remove('active'));
    s[1].classList.add('active');
  });
  await m.waitForTimeout(250);
  await m.screenshot({ path: 'scripts/s572-mobile-p1.png' });
  await browser.close();
  console.log('done');
})();
