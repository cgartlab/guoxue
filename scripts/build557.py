#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build557: 以 556 课件（四句版式）为模板生成第 557 课《谨·衣贵洁，不贵华》。
「谨」第三段整段八句：前四句讲穿衣（洁净不华、循分称家），后四句讲吃饭（勿拣择、勿过则）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（穿衣吃饭都有度）/ 3 衣贵洁不贵华·上循分下称家 /
  4 对饮食勿拣择·食适可勿过则 / 5 两句合看（穿与吃）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/556-zhi-guan-fu/index.html"
DST = ROOT + "/lessons/557-yi-gui-jie/index.html"

TITLE = '谨 · 衣贵洁，不贵华，对饮食，勿拣择 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '衣贵洁，不贵华；食适可，勿过则 · 弟子规课堂'
DESC = ('《弟子规》第十七课，谨第三段。原文：「衣贵洁，不贵华。上循分，下称家。'
        '对饮食，勿拣择。食适可，勿过则。」讲穿衣吃饭的度：衣服干净就好，不攀比华丽，'
        '合乎身份与家境；吃饭不挑食，吃到合适就停，不暴饮暴食。')
OG_DESC = '《弟子规》第十七课：衣贵洁不贵华，食适可勿过则。谨第三段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/557-yi-gui-jie/index.html'

ORIG = '衣贵洁，不贵华。上循分，下称家。对饮食，勿拣择。食适可，勿过则。'
ORIG_COMMA = '衣贵洁，不贵华；上循分，下称家；对饮食，勿拣择；食适可，勿过则。'
OLD_ORIG = '冠必正，纽必结。袜与履，俱紧切。置冠服，有定位。勿乱顿，致污秽。'
OLD_ORIG_COMMA = '冠必正，纽必结；袜与履，俱紧切；置冠服，有定位；勿乱顿，致污秽。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('衣贵洁不贵华', ['yī', 'guì', 'jié', 'bù', 'guì', 'huá'], True)
             + ju('上循分下称家', ['shàng', 'xún', 'fèn', 'xià', 'chèn', 'jiā'], False)
             + ju('对饮食勿拣择', ['duì', 'yǐn', 'shí', 'wù', 'jiǎn', 'zé'], False)
             + ju('食适可勿过则', ['shí', 'shì', 'kě', 'wù', 'guò', 'zé'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">衣贵洁</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第三段：衣贵洁，不贵华</p><p class="cover-desc">谨门第三段讲穿衣吃饭。衣服不在花哨，干净整齐就好，还要合身份、称家境；吃饭不挑食，吃到合适就停。穿衣吃饭里，藏着「度」。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第三段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>衣服贵在干净整齐，不贵在华丽漂亮；穿着要合乎自己的身份，也要和家境相称。吃饭不要挑挑拣拣；吃到合适的量就停下来，不要超过限度。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「华」读 huá，是华丽、花哨；「循」是依照；「分」读 fèn，是身份、本分；「称」读 chèn，是相称、相配；「拣择」是挑挑拣拣；「适可」是到了适当的程度就停止；「则」是限度、准则。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 穿衣吃饭都有度</h2><p style="margin:0"><strong>先说「穿」</strong><br/>① <strong>干净整齐最重要，不比华丽</strong><br/>② <strong>合身份、称家境，不攀比</strong><br/><br/><strong>一句话：整洁比名牌体面。</strong></p><p><strong>再说「吃」</strong><br/>① <strong>不挑食，营养才全面</strong><br/>② <strong>吃饱就停，不撑着</strong><br/><br/><strong>一句话：会吃饭也是自律。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>穿衣吃饭天天有，度也天天练</strong><br/>② <strong>懂得够了、停了，才算管住自己</strong><br/><br/><strong>一句话：有度才自在。</strong></p></div>
<!-- 4. 衣贵洁不贵华·上循分下称家 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>衣贵洁，不贵华；上循分，下称家</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>华 huá：华丽、花哨；循：依照</strong><br/>② <strong>分 fèn：身份；称 chèn：相称；家：家境</strong><br/><br/><strong>一句话：干净胜过漂亮。</strong></p><p><strong>衣贵洁，不贵华</strong><br/>① <strong>衣服洗得干干净净，比名牌更体面</strong><br/>② <strong>比穿戴，比的是家风不是钱</strong><br/><br/><strong>一句话：比干净，不比贵。</strong></p><p><strong>上循分，下称家</strong><br/>① <strong>什么身份穿什么衣服，合乎本分</strong><br/>② <strong>家里什么条件，就穿什么衣服，不加重家里负担</strong><br/><br/><strong>一句话：不攀比，是懂事。</strong></p></div>
<!-- 5. 对饮食勿拣择·食适可勿过则 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>对饮食，勿拣择；食适可，勿过则</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>拣择：挑挑拣拣；适可：适可而止</strong><br/>② <strong>过：超过；则：限度、准则</strong><br/><br/><strong>一句话：吃饭也有分寸。</strong></p><p><strong>对饮食，勿拣择</strong><br/>① <strong>青菜豆腐都要吃，营养才全面</strong><br/>② <strong>挑食偏食，个子长不好、身子也弱</strong><br/><br/><strong>一句话：不挑食，长得好。</strong></p><p><strong>食适可，勿过则</strong><br/>① <strong>吃到七八分饱就停筷子</strong><br/>② <strong>再好吃的，吃撑了也伤身体</strong><br/><br/><strong>一句话：贪嘴要吃亏。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 穿与吃</h2><p style="margin:0"><strong>前四句讲「穿」</strong><br/>① <strong>贵洁不贵华——干净第一</strong><br/>② <strong>循分称家——不攀比</strong><br/><br/><strong>一句话：穿上有度。</strong></p><p><strong>后四句讲「吃」</strong><br/>① <strong>勿拣择——不挑食</strong><br/>② <strong>勿过则——不暴饮暴食</strong><br/><br/><strong>一句话：吃上有度。</strong></p><p><strong>谨的功夫</strong><br/>① <strong>前面管作息、管穿戴，这里管吃喝</strong><br/>② <strong>样样有分寸，就是管住了自己</strong><br/><br/><strong>一句话：度，是练出来的。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：怎么穿</strong><br/>① <strong>衣贵洁，不贵华——干净就好</strong><br/>② <strong>上循分，下称家——合身份不攀比</strong><br/><br/><strong>一句话：穿上有分寸。</strong></p><p><strong>后四句：怎么吃</strong><br/>① <strong>对饮食，勿拣择——不挑不拣</strong><br/>② <strong>食适可，勿过则——吃饱就停</strong><br/><br/><strong>一句话：吃上有节制。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>穿干净，不比阔</strong><br/>② <strong>饭不挑，吃到够</strong><br/><br/><strong>一句话：够了就停，才是本事。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>衣服干净不攀比，吃饭不挑不过量。</p><p>📖 穿吃有度</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>懂得满足、懂得节制，人就不被欲望牵着走。</p><p>💡 有度才自在</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 衣贵洁，不贵华</p>
<p>这是「弟子规课堂」第十七课：谨第三段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「不贵华」的「华」怎么读？</h3><p><strong>读 huá，华丽的意思。</strong><br/><br/>① <strong>不贵华：不追求花哨漂亮</strong><br/>② <strong>跟「华山」的 huà、「花朵」的 huā 都不同</strong><br/>③ <strong>记法：华丽的花样叫华。</strong></p><h3>❓ 「上循分，下称家」是什么意思？</h3><p><strong>穿着合身份、称家境。</strong><br/><br/>① <strong>分 fèn：身份本分；称 chèn：相称</strong><br/>② <strong>家里什么条件就穿什么，不加重负担</strong><br/>③ <strong>记法：不攀比是懂事。</strong></p><h3>❓ 「食适可」是什么意思？</h3><p><strong>吃到合适的量就停下来。</strong><br/><br/>① <strong>就是成语「适可而止」的意思</strong><br/>② <strong>吃到七八分饱，不撑着</strong><br/>③ <strong>记法：够了就停筷子。</strong></p><h3>❓ 「勿过则」的「则」是什么意思？</h3><p><strong>限度、准则。</strong><br/><br/>① <strong>过则：超过限度</strong><br/>② <strong>再爱吃的东西，过了量都伤身体</strong><br/>③ <strong>记法：则是画好的线。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 衣服洗干净再穿</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>领口袖口都干净，比穿名牌体面</strong>；<strong>这就是「衣贵洁，不贵华」</strong>。</p><p>💡 不跟同学比穿戴</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>家里买得起什么就穿什么，不吵着买贵的</strong>；<strong>这就是「上循分，下称家」</strong>。</p><p>🌱 吃饭不挑、吃饱就停</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>青菜也吃、饭量合适，不撑着</strong>；<strong>这就是「勿拣择」「勿过则」</strong><br/><br/><strong>本课的落点：穿衣吃饭都有度。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第三段。记牢：<strong>衣贵洁，不贵华</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第三段 · 穿衣吃饭都有度。<strong>有度才自在</strong>。</p><p>衣贵洁，不贵华 · 干净第一。<strong>整洁比名牌体面</strong>。</p><p>上循分，下称家 · 不攀比。<strong>合身份称家境</strong>。</p><p>对饮食，勿拣择 · 不挑食。<strong>营养才全面</strong>。</p><p>食适可，勿过则 · 七八分饱。<strong>贪嘴要吃亏</strong>。</p><p><strong>在全篇中的位置:</strong>谨第三段；上一课讲穿戴整齐与冠服归位，这一课讲穿衣不攀比、吃饭有节制。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「华」「分」「称」在这几句里怎么读。② 今天吃饭挑一样平时不爱吃的菜，尝两口。③ 吃到七八分饱就停筷子一次。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「衣贵洁」的「洁」是什么意思？', opts: ['干净', '节日', '团结'], ans: 0, exp: '洁是干净'},
  {q: '2. 「不贵华」的「华」怎么读？', opts: ['huá，华丽', 'huà，华山', 'huā，花朵'], ans: 0, exp: '华读 huá，华丽'},
  {q: '3. 「上循分」的「分」怎么读？', opts: ['fèn，身份本分', 'fēn，分数', 'fēng，大风'], ans: 0, exp: '分读 fèn'},
  {q: '4. 「下称家」的「称」怎么读？', opts: ['chèn，相称', 'chēng，称呼', 'chèng，秤杆'], ans: 0, exp: '称读 chèn，相称'},
  {q: '5. 「拣择」是什么意思？', opts: ['挑挑拣拣', '捡到东西', '检查作业'], ans: 0, exp: '拣择是挑拣'},
  {q: '6. 「对饮食，勿拣择」讲什么？', opts: ['吃饭不要挑挑拣拣', '多吃零食', '不吃饭来减肥'], ans: 0, exp: '不挑食'},
  {q: '7. 「食适可」讲什么？', opts: ['吃到合适的量就停下来', '吃得越饱越好', '只吃爱吃的'], ans: 0, exp: '适可而止'},
  {q: '8. 「勿过则」的「则」是什么意思？', opts: ['限度、准则', '否则', '处罚'], ans: 0, exp: '则是限度'},
  {q: '9. 挑食的坏处是什么？', opts: ['营养不全面，长不好', '可以省饭钱', '吃饭速度更快'], ans: 0, exp: '不挑食营养全'},
  {q: '10. 这一段总的讲什么？', opts: ['穿衣吃饭都有度，不攀比不贪吃', '只穿名牌才体面', '想吃什么就吃什么'], ans: 0, exp: '穿吃有度'},
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
s = s.replace('《弟子规》第十六课', '《弟子规》第十七课')
s = s.replace('谨第二段', '谨第三段')
s = s.replace("window.GUOXUE_COURSE_ID = '556-zhi-guan-fu';", "window.GUOXUE_COURSE_ID = '557-yi-gui-jie';")
s = s.replace('yaoyue558', 'yaoyue559')

# ---- 校验 ----
for w in ['冠必正', '纽必结', '袜与履', '俱紧切', '置冠服', '有定位', '勿乱顿', '致污秽',
          '谨第二段', '556-zhi-guan-fu', 'yaoyue558', '第十六课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
expect = {'slide': s.count('class="slide'), 'ruby': s.count('<ruby'), 'rt': s.count('<rt>'),
          'quiz': s.count("{q: '"), 'page_max': len(re.findall(r'data-page="', s))}
if expect['slide'] != 26 or expect['ruby'] != 24 or expect['rt'] != 24 or expect['quiz'] != 10 or expect['page_max'] != 24:
    print('[FAIL] 结构计数不符（slide 含 viewport/container 两个前缀，应为 24 页 + 2；本课原文 4 句，ruby 应为 24）:', expect)
    sys.exit(1)
print('[OK] 结构计数:', expect)
print('[OK] 章节锚点: 讲义区 %d→%d, 答疑区 %d→%d' % (i1, i2, j1, j2))

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(s)
print('[OK] 已生成', DST)
