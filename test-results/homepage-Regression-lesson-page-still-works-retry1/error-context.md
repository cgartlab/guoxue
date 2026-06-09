# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: homepage.spec.js >> Regression >> lesson page still works
- Location: tests/homepage.spec.js:368:3

# Error details

```
Test timeout of 30000ms exceeded.
```

```
Error: page.goto: Test timeout of 30000ms exceeded.
Call log:
  - navigating to "http://localhost:7890/lessons/01-lunyu/index.html", waiting until "load"

```

# Test source

```ts
  269 | 
  270 |     const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
  271 |     const mengxueNav = page.locator('.home-sidebar__nav').filter({ hasText: '论语' }).first();
  272 | 
  273 |     // Initially hidden
  274 |     let isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
  275 |     expect(isHidden).toBe(true);
  276 | 
  277 |     // Click to expand
  278 |     await mengxueHeader.click();
  279 |     isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
  280 |     expect(isHidden).toBe(false);
  281 |     // toHaveClass does exact match, use evaluate instead
  282 |     let hasExpanded = await mengxueHeader.evaluate(el => el.classList.contains('is-expanded'));
  283 |     expect(hasExpanded).toBe(true);
  284 | 
  285 |     // Click to collapse
  286 |     await mengxueHeader.click();
  287 |     isHidden = await mengxueNav.evaluate(el => el.hasAttribute('hidden'));
  288 |     expect(isHidden).toBe(true);
  289 |     hasExpanded = await mengxueHeader.evaluate(el => el.classList.contains('is-expanded'));
  290 |     expect(hasExpanded).toBe(false);
  291 |   });
  292 | 
  293 |   test('click on ready discipline filters cards', async ({ page }) => {
  294 |     await page.goto(`http://localhost:${PORT}/`);
  295 | 
  296 |     // Click the "蒙学" category header first to expand
  297 |     const mengxueHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '蒙学' }).first();
  298 |     await mengxueHeader.click();
  299 | 
  300 |     // Then click the filter link
  301 |     const mengxueFilterLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '三字经 · 百家姓' }).first();
  302 |     await mengxueFilterLink.click({ noWaitAfter: true });
  303 | 
  304 |     const title = page.locator('#filter-title');
  305 |     await expect(title).toContainText('蒙学');
  306 | 
  307 |     // Should show 6 ready lessons in mengxue
  308 |     const cards = page.locator('#lesson-cards .ds-lesson-card');
  309 |     await expect(cards).toHaveCount(6);
  310 |   });
  311 | 
  312 |   test('click on coming discipline shows placeholder', async ({ page }) => {
  313 |     await page.goto(`http://localhost:${PORT}/`);
  314 | 
  315 |     // Expand 经部 first
  316 |     const jingHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '经部' }).first();
  317 |     await jingHeader.click();
  318 | 
  319 |     // Click filter link
  320 |     const jingFilterLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '儒家经典' }).first();
  321 |     await jingFilterLink.click({ noWaitAfter: true });
  322 | 
  323 |     const comingEl = page.locator('#coming-soon');
  324 |     await expect(comingEl).toBeVisible();
  325 |     await expect(comingEl).toContainText('经部');
  326 |     await expect(comingEl).toContainText('即将上线');
  327 | 
  328 |     const grid = page.locator('#lesson-cards');
  329 |     await expect(grid).toHaveAttribute('hidden');
  330 |   });
  331 | 
  332 |   test('click "全部课程" resets to all', async ({ page }) => {
  333 |     await page.goto(`http://localhost:${PORT}/`);
  334 | 
  335 |     // Expand and click 经部
  336 |     const jingHeader = page.locator('.home-sidebar__category-header').filter({ hasText: '经部' }).first();
  337 |     await jingHeader.click();
  338 |     const jingLink = page.locator('.home-sidebar__link--filter').filter({ hasText: '儒家经典' }).first();
  339 |     await jingLink.click({ noWaitAfter: true });
  340 |     await expect(page.locator('#coming-soon')).toBeVisible();
  341 | 
  342 |     // Click reset
  343 |     const allLink = page.locator('.home-sidebar__nav--all .home-sidebar__link').first();
  344 |     await allLink.click({ noWaitAfter: true });
  345 | 
  346 |     await expect(page.locator('#lesson-cards')).toBeVisible();
  347 |     await expect(page.locator('#filter-title')).toContainText('全部课程');
  348 |   });
  349 | });
  350 | 
  351 | // ===== 回归测试 =====
  352 | test.describe('Regression', () => {
  353 |   test.use({ viewport: { width: 1440, height: 900 } });
  354 | 
  355 |   test('about.html still works', async ({ page }) => {
  356 |     await page.goto(`http://localhost:${PORT}/about.html`);
  357 | 
  358 |     // About page should not use home-wrapper
  359 |     const hasHomeWrapper = await page.evaluate(() =>
  360 |       document.querySelector('.home-wrapper') !== null
  361 |     );
  362 |     expect(hasHomeWrapper).toBe(false);
  363 | 
  364 |     const title = page.locator('h1');
  365 |     await expect(title).toBeVisible();
  366 |   });
  367 | 
  368 |   test('lesson page still works', async ({ page }) => {
> 369 |     await page.goto(`http://localhost:${PORT}/lessons/01-lunyu/index.html`);
      |                ^ Error: page.goto: Test timeout of 30000ms exceeded.
  370 | 
  371 |     const hasHomeWrapper = await page.evaluate(() =>
  372 |       document.querySelector('.home-wrapper') !== null
  373 |     );
  374 |     expect(hasHomeWrapper).toBe(false);
  375 | 
  376 |     const slideViewport = page.locator('.slide-viewport');
  377 |     await expect(slideViewport).toBeVisible();
  378 |   });
  379 | 
  380 |   test('404.html still works', async ({ page }) => {
  381 |     await page.goto(`http://localhost:${PORT}/404.html`);
  382 | 
  383 |     const title = await page.title();
  384 |     expect(title).toMatch(/404|页面不存在/i);
  385 | 
  386 |     const heading = page.locator('h1');
  387 |     await expect(heading).toContainText('抱歉，这个页面不存在');
  388 | 
  389 |     const fourOhFour = page.locator('text=/^404$/');
  390 |     await expect(fourOhFour).toBeVisible();
  391 |   });
  392 | });
  393 | 
```