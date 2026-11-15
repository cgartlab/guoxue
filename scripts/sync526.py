#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync526: 把 526 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '526-yuan-xing'," + SEP +
    "        num: '526'," + SEP +
    "        title: '至元兴 · 金绪歇'," + SEP +
    "        subtitle: '金绪歇，有宋世，一同灭；并中国，兼戎狄，九十年，国祚废'," + SEP +
    "        path: 'lessons/526-yuan-xing/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十三课精讲：至元兴，金绪歇。有宋世，一同灭。并中国，兼戎狄。九十年，国祚废。上一课讲了宋朝兴替与辽金并立——赵匡胤受禅建宋、南北两宋递嬗、辽金先后称帝。这一课接着讲：蒙古兴起，元世祖忽必烈定国号元、年号至元（至元兴）；金国被蒙古所灭、统绪断绝（金绪歇）；到了宋朝，宋也被元一同灭掉（有宋世，一同灭）；元朝兼并中原中国，兼有戎狄等边疆各族（并中国，兼戎狄）；元朝国祚约九十年就废亡了（九十年，国祚废）。八句三言，讲完金宋俱灭、元朝兴亡。'," + SEP +
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
    print("  [OK] manifest: 插入 526 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 525 课", "index 共N课"):
    s = s.replace("共 525 课", "共 526 课")
else:
    ok = False
if s.count("yaoyue525") > 0:
    s = s.replace("yaoyue525", "yaoyue526")
    print(f"  [OK] index: yaoyue525 -> yaoyue526 ({s.count('yaoyue526')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue525")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(525)") > 0:
    n = s.count("toHaveCount(525)")
    s = s.replace("toHaveCount(525)", "toHaveCount(526)")
    print(f"  [OK] tests: toHaveCount(525) -> 526 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(525)")
    ok = False
if assert_once(s, "toBe('525')", "tests toBe"):
    s = s.replace("toBe('525')", "toBe('526')")
else:
    ok = False
if assert_once(s, "toHaveText('525')", "tests toHaveText"):
    s = s.replace("toHaveText('525')", "toHaveText('526')")
else:
    ok = False
# expectedChipCounts 末项 32 -> 33
if assert_once(s, " 8, 1, 32]", "tests chip 末项"):
    s = s.replace(" 8, 1, 32]", " 8, 1, 33]")
    print("  [OK] tests: expectedChipCounts 末项 32 -> 33")
else:
    ok = False
if s.count("三字经课堂=32") > 0:
    s = s.replace("三字经课堂=32", "三字经课堂=33")
    print("  [OK] tests: 注释 三字经课堂=32 -> 33")
if s.count("（合计 525）") > 0:
    s = s.replace("（合计 525）", "（合计 526）")
    print("  [OK] tests: 注释 合计 525 -> 526")
if s.count("末项 = 525") > 0:
    s = s.replace("末项 = 525", "末项 = 526")
    print("  [OK] tests: 注释 末项 525 -> 526")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/526-yuan-xing/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 526 条目")
else:
    ok = False

print("=== sync526 完成, 全部通过" if ok else "=== sync526 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
