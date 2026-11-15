#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync535: 把 535 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '535-ying-ba-sui'," + SEP +
    "        num: '535'," + SEP +
    "        title: '莹八岁 · 能咏诗'," + SEP +
    "        subtitle: '能咏诗，能赋棋；彼颖悟，人称奇，尔幼学，当效之'," + SEP +
    "        path: 'lessons/535-ying-ba-sui/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十二课精讲：莹八岁，能咏诗。泌七岁，能赋棋。彼颖悟，人称奇。尔幼学，当效之。上一课讲高龄夺魁、立志不分早晚，这一课换个角度讲小小年纪也能有大学问：北魏祖莹八岁就能咏诗，唐代李泌七岁能以棋为题作赋；两人天资聪慧，人人称奇；所以《三字经》叮嘱幼年求学的人：应当效法他们。八句三言告诉孩子：聪明更要用功，从小把书读扎实。'," + SEP +
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
    print("  [OK] manifest: 插入 535 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 534 课", "index 共N课"):
    s = s.replace("共 534 课", "共 535 课")
else:
    ok = False
if s.count("yaoyue534") > 0:
    n = s.count("yaoyue534")
    s = s.replace("yaoyue534", "yaoyue535")
    print(f"  [OK] index: yaoyue534 -> yaoyue535 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue534")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(534)") > 0:
    n = s.count("toHaveCount(534)")
    s = s.replace("toHaveCount(534)", "toHaveCount(535)")
    print(f"  [OK] tests: toHaveCount(534) -> 535 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(534)")
    ok = False
if assert_once(s, "toBe('534')", "tests toBe"):
    s = s.replace("toBe('534')", "toBe('535')")
else:
    ok = False
if assert_once(s, "toHaveText('534')", "tests toHaveText"):
    s = s.replace("toHaveText('534')", "toHaveText('535')")
else:
    ok = False
if assert_once(s, " 8, 1, 41]", "tests chip 末项"):
    s = s.replace(" 8, 1, 41]", " 8, 1, 42]")
    print("  [OK] tests: expectedChipCounts 末项 41 -> 42")
else:
    ok = False
if s.count("三字经课堂=41") > 0:
    s = s.replace("三字经课堂=41", "三字经课堂=42")
    print("  [OK] tests: 注释 三字经课堂=41 -> 42")
if s.count("（合计 534）") > 0:
    s = s.replace("（合计 534）", "（合计 535）")
    print("  [OK] tests: 注释 合计 534 -> 535")
if s.count("末项 = 534") > 0:
    s = s.replace("末项 = 534", "末项 = 535")
    print("  [OK] tests: 注释 末项 534 -> 535")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/535-ying-ba-sui/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 535 条目")
else:
    ok = False

print("=== sync535 完成, 全部通过" if ok else "=== sync535 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
