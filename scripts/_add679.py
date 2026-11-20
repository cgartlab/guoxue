# -*- coding: utf-8 -*-
"""登记第679课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '679-zhe-gui-zan-hua' not in s, 'manifest already has 679'
entry = """    {
        num: '679',
        id: '679-zhe-gui-zan-hua',
        title: '对韵 · 折桂簪花，四皓三仁（功名与人物）',
        subtitle: '折桂簪花：功名与人物',
        path: 'lessons/679-zhe-gui-zan-hua/index.html',
        grade: '小学低中年级',
        description: '对韵段，原文：「折桂客，簪花人。四皓对三仁。王乔云外鸟，郭泰雨中巾。」折桂谓科举及第，出《晋书·郤诜传》「犹桂林之一枝，昆山之片玉」，后称蟾宫折桂；簪读zān，簪花谓插花于冠，唐宋进士及第赐花簪戴、骑马游街夸官。四皓为秦末汉初商山四位白发隐士——东园公、夏黄公、绮里季、甪里先生，刘邦欲废太子，吕后礼请四人出山辅翼，太子遂安；三仁出《论语·微子》「微子去之，箕子为之奴，比干谏而死」，孔子曰「殷有三仁焉」。王乔为汉明帝时叶县令，有道术，朔望来朝不乘车骑，惟见双凫飞来，张罗捕之得一双舄，通行本作「王乔云外舄」，舄读xì即鞋，教材本改写为鸟；郭泰字林宗，东汉名士，行遇雨巾一角垫，时人故折巾角效之，称林宗巾，见《后汉书》。接678课，同属《笠翁对韵》十一真第二段。落点：名从行来，不从口来。',
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
assert '共 678 课' in s
s = s.replace('共 678 课', '共 679 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '679-zhe-gui-zan-hua' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/678-xiong-dui-di/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/679-zhe-gui-zan-hua/index.html</loc>',
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
assert '679' not in s
s = s.replace('678', '679')
assert '笠翁对韵课堂=91' in s
s = s.replace('笠翁对韵课堂=91', '笠翁对韵课堂=92')
assert '2, 6, 91]' in s
s = s.replace('2, 6, 91]', '2, 6, 92]')
write(p, s)
print('tests ok')
