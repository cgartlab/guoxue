#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync534: 把 534 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '534-ruo-liang-hao'," + SEP +
    "        num: '534'," + SEP +
    "        title: '若梁灏 · 八十二'," + SEP +
    "        subtitle: '八十二，对大廷，魁多士；彼既成，众称异，尔小生，宜立志'," + SEP +
    "        path: 'lessons/534-ruo-liang-hao/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十一课精讲：若梁灏，八十二。对大廷，魁多士。彼既成，众称异。尔小生，宜立志。上一课讲晚学可成、劝人趁早，这一课换个角度讲立定志向，几岁开始都不晚：相传梁灏八十二岁对策大廷、压过众多读书人夺魁，学成之后人人称奇；所以《三字经》转过来叮嘱小孩子：你们该早早立下志向。八句三言告诉孩子：年纪不是借口，先立志再下功夫。'," + SEP +
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
    print("  [OK] manifest: 插入 534 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 533 课", "index 共N课"):
    s = s.replace("共 533 课", "共 534 课")
else:
    ok = False
if s.count("yaoyue533") > 0:
    n = s.count("yaoyue533")
    s = s.replace("yaoyue533", "yaoyue534")
    print(f"  [OK] index: yaoyue533 -> yaoyue534 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue533")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(533)") > 0:
    n = s.count("toHaveCount(533)")
    s = s.replace("toHaveCount(533)", "toHaveCount(534)")
    print(f"  [OK] tests: toHaveCount(533) -> 534 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(533)")
    ok = False
if assert_once(s, "toBe('533')", "tests toBe"):
    s = s.replace("toBe('533')", "toBe('534')")
else:
    ok = False
if assert_once(s, "toHaveText('533')", "tests toHaveText"):
    s = s.replace("toHaveText('533')", "toHaveText('534')")
else:
    ok = False
if assert_once(s, " 8, 1, 40]", "tests chip 末项"):
    s = s.replace(" 8, 1, 40]", " 8, 1, 41]")
    print("  [OK] tests: expectedChipCounts 末项 40 -> 41")
else:
    ok = False
if s.count("三字经课堂=40") > 0:
    s = s.replace("三字经课堂=40", "三字经课堂=41")
    print("  [OK] tests: 注释 三字经课堂=40 -> 41")
if s.count("（合计 533）") > 0:
    s = s.replace("（合计 533）", "（合计 534）")
    print("  [OK] tests: 注释 合计 533 -> 534")
if s.count("末项 = 533") > 0:
    s = s.replace("末项 = 533", "末项 = 534")
    print("  [OK] tests: 注释 末项 533 -> 534")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/534-ruo-liang-hao/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 534 条目")
else:
    ok = False

print("=== sync534 完成, 全部通过" if ok else "=== sync534 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
