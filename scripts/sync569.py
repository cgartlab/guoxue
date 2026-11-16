#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync569: 第 569 课《若衣服，若饮食》，同步四处
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
DESC = ('《弟子规》第二十九课，信第六段。原文：「若衣服，若饮食。不如人，勿生戚。'
        '闻过怒，闻誉乐。损友来，益友却。」前四句讲穿的吃的比不上别人，不必忧愁难过；'
        '后四句讲一听批评就发怒、一听称赞就高兴，坏朋友就会凑上来，'
        '好朋友就会走开。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '569-ruo-yi-fu'," + SEP +
    "        num: '569'," + SEP +
    "        title: '若衣服 · 不慕吃穿，能受批评（信第六段）'," + SEP +
    "        subtitle: '《弟子规》信第六段：若衣服，若饮食'," + SEP +
    "        path: 'lessons/569-ruo-yi-fu/index.html'," + SEP +
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
s2, g1 = once(s, "共 568 课", "index 封面课程数", "共 569 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 568 课 -> 共 569 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("568")
s = s.replace("568", "569")
s, g1 = once(s, "弟子规课堂=28（合计 569）", "tests 注释", "弟子规课堂=29（合计 569）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 28]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 29]")
ok = ok and g2
write(p, s)
print(f"  [{'OK' if (g1 and g2) else 'PART'}] tests: 替换 {n} 处 568->569，弟子规组 28->29")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/569-ruo-yi-fu/index.html</loc>\n"
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
