#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync565: 第 565 课《奸巧语，秽污词》，同步四处
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
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:30]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True
DESC = ('《弟子规》第二十五课，信第二段。原文「奸巧语，秽污词。市井气，切戒之。见未真，勿轻言。'
        '知未的，勿轻传。」前四句讲奸诈取巧的话、脏话粗话、粗俗习气，都要切切戒掉；'
        '后四句讲没看清的事不要随便说，没弄清的事不要随便传。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '565-jian-qiao-yu'," + SEP +
    "        num: '565'," + SEP +
    "        title: '奸巧语 · 口要干净，话要留稳（信第二段）'," + SEP +
    "        subtitle: '《弟子规》信第二段：奸巧语，秽污词'," + SEP +
    "        path: 'lessons/565-jian-qiao-yu/index.html'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 565 条目")

# ---------- 2) index.html 封面课程数 ----------
p = f"{ROOT}/index.html"
s = read(p)
s2, g1 = once(s, "共 564 课", "index 封面课程数", "共 565 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 564 课 -> 共 565 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("564")
s = s.replace("564", "565")
s, g1 = once(s, "弟子规课堂=24（合计 565）", "tests 注释", "弟子规课堂=25（合计 565）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 24]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 25]")
ok = ok and g2
if g1 and g2:
    write(p, s); print(f"  [OK] tests: 替换 {n} 处 564->565，弟子规组 24->25")
else:
    write(p, s); print("  [PART] tests: 已写入，但有条目未命中")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/565-jian-qiao-yu/index.html</loc>\n"
         "    <lastmod>2026-11-16</lastmod>\n"
         "    <changefreq>weekly</changefreq>\n"
         "    <priority>0.8</priority>\n"
         "    </url>\n"
         "</urlset>")
s, g1 = once(s, "</urlset>", "sitemap urlset", block)
ok = ok and g1
if g1:
    write(p, s); print("  [OK] sitemap: 追加 565 条目")

print("RESULT:", "ALL OK" if ok else "CHECK WARNINGS")
