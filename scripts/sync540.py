#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync540: 把 540 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '540-ren-yi-zi'," + SEP +
    "        num: '540'," + SEP +
    "        title: '人遗子 · 金满籝'," + SEP +
    "        subtitle: '金满籝，我教子；惟一经，勤有功，戏无益，宜勉力'," + SEP +
    "        path: 'lessons/540-ren-yi-zi/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十七课精讲：人遗子，金满籝。我教子，惟一经。勤有功，戏无益。戒之哉，宜勉力。这是《三字经》的收尾一课：别人给子孙留满箱金银，我教子孙的只有一部经书；勤勉才有成效，嬉戏贪玩没有好处；所以要警戒自己，好好用功。八句三言告诉孩子：留给后人最要紧的不是钱财，是读书向学的道理。'," + SEP +
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
    print("  [OK] manifest: 插入 540 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 539 课", "index 共N课"):
    s = s.replace("共 539 课", "共 540 课")
else:
    ok = False
if s.count("yaoyue539") > 0:
    n = s.count("yaoyue539")
    s = s.replace("yaoyue539", "yaoyue540")
    print(f"  [OK] index: yaoyue539 -> yaoyue540 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue539")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(539)") > 0:
    n = s.count("toHaveCount(539)")
    s = s.replace("toHaveCount(539)", "toHaveCount(540)")
    print(f"  [OK] tests: toHaveCount(539) -> 540 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(539)")
    ok = False
if assert_once(s, "toBe('539')", "tests toBe"):
    s = s.replace("toBe('539')", "toBe('540')")
else:
    ok = False
if assert_once(s, "toHaveText('539')", "tests toHaveText"):
    s = s.replace("toHaveText('539')", "toHaveText('540')")
else:
    ok = False
if assert_once(s, " 8, 1, 46]", "tests chip 末项"):
    s = s.replace(" 8, 1, 46]", " 8, 1, 47]")
    print("  [OK] tests: expectedChipCounts 末项 46 -> 47")
else:
    ok = False
if s.count("三字经课堂=46") > 0:
    s = s.replace("三字经课堂=46", "三字经课堂=47")
    print("  [OK] tests: 注释 三字经课堂=46 -> 47")
if s.count("（合计 539）") > 0:
    s = s.replace("（合计 539）", "（合计 540）")
    print("  [OK] tests: 注释 合计 539 -> 540")
if s.count("末项 = 539") > 0:
    s = s.replace("末项 = 539", "末项 = 540")
    print("  [OK] tests: 注释 末项 539 -> 540")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/540-ren-yi-zi/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-16</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 540 条目")
else:
    ok = False

print("=== sync540 完成, 全部通过" if ok else "=== sync540 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
