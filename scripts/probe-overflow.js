const { chromium } = require('playwright-core');
const path = require('path');

const targets = [
  ['122', 'lessons/122-yan-yuan-ji-lu-shi/index.html'],
  ['123', 'lessons/123-shi-shi-zhi-yi/index.html'],
  ['124', 'lessons/124-yong-ye-ke-shi-nan-mian/index.html'],
  ['125', 'lessons/125-ai-gong-wen-hao-xue/index.html'],
  ['126', 'lessons/126-zhou-ji-bu-ji-fu/index.html'],
  ['127', 'lessons/127-li-niu-zhi-zi/index.html'],
  ['128', 'lessons/128-hui-ye-san-yue-bu-wei-ren/index.html'],
  ['129', 'lessons/129-ji-kang-zi-wen-cong-zheng/index.html'],
  ['130', 'lessons/130-ji-shi-shi-min-zi-qian/index.html'],
  ['131', 'lessons/131-bo-niu-you-ji/index.html'],
  ['132', 'lessons/132-xian-zai-hui-ye/index.html'],
  ['133', 'lessons/133-yuan-si-wei-zhi-zai/index.html'],
  ['134', 'lessons/134-xi-hu-wu-jian-qi-jin/index.html'],
  ['135', 'lessons/135-li-bu-zu-zhong-dao-er-fei/index.html'],
  ['136', 'lessons/136-jun-zi-ru-xiao-ren-ru/index.html'],
  ['137', 'lessons/137-zi-you-wei-wu-cheng-zai/index.html'],
  ['138', 'lessons/138-meng-zhi-fan-bu-fa/index.html'],
  ['139', 'lessons/139-bu-you-zhu-tuo-zhi-ning/index.html'],
  ['140', 'lessons/140-shui-neng-chu-bu-you-hu/index.html'],
  ['141', 'lessons/141-ren-zhi-sheng-ye-zhi/index.html'],
  ['142', 'lessons/142-zhi-zhi-zhe-bu-ru-hao-zhi-zhe/index.html'],
  ['143', 'lessons/143-zhong-ren-yi-shang-ke-yi-yu-shang/index.html'],
  ['144', 'lessons/144-fan-chi-wen-zhi-wu-min-zhi-yi/index.html'],
  ['145', 'lessons/145-zhi-zhe-le-shui-ren-zhe-le-shan/index.html'],
  ['146', 'lessons/146-qi-yi-bian-zhi-yu-lu/index.html'],
  ['147', 'lessons/147-gu-bu-gu-gu-zai-gu-zai/index.html'],
  ['148', 'lessons/148-zai-wo-wen-jing-you-ren/index.html'],
  ['149', 'lessons/149-jun-zi-bo-xue-yu-wen/index.html'],
  ['150', 'lessons/150-zi-jian-nan-zi/index.html'],
  ['151', 'lessons/151-zhi-sheng-wen-ze-ye/index.html'],
  ['152', 'lessons/152-zhong-yong-zhi-wei-de/index.html'],
  ['153', 'lessons/153-bo-shi-yu-min/index.html'],
  ['154', 'lessons/154-shu-er-bu-zuo/index.html'],
  ['155', 'lessons/155-mo-er-shi-zhi/index.html'],
  ['156', 'lessons/156-de-zhi-bu-xiu/index.html'],
  ['157', 'lessons/157-zhi-yu-dao-ju-yu-de/index.html'],
  ['158', 'lessons/158-tian-sheng-de-yu-yu/index.html'],
  ['159', 'lessons/159-er-san-zi-yi-wo-wei-yin/index.html'],
  ['160', 'lessons/160-zi-yi-si-jiao/index.html'],
  ['161', 'lessons/161-sheng-ren-wu-bu-de-er-jian/index.html'],
  ['162', 'lessons/162-diao-er-bu-gang/index.html'],
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
    const url = 'file:///' + path.resolve(__dirname, '..', rel).replace(/\\/g, '/');
    await page.goto(url, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(800);

    // 逐页强制 active 后测量自身滚动高度（与引擎状态解耦，只量版面）
    const rows = await page.evaluate(() => {
      const slides = Array.from(document.querySelectorAll('.slide-container > .slide'));
      const out = [];
      slides.forEach((el, i) => {
        slides.forEach((s) => s.classList.remove('active'));
        el.classList.add('active');
        const cs = getComputedStyle(el);
        out.push({
          i,
          page: el.getAttribute('data-page'),
          sec: el.getAttribute('data-section'),
          overflow: el.scrollHeight - el.clientHeight,
          scrollH: el.scrollHeight,
          clientH: el.clientHeight,
          display: cs.display,
        });
      });
      return out;
    });

    const bad = rows.filter((r) => r.overflow > 2);
    console.log(`\n=== ${label} ===  共 ${rows.length} 页`);
    console.log('尺寸样例:', `clientH=${rows[1].clientH} display=${rows[1].display}`);
    console.log('溢出页:', bad.length ? bad.map((r) => `p${r.page}(+${r.overflow})`).join(' ') : '无');
    console.log('逐页:', rows.map((r) => `p${r.page}:${r.overflow}`).join(' '));
  }

  await browser.close();
})();
