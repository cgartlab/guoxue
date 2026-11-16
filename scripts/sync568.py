#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync568: 第 568 课《见人恶，即内省》，同步四处
（manifest / index / tests / sitemap）。"""
import io

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:40]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True
DESC = ('《弟子规》第二十八课，信第五段。原文：「见人恶，即内省。有则改，无加警。'
        '唯德学，唯才艺。不如人，当自砺。」前四句讲看见别人的坏处，先回头反省自己有没有，'
        '有的就改，没有也要加倍警惕；后四句讲要比的只有品德学问和才能技艺，'
        '这些不如别人，就该自己下功夫磨炼。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '568-jian-ren-e'," + SEP +
    "        num: '568'," + SEP +
    "        title: '见人恶 · 照见自己，自己磨炼（信第五段）'," + SEP +
    "        subtitle: '《弟子规》信第五段：见人恶，即内省'," + SEP +
    "        path: 'lessons/568-jian-ren-e/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '" + DESC + "'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 567 条目")

# ---------- 2) index.html 封面课程数 ----------
p = f"{ROOT}/index.html"
s = read(p)
s2, g1 = once(s, "共 567 课", "index 封面课程数", "共 568 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 567 课 -> 共 568 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("567")
s = s.replace("567", "568")
s, g1 = once(s, "弟子规课堂=27（合计 568）", "tests 注释", "弟子规课堂=28（合计 568）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 27]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 28]")
ok = ok and g2
write(p, s)
print(f"  [{'OK' if (g1 and g2) else 'PART'}] tests: 替换 {n} 处 567->568，弟子规组 27->28")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/568-jian-ren-e/index.html</loc>\n"
         "    <lastmod>2026-11-17</lastmod>\n"
         "    <changefreq>weekly</changefreq>\n"
         "    <priority>0.8</priority>\n"
         "    </url>\n"
         "</urlset>")
s, g1 = once(s, "</urlset>", "sitemap urlset", block)
ok = ok and g1
if g1:
    write(p, s); print("  [OK] sitemap: 追加 567 条目")

print("RESULT:", "ALL OK" if ok else "CHECK WARNINGS")
