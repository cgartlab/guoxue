#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync571: 第 571 课《过能改，归于无》，同步四处
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
DESC = ('《弟子规》第三十一课，信第八段（信门末段）。原文：「过能改，归于无。倘揜饰，增一辜。」'
        '前两句讲有了过错肯改，就像没有过错一样；后两句讲如果犯了错还遮盖掩饰，'
        '就等于又添了一条罪。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '571-guo-neng-gai'," + SEP +
    "        num: '571'," + SEP +
    "        title: '过能改 · 错了就改，别遮（信末段）'," + SEP +
    "        subtitle: '《弟子规》信第八段：过能改，归于无'," + SEP +
    "        path: 'lessons/571-guo-neng-gai/index.html'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 571 条目")

# ---------- 2) index.html 封面课程数 ----------
p = f"{ROOT}/index.html"
s = read(p)
s2, g1 = once(s, "共 570 课", "index 封面课程数", "共 571 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 570 课 -> 共 571 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("570")
s = s.replace("570", "571")
s, g1 = once(s, "弟子规课堂=30（合计 571）", "tests 注释", "弟子规课堂=31（合计 571）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 30]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 31]")
ok = ok and g2
write(p, s)
print(f"  [{'OK' if (g1 and g2) else 'PART'}] tests: 替换 {n} 处 570->571，弟子规组 30->31")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/571-guo-neng-gai/index.html</loc>\n"
         "    <lastmod>2026-11-17</lastmod>\n"
         "    <changefreq>weekly</changefreq>\n"
         "    <priority>0.8</priority>\n"
         "    </url>\n"
         "</urlset>")
s, g1 = once(s, "</urlset>", "sitemap urlset", block)
ok = ok and g1
if g1:
    write(p, s); print("  [OK] sitemap: 追加 571 条目")

print("RESULT:", "ALL OK" if ok else "CHECK WARNINGS")
