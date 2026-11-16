#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build552: 以 551 课件为模板生成第 552 课《出则悌·骑下马，乘下车》。
「出则悌」第四段，讲一路上的礼：下车、等远、长者立幼勿坐、命乃坐。
讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（下、等、立、坐）/ 3 骑下马乘下车·过犹待百步余 /
  4 长者立幼勿坐·长者坐命乃坐 / 5 两句合看（路上与座前）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/551-cheng-zun-zhang/index.html"
DST = ROOT + "/lessons/552-qi-xia-ma/index.html"

TITLE = '出则悌 · 骑下马，乘下车，过犹待，百步余 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '骑下马，乘下车；过犹待，百步余 · 弟子规课堂'
DESC = ('《弟子规》第十二课，出则悌第四段。原文：「骑下马，乘下车。过犹待，百步余。'
        '长者立，幼勿坐。长者坐，命乃坐。」讲一路上的规矩：路上遇见长辈，骑马要下马、'
        '坐车要下车；长辈走过去了，还要站着等，等走远了再走；长辈站着，年纪小的不要先坐；'
        '长辈坐下了、让你坐，你才坐。敬，就藏在「让先」和「等候」里。')
OG_DESC = '《弟子规》第十二课：骑下马乘下车、过犹待百步余、长者立幼勿坐、长者坐命乃坐。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/552-qi-xia-ma/index.html'

ORIG = '骑下马，乘下车。过犹待，百步余。长者立，幼勿坐。长者坐，命乃坐。'
ORIG_COMMA = '骑下马，乘下车；过犹待，百步余；长者立，幼勿坐；长者坐，命乃坐。'
OLD_ORIG = '称尊长，勿呼名。对尊长，勿见能。路遇长，疾趋揖。长无言，退恭立。'
OLD_ORIG_COMMA = '称尊长，勿呼名，对尊长，勿见能；路遇长，疾趋揖，长无言，退恭立。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('骑下马乘下车', ['qí', 'xià', 'mǎ', 'chéng', 'xià', 'chē'], True)
             + ju('过犹待百步余', ['guò', 'yóu', 'dài', 'bǎi', 'bù', 'yú'], False)
             + ju('长者立幼勿坐', ['zhǎng', 'zhě', 'lì', 'yòu', 'wù', 'zuò'], False)
             + ju('长者坐命乃坐', ['zhǎng', 'zhě', 'zuò', 'mìng', 'nǎi', 'zuò'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">百步余</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第四段：骑下马，乘下车</p><p class="cover-desc">上一段讲见了长辈怎么喊、怎么退，这一段讲一路上的规矩：坐在车上看见长辈要下来；长辈走过去了，还要站着等；长辈站着，你别先坐；长辈让你坐，你再坐。敬，就藏在「让先」和「等候」里。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第四段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>路上遇见长辈，骑马的要下马，坐车的要下车。长辈走过去了，还要站着等，等长辈走远了再走。长辈站着的时候，年纪小的不要先坐下。长辈坐下了，让你坐，你才坐。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「骑」读 qí，是骑马；「乘」读 chéng，是坐车，不读 shèng；「犹」是还、仍然；「待」是等；「余」是多出来的；「百步余」就是一百多步，形容走得远了，不是让你数着步子；「命」是吩咐、让你；「乃」是才。前四句讲路上相遇，后四句讲一处坐下。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 下、等、立、坐</h2><p style="margin:0"><strong>先讲路上</strong><br/>① <strong>见了长辈，先下来</strong><br/>② <strong>长辈过去了，还站着等</strong><br/><br/><strong>一句话：路上不抢。</strong></p><p><strong>再讲座前</strong><br/>① <strong>长辈站着，我不坐</strong><br/>② <strong>让我坐，我再坐</strong><br/><br/><strong>一句话：座上有让。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>敬不是喊一句「我尊敬您」</strong><br/>② <strong>是肯停下、肯多等一会</strong><br/><br/><strong>一句话：慢半拍，就是敬。</strong></p></div>
<!-- 4. 骑下马乘下车·过犹待百步余 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>骑下马，乘下车；过犹待，百步余</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>骑 qí：骑马；乘 chéng：坐车</strong><br/>② <strong>犹：还；待：等；余：多出来的</strong><br/><br/><strong>一句话：认准读音，才懂礼。</strong></p><p><strong>骑下马，乘下车</strong><br/>① <strong>路上遇见长辈，先下来，站定了再问好</strong><br/>② <strong>不下来就问，人还在车上，话就轻了</strong><br/><br/><strong>一句话：下来，才叫见。</strong></p><p><strong>过犹待，百步余</strong><br/>① <strong>长辈过去了，还站着看</strong><br/>② <strong>等走远了再走，不必数步子</strong><br/><br/><strong>一句话：走远了，我才走。</strong></p></div>
<!-- 5. 长者立幼勿坐·长者坐命乃坐 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>长者立，幼勿坐；长者坐，命乃坐</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>立：站着；幼：年纪小的</strong><br/>② <strong>命：吩咐、让你；乃：才</strong><br/><br/><strong>一句话：一个「命」字，就是让。</strong></p><p><strong>长者立，幼勿坐</strong><br/>① <strong>长辈站着，你先坐下了，像什么话</strong><br/>② <strong>屋里、车上、饭桌前，都一个理</strong><br/><br/><strong>一句话：他不坐，我不坐。</strong></p><p><strong>长者坐，命乃坐</strong><br/>① <strong>长辈坐下了，让你坐，你再坐</strong><br/>② <strong>让你坐就坐，不必推来推去</strong><br/><br/><strong>一句话：让坐就坐。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 路上与座前</h2><p style="margin:0"><strong>前四句讲「路上」</strong><br/>① <strong>见了就下来，是心里有他</strong><br/>② <strong>走远了才走，是心里还挂着</strong><br/><br/><strong>一句话：路上有礼。</strong></p><p><strong>后四句讲「座前」</strong><br/>① <strong>长辈站着我不坐</strong><br/>② <strong>让我坐我才坐</strong><br/><br/><strong>一句话：座上有让。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>骑车、坐车、戴耳机，见长辈都先停下</strong><br/>② <strong>门、电梯、饭桌，都让长辈先</strong><br/><br/><strong>一句话：礼可改，先后不能改。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：一路上的敬</strong><br/>① <strong>骑下马，乘下车——先下来</strong><br/>② <strong>过犹待，百步余——走远再走</strong><br/><br/><strong>一句话：下得早，等得久。</strong></p><p><strong>后四句：一座之间的敬</strong><br/>① <strong>长者立，幼勿坐——我不先坐</strong><br/>② <strong>长者坐，命乃坐——让坐才坐</strong><br/><br/><strong>一句话：站得等，坐得让。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>见了下车站一站</strong><br/>② <strong>长辈没坐我不坐</strong><br/><br/><strong>一句话：先后让出来，就是敬。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>见长辈先下来，走远才走；他没坐我不坐。</p><p>📖 先下与后坐</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>敬就是让先、就是肯等。</p><p>💡 让先与等候</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 骑下马，乘下车</p>
<p>这是「弟子规课堂」第十二课：出则悌第四段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 现在不骑马、不坐马车了，这条还有用吗？</h3><p><strong>有用，换成今天的样子就是了。</strong><br/><br/>① <strong>骑自行车、坐电动车，见了长辈先停下</strong><br/>② <strong>走路戴着耳机，也要摘下耳机、站好再问好</strong><br/>③ <strong>记法：先停下，就是今天的「下车」。</strong></p><h3>❓ 「百步余」要数着一百步吗？</h3><p><strong>不是数步子，是形容走得远了。</strong><br/><br/>① <strong>长辈走过去、走远、看不见了，你再走</strong><br/>② <strong>不是站着发呆，是目送—看着人走远</strong><br/>③ <strong>记法：人走远了，我才走。</strong></p><h3>❓ 长辈让我坐，我推辞是不是更有礼？</h3><p><strong>让坐就坐，推来推去反而添乱。</strong><br/><br/>① <strong>长辈站着时你站着，这叫「幼勿坐」</strong><br/>② <strong>长辈坐下了、让你坐，你坐下才对</strong><br/>③ <strong>记法：该站就站，该坐就坐。</strong></p><h3>❓ 公交地铁上要给长辈让座吗？</h3><p><strong>要，跟「长者立，幼勿坐」一个道理。</strong><br/><br/>① <strong>看见长辈站着，起身让一让</strong><br/>② <strong>自己不舒服、腿上有伤，说一声，别硬撑</strong><br/>③ <strong>记法：能站就站，让座不丢人。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 见了长辈先停下</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>骑车的下车、坐车的下车、走路的站住</strong>；<strong>摘下耳机，问一声好，这就是「骑下马，乘下车」</strong>。</p><p>💡 让长辈先走先坐</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>进门让长辈先进，电梯让长辈先上先下</strong>；<strong>饭桌上长辈没坐，你先不坐</strong>。</p><p>🌱 走的时候等一等</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>长辈走远了再走，目送到看不见</strong>；<strong>这就是「过犹待，百步余」</strong><br/><br/><strong>本课的落点：骑下马，乘下车。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第四段。记牢：<strong>骑下马，乘下车</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>下、等、立、坐 · 路上不抢，座上有让。<strong>慢半拍就是敬</strong>。</p><p>骑下马，乘下车 · 见了长辈先下来。<strong>停下再问好</strong>。</p><p>过犹待，百步余 · 等长辈走远再走。<strong>目送到看不见</strong>。</p><p>长者立，幼勿坐 · 长辈站着我不坐。<strong>他不坐我不坐</strong>。</p><p>长者坐，命乃坐 · 长辈让你坐再坐。<strong>让坐就坐</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第四段；上一课讲怎么称呼、怎么退，这一课讲路上遇见和一处坐下。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「乘下车」的「乘」读什么音。② 今天见长辈，先停下再问好。③ 和长辈同坐，等长辈先坐。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「骑下马」的「骑」怎么读？', opts: ['qí，骑马', 'jì，骑兵', 'qì，坐骑'], ans: 0, exp: '骑读 qí'},
  {q: '2. 「乘下车」的「乘」怎么读？', opts: ['chéng，坐车', 'shèng，车马', 'chèng，量词'], ans: 0, exp: '乘车读 chéng'},
  {q: '3. 「骑下马，乘下车」是什么意思？', opts: ['路上遇见长辈，骑马要下马、坐车要下车', '骑马要骑到马上，坐车要坐到车上', '下车以后再去骑马'], ans: 0, exp: '见了长辈先下来'},
  {q: '4. 「过犹待」的「犹」是什么意思？', opts: ['还、仍然', '犹豫', '好像'], ans: 0, exp: '犹是还'},
  {q: '5. 「百步余」是什么意思？', opts: ['一百多步，形容走得远了', '正好一百步', '一百步以内'], ans: 0, exp: '余是多出来的'},
  {q: '6. 「过犹待，百步余」该怎么做？', opts: ['长辈过去了还站着，等走远再走', '长辈一过去就快走', '跟着长辈一起走'], ans: 0, exp: '目送到走远'},
  {q: '7. 「长者立，幼勿坐」是什么意思？', opts: ['长辈站着，年纪小的不要先坐下', '长辈站着，小孩不能站着', '长辈站着要给他搬凳子'], ans: 0, exp: '他不坐我不坐'},
  {q: '8. 「命乃坐」的「命」是什么意思？', opts: ['吩咐、让', '性命', '命运'], ans: 0, exp: '命是吩咐'},
  {q: '9. 「长者坐，命乃坐」该怎么做？', opts: ['长辈坐下让你坐，你才坐', '长辈坐下你就坐', '长辈坐下你就走'], ans: 0, exp: '让坐就坐'},
  {q: '10. 这一段总的讲什么？', opts: ['路上遇见长辈和一处坐下的先后之礼', '怎么骑马坐车', '怎么给长辈搬椅子'], ans: 0, exp: '路上与座前的敬'},
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
s = s.replace('《弟子规》第十一课', '《弟子规》第十二课')
s = s.replace("window.GUOXUE_COURSE_ID = '551-cheng-zun-zhang';", "window.GUOXUE_COURSE_ID = '552-qi-xia-ma';")
s = s.replace('yaoyue552', 'yaoyue553')

# ---- 校验 ----
for w in ['称尊长', '勿呼名', '勿见能', '路遇长', '疾趋揖', '长无言', '退恭立',
          '出则悌第三段', '551-cheng-zun-zhang', 'yaoyue552', '第十一课']:
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
