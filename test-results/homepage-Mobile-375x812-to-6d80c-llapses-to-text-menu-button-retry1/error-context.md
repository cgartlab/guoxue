# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: homepage.spec.js >> Mobile (375x812) >> top nav collapses to text menu button
- Location: tests/homepage.spec.js:170:3

# Error details

```
Error: expect(locator).toBeVisible() failed

Locator: locator('#menu-toggle')
Expected: visible
Timeout: 5000ms
Error: element(s) not found

Call log:
  - Expect "toBeVisible" with timeout 5000ms
  - waiting for locator('#menu-toggle')

```

```yaml
- link "跳过导航":
  - /url: "#main-content"
- navigation "主导航":
  - link "国学课堂":
    - /url: index.html
  - button "展开课程目录": ☰
  - link "关于本站":
    - /url: about.html
- complementary "课程分类导航":
  - text: 课程导航
  - button "收起侧栏"
  - text: 📜 📚 💭 ✒️ 🌱 🖌️ 🎨 🌿 🥋 🏮 🎵 ♟️
- main:
  - paragraph: 传承经典 · 启迪智慧
  - heading "国学课堂 · 系列课程总览" [level=1]
  - paragraph: 涵盖经史子集 · 蒙学书法国画等十二门类
  - text: 6 已上线课程 0 筹备中 12 学科门类
  - link "浏览课程 ↓":
    - /url: "#lesson-cards"
  - heading "全部课程" [level=2]
  - link "📖 小学中高年级 《论语》国学问答 传承经典 · 启迪智慧 · 约 15 分钟 走近孔子,理解仁、学、孝、礼四大核心思想,精读六句千古名言,配套十道互动测验。 开始学习 →":
    - /url: lessons/01-lunyu/index.html
    - text: 📖 小学中高年级
    - heading "《论语》国学问答" [level=3]
    - paragraph: 传承经典 · 启迪智慧
    - text: · 约 15 分钟
    - paragraph: 走近孔子,理解仁、学、孝、礼四大核心思想,精读六句千古名言,配套十道互动测验。
    - text: 开始学习 →
  - link "📚 小学高年级 / 初中 《论语》问答课件 · 混合版 拓展版 · 内容更详尽 在标准版基础上拓展内容深度,适合学有余力的学生深入研读。 开始学习 →":
    - /url: lessons/01-lunyu-mixed/index.html
    - text: 📚 小学高年级 / 初中
    - heading "《论语》问答课件 · 混合版" [level=3]
    - paragraph: 拓展版 · 内容更详尽
    - paragraph: 在标准版基础上拓展内容深度,适合学有余力的学生深入研读。
    - text: 开始学习 →
  - link "📜 小学低中年级 《三字经》国学启蒙 人之初 · 性本善 · 约 15 分钟 走进\"三百千\"之首,从开篇哲学到教育之道,从孝悌故事到历史长河,在朗朗书声中收获成长。 开始学习 →":
    - /url: lessons/02-sanzijing/index.html
    - text: 📜 小学低中年级
    - heading "《三字经》国学启蒙" [level=3]
    - paragraph: 人之初 · 性本善
    - text: · 约 15 分钟
    - paragraph: 走进"三百千"之首,从开篇哲学到教育之道,从孝悌故事到历史长河,在朗朗书声中收获成长。
    - text: 开始学习 →
  - link "🌱 小学中高年级 《学而》三问 学而时习 · 君子之道 · 约 12 分钟 深入解读《论语·学而》开篇三问：学而时习、有朋远来、人不知愠，理解君子修养的三重境界。 开始学习 →":
    - /url: lessons/02-xueer/index.html
    - text: 🌱 小学中高年级
    - heading "《学而》三问" [level=3]
    - paragraph: 学而时习 · 君子之道
    - text: · 约 12 分钟
    - paragraph: 深入解读《论语·学而》开篇三问：学而时习、有朋远来、人不知愠，理解君子修养的三重境界。
    - text: 开始学习 →
  - link "🌿 小学中高年级 孝悌为仁之本 学而第二章 · 有子曰 · 约 10 分钟 《论语·学而》第二章名句解读：孝悌是仁的根本，君子务本，本立而道生。配套十道互动测验。 开始学习 →":
    - /url: lessons/03-xueer-xiaoti/index.html
    - text: 🌿 小学中高年级
    - heading "孝悌为仁之本" [level=3]
    - paragraph: 学而第二章 · 有子曰
    - text: · 约 10 分钟
    - paragraph: 《论语·学而》第二章名句解读：孝悌是仁的根本，君子务本，本立而道生。配套十道互动测验。
    - text: 开始学习 →
  - link "🔄 小学中高年级 曾子三省 吾日三省吾身 · 约 12 分钟 《论语·学而》第四章精讲：吾日三省吾身——为人谋而不忠乎？与朋友交而不信乎？传不习乎？配套十道互动测验。 开始学习 →":
    - /url: lessons/04-zengzi-sansheng/index.html
    - text: 🔄 小学中高年级
    - heading "曾子三省" [level=3]
    - paragraph: 吾日三省吾身
    - text: · 约 12 分钟
    - paragraph: 《论语·学而》第四章精讲：吾日三省吾身——为人谋而不忠乎？与朋友交而不信乎？传不习乎？配套十道互动测验。
    - text: 开始学习 →
- contentinfo:
  - text: © 2026
  - link "八〇二三老战士":
    - /url: https://8023laozhanshi.cc/
  - text: · 国学课堂 · Powered by GitHub Pages
```

# Test source

```ts
  74  |     await expect(stats).toHaveCount(3); // 已上线 / 筹备中 / 门类
  75  |   });
  76  | 
  77  |   test('top nav menu shows pure text (no emoji)', async ({ page }) => {
  78  |     await page.goto(`http://localhost:${PORT}/`);
  79  | 
  80  |     // 主菜单项(首页/课程/门类)
  81  |     const menuLinks = page.locator('.ds-navbar__menu .ds-btn-nav--ghost');
  82  |     await expect(menuLinks).toHaveCount(3);
  83  | 
  84  |     // 品牌链接
  85  |     const brand = page.locator('.ds-btn-nav--brand');
  86  |     await expect(brand).toHaveText('国学课堂');
  87  | 
  88  |     // 菜单切换按钮(桌面端可见,文字"菜单")
  89  |     const menuToggle = page.locator('#menu-toggle .ds-btn-nav__text');
  90  |     await expect(menuToggle).toHaveText('菜单');
  91  | 
  92  |     // 抽屉切换按钮(桌面端可见,文字"目录")
  93  |     const drawerToggle = page.locator('#drawer-toggle .ds-btn-nav__text');
  94  |     await expect(drawerToggle).toHaveText('目录');
  95  |   });
  96  | 
  97  |   test('sidebar renders 12 collapsible categories (default collapsed)', async ({ page }) => {
  98  |     await page.goto(`http://localhost:${PORT}/`);
  99  | 
  100 |     const groups = page.locator('.home-sidebar__group');
  101 |     await expect(groups).toHaveCount(12);
  102 | 
  103 |     // Category headers visible
  104 |     const headers = page.locator('.home-sidebar__category-header');
  105 |     await expect(headers).toHaveCount(12);
  106 | 
  107 |     // Sub navs should be hidden by default
  108 |     const subNavs = page.locator('.home-sidebar__nav:not(.home-sidebar__nav--all)');
  109 |     for (let i = 0; i < await subNavs.count(); i++) {
  110 |       const nav = subNavs.nth(i);
  111 |       const isHidden = await nav.evaluate(el => el.hasAttribute('hidden'));
  112 |       expect(isHidden).toBe(true);
  113 |     }
  114 | 
  115 |     // "全部课程" reset link visible
  116 |     const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
  117 |     await expect(allLink).toBeVisible();
  118 |     await expect(allLink).toContainText('全部课程');
  119 |   });
  120 | 
  121 |   test('search box renders with L2 styling', async ({ page }) => {
  122 |     await page.goto(`http://localhost:${PORT}/`);
  123 | 
  124 |     const searchInput = page.locator('#sidebar-search');
  125 |     await expect(searchInput).toBeVisible();
  126 |     await expect(searchInput).toHaveAttribute('placeholder', '搜索课程…');
  127 |   });
  128 | 
  129 |   test('lesson cards render correctly', async ({ page }) => {
  130 |     await page.goto(`http://localhost:${PORT}/`);
  131 | 
  132 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  133 |     await expect(cards).toHaveCount(6);
  134 | 
  135 |     const firstCard = cards.first();
  136 |     await expect(firstCard.locator('.lesson-title')).toContainText('论语');
  137 |   });
  138 | 
  139 |   test('series cover stats show correct counts', async ({ page }) => {
  140 |     await page.goto(`http://localhost:${PORT}/`);
  141 | 
  142 |     const values = page.locator('.series-stat__value');
  143 |     const vals = await values.allTextContents();
  144 |     // 6 ready lessons, 0 coming lessons, 12 categories
  145 |     expect(vals[0]).toBe('6'); // 已上线
  146 |     expect(vals[1]).toBe('0'); // 筹备中
  147 |     expect(vals[2]).toBe('12'); // 门类
  148 |   });
  149 | });
  150 | 
  151 | // ===== 平板测试 (768x1024) =====
  152 | test.describe('Tablet (768x1024)', () => {
  153 |   test.use({ viewport: { width: 768, height: 1024 } });
  154 | 
  155 |   test('sidebar visible, cards in 2 columns', async ({ page }) => {
  156 |     await page.goto(`http://localhost:${PORT}/`);
  157 | 
  158 |     const sidebar = page.locator('.home-sidebar');
  159 |     await expect(sidebar).toBeVisible();
  160 | 
  161 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  162 |     await expect(cards).toHaveCount(6);
  163 |   });
  164 | });
  165 | 
  166 | // ===== 移动端测试 (375x812) =====
  167 | test.describe('Mobile (375x812)', () => {
  168 |   test.use({ viewport: { width: 375, height: 812 } });
  169 | 
  170 |   test('top nav collapses to text menu button', async ({ page }) => {
  171 |     await page.goto(`http://localhost:${PORT}/`);
  172 | 
  173 |     const toggle = page.locator('#menu-toggle');
> 174 |     await expect(toggle).toBeVisible();
      |                          ^ Error: expect(locator).toBeVisible() failed
  175 |     // 移动端只显示图标(无文字)
  176 |     const menuToggleText = page.locator('#menu-toggle .ds-btn-nav__text');
  177 |     const isVisible = await menuToggleText.isVisible();
  178 |     expect(isVisible).toBe(false);
  179 | 
  180 |     const menu = page.locator('#primary-menu');
  181 |     const hasOpenClass = await menu.evaluate(el => el.classList.contains('is-open'));
  182 |     expect(hasOpenClass).toBe(false);
  183 | 
  184 |     await toggle.click();
  185 |     await expect(menu).toHaveClass(/is-open/);
  186 |     await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  187 | 
  188 |     await toggle.click();
  189 |     await expect(menu).not.toHaveClass(/is-open/);
  190 |     await expect(toggle).toHaveAttribute('aria-expanded', 'false');
  191 |   });
  192 | 
  193 |   test('drawer toggle button visible on mobile', async ({ page }) => {
  194 |     await page.goto(`http://localhost:${PORT}/`);
  195 | 
  196 |     const drawerBtn = page.locator('#drawer-toggle');
  197 |     await expect(drawerBtn).toBeVisible();
  198 | 
  199 |     // Sidebar hidden by default on mobile (transform: translateX(-100%) → matrix with negative tx)
  200 |     const sidebar = page.locator('.home-sidebar');
  201 |     const transform = await sidebar.evaluate(el => getComputedStyle(el).transform);
  202 |     // matrix(1, 0, 0, 1, -260, 0) means translateX(-260px)
  203 |     expect(transform).toMatch(/-\d+/);
  204 | 
  205 |     // Click drawer to open
  206 |     await drawerBtn.click();
  207 |     const isOpen = await sidebar.evaluate(el => el.classList.contains('is-open'));
  208 |     expect(isOpen).toBe(true);
  209 | 
  210 |     // 抽屉打开后,按钮文字变成"收起"
  211 |     const text = page.locator('#drawer-toggle .ds-btn-nav__text');
  212 |     // 移动端文字隐藏(只显示图标),所以通过 JS 检查
  213 |     const textContent = await text.evaluate(el => el.textContent);
  214 |     expect(textContent).toBe('收起');
  215 |   });
  216 | 
  217 |   test('search box hidden on mobile when drawer closed', async ({ page }) => {
  218 |     await page.goto(`http://localhost:${PORT}/`);
  219 | 
  220 |     const searchBox = page.locator('.search-box');
  221 |     const sidebar = page.locator('.home-sidebar');
  222 | 
  223 |     // When drawer is closed (sidebar off-canvas), search box should not be interactable
  224 |     const drawerClosed = await sidebar.evaluate(el => !el.classList.contains('is-open'));
  225 |     expect(drawerClosed).toBe(true);
  226 | 
  227 |     // Open drawer
  228 |     const drawerBtn = page.locator('#drawer-toggle');
  229 |     await drawerBtn.click();
  230 | 
  231 |     // Now search box should be visible inside the opened drawer
  232 |     const isOpen = await sidebar.evaluate(el => el.classList.contains('is-open'));
  233 |     expect(isOpen).toBe(true);
  234 |     await expect(searchBox).toBeVisible();
  235 |   });
  236 | 
  237 |   test('cards render in single column on mobile', async ({ page }) => {
  238 |     await page.goto(`http://localhost:${PORT}/`);
  239 | 
  240 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  241 |     await expect(cards).toHaveCount(6);
  242 |   });
  243 | });
  244 | 
  245 | // ===== 交互测试 =====
  246 | test.describe('Interactions', () => {
  247 |   test.use({ viewport: { width: 1440, height: 900 } });
  248 | 
  249 |   test('sidebar search filters sidebar links', async ({ page }) => {
  250 |     await page.goto(`http://localhost:${PORT}/`);
  251 | 
  252 |     // 先展开所有门类,让所有链接可见(默认是折叠的)
  253 |     const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link');
  254 |     await allLink.click({ noWaitAfter: true });
  255 |     await page.waitForTimeout(200);
  256 | 
  257 |     const searchInput = page.locator('#sidebar-search');
  258 |     await searchInput.fill('诗书');
  259 | 
  260 |     const jingLink = page.locator('.home-sidebar__link').filter({ hasText: '儒家经典' }).first();
  261 |     await expect(jingLink).toBeVisible();
  262 | 
  263 |     const mengxueDescLink = page.locator('.home-sidebar__link').filter({ hasText: '三字经 · 百家姓' }).first();
  264 |     await expect(mengxueDescLink).toBeHidden();
  265 |   });
  266 | 
  267 |   test('click category header expands/collapses sub-items', async ({ page }) => {
  268 |     await page.goto(`http://localhost:${PORT}/`);
  269 | 
  270 |     const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
  271 |     const mengxueNav = page.locator('.home-sidebar__nav').filter({ hasText: '论语' }).first();
  272 | 
  273 |     // Initially hidden
  274 |     let isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
```