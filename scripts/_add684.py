# -*- coding: utf-8 -*-
"""登记第684课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「忧对喜，戚对欣。五典对三坟。佛经对仙语，夏耨对春耘。」'
        '此段见《笠翁对韵》上卷十二文其一开篇，接683课十一真其三之后，自「真」韵转入「文」韵。'
        '忧、喜、戚、欣四字皆言心境：忧为愁，喜为乐，戚为悲，欣为悦，两两同类而正反相对。'
        '戚本义为斧，借为亲属之称，又引申为悲戚，此处作悲伤解。'
        '五典、三坟为上古书籍之名，出《左传·昭公十二年》「是能读三坟、五典、八索、九丘」。'
        '孔安国《尚书序》谓伏羲、神农、黄帝之书为三坟，言大道；少昊、颛顼、高辛、唐、虞之书为五典，言常道。'
        '坟非坟墓，乃大之意。此类古书今多不存，仅余其名。'
        '佛经谓佛教典籍，自印度译入；仙语谓道家之言，如《老子》《庄子》，一外来一本土，同类相对。'
        '耨读nòu，除草；耘读yún，除草培土。夏耨对春耘，农事相同而季节相对，换字所以避复。'
        '全段四组，皆就同类中取相对者：心情对心情，典籍对典籍，教门对教门，农活对农活。'
        '落点：耕读传家，日子就稳。')

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '684-you-dui-xi' not in s, 'manifest already has 684'
entry = """    {
        num: '684',
        id: '684-you-dui-xi',
        title: '对韵 · 五典三坟，忧喜耕读（典籍与农事）',
        subtitle: '五典三坟：典籍与农事',
        path: 'lessons/684-you-dui-xi/index.html',
        grade: '小学低中年级',
        description: '%s',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'liwengduiyun',
        tier: 'core',
        featured: false
    }
""" % DESC
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
assert '共 683 课' in s
s = s.replace('共 683 课', '共 684 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '684-you-dui-xi' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/683-wang-you-han-xiao/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/684-you-dui-xi/index.html</loc>',
    '    <lastmod>2026-11-21</lastmod>',
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
assert '684' not in s
s = s.replace('683', '684')
assert '笠翁对韵课堂=96' in s
s = s.replace('笠翁对韵课堂=96', '笠翁对韵课堂=97')
assert '2, 6, 96]' in s
s = s.replace('2, 6, 96]', '2, 6, 97]')
write(p, s)
print('tests ok')
