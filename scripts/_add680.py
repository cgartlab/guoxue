# -*- coding: utf-8 -*-
"""登记第680课：manifest / index.html / sitemap / tests 四处同步。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    return io.open(os.path.join(root, p), encoding='utf-8', newline='').read()

def write(p, s):
    io.open(os.path.join(root, p), 'w', encoding='utf-8', newline='').write(s)

DESC = ('对韵段，原文：「人交好友求三益，士有贤妻备五伦。文教南宣，武帝平蛮开百越；义旗西指，韩侯扶汉卷三秦。」'
        '三益出《论语·季氏》「益者三友：友直、友谅、友多闻，益矣」，谓交朋友要交正直、守信、多见识之人；'
        '五伦谓君臣、父子、兄弟、夫妇、朋友五种人伦，出《孟子·滕文公上》，古人以有夫妇然后有父子，故言「贤妻备五伦」。'
        '「文教南宣」谓中原礼乐教化向南推行：汉武帝元鼎五年（前112）南越丞相吕嘉杀王反汉，汉发五路兵，'
        '元鼎六年（前111）平定，设南海、苍梧、郁林、合浦、交趾、九真、日南、珠崖、儋耳九郡，岭南始入郡县。'
        '「义旗西指」谓韩信辅汉王刘邦自汉中还定关中：项羽分关中为三，王章邯、司马欣、董翳，故称三秦；'
        '汉元年（前206）八月韩信出陈仓道，明修栈道暗度陈仓，岁余尽定，三秦遂为汉有。'
        '接679课，对韵人伦开疆段。落点：先齐家，后安天下。')

# ---------- 1. manifest ----------
p = 'assets/js/lessons-manifest.js'
s = read(p)
assert '680-ren-jiao-hao-you' not in s, 'manifest already has 680'
entry = """    {
        num: '680',
        id: '680-ren-jiao-hao-you',
        title: '对韵 · 益友贤妻，平越定秦（人伦与开疆）',
        subtitle: '益友贤妻：人伦与开疆',
        path: 'lessons/680-ren-jiao-hao-you/index.html',
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
assert '共 679 课' in s
s = s.replace('共 679 课', '共 680 课')
write(p, s)
print('index ok')

# ---------- 3. sitemap ----------
p = 'sitemap.xml'
s = read(p)
assert '680-ren-jiao-hao-you' not in s
nl = '\r\n' if '\r\n' in s else '\n'
old = '    <loc>https://guoxue.8023laozhanshi.cc/lessons/679-zhe-gui-zan-hua/index.html</loc>'
i = s.find(old)
assert i != -1
j = s.find('</url>', i) + len('</url>')
block = nl.join([
    '  <url>',
    '    <loc>https://guoxue.8023laozhanshi.cc/lessons/680-ren-jiao-hao-you/index.html</loc>',
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
assert '680' not in s
s = s.replace('679', '680')
assert '笠翁对韵课堂=92' in s
s = s.replace('笠翁对韵课堂=92', '笠翁对韵课堂=93')
assert '2, 6, 92]' in s
s = s.replace('2, 6, 92]', '2, 6, 93]')
write(p, s)
print('tests ok')
