#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync522: 把 522 同步到四处（manifest / index.html / tests / sitemap）。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def assert_once(s, sub, where):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望出现 1 次 '{sub[:30]}', 实际 {n} 次")
        return False
    return True

ok = True

# ---------- 1) manifest (CRLF) ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old_block = ("        featured: false" + SEP + "    }" + SEP + "];")
new_entry = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '522-song-qi-ji'," + SEP +
    "        num: '522'," + SEP +
    "        title: '宋齐继 · 梁陈承'," + SEP +
    "        subtitle: '为南朝，都金陵；北元魏，分东西，宇文周，与高齐'," + SEP +
    "        path: 'lessons/522-song-qi-ji/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第二十九课精讲：宋齐继，梁陈承。为南朝，都金陵。北元魏，分东西。宇文周，与高齐。上一课讲了光武中兴、三国两晋——西晋东晋相承。这一课接着讲：南朝宋齐梁陈四代相承（宋齐继，梁陈承），统称南朝、都城建康即金陵（为南朝，都金陵）；北方北魏（元魏）立国，后来分裂为东魏西魏（北元魏，分东西），宇文氏建立北周、高氏建立北齐，与北周并立（宇文周，与高齐）。八句三言，讲完南北朝南北对峙。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'sanzijing'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }" + SEP + "];"
)
if assert_once(s, old_block, "manifest old_block"):
    s = s.replace(old_block, new_entry)
    write(p, s)
    print("  [OK] manifest: 插入 522 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 521 课", "index 共N课"):
    s = s.replace("共 521 课", "共 522 课")
else:
    ok = False
if s.count("yaoyue521") > 0:
    s = s.replace("yaoyue521", "yaoyue522")
    print(f"  [OK] index: yaoyue521 -> yaoyue522 ({s.count('yaoyue522')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue521")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
# 关键运行断言：toHaveCount(521) / toBe('521') / toHaveText('521')
if s.count("toHaveCount(521)") > 0:
    s = s.replace("toHaveCount(521)", "toHaveCount(522)")
    print("  [OK] tests: toHaveCount(521) -> 522")
else:
    print("  [WARN] tests: 未找到 toHaveCount(521)")
    ok = False
if assert_once(s, "toBe('521')", "tests toBe"):
    s = s.replace("toBe('521')", "toBe('522')")
else:
    ok = False
if assert_once(s, "toHaveText('521')", "tests toHaveText"):
    s = s.replace("toHaveText('521')", "toHaveText('522')")
else:
    ok = False
# expectedChipCounts 末项 28 -> 29
if assert_once(s, " 8, 1, 28]", "tests chip 末项"):
    s = s.replace(" 8, 1, 28]", " 8, 1, 29]")
    print("  [OK] tests: expectedChipCounts 末项 28 -> 29")
else:
    ok = False
# 注释：三字经课堂=28（合计 521） 与 末项 = 521
if s.count("三字经课堂=28") > 0:
    s = s.replace("三字经课堂=28", "三字经课堂=29")
    print("  [OK] tests: 注释 三字经课堂=28 -> 29")
if s.count("（合计 521）") > 0:
    s = s.replace("（合计 521）", "（合计 522）")
    print("  [OK] tests: 注释 合计 521 -> 522")
if s.count("末项 = 521") > 0:
    s = s.replace("末项 = 521", "末项 = 522")
    print("  [OK] tests: 注释 末项 521 -> 522")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/522-song-qi-ji/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "  </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 522 条目")
else:
    ok = False

print("=== sync522 完成, 全部通过" if ok else "=== sync522 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
