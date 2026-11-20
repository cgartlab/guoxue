# -*- coding: utf-8 -*-
"""登记第677课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '677-chao-yan-sai-hong' not in s, 'manifest already has 677'
entry = """    {
        num: '677',
        id: '677-chao-yan-sai-hong',
        title: '对韵 · 春燕秋鸿，泰山沧海（守时与无常）',
        subtitle: '燕鸿砺尘：守时与无常',
        path: 'lessons/677-chao-yan-sai-hong/index.html',
        grade: '小学低中年级',
        description: '对韵段，原文：「巢燕三春尝唤友，塞鸿八月始来宾。古往今来，谁见泰山曾作砺；天长地久，人传沧海几扬尘。」巢燕为檐下筑巢之燕，三春指孟春仲春季春，尝读cháng为曾经常常，唤友出《诗经·小雅·伐木》「嘤其鸣矣，求其友声」；塞鸿为边塞南飞之雁，塞读sài，八月始来宾本《礼记·月令》仲秋之月鸿雁来，宾谓把雁当守礼远客。砺读lì为磨刀石，泰山作砺出《史记·高祖功臣侯者年表》封爵之誓「使河如带，泰山若厉」，言纵使黄河细如衣带、泰山磨成砺石，封国亦不绝；沧海扬尘出《神仙传》，麻姑自言已见东海三为桑田。前二句写候鸟守时，后二句写时间无常。接676课，同属《笠翁对韵》十一真第一段。落点：天地也会老，人只争朝夕。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'liwengduiyun',
        tier: 'core',
        featured: false
    }
"""
m = None
for pat in ['    }\r\n];', '    }\n];']:
    i = s.rfind(pat)
    if i != -1:
        m = (i, pat); break
assert m, 'manifest tail not found'
i, pat = m
nl = '\r\n' if '\r\n' in pat else '\n'
s = s[:i] + '    },' + nl + entry.replace('\n', nl) + '];' + s[i+len(pat):]
write(p, s)
print('manifest ok')

# ---------- 2. index.html ----------
p = 'index.html'
s = read(p)
assert '共 676 课' in s
s = s.replace('共 676 课', '共 677 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '677-chao-yan-sai-hong' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/676-luo-yue-sou/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/677-chao-yan-sai-hong/index.html</loc>',
    '    <lastmod>2026-11-20</lastmod>',
    '    <changefreq>weekly</changefreq>',
    '    <priority>0.8</priority>',
    '  </url>',
])
s = s[:j] + nl + block + s[j:]
write(p, s)
print('sitemap ok')

# ---------- 4. tests ----------
p = 'tests/homepage.spec.js'
s = read(p)
assert '677' not in s
s = s.replace('676', '677')
# chip 组数：笠翁对韵课堂 89 -> 90
assert '笠翁对韵课堂=89' in s
s = s.replace('笠翁对韵课堂=89', '笠翁对韵课堂=90')
assert '2, 6, 89]' in s
s = s.replace('2, 6, 89]', '2, 6, 90]')
write(p, s)
print('tests ok')
