#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync564: 第 564 课《凡出言，信为先》，同步四处
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
    "        id: '564-fan-chu-yan'," + SEP +
    "        num: '564'," + SEP +
    "        title: '凡出言 · 说话守信，说对话（信第一段）'," + SEP +
    "        subtitle: '《弟子规》信第一段：凡出言，信为先'," + SEP +
    "        path: 'lessons/564-fan-chu-yan/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第二十四课，信第一段（开篇）。原文「凡出言，信为先。诈与妄，奚可焉。话说多，不如少。惟其是，勿佞巧。」前四句讲开口先把信放在第一位，欺诈骗人的话怎么可以；后四句讲话不在多而在对，说话要实在，不花言巧语。信门开篇。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 564 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 563 课", "index 共N课", "共 564 课")
n = s.count("yaoyue563")
if n:
    s = s.replace("yaoyue563", "yaoyue564"); print(f"  [OK] index: yaoyue563 -> yaoyue564 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue563"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 563 lessons (num 01..563, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 564 lessons (num 01..564, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 563 in total)", "tests 头注释2", "(flat sorted chips, 564 in total)")
s, g2 = once(s, "series cover stats show correct counts (563/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (564/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('563'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('564'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 563 lesson cards'", "tests 平板用例名", "test('sidebar visible, 564 lesson cards'")
s, g5 = once(s, "numstrip visible with 563 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 564 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=23（合计 563）", "tests chip 注释", "弟子规课堂=24（合计 564）")
s, g7 = once(s, "8, 1, 47, 23];", "tests chip 数组", "8, 1, 47, 24];")
s = s.replace("// 全部 563 个序号 chip", "// 全部 564 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 563", "tests 末组注释", "末组「弟子规课堂」末项 = 564")
n_cards = s.count("toHaveCount(563)")
s = s.replace("toHaveCount(563)", "toHaveCount(564)")
s = s.replace("toHaveText('563')", "toHaveText('564')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 563 -> 564 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/564-fan-chu-yan/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 564 条目")

print("=== sync564 完成, 全部通过" if ok else "=== sync564 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
