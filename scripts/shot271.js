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
  const abs = path.resolve(__dirname, '../lessons/271-wen-si-xing-zhu/index.html');
  const url = 'file:///' + abs.split(path.sep).join('/');
  await p.goto(url, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(900);

  // 溢出检测：逐页激活，量内容高度
  const report = await p.evaluate(async () => {
    const s = [...document.querySelectorAll('.slide-container > .slide')];
    const out = [];
    for (let i = 0; i < s.length; i++) {
      s.forEach((x) => x.classList.remove('active'));
      s[i].classList.add('active');
      await new Promise((r) => setTimeout(r, 60));
      const el = s[i];
      const over = el.scrollHeight - el.clientHeight;
      out.push({ i, sh: el.scrollHeight, ch: el.clientHeight, over });
    }
    return out;
  });
  const bad = report.filter((r) => r.over > 4);
  console.log('总页数:', report.length);
  console.log('溢出页:', bad.length ? JSON.stringify(bad) : '无');
  console.log(report.map((r) => `${r.i}:${r.sh}/${r.ch}`).join('  '));

  for (const i of [0, 1, 3, 7, 20, 22]) {
    await p.evaluate((n) => {
      const s = document.querySelectorAll('.slide-container > .slide');
      s.forEach((x) => x.classList.remove('active'));
      s[n].classList.add('active');
    }, i);
    await p.waitForTimeout(250);
    await p.screenshot({ path: `C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站/test-results/l271-${i}.png` });
  }
  await b.close();
  console.log('shots ok');
})();
