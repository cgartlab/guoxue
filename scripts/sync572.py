#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync572: 第 572 课《凡是人，皆须爱》，同步四处
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
DESC = ('《弟子规》第三十二课，泛爱众第一段。原文：「凡是人，皆须爱。天同覆，地同载。'
        '行高者，名自高。人所重，非貌高。」前四句讲只要是人就该去爱，因为大家同顶一片天、'
        '同踩一块地；后四句讲品行高的人名声自然高，别人看重的是德行，不是相貌外表。')

# ---------- 1) manifest ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '572-fan-shi-ren'," + SEP +
    "        num: '572'," + SEP +
    "        title: '凡是人 · 人都要爱，重德不重貌（泛爱众第一段）'," + SEP +
    "        subtitle: '《弟子规》泛爱众第一段：凡是人，皆须爱'," + SEP +
    "        path: 'lessons/572-fan-shi-ren/index.html'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 572 条目")

# ---------- 2) index.html 封面课程数 ----------
p = f"{ROOT}/index.html"
s = read(p)
s2, g1 = once(s, "共 571 课", "index 封面课程数", "共 572 课")
ok = ok and g1
if g1:
    write(p, s2); print("  [OK] index: 共 571 课 -> 共 572 课")

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
n = s.count("571")
s = s.replace("571", "572")
s, g1 = once(s, "弟子规课堂=31（合计 572）", "tests 注释", "弟子规课堂=32（合计 572）")
ok = ok and g1
s, g2 = once(s, "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 31]",
             "tests expectedChipCounts",
             "[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 47, 32]")
ok = ok and g2
write(p, s)
print(f"  [{'OK' if (g1 and g2) else 'PART'}] tests: 替换 {n} 处 571->572，弟子规组 31->32")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
block = ("  <url>\n"
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/572-fan-shi-ren/index.html</loc>\n"
         "    <lastmod>2026-11-17</lastmod>\n"
         "    <changefreq>weekly</changefreq>\n"
         "    <priority>0.8</priority>\n"
         "    </url>\n"
         "</urlset>")
s, g1 = once(s, "</urlset>", "sitemap urlset", block)
ok = ok and g1
if g1:
    write(p, s); print("  [OK] sitemap: 追加 572 条目")

print("RESULT:", "ALL OK" if ok else "CHECK WARNINGS")
