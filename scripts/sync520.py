#!/usr/bin/env python3
# sync520.py —— 第520课四处同步
import io

CRLF = '\r\n'
LF = '\n'
B = 'https://guoxue.8023laozhanshi.cc'

# ---------- 1. manifest (CRLF) ----------
mp = 'assets/js/lessons-manifest.js'
m = io.open(mp, 'r', newline='').read()
old_m = "        featured: false" + CRLF + "    }" + CRLF + "];"
new_m = (
    "        featured: false" + CRLF +
    "    }," + CRLF +
    "    {" + CRLF +
    "        id: '520-ying-qin-shi'," + CRLF +
    "        num: '520'," + CRLF +
    "        title: '嬴秦氏 · 始兼并'," + CRLF +
    "        subtitle: '传二世，楚汉争；高祖兴，汉业建，至孝平，王莽篡'," + CRLF +
    "        path: 'lessons/520-ying-qin-shi/index.html'," + CRLF +
    "        grade: '小学低中年级'," + CRLF +
    "        description: '《三字经》第二十七课精讲：嬴秦氏，始兼并。传二世，楚汉争。高祖兴，汉业建。至孝平，王莽篡。上一课讲了战国七雄并出——东周乱世终结于秦。这一课接着讲：秦国（嬴秦氏）起兵吞并六国、统一天下（始兼并）；秦朝传到第二代便灭亡，随后项羽刘邦争夺天下（传二世，楚汉争）；汉高祖刘邦兴起，建立汉朝基业（高祖兴，汉业建）；传到汉平帝时，外戚王莽篡夺汉位（至孝平，王莽篡）。八句六言，讲完秦的统一与速亡、楚汉相争到汉朝兴起与王莽篡汉。'," + CRLF +
    "        status: 'ready'," + CRLF +
    "        duration: '约 15 分钟'," + CRLF +
    "        subject: 'sanzijing'," + CRLF +
    "        tier: 'core'," + CRLF +
    "        featured: false" + CRLF +
    "    }" + CRLF +
    "];"
)
assert old_m in m, "manifest old 未匹配"
m = m.replace(old_m, new_m, 1)
io.open(mp, 'w', newline='').write(m)
print("manifest 已加 520 条目")

# ---------- 2. index.html (LF) ----------
ip = 'index.html'
i = io.open(ip, 'r', newline='').read()
assert "共 519 课" in i
i = i.replace("共 519 课", "共 520 课")
i = i.replace("yaoyue519", "yaoyue520")
io.open(ip, 'w', newline='').write(i)
print("index 共520课 & yaoyue520 完成")

# ---------- 3. tests (CRLF) ----------
tp = 'tests/homepage.spec.js'
t = io.open(tp, 'r', newline='').read()
# a. expectedChipCounts 末项 26 -> 27
assert ", 1, 26]" in t, "chip 末项未匹配"
t = t.replace(", 1, 26]", ", 1, 27]")
# b. 注释 三字经课堂=26（合计 519）
assert "三字经课堂=26（合计 519）" in t
t = t.replace("三字经课堂=26（合计 519）", "三字经课堂=27（合计 520）")
# c. 其余 519 -> 520
t = t.replace("519", "520")
io.open(tp, 'w', newline='').write(t)
print("tests 计数520 & chip27 完成")

# ---------- 4. sitemap (LF) ----------
sp = 'sitemap.xml'
s = io.open(sp, 'r', newline='').read()
url520 = (
    LF + "  <url>" + LF +
    "    <loc>" + B + "/lessons/520-ying-qin-shi/index.html</loc>" + LF +
    "    <lastmod>2026-11-15</lastmod>" + LF +
    "    <changefreq>weekly</changefreq>" + LF +
    "    <priority>0.8</priority>" + LF +
    "  </url>" + LF + "</urlset>"
)
assert "</urlset>" in s, "sitemap 无 urlset"
s = s.replace("</urlset>", url520, 1)
io.open(sp, 'w', newline='').write(s)
print("sitemap 已补 520 条目")

print("=== sync520 全部完成 ===")
