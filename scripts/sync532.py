#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync532: 把 532 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '532-ru-nang-ying'," + SEP +
    "        num: '532'," + SEP +
    "        title: '如囊萤 · 如映雪'," + SEP +
    "        subtitle: '如映雪，家虽贫，学不辍；如负薪，如挂角，身虽劳，犹苦卓'," + SEP +
    "        path: 'lessons/532-ru-nang-ying/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十九课精讲：如囊萤，如映雪。家虽贫，学不辍。如负薪，如挂角。身虽劳，犹苦卓。上一课讲古人无书、无人督促仍苦读，这一课再举四位在贫苦劳作中不废学的人：晋代车胤家贫买不起灯油，夏夜捉萤火虫装进纱袋照着读；孙康冬夜借雪地反光读书；家里虽穷，学习却不中断。西汉朱买臣靠砍柴为生，担柴时仍背书；隋代李密放牛把书挂在牛角上边走边读；身子虽然劳累，用功却格外超群。八句三言告诉孩子：穷与累，都挡不住真想读书的人。'," + SEP +
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
    print("  [OK] manifest: 插入 532 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 531 课", "index 共N课"):
    s = s.replace("共 531 课", "共 532 课")
else:
    ok = False
if s.count("yaoyue531") > 0:
    s = s.replace("yaoyue531", "yaoyue532")
    print(f"  [OK] index: yaoyue531 -> yaoyue532 ({s.count('yaoyue532')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue531")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(531)") > 0:
    n = s.count("toHaveCount(531)")
    s = s.replace("toHaveCount(531)", "toHaveCount(532)")
    print(f"  [OK] tests: toHaveCount(531) -> 532 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(531)")
    ok = False
if assert_once(s, "toBe('531')", "tests toBe"):
    s = s.replace("toBe('531')", "toBe('532')")
else:
    ok = False
if assert_once(s, "toHaveText('531')", "tests toHaveText"):
    s = s.replace("toHaveText('531')", "toHaveText('532')")
else:
    ok = False
# expectedChipCounts 末项 38 -> 39
if assert_once(s, " 8, 1, 38]", "tests chip 末项"):
    s = s.replace(" 8, 1, 38]", " 8, 1, 39]")
    print("  [OK] tests: expectedChipCounts 末项 38 -> 39")
else:
    ok = False
if s.count("三字经课堂=38") > 0:
    s = s.replace("三字经课堂=38", "三字经课堂=39")
    print("  [OK] tests: 注释 三字经课堂=38 -> 39")
if s.count("（合计 531）") > 0:
    s = s.replace("（合计 531）", "（合计 532）")
    print("  [OK] tests: 注释 合计 531 -> 532")
if s.count("末项 = 531") > 0:
    s = s.replace("末项 = 531", "末项 = 532")
    print("  [OK] tests: 注释 末项 531 -> 532")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/532-ru-nang-ying/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 532 条目")
else:
    ok = False

print("=== sync532 完成, 全部通过" if ok else "=== sync532 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
