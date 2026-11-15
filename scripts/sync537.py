#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync537: 把 537 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '537-tang-liu-yan'," + SEP +
    "        num: '537'," + SEP +
    "        title: '唐刘晏 · 方七岁'," + SEP +
    "        subtitle: '方七岁，作正字；彼虽幼，身已仕，尔幼学，勉而致'," + SEP +
    "        path: 'lessons/537-tang-liu-yan/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十四课精讲：唐刘晏，方七岁。举神童，作正字。彼虽幼，身已仕。尔幼学，勉而致。上一课讲才女聪敏、人人自警，这一课讲年少有为：唐朝刘晏七岁就被举为神童，做了校正文字的正字官；他年纪虽小已经任职做事；所以《三字经》劝幼年求学的人：努力也能做到。八句三言告诉孩子：年纪小不是理由，肯用功就能早有作为。'," + SEP +
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
    print("  [OK] manifest: 插入 537 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 536 课", "index 共N课"):
    s = s.replace("共 536 课", "共 537 课")
else:
    ok = False
if s.count("yaoyue536") > 0:
    n = s.count("yaoyue536")
    s = s.replace("yaoyue536", "yaoyue537")
    print(f"  [OK] index: yaoyue536 -> yaoyue537 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue536")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(536)") > 0:
    n = s.count("toHaveCount(536)")
    s = s.replace("toHaveCount(536)", "toHaveCount(537)")
    print(f"  [OK] tests: toHaveCount(536) -> 537 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(536)")
    ok = False
if assert_once(s, "toBe('536')", "tests toBe"):
    s = s.replace("toBe('536')", "toBe('537')")
else:
    ok = False
if assert_once(s, "toHaveText('536')", "tests toHaveText"):
    s = s.replace("toHaveText('536')", "toHaveText('537')")
else:
    ok = False
if assert_once(s, " 8, 1, 43]", "tests chip 末项"):
    s = s.replace(" 8, 1, 43]", " 8, 1, 44]")
    print("  [OK] tests: expectedChipCounts 末项 43 -> 44")
else:
    ok = False
if s.count("三字经课堂=43") > 0:
    s = s.replace("三字经课堂=43", "三字经课堂=44")
    print("  [OK] tests: 注释 三字经课堂=43 -> 44")
if s.count("（合计 536）") > 0:
    s = s.replace("（合计 536）", "（合计 537）")
    print("  [OK] tests: 注释 合计 536 -> 537")
if s.count("末项 = 536") > 0:
    s = s.replace("末项 = 536", "末项 = 537")
    print("  [OK] tests: 注释 末项 536 -> 537")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/537-tang-liu-yan/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 537 条目")
else:
    ok = False

print("=== sync537 完成, 全部通过" if ok else "=== sync537 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
