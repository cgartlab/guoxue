#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync524: 把 524 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '524-er-shi-chuan'," + SEP +
    "        num: '524'," + SEP +
    "        title: '二十传 · 三百载'," + SEP +
    "        subtitle: '三百载，梁灭之，国乃改；梁唐晋，及汉周，称五代，皆有由'," + SEP +
    "        path: 'lessons/524-er-shi-chuan/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十一课精讲：二十传，三百载。梁灭之，国乃改。梁唐晋，及汉周。称五代，皆有由。上一课讲了隋唐更替——隋文帝一统、隋祚短促、唐高祖建唐开基。这一课接着讲：唐朝传了二十代皇帝、约三百年（二十传，三百载），被朱温所灭、改朝换代（梁灭之，国乃改）；其后梁、唐、晋、汉、周五个朝代相继（梁唐晋，及汉周），称为五代，各有其因（称五代，皆有由）。八句三言，讲完唐朝世系与五代更替。'," + SEP +
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
    print("  [OK] manifest: 插入 524 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 523 课", "index 共N课"):
    s = s.replace("共 523 课", "共 524 课")
else:
    ok = False
if s.count("yaoyue523") > 0:
    s = s.replace("yaoyue523", "yaoyue524")
    print(f"  [OK] index: yaoyue523 -> yaoyue524 ({s.count('yaoyue524')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue523")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(523)") > 0:
    n = s.count("toHaveCount(523)")
    s = s.replace("toHaveCount(523)", "toHaveCount(524)")
    print(f"  [OK] tests: toHaveCount(523) -> 524 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(523)")
    ok = False
if assert_once(s, "toBe('523')", "tests toBe"):
    s = s.replace("toBe('523')", "toBe('524')")
else:
    ok = False
if assert_once(s, "toHaveText('523')", "tests toHaveText"):
    s = s.replace("toHaveText('523')", "toHaveText('524')")
else:
    ok = False
# expectedChipCounts 末项 30 -> 31
if assert_once(s, " 8, 1, 30]", "tests chip 末项"):
    s = s.replace(" 8, 1, 30]", " 8, 1, 31]")
    print("  [OK] tests: expectedChipCounts 末项 30 -> 31")
else:
    ok = False
# 注释：三字经课堂=30（合计 523） 与 末项 = 523
if s.count("三字经课堂=30") > 0:
    s = s.replace("三字经课堂=30", "三字经课堂=31")
    print("  [OK] tests: 注释 三字经课堂=30 -> 31")
if s.count("（合计 523）") > 0:
    s = s.replace("（合计 523）", "（合计 524）")
    print("  [OK] tests: 注释 合计 523 -> 524")
if s.count("末项 = 523") > 0:
    s = s.replace("末项 = 523", "末项 = 524")
    print("  [OK] tests: 注释 末项 523 -> 524")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/524-er-shi-chuan/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "  </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 524 条目")
else:
    ok = False

print("=== sync524 完成, 全部通过" if ok else "=== sync524 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
