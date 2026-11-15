# -*- coding: utf-8 -*-
"""第 517 课《夏有禹·三王与家天下》：以 516 为骨架，逐行替换内容生成新课件。
原文四句话（两组，每组六言两句，共四句24字）：
  夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '516-zi-xi-nong', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '517-xia-you-yu')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第二十四课精讲：夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。上一课讲了「三皇二帝」的禅让盛世，这一课顺着读史往下讲——夏商周三代的开国之君禹、汤、文王武王被称为「三王」；大禹把天下传给儿子启，「家天下」从此开始，夏朝四百年后社稷迁移。八句短语（四句六言），讲完三代的开端与「家天下」的由来。" name="description"/>'''
R[7] = '''<meta content="夏有禹 · 商有汤，周文武，称三王 · 夏传子，家天下，四百载，迁夏社 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第二十四课：夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/517-xia-you-yu/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/517-xia-you-yu/index.html" rel="canonical"/>'''
R[12] = '''<title>夏有禹 · 商有汤，周文武，称三王 · 夏传子，家天下，四百载，迁夏社 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">夏有禹</h2><div class="cover-ornament"></div><p class="cover-subtitle">商有汤，周文武，称三王；夏传子，家天下，四百载，迁夏社</p><p class="cover-desc">上一课讲了「三皇二帝」——远古的禅让盛世。这一课顺着读史往下讲：夏朝有大禹，商朝有汤，周朝有文王武王，他们被称为「三王」，是三代的开国之君；大禹把天下传给儿子启，「家天下」从此开始，夏朝延续四百年后社稷迁移。八句短语，讲完三代的开端与世袭的由来。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文四句（两句一组，共四句） ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


# 原文共四句（两组），合并成四行
R[55] = ruby_line(STYLE_A, [('夏', 'xià'), ('有', 'yǒu'), ('禹', 'yǔ'), ('商', 'shāng'), ('有', 'yǒu'), ('汤', 'tāng')]) \
     + ruby_line(STYLE_B, [('周', 'zhōu'), ('文', 'wén'), ('武', 'wǔ'), ('称', 'chēng'), ('三', 'sān'), ('王', 'wáng')]) \
     + ruby_line(STYLE_B, [('夏', 'xià'), ('传', 'chuán'), ('子', 'zǐ'), ('家', 'jiā'), ('天', 'tiān'), ('下', 'xià')]) \
     + ruby_line(STYLE_B, [('四', 'sì'), ('百', 'bǎi'), ('载', 'zǎi'), ('迁', 'qiān'), ('夏', 'xià'), ('社', 'shè')])
R[56] = ''
R[57] = ''
R[58] = ''
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>夏朝有大禹，商朝有汤，周朝有文王武王，他们被尊为「三王」；大禹把王位传给儿子，天下成为一家的私有，夏朝历经四百年，最终社稷迁移（亡于桀）。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》在讲完三皇二帝之后，紧接着讲夏商周三代——先讲三代开国之君「三王」，再讲「家天下」的由来。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>三王开基，家天下始。</strong></p></div>'''

# ---------- 3. 字词梳理 · 九关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">夏有禹</span>：<strong>夏是夏朝，禹是大禹</strong>——<strong>夏朝的开国之君，治水的功臣</strong>。</p><p><span class="ds-highlight">商有汤</span>：<strong>商是商朝，汤是商汤</strong>——<strong>商朝的开国之君，灭夏建商</strong>。</p><p><span class="ds-highlight">周文武</span>：<strong>周是周朝，文是周文王，武是周武王</strong>——<strong>周朝两位开国之君</strong>。</p><p><span class="ds-highlight">称三王</span>：<strong>称是尊称，三王是夏禹、商汤、周文武</strong>——<strong>三代开国之君并称「三王」</strong>。</p><p><span class="ds-highlight">夏传子</span>：<strong>传是传给，子是儿子（启）</strong>——<strong>大禹把王位传给儿子启</strong>。</p><p><span class="ds-highlight">家天下</span>：<strong>家是当作自家，天下是江山</strong>——<strong>天下成为一姓的私有，世袭开始</strong>。</p><p><span class="ds-highlight">四百载</span>：<strong>载是年，四百载是约四百年</strong>——<strong>夏朝享国的年数</strong>。</p><p><span class="ds-highlight">迁夏社</span>：<strong>迁是迁移，社是社稷（国家）</strong>——<strong>夏朝灭亡，社稷随之迁移</strong>。</p><p><span class="ds-highlight">三王家天下</span>：<strong>三王开基，家天下承</strong>——<strong>从禅让到世袭，制度为之一变</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>夏禹商汤周文武，三代三王；禹传启，家天下。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '夏有禹，商有汤', '夏 有 禹 ， 商 有 汤', [
    ('「夏有禹」指谁？', '大禹，夏朝开国之君', '治水功成，奠定夏基', '禹奠夏基'),
    ('「商有汤」的汤是谁？', '商汤，商朝开国之君', '灭夏建商，开一代之业', '汤建商基'),
    ('这句讲什么？', '夏商两代，各有开基之君', '先举夏商，引出三王', '夏商开基'),
])
R[65] = interp(4, '二', '周文武，称三王', '周 文 武 ， 称 三 王', [
    ('「周文武」是谁？', '周文王、周武王', '周朝两位开国之君', '周室开基'),
    ('为何称「三王」？', '禹、汤、文武，三代开国之君并称', '功在天下，万世景仰', '三王并称'),
    ('与前句的关系？', '夏商周三代，各举其君，归于三王', '三代相继，同称三王', '三代三王'),
])
R[67] = interp(5, '三', '夏传子，家天下', '夏 传 子 ， 家 天 下', [
    ('「夏传子」传的是谁？', '启，大禹的儿子', '禹传位给儿子启', '禹传于启'),
    ('什么是「家天下」？', '天下成为一家的私有', '世袭由此开始', '家天下始'),
    ('这句的落点？', '从禅让到世袭，制度一大变', '公天下变作家天下', '世袭开端'),
])
R[69] = interp(6, '四', '四百载，迁夏社', '四 百 载 ， 迁 夏 社', [
    ('「四百载」指谁？', '夏朝，享国约四百年', '历时久远', '夏祚四百年'),
    ('「迁夏社」什么意思？', '夏亡，社稷迁移', '商汤灭夏，社稷易主', '夏亡迁社'),
    ('这一句的落点？', '再长的王朝也有终，兴衰有数', '居安思危，方得长久', '兴衰有数'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社</h2><p>一句话，两层意思——</p><h3>"夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前两句讲三代三王——禹、汤、文武，开基立业；后两句讲家天下——大禹传子，夏朝四百年后社稷迁移。</p><p>👑 三代三王</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>从三皇二帝的禅让，到夏的世袭，制度为之一变；兴亡有数，居安思危。</p><p>🏺 家天下</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>三王开基，家天下承；四百年终迁社，提醒后世居安思危。</p><p>⚖️ 兴衰有数</p>'''
R[75] = '''<p>这是「三字经课堂」第二十四课：夏有禹，商有汤。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「三王」指哪三位？</h3><p><strong>是夏禹、商汤、周文王武王。</strong><br/><br/>① <strong>禹奠夏基、汤建商基、文武开周基</strong><br/>② <strong>三代开国之君并称「三王」</strong><br/>③ <strong>与「三皇二帝」不同，三王是三代之君</strong><br/><br/><strong>记法：三代三王。</strong></p><h3>❓ 「夏有禹」的禹是谁？</h3><p><strong>是大禹，夏朝的开国之君，治水的功臣。</strong><br/><br/>① <strong>禹治水十三年，三过家门不入</strong><br/>② <strong>功成受禅，奠定夏朝</strong><br/>③ <strong>非帝王本名，是尊称</strong><br/><br/><strong>记法：禹奠夏基。</strong></p><h3>❓ 什么是「家天下」？</h3><p><strong>是大禹把王位传给儿子启，天下成为一家的私有，世袭制度从此开始。</strong><br/><br/>① <strong>此前是禅让，传贤不传子</strong><br/>② <strong>此后是世袭，传子不传贤</strong><br/>③ <strong>公天下变成了家天下</strong><br/><br/><strong>记法：家天下始。</strong></p><h3>❓ 为什么要「迁夏社」？</h3><p><strong>夏桀暴虐，商汤起兵灭夏，夏的社稷随之迁移。</strong><br/><br/>① <strong>夏享国约四百年</strong><br/>② <strong>桀失德，汤顺天应人</strong><br/>③ <strong>社稷迁移，朝代易主</strong><br/><br/><strong>记法：夏亡迁社。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这四句，给我们三样提醒——</p><p>👑 立业不易</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「夏有禹，商有汤」</strong>；<strong>三王开基不易，后人当饮水思源、敬重开创者</strong>。</p><p>🏺 公与私</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「家天下」提醒我们</strong>；<strong>从禅让到世袭，是制度的一大变迁，读史要懂其所以然</strong>。</p><p>⚖️ 居安思危</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「四百载，迁夏社」</strong>；<strong>再稳固的位子也当警醒，居安思危方能长久</strong><br/><br/><strong>本课的落点：夏有禹，商有汤。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第二十四课。记牢：<strong>夏有禹，商有汤</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>夏有禹，商有汤 · 夏商两代的开国之君。<strong>三王开基。</strong></p><p>周文武，称三王 · 周朝文王武王，三代并称三王。<strong>三代三王。</strong></p><p>夏传子，家天下 · 禹传启，世袭开始。<strong>家天下始。</strong></p><p>四百载，迁夏社 · 夏亡，社稷迁移。<strong>夏亡迁社。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲「三皇二帝」，这一课讲三代三王与家天下，下一课接着讲「汤伐夏，国号商」。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「三王」是哪三位。③ 讲清「家天下」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>夏有禹，商有汤，周文武，称三王，夏传子，家天下，四百载，迁夏社。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '517-xia-you-yu';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 「三王」指哪三代的君主？', ['夏禹、商汤、周文武', '尧、舜、禹', '天、地、人'], '三王是夏商周开国之君'),
    ('2. 「夏有禹」中禹的故事？', ['治水开国，夏朝始祖', '发明文字', '建立商朝'], '大禹治水，奠定夏基'),
    ('3. 「周文武」是谁？', ['周文王、周武王', '周成王、周康王', '周公、召公'], '周朝两位开国之君'),
    ('4. 「称三王」的「王」指什么？', ['三代开国之君的尊称', '皇帝', '神仙'], '禹汤文武并称三王'),
    ('5. 「夏传子」传的是谁？', ['启（禹的儿子）', '舜', '尧'], '大禹传位给儿子启'),
    ('6. 什么是「家天下」？', ['天下成一家私有，世袭开始', '天下是大家的', '分封诸侯'], '禹传启，家天下始'),
    ('7. 「四百载」指哪个朝代？', ['夏朝', '商朝', '周朝'], '夏朝享国约四百年'),
    ('8. 「迁夏社」什么意思？', ['夏亡，社稷迁移', '夏迁都', '夏建国'], '商汤灭夏，社稷迁移'),
    ('9. 从上一课到这一课，制度有何变化？', ['从禅让到世袭（家天下）', '从世袭到禅让', '没有变化'], '三皇二帝禅让 → 夏家天下'),
    ('10. 这一课八句合起来讲什么？', ['三代三王开国与家天下由来', '三皇二帝', '朝代更替全部'], '三王开基，家天下始'),
]
for i, (q, opts, exp) in enumerate(QUIZ):
    R[135 + i] = "  {q: '%s', opts: ['%s', '%s', '%s'], ans: 0, exp: '%s'}," % (q, opts[0], opts[1], opts[2], exp)

for n, text in R.items():
    assert 1 <= n <= len(lines), '行号越界: %d' % n
    lines[n - 1] = text

s = '\n'.join(lines)
s = s.replace('516-zi-xi-nong', '517-xia-you-yu')
s = s.replace('yaoyue518', 'yaoyue519')
s = s.replace('第二十三课', '第二十四课')
assert '516-zi-xi-nong' not in s and 'yaoyue518' not in s and '第二十三课' not in s

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK', DST, len(s), 'chars,', len(s.split('\n')), 'lines')
