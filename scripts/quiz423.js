const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');

(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.addInitScript(() => {
    try {
      localStorage.setItem('guoxue_unlocked', '1');
      localStorage.setItem('guoxue_unlock_code', 'SCREENSHOT-LOCAL');
    } catch (e) {}
  });
  await page.route('**/*', (r) => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  const url = 'file:///' + path.resolve(__dirname, '../lessons/423-jun-zi-you-san-wei/index.html').split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(800);

  // 真翻页：点「测验」标签进入第一题
  await page.locator('.ds-tab[data-section="quiz"]').click();
  await page.waitForTimeout(400);

  // 测验说明页 → 第一题
  await page.locator('#nav-next').click();
  await page.waitForTimeout(300);

  for (let i = 0; i < 10; i++) {
    const slid = page.locator('#quiz-' + i);
    const opts = slid.locator('.quiz-option');
    const cnt = await opts.count();
    if (cnt === 0) { console.log('第 ' + (i + 1) + ' 题未渲染'); break; }
    // 选项在引擎里被随机打乱，按正确答案文本点选
    const right = await page.evaluate((k) => {
      const it = window.GUOXUE_QUIZ_OVERRIDE[k];
      return it.opts[it.ans];
    }, i);
    let hit = -1;
    for (let j = 0; j < cnt; j++) {
      const t = await opts.nth(j).innerText();
      if (t.replace(/\s/g, '').includes(right.replace(/\s/g, ''))) { hit = j; break; }
    }
    if (hit < 0) { console.log('第 ' + (i + 1) + ' 题未匹配到正确答案：' + right); }
    await opts.nth(hit < 0 ? 0 : hit).click();
    await page.waitForTimeout(180);
    await page.locator('#nav-next').click();
    await page.waitForTimeout(220);
  }

  // 走完得分页
  await page.waitForTimeout(400);
  const score = await page.locator('#total-score').textContent();
  const correct = await page.locator('#correct-count').textContent();
  const msg = await page.locator('#score-message').textContent();
  const indicator = await page.locator('#page-indicator').textContent();
  console.log(`得分 ${score} / 100 | 答对 ${correct} / 10 | ${msg} | 页码 ${indicator}`);

  await browser.close();
})();
