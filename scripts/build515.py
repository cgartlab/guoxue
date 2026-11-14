# -*- coding: utf-8 -*-
"""第 515 课《五子者·经子通》：以 514 为骨架，逐行替换内容生成新课件。
原文两句话（两组，每组六言两句，共四句24字）合成一课，对齐 514 模式：
  五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '514-san-zhuan-zhe', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '515-wu-zi-zhe')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第二十二课精讲：五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。上一课讲了《春秋》三传与「经既明，方读子」的读书次第，这一课先举出诸子百家最重要的五位代表——荀况、扬雄、文中子、老子、庄子（五子）；再告诉我们读罢经子要读史，考究世代的统系、知晓兴衰的终始。八句话，讲完「子」与「史」。" name="description"/>'''
R[7] = '''<meta content="五子者 · 有荀扬，文中子，及老庄 · 经子通，读诸史 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第二十二课：五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/515-wu-zi-zhe/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/515-wu-zi-zhe/index.html" rel="canonical"/>'''
R[12] = '''<title>五子者 · 有荀扬，文中子，及老庄 · 经子通，读诸史 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">五子者</h2><div class="cover-ornament"></div><p class="cover-subtitle">有荀扬，文中子，及老庄；经子通，读诸史，考世系，知终始</p><p class="cover-desc">上一课讲了《春秋》三传，又讲了「经既明，方读子」——六经读通之后，才去读诸子百家。这一课《三字经》先点出诸子中最要紧的五位大贤：荀况（荀子）、扬雄、文中子（王通）、老子、庄子，合称「五子」；再告诉我们：经子读通之后，就要去读史书，考究世代的统系、知道王朝兴衰的终始。八句话，讲完「子」与「史」。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文四句（两句一组，共四句） ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


# 原文共四句（两组），合并成四行
R[55] = ruby_line(STYLE_A, [('五', 'wǔ'), ('子', 'zǐ'), ('者', 'zhě'), ('有', 'yǒu'), ('荀', 'xún'), ('扬', 'yáng')]) \
     + ruby_line(STYLE_B, [('文', 'wén'), ('中', 'zhōng'), ('子', 'zǐ'), ('及', 'jí'), ('老', 'lǎo'), ('庄', 'zhuāng')]) \
     + ruby_line(STYLE_B, [('经', 'jīng'), ('子', 'zǐ'), ('通', 'tōng'), ('读', 'dú'), ('诸', 'zhū'), ('史', 'shǐ')]) \
     + ruby_line(STYLE_B, [('考', 'kǎo'), ('世', 'shì'), ('系', 'xì'), ('知', 'zhī'), ('终', 'zhōng'), ('始', 'shǐ')])
R[56] = ''
R[57] = ''
R[58] = ''
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>诸子百家之中，有五位最重要的学者：荀况（荀子）、扬雄、文中子（王通），以及老子和庄子，合称「五子」。读经、读子都通晓之后，便去读历代史书；读史要考究世代的统系，知晓王朝兴衰的终始。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》在「经既明，方读子」之后，先举出诸子代表「五子」，再讲读书的次第——经、子之后是史。经子史贯通，学问才有根有叶有脉络。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>经以载道，子以明术，史以知变。</strong></p></div>'''

# ---------- 3. 字词梳理 · 九关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">五子者</span>：<strong>子是诸子百家，五子指五位最重要的学者</strong>——<strong>荀况、扬雄、文中子、老子、庄子</strong>。</p><p><span class="ds-highlight">有荀扬</span>：<strong>荀指荀况（尊称荀子），扬指扬雄（字子云）</strong>——<strong>两位都是儒家大贤</strong>。</p><p><span class="ds-highlight">文中子</span>：<strong>隋代学者王通，门人私谥「文中子」</strong>——<strong>著《中说》，拟《论语》讲王道</strong>。</p><p><span class="ds-highlight">及老庄</span>：<strong>老指老子（李耳），庄指庄子（庄周）</strong>——<strong>二人开创道家</strong>。</p><p><span class="ds-highlight">经子通</span>：<strong>经是六经，子是诸子，通是通晓</strong>——<strong>经与子都读通了</strong>。</p><p><span class="ds-highlight">读诸史</span>：<strong>诸是众多，史是史书</strong>——<strong>接着去读历代史册</strong>。</p><p><span class="ds-highlight">考世系</span>：<strong>考是考究，世系是家族与朝代的统系</strong>——<strong>弄清谁承接谁</strong>。</p><p><span class="ds-highlight">知终始</span>：<strong>终是末代，始是开国</strong>——<strong>知晓王朝兴衰的来龙去脉</strong>。</p><p><span class="ds-highlight">经与史</span>：<strong>经立根本，史观变迁</strong>——<strong>经子之后读史，学问方全</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>五子荀扬，文中老庄；经子既通，读史知变。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '五子者，有荀扬', '五 子 者 ， 有 荀 扬', [
    ('「五子」是哪五位？', '荀况、扬雄、文中子、老子、庄子', '都是诸子中的大贤', '五子并出'),
    ('为什么单举这五位？', '他们代表儒道各家的最高成就', '读子书要从要紧处入手', '提纲挈领'),
    ('「子」指什么？', '诸子百家的学者与著作', '经之后才读子', '经子并观'),
])
R[65] = interp(4, '二', '文中子，及老庄', '文 中 子 ， 及 老 庄', [
    ('「文中子」是谁？', '隋代学者王通，门人私谥文中子', '著《中说》，仿《论语》讲王道', '文中讲学'),
    ('「老」「庄」指谁？', '老子（李耳）与庄子（庄周）', '二人共创道家一脉', '道儒并秀'),
    ('老庄与荀扬有何不同？', '荀扬归儒，老庄归道', '儒道并立，各有所长', '儒道双峰'),
])
R[67] = interp(5, '三', '经子通，读诸史', '经 子 通 ， 读 诸 史', [
    ('「经子通」怎么讲？', '六经与诸子都读通了', '根基与博学兼备', '经子贯通'),
    ('为什么要「读诸史」？', '史书记录历代兴亡得失', '以史为鉴，可知兴替', '读史明智'),
    ('读书的次第是什么？', '先经，再子，后史', '本末有序，脉络才清', '经子史次第'),
])
R[69] = interp(6, '四', '考世系，知终始', '考 世 系 ， 知 终 始', [
    ('「考世系」考什么？', '考究家族与朝代的传承统系', '弄清谁承接谁', '考索源流'),
    ('「知终始」知什么？', '知晓王朝由兴到亡的始末', '明白兴衰的来龙去脉', '通观终始'),
    ('这一句的落点？', '经子之后读史，读史要明统系', '学问经子史贯通', '经子史全'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始</h2><p>一句话，两层意思——</p><h3>"五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前四句举出诸子百家中最重要的五位——荀、扬、文中子、老、庄；后四句讲读书的次第：经子读通后读史，读史要考世系、知终始。</p><p>📜 五子并出</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>经立根本，子明方术，史观变迁；先经后子再史，本末有序，学问才有根有叶有脉络。</p><p>📚 经子史次第</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>五子各有所长，皆为中华学问的瑰宝；读罢经子读史，方能贯通古今。</p><p>🌿 经子史贯通</p>'''
R[75] = '''<p>这是「三字经课堂」第二十二课：五子者，有荀扬。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「五子」是哪五位？</h3><p><strong>是荀况（荀子）、扬雄、文中子（王通）、老子、庄子。</strong><br/><br/>① <strong>荀、扬、文中子属儒家一脉</strong><br/>② <strong>老、庄开创道家</strong><br/>③ <strong>五人合称「五子」</strong><br/><br/><strong>记法：五子荀扬，文中老庄。</strong></p><h3>❓ 「文中子」是谁？为什么叫这个名字？</h3><p><strong>是隋代学者王通，门人追尊他为「文中子」。</strong><br/><br/>① <strong>「文中」是私谥，赞其学问与德行</strong><br/>② <strong>他著《中说》，仿《论语》讲王道</strong><br/>③ <strong>不是本名，是尊称</strong><br/><br/><strong>记法：文中讲学。</strong></p><h3>❓ 「经子通，读诸史」是什么意思？</h3><p><strong>六经和诸子都读通之后，接着去读历代史书。</strong><br/><br/>① <strong>经立根本，子明方术</strong><br/>② <strong>史书记录兴亡得失，以史为鉴</strong><br/>③ <strong>先经后子再史，本末有序</strong><br/><br/><strong>记法：经子史次第。</strong></p><h3>❓ 「考世系，知终始」怎么理解？</h3><p><strong>读史要考究家族与朝代的统系，知晓王朝兴衰的来龙去脉。</strong><br/><br/>① <strong>世系是传承的脉络</strong><br/>② <strong>终始是兴亡的始末</strong><br/>③ <strong>明统系方能通观古今</strong><br/><br/><strong>记法：考索源流。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这八句，给我们三样提醒——</p><p>📚 博览群书</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「五子者，有荀扬」</strong>；<strong>学问要广博，多读各家之长，眼界才开阔</strong>。</p><p>🎯 提纲挈领</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「考世系，知终始」提醒我们</strong>；<strong>看事要看来龙去脉，不囫囵吞枣</strong>。</p><p>🧭 读史明智</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>经子史次第</strong>；<strong>先立根本，再广采众说、通观古今，人生与学问都更厚重</strong><br/><br/><strong>本课的落点：五子者，有荀扬。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第二十二课。记牢：<strong>五子者，有荀扬</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>五子者，有荀扬 · 诸子中最要紧的五位：荀、扬、文中子、老、庄。<strong>五子并出。</strong></p><p>文中子，及老庄 · 王通著《中说》，老子庄子开创道家。<strong>道儒并秀。</strong></p><p>经子通，读诸史 · 经子读通，接着读历代史书。<strong>经子史次第。</strong></p><p>考世系，知终始 · 考究统系，知晓兴衰始末。<strong>考索源流。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲《春秋》三传与「经既明，方读子」，这一课讲读子要从「五子」入手、读罢经子要读史，下一课接着讲读史的开端（三皇五帝）。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「五子」是哪五位。③ 讲清「经子通，读诸史」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>五子者，有荀扬，文中子，及老庄，经子通，读诸史，考世系，知终始。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "五子者，有荀扬。文中子，及老庄。经子通，读诸史。考世系，知终始。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '515-wu-zi-zhe';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 「五子」指的是哪五位？', ['荀况、扬雄、文中子、老子、庄子', '李白、杜甫、王维、白居易、李商隐', '伏羲、神农、黄帝、尧、舜'], '五子是诸子中的五位大贤'),
    ('2. 「荀」指的是谁？', ['荀况（荀子）', '荀彧', '荀攸'], '战国儒家大师，著《荀子》'),
    ('3. 「扬」指的是谁？', ['扬雄（字子云）', '扬执戟', '扬朱'], '西汉学者，著《法言》《太玄》'),
    ('4. 「文中子」是谁？', ['隋代学者王通', '孔子', '孟子'], '门人私谥文中子，著《中说》'),
    ('5. 「老」「庄」开创哪一家？', ['道家', '儒家', '法家'], '老子庄子共创道家一脉'),
    ('6. 「经子通」是什么意思？', ['六经与诸子都读通了', '经历和子女都通晓', '经书和孩子都读过'], '根基与博学兼备'),
    ('7. 「读诸史」的「史」指什么？', ['历代史书', '历史故事书', '史官'], '读史以鉴兴替'),
    ('8. 「考世系」考什么？', ['家族与朝代的传承统系', '世界的系统', '事业的体系'], '弄清谁承接谁'),
    ('9. 「知终始」知什么？', ['王朝兴衰的来龙去脉', '事情的结尾', '终点和起点'], '通观兴亡始末'),
    ('10. 这一课八句合起来讲什么？', ['诸子代表「五子」与读经子后读史的次第', '五经的作者', '五代的历史'], '五子并出，经子史次第'),
]
for i, (q, opts, exp) in enumerate(QUIZ):
    R[135 + i] = "  {q: '%s', opts: ['%s', '%s', '%s'], ans: 0, exp: '%s'}," % (q, opts[0], opts[1], opts[2], exp)

for n, text in R.items():
    assert 1 <= n <= len(lines), '行号越界: %d' % n
    lines[n - 1] = text

s = '\n'.join(lines)
s = s.replace('514-san-zhuan-zhe', '515-wu-zi-zhe')
s = s.replace('yaoyue516', 'yaoyue517')
s = s.replace('第二十一课', '第二十二课')
assert '514-san-zhuan-zhe' not in s and 'yaoyue516' not in s and '第二十一课' not in s

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK', DST, len(s), 'chars,', len(s.split('\n')), 'lines')
