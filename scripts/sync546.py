#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync546: 第 546 课《亲爱我，孝何难》，同步四处
（manifest / index / tests / sitemap）。
本课是弟子规课堂第一课收费：freePrefixes 只到 545-，546 不再加前缀（unlock.js 不动）。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:26]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True

# ---------- 1) manifest（CRLF） ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '546-qin-ai-wo'," + SEP +
    "        num: '546'," + SEP +
    "        title: '亲爱我 · 孝何难、孝方贤'," + SEP +
    "        subtitle: '《弟子规》入则孝第五段：亲爱我，孝何难'," + SEP +
    "        path: 'lessons/546-qin-ai-wo/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第六课，入则孝第五段。原文「亲爱我，孝何难。亲憎我，孝方贤。亲有过，谏使更。怡吾色，柔吾声。」讲两层：父母疼我，孝顺不算难；父母不疼我还能尽孝，才见修养。父母有了过错，做子女的要劝，但劝要有法子——脸色和缓、声音柔和，让父母听得进去、改得过来。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'dizigui'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }" + SEP + "];"
)
s, good = once(s, old, "manifest 末条", new)
ok = ok and good
if good:
    write(p, s); print("  [OK] manifest: 插入 546 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 545 课", "index 共N课", "共 546 课")
n = s.count("yaoyue545")
if n:
    s = s.replace("yaoyue545", "yaoyue546"); print(f"  [OK] index: yaoyue545 -> yaoyue546 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue545"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 545 lessons (num 01..545, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 546 lessons (num 01..546, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 545 in total)", "tests 头注释2", "(flat sorted chips, 546 in total)")
s, g2 = once(s, "series cover stats show correct counts (545/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (546/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('545'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('546'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 545 lesson cards'", "tests 平板用例名", "test('sidebar visible, 546 lesson cards'")
s, g5 = once(s, "numstrip visible with 545 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 546 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=5（合计 545）", "tests chip 注释", "弟子规课堂=6（合计 546）")
s, g7 = once(s, "8, 1, 47, 5];", "tests chip 数组", "8, 1, 47, 6];")
s = s.replace("// 全部 545 个序号 chip", "// 全部 546 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 545", "tests 末组注释", "末组「弟子规课堂」末项 = 546")
n_cards = s.count("toHaveCount(545)")
s = s.replace("toHaveCount(545)", "toHaveCount(546)")
s = s.replace("toHaveText('545')", "toHaveText('546')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 545 -> 546 共 {n_cards} 处 toHaveCount")

# ---------- 3b) paywall.spec.js：固化弟子规免费边界（541-545 免费，546 起收费） ----------
p = f"{ROOT}/tests/paywall.spec.js"
s = read(p)
anchor = """    const isFree = await page.evaluate(() => window.UNLOCK.isCourseFree('501-yue-chun-xia'));
    expect(isFree).toBe(false);
  });
"""
add = anchor + """
  test('弟子规课堂免费段末课(545):不弹窗,可直接学习', async ({ page }) => {
    await page.goto(`${BASE}/lessons/545-qin-suo-hao/index.html`, { waitUntil: 'domcontentloaded' });

    await expect(page.locator('.paywall-overlay--show')).toHaveCount(0);
    await expect(page.locator('#page-indicator')).toHaveText('1 / 24');
    await expect(page.locator('#quiz-0 .quiz-option').first()).toBeAttached();

    const isFree = await page.evaluate(() => window.UNLOCK.isCourseFree('545-qin-suo-hao'));
    expect(isFree).toBe(true);
  });

  test('弟子规课堂 546 课起付费:弹窗出现且引擎不初始化', async ({ page }) => {
    await page.goto(`${BASE}/lessons/546-qin-ai-wo/index.html`, { waitUntil: 'domcontentloaded' });

    await expect(page.locator('.paywall-overlay--show')).toBeVisible();
    await expect(page.locator('#quiz-0 .quiz-option')).toHaveCount(0);

    const isFree = await page.evaluate(() => window.UNLOCK.isCourseFree('546-qin-ai-wo'));
    expect(isFree).toBe(false);
  });
"""
s, gpay = once(s, anchor, "paywall 边界用例锚点", add)
ok = ok and gpay
write(p, s)

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/546-qin-ai-wo/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 546 条目")

print("=== sync546 完成, 全部通过" if ok else "=== sync546 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
