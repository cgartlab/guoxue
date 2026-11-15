#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync536: 把 536 同步到四处（manifest / index.html / tests / sitemap）。"""
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
old_block = "        featured: false" + SEP + "    }" + SEP + "];"
new_entry = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '536-cai-wen-ji'," + SEP +
    "        num: '536'," + SEP +
    "        title: '蔡文姬 · 能辨琴'," + SEP +
    "        subtitle: '能辨琴，能咏吟；彼女子，且聪敏，尔男子，当自警'," + SEP +
    "        path: 'lessons/536-cai-wen-ji/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十三课精讲：蔡文姬，能辨琴。谢道韫，能咏吟。彼女子，且聪敏。尔男子，当自警。上一课讲神童颖悟、幼学当效，这一课换个角度讲有学问不分男女：东汉蔡文姬听琴能辨弦音，东晋谢道韫随口能吟诗句；两位女子尚且聪敏过人；所以《三字经》叮嘱求学的人：更该警醒自己别松劲。八句三言告诉孩子：才学靠用功，谁都别轻看谁，也别落下自己。'," + SEP +
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
    print("  [OK] manifest: 插入 536 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 535 课", "index 共N课"):
    s = s.replace("共 535 课", "共 536 课")
else:
    ok = False
if s.count("yaoyue535") > 0:
    n = s.count("yaoyue535")
    s = s.replace("yaoyue535", "yaoyue536")
    print(f"  [OK] index: yaoyue535 -> yaoyue536 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue535")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(535)") > 0:
    n = s.count("toHaveCount(535)")
    s = s.replace("toHaveCount(535)", "toHaveCount(536)")
    print(f"  [OK] tests: toHaveCount(535) -> 536 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(535)")
    ok = False
if assert_once(s, "toBe('535')", "tests toBe"):
    s = s.replace("toBe('535')", "toBe('536')")
else:
    ok = False
if assert_once(s, "toHaveText('535')", "tests toHaveText"):
    s = s.replace("toHaveText('535')", "toHaveText('536')")
else:
    ok = False
if assert_once(s, " 8, 1, 42]", "tests chip 末项"):
    s = s.replace(" 8, 1, 42]", " 8, 1, 43]")
    print("  [OK] tests: expectedChipCounts 末项 42 -> 43")
else:
    ok = False
if s.count("三字经课堂=42") > 0:
    s = s.replace("三字经课堂=42", "三字经课堂=43")
    print("  [OK] tests: 注释 三字经课堂=42 -> 43")
if s.count("（合计 535）") > 0:
    s = s.replace("（合计 535）", "（合计 536）")
    print("  [OK] tests: 注释 合计 535 -> 536")
if s.count("末项 = 535") > 0:
    s = s.replace("末项 = 535", "末项 = 536")
    print("  [OK] tests: 注释 末项 535 -> 536")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/536-cai-wen-ji/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 536 条目")
else:
    ok = False

print("=== sync536 完成, 全部通过" if ok else "=== sync536 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
