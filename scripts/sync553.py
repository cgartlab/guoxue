#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync553: 第 553 课《尊长前，声要低》，同步四处
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
    "        id: '553-zun-zhang-qian'," + SEP +
    "        num: '553'," + SEP +
    "        title: '声要低 · 敬在声音与进退'," + SEP +
    "        subtitle: '《弟子规》出则悌第五段：尊长前，声要低'," + SEP +
    "        path: 'lessons/553-zun-zhang-qian/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十三课，出则悌第五段。原文「尊长前，声要低。低不闻，却非宜。进必趋，退必迟。问起对，视勿移。」讲在长辈跟前怎么办：说话声音放低，但低到听不见也不合适；叫你就快些过去，退出来要慢；长辈问话，站起来答，目光看着长辈。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 553 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 552 课", "index 共N课", "共 553 课")
n = s.count("yaoyue552")
if n:
    s = s.replace("yaoyue552", "yaoyue553"); print(f"  [OK] index: yaoyue552 -> yaoyue553 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue552"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 552 lessons (num 01..552, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 553 lessons (num 01..553, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 552 in total)", "tests 头注释2", "(flat sorted chips, 553 in total)")
s, g2 = once(s, "series cover stats show correct counts (552/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (553/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('552'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('553'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 552 lesson cards'", "tests 平板用例名", "test('sidebar visible, 553 lesson cards'")
s, g5 = once(s, "numstrip visible with 552 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 553 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=12（合计 552）", "tests chip 注释", "弟子规课堂=13（合计 553）")
s, g7 = once(s, "8, 1, 47, 12];", "tests chip 数组", "8, 1, 47, 13];")
s = s.replace("// 全部 552 个序号 chip", "// 全部 553 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 552", "tests 末组注释", "末组「弟子规课堂」末项 = 553")
n_cards = s.count("toHaveCount(552)")
s = s.replace("toHaveCount(552)", "toHaveCount(553)")
s = s.replace("toHaveText('552')", "toHaveText('553')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 552 -> 553 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/553-zun-zhang-qian/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 553 条目")

print("=== sync553 完成, 全部通过" if ok else "=== sync553 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
