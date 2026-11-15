#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync528: 把 528 同步到四处（manifest / index.html / tests / sitemap）。"""
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
    "        id: '528-qing-tai-zu'," + SEP +
    "        num: '528'," + SEP +
    "        title: '清太祖 · 膺景命'," + SEP +
    "        subtitle: '膺景命，靖四方，克大定；至世祖，乃大同，十二世，清祚终'," + SEP +
    "        path: 'lessons/528-qing-tai-zu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第三十五课精讲：清太祖，膺景命。靖四方，克大定。至世祖，乃大同。十二世，清祚终。上一课讲了明朝的兴与亡——布衣开国、传位建文、成祖迁都北京，到崇祯煤山殉国。这一课接着讲：清太祖努尔哈赤承受天命、统一女真，为清朝奠定基业（清太祖，膺景命）；平定四方，大局安定（靖四方，克大定）；到清世祖顺治入关定鼎，天下归一（至世祖，乃大同）；自太祖至宣统共传十二帝，清朝国祚终结（十二世，清祚终）。八句三言，讲完清朝的兴与亡，也为整段朝代更替收尾。'," + SEP +
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
    print("  [OK] manifest: 插入 528 条目")
else:
    ok = False

# ---------- 2) index.html (LF) ----------
p = f"{ROOT}/index.html"
s = read(p)
if assert_once(s, "共 527 课", "index 共N课"):
    s = s.replace("共 527 课", "共 528 课")
else:
    ok = False
if s.count("yaoyue527") > 0:
    s = s.replace("yaoyue527", "yaoyue528")
    print(f"  [OK] index: yaoyue527 -> yaoyue528 ({s.count('yaoyue528')} 处)")
else:
    print("  [WARN] index: 未找到 yaoyue527")
    ok = False
write(p, s)

# ---------- 3) tests (CRLF) ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if s.count("toHaveCount(527)") > 0:
    n = s.count("toHaveCount(527)")
    s = s.replace("toHaveCount(527)", "toHaveCount(528)")
    print(f"  [OK] tests: toHaveCount(527) -> 528 ({n} 处)")
else:
    print("  [WARN] tests: 未找到 toHaveCount(527)")
    ok = False
if assert_once(s, "toBe('527')", "tests toBe"):
    s = s.replace("toBe('527')", "toBe('528')")
else:
    ok = False
if assert_once(s, "toHaveText('527')", "tests toHaveText"):
    s = s.replace("toHaveText('527')", "toHaveText('528')")
else:
    ok = False
# expectedChipCounts 末项 34 -> 35
if assert_once(s, " 8, 1, 34]", "tests chip 末项"):
    s = s.replace(" 8, 1, 34]", " 8, 1, 35]")
    print("  [OK] tests: expectedChipCounts 末项 34 -> 35")
else:
    ok = False
if s.count("三字经课堂=34") > 0:
    s = s.replace("三字经课堂=34", "三字经课堂=35")
    print("  [OK] tests: 注释 三字经课堂=34 -> 35")
if s.count("（合计 527）") > 0:
    s = s.replace("（合计 527）", "（合计 528）")
    print("  [OK] tests: 注释 合计 527 -> 528")
if s.count("末项 = 527") > 0:
    s = s.replace("末项 = 527", "末项 = 528")
    print("  [OK] tests: 注释 末项 527 -> 528")
write(p, s)

# ---------- 4) sitemap (LF) ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
entry = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/528-qing-tai-zu/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "    </url>" + "\n"
)
if assert_once(s, "</urlset>", "sitemap urlset"):
    s = s.replace("</urlset>", entry + "</urlset>", 1)
    write(p, s)
    print("  [OK] sitemap: 插入 528 条目")
else:
    ok = False

print("=== sync528 完成, 全部通过" if ok else "=== sync528 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
