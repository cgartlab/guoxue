const { chromium } = require('playwright');
const PORT = process.env.PORT || 8899;
const ID = '414-ci-da-er-yi-yi';

(async () => {
  const browser = await chromium.launch();
  const results = [];
  for (const vp of [{ w: 1440, h: 900, n: 'desktop' }, { w: 390, h: 844, n: 'mobile' }]) {
    const page = await browser.newPage({ viewport: { width: vp.w, height: vp.h } });
    await page.addInitScript(() => { localStorage.setItem('guoxue_unlocked', '1'); });
    const errs = [];
    page.on('pageerror', e => errs.push(String(e)));
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await page.goto(`http://localhost:${PORT}/lessons/${ID}/index.html`, { waitUntil: 'networkidle' });

    const slides = await page.locator('.slide').count();
    const quizCards = await page.locator('#quiz-0:not(:empty)').count();
    const overflowing = await page.evaluate(() => {
      const out = [];
      document.querySelectorAll('.slide').forEach((s, i) => {
        const prev = s.classList.contains('active');
        s.classList.add('active');
        const r = s.getBoundingClientRect();
        if (s.scrollWidth > s.clientWidth + 2 || s.scrollHeight > s.clientHeight + 4) {
          out.push({ page: i, sw: s.scrollWidth, cw: s.clientWidth, sh: s.scrollHeight, ch: s.clientHeight });
        }
        if (!prev) s.classList.remove('active');
      });
      return out;
    });
    const indicator = await page.locator('#page-indicator').innerText();
    results.push({ vp: vp.n, slides, quizCards, indicator, errs, overflowing });
    await page.close();
  }
  // quiz 完整流程（desktop）
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.addInitScript(() => { localStorage.setItem('guoxue_unlocked', '1'); });
  await page.goto(`http://localhost:${PORT}/lessons/${ID}/index.html`, { waitUntil: 'networkidle' });
  let correct = 0;
  for (let i = 0; i < 10; i++) {
    await page.evaluate(() => window.goToPage && window.goToPage(9 + i));
    await page.waitForTimeout(120);
  }
  await page.evaluate(() => window.goToPage && window.goToPage(19));
  await page.waitForTimeout(300);
  const scoreText = await page.locator('#total-score').innerText().catch(() => 'n/a');
  results.push({ scorePageScore: scoreText });
  await page.close();
  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();
