#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build544: 以 543 课件为模板生成第 544 课《入则孝·事虽小勿擅为》。

讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（两个「小」）/ 3 事虽小勿擅为 / 4 物虽小勿私藏 /
  5 两句合看（擅与私，都是瞒着）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。
区域替换法：讲义区整块换、答疑区整块换、QUIZ 数组整块换、头部 meta 正则换。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/543-dong-wen-xia-qing/index.html"
DST = ROOT + "/lessons/544-shi-sui-xiao/index.html"

TITLE = '入则孝 · 事虽小，勿擅为，小处见心 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '事虽小，勿擅为；物虽小，勿私藏 · 弟子规课堂'
DESC = ('《弟子规》第四课，入则孝第三段。原文：「事虽小，勿擅为。苟擅为，子道亏。'
        '物虽小，勿私藏。苟私藏，亲心伤。」讲两个「小」——事再小，也别自作主张；'
        '东西再小，也别偷偷藏起来不说。前两句说「擅」，自作主张会让做子女的本分缺一块；'
        '后两句说「私」，瞒着父母，父母伤心的不是那件东西，是你不肯说。'
        '两句合起来一个意思：不让父母知道的事，越小越要小心。')
OG_DESC = '《弟子规》第四课：事虽小勿擅为、物虽小勿私藏——小事不擅作主张，东西不瞒着父母。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/544-shi-sui-xiao/index.html'

ORIG = '事虽小，勿擅为。苟擅为，子道亏。物虽小，勿私藏。苟私藏，亲心伤。'
ORIG_COMMA = '事虽小，勿擅为，苟擅为，子道亏；物虽小，勿私藏，苟私藏，亲心伤。'
OLD_ORIG = '冬则温，夏则凊。晨则省，昏则定。出必告，反必面。居有常，业无变。'
OLD_ORIG_COMMA = '冬则温，夏则凊，晨则省，昏则定；出必告，反必面，居有常，业无变。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('事虽小勿擅为', ['shì', 'suī', 'xiǎo', 'wù', 'shàn', 'wéi'], True)
             + ju('苟擅为子道亏', ['gǒu', 'shàn', 'wéi', 'zǐ', 'dào', 'kuī'], False)
             + ju('物虽小勿私藏', ['wù', 'suī', 'xiǎo', 'wù', 'sī', 'cáng'], False)
             + ju('苟私藏亲心伤', ['gǒu', 'sī', 'cáng', 'qīn', 'xīn', 'shāng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">勿擅为</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第三段：事虽小，勿擅为</p><p class="cover-desc">上一段讲照料父母，这一段讲管住自己。四句里反复出现一个「小」字：事小、物小。人最容易在小处松手，也最容易在小处让父母伤心。这一课就讲这两个「小」。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第三段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>事情再小，也不要自作主张；如果自作主张，做子女的本分就缺了一块。东西再小，也不要偷偷藏起来；如果偷偷藏起来，父母的心就伤了。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「擅」是自作主张，「苟」是如果，「子道」是做子女的道理，「亏」是缺、亏损。四句两两成对：前一对说「擅」，后一对说「私」。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 两个「小」字</h2><p style="margin:0"><strong>「虽小」出现两次</strong><br/>① <strong>事虽小：事情不大</strong><br/>② <strong>物虽小：东西不值钱</strong><br/><br/><strong>一句话：都拿「小」来说事。</strong></p><p><strong>小处最容易松手</strong><br/>① <strong>大事人人小心，小事随手就做了</strong><br/>② <strong>坏习惯都是从「这点小事」开始的</strong><br/><br/><strong>一句话：小处才见真章。</strong></p><p><strong>这一课说两件事</strong><br/>① <strong>做事别自作主张</strong><br/>② <strong>东西别瞒着父母</strong><br/><br/><strong>一句话：别让父母靠猜。</strong></p></div>
<!-- 4. 事虽小勿擅为 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>事虽小，勿擅为；苟擅为，子道亏</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>擅：自作主张；亏：缺了一块</strong><br/>② <strong>苟：如果；子道：做子女的道理</strong><br/><br/><strong>一句话：擅自做主，本分就缺。</strong></p><p><strong>什么叫擅为</strong><br/>① <strong>父母不在，擅自翻人家的东西</strong><br/>② <strong>没问过，就替家里答应别人的事</strong><br/><br/><strong>一句话：不问就做，就是擅。</strong></p><p><strong>为什么小事更要问</strong><br/>① <strong>小事不问成了习惯，大事更不会商量</strong><br/>② <strong>问一句，是尊重，不是没主见</strong><br/><br/><strong>一句话：会商量，才算长大。</strong></p></div>
<!-- 5. 物虽小勿私藏 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>物虽小，勿私藏；苟私藏，亲心伤</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>物：东西；亲：父母</strong><br/>② <strong>私藏：偷偷收起来不说</strong><br/><br/><strong>一句话：藏起来，父母就伤心。</strong></p><p><strong>什么叫私藏</strong><br/>① <strong>捡到东西，不说，自己收着</strong><br/>② <strong>成绩单、通知单，压在书包底</strong><br/><br/><strong>一句话：不说的东西，就是藏。</strong></p><p><strong>父母伤的是什么</strong><br/>① <strong>不是那件东西值多少钱</strong><br/>② <strong>是你有事不肯跟他说</strong><br/><br/><strong>一句话：伤心在「你不说」。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 擅与私</h2><p style="margin:0"><strong>一个「擅」，一个「私」</strong><br/>① <strong>擅：不问就做</strong><br/>② <strong>私：不说就藏</strong><br/><br/><strong>一句话：都是瞒着父母。</strong></p><p><strong>后果不一样</strong><br/>① <strong>擅为亏的是「子道」，缺的是本分</strong><br/>② <strong>私藏伤的是「亲心」，疼的是父母</strong><br/><br/><strong>一句话：一个亏己，一个伤人。</strong></p><p><strong>补救只有一条路</strong><br/>① <strong>做了就说，别瞒着</strong><br/>② <strong>越瞒越难开口，越早说越轻</strong><br/><br/><strong>一句话：说出来，事就小了。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一串</h2><p style="margin:0"><strong>前两句：管「做」</strong><br/>① <strong>事虽小，勿擅为——不问不做</strong><br/>② <strong>苟擅为，子道亏——做了就亏本分</strong><br/><br/><strong>一句话：先问一句再动手。</strong></p><p><strong>后两句：管「藏」</strong><br/>① <strong>物虽小，勿私藏——不收着不说</strong><br/>② <strong>苟私藏，亲心伤——藏了就伤父母心</strong><br/><br/><strong>一句话：有话摆到桌面上。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>不问不做，不藏不说</strong><br/>② <strong>做了就说，藏了就补</strong><br/><br/><strong>一句话：别让父母靠猜。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>小事别自作主张，小东西别偷偷藏着。</p><p>📖 都在说小事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>孝不孝，先看有没有事瞒着父母；肯说、肯问，就是敬。</p><p>💡 小处见心</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 不瞒、不擅</p>
<p>这是「弟子规课堂」第四课：入则孝第三段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 小事也要问，是不是太啰嗦？</h3><p><strong>问的是「该不该」，不是「能不能」。</strong><br/><br/>① <strong>花钱、答应别人、动家里的东西，先问</strong><br/>② <strong>自己的功课、穿衣吃饭，说一声就行</strong><br/>③ <strong>界线看两条：影响不影响别人，让不让父母悬心</strong><br/><br/><strong>记法：怕父母担心的先问。</strong></p><h3>❓ 家里的东西，藏起来也算私藏？</h3><p><strong>私藏说的是「瞒着」。</strong><br/><br/>① <strong>拿家里的钱不吭声</strong><br/>② <strong>收了别人的东西不说</strong><br/>③ <strong>考砸了把卷子藏进抽屉</strong><br/><br/><strong>记法：瞒着才是藏。</strong></p><h3>❓ 已经擅自做了，怎么办？</h3><p><strong>赶紧说，别瞒。</strong><br/><br/>① <strong>如实说清做了什么、后果怎样</strong><br/>② <strong>该认的认，该补的补</strong><br/>③ <strong>瞒下去，小事才变大事</strong><br/><br/><strong>记法：早说早轻。</strong></p><h3>❓ 「子道亏」的「亏」是吃亏吗？</h3><p><strong>是亏损、缺了一块。</strong><br/><br/>① <strong>不是钱上吃亏</strong><br/>② <strong>是做子女的本分缺了一角</strong><br/>③ <strong>补回来只能靠以后不擅为</strong><br/><br/><strong>记法：亏的是本分。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练两样本事——</p><p>📖 动手前先问一句</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>动家里的东西、答应别人的事，先说一声</strong>；<strong>问一句不丢人，是尊重</strong>。</p><p>💡 有事当天就说</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>考砸了、丢了东西、跟同学闹了别扭</strong>；<strong>当天说出来，父母才帮得上</strong>。</p><p>🌱 收着的东西交出来</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>捡到的东西交老师或交父母</strong>；<strong>压着没说的单子，今天摊开</strong><br/><br/><strong>本课的落点：事虽小，勿擅为。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第三段。记牢：<strong>事虽小，勿擅为</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>两个「小」 · 事小、物小，小处最容易松手。<strong>小处见真章</strong>。</p><p>事虽小，勿擅为 · 不问就做，本分缺一块。<strong>先问再做</strong>。</p><p>物虽小，勿私藏 · 偷偷藏着，父母伤心在「你不说」。<strong>别瞒着</strong>。</p><p>擅与私 · 一个亏己，一个伤人，补救都是「说出来」。<strong>早说早轻</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第三段，讲管住自己；下一课讲「亲所好，力为具」、「身有伤，贻亲忧」。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「擅」和「苟」是什么意思。② 举一个「私藏」的例子。③ 今天有一件事瞒着父母吗？说出来。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「事虽小，勿擅为」的「擅」是什么意思？', opts: ['自作主张', '擅长做某事', '擅自离开'], ans: 0, exp: '不问就做'},
  {q: '2. 「勿擅为」的「为」怎么读？', opts: ['wéi，做', 'wèi，为了', 'wéi，成为'], ans: 0, exp: '为是做'},
  {q: '3. 「苟擅为」的「苟」是什么意思？', opts: ['如果', '苟且偷安', '随便应付'], ans: 0, exp: '苟是如果'},
  {q: '4. 「子道亏」的「亏」是什么意思？', opts: ['亏损、缺了一块', '钱上吃亏', '亏欠别人'], ans: 0, exp: '本分缺一角'},
  {q: '5. 「勿私藏」的「私藏」是什么意思？', opts: ['偷偷收起来不说', '私人收藏爱好', '藏在自己家里'], ans: 0, exp: '瞒着才是藏'},
  {q: '6. 「亲心伤」的「亲」指谁？', opts: ['父母', '亲戚', '亲近的朋友'], ans: 0, exp: '亲指父母'},
  {q: '7. 父母最伤心的是什么？', opts: ['你有事不肯跟他说', '东西丢了', '东西不值钱'], ans: 0, exp: '伤心在你不说'},
  {q: '8. 四句里两次说「虽小」，是想说明什么？', opts: ['事小也不能自作主张、不能瞒', '小事根本不用管', '小东西不值钱，随便处置'], ans: 0, exp: '小处见真章'},
  {q: '9. 已经擅自做了事，最好的补救是什么？', opts: ['赶紧如实说明，该补的补', '瞒到底，别让人知道', '假装没发生过'], ans: 0, exp: '早说早轻'},
  {q: '10. 这一段总的讲什么？', opts: ['小事不擅作主张，东西不瞒着父母', '怎么读书作文', '怎么与兄弟相处'], ans: 0, exp: '不擅、不私'},
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
s = s.replace('《弟子规》第三课', '《弟子规》第四课')
s = s.replace("window.GUOXUE_COURSE_ID = '543-dong-wen-xia-qing';", "window.GUOXUE_COURSE_ID = '544-shi-sui-xiao';")
s = s.replace('yaoyue544', 'yaoyue545')

# ---- 校验 ----
for w in ['冬则温', '夏则凊', '晨则省', '昏则定', '黄香', '543-dong-wen-xia-qing', 'yaoyue544', '第三课']:
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
