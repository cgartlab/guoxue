#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build556: 以 554 课件（两句版式）为模板生成第 556 课《谨·置冠服，有定位》。
「谨」第二段，讲东西放好：冠服有定位，勿乱顿致污秽。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（东西有家）/ 3 置冠服有定位 /
  4 勿乱顿致污秽 / 5 两句合看（放与找）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/554-shi-zhu-fu/index.html"
DST = ROOT + "/lessons/556-zhi-guan-fu/index.html"

TITLE = '谨 · 置冠服，有定位，勿乱顿，致污秽 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '置冠服，有定位；勿乱顿，致污秽 · 弟子规课堂'
DESC = ('《弟子规》第十六课，谨第二段。原文：「置冠服，有定位。勿乱顿，致污秽。」'
        '讲东西放好：帽子和衣服脱下来要放到固定的位置，不乱堆乱丢，'
        '免得弄脏弄坏。东西有自己的家，找起来快，也不会弄糟。')
OG_DESC = '《弟子规》第十六课：置冠服有定位，勿乱顿致污秽。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/556-zhi-guan-fu/index.html'

ORIG = '置冠服，有定位。勿乱顿，致污秽。'
ORIG_COMMA = '置冠服，有定位；勿乱顿，致污秽。'
OLD_ORIG = '事诸父，如事父。事诸兄，如事兄。'
OLD_ORIG_COMMA = '事诸父，如事父；事诸兄，如事兄。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('置冠服有定位', ['zhì', 'guān', 'fú', 'yǒu', 'dìng', 'wèi'], True)
             + ju('勿乱顿致污秽', ['wù', 'luàn', 'dùn', 'zhì', 'wū', 'huì'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">有定位</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第二段：置冠服，有定位</p><p class="cover-desc">上一课讲作息和洗漱，这一课讲放东西：帽子和衣服脱下来，放到固定的地方，不乱堆乱丢。东西有自己的「家」，找起来快，也不会弄脏弄坏。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第二段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>摆放帽子和衣服，要有固定的位置；不要乱堆乱放，免得把它们弄脏弄乱。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「置」是摆放；「冠」读 guān，是帽子；「服」是衣服；「定位」是固定的位置；「勿」是不要；「顿」是搁置、放下，乱顿就是乱堆乱放；「致」是导致；「污」是脏；「秽」读 huì，是脏乱。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 东西有家</h2><p style="margin:0"><strong>先说「放」</strong><br/>① <strong>每样东西都有自己的家</strong><br/>② <strong>帽子挂帽钩，衣服进衣柜</strong><br/><br/><strong>一句话：放回原处。</strong></p><p><strong>再说「找」</strong><br/>① <strong>放得整齐，找得就快</strong><br/>② <strong>乱堆乱丢，翻半天找不到</strong><br/><br/><strong>一句话：乱放是给自己添堵。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>管东西，也是「谨」的一部分</strong><br/>② <strong>放好一顶帽子，就是练一次自律</strong><br/><br/><strong>一句话：物归其位。</strong></p></div>
<!-- 4. 置冠服，有定位 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>置冠服，有定位</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>置：摆放；冠 guān：帽子</strong><br/>② <strong>定位：固定的位置</strong><br/><br/><strong>一句话：脱下来就要放好。</strong></p><p><strong>置冠服，有定位</strong><br/>① <strong>放学回家，外套帽子挂到固定的钩子上</strong><br/>② <strong>睡前脱下的衣服，叠好放在床头椅上</strong><br/><br/><strong>一句话：给东西安个家。</strong></p><p><strong>为什么放固定位置</strong><br/>① <strong>固定了，闭着眼都找得到</strong><br/>② <strong>第二天上学不手忙脚乱</strong><br/><br/><strong>一句话：省时间，省力气。</strong></p></div>
<!-- 5. 勿乱顿，致污秽 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>勿乱顿，致污秽</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>勿：不要；顿：搁置、放下</strong><br/>② <strong>致：导致；污秽：又脏又乱</strong><br/><br/><strong>一句话：乱放有代价。</strong></p><p><strong>勿乱顿，致污秽</strong><br/>① <strong>扔在地上、塞在床底，很容易踩脏、压皱</strong><br/>② <strong>脏了要重洗，皱了要重整，费的是自己的时间</strong><br/><br/><strong>一句话：乱丢一下下，收拾半小时。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>书包、铅笔、玩具，用完都送回原位</strong><br/>② <strong>脱下的鞋摆进鞋架，摆整齐</strong><br/><br/><strong>一句话：归位只用十秒。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 放与找</h2><p style="margin:0"><strong>前一句讲「规矩」</strong><br/>① <strong>有定位——东西的家定下来</strong><br/>② <strong>回回放同一个地方</strong><br/><br/><strong>一句话：定下来才有得靠。</strong></p><p><strong>后一句讲「后果」</strong><br/>① <strong>乱顿——图一时省事</strong><br/>② <strong>换来的是脏、皱、找不到</strong><br/><br/><strong>一句话：省小事，误大事。</strong></p><p><strong>谨的功夫</strong><br/>① <strong>上一课管作息，这一课管东西</strong><br/>② <strong>天天做、不用催，就是「谨」</strong><br/><br/><strong>一句话：自律看得见。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 两句一对</h2><p style="margin:0"><strong>前一句：怎么做</strong><br/>① <strong>置冠服，有定位——放固定位置</strong><br/>② <strong>帽子归帽钩，衣服归衣柜</strong><br/><br/><strong>一句话：物有其位。</strong></p><p><strong>后一句：不怎么做</strong><br/>① <strong>勿乱顿——不乱堆乱丢</strong><br/>② <strong>免得致污秽——脏了皱了难收拾</strong><br/><br/><strong>一句话：不贪图省事。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>脱下来，放回去，位置不换</strong><br/>② <strong>不乱丢，不乱堆，东西不糟</strong><br/><br/><strong>一句话：东西有家，随时能找。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>帽子和衣服放到固定位置，不乱堆乱丢。</p><p>📖 物归其位</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>管得住东西的人，才管得住自己。</p><p>💡 整齐即自律</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 置冠服，有定位</p>
<p>这是「弟子规课堂」第十六课：谨第二段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「置冠服」是什么意思？</h3><p><strong>摆放帽子和衣服。</strong><br/><br/>① <strong>置：摆放；冠 guān：帽子；服：衣服</strong><br/>② <strong>脱下来的、摘下来的，都要放好</strong><br/>③ <strong>记法：脱下来就归位。</strong></p><h3>❓ 「有定位」为什么重要？</h3><p><strong>固定位置，好处马上看得见。</strong><br/><br/>① <strong>找起来快，出门不翻箱倒柜</strong><br/>② <strong>不易弄脏弄坏，东西用得久</strong><br/>③ <strong>记法：东西有家，随手可取。</strong></p><h3>❓ 「乱顿」的「顿」是什么意思？</h3><p><strong>搁置、放下的意思。</strong><br/><br/>① <strong>乱顿 = 乱堆乱放、随手一丢</strong><br/>② <strong>图省事一下，麻烦的是以后</strong><br/>③ <strong>记法：顿是放下，乱顿是乱丢。</strong></p><h3>❓ 书包、玩具也算「冠服」吗？</h3><p><strong>道理一样，都适用。</strong><br/><br/>① <strong>课本、铅笔、玩具，都给它们定个家</strong><br/>② <strong>用完送回原位，就是「有定位」</strong><br/>③ <strong>记法：一样东西一个家。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 外套帽子挂挂钩</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>放学回家，外套帽子挂到固定的钩子上</strong>；<strong>这就是「置冠服，有定位」</strong>。</p><p>💡 脱下的鞋摆整齐</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>进屋脱鞋摆进鞋架，鞋头朝外</strong>；<strong>不乱踢乱甩</strong>。</p><p>🌱 书包铅笔用完归位</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>铅笔插回笔盒，书包放回原位</strong>；<strong>第二天不手忙脚乱</strong><br/><br/><strong>本课的落点：置冠服，有定位。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第二段。记牢：<strong>置冠服，有定位</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第二段 · 管东西也是自律。<strong>物归其位</strong>。</p><p>置冠服，有定位 · 放固定位置。<strong>东西有家</strong>。</p><p>勿乱顿，致污秽 · 乱放有代价。<strong>脏皱难收拾</strong>。</p><p>放好再找 · 放得整齐找得快。<strong>省时省力</strong>。</p><p>天天归位 · 十秒钟的事。<strong>习惯不用催</strong>。</p><p><strong>在全篇中的位置:</strong>谨第二段；上一课讲作息与卫生，这一课讲把脱下来的冠服放好、不乱堆乱丢。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「冠」和「秽」怎么读。② 今天脱下的外套挂到固定的钩子上。③ 铅笔用完马上插回笔盒一次。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「置冠服」的「置」是什么意思？', opts: ['摆放', '买', '戴着'], ans: 0, exp: '置是摆放'},
  {q: '2. 「冠」指的是什么？', opts: ['帽子', '衣服', '鞋子'], ans: 0, exp: '冠读 guān，是帽子'},
  {q: '3. 「有定位」的「位」是什么意思？', opts: ['固定的位置', '座位', '职位'], ans: 0, exp: '位是位置'},
  {q: '4. 「勿乱顿」的「顿」是什么意思？', opts: ['搁置、放下', '一顿饭', '停顿'], ans: 0, exp: '顿是搁置'},
  {q: '5. 「致污秽」的「秽」怎么读？', opts: ['huì', 'suì', 'chóng'], ans: 0, exp: '秽读 huì'},
  {q: '6. 「置冠服，有定位」讲什么？', opts: ['帽子和衣服要放在固定的地方', '衣服要天天买新的', '出门必须戴帽子'], ans: 0, exp: '放固定位置'},
  {q: '7. 「致污秽」说的是什么后果？', opts: ['东西被弄脏弄乱', '东西被别人拿走', '衣服变小了'], ans: 0, exp: '脏乱难收拾'},
  {q: '8. 脱下来的外套应该？', opts: ['挂到固定的地方', '扔在椅子上', '塞进床底下'], ans: 0, exp: '放回定位'},
  {q: '9. 铅笔用完了应该？', opts: ['马上放回文具盒', '随手一丢', '塞进裤兜'], ans: 0, exp: '用完归位'},
  {q: '10. 这一段总的讲什么？', opts: ['东西放好，不乱堆乱丢', '多买几件新衣服', '早点睡觉早点起'], ans: 0, exp: '物归其位'},
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
s = s.replace('《弟子规》第十四课', '《弟子规》第十六课')
s = s.replace('出则悌第六段', '谨第二段')
s = s.replace("window.GUOXUE_COURSE_ID = '554-shi-zhu-fu';", "window.GUOXUE_COURSE_ID = '556-zhi-guan-fu';")
s = s.replace('yaoyue555', 'yaoyue557')

# ---- 校验 ----
for w in ['事诸父', '如事父', '事诸兄', '如事兄', '出则悌第六段',
          '554-shi-zhu-fu', 'yaoyue555', '第十四课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
expect = {'slide': s.count('class="slide'), 'ruby': s.count('<ruby'), 'rt': s.count('<rt>'),
          'quiz': s.count("{q: '"), 'page_max': len(re.findall(r'data-page="', s))}
if expect['slide'] != 26 or expect['ruby'] != 12 or expect['rt'] != 12 or expect['quiz'] != 10 or expect['page_max'] != 24:
    print('[FAIL] 结构计数不符（slide 含 viewport/container 两个前缀，应为 24 页 + 2；本课原文 2 句，ruby 应为 12）:', expect)
    sys.exit(1)
print('[OK] 结构计数:', expect)
print('[OK] 章节锚点: 讲义区 %d→%d, 答疑区 %d→%d' % (i1, i2, j1, j2))

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(s)
print('[OK] 已生成', DST)
