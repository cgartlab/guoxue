# -*- coding: utf-8 -*-
"""登记第678课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '678-xiong-dui-di' not in s, 'manifest already has 678'
entry = """    {
        num: '678',
        id: '678-xiong-dui-di',
        title: '对韵 · 弟兄吏民，勾丁赴卯（伦常与当差）',
        subtitle: '弟兄君臣：伦常与当差',
        path: 'lessons/678-xiong-dui-di/index.html',
        grade: '小学低中年级',
        description: '对韵段，原文：「兄对弟，吏对民。父子对君臣。勾丁对甫甲，赴卯对同寅。」兄对弟谓长幼有序，《三字经》「兄则友，弟则恭」；吏对民谓衙门办事之小吏对种田做工之百姓；父子对君臣谓血缘之上下对名分之上下，《论语》「君君，臣臣，父父，子子」，古人合父子君臣兄弟夫妇朋友为五伦。勾丁谓按户籍勾取成年男子服役，丁为壮丁、亦天干之一；甫读fǔ是刚刚、才，甲为甲士、亦天干之首，甫甲即刚及龄入册之丁壮，丁对甲、勾对甫，一征调一初始。赴卯谓卯时晨五至七时到衙门点名，故称点卯，迟到曰误卯；同寅谓同衙之僚属，出《尚书》「同寅协恭和衷哉」，寅在卯前一位，时辰天然成对。前四句讲名分，后两句讲当差。接677课，同属《笠翁对韵》十一真第二段。落点：人各有位，位各有分。',
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
assert '共 677 课' in s
s = s.replace('共 677 课', '共 678 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '678-xiong-dui-di' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/677-chao-yan-sai-hong/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/678-xiong-dui-di/index.html</loc>',
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
assert '678' not in s
s = s.replace('677', '678')
assert '笠翁对韵课堂=90' in s
s = s.replace('笠翁对韵课堂=90', '笠翁对韵课堂=91')
assert '2, 6, 90]' in s
s = s.replace('2, 6, 90]', '2, 6, 91]')
write(p, s)
print('tests ok')
