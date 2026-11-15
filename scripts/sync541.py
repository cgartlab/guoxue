#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync541: 新门类 dizigui + 第 541 课，同步六处
（categories / unlock 免费名单 / manifest / index / tests / sitemap）。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:24]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True

# ---------- 1) categories.js：新增弟子规门类 ----------
p = f"{ROOT}/assets/data/categories.js"
s = read(p)
SEP = "\r\n" if "\r\n" in s else "\n"
old = ("        description: '《三字经》逐句精讲 · 独立课堂'," + SEP +
       "        status: 'ready'," + SEP +
       "        order: 23" + SEP +
       "    }" + SEP + "];")
new = ("        description: '《三字经》逐句精讲 · 独立课堂'," + SEP +
       "        status: 'ready'," + SEP +
       "        order: 23" + SEP +
       "    }," + SEP +
       "    {" + SEP +
       "        key: 'dizigui'," + SEP +
       "        label: '弟子规课堂'," + SEP +
       "        num: '24'," + SEP +
       "        description: '《弟子规》逐句精讲 · 先做人后学文'," + SEP +
       "        status: 'ready'," + SEP +
       "        order: 24" + SEP +
       "    }" + SEP + "];")
s, good = once(s, old, "categories 末条", new)
ok = ok and good
if good:
    write(p, s); print("  [OK] categories: 新增 dizigui（num 24）")

# ---------- 2) unlock.js：弟子规前五课免费 ----------
p = f"{ROOT}/assets/js/unlock.js"
s = read(p)
old = ("        // 免费学科门类(该门类下所有课程一律免费)")
new = ("""        // 弟子规课堂前 5 课(541-545)免费试看,与三字经课堂同一策略;546 课起付费
        freePrefixes: ['541-', '542-', '543-', '544-', '545-'],
        // 免费学科门类(该门类下所有课程一律免费)""")
s, good = once(s, old, "unlock 配置项", new)
ok = ok and good
old2 = """    function isCourseFree(courseId) {
        // 1. 显式白名单
        for (var i = 0; i < CONFIG.freeCourses.length; i++) {
            if (CONFIG.freeCourses[i] === courseId) return true;
        }"""
new2 = """    function isCourseFree(courseId) {
        // 1. 显式白名单
        for (var i = 0; i < CONFIG.freeCourses.length; i++) {
            if (CONFIG.freeCourses[i] === courseId) return true;
        }
        // 1b. 白名单前缀(按课程序号段免费,如弟子规 541-545)
        var prefixes = CONFIG.freePrefixes || [];
        for (var k = 0; k < prefixes.length; k++) {
            if (courseId && courseId.indexOf(prefixes[k]) === 0) return true;
        }"""
s, good2 = once(s, old2, "unlock 判定函数", new2)
ok = ok and good2
if good and good2:
    write(p, s); print("  [OK] unlock: 541-545 免费前缀")

# ---------- 3) manifest（CRLF） ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
SEP = "\r\n"
old = "        featured: false" + SEP + "    }" + SEP + "];"
new = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '541-dizigui-kaipian'," + SEP +
    "        num: '541'," + SEP +
    "        title: '走近弟子规 · 作者与时代'," + SEP +
    "        subtitle: '李毓秀原著，康熙年间成书；先认书，再读书'," + SEP +
    "        path: 'lessons/541-dizigui-kaipian/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第一课（导论）：先认书，不急着背句子。作者李毓秀（1647—1729），字子潜，号采三，山西绛州人，康熙年间的秀才，一生没做官，在乡里教书，人称李夫子，写下启蒙课本《训蒙文》；后来清代山西浮山人贾存仁修订改编，改名《弟子规》。时代背景是康熙年间天下初定、朝廷重教化，各地办社学义学，村塾需要浅近易诵的规矩书。全书三字一句、两句一韵，360 句 1080 字，分总叙与七门。'," + SEP +
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
    write(p, s); print("  [OK] manifest: 插入 541 条目")

# ---------- 4) index.html ----------
p = f"{ROOT}/index.html"
s = read(p)
s, g1 = once(s, "共 540 课", "index 共N课", "共 541 课")
s, g2 = once(s, "兼蒙学启蒙 · 三字经课堂 · 共 541 课", "index 简介", "兼蒙学启蒙 · 三字经课堂 · 弟子规课堂 · 共 541 课")
n = s.count("yaoyue540")
if n:
    s = s.replace("yaoyue540", "yaoyue541"); print(f"  [OK] index: yaoyue540 -> yaoyue541 ({n} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue540"); ok = False
ok = ok and g1 and g2
write(p, s)

# ---------- 5) tests ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
old = "    const vals = await values.allTextContents();"
s, _ = once(s, "//   - 521 lessons (num 01..521, all status:'ready') in lessons-manifest.js",
            "tests 头注释1", "//   - 541 lessons (num 01..541, all status:'ready') in lessons-manifest.js")
s, _ = once(s, "//   - 23 categories (…/mengxue/sanzijing, num 01..23, all ready)",
            "tests 头注释2", "//   - 24 categories (…/mengxue/sanzijing/dizigui, num 01..24, all ready)")
s, _ = once(s, "//   - Sidebar rendered by homepage.js: 23 groups, collapsed sub-navs, filter + reset links",
            "tests 头注释3", "//   - Sidebar rendered by homepage.js: 24 groups, collapsed sub-navs, filter + reset links")
s, _ = once(s, "//   - Mobile (<768px): sidebar hidden, top numstrip visible (flat sorted chips, 521 in total)",
            "tests 头注释4", "//   - Mobile (<768px): sidebar hidden, top numstrip visible (flat sorted chips, 541 in total)")
s, _ = once(s, "sidebar renders 22 ready categories (default collapsed)",
            "tests 用例名", "sidebar renders 24 ready categories (default collapsed)")
s, _ = once(s, "series cover stats show correct counts (521/0/23)",
            "tests 统计用例名", "series cover stats show correct counts (541/0/24)")
s, _ = once(s, "sidebar visible, 521 lesson cards", "tests 平板用例名", "sidebar visible, 541 lesson cards")
s, _ = once(s, "sidebar hidden, numstrip visible with 521 chips", "tests 移动用例名", "sidebar hidden, numstrip visible with 541 chips")

n_groups = s.count("await expect(groups).toHaveCount(23);")
s = s.replace("await expect(groups).toHaveCount(23);", "await expect(groups).toHaveCount(24);")
n_head = s.count("await expect(headers).toHaveCount(23);")
s = s.replace("await expect(headers).toHaveCount(23);", "await expect(headers).toHaveCount(24);")
n_cards = s.count("toHaveCount(540)")
s = s.replace("toHaveCount(540)", "toHaveCount(541)")
s, gv = once(s, "expect(vals[2]).toBe('23'); // 学科门类", "tests 门类数", "expect(vals[2]).toBe('24'); // 学科门类")
s, gt = once(s, "expect(vals[0]).toBe('540'); // 已上线", "tests 已上线", "expect(vals[0]).toBe('541'); // 已上线")
s = s.replace('toHaveText(\'540\')', 'toHaveText(\'541\')')
s, gl = once(s, "'季氏', '阳货', '微子', '子张', '尧曰', '蒙学', '三字经课堂']",
             "tests labels 数组", "'季氏', '阳货', '微子', '子张', '尧曰', '蒙学', '三字经课堂', '弟子规课堂']")
s, gc = once(s, " 8, 1, 47]", "tests chip 数组", " 8, 1, 47, 1]")
s, gcm = once(s, "三字经课堂=47（合计 540）", "tests chip 注释", "三字经课堂=47、弟子规课堂=1（合计 541）")
s, gcm2 = once(s, "末组「三字经课堂」末项 = 540", "tests 末组注释", "末组「弟子规课堂」末项 = 541")
s = s.replace("// 全部 521 个序号 chip", "// 全部 541 个序号 chip")
if not (gv and gt and gl and gc and gcm and gcm2):
    ok = False
write(p, s)
print(f"  [OK] tests: groups/headers 23->24 ({n_groups}/{n_head}) 处, toHaveCount 540->541 ({n_cards}) 处")

# ---------- 6) sitemap ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = ("  <url>" + "\n" +
         "    <loc>https://guoxue.8023laozhanshi.cc/lessons/541-dizigui-kaipian/index.html</loc>" + "\n" +
         "    <lastmod>2026-11-16</lastmod>" + "\n" +
         "    <changefreq>weekly</changefreq>" + "\n" +
         "    <priority>0.8</priority>" + "\n" +
         "    </url>" + "\n")
s, good = once(s, "</urlset>", "sitemap urlset", entry + "</urlset>")
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 插入 541 条目")

print("=== sync541 完成, 全部通过" if ok else "=== sync541 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
