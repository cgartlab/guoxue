#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build542: 以 541 课件为模板生成第 542 课《入则孝·父母呼应勿缓》。

弟子规课堂第二课，正文第一门「入则孝」开篇四句。讲义 8 页排布：
  0 封面 / 1 入则孝总说 / 2 父母呼应勿缓 / 3 父母命行勿懒 /
  4 父母教敬听·父母责顺承 / 5 原文 / 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。
区域替换法：讲义区整块换、答疑区整块换、QUIZ 数组整块换、头部 meta 正则换。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/541-dizigui-kaipian/index.html"
DST = ROOT + "/lessons/542-ru-ze-xiao-fu-mu-hu/index.html"

TITLE = '入则孝 · 父母呼，应勿缓，四句讲透 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '入则孝 · 父母呼，应勿缓，孩子对父母的四个回应 · 弟子规课堂'
DESC = ('《弟子规》第二课，进正文第一门「入则孝」。原文：「父母呼，应勿缓。父母命，行勿懒。'
        '父母教，须敬听。父母责，须顺承。」讲孩子对父母的四种回应——父母叫，马上应一声，'
        '别拖着（应勿缓）；父母交代事，赶紧去做，别偷懒（行勿懒）；父母讲道理，恭敬地听进去'
        '（须敬听）；父母责备，先把话接下来，别顶嘴（须顺承）。呼、命、教、责是父母那边做的，'
        '应、行、听、承是我这边该做的。这一门是全篇第一门，孝排在最先，因为孝是根。'
        '孝道不从大道理开始，从答应一声开始。')
OG_DESC = '《弟子规》第二课：入则孝开篇四句，呼与应、命与行、教与听、责与承，讲孩子对父母的四种回应。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/542-ru-ze-xiao-fu-mu-hu/index.html'

ORIG = '父母呼，应勿缓。父母命，行勿懒。父母教，须敬听。父母责，须顺承。'
ORIG_COMMA = '父母呼，应勿缓，父母命，行勿懒；父母教，须敬听，父母责，须顺承。'
OLD_ORIG = '弟子规，圣人训。首孝弟，次谨信。泛爱众，而亲仁。有余力，则学文。'
OLD_ORIG_COMMA = '弟子规，圣人训，首孝弟，次谨信；泛爱众，而亲仁，有余力，则学文。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('父母呼应勿缓', ['fù', 'mǔ', 'hū', 'yìng', 'wù', 'huǎn'], True)
             + ju('父母命行勿懒', ['fù', 'mǔ', 'mìng', 'xíng', 'wù', 'lǎn'], False)
             + ju('父母教须敬听', ['fù', 'mǔ', 'jiào', 'xū', 'jìng', 'tīng'], False)
             + ju('父母责须顺承', ['fù', 'mǔ', 'zé', 'xū', 'shùn', 'chéng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">入则孝</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》正文第一门：父母呼，应勿缓</p><p class="cover-desc">上一课认了书，这一课进正文。第一门叫「入则孝」——回到家里怎么待父母。开头四句最短，也最实在：父母叫你，你应不应声。孝道不从大道理起头，从这一声答应起头。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝开篇四句</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>父母叫你，马上应一声，别拖着；父母交代事情，赶紧去做，别偷懒；父母教导你，要恭恭敬敬地听；父母责备你，要先顺从地接受下来。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>这四句是「入则孝」的开头，讲的全是日常小事。总叙八句里「首孝弟」三个字，到这儿落到具体做法上。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 入则孝总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>入则孝 · 全篇第一门</h2><p style="margin:0"><strong>为什么排第一</strong><br/>① <strong>总叙说「首孝弟」，孝排在最前</strong><br/>② <strong>所以正文第一门就是入则孝</strong><br/><br/><strong>一句话：孝是根。</strong></p><p><strong>「入」是什么意思</strong><br/>① <strong>入：回到家里</strong><br/>② <strong>孝：好好待父母</strong><br/><br/><strong>一句话：在家对父母。</strong></p><p><strong>这一门管多宽</strong><br/>① <strong>从「父母呼」一直讲到身后祭祀</strong><br/>② <strong>生前奉养、生病侍候、去世守丧都在内</strong><br/><br/><strong>一句话：管一辈子。</strong></p></div>
<!-- 4. 父母呼应勿缓 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>父母呼，应勿缓</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>呼：叫；应：应一声</strong><br/>② <strong>缓：慢、拖着</strong><br/><br/><strong>一句话：叫你就应，别拖。</strong></p><p><strong>怎么做</strong><br/>① <strong>听见就答一声「来了」</strong><br/>② <strong>手里的活可以不停</strong><br/><br/><strong>一句话：先应声，再说事。</strong></p><p><strong>为什么急在这声</strong><br/>① <strong>应一声，父母心里就安了</strong><br/>② <strong>不应，父母就起身来找</strong><br/><br/><strong>一句话：一声就是安心。</strong></p></div>
<!-- 5. 父母命行勿懒 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>父母命，行勿懒</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>命：吩咐、交代；行：去做</strong><br/>② <strong>懒：拖着不办</strong><br/><br/><strong>一句话：交代了就去做。</strong></p><p><strong>怎么做</strong><br/>① <strong>记下来，马上去办</strong><br/>② <strong>办不了就说清，别应着不动</strong><br/><br/><strong>一句话：宁可说清，不可空应。</strong></p><p><strong>为什么懒不得</strong><br/>① <strong>答应了不做，比不答应更伤人</strong><br/>② <strong>懒两回，就不敢再托你</strong><br/><br/><strong>一句话：懒一次，失信一次。</strong></p></div>
<!-- 6. 父母教敬听 / 父母责顺承 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>父母教，须敬听；父母责，须顺承</h2><p style="margin:0"><strong>父母教，须敬听</strong><br/>① <strong>教：教导、指点</strong><br/>② <strong>须：一定要；敬听：恭敬地听</strong><br/><br/><strong>一句话：讲道理，要听进去。</strong></p><p><strong>父母责，须顺承</strong><br/>① <strong>责：责备</strong><br/>② <strong>顺承：先接下来，不顶嘴</strong><br/><br/><strong>一句话：挨说了，先受着。</strong></p><p><strong>两句合看</strong><br/>① <strong>教是讲道理，责是动了气</strong><br/>② <strong>一个要听进去，一个要先接住</strong><br/><br/><strong>一句话：都别顶嘴。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四个动作，四种回应</h2><p style="margin:0"><strong>前一对手：呼与应、命与行</strong><br/>① <strong>呼是叫你，应是答一声</strong><br/>② <strong>命是派事，行是动手去办</strong><br/><br/><strong>一句话：嘴要应，手要动。</strong></p><p><strong>后一对手：教与听、责与承</strong><br/>① <strong>教是讲道理，听是听进心里</strong><br/>② <strong>责是动了气，承是先接住</strong><br/><br/><strong>一句话：耳朵要开，脾气要收。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>不慢、不懒</strong><br/>② <strong>不驳、不顶</strong><br/><br/><strong>一句话：四句只讲一个「顺」字。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>父母叫、派、教、说，我这边应、做、听、受。</p><p>📖 全是小事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>小事上肯低头，大事上才立得住；连一声都懒得应，谈孝都是空的。</p><p>💡 孝在细处</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 从答应一声起</p>
<p>这是「弟子规课堂」第二课：进正文第一门。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 正在写作业，父母一叫也得马上应吗？</h3><p><strong>应一声不耽误事。</strong><br/><br/>① <strong>先答「来了」，手上的笔可以不停</strong><br/>② <strong>再说一句「这两分钟写完就过去」</strong><br/>③ <strong>最忌装没听见</strong><br/><br/><strong>记法：先应声，再说事。</strong></p><h3>❓ 父母说的不对，也要「敬听」吗？</h3><p><strong>敬听不是盲从。</strong><br/><br/>① <strong>先听完，别打断</strong><br/>② <strong>再有礼地说自己的想法</strong><br/>③ <strong>后文「亲有过，谏使更」专门讲怎么劝</strong><br/><br/><strong>记法：先听完，再说话。</strong></p><h3>❓ 被冤枉了，也要「顺承」吗？</h3><p><strong>先接态度，再讲事实。</strong><br/><br/>① <strong>当场顶嘴，只会把火拱得更大</strong><br/>② <strong>等气平了，再把经过说清楚</strong><br/>③ <strong>顺承不是认下没做的事</strong><br/><br/><strong>记法：不顶嘴，不等于认错。</strong></p><h3>❓ 孩子在外地，这四句还有用吗？</h3><p><strong>电话、视频就是「呼」与「应」。</strong><br/><br/>① <strong>父母来电尽量接，没接上回头就回</strong><br/>② <strong>交代的事办完，给个回话</strong><br/>③ <strong>一声回话，隔多远都管用</strong><br/><br/><strong>记法：隔千里，也应一声。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课全是能做的小事——</p><p>📖 听见就叫一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>父母叫你，第一声就答「来了」</strong>；<strong>别等叫到第二声、第三声</strong>。</p><p>💡 交代的事记一笔</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>写在纸上或手机备忘录里</strong>；<strong>办完回一句「办好了」</strong>。</p><p>🌱 被说的时候先听完</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不打断、不翻白眼</strong>；<strong>听完了，再讲自己的想法</strong><br/><br/><strong>本课的落点：父母呼，应勿缓。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天进正文第一门。记牢：<strong>父母呼，应勿缓</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>入则孝 · 全篇第一门，讲在家怎么待父母。<strong>孝是根</strong>。</p><p>父母呼，应勿缓 · 听见就应一声，别拖。<strong>先应声</strong>。</p><p>父母命，行勿懒 · 交代了就去做，别懒。<strong>答应了就办</strong>。</p><p>父母教敬听、父母责顺承 · 讲道理要听，责备先接。<strong>都别顶嘴</strong>。</p><p><strong>在全篇中的位置:</strong>「入则孝」第一段，讲日常的呼应；下一课讲冬温夏凊、晨省昏定。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「应勿缓」的「缓」是什么意思。② 说出父母做的四个动作、我该做的四个回应。③ 今天父母叫你时，第一声就应。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 《弟子规》正文第一门是什么？', opts: ['入则孝', '出则弟', '余力学文'], ans: 0, exp: '总叙说首孝弟'},
  {q: '2. 「入则孝」的「入」是什么意思？', opts: ['回到家里', '进入学堂', '收入'], ans: 0, exp: '在家对父母'},
  {q: '3. 「父母呼，应勿缓」的「应」是什么意思？', opts: ['答应、应一声', '应该', '应付'], ans: 0, exp: '听见就应'},
  {q: '4. 「应勿缓」的「缓」是什么意思？', opts: ['慢、拖着', '缓和', '缓缓走'], ans: 0, exp: '别拖延'},
  {q: '5. 「父母命，行勿懒」的「命」指什么？', opts: ['吩咐、交代', '性命', '命运'], ans: 0, exp: '派你做事'},
  {q: '6. 「行勿懒」的「行」是什么意思？', opts: ['去做、动手', '走路', '品行'], ans: 0, exp: '赶紧去办'},
  {q: '7. 「须敬听」的「敬」是什么态度？', opts: ['恭敬、认真', '害怕', '随便听听'], ans: 0, exp: '恭敬地听'},
  {q: '8. 「须顺承」的「顺承」是什么意思？', opts: ['先顺从接受，不顶嘴', '顺着路走', '承担家务'], ans: 0, exp: '先接下来'},
  {q: '9. 这四句里的四个回应是哪些？', opts: ['应、行、听、承', '呼、命、教、责', '读、写、背、算'], ans: 0, exp: '父母那边是呼命教责'},
  {q: '10. 学这四句，最先该做到的哪一件？', opts: ['父母叫时第一声就应', '先背熟 1080 字', '先学会讲道理'], ans: 0, exp: '从一声答应起'},
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
s = s.replace('《弟子规》第一课', '《弟子规》第二课')
s = s.replace("window.GUOXUE_COURSE_ID = '541-dizigui-kaipian';", "window.GUOXUE_COURSE_ID = '542-ru-ze-xiao-fu-mu-hu';")
s = s.replace('yaoyue542', 'yaoyue543')

# ---- 校验 ----
for w in ['弟子规，圣人训', '李毓秀', '贾存仁', '训蒙文', '541-dizigui-kaipian', 'yaoyue542', '第一课']:
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
