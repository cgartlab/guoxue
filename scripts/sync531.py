#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync531: 把 531 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '531-pi-pu-bian'," + SEP +
    "        num: '531'," + SEP +
    "        title: '披蒲编 · 削竹简'," + SEP +
    "        subtitle: '削竹简，彼无书，且知勉；头悬梁，锥刺股，彼不教，自勤苦'," + SEP +
    "        path: 'lessons/531-pi-pu-bian/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十八课精讲：披蒲编，削竹简。彼无书，且知勉。头悬梁，锥刺股。彼不教，自勤苦。上一课举出孔子与赵普勤学的榜样，这一课再讲四位在困苦里自学的人：西汉路温舒把蒲草编成席，借书抄在上头读；公孙弘削竹片抄书，边放猪边苦学；他们没有书，尚且知道勉力。东汉孙敬把头发系在屋梁上防打瞌睡；战国苏秦困倦时以锥刺大腿提神；没有人督促，全靠自己勤苦。八句三言告诉孩子：条件差、没人催，都不是不读书的理由。'," + SEP +
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
    print("  [OK] manifest: 插入 531 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 530 课", "index 共N课"):
    s = s.replace("共 530 课", "共 531 课")
else:
    ok = False
if s.count("yaoyue530") > 0:
    s = s.replace("yaoyue530", "yaoyue531")
    print(f"  [OK] index: yaoyue530 -> yaoyue531 ({s.count('yaoyue531')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue530")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(530)") > 0:
    n = s.count("toHaveCount(530)")
    s = s.replace("toHaveCount(530)", "toHaveCount(531)")
    print(f"  [OK] tests: toHaveCount(530) -> 531 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(530)")
    ok = False
if assert_once(s, "toBe('530')", "tests toBe"):
    s = s.replace("toBe('530')", "toBe('531')")
else:
    ok = False
if assert_once(s, "toHaveText('530')", "tests toHaveText"):
    s = s.replace("toHaveText('530')", "toHaveText('531')")
else:
    ok = False
# expectedChipCounts 末项 37 -> 38
if assert_once(s, " 8, 1, 37]", "tests chip 末项"):
    s = s.replace(" 8, 1, 37]", " 8, 1, 38]")
    print("  [OK] tests: expectedChipCounts 末项 37 -> 38")
else:
    ok = False
if s.count("三字经课堂=37") > 0:
    s = s.replace("三字经课堂=37", "三字经课堂=38")
    print("  [OK] tests: 注释 三字经课堂=37 -> 38")
if s.count("（合计 530）") > 0:
    s = s.replace("（合计 530）", "（合计 531）")
    print("  [OK] tests: 注释 合计 530 -> 531")
if s.count("末项 = 530") > 0:
    s = s.replace("末项 = 530", "末项 = 531")
    print("  [OK] tests: 注释 末项 530 -> 531")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/531-pi-pu-bian/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 531 条目")
else:
    ok = False

print("=== sync531 完成, 全部通过" if ok else "=== sync531 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
