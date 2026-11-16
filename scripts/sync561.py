#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync561: 第 561 课《斗闹场，绝勿近》，同步四处
（manifest / index / tests / sitemap）。付费课，unlock.js 不动。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:26]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True

# ---------- 1) manifest（CRLF） ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '561-dou-nao-chang'," + SEP +
    "        num: '561'," + SEP +
    "        title: '斗闹场 · 远是非，讲礼貌（谨第七段）'," + SEP +
    "        subtitle: '《弟子规》谨第七段：斗闹场，绝勿近'," + SEP +
    "        path: 'lessons/561-dou-nao-chang/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第二十一课，谨第七段。原文「斗闹场，绝勿近。邪僻事，绝勿问。将入门，问孰存。将上堂，声必扬。」前四句讲远离是非：争吵打闹的场合绝不靠近，邪僻不正的事绝不打听；后四句讲进门有礼：进门先问有人在不在，上堂先出声让人知道。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'dizigui'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }" + SEP + "];"
)
s, good = once(s, old, "manifest 末条", new)
ok = ok and good
if good:
    write(p, s); print("  [OK] manifest: 插入 561 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 560 课", "index 共N课", "共 561 课")
n = s.count("yaoyue560")
if n:
    s = s.replace("yaoyue560", "yaoyue561"); print(f"  [OK] index: yaoyue560 -> yaoyue561 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue560"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 560 lessons (num 01..560, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 561 lessons (num 01..561, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 560 in total)", "tests 头注释2", "(flat sorted chips, 561 in total)")
s, g2 = once(s, "series cover stats show correct counts (560/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (561/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('560'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('561'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 560 lesson cards'", "tests 平板用例名", "test('sidebar visible, 561 lesson cards'")
s, g5 = once(s, "numstrip visible with 560 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 561 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=20（合计 560）", "tests chip 注释", "弟子规课堂=21（合计 561）")
s, g7 = once(s, "8, 1, 47, 20];", "tests chip 数组", "8, 1, 47, 21];")
s = s.replace("// 全部 560 个序号 chip", "// 全部 561 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 560", "tests 末组注释", "末组「弟子规课堂」末项 = 561")
n_cards = s.count("toHaveCount(560)")
s = s.replace("toHaveCount(560)", "toHaveCount(561)")
s = s.replace("toHaveText('560')", "toHaveText('561')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 560 -> 561 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/561-dou-nao-chang/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 561 条目")

print("=== sync561 完成, 全部通过" if ok else "=== sync561 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
