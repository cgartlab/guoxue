#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync523: 把 523 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '523-dai-zhi-sui'," + SEP +
    "        num: '523'," + SEP +
    "        title: '迨至隋 · 一土宇'," + SEP +
    "        subtitle: '不再传，失统绪；唐高祖，起义师，除隋乱，创国基'," + SEP +
    "        path: 'lessons/523-dai-zhi-sui/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十课精讲：迨至隋，一土宇。不再传，失统绪。唐高祖，起义师。除隋乱，创国基。上一课讲了南北朝对峙——南朝宋齐梁陈、北朝魏周齐分治。这一课接着讲：等到隋朝统一天下（迨至隋，一土宇），但隋朝短祚、皇位没有长久传承、失去统治统系（不再传，失统绪）；唐高祖李渊起兵讨逆（唐高祖，起义师），平定隋末之乱、开创唐朝基业（除隋乱，创国基）。八句三言，讲完隋唐更替、鼎革相继。'," + SEP +
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
    print("  [OK] manifest: 插入 523 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 522 课", "index 共N课"):
    s = s.replace("共 522 课", "共 523 课")
else:
    ok = False
if s.count("yaoyue522") > 0:
    s = s.replace("yaoyue522", "yaoyue523")
    print(f"  [OK] index: yaoyue522 -> yaoyue523 ({s.count('yaoyue523')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue522")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(522)") > 0:
    s = s.replace("toHaveCount(522)", "toHaveCount(523)")
    print("  [OK] tests: toHaveCount(522) -> 523")
else:
    print("  [WARN] tests: 未找到 toHaveCount(522)")
    ok = False
if assert_once(s, "toBe('522')", "tests toBe"):
    s = s.replace("toBe('522')", "toBe('523')")
else:
    ok = False
if assert_once(s, "toHaveText('522')", "tests toHaveText"):
    s = s.replace("toHaveText('522')", "toHaveText('523')")
else:
    ok = False
# expectedChipCounts 末项 29 -> 30
if assert_once(s, " 8, 1, 29]", "tests chip 末项"):
    s = s.replace(" 8, 1, 29]", " 8, 1, 30]")
    print("  [OK] tests: expectedChipCounts 末项 29 -> 30")
else:
    ok = False
# 注释：三字经课堂=29（合计 522） 与 末项 = 522
if s.count("三字经课堂=29") > 0:
    s = s.replace("三字经课堂=29", "三字经课堂=30")
    print("  [OK] tests: 注释 三字经课堂=29 -> 30")
if s.count("（合计 522）") > 0:
    s = s.replace("（合计 522）", "（合计 523）")
    print("  [OK] tests: 注释 合计 522 -> 523")
if s.count("末项 = 522") > 0:
    s = s.replace("末项 = 522", "末项 = 523")
    print("  [OK] tests: 注释 末项 522 -> 523")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/523-dai-zhi-sui/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "  </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 523 条目")
else:
    ok = False

print("=== sync523 完成, 全部通过" if ok else "=== sync523 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
