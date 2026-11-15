#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync525: 把 525 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '525-yan-song-xing'," + SEP +
    "        num: '525'," + SEP +
    "        title: '炎宋兴 · 受周禅'," + SEP +
    "        subtitle: '受周禅，十八传，南北混；辽与金，帝号纷，迨灭辽，宋犹存'," + SEP +
    "        path: 'lessons/525-yan-song-xing/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十二课精讲：炎宋兴，受周禅。十八传，南北混。辽与金，帝号纷。迨灭辽，宋犹存。上一课讲了五代更替——梁唐晋汉周相继、各有其由。这一课接着讲：赵匡胤陈桥兵变、受后周禅让建立宋朝（炎宋兴，受周禅）；宋朝传十八代皇帝，历经北宋、南宋（十八传，南北混）；契丹辽与女真金先后称帝（辽与金，帝号纷）；等到金灭了辽，宋朝还存在（迨灭辽，宋犹存）。八句三言，讲完宋朝兴替与辽金纷争。'," + SEP +
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
    print("  [OK] manifest: 插入 525 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 524 课", "index 共N课"):
    s = s.replace("共 524 课", "共 525 课")
else:
    ok = False
if s.count("yaoyue524") > 0:
    s = s.replace("yaoyue524", "yaoyue525")
    print(f"  [OK] index: yaoyue524 -> yaoyue525 ({s.count('yaoyue525')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue524")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(524)") > 0:
    n = s.count("toHaveCount(524)")
    s = s.replace("toHaveCount(524)", "toHaveCount(525)")
    print(f"  [OK] tests: toHaveCount(524) -> 525 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(524)")
    ok = False
if assert_once(s, "toBe('524')", "tests toBe"):
    s = s.replace("toBe('524')", "toBe('525')")
else:
    ok = False
if assert_once(s, "toHaveText('524')", "tests toHaveText"):
    s = s.replace("toHaveText('524')", "toHaveText('525')")
else:
    ok = False
# expectedChipCounts 末项 31 -> 32
if assert_once(s, " 8, 1, 31]", "tests chip 末项"):
    s = s.replace(" 8, 1, 31]", " 8, 1, 32]")
    print("  [OK] tests: expectedChipCounts 末项 31 -> 32")
else:
    ok = False
# 注释：三字经课堂=31（合计 524） 与 末项 = 524
if s.count("三字经课堂=31") > 0:
    s = s.replace("三字经课堂=31", "三字经课堂=32")
    print("  [OK] tests: 注释 三字经课堂=31 -> 32")
if s.count("（合计 524）") > 0:
    s = s.replace("（合计 524）", "（合计 525）")
    print("  [OK] tests: 注释 合计 524 -> 525")
if s.count("末项 = 524") > 0:
    s = s.replace("末项 = 524", "末项 = 525")
    print("  [OK] tests: 注释 末项 524 -> 525")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/525-yan-song-xing/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 525 条目")
else:
    ok = False

print("=== sync525 完成, 全部通过" if ok else "=== sync525 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
