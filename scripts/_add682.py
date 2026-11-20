# -*- coding: utf-8 -*-
"""登记第682课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「花馥馥，叶蓁蓁。粉颈对朱唇。曹公奸似鬼，尧帝智如神。」'
        '馥馥读fù fù，香气浓盛；蓁蓁读zhēn zhēn，草木茂盛之貌，出《诗经·周南·桃夭》'
        '「桃之夭夭，其叶蓁蓁」，原是贺人新婚、祝其家室兴旺的话。'
        '粉颈谓白净的颈项，朱唇谓红润的嘴唇，粉与朱以色相对，颈与唇以部位相对，是写美人容貌的工整对法。'
        '曹公指曹操，「奸似鬼」是《三国演义》与戏曲给出的评语，非史书定论：清代毛宗岗评三国人物有「三绝」，'
        '诸葛亮智绝、关羽义绝、曹操奸绝，戏台上曹操勾白脸，白脸即奸臣的脸谱；然史书中的曹操统一北方、'
        '兴屯田、唯才是举，诗赋亦卓然可观。尧帝即陶唐氏放勋，《史记·五帝本纪》称「其仁如天，其知如神」，'
        '知即智，「智如神」三字本此；尧以天下让舜，是为禅让，孔子赞「大哉尧之为君也」。'
        '一奸一智，皆是后人给的脸；前四句写草木容颜，后两句写心中术。'
        '接681课，同属《笠翁对韵》十一真第三段。落点：颜容易老，心术留名。')

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '682-hua-fu-fu' not in s, 'manifest already has 682'
entry = """    {
        num: '682',
        id: '682-hua-fu-fu',
        title: '对韵 · 花叶容颜，奸智两般（草木与人）',
        subtitle: '花叶容颜：草木与人',
        path: 'lessons/682-hua-fu-fu/index.html',
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
assert '共 681 课' in s
s = s.replace('共 681 课', '共 682 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '682-hua-fu-fu' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/681-shen-dui-wu/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/682-hua-fu-fu/index.html</loc>',
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
assert '682' not in s
s = s.replace('681', '682')
assert '笠翁对韵课堂=94' in s
s = s.replace('笠翁对韵课堂=94', '笠翁对韵课堂=95')
assert '2, 6, 94]' in s
s = s.replace('2, 6, 94]', '2, 6, 95]')
write(p, s)
print('tests ok')
