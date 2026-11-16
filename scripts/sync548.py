#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync548: 第 548 课《丧三年，常悲咽》，同步四处
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
    "        id: '548-sang-san-nian'," + SEP +
    "        num: '548'," + SEP +
    "        title: '丧三年 · 事死者、如事生'," + SEP +
    "        subtitle: '《弟子规》入则孝第七段：丧三年，常悲咽'," + SEP +
    "        path: 'lessons/548-sang-san-nian/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第八课，入则孝第七段，也是入则孝一门收官。原文「丧三年，常悲咽。居处变，酒肉绝。丧尽礼，祭尽诚。事死者，如事生。」讲父母身后的事：守丧三年，想起父母就难过，日子过得简朴；办丧事礼数要做全，祭祀时心里要真，对待去世的父母像活着时一样。孝从生前一直走到身后。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 548 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 547 课", "index 共N课", "共 548 课")
n = s.count("yaoyue547")
if n:
    s = s.replace("yaoyue547", "yaoyue548"); print(f"  [OK] index: yaoyue547 -> yaoyue548 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue547"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 547 lessons (num 01..547, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 548 lessons (num 01..548, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 547 in total)", "tests 头注释2", "(flat sorted chips, 548 in total)")
s, g2 = once(s, "series cover stats show correct counts (547/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (548/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('547'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('548'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 547 lesson cards'", "tests 平板用例名", "test('sidebar visible, 548 lesson cards'")
s, g5 = once(s, "numstrip visible with 547 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 548 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=7（合计 547）", "tests chip 注释", "弟子规课堂=8（合计 548）")
s, g7 = once(s, "8, 1, 47, 7];", "tests chip 数组", "8, 1, 47, 8];")
s = s.replace("// 全部 547 个序号 chip", "// 全部 548 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 547", "tests 末组注释", "末组「弟子规课堂」末项 = 548")
n_cards = s.count("toHaveCount(547)")
s = s.replace("toHaveCount(547)", "toHaveCount(548)")
s = s.replace("toHaveText('547')", "toHaveText('548')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 547 -> 548 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/548-sang-san-nian/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 548 条目")

print("=== sync548 完成, 全部通过" if ok else "=== sync548 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
