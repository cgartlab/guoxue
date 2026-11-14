# -*- coding: utf-8 -*-
"""第 515 课《五子者》：以 514 为骨架，逐行替换内容生成新课件。"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '514-san-zhuan-zhe', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '515-wu-zi-zhe')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第二十二课精讲：五子者，有荀扬。文中子，及老庄。上一课讲了《春秋》三传与「经既明，方读子」的读书次第，这一课接着点出诸子百家中最重要的五位代表人物——荀况（荀子）、扬雄、文中子（王通）、老子、庄子。四句话，带我们认识「五子」。" name="description"/>'''
R[7] = '''<meta content="五子者 · 有荀扬，文中子，及老庄 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第二十二课：五子者，有荀扬。文中子，及老庄。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/515-wu-zi-zhe/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/515-wu-zi-zhe/index.html" rel="canonical"/>'''
R[12] = '''<title>五子者 · 有荀扬，文中子，及老庄 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">五子者</h2><div class="cover-ornament"></div><p class="cover-subtitle">有荀扬，文中子，及老庄</p><p class="cover-desc">上一课讲了《春秋》三传，又讲了「经既明，方读子」——六经读通之后，才去读诸子百家。这一课《三字经》紧接着点出诸子中最要紧的五位：荀况（荀子）、扬雄、文中子（王通）、老子、庄子，合称「五子」。四句话，带我们认识这五位大贤。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文四句（两行，每行六字） ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


# 原文仅 12 字（四句），合并成两行，余下空行清空
R[55] = ruby_line(STYLE_A, [('五', 'wǔ'), ('子', 'zǐ'), ('者', 'zhě'), ('有', 'yǒu'), ('荀', 'xún'), ('扬', 'yáng')]) \
     + ruby_line(STYLE_B, [('文', 'wén'), ('中', 'zhōng'), ('子', 'zǐ'), ('及', 'jí'), ('老', 'lǎo'), ('庄', 'zhuāng')])
R[56] = ''
R[57] = ''
R[58] = ''
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>诸子百家之中，有五位最重要的学者：荀况（荀子）、扬雄、文中子（王通），以及老子和庄子。读罢六经，再去博览诸子，而诸子里头，要以这五位最为紧要，所以特地点出来。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》在「经既明，方读子」之后，紧接着举出诸子的代表人物——荀、扬、文中子、老、庄，称「五子」。既告诉我们要读子书，也告诉我们该从哪几位大贤读起。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>诸子之学，各有所长。</strong></p></div>'''

# ---------- 3. 字词梳理 · 八个关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 八个关节</h2><p><span class="ds-highlight">五子者</span>：<strong>子是诸子百家，五子指五位最重要的学者</strong>——<strong>荀况、扬雄、文中子、老子、庄子</strong>。</p><p><span class="ds-highlight">有荀扬</span>：<strong>荀指荀况（尊称荀子），扬指扬雄（字子云）</strong>——<strong>两位都是儒家大贤</strong>。</p><p><span class="ds-highlight">文中子</span>：<strong>隋代学者王通，门人私谥「文中子」</strong>——<strong>著《中说》，拟《论语》讲王道</strong>。</p><p><span class="ds-highlight">及老庄</span>：<strong>老指老子（李耳），庄指庄子（庄周）</strong>——<strong>二人开创道家</strong>。</p><p><span class="ds-highlight">荀子</span>：<strong>战国赵人，著《荀子》，主张性恶、隆礼</strong>——<strong>儒家另一大宗</strong>。</p><p><span class="ds-highlight">扬雄</span>：<strong>西汉成都人，著《法言》《太玄》</strong>——<strong>拟《论语》而作，博通儒道</strong>。</p><p><span class="ds-highlight">老子</span>：<strong>姓李名耳字聃，著《道德经》</strong>——<strong>道家始祖，言清静无为</strong>。</p><p><span class="ds-highlight">庄子</span>：<strong>名周，战国宋人，著《庄子》</strong>——<strong>道家代表，文辞汪洋恣肆</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>五子荀扬，文中老庄。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '五子者', '五 子 者', [
    ('「五子」是哪五位？', '荀况、扬雄、文中子、老子、庄子', '都是诸子中的大贤', '五子并出'),
    ('为什么单举这五位？', '他们代表儒道各家的最高成就', '读子书要从要紧处入手', '提纲挈领'),
    ('「子」指什么？', '诸子百家的学者与著作', '经之后才读子', '经子并观'),
])
R[65] = interp(4, '二', '有荀扬', '有 荀 扬', [
    ('「荀」指谁？', '荀况，尊称荀子，战国赵人', '著《荀子》，主张性恶隆礼', '荀子重礼'),
    ('「扬」指谁？', '扬雄，字子云，西汉成都人', '著《法言》《太玄》，拟《论语》', '扬雄博通'),
    ('两人同属哪一家？', '都归儒家一脉', '荀子重礼法，扬雄重文辞', '儒门两贤'),
])
R[67] = interp(5, '三', '文中子', '文 中 子', [
    ('「文中子」是谁？', '隋代学者王通，门人私谥文中子', '著《中说》，仿《论语》讲王道', '文中讲学'),
    ('为什么叫「文中子」？', '「文中」是私谥，赞其学问德行', '不是本名，是尊称', '谥号尊贤'),
    ('他的书有什么特点？', '《中说》拟《论语》体例', '记录他讲学的言行', '拟论而作'),
])
R[69] = interp(6, '四', '及老庄', '及 老 庄', [
    ('「老」指谁？', '老子，姓李名耳字聃', '著《道德经》，道家始祖', '老子尊道'),
    ('「庄」指谁？', '庄子，名周，战国宋人', '著《庄子》，道家代表', '庄子逍遥'),
    ('老庄合称说明什么？', '二人共创道家一脉', '与儒家的荀扬、文中子并列', '道儒并秀'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 五子者，有荀扬。文中子，及老庄</h2><p>一句话，一层意思——</p><h3>"五子者，有荀扬。文中子，及老庄。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>举出诸子百家中最重要的五位——荀、扬、文中子、老、庄。</p><p>🧭 五子并出</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>读罢六经，要博览诸子；而诸子繁多，先从这五位大贤读起，博采众长。</p><p>📚 由经及子</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>五子各有所长，皆为中华学问的瑰宝；读子书要抓要紧人物，提纲挈领。</p><p>🌿 各有所长</p>'''
R[75] = '''<p>这是「三字经课堂」第二十二课：五子者，有荀扬。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「五子」是哪五位？</h3><p><strong>是荀况（荀子）、扬雄、文中子（王通）、老子、庄子。</strong><br/><br/>① <strong>荀、扬、文中子属儒家一脉</strong><br/>② <strong>老、庄开创道家</strong><br/>③ <strong>五人合称「五子」</strong><br/><br/><strong>记法：五子荀扬，文中老庄。</strong></p><h3>❓ 「文中子」是谁？为什么叫这个名字？</h3><p><strong>是隋代学者王通，门人追尊他为「文中子」。</strong><br/><br/>① <strong>「文中」是私谥，赞其学问与德行</strong><br/>② <strong>他著《中说》，仿《论语》讲王道</strong><br/>③ <strong>不是本名，是尊称</strong><br/><br/><strong>记法：文中讲学。</strong></p><h3>❓ 老子和庄子是什么关系？</h3><p><strong>老子是道家始祖，庄子是道家代表，二人合称「老庄」。</strong><br/><br/>① <strong>老子著《道德经》，讲清静无为</strong><br/>② <strong>庄子著《庄子》，文辞汪洋恣肆</strong><br/>③ <strong>同属道家，一祖一宗</strong><br/><br/><strong>记法：道儒并秀。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这四句，给我们三样提醒——</p><p>📚 博览群书</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「五子者，有荀扬」</strong>；<strong>学问要广博，多读各家之长，眼界才开阔</strong>。</p><p>🎯 各取所长</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>五位大贤各有所长</strong>；<strong>学习也讲取长补短，不必拘于一派</strong>。</p><p>🧭 兼容并包</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>由经及子，提纲挈领</strong>；<strong>先立根本，再广采众说，人生与学问都更厚重</strong><br/><br/><strong>本课的落点：五子者，有荀扬。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第二十二课。记牢：<strong>五子者，有荀扬</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                五子者，有荀扬。文中子，及老庄。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>五子者 · 诸子中最要紧的五位：荀、扬、文中子、老、庄。<strong>五子并出。</strong></p><p>有荀扬 · 荀子重礼法，扬雄博通儒道。<strong>儒门两贤。</strong></p><p>文中子 · 王通著《中说》，拟《论语》讲学。<strong>文中讲学。</strong></p><p>及老庄 · 老子道家始祖，庄子道家代表。<strong>道儒并秀。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲《春秋》三传与「经既明，方读子」，这一课讲读子要从「五子」入手，下一课接着讲读罢经子要读史（「经子通，读诸史」）。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>五子者，有荀扬。文中子，及老庄。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这四句背下来。② 说出「五子」是哪五位。③ 讲清「文中子」是谁。</p><p><strong>把这一课记在心里:</strong><strong>五子者，有荀扬，文中子，及老庄。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "五子者，有荀扬。文中子，及老庄。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '515-wu-zi-zhe';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 「五子」指的是哪五位？', ['荀况、扬雄、文中子、老子、庄子', '李白、杜甫、王维、白居易、李商隐', '伏羲、神农、黄帝、尧、舜'], '五子是诸子中的五位大贤'),
    ('2. 「荀」指的是谁？', ['荀况（荀子）', '荀彧', '荀攸'], '战国儒家大师，著《荀子》'),
    ('3. 「扬」指的是谁？', ['扬雄（字子云）', '扬执戟', '扬朱'], '西汉学者，著《法言》《太玄》'),
    ('4. 「文中子」是谁？', ['隋代学者王通', '孔子', '孟子'], '门人私谥文中子，著《中说》'),
    ('5. 「老」指的是谁？', ['老子（李耳）', '老莱子', '老聃的弟子'], '道家始祖，著《道德经》'),
    ('6. 「庄」指的是谁？', ['庄子（庄周）', '庄蹻', '庄贾'], '道家代表，著《庄子》'),
    ('7. 「五子」属于哪一类人？', ['诸子百家的学者', '五经博士', '五代君主'], '经之后读子，五子为子书代表'),
    ('8. 老子的主要著作是？', ['《道德经》', '《论语》', '《孟子》'], '道家根本经典'),
    ('9. 庄子的主要著作是？', ['《庄子》', '《荀子》', '《法言》'], '道家代表之作'),
    ('10. 这一课四句讲什么？', ['诸子百家中最重要的五位代表', '五经的作者', '五代的历史'], '五子荀扬，文中老庄'),
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
