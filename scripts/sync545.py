#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync545: 第 545 课《亲所好，力为具》，同步四处
（manifest / index / tests / sitemap）。门类与免费名单前课已建（545- 已在 freePrefixes）。"""
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
    "        id: '545-qin-suo-hao'," + SEP +
    "        num: '545'," + SEP +
    "        title: '亲所好 · 力为具、谨为去'," + SEP +
    "        subtitle: '《弟子规》入则孝第四段：亲所好，力为具'," + SEP +
    "        path: 'lessons/545-qin-suo-hao/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第五课，入则孝第四段。原文「亲所好，力为具。亲所恶，谨为去。身有伤，贻亲忧。德有伤，贻亲羞。」讲两件事：父母喜欢的尽力备办，父母讨厌的小心避开；自己身上受伤，父母先忧愁，品行有亏，父母更羞愧。前一对顺着父母的心意，后一对护好自己的身心——孝不只是给吃给穿，还要不让父母操心、不让父母丢脸。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 545 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 544 课", "index 共N课", "共 545 课")
n = s.count("yaoyue544")
if n:
    s = s.replace("yaoyue544", "yaoyue545"); print(f"  [OK] index: yaoyue544 -> yaoyue545 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue544"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 544 lessons (num 01..544, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 545 lessons (num 01..545, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 544 in total)", "tests 头注释2", "(flat sorted chips, 545 in total)")
s, g2 = once(s, "series cover stats show correct counts (544/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (545/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('544'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('545'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 544 lesson cards'", "tests 平板用例名", "test('sidebar visible, 545 lesson cards'")
s, g5 = once(s, "numstrip visible with 544 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 545 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=4（合计 544）", "tests chip 注释", "弟子规课堂=5（合计 545）")
s, g7 = once(s, "8, 1, 47, 4];", "tests chip 数组", "8, 1, 47, 5];")
s = s.replace("// 全部 544 个序号 chip", "// 全部 545 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 544", "tests 末组注释", "末组「弟子规课堂」末项 = 545")
n_cards = s.count("toHaveCount(544)")
s = s.replace("toHaveCount(544)", "toHaveCount(545)")
s = s.replace("toHaveText('544')", "toHaveText('545')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 544 -> 545 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/545-qin-suo-hao/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 545 条目")

print("=== sync545 完成, 全部通过" if ok else "=== sync545 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
