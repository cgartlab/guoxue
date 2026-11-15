#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync538: 把 538 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '538-you-wei-zhe'," + SEP +
    "        num: '538'," + SEP +
    "        title: '有为者 · 亦若是'," + SEP +
    "        subtitle: '亦若是，犬守夜；苟不学，曷为人，人不学，不如物'," + SEP +
    "        path: 'lessons/538-you-wei-zhe/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第四十五课精讲：有为者，亦若是。犬守夜，鸡司晨。苟不学，曷为人。蚕吐丝，蜂酿蜜。人不学，不如物。上一课讲神童七岁任事、年少有为，这一课把话收到每个人身上：有作为的人也能像他那样；狗守夜、鸡报晓各守本分；人若不学习，怎么配叫人；蚕吐丝、蜂酿蜜，连小虫都做出有用的东西；所以不学的人连它们都不如。十句三言告诉孩子：万物都在尽本分，人更要学、更要有用。'," + SEP +
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
    print("  [OK] manifest: 插入 538 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 537 课", "index 共N课"):
    s = s.replace("共 537 课", "共 538 课")
else:
    ok = False
if s.count("yaoyue537") > 0:
    n = s.count("yaoyue537")
    s = s.replace("yaoyue537", "yaoyue538")
    print(f"  [OK] index: yaoyue537 -> yaoyue538 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue537")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(537)") > 0:
    n = s.count("toHaveCount(537)")
    s = s.replace("toHaveCount(537)", "toHaveCount(538)")
    print(f"  [OK] tests: toHaveCount(537) -> 538 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(537)")
    ok = False
if assert_once(s, "toBe('537')", "tests toBe"):
    s = s.replace("toBe('537')", "toBe('538')")
else:
    ok = False
if assert_once(s, "toHaveText('537')", "tests toHaveText"):
    s = s.replace("toHaveText('537')", "toHaveText('538')")
else:
    ok = False
if assert_once(s, " 8, 1, 44]", "tests chip 末项"):
    s = s.replace(" 8, 1, 44]", " 8, 1, 45]")
    print("  [OK] tests: expectedChipCounts 末项 44 -> 45")
else:
    ok = False
if s.count("三字经课堂=44") > 0:
    s = s.replace("三字经课堂=44", "三字经课堂=45")
    print("  [OK] tests: 注释 三字经课堂=44 -> 45")
if s.count("（合计 537）") > 0:
    s = s.replace("（合计 537）", "（合计 538）")
    print("  [OK] tests: 注释 合计 537 -> 538")
if s.count("末项 = 537") > 0:
    s = s.replace("末项 = 537", "末项 = 538")
    print("  [OK] tests: 注释 末项 537 -> 538")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/538-you-wei-zhe/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-16</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 538 条目")
else:
    ok = False

print("=== sync538 完成, 全部通过" if ok else "=== sync538 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
