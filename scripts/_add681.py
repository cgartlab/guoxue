# -*- coding: utf-8 -*-
"""登记第681课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「申对午，侃对訚。阿魏对茵陈。楚兰对湘芷，碧柳对青筠。」'
        '申、午为十二地支中两位，午第七、申第九，一个时辰两小时，午时当上午十一时至下午一时，'
        '申时当下午三时至五时，平仄上午仄申平，同类相对故成对。侃读kǎn，刚直而和乐；訚读yín，'
        '说话和悦而持正不阿，二字出《论语·乡党》「朝，与下大夫言，侃侃如也；与上大夫言，訚訚如也」。'
        '阿魏为伞形科植物，药取其根部渗出的树脂，气味极臭，能消积杀虫；茵陈即茵陈蒿，早春采嫩苗入药，'
        '气香，为退黄疸要药，杜甫《陪郑广文游何将军山林》有「茵陈春藕香」句。'
        '楚兰谓产于楚地之兰，香草，古人佩以祓除；湘芷谓湘水一带之白芷，同属香草，'
        '《离骚》「纫秋兰以为佩」，香草以喻君子。筠读yún，本指竹之青皮，亦代指竹；'
        '碧柳对青筠，色同而种异，一柔一挺。接680课，同属《笠翁对韵》十一真第三段开篇。'
        '落点：说话看人，分寸在己。')

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '681-shen-dui-wu' not in s, 'manifest already has 681'
entry = """    {
        num: '681',
        id: '681-shen-dui-wu',
        title: '对韵 · 时辰药草，侃侃訚訚（名物与说话）',
        subtitle: '时辰药草：名物与说话',
        path: 'lessons/681-shen-dui-wu/index.html',
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
assert '共 680 课' in s
s = s.replace('共 680 课', '共 681 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '681-shen-dui-wu' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/680-ren-jiao-hao-you/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/681-shen-dui-wu/index.html</loc>',
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
assert '681' not in s
s = s.replace('680', '681')
assert '笠翁对韵课堂=93' in s
s = s.replace('笠翁对韵课堂=93', '笠翁对韵课堂=94')
assert '2, 6, 93]' in s
s = s.replace('2, 6, 93]', '2, 6, 94]')
write(p, s)
print('tests ok')
