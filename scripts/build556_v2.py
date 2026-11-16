#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build556（全段版）: 以 555 课件（四句版式）为模板，重做第 556 课《谨·冠必正…致污秽》。
「谨」第二段整段八句：前四句讲穿戴（冠正、纽结、袜履紧切），后四句讲归位（有定位、勿乱顿）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（穿戴与归位）/ 3 冠必正纽必结·袜与履俱紧切 /
  4 置冠服有定位·勿乱顿致污秽 / 5 两句合看（穿与放）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
课程 id 与网址不变（556-zhi-guan-fu），仅内容补全为八句整段。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/555-zhao-qi-zao/index.html"
DST = ROOT + "/lessons/556-zhi-guan-fu/index.html"

TITLE = '谨 · 冠必正，纽必结，袜与履，俱紧切 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '冠必正，纽必结；置冠服，有定位 · 弟子规课堂'
DESC = ('《弟子规》第十六课，谨第二段。原文：「冠必正，纽必结。袜与履，俱紧切。'
        '置冠服，有定位。勿乱顿，致污秽。」讲穿戴与归位：帽子戴正、纽扣系好，'
        '袜子和鞋穿得服帖；脱下来的冠服放到固定位置，不乱堆乱丢，免得弄脏弄坏。')
OG_DESC = '《弟子规》第十六课：冠必正纽必结，置冠服有定位。谨第二段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/556-zhi-guan-fu/index.html'

ORIG = '冠必正，纽必结。袜与履，俱紧切。置冠服，有定位。勿乱顿，致污秽。'
ORIG_COMMA = '冠必正，纽必结；袜与履，俱紧切；置冠服，有定位；勿乱顿，致污秽。'
OLD_ORIG = '朝起早，夜眠迟。老易至，惜此时。晨必盥，兼漱口。便溺回，辄净手。'
OLD_ORIG_COMMA = '朝起早，夜眠迟；老易至，惜此时；晨必盥，兼漱口；便溺回，辄净手。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('冠必正纽必结', ['guān', 'bì', 'zhèng', 'niǔ', 'bì', 'jié'], True)
             + ju('袜与履俱紧切', ['wà', 'yǔ', 'lǚ', 'jù', 'jǐn', 'qiè'], False)
             + ju('置冠服有定位', ['zhì', 'guān', 'fú', 'yǒu', 'dìng', 'wèi'], False)
             + ju('勿乱顿致污秽', ['wù', 'luàn', 'dùn', 'zhì', 'wū', 'huì'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">冠必正</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第二段：冠必正，纽必结</p><p class="cover-desc">谨门第二段，八句说两件事：前四句讲「穿」——帽子戴正、纽扣结好、袜子鞋穿得服帖；后四句讲「放」——脱下来的冠服放回固定位置，不乱堆乱丢。穿得整齐，放得妥当，人就精神。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第二段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>帽子要戴正，纽扣要系好；袜子和鞋都要穿得服帖。脱下来的帽子和衣服，要放到固定的位置；不要乱堆乱放，免得把它们弄脏弄乱。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「冠」读 guān，是帽子；「纽」是纽扣；「结」是系好；「履」读 lǚ，是鞋；「俱」是都；「紧切」是紧紧贴身、服帖；「置」是摆放；「定位」是固定的位置；「顿」是搁置，乱顿就是乱堆乱放；「秽」读 huì，是脏乱。前四句讲穿，后四句讲放。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 穿戴与归位</h2><p style="margin:0"><strong>先说「穿」</strong><br/>① <strong>帽子正、纽扣结、鞋袜服帖</strong><br/>② <strong>穿得整齐，人也精神</strong><br/><br/><strong>一句话：整齐不用贵。</strong></p><p><strong>再说「放」</strong><br/>① <strong>脱下来放回固定位置</strong><br/>② <strong>不乱堆乱丢，不脏不皱</strong><br/><br/><strong>一句话：东西有家。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>穿和放，都是天天的小事</strong><br/>② <strong>小事做周全，就是「谨」</strong><br/><br/><strong>一句话：严谨看得见。</strong></p></div>
<!-- 4. 冠必正纽必结·袜与履俱紧切 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>冠必正，纽必结；袜与履，俱紧切</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>冠 guān：帽子；纽：纽扣；结：系好</strong><br/>② <strong>履 lǚ：鞋；俱：都；紧切：服帖</strong><br/><br/><strong>一句话：穿戴有讲究。</strong></p><p><strong>冠必正，纽必结</strong><br/>① <strong>帽子歪了扶一扶，纽扣开了系回去</strong><br/>② <strong>衣冠不整，是对人也是对己不尊重</strong><br/><br/><strong>一句话：出门先照一照。</strong></p><p><strong>袜与履，俱紧切</strong><br/>① <strong>袜子提好，鞋带系紧，鞋子穿正</strong><br/>② <strong>拖拖拉拉趿着鞋，做事也容易拖拖拉拉</strong><br/><br/><strong>一句话：脚下利索，人才利索。</strong></p></div>
<!-- 5. 置冠服有定位·勿乱顿致污秽 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>置冠服，有定位；勿乱顿，致污秽</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>置：摆放；定位：固定的位置</strong><br/>② <strong>顿：搁置；致：导致；污秽：脏乱</strong><br/><br/><strong>一句话：脱下来也要有规矩。</strong></p><p><strong>置冠服，有定位</strong><br/>① <strong>放学回家，外套帽子挂到固定的钩子上</strong><br/>② <strong>睡前脱下的衣服叠好放整齐</strong><br/><br/><strong>一句话：给东西安个家。</strong></p><p><strong>勿乱顿，致污秽</strong><br/>① <strong>扔在地上、塞进床底，容易踩脏压皱</strong><br/>② <strong>脏了重洗、皱了重整，费的是自己的时间</strong><br/><br/><strong>一句话：乱丢一下下，收拾半小时。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 穿与放</h2><p style="margin:0"><strong>前四句讲「穿」</strong><br/>① <strong>正、结、紧——身上利落</strong><br/>② <strong>穿戴整齐是精神头，也是礼</strong><br/><br/><strong>一句话：人靠衣冠齐。</strong></p><p><strong>后四句讲「放」</strong><br/>① <strong>有定位、不乱顿——屋里利落</strong><br/>② <strong>东西归位，随时能找</strong><br/><br/><strong>一句话：屋里齐，心里齐。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>出门前照镜子：帽正、扣结、鞋穿好</strong><br/>② <strong>回家后归位：挂钩挂好、鞋摆整齐</strong><br/><br/><strong>一句话：一穿一放，都见功夫。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：怎么穿</strong><br/>① <strong>冠必正，纽必结——头面齐整</strong><br/>② <strong>袜与履，俱紧切——脚下服帖</strong><br/><br/><strong>一句话：从头到脚都利索。</strong></p><p><strong>后四句：怎么放</strong><br/>① <strong>置冠服，有定位——放回原处</strong><br/>② <strong>勿乱顿，致污秽——不乱堆乱丢</strong><br/><br/><strong>一句话：脱下来也有规矩。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>帽正扣结鞋穿好</strong><br/>② <strong>脱下放回原位置，不脏不皱好寻找</strong><br/><br/><strong>一句话：穿放都有谱。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>穿戴整齐，冠服归位，不脏不乱。</p><p>📖 穿放有谱</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>衣冠是一个人的精神头，管住小事才管得住自己。</p><p>💡 整齐即自律</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 冠必正，纽必结</p>
<p>这是「弟子规课堂」第十六课：谨第二段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「冠」字怎么读、什么意思？</h3><p><strong>读 guān，是帽子。</strong><br/><br/>① <strong>冠必正：帽子要戴正</strong><br/>② <strong>拿掉「必」就是「帽子正」的意思</strong><br/>③ <strong>记法： 戴在头上的叫冠。</strong></p><h3>❓ 「袜与履，俱紧切」是什么意思？</h3><p><strong>袜子和鞋都要穿得服帖。</strong><br/><br/>① <strong>履 lǚ 是鞋；俱是「都」；紧切是贴身服帖</strong><br/>② <strong>袜子提好、鞋带系紧，不拖拖拉拉</strong><br/>③ <strong>记法：脚下利索，人才利索。</strong></p><h3>❓ 「乱顿」的「顿」是什么意思？</h3><p><strong>搁置、放下的意思。</strong><br/><br/>① <strong>乱顿 = 乱堆乱放、随手一丢</strong><br/>② <strong>图省事一下，换来脏皱难找</strong><br/>③ <strong>记法：顿是放下，乱顿是乱丢。</strong></p><h3>❓ 「致污秽」的「秽」怎么读？</h3><p><strong>读 huì，是脏乱。</strong><br/><br/>① <strong>致污秽：弄到又脏又乱</strong><br/>② <strong>跟「污」连在一起记：污秽</strong><br/>③ <strong>记法：秽是有「秽气」的脏。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 出门前照一照</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>帽子正不正、纽扣结没结、鞋带紧不紧</strong>；<strong>这就是「冠必正，纽必结」</strong>。</p><p>💡 脱下的外套挂挂钩</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>回家挂在固定的钩子上，不扔椅子上</strong>；<strong>这就是「置冠服，有定位」</strong>。</p><p>🌱 脱下的鞋摆整齐</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>鞋头朝外摆进鞋架，不乱踢乱甩</strong>；<strong>不堆不丢就不脏不皱</strong><br/><br/><strong>本课的落点：穿得整齐，放得妥当。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第二段。记牢：<strong>冠必正，纽必结</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第二段 · 穿和放都有规矩。<strong>整齐即自律</strong>。</p><p>冠必正，纽必结 · 头面齐整。<strong>出门先照一照</strong>。</p><p>袜与履，俱紧切 · 脚下服帖。<strong>脚下利索</strong>。</p><p>置冠服，有定位 · 放回原处。<strong>东西有家</strong>。</p><p>勿乱顿，致污秽 · 不乱堆乱丢。<strong>不脏不皱</strong>。</p><p><strong>在全篇中的位置:</strong>谨第二段；上一课讲作息与卫生，这一课讲穿戴整齐与冠服归位。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「冠」「履」「秽」怎么读。② 明天出门前照镜子检查帽子和纽扣。③ 脱下的外套挂到固定的钩子上一次。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「冠必正」的「冠」怎么读？', opts: ['guān，帽子', 'guàn，冠军', 'kòu，扣子'], ans: 0, exp: '冠读 guān，是帽子'},
  {q: '2. 「纽必结」的「纽」是什么？', opts: ['纽扣', '纽带', '手指'], ans: 0, exp: '纽是纽扣'},
  {q: '3. 「袜与履」的「履」是什么意思？', opts: ['鞋', '走路', '袜子'], ans: 0, exp: '履读 lǚ，是鞋'},
  {q: '4. 「俱紧切」的「俱」是什么意思？', opts: ['都、全部', '聚会', '剧团'], ans: 0, exp: '俱是都'},
  {q: '5. 「勿乱顿」的「顿」是什么意思？', opts: ['搁置、放下', '一顿饭', '停顿'], ans: 0, exp: '顿是搁置'},
  {q: '6. 「冠必正，纽必结」讲什么？', opts: ['帽子要戴正，纽扣要系好', '帽子要天天洗', '纽扣越多越好看'], ans: 0, exp: '穿戴整齐'},
  {q: '7. 「袜与履，俱紧切」讲什么？', opts: ['袜子和鞋都要穿得服帖', '袜子越紧越好', '不穿袜子也行'], ans: 0, exp: '穿得服帖'},
  {q: '8. 脱下来的帽子应该放哪？', opts: ['放到固定的地方', '扔在椅子上', '塞进书包里'], ans: 0, exp: '有定位'},
  {q: '9. 为什么不能乱放衣服？', opts: ['容易弄脏弄皱', '会被晒化', '会变大变长'], ans: 0, exp: '致污秽'},
  {q: '10. 这一段总的讲什么？', opts: ['穿得整齐、放得妥当', '多买几件新衣服', '怎么跑得快'], ans: 0, exp: '谨第二段'},
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
s = s.replace('《弟子规》第十五课', '《弟子规》第十六课')
s = s.replace('谨第一段', '谨第二段')
s = s.replace("window.GUOXUE_COURSE_ID = '555-zhao-qi-zao';", "window.GUOXUE_COURSE_ID = '556-zhi-guan-fu';")
s = s.replace('yaoyue556', 'yaoyue558')

# ---- 校验 ----
for w in ['朝起早', '夜眠迟', '老易至', '惜此时', '晨必盥', '兼漱口', '便溺回', '辄净手',
          '谨第一段', '555-zhao-qi-zao', 'yaoyue556', '第十五课']:
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
