const { chromium } = require('playwright-core');
const path = require('path');

const rel = 'lessons/409-dang-ren-bu-rang-yu-shi/index.html';

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  await ctx.addInitScript(() => {
    try { localStorage.clear(); localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {}
  });
  const page = await ctx.newPage();
  await page.route('**/*', (r) => (r.request().url().startsWith('file://') ? r.continue() : r.abort()));

  const url = 'file:///' + path.resolve(__dirname, '..', rel).split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(700);

  const quiz = await page.evaluate(() => window.GUOXUE_QUIZ_OVERRIDE || []);
  console.log('题目数:', quiz.length);

  for (let i = 0; i < 9; i++) {
    await page.click('#nav-next');
    await page.waitForTimeout(90);
  }

  for (let i = 0; i < quiz.length; i++) {
    const text = quiz[i].opts[quiz[i].ans];
    const opt = page.locator(`#quiz-${i} .quiz-option`).filter({ hasText: text }).first();
    if (!(await opt.count())) { console.log(`Q${i + 1} 找不到选项「${text}」`); }
    else {
      await opt.click();
      await page.waitForTimeout(160);
      const ok = await page.evaluate((n) => {
        const el = document.querySelector(`[data-q="${n}"].correct`);
        return !!el;
      }, i);
      console.log(`Q${i + 1} 答「${text}」→ ${ok ? '正确' : '未标记正确'}`);
    }
    await page.click('#nav-next');
    await page.waitForTimeout(160);
  }

  console.log('indicator:', await page.textContent('#page-indicator'));
  const score = await page.evaluate(() => {
    const el = document.querySelector('#score-display');
    return el ? el.textContent.trim() : 'n/a';
  });
  const correct = await page.evaluate(() => {
    const el = document.querySelector('#correct-count');
    return el ? el.textContent.trim() : 'n/a';
  });
  console.log('SCORE=' + score, 'CORRECT=' + correct, '/10');

  await browser.close();
})();
