#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync544: 第 544 课《事虽小勿擅为》，同步四处
（manifest / index / tests / sitemap）。门类与免费名单前课已建。"""
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
    "        id: '544-shi-sui-xiao'," + SEP +
    "        num: '544'," + SEP +
    "        title: '事虽小 · 勿擅为、勿私藏'," + SEP +
    "        subtitle: '《弟子规》入则孝第三段：事虽小，勿擅为'," + SEP +
    "        path: 'lessons/544-shi-sui-xiao/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第四课，入则孝第三段。原文「事虽小，勿擅为。苟擅为，子道亏。物虽小，勿私藏。苟私藏，亲心伤。」讲两个小：事再小也别自作主张，东西再小也别偷偷藏起来不说。前两句说擅，自作主张会让做子女的本分缺一块；后两句说私，瞒着父母，父母伤心的不是那件东西，是你不肯说。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 544 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 543 课", "index 共N课", "共 544 课")
n = s.count("yaoyue543")
if n:
    s = s.replace("yaoyue543", "yaoyue544"); print(f"  [OK] index: yaoyue543 -> yaoyue544 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue543"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 543 lessons (num 01..543, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 544 lessons (num 01..544, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 543 in total)", "tests 头注释2", "(flat sorted chips, 544 in total)")
s, g2 = once(s, "series cover stats show correct counts (543/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (544/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('543'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('544'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 543 lesson cards'", "tests 平板用例名", "test('sidebar visible, 544 lesson cards'")
s, g5 = once(s, "numstrip visible with 543 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 544 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=3（合计 543）", "tests chip 注释", "弟子规课堂=4（合计 544）")
s, g7 = once(s, "8, 1, 47, 3];", "tests chip 数组", "8, 1, 47, 4];")
s = s.replace("// 全部 543 个序号 chip", "// 全部 544 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 543", "tests 末组注释", "末组「弟子规课堂」末项 = 544")
n_cards = s.count("toHaveCount(543)")
s = s.replace("toHaveCount(543)", "toHaveCount(544)")
s = s.replace("toHaveText('543')", "toHaveText('544')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 543 -> 544 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/544-shi-sui-xiao/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 544 条目")

print("=== sync544 完成, 全部通过" if ok else "=== sync544 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
