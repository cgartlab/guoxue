# -*- coding: utf-8 -*-
"""登记第683课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「南阮才郎差北富，东邻丑女效西颦。色艳北堂，草号忘忧忧甚事；'
        '香浓南国，花名含笑笑何人。」'
        '南阮北阮出《世说新语·任诞》：阮咸（字仲容）与阮籍居道南，诸阮居道北，北阮富而南阮贫；'
        '七月七日北阮盛晒纱罗锦绮，阮咸以竹竿挂大布犊鼻裈于中庭，人怪之，答曰「未能免俗，聊复尔耳」。'
        '差读chā，谓相差、比不上，贫富相形而才名自在。'
        '东邻丑女效西颦用《庄子·天运》「东施效颦」事：西施病心而颦，其里之丑人见而美之，'
        '归亦捧心而颦，富人见之闭门不出，贫人见之挈妻子而去；原文止称「其里之丑人」，'
        '「东施」是后人给的名字。所效者形，所不知者所以美，故庄子曰「彼知颦美，而不知颦之所以美」。'
        '北堂为古代居室东房后部，主妇所居，后借指母亲；忘忧草即萱草，'
        '《诗经·卫风·伯兮》「焉得谖草，言树之背」，谖草即萱草，背即北堂，故萱草又称母亲花。'
        '含笑为木兰科常绿灌木，产于岭南闽粤，花淡黄带紫边，半开时最香，状如抿嘴而笑，故有其名。'
        '末二句以反问收束：草名忘忧，究竟忘了什么忧；花名含笑，究竟笑的是谁。'
        '接682课，为《笠翁对韵》十一真第三段收尾。落点：境遇由天，忧笑由己。')

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '683-wang-you-han-xiao' not in s, 'manifest already has 683'
entry = """    {
        num: '683',
        id: '683-wang-you-han-xiao',
        title: '对韵 · 忘忧含笑，南阮东施（典故与花草）',
        subtitle: '忘忧含笑：典故与花草',
        path: 'lessons/683-wang-you-han-xiao/index.html',
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
assert '共 682 课' in s
s = s.replace('共 682 课', '共 683 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '683-wang-you-han-xiao' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/682-hua-fu-fu/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/683-wang-you-han-xiao/index.html</loc>',
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
assert '683' not in s
s = s.replace('682', '683')
assert '笠翁对韵课堂=95' in s
s = s.replace('笠翁对韵课堂=95', '笠翁对韵课堂=96')
assert '2, 6, 95]' in s
s = s.replace('2, 6, 95]', '2, 6, 96]')
write(p, s)
print('tests ok')
