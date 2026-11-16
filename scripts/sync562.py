#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync562: 第 562 课《人问谁，对以名》，同步四处
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
    "        id: '562-ren-wen-shei'," + SEP +
    "        num: '562'," + SEP +
    "        title: '人问谁 · 说清楚，先征求（谨第八段）'," + SEP +
    "        subtitle: '《弟子规》谨第八段：人问谁，对以名'," + SEP +
    "        path: 'lessons/562-ren-wen-shei/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第二十二课，谨第八段。原文「人问谁，对以名。吾与我，不分明。用人物，须明求。倘不问，即为偷。」前四句讲报名姓：人家问是谁，要报出名字，光说「我」「吾」分不清；后四句讲用物有礼：用别人的东西要先明明白白请求，不问就拿，就跟偷一样。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 562 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 561 课", "index 共N课", "共 562 课")
n = s.count("yaoyue561")
if n:
    s = s.replace("yaoyue561", "yaoyue562"); print(f"  [OK] index: yaoyue561 -> yaoyue562 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue561"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 561 lessons (num 01..561, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 562 lessons (num 01..562, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 561 in total)", "tests 头注释2", "(flat sorted chips, 562 in total)")
s, g2 = once(s, "series cover stats show correct counts (561/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (562/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('561'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('562'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 561 lesson cards'", "tests 平板用例名", "test('sidebar visible, 562 lesson cards'")
s, g5 = once(s, "numstrip visible with 561 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 562 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=21（合计 561）", "tests chip 注释", "弟子规课堂=22（合计 562）")
s, g7 = once(s, "8, 1, 47, 21];", "tests chip 数组", "8, 1, 47, 22];")
s = s.replace("// 全部 561 个序号 chip", "// 全部 562 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 561", "tests 末组注释", "末组「弟子规课堂」末项 = 562")
n_cards = s.count("toHaveCount(561)")
s = s.replace("toHaveCount(561)", "toHaveCount(562)")
s = s.replace("toHaveText('561')", "toHaveText('562')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 561 -> 562 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/562-ren-wen-shei/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 562 条目")

print("=== sync562 完成, 全部通过" if ok else "=== sync562 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
