#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync557: 第 557 课《衣贵洁，不贵华》，同步四处
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
    "        id: '557-yi-gui-jie'," + SEP +
    "        num: '557'," + SEP +
    "        title: '衣贵洁 · 穿吃有度（谨第三段）'," + SEP +
    "        subtitle: '《弟子规》谨第三段：衣贵洁，不贵华'," + SEP +
    "        path: 'lessons/557-yi-gui-jie/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十七课，谨第三段。原文「衣贵洁，不贵华。上循分，下称家。对饮食，勿拣择。食适可，勿过则。」讲穿衣吃饭的度：衣服干净就好不攀比，合乎身份与家境；吃饭不挑食，吃到合适就停，不暴饮暴食。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 557 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 556 课", "index 共N课", "共 557 课")
n = s.count("yaoyue556")
if n:
    s = s.replace("yaoyue556", "yaoyue557"); print(f"  [OK] index: yaoyue556 -> yaoyue557 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue556"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 556 lessons (num 01..556, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 557 lessons (num 01..557, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 556 in total)", "tests 头注释2", "(flat sorted chips, 557 in total)")
s, g2 = once(s, "series cover stats show correct counts (556/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (557/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('556'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('557'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 556 lesson cards'", "tests 平板用例名", "test('sidebar visible, 557 lesson cards'")
s, g5 = once(s, "numstrip visible with 556 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 557 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=16（合计 556）", "tests chip 注释", "弟子规课堂=17（合计 557）")
s, g7 = once(s, "8, 1, 47, 16];", "tests chip 数组", "8, 1, 47, 17];")
s = s.replace("// 全部 556 个序号 chip", "// 全部 557 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 556", "tests 末组注释", "末组「弟子规课堂」末项 = 557")
n_cards = s.count("toHaveCount(556)")
s = s.replace("toHaveCount(556)", "toHaveCount(557)")
s = s.replace("toHaveText('556')", "toHaveText('557')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 556 -> 557 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/557-yi-gui-jie/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 557 条目")

print("=== sync557 完成, 全部通过" if ok else "=== sync557 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
