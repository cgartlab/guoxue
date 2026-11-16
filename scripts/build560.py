#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build560: 以 559 课件（八句版式）为模板生成第 560 课《谨·执虚器，如执盈》。
「谨」第六段整段八句：前四句讲恭敬用心（执虚器、如执盈、入虚室、如有人），
后四句讲做事态度（事勿忙、忙多错、勿畏难、勿轻略）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（心里有敬，做事有稳）/ 3 执虚器如执盈·入虚室如有人 /
  4 事勿忙忙多错·勿畏难勿轻略 / 5 两句合看（敬与稳）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/559-wu-jian-yu/index.html"
DST = ROOT + "/lessons/560-zhi-xu-qi/index.html"

TITLE = '谨 · 执虚器，如执盈，事勿忙，忙多错 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '执虚器，如执盈；事勿忙，忙多错 · 弟子规课堂'
DESC = ('《弟子规》第二十课，谨第六段。原文：「执虚器，如执盈。入虚室，如有人。'
        '事勿忙，忙多错。勿畏难，勿轻略。」前四句讲恭敬用心：空器皿也端得像满的一样小心，'
        '空屋子也像有人在一样守规矩；后四句讲做事态度：不慌不乱、不怕难、不马虎。')
OG_DESC = '《弟子规》第二十课：执虚器如执盈，事勿忙忙多错。谨第六段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/560-zhi-xu-qi/index.html'

ORIG = '执虚器，如执盈。入虚室，如有人。事勿忙，忙多错。勿畏难，勿轻略。'
ORIG_COMMA = '执虚器，如执盈；入虚室，如有人；事勿忙，忙多错；勿畏难，勿轻略。'
OLD_ORIG = '勿践阈，勿跛倚。勿箕踞，勿摇髀。缓揭帘，勿有声。宽转弯，勿触棱。'
OLD_ORIG_COMMA = '勿践阈，勿跛倚；勿箕踞，勿摇髀；缓揭帘，勿有声；宽转弯，勿触棱。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('执虚器如执盈', ['zhí', 'xū', 'qì', 'rú', 'zhí', 'yíng'], True)
             + ju('入虚室如有人', ['rù', 'xū', 'shì', 'rú', 'yǒu', 'rén'], False)
             + ju('事勿忙忙多错', ['shì', 'wù', 'máng', 'máng', 'duō', 'cuò'], False)
             + ju('勿畏难勿轻略', ['wù', 'wèi', 'nán', 'wù', 'qīng', 'lüè'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">执虚器</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第六段：执虚器，如执盈</p><p class="cover-desc">谨门第六段讲两件事：心里有敬、做事有稳。空杯子也端得像满的一样小心，空屋子也像有人一样守规矩；做事不慌张，不怕难也不马虎。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第六段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>拿空器皿，要像拿着装满的东西一样小心；进空屋子，要像屋里有人一样守规矩。做事不要慌忙，一慌就容易出错；不要怕难，也不要轻视、马虎。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「虚」是空；「器」是器皿；「盈」读 yíng，是满；「畏」是害怕；「轻略」是轻视、不当回事。「如执盈」「如有人」的两个「如」，教的就是一个「敬」字——没人看见也照规矩做。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 心里有敬，做事有稳</h2><p style="margin:0"><strong>先说「敬」</strong><br/>① <strong>空器当满器端，空室当有人待</strong><br/>② <strong>没人看见，也不打折扣</strong><br/><br/><strong>一句话：心里有敬。</strong></p><p><strong>再说「稳」</strong><br/>① <strong>事不多慌，忙中易错</strong><br/>② <strong>难事敢做，易事认真</strong><br/><br/><strong>一句话：做事有稳。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>敬是对人对事的心，稳是做事的样子</strong><br/>② <strong>心稳了，事才做得好</strong><br/><br/><strong>一句话：心敬事稳。</strong></p></div>
<!-- 4. 执虚器如执盈·入虚室如有人 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>执虚器，如执盈；入虚室，如有人</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>虚：空；器：器皿；盈 yíng：满</strong><br/>② <strong>两个「如」：当作、好像</strong><br/><br/><strong>一句话：小心，是练出来的。</strong></p><p><strong>执虚器，如执盈</strong><br/>① <strong>空杯空盘也端稳，不毛手毛脚</strong><br/>② <strong>东西少也不随便，养成细心</strong><br/><br/><strong>一句话：手里空，心里不空。</strong></p><p><strong>入虚室，如有人</strong><br/>① <strong>一个人也不乱翻乱动</strong><br/>② <strong>没人看着，规矩照样在</strong><br/><br/><strong>一句话：无人也自律。</strong></p></div>
<!-- 5. 事勿忙忙多错·勿畏难勿轻略 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>事勿忙，忙多错；勿畏难，勿轻略</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>忙：慌张；错：出错</strong><br/>② <strong>畏：怕；轻略：轻视、马虎</strong><br/><br/><strong>一句话：不慌、不怕、不敷衍。</strong></p><p><strong>事勿忙，忙多错</strong><br/>① <strong>越急越容易出错，稳一点反而快</strong><br/>② <strong>事多就一件一件来，别乱了套</strong><br/><br/><strong>一句话：慢下来，才做得对。</strong></p><p><strong>勿畏难，勿轻略</strong><br/>① <strong>难题敢上手，试了才会</strong><br/>② <strong>简单题也认真，别大意丢分</strong><br/><br/><strong>一句话：难的不怕，易的不轻。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 敬与稳</h2><p style="margin:0"><strong>前四句讲「敬」</strong><br/>① <strong>空器也端稳，空室也守规矩</strong><br/>② <strong>敬不在人前，在没人看见的时候</strong><br/><br/><strong>一句话：慎独。</strong></p><p><strong>后四句讲「稳」</strong><br/>① <strong>不慌、不怕、不马虎</strong><br/>② <strong>态度端正，事情才做得好</strong><br/><br/><strong>一句话：稳当。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>端空碗也端稳，一个人在屋也守规矩</strong><br/>② <strong>作业多不慌，难题敢试、易题认真</strong><br/><br/><strong>一句话：心敬事稳。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：心里有敬</strong><br/>① <strong>执虚器，如执盈——空器也小心</strong><br/>② <strong>入虚室，如有人——无人也自律</strong><br/><br/><strong>一句话：敬在心里。</strong></p><p><strong>后四句：做事有稳</strong><br/>① <strong>事勿忙，忙多错——不慌不乱</strong><br/>② <strong>勿畏难，勿轻略——不怕不敷衍</strong><br/><br/><strong>一句话：稳在手上。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>空器端稳，空室守规</strong><br/>② <strong>不慌、不怕、不马虎</strong><br/><br/><strong>一句话：心敬事稳。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>空器当满器端，做事不慌不怕不马虎。</p><p>📖 敬与稳</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>敬在没人看见时，稳在不慌不忙中。</p><p>💡 慎独慎微</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 执虚器，如执盈</p>
<p>这是「弟子规课堂」第二十课：谨第六段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 空杯子为什么要端得像满的一样？</h3><p><strong>练的是小心和敬。</strong><br/><br/>① <strong>空杯也端稳，不洒不碰，养成细心</strong><br/>② <strong>东西少也不随便，习惯成自然</strong><br/>③ <strong>记法：手里空，心里不空。</strong></p><h3>❓ 「入虚室，如有人」是什么意思？</h3><p><strong>空屋子也当有人，守规矩不偷懒。</strong><br/><br/>① <strong>没人看着也不乱翻乱动</strong><br/>② <strong>规矩不是做给人看的，是自己的修养</strong><br/>③ <strong>记法：无人也自律，叫慎独。</strong></p><h3>❓ 「事勿忙」是做事慢吞吞吗？</h3><p><strong>不是慢，是不慌。</strong><br/><br/>① <strong>一慌就容易出错，稳一点反而更快</strong><br/>② <strong>事多就一件一件来，别乱了套</strong><br/>③ <strong>记法：慢下来，才做得对。</strong></p><h3>❓ 「勿畏难，勿轻略」怎么理解？</h3><p><strong>难的不怕，易的不轻。</strong><br/><br/>① <strong>畏是怕；难事敢试，试了才会</strong><br/>② <strong>轻略是马虎；简单的事也认真做</strong><br/>③ <strong>记法：难事敢上手，易事不大意。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 端东西也端稳</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>空杯空盘也小心端好，轻拿轻放</strong>；<strong>这就是「执虚器，如执盈」</strong>。</p><p>💡 一个人也守规矩</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>没人看着也不乱翻乱动，不偷懒</strong>；<strong>这就是「入虚室，如有人」</strong>。</p><p>🌱 做事不慌不马虎</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>作业多一件件做，难题敢试、易题认真</strong>；<strong>这就是「事勿忙，勿轻略」</strong><br/><br/><strong>本课的落点：心敬事稳。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第六段。记牢：<strong>执虚器，如执盈</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第六段 · 心里有敬，做事有稳。<strong>心敬事稳</strong>。</p><p>执虚器，如执盈 · 空器也端稳。<strong>细心</strong>。</p><p>入虚室，如有人 · 无人也守规矩。<strong>自律</strong>。</p><p>事勿忙，忙多错 · 不慌不乱。<strong>稳当</strong>。</p><p>勿畏难，勿轻略 · 不怕难不马虎。<strong>有担当</strong>。</p><p><strong>在全篇中的位置:</strong>谨第六段；上一课讲坐立规矩和动作轻缓，这一课讲做事的敬与稳。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「盈」「畏」「略」怎么读。② 端一次空杯子，也端得稳稳的。③ 今天做事前先想一想，不慌不忙。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「执虚器」的「虚」是什么意思？', opts: ['空的', '假的', '虚弱'], ans: 0, exp: '虚是空'},
  {q: '2. 「如执盈」的「盈」是什么意思？', opts: ['满的', '干净', '贵重'], ans: 0, exp: '盈读 yíng，是满'},
  {q: '3. 「入虚室，如有人」讲什么？', opts: ['空屋子也当有人守规矩', '进屋前要敲门', '屋里一定有人'], ans: 0, exp: '无人也自律'},
  {q: '4. 「事勿忙」是为什么？', opts: ['忙中容易出错', '忙显得能干', '忙才做得快'], ans: 0, exp: '忙多错'},
  {q: '5. 「忙多错」的「错」是什么意思？', opts: ['出错', '错开', '交错'], ans: 0, exp: '错是出错'},
  {q: '6. 「勿畏难」的「畏」是什么意思？', opts: ['害怕', '敬佩', '围墙'], ans: 0, exp: '畏是怕'},
  {q: '7. 「勿轻略」讲什么？', opts: ['不轻视、不马虎', '走路要轻', '省略步骤'], ans: 0, exp: '轻略是马虎'},
  {q: '8. 端空杯子应该怎样？', opts: ['像端满的一样小心', '随便拿', '两只手捧着跑'], ans: 0, exp: '执虚器如执盈'},
  {q: '9. 一个人在屋里应该怎样？', opts: ['也守规矩不乱动', '随便翻东西', '大声吵闹'], ans: 0, exp: '入虚室如有人'},
  {q: '10. 这一段总的讲什么？', opts: ['心里有敬，做事稳当', '怎么端杯子', '怎么快做完事'], ans: 0, exp: '心敬事稳'},
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
s = s.replace('《弟子规》第十九课', '《弟子规》第二十课')
s = s.replace('谨第五段', '谨第六段')
s = s.replace("window.GUOXUE_COURSE_ID = '559-wu-jian-yu';", "window.GUOXUE_COURSE_ID = '560-zhi-xu-qi';")
s = s.replace('yaoyue561', 'yaoyue562')

# ---- 校验 ----
for w in ['勿践阈，勿跛倚', '勿箕踞，勿摇髀', '缓揭帘，勿有声', '宽转弯，勿触棱',
          '谨第五段', '559-wu-jian-yu', 'yaoyue561', '第十九课']:
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
