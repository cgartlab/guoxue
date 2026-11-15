#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync542: 第 542 课《入则孝·父母呼应勿缓》，同步四处
（manifest / index / tests / sitemap）。门类与免费名单 541 已建，本课无需改动。"""
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
    "        id: '542-ru-ze-xiao-fu-mu-hu'," + SEP +
    "        num: '542'," + SEP +
    "        title: '入则孝 · 父母呼，应勿缓'," + SEP +
    "        subtitle: '《弟子规》正文第一门：父母呼，应勿缓'," + SEP +
    "        path: 'lessons/542-ru-ze-xiao-fu-mu-hu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第二课，进正文第一门入则孝。原文「父母呼，应勿缓。父母命，行勿懒。父母教，须敬听。父母责，须顺承。」讲孩子对父母的四种回应：父母叫，马上应一声，别拖着；父母交代事，赶紧去做，别偷懒；父母讲道理，恭敬地听进去；父母责备，先把话接下来，别顶嘴。呼、命、教、责是父母那边做的，应、行、听、承是我这边该做的。孝道不从大道理开始，从答应一声开始。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 542 条目")

# ---------- 2) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 541 课", "index 共N课", "共 542 课")
n = s.count("yaoyue541")
if n:
    s = s.replace("yaoyue541", "yaoyue542"); print(f"  [OK] index: yaoyue541 -> yaoyue542 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue541"); ok = False
ok = ok and g1
write(p, s)

# ---------- 3) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
s, _ = once(s, "//   - 541 lessons (num 01..541, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 542 lessons (num 01..542, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "(flat sorted chips, 541 in total)", "tests 头注释2", "(flat sorted chips, 542 in total)")
s, g2 = once(s, "series cover stats show correct counts (541/0/24)",
             "tests 统计用例名", "series cover stats show correct counts (542/0/24)")
s, g3 = once(s, "expect(vals[0]).toBe('541'); // 已上线", "tests 已上线数", "expect(vals[0]).toBe('542'); // 已上线")
s, g4 = once(s, "test('sidebar visible, 541 lesson cards'", "tests 平板用例名", "test('sidebar visible, 542 lesson cards'")
s, g5 = once(s, "numstrip visible with 541 chips and horizontal scroll", "tests 移动用例名",
             "numstrip visible with 542 chips and horizontal scroll")
s, g6 = once(s, "弟子规课堂=1（合计 541）", "tests chip 注释", "弟子规课堂=2（合计 542）")
s, g7 = once(s, "8, 1, 47, 1];", "tests chip 数组", "8, 1, 47, 2];")
s = s.replace("// 全部 541 个序号 chip", "// 全部 542 个序号 chip")
s, g8 = once(s, "末组「弟子规课堂」末项 = 541", "tests 末组注释", "末组「弟子规课堂」末项 = 542")
n_cards = s.count("toHaveCount(541)")
s = s.replace("toHaveCount(541)", "toHaveCount(542)")
s = s.replace("toHaveText('541')", "toHaveText('542')")
if not (g2 and g3 and g4 and g5 and g6 and g7 and g8):
    ok = False
write(p, s)
print(f"  [OK] tests: 541 -> 542 共 {n_cards} 处 toHaveCount")

# ---------- 4) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/542-ru-ze-xiao-fu-mu-hu/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 542 条目")

print("=== sync542 完成, 全部通过" if ok else "=== sync542 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
