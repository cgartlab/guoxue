#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build551: 以 550 课件为模板生成第 551 课《出则悌·称尊长，勿呼名》。
本课是「出则悌」一门第三段，讲对尊长的称呼、态度与见面礼。
讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（称呼、态度、见面）/ 3 称尊长勿呼名·对尊长勿见能 /
  4 路遇长疾趋揖·长无言退恭立 / 5 两句合看（敬在称呼与举动）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/550-zhang-zhe-xian/index.html"
DST = ROOT + "/lessons/551-cheng-zun-zhang/index.html"

TITLE = '出则悌 · 称尊长，勿呼名，对尊长，勿见能 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '称尊长，勿呼名；路遇长，疾趋揖 · 弟子规课堂'
DESC = ('《弟子规》第十一课，出则悌第三段。原文：「称尊长，勿呼名。对尊长，勿见能。'
        '路遇长，疾趋揖。长无言，退恭立。」讲见了长辈怎么办：称呼要带称呼，不直呼其名；'
        '在长辈面前不卖弄本事、不抢话显摆；路上遇见长辈，快步上前问好行礼；'
        '长辈没话说了，退到一旁恭敬站着。敬一个人，先从嘴上、再从身上看得出来。')
OG_DESC = '《弟子规》第十一课：称尊长勿呼名、对尊长勿见能、路遇长疾趋揖、长无言退恭立。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/551-cheng-zun-zhang/index.html'

ORIG = '称尊长，勿呼名。对尊长，勿见能。路遇长，疾趋揖。长无言，退恭立。'
ORIG_COMMA = '称尊长，勿呼名，对尊长，勿见能；路遇长，疾趋揖，长无言，退恭立。'
OLD_ORIG = '或饮食，或坐走。长者先，幼者后。长呼人，即代叫。人不在，己即到。'
OLD_ORIG_COMMA = '或饮食，或坐走，长者先，幼者后；长呼人，即代叫，人不在，己即到。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('称尊长勿呼名', ['chēng', 'zūn', 'zhǎng', 'wù', 'hū', 'míng'], True)
             + ju('对尊长勿见能', ['duì', 'zūn', 'zhǎng', 'wù', 'xiàn', 'néng'], False)
             + ju('路遇长疾趋揖', ['lù', 'yù', 'zhǎng', 'jí', 'qū', 'yī'], False)
             + ju('长无言退恭立', ['zhǎng', 'wú', 'yán', 'tuì', 'gōng', 'lì'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">勿呼名</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第三段：称尊长，勿呼名</p><p class="cover-desc">上一段讲先后次序，这一段讲见了长辈怎么办：怎么称呼、怎么说话、怎么行礼、怎么退开。敬一个人，先从嘴上看得出来，再从身上看得出来。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第三段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>称呼长辈，不要直呼他的名字。在长辈面前，不要卖弄自己的本事。路上遇见长辈，要快步上前问好行礼。长辈没有别的话说了，就退到一旁，恭恭敬敬地站着。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「尊长」指辈分高、年纪长的人；「勿」是不要；「见能」的「见」读 xiàn，同「现」，是显露、卖弄；「疾」是快；「趋」是快步上前；「揖」读 yī，是拱手行礼；「退」是退到一边。前四句讲嘴上的敬，后四句讲身上的敬。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 称呼、说话、见面</h2><p style="margin:0"><strong>先说嘴上的敬</strong><br/>① <strong>有称呼，不直呼其名</strong><br/>② <strong>不显摆，不抢长辈的话</strong><br/><br/><strong>一句话：嘴上有分寸。</strong></p><p><strong>再说身上的敬</strong><br/>① <strong>路上遇见，快步上前行礼</strong><br/>② <strong>长辈没话了，退到一旁站好</strong><br/><br/><strong>一句话：身上有规矩。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>敬不是嘴上说「我尊敬您」</strong><br/>② <strong>是喊什么、说什么、怎么站</strong><br/><br/><strong>一句话：敬要看得出来。</strong></p></div>
<!-- 4. 称尊长勿呼名·对尊长勿见能 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>称尊长，勿呼名；对尊长，勿见能</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>称：称呼；尊长：辈分高的长辈</strong><br/>② <strong>见能 xiàn néng：显摆本事</strong><br/><br/><strong>一句话：叫得对，才叫敬。</strong></p><p><strong>称尊长，勿呼名</strong><br/>① <strong>喊「王老师」「李爷爷」，不喊全名</strong><br/>② <strong>名字不是不能说，是不能当面直呼</strong><br/><br/><strong>一句话：一声称呼，一份敬。</strong></p><p><strong>对尊长，勿见能</strong><br/>① <strong>不在长辈面前卖弄、抢话、逞能</strong><br/>② <strong>长辈在说话，先听完，别急着表现自己</strong><br/><br/><strong>一句话：有本事，不用显。</strong></p></div>
<!-- 5. 路遇长疾趋揖·长无言退恭立 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>路遇长，疾趋揖；长无言，退恭立</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>疾：快；趋：快步上前；揖 yī：拱手行礼</strong><br/>② <strong>无言：没有别的话了；退：退到一旁；恭立：恭敬地站</strong><br/><br/><strong>一句话：见人要主动。</strong></p><p><strong>路遇长，疾趋揖</strong><br/>① <strong>看见长辈，主动上前问好，不要低头躲开</strong><br/>② <strong>古时作揖，今天点头、问好、鞠躬都一样</strong><br/><br/><strong>一句话：看见就上前。</strong></p><p><strong>长无言，退恭立</strong><br/>① <strong>话说完了，长辈没别的吩咐</strong><br/>② <strong>退到一旁站好，不插嘴、不扭头就走</strong><br/><br/><strong>一句话：进退都有礼。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 敬在嘴与身</h2><p style="margin:0"><strong>前四句讲「嘴」</strong><br/>① <strong>称呼到位，敬就有了开头</strong><br/>② <strong>不卖弄，敬才不假</strong><br/><br/><strong>一句话：话里带敬。</strong></p><p><strong>后四句讲「身」</strong><br/>① <strong>遇见就上前，是心里有他</strong><br/>② <strong>退得稳，是知道分寸</strong><br/><br/><strong>一句话：身上有礼。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>不必作揖磕头，问好、点头就够</strong><br/>② <strong>但主动、真诚这两样，一点不能省</strong><br/><br/><strong>一句话：礼可简，心不可减。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一组</h2><p style="margin:0"><strong>前四句：嘴上的敬</strong><br/>① <strong>称尊长，勿呼名——有称呼</strong><br/>② <strong>对尊长，勿见能——不显摆</strong><br/><br/><strong>一句话：叫得对，说得稳。</strong></p><p><strong>后四句：身上的敬</strong><br/>① <strong>路遇长，疾趋揖——主动上前</strong><br/>② <strong>长无言，退恭立——退得恭敬</strong><br/><br/><strong>一句话：来得快，退得稳。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>叫声老师，不喊全名</strong><br/>② <strong>见了就上前，说完再退开</strong><br/><br/><strong>一句话：敬，做出来才算。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>称呼不喊名，不卖弄；见了上前，说完退开。</p><p>📖 嘴与身</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>敬要看得见——在嘴上、在身上、在进退上。</p><p>💡 敬要看得见</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 称尊长，勿呼名</p>
<p>这是「弟子规课堂」第十一课：出则悌第三段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「勿呼名」是不是连名字都不能说？</h3><p><strong>不是不能说，是不能当面直呼。</strong><br/><br/>① <strong>当面喊「王老师」「李爷爷」，是敬</strong><br/>② <strong>跟别人介绍、写在本子上，照实说无妨</strong><br/>③ <strong>记法：称呼在前，名字在后。</strong></p><h3>❓ 现在见面还作揖吗？</h3><p><strong>不作揖了，但那份主动不能少。</strong><br/><br/>① <strong>问一声「老师好」、点个头，就够</strong><br/>② <strong>重点是「疾趋」：看见就上前，别低头躲开</strong><br/>③ <strong>记法：形式可改，主动不能改。</strong></p><h3>❓ 「勿见能」是什么意思？</h3><p><strong>有本事，不用急着给人看。</strong><br/><br/>① <strong>长辈说话，先听完，别抢话</strong><br/>② <strong>会做也别抢着显摆，做出来自然有人看见</strong><br/>③ <strong>记法：藏得住，才叫稳。</strong></p><h3>❓ 长辈不说话，我要一直站着吗？</h3><p><strong>是「没别的话了」，不是罚站。</strong><br/><br/>① <strong>长辈没别的吩咐，就退到一旁站好</strong><br/>② <strong>长辈在忙，安静退开，也是懂分寸</strong><br/>③ <strong>记法：该站就站，该退就退。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 见面先喊一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>见老师喊「老师好」，见邻居喊「爷爷好」「阿姨好」</strong>；<strong>不喊名字，喊称呼</strong>。</p><p>💡 长辈说话先听完</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>大人说话时不插嘴、不抢着表演</strong>；<strong>等他说完，你再说</strong>。</p><p>🌱 走的时候说一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>离开时说「我先走了，再见」</strong>；<strong>不扭头就跑，这就是「退恭立」</strong><br/><br/><strong>本课的落点：称尊长，勿呼名。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第三段。记牢：<strong>称尊长，勿呼名</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>称呼、说话、见面 · 嘴上的敬、身上的敬。<strong>敬要看得出来</strong>。</p><p>称尊长，勿呼名 · 喊称呼，不喊全名。<strong>一声称呼一份敬</strong>。</p><p>对尊长，勿见能 · 不卖弄、不抢话。<strong>有本事不用显</strong>。</p><p>路遇长，疾趋揖 · 看见就上前问好。<strong>别低头躲开</strong>。</p><p>长无言，退恭立 · 没话了退到一旁站好。<strong>进退都有礼</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第三段；上一课讲先后次序，这一课讲怎么称呼、怎么行礼。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「勿见能」的「见」读什么音。② 今天见老师，主动喊一声问好。③ 长辈说话时，完整听完一次不插嘴。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「勿见能」的「见」怎么读？', opts: ['xiàn，显露、卖弄', 'jiàn，看见', 'jiàn，见面'], ans: 0, exp: '见同现，读 xiàn'},
  {q: '2. 「称尊长」的「称」是什么意思？', opts: ['称呼', '称重', '称赞'], ans: 0, exp: '称是称呼'},
  {q: '3. 「勿呼名」的「呼名」是什么意思？', opts: ['直呼其名', '喊他起床', '记住名字'], ans: 0, exp: '不直呼其名'},
  {q: '4. 「对尊长，勿见能」是什么意思？', opts: ['不要在人前卖弄本事', '不要给长辈表演', '不要帮长辈做事'], ans: 0, exp: '不显摆、不逞能'},
  {q: '5. 「路遇长」的「遇」是什么意思？', opts: ['遇见、碰上', '待遇', '遭遇'], ans: 0, exp: '遇是碰到'},
  {q: '6. 「疾趋揖」的「疾」是什么意思？', opts: ['快、快步', '生病', '着急'], ans: 0, exp: '疾是快'},
  {q: '7. 「疾趋揖」的「揖」是什么动作？', opts: ['拱手行礼', '跪下磕头', '握手问好'], ans: 0, exp: '揖读 yī'},
  {q: '8. 「长无言，退恭立」该怎么做？', opts: ['长辈没话了，退到一旁恭敬站着', '长辈不说话就快走', '站着一直不动'], ans: 0, exp: '进退都有礼'},
  {q: '9. 路上遇见老师，怎么做最合适？', opts: ['主动上前问好', '低头快走避开', '等老师先开口'], ans: 0, exp: '疾趋揖'},
  {q: '10. 这一段总的讲什么？', opts: ['对长辈的称呼、态度和见面礼', '怎么记住长辈名字', '怎么给长辈表演'], ans: 0, exp: '嘴与身的敬'},
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
s = s.replace('《弟子规》第十课', '《弟子规》第十一课')
s = s.replace("window.GUOXUE_COURSE_ID = '550-zhang-zhe-xian';", "window.GUOXUE_COURSE_ID = '551-cheng-zun-zhang';")
s = s.replace('yaoyue551', 'yaoyue552')

# ---- 校验 ----
for w in ['长者先', '幼者后', '或饮食', '或坐走', '长呼人', '即代叫', '人在不在',
          '出则悌第二段', '550-zhang-zhe-xian', 'yaoyue551', '第十课']:
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
