const path = require('path');
const { chromium } = require('C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/node_modules/playwright-core');
(async () => {
  const browser = await chromium.launch({
    executablePath: 'C:/Users/Chenzhigang/AppData/Local/ms-playwright/chromium-1223/chrome-win64/chrome.exe',
    args: ['--no-proxy-server'],
  });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.addInitScript(() => {
    try { localStorage.setItem('guoxue_unlocked', '1'); } catch (e) {}
  });
  await page.route('**/*', (r) => r.request().url().startsWith('file://') ? r.continue() : r.abort());
  const url = 'file:///' + path.resolve(__dirname, '../index.html').split(path.sep).join('/');
  await page.goto(url, { waitUntil: 'load' });
  await page.waitForTimeout(1200);
  const cards = await page.locator('#lesson-cards .ds-lesson-card').count();
  const chips = await page.locator('.numstrip__chip, [class*="chip"]').count();
  const total = await page.locator('.home-sidebar__link--sub').count();
  const txt = await page.locator('body').innerText();
  const m = txt.match(/共\s*\d+\s*课/);
  const lastCard = await page.locator('#lesson-cards .ds-lesson-card').last().innerText().catch(() => '');
  console.log('cards', cards, '| sidebarSub', total, '| chips', chips, '|', m && m[0]);
  console.log('last card:', lastCard.replace(/\n/g, ' / ').slice(0, 90));
  await browser.close();
})();
