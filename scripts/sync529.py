#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync529: 把 529 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '529-du-shi-zhe'," + SEP +
    "        num: '529'," + SEP +
    "        title: '读史者 · 考实录'," + SEP +
    "        subtitle: '考实录，通古今，若亲目；口而诵，心而惟，朝于斯，夕于斯'," + SEP +
    "        path: 'lessons/529-du-shi-zhe/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十六课精讲：读史者，考实录。通古今，若亲目。口而诵，心而惟。朝于斯，夕于斯。上一课讲完了从唐到清的朝代更替，这一课调转笔锋，教孩子怎样读书：读历史的人要查考真实可靠的记载（读史者，考实录）；把古今的事理贯通起来，就像亲眼见过一样明白（通古今，若亲目）；读书要口中诵读，心里同时思索（口而诵，心而惟）；从早到晚都专一用功，不肯松懈（朝于斯，夕于斯）。八句三言，从讲历史转到怎样学，是全篇由史入学的转折。'," + SEP +
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
    print("  [OK] manifest: 插入 529 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 528 课", "index 共N课"):
    s = s.replace("共 528 课", "共 529 课")
else:
    ok = False
if s.count("yaoyue528") > 0:
    s = s.replace("yaoyue528", "yaoyue529")
    print(f"  [OK] index: yaoyue528 -> yaoyue529 ({s.count('yaoyue529')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue528")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(528)") > 0:
    n = s.count("toHaveCount(528)")
    s = s.replace("toHaveCount(528)", "toHaveCount(529)")
    print(f"  [OK] tests: toHaveCount(528) -> 529 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(528)")
    ok = False
if assert_once(s, "toBe('528')", "tests toBe"):
    s = s.replace("toBe('528')", "toBe('529')")
else:
    ok = False
if assert_once(s, "toHaveText('528')", "tests toHaveText"):
    s = s.replace("toHaveText('528')", "toHaveText('529')")
else:
    ok = False
# expectedChipCounts 末项 35 -> 36
if assert_once(s, " 8, 1, 35]", "tests chip 末项"):
    s = s.replace(" 8, 1, 35]", " 8, 1, 36]")
    print("  [OK] tests: expectedChipCounts 末项 35 -> 36")
else:
    ok = False
if s.count("三字经课堂=35") > 0:
    s = s.replace("三字经课堂=35", "三字经课堂=36")
    print("  [OK] tests: 注释 三字经课堂=35 -> 36")
if s.count("（合计 528）") > 0:
    s = s.replace("（合计 528）", "（合计 529）")
    print("  [OK] tests: 注释 合计 528 -> 529")
if s.count("末项 = 528") > 0:
    s = s.replace("末项 = 528", "末项 = 529")
    print("  [OK] tests: 注释 末项 528 -> 529")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/529-du-shi-zhe/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 529 条目")
else:
    ok = False

print("=== sync529 完成, 全部通过" if ok else "=== sync529 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
