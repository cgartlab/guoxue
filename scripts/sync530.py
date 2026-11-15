#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync530: 把 530 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '530-xi-zhong-ni'," + SEP +
    "        num: '530'," + SEP +
    "        title: '昔仲尼 · 师项橐'," + SEP +
    "        subtitle: '师项橐，古圣贤，尚勤学；赵中令，读鲁论，彼既仕，学且勤'," + SEP +
    "        path: 'lessons/530-xi-zhong-ni/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十七课精讲：昔仲尼，师项橐。古圣贤，尚勤学。赵中令，读鲁论。彼既仕，学且勤。上一课教了读书的方法，这一课举出勤学的榜样：从前孔子曾向七岁的项橐请教（昔仲尼，师项橐）；古代的圣贤尚且勤勉好学（古圣贤，尚勤学）；宋朝的赵普官至中书令，还常读《论语》（赵中令，读鲁论）；他已经做了大官，学习依旧勤勉（彼既仕，学且勤）。八句三言，用两位榜样告诉孩子：学问不问长幼，也不问忙闲。'," + SEP +
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
    print("  [OK] manifest: 插入 530 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 529 课", "index 共N课"):
    s = s.replace("共 529 课", "共 530 课")
else:
    ok = False
if s.count("yaoyue529") > 0:
    s = s.replace("yaoyue529", "yaoyue530")
    print(f"  [OK] index: yaoyue529 -> yaoyue530 ({s.count('yaoyue530')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue529")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(529)") > 0:
    n = s.count("toHaveCount(529)")
    s = s.replace("toHaveCount(529)", "toHaveCount(530)")
    print(f"  [OK] tests: toHaveCount(529) -> 530 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(529)")
    ok = False
if assert_once(s, "toBe('529')", "tests toBe"):
    s = s.replace("toBe('529')", "toBe('530')")
else:
    ok = False
if assert_once(s, "toHaveText('529')", "tests toHaveText"):
    s = s.replace("toHaveText('529')", "toHaveText('530')")
else:
    ok = False
# expectedChipCounts 末项 36 -> 37
if assert_once(s, " 8, 1, 36]", "tests chip 末项"):
    s = s.replace(" 8, 1, 36]", " 8, 1, 37]")
    print("  [OK] tests: expectedChipCounts 末项 36 -> 37")
else:
    ok = False
if s.count("三字经课堂=36") > 0:
    s = s.replace("三字经课堂=36", "三字经课堂=37")
    print("  [OK] tests: 注释 三字经课堂=36 -> 37")
if s.count("（合计 529）") > 0:
    s = s.replace("（合计 529）", "（合计 530）")
    print("  [OK] tests: 注释 合计 529 -> 530")
if s.count("末项 = 529") > 0:
    s = s.replace("末项 = 529", "末项 = 530")
    print("  [OK] tests: 注释 末项 529 -> 530")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/530-xi-zhong-ni/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 530 条目")
else:
    ok = False

print("=== sync530 完成, 全部通过" if ok else "=== sync530 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
