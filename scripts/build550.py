#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build550: 以 549 课件为模板生成第 550 课《出则悌·或饮食，或坐走》。
本课是「出则悌」一门第二段，讲长幼先后与应对传话。
讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（长幼之序）/ 3 或饮食或坐走·长者先幼者后 /
  4 长呼人即代叫·人不在己即到 / 5 两句合看（让与应）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/549-xiong-dao-you/index.html"
DST = ROOT + "/lessons/550-zhang-zhe-xian/index.html"

TITLE = '出则悌 · 或饮食，或坐走，长者先，幼者后 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '长者先，幼者后；长呼人，即代叫 · 弟子规课堂'
DESC = ('《弟子规》第十课，出则悌第二段。原文：「或饮食，或坐走。长者先，幼者后。'
        '长呼人，即代叫。人不在，己即到。」讲日常起居里的长幼之序：吃饭、坐下、走路，'
        '先请长辈，自己跟在后面；长辈要叫谁，听见了就帮着传话；要找的人不在，'
        '就自己过去回一声、问一句能不能帮忙。礼仪不在大场面，就在一顿饭、一步路、一句应答里。')
OG_DESC = '《弟子规》第十课：或饮食或坐走、长者先幼者后、长呼人即代叫、人不在己即到——长幼之序。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/550-zhang-zhe-xian/index.html'

ORIG = '或饮食，或坐走。长者先，幼者后。长呼人，即代叫。人不在，己即到。'
ORIG_COMMA = '或饮食，或坐走，长者先，幼者后；长呼人，即代叫，人不在，己即到。'
OLD_ORIG = '兄道友，弟道恭。兄弟睦，孝在中。财物轻，怨何生。言语忍，忿自泯。'
OLD_ORIG_COMMA = '兄道友，弟道恭，兄弟睦，孝在中；财物轻，怨何生，言语忍，忿自泯。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('或饮食或坐走', ['huò', 'yǐn', 'shí', 'huò', 'zuò', 'zǒu'], True)
             + ju('长者先幼者后', ['zhǎng', 'zhě', 'xiān', 'yòu', 'zhě', 'hòu'], False)
             + ju('长呼人即代叫', ['zhǎng', 'hū', 'rén', 'jí', 'dài', 'jiào'], False)
             + ju('人不在己即到', ['rén', 'bù', 'zài', 'jǐ', 'jí', 'dào'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">长者先</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第二段：或饮食，或坐走</p><p class="cover-desc">上一段讲兄弟姐妹之间的爱与敬，这一段讲长幼之间的先与后。吃饭、坐下、走路，先请长辈；长辈叫你，快点答应；人不在，自己过去回一声。礼就藏在这些小事里。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第二段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>或是吃饭喝水，或是坐下起身、走路，都要请长辈在先，年幼的在后。长辈要叫某个人，听见了就赶紧帮着去叫。要是要找的人不在，自己就先过去回话，问问能帮什么。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「或」是有时、或是；「长者」读 zhǎng zhě，指年纪大、辈分高的人；「幼」是年纪小的；「呼」是叫、喊；「代」是代替、帮着；「即」是马上；「己」是自己。前四句讲先后次序，后四句讲听见呼唤怎么应对。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 长幼之序</h2><p style="margin:0"><strong>上一段与这一段</strong><br/>① <strong>上一段：兄弟之间，讲爱与敬</strong><br/>② <strong>这一段：长幼之间，讲先与后</strong><br/><br/><strong>一句话：同辈讲和，长幼讲序。</strong></p><p><strong>这一段分两层</strong><br/>① <strong>走在前面的事：吃、坐、走，让长辈先</strong><br/>② <strong>听见呼唤的事：代叫、回话、跟到</strong><br/><br/><strong>一句话：一层是让，一层是应。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>让，是把方便先给别人</strong><br/>② <strong>应，是让别人找得到你</strong><br/><br/><strong>一句话：有礼，就是让人安心。</strong></p></div>
<!-- 4. 或饮食或坐走·长者先幼者后 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>或饮食，或坐走；长者先，幼者后</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>或：有时、或是；长者 zhǎng zhě：长辈</strong><br/>② <strong>幼：年纪小的；先、后：次序</strong><br/><br/><strong>一句话：小事先让长辈。</strong></p><p><strong>或饮食</strong><br/>① <strong>吃饭时，等长辈先动筷</strong><br/>② <strong>好吃的先请长辈尝，不抢不挑</strong><br/><br/><strong>一句话：一筷子见教养。</strong></p><p><strong>或坐走，长者先，幼者后</strong><br/>① <strong>进门、落座、上车，都请长辈先</strong><br/>② <strong>走路让长辈走里侧，自己跟半步</strong><br/><br/><strong>一句话：让一步，不吃亏。</strong></p></div>
<!-- 5. 长呼人即代叫·人不在己即到 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>长呼人，即代叫；人不在，己即到</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>呼：叫、喊；即：马上；代：帮着</strong><br/>② <strong>不在：人没在；己：自己；到：走过去</strong><br/><br/><strong>一句话：答应要快。</strong></p><p><strong>长呼人，即代叫</strong><br/>① <strong>长辈叫谁，听见就快去传话</strong><br/>② <strong>不能装没听见，也不能只喊一声就算</strong><br/><br/><strong>一句话：听见就动身。</strong></p><p><strong>人不在，己即到</strong><br/>① <strong>要找的人不在，自己过去回一声</strong><br/>② <strong>顺口问一句：有事我可以帮您转告吗</strong><br/><br/><strong>一句话：事情要有着落。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 让与应</h2><p style="margin:0"><strong>前四句讲「让」</strong><br/>① <strong>吃、坐、走，都是天天有的事</strong><br/>② <strong>天天让一次，敬意就长在身上</strong><br/><br/><strong>一句话：让成习惯，就是礼。</strong></p><p><strong>后四句讲「应」</strong><br/>① <strong>听见呼唤，马上应、马上去</strong><br/>② <strong>人不在，也要把话带回去</strong><br/><br/><strong>一句话：应答有声，做事有尾。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>电梯、门口、餐桌，都可以让</strong><br/>② <strong>让的是次序，不是把自己看小</strong><br/><br/><strong>一句话：敬人，也自重。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一组</h2><p style="margin:0"><strong>前四句：先后之序</strong><br/>① <strong>或饮食，或坐走——日常小事</strong><br/>② <strong>长者先，幼者后——长者先行</strong><br/><br/><strong>一句话：小事见礼。</strong></p><p><strong>后四句：呼唤之应</strong><br/>① <strong>长呼人，即代叫——听见就传</strong><br/>② <strong>人不在，己即到——自己回话</strong><br/><br/><strong>一句话：件件有回应。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>饭先请，路先让</strong><br/>② <strong>叫就应，不在就到</strong><br/><br/><strong>一句话：让得下，也应得快。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>吃坐走让长辈先；长辈叫人就代叫；人不在自己过去回话。</p><p>📖 让与应</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>把方便先给人，把回话做到位；礼在日常，不在场面。</p><p>💡 长幼之序</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 长者先，幼者后</p>
<p>这是「弟子规课堂」第十课：出则悌第二段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 让长辈先，我是不是永远排最后？</h3><p><strong>让的是次序，不是把你排到最后。</strong><br/><br/>① <strong>吃饭、进门、落座，请长辈先，是敬</strong><br/>② <strong>该你上场、该你发言，不必退让</strong><br/>③ <strong>记法：场合不同，先后不同。</strong></p><h3>❓ 电梯、地铁上也要让吗？</h3><p><strong>让的是先后，不是非让座不可。</strong><br/><br/>① <strong>进电梯请长辈先进，出电梯请长辈先出</strong><br/>② <strong>人多时帮着按一下门，就是周到</strong><br/>③ <strong>记法：小动作，大分寸。</strong></p><h3>❓ 「长呼人，即代叫」怎么做？</h3><p><strong>听见就动，别装没听见。</strong><br/><br/>① <strong>放下手里的事，快去传一句</strong><br/>② <strong>别只喊「有人找你」，要说清是谁找</strong><br/>③ <strong>记法：传话要传清楚。</strong></p><h3>❓ 「人不在，己即到」是什么意思？</h3><p><strong>找不到人，你自己去回个话。</strong><br/><br/>① <strong>说：他不在，有什么事我可以转告</strong><br/>② <strong>能帮的先帮一把，别让长辈干等</strong><br/>③ <strong>记法：事事有着落。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 吃饭先请长辈动筷</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>菜端上来，先请爷爷奶奶、爸爸妈妈动筷</strong>；<strong>不翻菜、不抢最后一块</strong>。</p><p>💡 进门出门让一让</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>开门先让长辈过，电梯先让长辈进出</strong>；<strong>这不是客气，是心里有别人</strong>。</p><p>🌱 大人叫，马上应</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>听见叫名字，先应一声「来了」，再过去问什么事</strong>；<strong>这就是「即代叫」「己即到」</strong><br/><br/><strong>本课的落点：长者先，幼者后。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第二段。记牢：<strong>长者先，幼者后</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>长幼之序 · 同辈讲和，长幼讲序。<strong>各有各的礼</strong>。</p><p>或饮食，或坐走 · 天天都有的事。<strong>小事见教养</strong>。</p><p>长者先，幼者后 · 吃坐走都让长辈先。<strong>让一步不吃亏</strong>。</p><p>长呼人，即代叫 · 听见就快去传话。<strong>别装没听见</strong>。</p><p>人不在，己即到 · 自己过去回个话。<strong>事事有着落</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第二段；上一课讲兄弟之爱与敬，这一课讲长幼之先与后。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「长者」的「长」读什么音。② 今天吃饭，等长辈先动筷。③ 长辈叫你，三秒内应一声。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「长者先」的「长」怎么读？', opts: ['zhǎng，指长辈', 'cháng，长短', 'zhàng，高'], ans: 0, exp: '长者读 zhǎng zhě'},
  {q: '2. 「或饮食」的「或」是什么意思？', opts: ['有时、或是', '或许不来', '有人'], ans: 0, exp: '或是有时'},
  {q: '3. 「或坐走」的「走」在这里指什么？', opts: ['行走、走路', '跑开', '离开'], ans: 0, exp: '坐和走'},
  {q: '4. 「幼者后」的「幼」是什么意思？', opts: ['年纪小的', '幼小可爱', '幼稚'], ans: 0, exp: '幼是年少'},
  {q: '5. 「长者先，幼者后」讲的是什么？', opts: ['长幼之间的先后次序', '谁走得快谁先', '长辈要等晚辈'], ans: 0, exp: '长幼之序'},
  {q: '6. 「长呼人」的「呼」是什么意思？', opts: ['叫、喊', '呼吸', '呼声'], ans: 0, exp: '呼是叫'},
  {q: '7. 「即代叫」的「代」是什么意思？', opts: ['代替、帮着', '代表', '时代'], ans: 0, exp: '代是帮着'},
  {q: '8. 「人不在，己即到」该怎么做？', opts: ['自己过去回话，问能帮什么', '回来就算了', '大声喊人'], ans: 0, exp: '事事有着落'},
  {q: '9. 长辈叫你的时候，你应该？', opts: ['先应一声，再过去问什么事', '装没听见', '先做完自己的事'], ans: 0, exp: '马上应、马上到'},
  {q: '10. 这一段总的讲什么？', opts: ['起居要让长辈先行，长辈叫人有回应', '怎么安排吃饭座位', '怎么请客吃饭'], ans: 0, exp: '让与应'},
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
s = s.replace('《弟子规》第九课', '《弟子规》第十课')
s = s.replace("window.GUOXUE_COURSE_ID = '549-xiong-dao-you';", "window.GUOXUE_COURSE_ID = '550-zhang-zhe-xian';")
s = s.replace('yaoyue550', 'yaoyue551')

# ---- 校验 ----
for w in ['兄道友', '弟道恭', '兄弟睦', '孝在中', '财物轻', '怨何生', '言语忍', '忿自泯',
          '出则悌第一段', '549-xiong-dao-you', 'yaoyue550', '第九课']:
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
