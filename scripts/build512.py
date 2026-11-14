# -*- coding: utf-8 -*-
"""第 512 课《我周公》：以 511 为骨架，逐行替换内容生成新课件。"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '511-you-lian-shan', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '512-wo-zhou-gong')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第十九课精讲：我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。上一课讲了「六经」里的《易》与《书》，这一课讲其中的《礼》：先说《周礼》相传是周公所作，他设立了六官、定下治国的体制；再说西汉的大戴、小戴两家人给《礼记》作注，把圣人的言论传了下来，礼和乐就都齐备了。" name="description"/>'''
R[7] = '''<meta content="我周公 · 作周礼，礼乐备 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第十九课：我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/512-wo-zhou-gong/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/512-wo-zhou-gong/index.html" rel="canonical"/>'''
R[12] = '''<title>我周公 · 作周礼，礼乐备 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">我周公</h2><div class="cover-ornament"></div><p class="cover-subtitle">作周礼，礼乐备</p><p class="cover-desc">上一课把「六经」里的《易》和《书》讲了——一部讲阴阳变化，一部存上古之言。这一课讲其中的《礼》：《周礼》相传是周公制定的，他设立了六官、定下治国的体制；《礼记》则由西汉的大戴、小戴两家人作注，把圣人的言论传了下来，礼和乐就都齐备了。四句话，把「礼」这门经典说清楚了。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文四句 ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


R[55] = ruby_line(STYLE_A, [('我', 'wǒ'), ('周', 'zhōu'), ('公', 'gōng'), ('作', 'zuò'), ('周', 'zhōu'), ('礼', 'lǐ')])
R[56] = ruby_line(STYLE_B, [('著', 'zhù'), ('六', 'liù'), ('官', 'guān'), ('存', 'cún'), ('治', 'zhì'), ('体', 'tǐ')])
R[57] = ruby_line(STYLE_B, [('大', 'dà'), ('小', 'xiǎo'), ('戴', 'dài'), ('注', 'zhù'), ('礼', 'lǐ'), ('记', 'jì')])
R[58] = ruby_line(STYLE_B, [('述', 'shù'), ('圣', 'shèng'), ('言', 'yán'), ('礼', 'lǐ'), ('乐', 'yuè'), ('备', 'bèi')])
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>我周公旦，制作了《周礼》；设立了天地春夏秋冬六官，保存了治国的体制。大戴戴德、小戴戴圣给《礼记》作注，记述圣人的言论，礼和乐就都齐备了。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>周公是周武王的弟弟姬旦，辅佐年幼的成王、平定天下，相传制礼作乐，奠定了周朝的典章；《礼记》是讲解礼仪、阐发礼义的书，西汉时戴德（大戴）、戴圣（小戴）分别编订注解，所以有「大小戴」之称。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>周礼立制度，礼记明礼义。</strong></p></div>'''

# ---------- 3. 字词梳理 · 九个关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九个关节</h2><p><span class="ds-highlight">我周公</span>：<strong>我在这里是「说起、提到」</strong>——<strong>周公是周武王的弟弟姬旦，辅佐成王、制礼作乐</strong>。</p><p><span class="ds-highlight">作周礼</span>：<strong>作是写作、制定</strong>——<strong>《周礼》是周公制定的官职与礼仪制度之书</strong>。</p><p><span class="ds-highlight">著六官</span>：<strong>著是设立、明文记载</strong>——<strong>六官指天、地、春、夏、秋、冬六官，分掌国家政务</strong>。</p><p><span class="ds-highlight">存治体</span>：<strong>存是保存，治体是治国的体制、根本法度</strong>——<strong>把一套安邦的制度留给了后世</strong>。</p><p><span class="ds-highlight">大小戴</span>：<strong>大戴是戴德，小戴是戴圣，二人是西汉传授《礼》的学者（叔侄关系）</strong>——<strong>「大小戴」是后人对他们的合称</strong>。</p><p><span class="ds-highlight">注礼记</span>：<strong>注是注解、编订</strong>——<strong>《礼记》是讲解礼仪、发挥礼义的书</strong>。</p><p><span class="ds-highlight">述圣言</span>：<strong>述是记述、传述，圣言是圣人的教训言论</strong>——<strong>把先王的智慧传下来</strong>。</p><p><span class="ds-highlight">礼乐备</span>：<strong>备是完备、齐备</strong>——<strong>礼定规矩，乐调和人心，二者俱全</strong>。</p><p><span class="ds-highlight">礼之两书</span>：<strong>《周礼》讲制度的框架，《礼记》讲礼义的精神</strong>——<strong>都是「六经」里「礼」的部分</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>周礼立制度，礼记明礼义。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '我周公，作周礼', '我 周 公 ， 作 周 礼', [
    ('周公是什么人？', '相传是周武王的弟弟姬旦', '他辅佐年幼的成王，平定天下、制礼作乐', '周室的奠基者'),
    ('《周礼》是他写的吗？', '相传由周公制定', '奠定了周代的官制和礼仪', '制礼作乐之人'),
    ('「作」在这里怎么讲？', '作是写作、创制', '「作周礼」就是制定这部礼书', '不是平常的「做」'),
])
R[64] = '<!-- 5. 解读二 -->'
R[65] = interp(4, '二', '著六官，存治体', '著 六 官 ， 存 治 体', [
    ('「六官」是哪六官？', '天、地、春、夏、秋、冬六官', '分掌国家各方面的事务', '六部的前身'),
    ('「著」是什么意思？', '著是设立、明文记载', '把官职制度写定下来', '立法定制'),
    ('「治体」指什么？', '治是治国，体是体制、根本', '指一套安邦定国的法度', '立国之本'),
])
R[66] = '<!-- 6. 解读三 -->'
R[67] = interp(5, '三', '大小戴，注礼记', '大 小 戴 ， 注 礼 记', [
    ('大小戴是谁？', '大戴戴德、小戴戴圣，西汉人', '二人是叔侄，都传《礼》学', '传礼两家'),
    ('《礼记》是本什么书？', '讲解礼仪、阐发礼义的书', '把礼节背后的道理说清楚', '与《仪礼》《周礼》合称「三礼」'),
    ('「注」怎么讲？', '注是注解、编订', '古人给经典作注，方便后人读', '注以传经'),
])
R[68] = '<!-- 7. 解读四 -->'
R[69] = interp(6, '四', '述圣言，礼乐备', '述 圣 言 ， 礼 乐 备', [
    ('「述圣言」说什么？', '述是记述，圣言是圣人的话', '把先王的教训传下来', '述而不作'),
    ('礼和乐什么关系？', '礼定规矩，乐调和人心', '一外一内，相辅而成', '礼乐相成'),
    ('这一课的落点？', '《周礼》立制度，《礼记》明礼义', '礼乐是古人教化的根本', '知礼而立'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备</h2><p>一句话，三层意思——</p><h3>"我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>四句讲《周礼》的来历和《礼记》的注家。</p><p>📜 周公制礼，大小戴注</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>《周礼》立下治国的制度框架，《礼记》把礼的精神说透，礼乐合起来就是古人的教化。</p><p>🏛️ 制度与精神</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>礼不是束缚，是让人与人相处有分寸、有温度。</p><p>🤝 以礼立人</p>'''
R[75] = '''<p>这是「三字经课堂」第十九课：作周礼，礼乐备。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 周公是不是周朝的一个「公」、一种爵位？</h3><p><strong>不是。周公是周武王的弟弟姬旦，封地在周，所以称「周公」；他是政治家、礼乐制度的奠基人，不是泛指的爵位。</strong><br/><br/>① <strong>周公名姬旦，是周文王的儿子、周武王的弟弟</strong><br/>② <strong>他辅佐成王、平定叛乱、制礼作乐</strong><br/>③ <strong>「公」在这里是尊称，不是爵位名</strong><br/><br/><strong>记法：周公是人，不是爵。</strong></p><h3>❓ 「六官」跟今天的部门有什么关系？</h3><p><strong>六官是周代官制，后来隋唐的「六部」就是它的流变。</strong><br/><br/>① <strong>六官是天、地、春、夏、秋、冬官</strong><br/>② <strong>分掌政务，各管一摊</strong><br/>③ <strong>六部（吏户礼兵刑工）承其脉络</strong><br/><br/><strong>记法：六官是六部的前身。</strong></p><h3>❓ 「大小戴」是一个人还是两家？</h3><p><strong>两家。大戴戴德、小戴戴圣，是叔侄二人，都研究《礼》。</strong><br/><br/>① <strong>大戴戴德，小戴戴圣，西汉人</strong><br/>② <strong>《小戴礼记》流传最广，就是我们常说的《礼记》</strong><br/>③ <strong>「大小戴」是后人对二人的合称</strong><br/><br/><strong>记法：大小戴，传礼两家。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这四句，给我们三样提醒——</p><p>🏛️ 立好规矩</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>周公设六官，是给国家立规矩</strong>；<strong>家里、班里也要有清楚的规矩，事情才好办</strong>。</p><p>🤝 规矩里有温度</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>礼不只是条条框框，更是让人舒服的分寸</strong>；<strong>礼到，情也在</strong>。</p><p>📜 把好的传下去</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>大小戴注《礼记》，是把先人的智慧传下来</strong>；<strong>我们也要把好的家风、学风传下去</strong><br/><br/><strong>本课的落点：作周礼，礼乐备。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第十九课。记牢：<strong>作周礼，礼乐备</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>我周公，作周礼 · 《周礼》相传为周公所作。<strong>周武王的弟弟姬旦。</strong></p><p>著六官，存治体 · 设天地春夏秋冬六官，保存治国体制。<strong>六部前身。</strong></p><p>大小戴，注礼记 · 西汉戴德、戴圣为《礼记》作注。<strong>传礼两家。</strong></p><p>述圣言，礼乐备 · 记述圣人言论，礼与乐齐备。<strong>教化之本。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲《易》与《书》，这一课讲《礼》（《周礼》《礼记》），下一课讲《诗》与《春秋》。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这四句背下来。② 说出「六官」指什么。③ 讲清「大小戴」是谁。</p><p><strong>把这一课记在心里:</strong><strong>我周公，作周礼，著六官，存治体，大小戴，注礼记，述圣言，礼乐备。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "我周公，作周礼。著六官，存治体。大小戴，注礼记。述圣言，礼乐备。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '512-wo-zhou-gong';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 《周礼》相传是谁制定的？', ['周公（姬旦）', '孔子', '老子'], '周公是周武王的弟弟，相传制礼作乐'),
    ('2. 「著六官」的「六官」指什么？', ['天、地、春、夏、秋、冬六官', '六名官员', '六部尚书（唐以后）'], '六官是周代官制，是后来六部的前身'),
    ('3. 「存治体」的「治体」是什么意思？', ['治国的体制、根本法度', '身体的健康', '治理池塘'], '指安邦定国的一套制度'),
    ('4. 「大小戴」是谁？', ['西汉戴德、戴圣叔侄二人', '两座山的名字', '两位皇帝'], '大戴戴德、小戴戴圣，都传授《礼》学'),
    ('5. 我们常说的《礼记》主要是谁编订的？', ['小戴戴圣', '大戴戴德', '周公'], '《小戴礼记》流传最广'),
    ('6. 「注礼记」的「注」怎么讲？', ['注解、编订', '注视', '注水'], '古人为经典作注，方便后人研读'),
    ('7. 《礼记》与什么合称「三礼」？', ['《周礼》《仪礼》', '《诗》《书》', '《易》《书》'], '三礼：周礼、仪礼、礼记'),
    ('8. 「述圣言」的「述」是什么意思？', ['记述、传述', '叙述故事', '逃跑'], '把圣人的言论传下来'),
    ('9. 为什么说「礼乐备」？', ['礼定规矩、乐和人心，二者俱全', '礼物很多', '音乐特别好听'], '礼乐相辅，教化才完整'),
    ('10. 这一课四句合起来讲什么？', ['《周礼》的来历与《礼记》的注家', '四季的变化', '九族的辈分'], '讲「六经」里「礼」这部经典'),
]
for i, (q, opts, exp) in enumerate(QUIZ):
    R[135 + i] = "  {q: '%s', opts: ['%s', '%s', '%s'], ans: 0, exp: '%s'}," % (q, opts[0], opts[1], opts[2], exp)

for n, text in R.items():
    assert 1 <= n <= len(lines), '行号越界: %d' % n
    lines[n - 1] = text

s = '\n'.join(lines)
s = s.replace('511-you-lian-shan', '512-wo-zhou-gong')
s = s.replace('yaoyue513', 'yaoyue514')
s = s.replace('第十八课', '第十九课')
assert '511-you-lian-shan' not in s and 'yaoyue513' not in s and '第十八课' not in s

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK', DST, len(s), 'chars,', len(s.split('\n')), 'lines')
