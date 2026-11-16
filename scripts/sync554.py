#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync554: 第 554 课《事诸父，如事父》，同步四处
（manifest / index / tests / sitemap）。付费课，unlock.js 不动。"""
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
    "        id: '554-shi-zhu-fu'," + SEP +
    "        num: '554'," + SEP +
    "        title: '如事父 · 敬及诸父诸兄（出则悌收官）'," + SEP +
    "        subtitle: '《弟子规》出则悌第六段：事诸父，如事父'," + SEP +
    "        path: 'lessons/554-shi-zhu-fu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十四课，出则悌第六段（收官）。原文「事诸父，如事父。事诸兄，如事兄。」讲把敬放大一圈：对待叔叔伯伯这些长辈，像对待父亲一样；对待堂哥表哥这些兄长，像对待哥哥一样。家里的礼练熟了，带到门外，见谁都自然。出则悌至此完结。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 554 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 553 课", "index 共N课", "共 554 课")
n = s.count("yaoyue553")
if n:
    s = s.replace("yaoyue553", "yaoyue554"); print(f"  [OK] index: yaoyue553 -> yaoyue554 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue553"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 553 lessons (num 01..553, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 554 lessons (num 01..554, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 553 in total)", "tests 头注释2", "(flat sorted chips, 554 in total)")
s, g2 = once(s, "series cover stats show correct counts (553/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (554/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('553'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('554'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 553 lesson cards'", "tests 平板用例名", "test('sidebar visible, 554 lesson cards'")
s, g5 = once(s, "numstrip visible with 553 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 554 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=13（合计 553）", "tests chip 注释", "弟子规课堂=14（合计 554）")
s, g7 = once(s, "8, 1, 47, 13];", "tests chip 数组", "8, 1, 47, 14];")
s = s.replace("// 全部 553 个序号 chip", "// 全部 554 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 553", "tests 末组注释", "末组「弟子规课堂」末项 = 554")
n_cards = s.count("toHaveCount(553)")
s = s.replace("toHaveCount(553)", "toHaveCount(554)")
s = s.replace("toHaveText('553')", "toHaveText('554')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 553 -> 554 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/554-shi-zhu-fu/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 554 条目")

print("=== sync554 完成, 全部通过" if ok else "=== sync554 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
