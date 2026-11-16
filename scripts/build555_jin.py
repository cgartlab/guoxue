#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build555_jin: 以 553 课件（四句版式）为模板生成第 555 课《谨·朝起早，夜眠迟》。
「谨」第一段（开篇），讲作息与卫生：早起晚睡惜时，晨起盥漱，便后净手。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（管好自己）/ 3 朝起早夜眠迟·老易至惜此时 /
  4 晨必盥兼漱口·便溺回辄净手 / 5 两句合看（惜时与卫生）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。谨门开篇。
说明：原先误排在此的「信·凡出言」内容由 scripts/build555.py 保留，待谨讲完后顺延排课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/553-zun-zhang-qian/index.html"
DST = ROOT + "/lessons/555-zhao-qi-zao/index.html"

TITLE = '谨 · 朝起早，夜眠迟，老易至，惜此时 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '朝起早，夜眠迟；晨必盥，兼漱口 · 弟子规课堂'
DESC = ('《弟子规》第十五课，谨第一段（开篇）。原文：「朝起早，夜眠迟。老易至，惜此时。'
        '晨必盥，兼漱口。便溺回，辄净手。」讲作息与卫生：早上早起、晚上不过早贪睡，'
        '珍惜少年时光；起床要洗脸漱口，上完厕所要洗手。管好自己，从每天睁眼开始。')
OG_DESC = '《弟子规》第十五课：朝起早夜眠迟，晨必盥兼漱口。谨门开篇。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/555-zhao-qi-zao/index.html'

ORIG = '朝起早，夜眠迟。老易至，惜此时。晨必盥，兼漱口。便溺回，辄净手。'
ORIG_COMMA = '朝起早，夜眠迟；老易至，惜此时；晨必盥，兼漱口；便溺回，辄净手。'
OLD_ORIG = '尊长前，声要低。低不闻，却非宜。进必趋，退必迟。问起对，视勿移。'
OLD_ORIG_COMMA = '尊长前，声要低；低不闻，却非宜；进必趋，退必迟；问起对，视勿移。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('朝起早夜眠迟', ['zhāo', 'qǐ', 'zǎo', 'yè', 'mián', 'chí'], True)
             + ju('老易至惜此时', ['lǎo', 'yì', 'zhì', 'xī', 'cǐ', 'shí'], False)
             + ju('晨必盥兼漱口', ['chén', 'bì', 'guàn', 'jiān', 'shù', 'kǒu'], False)
             + ju('便溺回辄净手', ['biàn', 'niào', 'huí', 'zhé', 'jìng', 'shǒu'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">惜此时</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第一段：朝起早，夜眠迟</p><p class="cover-desc">出则悌一门已经完结。从这一课起开新的一门「谨」——讲管好自己。第一段说两件事：一是作息，早起晚睡、珍惜少年时光；二是卫生，起床洗漱、便后洗手。管好自己，从每天睁眼开始。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第一段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>早上要早点起床，晚上不要天一黑就困着睡；人变老是很快的事，少年时光要好好珍惜。早晨起床后要洗脸洗手，还要漱口刷牙；上完厕所回来，就要马上把手洗干净。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「朝」读 zhāo，是早晨；「眠」是睡觉；「迟」是晚一些；「易」是容易；「惜」是珍惜；「盥」读 guàn，是洗手洗脸；「兼」是还要、同时；「漱口」是含水洗口腔；「溺」在这里读 niào，同「尿」；「辄」读 zhé，是就、总是。前四句讲珍惜光阴，后四句讲讲究卫生。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 管好自己</h2><p style="margin:0"><strong>先说作息</strong><br/>① <strong>早上不赖床，晚上不贪玩</strong><br/>② <strong>把时间用在该做的事上</strong><br/><br/><strong>一句话：日子是省出来的。</strong></p><p><strong>再说卫生</strong><br/>① <strong>起床洗漱，便后洗手</strong><br/>② <strong>干净是给自己，也是给别人</strong><br/><br/><strong>一句话：整洁不用提醒。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>「谨」就是自己管好自己</strong><br/>② <strong>不用人催、不用人盯</strong><br/><br/><strong>一句话：从小事练起。</strong></p></div>
<!-- 4. 朝起早夜眠迟·老易至惜此时 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>朝起早，夜眠迟；老易至，惜此时</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>朝 zhāo：早晨；迟：晚一些</strong><br/>② <strong>易：容易；惜：珍惜</strong><br/><br/><strong>一句话：时间不经花。</strong></p><p><strong>朝起早，夜眠迟</strong><br/>① <strong>早上不赖床，起来了就利利索索</strong><br/>② <strong>晚上不天一黑就睡，先做完该做的事</strong><br/><br/><strong>一句话：勤奋不贪懒。</strong></p><p><strong>老易至，惜此时</strong><br/>① <strong>一转眼就长大了、老了</strong><br/>② <strong>少年时候记性好、精力足，最该用功</strong><br/><br/><strong>一句话：现在就是最好的时候。</strong></p></div>
<!-- 5. 晨必盥兼漱口·便溺回辄净手 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>晨必盥，兼漱口；便溺回，辄净手</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>盥 guàn：洗手洗脸；兼：还要</strong><br/>② <strong>溺 niào：同「尿」；辄 zhé：就</strong><br/><br/><strong>一句话：卫生有规矩。</strong></p><p><strong>晨必盥，兼漱口</strong><br/>① <strong>起床第一件事：洗脸、洗手、漱口</strong><br/>② <strong>干干净净出门，自己也精神</strong><br/><br/><strong>一句话：清爽从早上开始。</strong></p><p><strong>便溺回，辄净手</strong><br/>① <strong>上完厕所，回来第一件事是洗手</strong><br/>② <strong>不用人提醒，成了习惯才叫「谨」</strong><br/><br/><strong>一句话：好习惯不等人催。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 惜时与卫生</h2><p style="margin:0"><strong>前四句讲「时间」</strong><br/>① <strong>作息规律，光阴不白过</strong><br/>② <strong>老得快，少年最金贵</strong><br/><br/><strong>一句话：惜时如惜金。</strong></p><p><strong>后四句讲「身体」</strong><br/>① <strong>洗漱、洗手，是天天的小事</strong><br/>② <strong>小事天天做，才叫管得住自己</strong><br/><br/><strong>一句话：干净是本分。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>定好睡觉、起床的点，不拖</strong><br/>② <strong>洗漱、饭前便后洗手，不用人叫</strong><br/><br/><strong>一句话：谨，从小事开始。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：惜时</strong><br/>① <strong>朝起早，夜眠迟——早晚都有安排</strong><br/>② <strong>老易至，惜此时——少年不重来</strong><br/><br/><strong>一句话：光阴不等人。</strong></p><p><strong>后四句：卫生</strong><br/>① <strong>晨必盥，兼漱口——起床就洗漱</strong><br/>② <strong>便溺回，辄净手——便后必洗手</strong><br/><br/><strong>一句话：干净天天做。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>起得早，睡得稳，时间省下来</strong><br/>② <strong>脸洗净，手洗勤，身体清爽</strong><br/><br/><strong>一句话：管好自己，从睁眼开始。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>早起晚睡惜光阴，洗漱洗手讲卫生。</p><p>📖 作息与卫生</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>「谨」是自己管好自己，小事不用人催。</p><p>💡 自律从小事起</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 朝起早，夜眠迟</p>
<p>这是「弟子规课堂」第十五课：谨第一段（开篇）。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「夜眠迟」是让我们熬夜玩吗？</h3><p><strong>不是，是把晚上的时间用在该做的事上。</strong><br/><br/>① <strong>功课做完了、东西收拾好了，再歇</strong><br/>② <strong>熬夜伤身体，孩子更不能玩手机到半夜</strong><br/>③ <strong>记法：晚上勤快，不是晚上贪玩。</strong></p><h3>❓ 「老易至」是什么意思？</h3><p><strong>人变老是很快的事。</strong><br/><br/>① <strong>一晃就长大，一晃就变老</strong><br/>② <strong>少年时光过去了就不再来</strong><br/>③ <strong>记法：现在最金贵。</strong></p><h3>❓ 「盥」字怎么读、什么意思？</h3><p><strong>读 guàn，洗手洗脸。</strong><br/><br/>① <strong>上面是两只手，下面是盆</strong><br/>② <strong>晨必盥：起床就要洗漱</strong><br/>③ <strong>记法：水里洗手就是盥。</strong></p><h3>❓ 「辄净手」的「辄」是什么意思？</h3><p><strong>读 zhé，是「就」。</strong><br/><br/>① <strong>便溺回，辄净手：上完厕所就洗手</strong><br/>② <strong>「就」字说明不用人提醒</strong><br/>③ <strong>记法：马上就做，才叫习惯。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 早上不赖床</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>铃响了就起来，起来就穿好衣服</strong>；<strong>这就是「朝起早」</strong>。</p><p>💡 起床先洗漱</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>洗脸、洗手、漱口刷牙，一样不落</strong>；<strong>这就是「晨必盥，兼漱口」</strong>。</p><p>🌱 便后马上洗手</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不用大人叫，自己就知道去洗</strong>；<strong>这就是「辄净手」</strong><br/><br/><strong>本课的落点：管好自己，从每天睁眼开始。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第一段，也是「谨」这门的开篇。记牢：<strong>朝起早，夜眠迟</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨门开篇 · 自己管好自己。<strong>从小事练起</strong>。</p><p>朝起早，夜眠迟 · 早晚有安排。<strong>勤奋不贪懒</strong>。</p><p>老易至，惜此时 · 少年不重来。<strong>现在最金贵</strong>。</p><p>晨必盥，兼漱口 · 起床就洗漱。<strong>清爽一整天</strong>。</p><p>便溺回，辄净手 · 马上就洗手。<strong>习惯不用催</strong>。</p><p><strong>在全篇中的位置:</strong>谨第一段（开篇）；上一门出则悌讲敬与让已经收官，这一课起开新的一门「谨」，先讲作息与卫生这两件最日常的小事。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「盥」和「辄」怎么读。② 明天早上铃响就起床，起来先洗漱。③ 上完厕所，不用提醒自己先洗手。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「朝起早」的「朝」怎么读？', opts: ['zhāo，早晨', 'cháo，朝代', 'cháo，朝向'], ans: 0, exp: '朝读 zhāo，早晨'},
  {q: '2. 「夜眠迟」的「迟」是什么意思？', opts: ['晚一些', '迟到挨批', '慢慢等待'], ans: 0, exp: '迟是晚一些'},
  {q: '3. 「老易至」讲什么？', opts: ['人变老是很快的事', '老人容易来家里', '老了容易忘事'], ans: 0, exp: '时光过得快'},
  {q: '4. 「惜此时」的「惜」是什么意思？', opts: ['珍惜', '可惜', '舍不得花钱'], ans: 0, exp: '惜是珍惜'},
  {q: '5. 「晨必盥」的「盥」怎么读？', opts: ['guàn', 'mén', 'huàn'], ans: 0, exp: '盥读 guàn'},
  {q: '6. 「晨必盥，兼漱口」讲什么？', opts: ['早上要洗脸洗手，还要漱口', '早上要跑步锻炼', '晚上睡前才洗漱'], ans: 0, exp: '起床先洗漱'},
  {q: '7. 「便溺回，辄净手」的「辄」是什么意思？', opts: ['就、马上', '彻底', '停止'], ans: 0, exp: '辄读 zhé，是就'},
  {q: '8. 「夜眠迟」的正确理解是？', opts: ['晚上把该做的事做完，不贪懒', '晚上玩游戏到半夜', '早上赖床不起'], ans: 0, exp: '勤奋不是贪玩'},
  {q: '9. 上完厕所回来，应该？', opts: ['马上把手洗干净', '接着去玩', '先吃东西'], ans: 0, exp: '便后必洗手'},
  {q: '10. 谨这一段总的讲什么？', opts: ['作息规律、讲究卫生，自己管好自己', '怎么考试拿高分', '怎么跟朋友玩'], ans: 0, exp: '谨门开篇'},
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
s = s.replace('《弟子规》第十三课', '《弟子规》第十五课')
s = s.replace('出则悌第五段', '谨第一段')
s = s.replace("window.GUOXUE_COURSE_ID = '553-zun-zhang-qian';", "window.GUOXUE_COURSE_ID = '555-zhao-qi-zao';")
s = s.replace('yaoyue554', 'yaoyue556')

# ---- 校验 ----
for w in ['尊长前', '声要低', '低不闻', '却非宜', '进必趋', '退必迟', '问起对', '视勿移',
          '出则悌第五段', '553-zun-zhang-qian', 'yaoyue554', '第十三课']:
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
