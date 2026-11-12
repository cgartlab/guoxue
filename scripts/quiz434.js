const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');

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
  page.setDefaultTimeout(8000);
  const errors = [];
  page.on('pageerror', (e) => errors.push(String(e)));

  await page.addInitScript(() => localStorage.setItem('guoxue_unlocked', '1'));
  const url = 'file:///' + path.resolve(__dirname, '..', 'lessons/434-gong-shan-fu-rao-yi-fei-pan/index.html').split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(900);

  const expected = await page.evaluate(() => window.GUOXUE_QUIZ_OVERRIDE.map((q) => q.opts[q.ans]));
  const answers = await page.evaluate(() => window.GUOXUE_QUIZ_OVERRIDE.map((q) => q.ans));

  await page.click('.ds-tab[data-section="quiz"]');
  await page.waitForTimeout(600);
  await page.click('#nav-next');
  await page.waitForTimeout(600);


  const picked = [];
  for (let i = 0; i < expected.length; i++) {
    const idx = answers[i];
    const text = expected[i];
    const btns = page.locator('.slide.active .quiz-option');
    const n = await btns.count();
    let hit = -1;
    for (let k = 0; k < n; k++) {
      const t = (await btns.nth(k).innerText()).trim().split(/\r?\n/).pop().trim();
      if (t === text) { hit = k; break; }
    }
    if (hit < 0) { picked.push(`Q${i + 1}:未匹配到「${text}」`); }
    else { await btns.nth(hit).click(); picked.push(`Q${i + 1}:ok`); }
    await page.waitForTimeout(450);
    await page.click('#nav-next');
    await page.waitForTimeout(450);
  }

  const score = await page.locator('#score-display').innerText().catch(() => 'n/a');
  const total = await page.locator('#total-score').innerText().catch(() => 'n/a');
  const correct = await page.locator('#correct-count').innerText().catch(() => 'n/a');
  const msg = await page.locator('#score-message').innerText().catch(() => 'n/a');
  console.log(`得分 ${score} 分 | 答对 ${correct}/10 | 合计 ${total}`);
  console.log('评语：' + msg);
  console.log(picked.join(' '));
  console.log(errors.length ? 'JS 报错: ' + errors.join(' | ') : 'JS 报错: 无');
  await browser.close();
})();
