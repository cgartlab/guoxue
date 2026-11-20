# -*- coding: utf-8 -*-
"""登记第685课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「烹早韭，剪春芹。暮雨对朝云。竹间斜白接，花下醉红裙。」此段见《笠翁对韵》上卷十二文其一收尾，接684课「夏耨对春耘」之后。烹早韭、剪春芹，两样都是早春的时鲜菜蔬：烹是下锅煮，剪是下地割。《南史》有「春初早韭，秋末晚菘」之说，杜甫《赠卫八处士》又有「夜雨剪春韭，新炊间黄粱」，都是这一句的来处。暮雨对朝云，出宋玉《高唐赋》巫山神女语「旦为朝云，暮为行雨，朝朝暮暮，阳台之下」，后世「朝云暮雨」遂成典故。暮对朝是时间相对，雨对云是天象相对。竹间斜白接，白接即白接䍦，白色头巾，䍦读lí。《世说新语·任诞》记时人歌「山公时一醉，径造高阳池。日莫倒载归，酩酊无所知。复能乘骏马，倒著白接䍦」，山简镇襄阳事；李白《襄阳歌》「倒著接䍦花下迷」即用此。花下醉红裙，红裙指穿红裙的女子，与上句白头巾一物一人相对；旧注亦有指红花之说。竹间对花下是地方相对，斜对醉是姿态相对，白对红是颜色相对。全段四组，写的都是家常物、眼前景。落点：身边的物，也能入诗。')


# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '685-peng-zao-jiu' not in s, 'manifest already has 685'
entry = """    {
        num: '685',
        id: '685-peng-zao-jiu',
        title: '对韵 · 春韭朝云，白接红裙（家常与时令）',
        subtitle: '春韭朝云：家常与时令',
        path: 'lessons/685-peng-zao-jiu/index.html',
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
assert '共 684 课' in s
s = s.replace('共 684 课', '共 685 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '685-peng-zao-jiu' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/684-you-dui-xi/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/685-peng-zao-jiu/index.html</loc>',
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
assert '685' not in s
s = s.replace('684', '685')
assert '笠翁对韵课堂=97' in s
s = s.replace('笠翁对韵课堂=97', '笠翁对韵课堂=98')
assert '2, 6, 97]' in s
s = s.replace('2, 6, 97]', '2, 6, 98]')
write(p, s)
print('tests ok')
