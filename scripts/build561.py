#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build561: 以 560 课件（八句版式）为模板生成第 561 课《谨·斗闹场，绝勿近》。
「谨」第七段整段八句：前四句讲远离是非（斗闹场、邪僻事），
后四句讲进门有礼（将入门、将上堂）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（远是非，讲礼貌）/ 3 斗闹场绝勿近·邪僻事绝勿问 /
  4 将入门问孰存·将上堂声必扬 / 5 两句合看（远与礼）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/560-zhi-xu-qi/index.html"
DST = ROOT + "/lessons/561-dou-nao-chang/index.html"

TITLE = '谨 · 斗闹场，绝勿近，将入门，问孰存 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '斗闹场，绝勿近；将入门，问孰存 · 弟子规课堂'
DESC = ('《弟子规》第二十一课，谨第七段。原文：「斗闹场，绝勿近。邪僻事，绝勿问。'
        '将入门，问孰存。将上堂，声必扬。」前四句讲远离是非：争吵打闹的场合绝不靠近，'
        '邪僻不正的事绝不打听；后四句讲进门有礼：进门先问有人在不在，上堂先出声让人知道。')
OG_DESC = '《弟子规》第二十一课：斗闹场绝勿近，将入门问孰存。谨第七段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/561-dou-nao-chang/index.html'

ORIG = '斗闹场，绝勿近。邪僻事，绝勿问。将入门，问孰存。将上堂，声必扬。'
ORIG_COMMA = '斗闹场，绝勿近；邪僻事，绝勿问；将入门，问孰存；将上堂，声必扬。'
OLD_ORIG = '执虚器，如执盈。入虚室，如有人。事勿忙，忙多错。勿畏难，勿轻略。'
OLD_ORIG_COMMA = '执虚器，如执盈；入虚室，如有人；事勿忙，忙多错；勿畏难，勿轻略。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('斗闹场绝勿近', ['dòu', 'nào', 'chǎng', 'jué', 'wù', 'jìn'], True)
             + ju('邪僻事绝勿问', ['xié', 'pì', 'shì', 'jué', 'wù', 'wèn'], False)
             + ju('将入门问孰存', ['jiāng', 'rù', 'mén', 'wèn', 'shú', 'cún'], False)
             + ju('将上堂声必扬', ['jiāng', 'shàng', 'táng', 'shēng', 'bì', 'yáng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">斗闹场</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第七段：斗闹场，绝勿近</p><p class="cover-desc">谨门第七段讲两件事：远离是非、进门有礼。争吵打闹的场合绝不靠近，邪僻不正的事绝不打听；进门先问一声有人在不在，上堂前先出声让人知道。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第七段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>遇到争吵打闹的场合，绝对不要靠近；遇到邪僻不正当的事，绝对不要打听。将要进门时，先问一声「有人在吗」；将要上堂时，先出声让人知道。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「斗闹场」是争吵打架的地方；「邪僻」读 xié pì，是不正经、不合正道的事；「绝」是绝对、断然；「将」是将要；「孰」读 shú，是谁；「存」是在；「堂」是厅堂；「扬」是出声。前四句教人远避是非，后四句教人进门有礼。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 远是非，讲礼貌</h2><p style="margin:0"><strong>先说「远是非」</strong><br/>① <strong>打闹的场合不凑，邪僻的事不打听</strong><br/>② <strong>离是非远一点，人就清净</strong><br/><br/><strong>一句话：绕着走。</strong></p><p><strong>再说「讲礼貌」</strong><br/>① <strong>进门先问一声，上堂先出个声</strong><br/>② <strong>不打扰别人，不冒失吓人</strong><br/><br/><strong>一句话：先打招呼。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>远是非，是管住自己的脚和嘴</strong><br/>② <strong>讲礼貌，是心里装着别人</strong><br/><br/><strong>一句话：远是非，讲礼貌。</strong></p></div>
<!-- 4. 斗闹场绝勿近·邪僻事绝勿问 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>斗闹场，绝勿近；邪僻事，绝勿问</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>斗闹场：争吵打架的场合</strong><br/>② <strong>邪僻 xié pì：不正经的事；绝：绝对</strong><br/><br/><strong>一句话：两个「绝」，态度要坚决。</strong></p><p><strong>斗闹场，绝勿近</strong><br/>① <strong>看热闹容易卷进去，还学到坏脾气</strong><br/>② <strong>有争执绕着走，不围观不起哄</strong><br/><br/><strong>一句话：是非之地，离远点。</strong></p><p><strong>邪僻事，绝勿问</strong><br/>① <strong>不正经的事不打听、不传播</strong><br/>② <strong>耳根清净，心也跟着正</strong><br/><br/><strong>一句话：不问不听不传。</strong></p></div>
<!-- 5. 将入门问孰存·将上堂声必扬 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>将入门，问孰存；将上堂，声必扬</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>将：将要；孰 shú：谁；存：在</strong><br/>② <strong>堂：厅堂；扬：出声让人知道</strong><br/><br/><strong>一句话：进门前，先出声。</strong></p><p><strong>将入门，问孰存</strong><br/>① <strong>先敲门问一声「有人在吗」</strong><br/>② <strong>有人应了再进去，不冒闯</strong><br/><br/><strong>一句话：先问一声再进。</strong></p><p><strong>将上堂，声必扬</strong><br/>① <strong>进厅堂前出个声，让人有准备</strong><br/>② <strong>不悄悄出现在人背后，吓人一跳</strong><br/><br/><strong>一句话：出声，是尊重。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 远与礼</h2><p style="margin:0"><strong>前四句讲「远」</strong><br/>① <strong>远打闹场、远邪僻事</strong><br/>② <strong>管住脚不去、管住嘴不问</strong><br/><br/><strong>一句话：绕着走。</strong></p><p><strong>后四句讲「礼」</strong><br/>① <strong>进门先问、上堂先出声</strong><br/>② <strong>心里装着别人，不打扰人</strong><br/><br/><strong>一句话：先打招呼。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>同学吵架不围观，是非话不打听</strong><br/>② <strong>进房间、进办公室先敲门出声</strong><br/><br/><strong>一句话：远是非，讲礼貌。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：远离是非</strong><br/>① <strong>斗闹场，绝勿近——不去凑热闹</strong><br/>② <strong>邪僻事，绝勿问——不打听不正经的事</strong><br/><br/><strong>一句话：离得远。</strong></p><p><strong>后四句：进门有礼</strong><br/>① <strong>将入门，问孰存——先问有人在吗</strong><br/>② <strong>将上堂，声必扬——先出声让人知道</strong><br/><br/><strong>一句话：先招呼。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>闹场不近，邪事不问</strong><br/>② <strong>进门先问，上堂出声</strong><br/><br/><strong>一句话：远是非，讲礼貌。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>闹场不靠近，进门先出声。</p><p>📖 远是非</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>远是非是管住自己，讲礼貌是尊重别人。</p><p>💡 心里有人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 斗闹场，绝勿近</p>
<p>这是「弟子规课堂」第二十一课：谨第七段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 别人吵架为什么不能凑过去看？</h3><p><strong>看热闹容易惹麻烦。</strong><br/><br/>① <strong>一围观容易卷进去，还学到坏脾气</strong><br/>② <strong>有争执绕着走，不围观不起哄</strong><br/>③ <strong>记法：是非之地，绕着走。</strong></p><h3>❓ 「邪僻事」指什么？</h3><p><strong>不正经、不合正道的事。</strong><br/><br/>① <strong>邪僻读 xié pì，比如赌博、说人坏话</strong><br/>② <strong>不打听、不听、不传，耳根清净</strong><br/>③ <strong>记法：不好的事，离得越远越好。</strong></p><h3>❓ 「问孰存」的「孰」怎么读？</h3><p><strong>读 shú，是「谁」的意思。</strong><br/><br/>① <strong>将入门，问孰存：进门先问「有人在吗」</strong><br/>② <strong>有人应了再进去，才是礼貌</strong><br/>③ <strong>记法：先问一声再进门。</strong></p><h3>❓ 「声必扬」是大声喊吗？</h3><p><strong>不是喊，是让人听见。</strong><br/><br/>① <strong>轻轻敲个门、出声打个招呼就行</strong><br/>② <strong>不悄悄出现在人背后，免得吓人一跳</strong><br/>③ <strong>记法：先出声，再进去。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 是非场合绕着走</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>同学吵架不围观，是非话不打听</strong>；<strong>这就是「斗闹场，绝勿近」</strong>。</p><p>💡 进门先问一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>敲敲门问「有人在吗」，有人应了再进</strong>；<strong>这就是「将入门，问孰存」</strong>。</p><p>🌱 出声再进去</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>进办公室、进房间先出声，不悄悄站到人身后</strong>；<strong>这就是「将上堂，声必扬」</strong><br/><br/><strong>本课的落点：远是非，讲礼貌。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第七段。记牢：<strong>斗闹场，绝勿近</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第七段 · 远是非，讲礼貌。<strong>心里有人</strong>。</p><p>斗闹场，绝勿近 · 打闹场合不凑。<strong>绕着走</strong>。</p><p>邪僻事，绝勿问 · 不正经事不打听。<strong>耳根清净</strong>。</p><p>将入门，问孰存 · 进门先问有人在吗。<strong>先问一声</strong>。</p><p>将上堂，声必扬 · 上堂先出声。<strong>先打招呼</strong>。</p><p><strong>在全篇中的位置:</strong>谨第七段；上一课讲做事的敬与稳，这一课讲远离是非和进门有礼。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「孰」怎么读、「邪僻」是什么意思。② 有人吵架，绕开不围观。③ 今天进房间先敲门问一声。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「斗闹场」指什么？', opts: ['争吵打架的场合', '热闹的集市', '玩耍的操场'], ans: 0, exp: '斗闹场是争吵打闹的地方'},
  {q: '2. 「绝勿近」的「绝」是什么意思？', opts: ['绝对、断然', '断绝朋友', '绝对不'], ans: 0, exp: '绝是绝对'},
  {q: '3. 「邪僻事，绝勿问」讲什么？', opts: ['不正经的事不打听', '路远的事不要问', '偏僻的地方别去'], ans: 0, exp: '邪僻事不打听'},
  {q: '4. 「将入门」的「将」是什么意思？', opts: ['将要', '将军', '把'], ans: 0, exp: '将是将要'},
  {q: '5. 「问孰存」的「孰」怎么读？', opts: ['shú，是谁', 'shū，书', 'shú，熟'], ans: 0, exp: '孰读 shú，是谁'},
  {q: '6. 「声必扬」的「扬」是什么意思？', opts: ['出声让人知道', '表扬', '飞扬'], ans: 0, exp: '扬是出声'},
  {q: '7. 进门前应该先做什么？', opts: ['敲门问一声有人在吗', '直接推门进去', '站在门口不出声'], ans: 0, exp: '问孰存'},
  {q: '8. 看到别人吵架应该怎样？', opts: ['绕开不围观', '凑过去看热闹', '跟着起哄'], ans: 0, exp: '绝勿近'},
  {q: '9. 进老师办公室应该怎样？', opts: ['先敲门出声，应了再进', '直接闯进去', '偷偷溜进去'], ans: 0, exp: '先出声再进'},
  {q: '10. 这一段总的讲什么？', opts: ['远离是非，进门有礼', '怎么打架', '怎么热闹'], ans: 0, exp: '远是非，讲礼貌'},
];'''

raw = io.open(SRC, 'r', encoding='utf-8', newline='').read()
s = raw.replace('\r\n', '\n')

# ---- 头部 meta ----
s = re.sub(r'<meta content="[^"]*" name="description"/>',
           '<meta content="' + DESC + '" name="description"/>', s, count=1)
s = re.sub(r'<meta content="[^"]*" property="og:title"/>',
           '<meta content="' + OG_TITLE + '" property="og:title"/>', s, count=1)
s = re.sub(r'<meta content="[^"]*" property="og:description"/>',
           '<meta content="' + OG_DESC + '" property="og:description"/>', s, count=1)
s = re.sub(r'<meta content="https://[^"]*" property="og:url"/>',
           '<meta content="' + CANON + '" property="og:url"/>', s, count=1)
s = re.sub(r'<link href="https://[^"]*" rel="canonical"/>',
           '<link href="' + CANON + '" rel="canonical"/>', s, count=1)
s = re.sub(r'<title>[^<]*</title>', '<title>' + TITLE + '</title>', s, count=1)

# ---- 讲义区整块替换 ----
A1 = '<!-- ====== 讲义部分 ====== -->'
A2 = '<!-- ====== 测验部分'
i1, i2 = s.find(A1), s.find(A2)
if i1 < 0 or i2 < 0 or i2 < i1:
    print('[FAIL] 找不到讲义区锚点', i1, i2); sys.exit(1)
s = s[:i1] + LECTURE + s[i2:]

# ---- 答疑区整块替换 ----
A3 = '<!-- ====== 答疑解惑 ====== -->'
A4 = '<!-- ====== 结束页 ====== -->'
j1, j2 = s.find(A3), s.find(A4)
if j1 < 0 or j2 < 0 or j2 < j1:
    print('[FAIL] 找不到答疑区锚点', j1, j2); sys.exit(1)
s = s[:j1] + REVIEW + s[j2:]

# ---- QUIZ 数组整块替换 ----
k1 = s.find('const QUIZ = [')
k2 = s.find('window.GUOXUE_QUIZ_OVERRIDE')
if k1 < 0 or k2 < 0 or k2 < k1:
    print('[FAIL] 找不到 QUIZ 锚点', k1, k2); sys.exit(1)
s = s[:k1] + QUIZ + '\n' + s[k2:]

# ---- 全局文字替换 ----
s = s.replace(OLD_ORIG_COMMA, ORIG_COMMA)
s = s.replace(OLD_ORIG, ORIG)
s = s.replace('《弟子规》第二十课', '《弟子规》第二十一课')
s = s.replace('谨第六段', '谨第七段')
s = s.replace("window.GUOXUE_COURSE_ID = '560-zhi-xu-qi';", "window.GUOXUE_COURSE_ID = '561-dou-nao-chang';")
s = s.replace('yaoyue562', 'yaoyue563')

# ---- 校验 ----
for w in ['执虚器，如执盈', '入虚室，如有人', '事勿忙，忙多错', '勿畏难，勿轻略',
          '谨第六段', '560-zhi-xu-qi', 'yaoyue562', '第二十课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
expect = {'slide': s.count('class="slide'), 'ruby': s.count('<ruby'), 'rt': s.count('<rt>'),
          'quiz': s.count("{q: '"), 'page_max': len(re.findall(r'data-page="', s))}
if expect['slide'] != 26 or expect['ruby'] != 24 or expect['rt'] != 24 or expect['quiz'] != 10 or expect['page_max'] != 24:
    print('[FAIL] 结构计数不符（slide 含 viewport/container 两个前缀，应为 24 页 + 2；原文 4 行 24 字，ruby 应为 24）:', expect)
    sys.exit(1)
print('[OK] 结构计数:', expect)
print('[OK] 章节锚点: 讲义区 %d→%d, 答疑区 %d→%d' % (i1, i2, j1, j2))

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(s)
print('[OK] 已生成', DST)
