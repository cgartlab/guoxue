#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync527: 把 527 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '527-ming-tai-zu'," + SEP +
    "        num: '527'," + SEP +
    "        title: '明太祖 · 久亲师'," + SEP +
    "        subtitle: '久亲师，传建文，方四祀；迁北京，永乐嗣，迨崇祯，煤山逝'," + SEP +
    "        path: 'lessons/527-ming-tai-zu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十四课精讲：明太祖，久亲师。传建文，方四祀。迁北京，永乐嗣。迨崇祯，煤山逝。上一课讲了金宋俱灭与元朝兴亡——蒙古兴起、金宋俱归于元，元朝统一中原，国祚约九十年而废。这一课接着讲：明太祖朱元璋出身布衣，多年亲自带兵打天下，推翻元朝、建立明朝（明太祖，久亲师）；帝位传给孙子建文帝，在位才四年（传建文，方四祀）；明成祖把都城迁到北京，以永乐为年号继承大统（迁北京，永乐嗣）；等到末帝崇祯，在煤山自尽殉国，明朝灭亡（迨崇祯，煤山逝）。八句三言，讲完明朝的兴与亡。'," + SEP +
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
    print("  [OK] manifest: 插入 527 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 526 课", "index 共N课"):
    s = s.replace("共 526 课", "共 527 课")
else:
    ok = False
if s.count("yaoyue526") > 0:
    s = s.replace("yaoyue526", "yaoyue527")
    print(f"  [OK] index: yaoyue526 -> yaoyue527 ({s.count('yaoyue527')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue526")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(526)") > 0:
    n = s.count("toHaveCount(526)")
    s = s.replace("toHaveCount(526)", "toHaveCount(527)")
    print(f"  [OK] tests: toHaveCount(526) -> 527 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(526)")
    ok = False
if assert_once(s, "toBe('526')", "tests toBe"):
    s = s.replace("toBe('526')", "toBe('527')")
else:
    ok = False
if assert_once(s, "toHaveText('526')", "tests toHaveText"):
    s = s.replace("toHaveText('526')", "toHaveText('527')")
else:
    ok = False
# expectedChipCounts 末项 33 -> 34
if assert_once(s, " 8, 1, 33]", "tests chip 末项"):
    s = s.replace(" 8, 1, 33]", " 8, 1, 34]")
    print("  [OK] tests: expectedChipCounts 末项 33 -> 34")
else:
    ok = False
if s.count("三字经课堂=33") > 0:
    s = s.replace("三字经课堂=33", "三字经课堂=34")
    print("  [OK] tests: 注释 三字经课堂=33 -> 34")
if s.count("（合计 526）") > 0:
    s = s.replace("（合计 526）", "（合计 527）")
    print("  [OK] tests: 注释 合计 526 -> 527")
if s.count("末项 = 526") > 0:
    s = s.replace("末项 = 526", "末项 = 527")
    print("  [OK] tests: 注释 末项 526 -> 527")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/527-ming-tai-zu/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 527 条目")
else:
    ok = False

print("=== sync527 完成, 全部通过" if ok else "=== sync527 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
