#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync533: 把 533 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '533-su-lao-quan'," + SEP +
    "        num: '533'," + SEP +
    "        title: '苏老泉 · 二十七'," + SEP +
    "        subtitle: '二十七，始发愤，读书籍；彼既老，犹悔迟，尔小生，宜早思'," + SEP +
    "        path: 'lessons/533-su-lao-quan/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十课精讲：苏老泉，二十七。始发愤，读书籍。彼既老，犹悔迟。尔小生，宜早思。上一课讲家贫身劳仍不废学，这一课换个角度讲什么时候开始读书：北宋苏洵号老泉，到二十七岁才下定决心发愤读书，后来成了大文章家；可他年纪大了，仍后悔起步太晚；所以《三字经》转过来叮嘱小孩子：你们该趁早想着用功。八句三言告诉孩子：晚学固然能成，早学更不辜负光阴。'," + SEP +
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
    print("  [OK] manifest: 插入 533 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 532 课", "index 共N课"):
    s = s.replace("共 532 课", "共 533 课")
else:
    ok = False
if s.count("yaoyue532") > 0:
    s = s.replace("yaoyue532", "yaoyue533")
    print(f"  [OK] index: yaoyue532 -> yaoyue533 ({s.count('yaoyue533')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue532")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(532)") > 0:
    n = s.count("toHaveCount(532)")
    s = s.replace("toHaveCount(532)", "toHaveCount(533)")
    print(f"  [OK] tests: toHaveCount(532) -> 533 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(532)")
    ok = False
if assert_once(s, "toBe('532')", "tests toBe"):
    s = s.replace("toBe('532')", "toBe('533')")
else:
    ok = False
if assert_once(s, "toHaveText('532')", "tests toHaveText"):
    s = s.replace("toHaveText('532')", "toHaveText('533')")
else:
    ok = False
# expectedChipCounts 末项 39 -> 40
if assert_once(s, " 8, 1, 39]", "tests chip 末项"):
    s = s.replace(" 8, 1, 39]", " 8, 1, 40]")
    print("  [OK] tests: expectedChipCounts 末项 39 -> 40")
else:
    ok = False
if s.count("三字经课堂=39") > 0:
    s = s.replace("三字经课堂=39", "三字经课堂=40")
    print("  [OK] tests: 注释 三字经课堂=39 -> 40")
if s.count("（合计 532）") > 0:
    s = s.replace("（合计 532）", "（合计 533）")
    print("  [OK] tests: 注释 合计 532 -> 533")
if s.count("末项 = 532") > 0:
    s = s.replace("末项 = 532", "末项 = 533")
    print("  [OK] tests: 注释 末项 532 -> 533")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/533-su-lao-quan/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 533 条目")
else:
    ok = False

print("=== sync533 完成, 全部通过" if ok else "=== sync533 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
