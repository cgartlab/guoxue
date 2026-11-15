#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build543: 以 542 课件为模板生成第 543 课《入则孝·冬温夏凊·晨省昏定》。

讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（上一课答应，这一课照料）/ 3 冬温夏凊（黄香温席）/
  4 晨省昏定 / 5 出告反面 + 居有常业无变 / 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。
区域替换法：讲义区整块换、答疑区整块换、QUIZ 数组整块换、头部 meta 正则换。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/542-ru-ze-xiao-fu-mu-hu/index.html"
DST = ROOT + "/lessons/543-dong-wen-xia-qing/index.html"

TITLE = '入则孝 · 冬温夏凊，晨省昏定 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '冬则温，夏则凊，晨则省，昏则定 · 弟子规课堂'
DESC = ('《弟子规》第三课，入则孝第二段。原文：「冬则温，夏则凊。晨则省，昏则定。'
        '出必告，反必面。居有常，业无变。」讲四件事——冬天替父母暖，夏天替父母凉；'
        '早晨向父母问安，晚上把父母安顿好；出门说一声去哪，回来先照个面；'
        '住处和作息有定准，学业本业踏实做不轻易改换。上一课讲「叫一声就应」，'
        '这一课讲「把父母放在心上」：冷暖有人管、早晚有人问、行踪有交代、生活有常法。'
        '东汉黄香九岁温席的故事，就是「冬则温」的来历。')
OG_DESC = '《弟子规》第三课：冬温夏凊、晨省昏定、出必告反必面、居有常业无变，讲四件照料父母的小事。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/543-dong-wen-xia-qing/index.html'

ORIG = '冬则温，夏则凊。晨则省，昏则定。出必告，反必面。居有常，业无变。'
ORIG_COMMA = '冬则温，夏则凊，晨则省，昏则定；出必告，反必面，居有常，业无变。'
OLD_ORIG = '父母呼，应勿缓。父母命，行勿懒。父母教，须敬听。父母责，须顺承。'
OLD_ORIG_COMMA = '父母呼，应勿缓，父母命，行勿懒；父母教，须敬听，父母责，须顺承。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('冬则温夏则凊', ['dōng', 'zé', 'wēn', 'xià', 'zé', 'qìng'], True)
             + ju('晨则省昏则定', ['chén', 'zé', 'xǐng', 'hūn', 'zé', 'dìng'], False)
             + ju('出必告反必面', ['chū', 'bì', 'gào', 'fǎn', 'bì', 'miàn'], False)
             + ju('居有常业无变', ['jū', 'yǒu', 'cháng', 'yè', 'wú', 'biàn'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">冬温夏凊</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第二段：晨则省，昏则定</p><p class="cover-desc">上一课讲「叫你就应」——那是嘴上的功夫。这一段往深走一层：父母的冷暖、早晚、行踪、生活，你心里有没有数。四组八个字，都是日常，做起来不难，难在天天做。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第二段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>冬天替父母暖，夏天替父母凉；早晨向父母问安，晚上把父母安顿好；出门说一声去哪里，回来先与父母照面；住处和作息有定准，本业踏实做不轻易改换。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「凊」读 qìng，是凉；「省」读 xǐng，是问安；「反」同「返」。这一段四组八字，讲的都是照料与交代。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 从「答应」到「照料」</h2><p style="margin:0"><strong>上一课管嘴</strong><br/>① <strong>叫你，应一声</strong><br/>② <strong>派你，动手办</strong><br/><br/><strong>一句话：先学会回应。</strong></p><p><strong>这一课管心</strong><br/>① <strong>冷暖、早晚、出门回来、日子怎么过</strong><br/>② <strong>心里装着父母，才会想到这些</strong><br/><br/><strong>一句话：把父母放在心上。</strong></p><p><strong>四组八字</strong><br/>① <strong>冬夏、晨昏、出反、居业</strong><br/>② <strong>身体、问安、行踪、根本</strong><br/><br/><strong>一句话：事事有交代。</strong></p></div>
<!-- 4. 冬温夏凊 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>冬则温，夏则凊</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>温：让父母不受冷</strong><br/>② <strong>凊读 qìng：凉，让父母不受热</strong><br/><br/><strong>一句话：冷热先想到父母。</strong></p><p><strong>黄香温席</strong><br/>① <strong>东汉黄香，九岁丧母，事父至孝</strong><br/>② <strong>冬天先躺进被窝暖热，夏天先扇凉枕席</strong><br/><br/><strong>一句话：九岁孩子想到的。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>提前开暖气、灌热水袋、把被窝暖上</strong><br/>② <strong>夏天空调别对着父母吹</strong><br/><br/><strong>一句话：换样做法，意思不变。</strong></p></div>
<!-- 5. 晨省昏定 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>晨则省，昏则定</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>晨：早上；昏：晚上</strong><br/>② <strong>省读 xǐng：问候请安；定：安顿好</strong><br/><br/><strong>一句话：早晚各照一面。</strong></p><p><strong>怎么做</strong><br/>① <strong>早上问一句「昨夜睡得好不好」</strong><br/>② <strong>晚上说一声「我回来了，您早些休息」</strong><br/><br/><strong>一句话：不用行礼，留个照面。</strong></p><p><strong>为什么放在早晚</strong><br/>① <strong>早晚是老人最容易出事的时候</strong><br/>② <strong>一面照见，就少一分牵挂</strong><br/><br/><strong>一句话：看一眼，心里有底。</strong></p></div>
<!-- 6. 出告反面 + 居有常业无变 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>出必告，反必面；居有常，业无变</h2><p style="margin:0"><strong>出必告，反必面</strong><br/>① <strong>出门说一声去哪儿、几时回</strong><br/>② <strong>反同返，回来先让父母看见你</strong><br/><br/><strong>一句话：行踪有交代。</strong></p><p><strong>居有常，业无变</strong><br/>① <strong>住处、作息有定准，不东飘西荡</strong><br/>② <strong>学业本业踏实做，不三天打鱼</strong><br/><br/><strong>一句话：日子有常法。</strong></p><p><strong>四句合看</strong><br/>① <strong>前两句管「一时」，后两句管「长久」</strong><br/>② <strong>都做到了，父母就不必替你悬心</strong><br/><br/><strong>一句话：安心是最大的孝。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四组对子</h2><p style="margin:0"><strong>管身体：冬温夏凊</strong><br/>① <strong>冷了先想着给父母添衣</strong><br/>② <strong>热了先想着给父母消暑</strong><br/><br/><strong>一句话：冷热挂在心上。</strong></p><p><strong>管问候：晨省昏定</strong><br/>① <strong>早上一句问安，晚上一句安顿</strong><br/>② <strong>人在跟前，就亲自去一趟</strong><br/><br/><strong>一句话：早晚不断线。</strong></p><p><strong>管行踪与根本：出告反面、居有常业无变</strong><br/>① <strong>出门回来都有声，父母不用猜</strong><br/>② <strong>生活有定准、本业有恒心</strong><br/><br/><strong>一句话：让父母放心。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>暖被窝、扇枕席、早晚问一句、出门说一声。</p><p>📖 全是琐事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>琐事里藏着「我心里有你」；孝不孝，先看这些事上你有没有数。</p><p>💡 心在细处</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 让父母放心</p>
<p>这是「弟子规课堂」第三课：入则孝第二段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 现在有空调暖气，「冬温夏凊」还怎么做？</h3><p><strong>换个做法，意思不变。</strong><br/><br/>① <strong>冬天先把屋子烘暖、被窝暖上</strong><br/>② <strong>夏天先把凉席擦净、温度调好</strong><br/>③ <strong>不在身边，就打个电话问冷问热</strong><br/><br/><strong>记法：想到冷热，就是温凊。</strong></p><h3>❓ 古人天天早晚请安，现在也要吗？</h3><p><strong>不用行礼，留个照面。</strong><br/><br/>① <strong>早上问一句睡得好不好</strong><br/>② <strong>晚上说一声我回来了</strong><br/>③ <strong>住得远，就早晚各一条消息</strong><br/><br/><strong>记法：早晚见个影、听个声。</strong></p><h3>❓ 都成年了，出门还要交代吗？</h3><p><strong>说一句，不丢面子。</strong><br/><br/>① <strong>不是请示，是让父母心里有底</strong><br/>② <strong>说清去哪儿、几时回</strong><br/>③ <strong>晚归提前说一声，免得等门</strong><br/><br/><strong>记法：一声交代，一夜安睡。</strong></p><h3>❓ 「业无变」是不许换工作吗？</h3><p><strong>讲的是别三天打鱼。</strong><br/><br/>① <strong>本业要踏实做，做出个样子</strong><br/>② <strong>不是不许改行，是改要有道理</strong><br/>③ <strong>频繁换、闹脾气就辞，最让父母悬心</strong><br/><br/><strong>记法：踏实比热闹要紧。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课四件事，今天就能做——</p><p>📖 晚上先做一件暖事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>给父母灌个热水袋、把被窝暖上</strong>；<strong>夏天就把凉席擦净、空调调到不直吹</strong>。</p><p>💡 早晚各一句话</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>早上「昨晚睡得好吗」，晚上「我回来了，您早点休息」</strong>；<strong>住得远，就发条消息</strong>。</p><p>🌱 出门回来说一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>去哪儿、几时回，先说一句</strong>；<strong>到家先进屋照个面</strong><br/><br/><strong>本课的落点：晨则省，昏则定。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第二段。记牢：<strong>冬则温，夏则凊</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>冬温夏凊 · 冷热先想到父母，黄香九岁温席。<strong>暖凉有人管</strong>。</p><p>晨省昏定 · 早问安、晚安顿，留个照面。<strong>早晚不断线</strong>。</p><p>出必告，反必面 · 出门说一声，回来照个面。<strong>行踪有交代</strong>。</p><p>居有常，业无变 · 作息有定准，本业踏实做。<strong>日子有常法</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第二段，讲照料与交代；下一课讲「事虽小，勿擅为」、「物虽小，勿私藏」。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「凊」怎么读、什么意思。② 说出黄香温席的故事。③ 今晚给父母做一件暖事，出门前说一声去哪儿。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「冬则温」的「温」指什么？', opts: ['让父母冬天不受冷', '天气温和', '态度温和'], ans: 0, exp: '暖被窝、暖屋子'},
  {q: '2. 「夏则凊」的「凊」是什么意思？', opts: ['凉，让父母不受热', '清静', '清爽的天气'], ans: 0, exp: '读 qìng'},
  {q: '3. 「温席」的故事讲的是谁？', opts: ['东汉黄香', '孔融', '司马光'], ans: 0, exp: '九岁温席'},
  {q: '4. 「晨则省」的「省」怎么读？', opts: ['xǐng，问候请安', 'shěng，节省', 'xǐng，反省自己'], ans: 0, exp: '问安'},
  {q: '5. 「昏则定」的「定」指什么？', opts: ['晚上把父母安顿好', '定下规矩', '天一黑就睡'], ans: 0, exp: '安顿父母'},
  {q: '6. 「出必告」的「告」是什么意思？', opts: ['出门前说一声去哪儿', '向老师告状', '报告成绩'], ans: 0, exp: '说一声'},
  {q: '7. 「反必面」的「反」同哪个字？', opts: ['返，回来', '反对', '反复'], ans: 0, exp: '回来了先照面'},
  {q: '8. 「居有常」的「居」指什么？', opts: ['住处、日常起居', '居住证件', '待在家里不出门'], ans: 0, exp: '作息有定准'},
  {q: '9. 「业无变」讲的是什么？', opts: ['本业踏实做，不轻易换来换去', '绝不许换工作', '事业永远不变'], ans: 0, exp: '别三天打鱼'},
  {q: '10. 这一段总的讲什么？', opts: ['照料冷暖、早晚问安、出入交代、生活有常', '怎么读书作文', '怎么与朋友相处'], ans: 0, exp: '让父母放心'},
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
s = s.replace('《弟子规》第二课', '《弟子规》第三课')
s = s.replace("window.GUOXUE_COURSE_ID = '542-ru-ze-xiao-fu-mu-hu';", "window.GUOXUE_COURSE_ID = '543-dong-wen-xia-qing';")
s = s.replace('yaoyue543', 'yaoyue544')

# ---- 校验 ----
for w in ['应勿缓', '行勿懒', '须敬听', '须顺承', '542-ru-ze-xiao-fu-mu-hu', 'yaoyue543', '第二课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
expect = {'slide': s.count('class="slide'), 'ruby': s.count('<ruby'), 'rt': s.count('<rt>'),
          'quiz': s.count("{q: '"), 'page_max': len(re.findall(r'data-page="', s))}
if expect['slide'] != 26 or expect['ruby'] != 24 or expect['rt'] != 24 or expect['quiz'] != 10 or expect['page_max'] != 24:
    print('[FAIL] 结构计数不符（slide 含 viewport/container 两个前缀，应为 24 页 + 2）:', expect)
    sys.exit(1)
print('[OK] 结构计数:', expect)
print('[OK] 章节锚点: 讲义区 %d→%d, 答疑区 %d→%d' % (i1, i2, j1, j2))

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(s)
print('[OK] 已生成', DST)
