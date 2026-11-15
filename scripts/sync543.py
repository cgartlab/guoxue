#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync543: 第 543 课《冬温夏凊·晨省昏定》，同步四处
（manifest / index / tests / sitemap）。门类与免费名单前课已建。"""
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
    "        id: '543-dong-wen-xia-qing'," + SEP +
    "        num: '543'," + SEP +
    "        title: '冬温夏凊 · 晨省昏定'," + SEP +
    "        subtitle: '《弟子规》入则孝第二段：晨则省，昏则定'," + SEP +
    "        path: 'lessons/543-dong-wen-xia-qing/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第三课，入则孝第二段。原文「冬则温，夏则凊。晨则省，昏则定。出必告，反必面。居有常，业无变。」讲四件事：冬天替父母暖、夏天替父母凉；早晨问安、晚上安顿；出门说一声、回来照个面；住处作息有定准、本业踏实做。上一课讲叫一声就应，这一课讲把父母放在心上。东汉黄香九岁温席，就是冬则温的来历。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 543 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 542 课", "index 共N课", "共 543 课")
n = s.count("yaoyue542")
if n:
    s = s.replace("yaoyue542", "yaoyue543"); print(f"  [OK] index: yaoyue542 -> yaoyue543 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue542"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 542 lessons (num 01..542, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 543 lessons (num 01..543, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 542 in total)", "tests 头注释2", "(flat sorted chips, 543 in total)")
s, g2 = once(s, "series cover stats show correct counts (542/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (543/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('542'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('543'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 542 lesson cards'", "tests 平板用例名", "test('sidebar visible, 543 lesson cards'")
s, g5 = once(s, "numstrip visible with 542 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 543 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=2（合计 542）", "tests chip 注释", "弟子规课堂=3（合计 543）")
s, g7 = once(s, "8, 1, 47, 2];", "tests chip 数组", "8, 1, 47, 3];")
s = s.replace("// 全部 542 个序号 chip", "// 全部 543 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 542", "tests 末组注释", "末组「弟子规课堂」末项 = 543")
n_cards = s.count("toHaveCount(542)")
s = s.replace("toHaveCount(542)", "toHaveCount(543)")
s = s.replace("toHaveText('542')", "toHaveText('543')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 542 -> 543 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/543-dong-wen-xia-qing/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 543 条目")

print("=== sync543 完成, 全部通过" if ok else "=== sync543 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
