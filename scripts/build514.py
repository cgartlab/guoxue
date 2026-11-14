# -*- coding: utf-8 -*-
"""第 514 课《三传者》：以 513 为骨架，逐行替换内容生成新课件。"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '513-yue-guo-feng', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '514-san-zhuan-zhe')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第二十一课精讲：三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。上一课讲了《诗经》与《春秋》，这一课先把《春秋》说完整——《春秋》字句太简，必须靠「传」来讲解，解说《春秋》的有三部书：公羊、左氏、谷梁，合称「三传」；再讲六经读通之后，方才去读诸子百家，抓住要点、记住事迹。八句话，讲清「传」与「子」。" name="description"/>'''
R[7] = '''<meta content="三传者 · 有公羊，有左氏，有谷梁 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第二十一课：三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/514-san-zhuan-zhe/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/514-san-zhuan-zhe/index.html" rel="canonical"/>'''
R[12] = '''<title>三传者 · 有公羊，有左氏，有谷梁 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">三传者</h2><div class="cover-ornament"></div><p class="cover-subtitle">有公羊，有左氏，有谷梁</p><p class="cover-desc">上一课讲了《诗经》与《春秋》。这一课先把《春秋》说完整——《春秋》字句太简，必须靠「传」来讲解，讲解《春秋》的有三部书：公羊、左氏、谷梁，合称「三传」。然后《三字经》告诉我们读书的次第：六经读通明白之后，才去读诸子百家，抓住要旨、记住事迹。八句话，讲清「传」与「子」。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文八句（四行，每行六字） ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


R[55] = ruby_line(STYLE_A, [('三', 'sān'), ('传', 'zhuàn'), ('者', 'zhě'), ('有', 'yǒu'), ('公', 'gōng'), ('羊', 'yáng')])
R[56] = ruby_line(STYLE_B, [('有', 'yǒu'), ('左', 'zuǒ'), ('氏', 'shì'), ('有', 'yǒu'), ('谷', 'gǔ'), ('梁', 'liáng')])
R[57] = ruby_line(STYLE_B, [('经', 'jīng'), ('既', 'jì'), ('明', 'míng'), ('方', 'fāng'), ('读', 'dú'), ('子', 'zǐ')])
R[58] = ruby_line(STYLE_B, [('撮', 'cuō'), ('其', 'qí'), ('要', 'yào'), ('记', 'jì'), ('其', 'qí'), ('事', 'shì')])
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>解说《春秋》的传有三家：有公羊高的《公羊传》，有左丘明的《左传》，有谷梁赤的《谷梁传》。六经读通、明白义理之后，才可以去读诸子百家的书；读子书要摘取其中的要点，记住他们所做的事迹。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《春秋》经文极简，像「春王正月」几个字背后藏着褒贬，所以后人作「传」来解释。影响最大的三部叫「三传」：公羊、左、谷梁。《三字经》接着讲读书次第——先经后子，由本及末。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>经以载道，子以明术。</strong></p></div>'''

# ---------- 3. 字词梳理 · 九个关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九个关节</h2><p><span class="ds-highlight">三传者</span>：<strong>传是解释经书的文字，三传指解说《春秋》的三部书</strong>——<strong>公羊、左氏、谷梁</strong>。</p><p><span class="ds-highlight">有公羊</span>：<strong>指《公羊传》，旧题公羊高所作</strong>——<strong>重在阐发微言大义，讲例不讲事</strong>。</p><p><span class="ds-highlight">有左氏</span>：<strong>指《左传》，相传左丘明所作</strong>——<strong>重在补充史实，叙事详明</strong>。</p><p><span class="ds-highlight">有谷梁</span>：<strong>指《谷梁传》，旧题谷梁赤所作</strong>——<strong>与公羊相近，重在义理</strong>。</p><p><span class="ds-highlight">经既明</span>：<strong>既是从、已经，明是明白、通晓</strong>——<strong>把六经读通了</strong>。</p><p><span class="ds-highlight">方读子</span>：<strong>方是才、方才，子是诸子百家</strong>——<strong>六经之后，才去读诸子</strong>。</p><p><span class="ds-highlight">撮其要</span>：<strong>撮是摘取、聚合，要是纲要</strong>——<strong>抓住书里的要点</strong>。</p><p><span class="ds-highlight">记其事</span>：<strong>事是事迹、故事</strong>——<strong>记住各家做了些什么</strong>。</p><p><span class="ds-highlight">经与子</span>：<strong>经是根本大道，子是各家的学问与方术</strong>——<strong>先立根本，再博采众长</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>经以载道，子以明术。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '三传者，有公羊', '三 传 者 ， 有 公 羊', [
    ('「三传」是哪三部？', '公羊、左氏、谷梁', '都是解说《春秋》的传', '三部解经'),
    ('为什么《春秋》要有「传」？', '经文太简，一字藏褒贬', '没有传，后人读不懂', '以传解经'),
    ('「公羊」指什么？', '《公羊传》，旧题公羊高作', '重在讲微言大义', '公羊讲义'),
])
R[65] = interp(4, '二', '有左氏，有谷梁', '有 左 氏 ， 有 谷 梁', [
    ('「左氏」指什么？', '《左传》，相传左丘明作', '重在补充史实、叙事详明', '左传重史'),
    ('「谷梁」指什么？', '《谷梁传》，旧题谷梁赤作', '与公羊相近，重在义理', '谷梁重理'),
    ('三部传有何不同？', '公羊、谷梁重义理，左氏重史实', '一重讲例，一重叙事', '义理与史'),
])
R[67] = interp(5, '三', '经既明，方读子', '经 既 明 ， 方 读 子', [
    ('「经」指什么？', '儒家六经（诗书礼易乐春秋）', '是先圣载道之书', '经是根本'),
    ('「方读子」为什么用「方」？', '方是才、方才', '强调次序：先经后子', '先经后子'),
    ('为什么要先经后子？', '经立根本，子博众长', '本末有序，学问才稳', '由本及末'),
])
R[69] = interp(6, '四', '撮其要，记其事', '撮 其 要 ， 记 其 事', [
    ('「撮其要」怎么讲？', '撮是摘取，要是纲要', '读子书要抓重点', '抓要点'),
    ('「记其事」记什么？', '记诸子各家的事迹作为', '借故事明其主张', '记事迹'),
    ('这一课的落点？', '读完经再读子，提纲挈领', '经以载道，子以明术', '经子并观'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事</h2><p>一句话，两层意思——</p><h3>"三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前四句讲《春秋》的三部传注，后四句讲读经之后读子书的次第。</p><p>📜 三传解春秋</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>经是根本大道，子是各家方术；先立根本，再广采众说，学问才有根有叶。</p><p>📚 先经后子</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>读书要讲次第，先本后末，提纲挈领。</p><p>🌿 经以载道，子以明术</p>'''
R[75] = '''<p>这是「三字经课堂」第二十一课：三传者，有公羊。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「三传」是哪三部书？</h3><p><strong>是《公羊传》《左传》《谷梁传》，都是解说《春秋》的传。</strong><br/><br/>① <strong>公羊、谷梁重在讲义理（微言大义）</strong><br/>② <strong>左氏重在补充史实（叙事详明）</strong><br/>③ <strong>三部并称「三传」</strong><br/><br/><strong>记法：三传解《春秋》。</strong></p><h3>❓ 「传」是什么意思？为什么《春秋》要有传？</h3><p><strong>「传」是解释经书的文字。《春秋》经文极简，一字藏褒贬，必须靠传才读得懂。</strong><br/><br/>① <strong>经是正文，传是注脚</strong><br/>② <strong>《春秋》太简，离了传就难明其意</strong><br/>③ <strong>解说《春秋》的传特别多，以三传最要</strong><br/><br/><strong>记法：以传解经。</strong></p><h3>❓ 「经既明，方读子」是说读完经才能读子书吗？</h3><p><strong>是讲读书的次第：先把六经读通，再去博览诸子。</strong><br/><br/>① <strong>经是根本，子是枝叶</strong><br/>② <strong>先立根本，再博采众长</strong><br/>③ <strong>不是绝对不许先读，而是强调本末有序</strong><br/><br/><strong>记法：先本后末。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这八句，给我们三样提醒——</p><p>📚 读书有次第</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「经既明，方读子」</strong>；<strong>学习也讲顺序，先把基础打牢，再拓展广度</strong>。</p><p>🎯 抓大放小</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「撮其要」提醒我们，读书要提纲要领</strong>；<strong>不求全记，但求抓住关键</strong>。</p><p>🧭 立根再长叶</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「经以载道，子以明术」</strong>；<strong>先立做人根本，再学各家本领，人生才稳当</strong><br/><br/><strong>本课的落点：三传者，有公羊。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第二十一课。记牢：<strong>三传者，有公羊</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>三传者，有公羊 · 《春秋》三部传：公羊、左氏、谷梁。<strong>三传解经。</strong></p><p>有左氏，有谷梁 · 《左传》重史实，《谷梁传》重义理。<strong>义理与史。</strong></p><p>经既明，方读子 · 六经读通，方读诸子。<strong>先经后子。</strong></p><p>撮其要，记其事 · 读子书抓要点、记事迹。<strong>提纲挈领。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲《诗经》与《春秋》（风雅颂、四诗、春秋笔法），这一课讲「三传」与「读子」，下一课讲诸子百家（五子者：荀扬文中老庄）。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「三传」指哪三部。③ 讲清「先经后子」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>三传者，有公羊，有左氏，有谷梁，经既明，方读子，撮其要，记其事。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "三传者，有公羊。有左氏，有谷梁。经既明，方读子。撮其要，记其事。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '514-san-zhuan-zhe';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 「三传」指的是哪三部书？', ['《公羊传》《左传》《谷梁传》', '《诗》《书》《礼》', '《论语》《孟子》《大学》'], '三部都是解说《春秋》的传'),
    ('2. 《公羊传》《谷梁传》侧重于什么？', ['阐发义理、微言大义', '补充历史事实', '讲解文字训诂'], '公羊、谷梁重在讲大义'),
    ('3. 《左传》最突出的特点是什么？', ['叙事详明、补充史实', '只讲道理不记事', '和公羊完全相同'], '左氏重史，叙事最详'),
    ('4. 「传」在这里是什么意思？', ['解释经书的文字', '传记文学', '传递消息'], '传是解经之作'),
    ('5. 「经既明」的「经」指什么？', ['儒家六经', '经历', '经常'], '先圣载道之书'),
    ('6. 「方读子」的「子」指什么？', ['诸子百家的书', '子女', '学子'], '子书是各家学说'),
    ('7. 「经既明，方读子」讲的是什么？', ['读书的次第：先经后子', '经和子一起读', '只读子不读经'], '先立根本，再博众长'),
    ('8. 「撮其要」的「撮」怎么讲？', ['摘取、抓住', '撮合', '一小撮'], '抓住书的要点'),
    ('9. 「记其事」的「事」指什么？', ['诸子各家的事迹作为', '事情的顺序', '事业'], '借事迹明其主张'),
    ('10. 这一课八句合起来讲什么？', ['《春秋》三传与读经之后读子的次第', '四季的变化', '周公的事迹'], '三传解经，先经后子'),
]
for i, (q, opts, exp) in enumerate(QUIZ):
    R[135 + i] = "  {q: '%s', opts: ['%s', '%s', '%s'], ans: 0, exp: '%s'}," % (q, opts[0], opts[1], opts[2], exp)

for n, text in R.items():
    assert 1 <= n <= len(lines), '行号越界: %d' % n
    lines[n - 1] = text

s = '\n'.join(lines)
s = s.replace('513-yue-guo-feng', '514-san-zhuan-zhe')
s = s.replace('yaoyue515', 'yaoyue516')
s = s.replace('第二十课', '第二十一课')
assert '513-yue-guo-feng' not in s and 'yaoyue515' not in s and '第二十课' not in s

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK', DST, len(s), 'chars,', len(s.split('\n')), 'lines')
