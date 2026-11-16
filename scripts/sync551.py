#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync551: 第 551 课《称尊长，勿呼名》，同步四处
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
    "        id: '551-cheng-zun-zhang'," + SEP +
    "        num: '551'," + SEP +
    "        title: '勿呼名 · 敬在称呼与进退'," + SEP +
    "        subtitle: '《弟子规》出则悌第三段：称尊长，勿呼名'," + SEP +
    "        path: 'lessons/551-cheng-zun-zhang/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十一课，出则悌第三段。原文「称尊长，勿呼名。对尊长，勿见能。路遇长，疾趋揖。长无言，退恭立。」讲见了长辈怎么办：称呼要带称呼，不直呼其名；在长辈面前不卖弄本事、不抢话；路上遇见长辈，快步上前问好行礼；长辈没话说了，退到一旁恭敬站着。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 551 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 550 课", "index 共N课", "共 551 课")
n = s.count("yaoyue550")
if n:
    s = s.replace("yaoyue550", "yaoyue551"); print(f"  [OK] index: yaoyue550 -> yaoyue551 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue550"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 550 lessons (num 01..550, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 551 lessons (num 01..551, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 550 in total)", "tests 头注释2", "(flat sorted chips, 551 in total)")
s, g2 = once(s, "series cover stats show correct counts (550/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (551/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('550'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('551'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 550 lesson cards'", "tests 平板用例名", "test('sidebar visible, 551 lesson cards'")
s, g5 = once(s, "numstrip visible with 550 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 551 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=10（合计 550）", "tests chip 注释", "弟子规课堂=11（合计 551）")
s, g7 = once(s, "8, 1, 47, 10];", "tests chip 数组", "8, 1, 47, 11];")
s = s.replace("// 全部 550 个序号 chip", "// 全部 551 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 550", "tests 末组注释", "末组「弟子规课堂」末项 = 551")
n_cards = s.count("toHaveCount(550)")
s = s.replace("toHaveCount(550)", "toHaveCount(551)")
s = s.replace("toHaveText('550')", "toHaveText('551')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 550 -> 551 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/551-cheng-zun-zhang/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 551 条目")

print("=== sync551 完成, 全部通过" if ok else "=== sync551 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
