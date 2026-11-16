#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build555: 以 554 课件为模板生成第 555 课《信·凡出言，信为先》。
「信」第一段（开篇），讲说话以守信为先，不撒谎不胡说。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（说话以信用为先）/ 3 凡出言信为先 /
  4 诈与妄奚可焉 / 5 两句合看（答应与不撒谎）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。信门开篇。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/554-shi-zhu-fu/index.html"
DST = ROOT + "/lessons/555-fan-chu-yan/index.html"

TITLE = '信 · 凡出言，信为先，诈与妄，奚可焉 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '凡出言，信为先；诈与妄，奚可焉 · 弟子规课堂'
DESC = ('《弟子规》第十五课，信第一段（开篇）。原文：「凡出言，信为先。诈与妄，奚可焉。」'
        '讲说话以守信为先：开口答应的事就要说到做到；骗人撒谎、瞎说胡说，怎么能行呢？'
        '上一门出则悌已收官，从这一课起开新的一门「信」。')
OG_DESC = '《弟子规》第十五课：凡出言信为先，诈与妄奚可焉。信门开篇。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/555-fan-chu-yan/index.html'

ORIG = '凡出言，信为先。诈与妄，奚可焉。'
ORIG_COMMA = '凡出言，信为先；诈与妄，奚可焉。'
OLD_ORIG = '事诸父，如事父。事诸兄，如事兄。'
OLD_ORIG_COMMA = '事诸父，如事父；事诸兄，如事兄。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('凡出言信为先', ['fán', 'chū', 'yán', 'xìn', 'wéi', 'xiān'], True)
             + ju('诈与妄奚可焉', ['zhà', 'yǔ', 'wàng', 'xī', 'kě', 'yān'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">信为先</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》信第一段：凡出言，信为先</p><p class="cover-desc">出则悌一门已经完结。从这一课起开新的一门「信」——讲怎么说话、怎么守信。第一段就说：开口说话，信用第一；骗人撒谎、瞎说胡说，那怎么能行呢？</p><div class="cover-seal">信</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 信第一段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>凡是开口说话，先把「讲信用」放在最前面。欺骗人、说瞎话，怎么能行呢？</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「凡」是凡是、所有；「言」是说话；「信」是说话算数、守信用；「诈」是骗人；「妄」是说没根据的瞎话；「奚」读 xī，是「怎么」；「焉」是语气词，「奚可焉」就是「怎么能行呢」——是一句反问。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 说话以信用为先</h2><p style="margin:0"><strong>先说「答应」</strong><br/>① <strong>开口答应的事，就是欠下的事</strong><br/>② <strong>说到就要做到</strong><br/><br/><strong>一句话：答应是门平，做到是门真。</strong></p><p><strong>再说「不骗」</strong><br/>① <strong>骗人一次，人家十次不信你</strong><br/>② <strong>瞎话容易说，收场难</strong><br/><br/><strong>一句话：谎话最贵，谁都赔不起。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>说话先想能不能做到</strong><br/>② <strong>做不到的不轻许，做到的说到做到</strong><br/><br/><strong>一句话：话里有信用。</strong></p></div>
<!-- 4. 凡出言，信为先 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>凡出言，信为先</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>凡：凡是、所有；言：说话</strong><br/>② <strong>信：说话算数、守信用</strong><br/><br/><strong>一句话：开口就带上信用。</strong></p><p><strong>凡出言，信为先</strong><br/>① <strong>每一句话出口前，先想能不能做到</strong><br/>② <strong>答应是容易的，做到是要花力气的</strong><br/><br/><strong>一句话：先掂量，再点头。</strong></p><p><strong>为什么先讲「信」</strong><br/>① <strong>人跟人打交道，靠的就是信任</strong><br/>② <strong>信用丢了，说什么都没人听</strong><br/><br/><strong>一句话：信用是立身之本。</strong></p></div>
<!-- 5. 诈与妄，奚可焉 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>诈与妄，奚可焉</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>诈：骗人；妄：瞎说、胡说</strong><br/>② <strong>奚可焉：怎么能行呢（反问）</strong><br/><br/><strong>一句话：骗和胡说，都不行。</strong></p><p><strong>诈与妄，奚可焉</strong><br/>① <strong>骗人换来一时的好处，丢掉的是长久的信任</strong><br/>② <strong>不知道的事瞎说，早晚露馅</strong><br/><br/><strong>一句话：反问语气，就是「坚决不行」。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>做错事说实话，不编瞎话遮掩</strong><br/>② <strong>不知道就说不知道</strong><br/><br/><strong>一句话：老实最省事。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 答应与不撒谎</h2><p style="margin:0"><strong>前一句讲「答应」</strong><br/>① <strong>出言信为先——说到做到</strong><br/>② <strong>答应前先想清楚</strong><br/><br/><strong>一句话：许诺要慎重。</strong></p><p><strong>后一句讲「底线」</strong><br/>① <strong>不骗人、不瞎说，是底线</strong><br/>② <strong>反问语气，是不给商量</strong><br/><br/><strong>一句话：一步不让。</strong></p><p><strong>信门开篇</strong><br/>① <strong>「信」这一门从这四句起头</strong><br/>② <strong>后面还讲怎么说话、怎么听人劝</strong><br/><br/><strong>一句话：先立住「信」字。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 两句一对</h2><p style="margin:0"><strong>前一句：怎么说</strong><br/>① <strong>凡出言，信为先——信用第一</strong><br/>② <strong>说之前先想能不能做到</strong><br/><br/><strong>一句话：先掂量再点头。</strong></p><p><strong>后一句：什么不能说</strong><br/>① <strong>诈——骗人的话不说</strong><br/>② <strong>妄——瞎话、没影的话不传</strong><br/><br/><strong>一句话：反问就是不行。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>答应要慎重，说话不掺假</strong><br/>② <strong>做不到的不许，知道多少说多少</strong><br/><br/><strong>一句话：话里有信用。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>说话信用第一，不骗人不瞎说。</p><p>📖 信为先</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>信用是人立身的根本，丢了就站不住。</p><p>💡 信用是本</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 凡出言，信为先</p>
<p>这是「弟子规课堂」第十五课：信第一段（开篇）。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「信」这一门到底讲什么？</h3><p><strong>讲怎么说话、怎么守信。</strong><br/><br/>① <strong>说话算数，答应的事做到</strong><br/>② <strong>不骗人、不瞎说、不传没影的话</strong><br/>③ <strong>记法：说到要做到。</strong></p><h3>❓ 「诈与妄」是什么意思？</h3><p><strong>两个都不能犯。</strong><br/><br/>① <strong>诈：骗人，编假话糊弄人</strong><br/>② <strong>妄：瞎说，不知道也随口编</strong><br/>③ <strong>记法：不骗不胡说。</strong></p><h3>❓ 答应了又做不到，怎么办？</h3><p><strong>最好的办法在答应之前。</strong><br/><br/>① <strong>答应前先想：我做得来吗？</strong><br/>② <strong>真做不到，赶紧道歉、说明原因</strong><br/>③ <strong>记法：答应前想清楚。</strong></p><h3>❓ 「奚可焉」是什么语气？</h3><p><strong>反问，就是「坚决不行」。</strong><br/><br/>① <strong>奚：怎么；可：可以；焉：呢</strong><br/>② <strong>「怎么能行呢」= 不行，没商量</strong><br/>③ <strong>记法：反问就是「不行」。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 答应的事要做到</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>借了同学的玩具，说好明天还就按时还</strong>；<strong>这就是「凡出言，信为先」</strong>。</p><p>💡 不撒谎</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>做错了事说实话认错，不编瞎话遮掩</strong>；<strong>这就是「诈与妄，奚可焉」</strong>。</p><p>🌱 不知道的不瞎说</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>没听清、没看见的事，别添油加醋传出去</strong>；<strong>老实最省事</strong><br/><br/><strong>本课的落点：凡出言，信为先。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲信第一段，也是「信」这门的开篇。记牢：<strong>凡出言，信为先</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>信门开篇 · 说话以信用为先。<strong>信用是本</strong>。</p><p>凡出言，信为先 · 开口先掂量。<strong>说到要做到</strong>。</p><p>诈与妄，奚可焉 · 不骗不瞎说。<strong>反问就是不行</strong>。</p><p>答应了做不到 · 赶紧道歉说明。<strong>答应前想清楚</strong>。</p><p>老实最省事 · 不用记瞎话。<strong>说话不掺假</strong>。</p><p><strong>在全篇中的位置:</strong>信第一段（开篇）；上一门讲出门在外的孝悌之礼已经收官，这一课起开新的一门「信」，讲怎么说话、怎么守信。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「诈」和「妄」各是什么意思。② 今天答应别人一件事，说到做到。③ 做错事主动说实话认一次错。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「凡出言」的「凡」是什么意思？', opts: ['凡是、所有', '平凡', '烦人'], ans: 0, exp: '凡是凡是、所有'},
  {q: '2. 「信为先」的「信」是什么意思？', opts: ['说话算数、守信用', '相信别人', '写信'], ans: 0, exp: '信是说话算数'},
  {q: '3. 「诈与妄」的「诈」是什么意思？', opts: ['欺骗', '害怕', '爆炸'], ans: 0, exp: '诈是骗人'},
  {q: '4. 「诈与妄」的「妄」是什么意思？', opts: ['瞎说、说没根据的话', '忘记', '奔跑'], ans: 0, exp: '妄是胡说瞎说'},
  {q: '5. 「奚可焉」的「奚」怎么读？', opts: ['xī', 'yàn', 'ào'], ans: 0, exp: '奚读 xī，怎么'},
  {q: '6. 「凡出言，信为先」讲什么？', opts: ['开口说话，守信放在第一位', '先写信再说话', '说话声音要大'], ans: 0, exp: '说话以信为先'},
  {q: '7. 「诈与妄，奚可焉」是什么语气？', opts: ['反问，意思是那样坚决不行', '高兴地夸奖', '问路'], ans: 0, exp: '反问表示不行'},
  {q: '8. 答应了同学明天带书，应该？', opts: ['说到做到，按时带去', '忘了就算了', '再编个理由搪塞'], ans: 0, exp: '说到做到'},
  {q: '9. 不小心打碎了杯子，应该？', opts: ['说实话认错', '怪到小猫身上', '偷偷把碎片藏起来'], ans: 0, exp: '不撒谎'},
  {q: '10. 「信」这一门总的讲什么？', opts: ['怎么说话、怎么守信', '怎么跑步锻炼', '怎么背课文'], ans: 0, exp: '信门讲说话守信'},
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
s = s.replace('《弟子规》第十四课', '《弟子规》第十五课')
s = s.replace('出则悌第六段', '信第一段')
s = s.replace("window.GUOXUE_COURSE_ID = '554-shi-zhu-fu';", "window.GUOXUE_COURSE_ID = '555-fan-chu-yan';")
s = s.replace('yaoyue555', 'yaoyue556')

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
