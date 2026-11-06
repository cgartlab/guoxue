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
  ['163', 'lessons/163-bu-zhi-er-zuo-zhi/index.html'],
  ['164', 'lessons/164-hu-xiang-tong-zi/index.html'],
  ['165', 'lessons/165-wo-yu-ren-si-ren-zhi-yi/index.html'],
  ['166', 'lessons/166-chen-si-bai-wen-zhao-gong/index.html'],
  ['167', 'lessons/167-yu-ren-ge-er-shan/index.html'],
  ['168', 'lessons/168-wen-mo-wu-you-ren/index.html'],
  ['169', 'lessons/169-ruo-sheng-yu-ren/index.html'],
  ['170', 'lessons/170-qiu-zhi-dao-jiu-yi/index.html'],
  ['171', 'lessons/171-she-ze-bu-xun/index.html'],
  ['172', 'lessons/172-jun-zi-tan-dang-dang/index.html'],
  ['173', 'lessons/173-wen-er-li/index.html'],
  ['174', 'lessons/174-tai-bo-san-rang/index.html'],
  ['175', 'lessons/175-gong-er-wu-li-ze-lao/index.html'],
  ['176', 'lessons/176-zeng-zi-you-ji/index.html'],
  ['177', 'lessons/177-zeng-zi-meng-jing-zi/index.html'],
  ['178', 'lessons/178-you-ruo-wu/index.html'],
  ['179', 'lessons/179-tuo-liu-chi-zhi-gu/index.html'],
  ['180', 'lessons/180-ren-zhong-er-dao-yuan/index.html'],
  ['181', 'lessons/181-xing-yu-shi-li-yu-yue/index.html'],
  ['182', 'lessons/182-min-ke-shi-you-zhi/index.html'],
  ['183', 'lessons/183-hao-yong-ji-pin/index.html'],
  ['184', 'lessons/184-zhou-gong-zhi-cai/index.html'],
  ['185', 'lessons/185-san-nian-xue/index.html'],
  ['186', 'lessons/186-du-xin-hao-xue/index.html'],
  ['187', 'lessons/187-bu-zai-qi-wei/index.html'],
  ['188', 'lessons/188-shi-zhi-zhi-shi/index.html'],
  ['189', 'lessons/189-kuang-er-bu-zhi/index.html'],
  ['190', 'lessons/190-xue-ru-bu-ji/index.html'],
  ['191', 'lessons/191-wei-wei-shun-yu/index.html'],
  ['192', 'lessons/192-da-zai-yao-wei-jun/index.html'],
  ['193', 'lessons/193-shun-you-chen-wu-ren/index.html'],
  ['194', 'lessons/194-yu-wu-jian-ran-yi/index.html'],
  ['195', 'lessons/195-zi-han-yan-li/index.html'],
  ['196', 'lessons/196-da-xiang-dang-ren/index.html'],
  ['197', 'lessons/197-ma-mian-bai-xia/index.html'],
  ['198', 'lessons/198-zi-jue-si/index.html'],
  ['199', 'lessons/199-zi-wei-yu-kuang/index.html'],
  ['200', 'lessons/200-tai-zai-wen-sheng/index.html'],
  ['201', 'lessons/201-wu-bu-shi-gu-yi/index.html'],
  ['202', 'lessons/202-wu-you-zhi-hu-zai/index.html'],
  ['203', 'lessons/203-feng-niao-bu-zhi/index.html'],
  ['204', 'lessons/204-zi-jian-zi-cui-zhe/index.html'],
  ['205', 'lessons/205-yang-zhi-mi-gao/index.html'],
  ['206', 'lessons/206-wu-shui-qi/index.html'],
  ['207', 'lessons/207-you-mei-yu-yu-si/index.html'],
  ['208', 'lessons/208-zi-yu-ju-jiu-yi/index.html'],
  ['209', 'lessons/209-wu-zi-wei-fan-lu/index.html'],
  ['210', 'lessons/210-chu-ze-shi-gong-qing/index.html'],
  ['211', 'lessons/211-shi-zhe-ru-si/index.html'],
  ['212', 'lessons/212-hao-de-ru-hao-se/index.html'],
  ['213', 'lessons/213-pi-ru-wei-shan/index.html'],
  ['214', 'lessons/214-yu-zhi-bu-duo/index.html'],
  ['215', 'lessons/215-miao-er-bu-xiu/index.html'],
  ['216', 'lessons/216-hou-sheng-ke-wei/index.html'],
  ['217', 'lessons/217-fa-yu-zhi-yan/index.html'],
  ['218', 'lessons/218-zhu-zhong-xin/index.html'],
  ['219', 'lessons/219-san-jun-ke-duo-shuai/index.html'],
  ['220', 'lessons/220-yi-bi-yun-pao/index.html'],
  ['221', 'lessons/221-sui-han-song-bai/index.html'],
  ['222', 'lessons/222-zhi-zhe-bu-huo/index.html'],
  ['223', 'lessons/223-ke-yu-gong-xue/index.html'],
  ['224', 'lessons/224-tang-di-zhi-hua/index.html'],
  ['225', 'lessons/225-kong-zi-yu-xiang-dang/index.html'],
  ['226', 'lessons/226-chao-yu-xia-da-fu-yan/index.html'],
  ['227', 'lessons/227-jun-zhao-shi-bin/index.html'],
  ['228', 'lessons/228-ru-gong-men/index.html'],
  ['229', 'lessons/229-zhi-gui/index.html'],
  ['230', 'lessons/230-jun-zi-bu-yi-gan-zou/index.html'],
  ['231', 'lessons/231-zhai-bi-you-ming-yi/index.html'],
  ['232', 'lessons/232-shi-bu-yan-jing/index.html'],
  ['233', 'lessons/233-ji-rou-you-qi/index.html'],
  ['234', 'lessons/234-shi-bu-yu-qin-bu-yan/index.html'],
  ['235', 'lessons/235-shu-shi-bi-ji/index.html'],
  ['236', 'lessons/236-xi-bu-zheng-bu-zuo/index.html'],
  ['237', 'lessons/237-zhang-zhe-chu-si-chu/index.html'],
  ['238', 'lessons/238-xiang-ren-nuo/index.html'],
  ['239', 'lessons/239-zai-bai-song-zhi/index.html'],
  ['240', 'lessons/240-kang-zi-kui-yao/index.html'],
  ['241', 'lessons/241-jiu-fen-wen-ren/index.html'],
  ['242', 'lessons/242-jun-ci-shi-zheng-xi-xian-chang/index.html'],
  ['243', 'lessons/243-ji-jun-shi-zhi/index.html'],
  ['244', 'lessons/244-jun-ming-zhao-bu-si-jia/index.html'],
  ['245', 'lessons/245-peng-you-si-yu-wo-bin/index.html'],
  ['246', 'lessons/246-peng-you-zhi-kui/index.html'],
  ['247', 'lessons/247-qin-bu-shi-ju-bu-ke/index.html'],
  ['248', 'lessons/248-jian-qi-cui-zhe/index.html'],
  ['249', 'lessons/249-sheng-che-zhi-sui/index.html'],
  ['250', 'lessons/250-shan-liang-ci-zhi/index.html'],
  ['251', 'lessons/251-xian-jin-yu-li-yue/index.html'],
  ['252', 'lessons/252-cong-wo-yu-chen-cai/index.html'],
  ['253', 'lessons/253-si-ke-shi-zhe/index.html'],
  ['254', 'lessons/254-hui-fei-zhu-wo/index.html'],
  ['255', 'lessons/255-xiao-zai-min-zi-qian/index.html'],
  ['256', 'lessons/256-nan-rong-san-fu-bai-gui/index.html'],
  ['257', 'lessons/257-ji-kang-zi-wen-hao-xue/index.html'],
  ['258', 'lessons/258-yan-yuan-si-tian-sang-yu/index.html'],
  ['259', 'lessons/259-yan-yuan-si-zi-ku-zhi-tong/index.html'],
  ['260', 'lessons/260-yan-yuan-si-men-ren-hou-zang/index.html'],
  ['261', 'lessons/261-wei-zhi-sheng-yan-zhi-si/index.html'],
  ['262', 'lessons/262-min-zi-shi-ce/index.html'],
  ['263', 'lessons/263-lu-ren-wei-chang-fu/index.html'],
  ['264', 'lessons/264-you-ye-sheng-tang-yi-wei-ru-yu-shi/index.html'],
  ['265', 'lessons/265-guo-you-bu-ji/index.html'],
  ['266', 'lessons/266-ming-gu-er-gong-zhi/index.html'],
  ['267', 'lessons/267-chai-ye-yu/index.html'],
  ['268', 'lessons/268-hui-ye-qi-shu-hu/index.html'],
  ['269', 'lessons/269-shan-ren-zhi-dao/index.html'],
  ['270', 'lessons/270-lun-du-shi-yu/index.html'],
  ['271', 'lessons/271-wen-si-xing-zhu/index.html'],
  ['272', 'lessons/272-zi-wei-yu-kuang/index.html'],
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
    if (process.argv[2] && label !== process.argv[2]) continue;
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
