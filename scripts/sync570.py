#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync570: 第 570 课《闻誉恐，闻过欣》，同步四处
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
DESC = ('《弟子规》第三十课，信第七段。原文：「闻誉恐，闻过欣。直谅士，渐相亲。'
        '无心非，名为错。有心非，名为恶。」前四句讲听到称赞反而惶恐、听到批评反而欢喜，'
        '正直诚实的朋友就渐渐和你亲近；后四句讲不是存心做的过失叫「错」，'
        '存心做的坏事叫「恶」。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '570-wen-yu-kong'," + SEP +
    "        num: '570'," + SEP +
    "        title: '闻誉恐 · 夸我不飘，批我不恼（信第七段）'," + SEP +
    "        subtitle: '《弟子规》信第七段：闻誉恐，闻过欣'," + SEP +
    "        path: 'lessons/570-wen-yu-kong/index.html'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 570 条目")

# ---------- 2) index.html 封面课程数 ----------
p = f"{ROOT}/index.html"
s = read(p)
s2, g1 = once(s, "共 569 课", "index 封面课程数", "共 570 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 569 课 -> 共 570 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("569")
s = s.replace("569", "570")
s, g1 = once(s, "弟子规课堂=29（合计 570）", "tests 注释", "弟子规课堂=30（合计 570）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 29]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 30]")
ok = ok and g2
write(p, s)
print(f"  [{'OK' if (g1 and g2) else 'PART'}] tests: 替换 {n} 处 569->570，弟子规组 29->30")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/570-wen-yu-kong/index.html</loc>\n"
         "    <lastmod>2026-11-17</lastmod>\n"
         "    <changefreq>weekly</changefreq>\n"
         "    <priority>0.8</priority>\n"
         "    </url>\n"
         "</urlset>")
s, g1 = once(s, "</urlset>", "sitemap urlset", block)
ok = ok and g1
if g1:
    write(p, s); print("  [OK] sitemap: 追加 570 条目")

print("RESULT:", "ALL OK" if ok else "CHECK WARNINGS")
