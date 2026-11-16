#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build564: 以 562 课件（八句版式）为模板生成第 564 课《信·凡出言，信为先》。
「信」第一段（开篇）整段八句：前四句讲说话要守信、不欺诈（凡出言、信为先、诈与妄、奚可焉），
后四句讲话不在多、要说得对（话说多、不如少、惟其是、勿佞巧）。
讲义 8 页（原文页在第 2 页），ruby=24；测验 12 页、答疑 4 页，总 24 页。付费课。
信门开篇。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/562-ren-wen-shei/index.html"
DST = ROOT + "/lessons/564-fan-chu-yan/index.html"

TITLE = '信 · 凡出言，信为先，话说多，不如少 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '凡出言，信为先；话说多，不如少 · 弟子规课堂'
DESC = ('《弟子规》第二十四课，信第一段（开篇）。原文：「凡出言，信为先。诈与妄，奚可焉。'
        '话说多，不如少。惟其是，勿佞巧。」前四句讲开口先把信放在第一位，欺诈骗人的话怎么可以；'
        '后四句讲话不在多而在对，说话要实在，不花言巧语。信门开篇。')
OG_DESC = '《弟子规》第二十四课：凡出言信为先，话说多不如少。信门开篇。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/564-fan-chu-yan/index.html'

ORIG = '凡出言，信为先。诈与妄，奚可焉。话说多，不如少。惟其是，勿佞巧。'
ORIG_COMMA = '凡出言，信为先；诈与妄，奚可焉；话说多，不如少；惟其是，勿佞巧。'
OLD_ORIG = '人问谁，对以名。吾与我，不分明。用人物，须明求。倘不问，即为偷。'
OLD_ORIG_COMMA = '人问谁，对以名；吾与我，不分明；用人物，须明求；倘不问，即为偷。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('凡出言信为先', ['fán', 'chū', 'yán', 'xìn', 'wéi', 'xiān'], True)
             + ju('诈与妄奚可焉', ['zhà', 'yǔ', 'wàng', 'xī', 'kě', 'yān'], False)
             + ju('话说多不如少', ['huà', 'shuō', 'duō', 'bù', 'rú', 'shǎo'], False)
             + ju('惟其是勿佞巧', ['wéi', 'qí', 'shì', 'wù', 'nìng', 'qiǎo'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">凡出言</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》信第一段：凡出言，信为先</p><p class="cover-desc">信门的开篇。开口说话，先把「信」放在第一位；欺人的话、虚假的话，万万不可以。话说得多不如说得少、说得对——话要实在，不耍花言巧语。</p><div class="cover-seal">信</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 信第一段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>凡是开口说话，首先要讲信用；欺骗、虚妄的话，怎么可以说呢？话说得多，不如说得少；说话要实在正确，不要花言巧语。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「信」是信用、诚实；「诈」读 zhà，是欺骗；「妄」读 wàng，是虚妄、不实；「奚」读 xī，是怎么、哪里；「惟」读 wéi，是只、只要；「是」是对、正确；「佞」读 nìng，是巧言谄媚；「佞巧」就是花言巧语。这一段是「信」门的开篇：说话先守信，话要少而真。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 说话守信，说对话</h2><p style="margin:0"><strong>先说「守信」</strong><br/>① <strong>开口第一件事，是让人信得过</strong><br/>② <strong>骗人的话，一句都不可以说</strong><br/><br/><strong>一句话：说话算数。</strong></p><p><strong>再说「说对」</strong><br/>① <strong>话不在多，贵在说到位</strong><br/>② <strong>实实在在，不耍嘴皮子</strong><br/><br/><strong>一句话：少而真。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>信门开篇，先管住自己的嘴</strong><br/>② <strong>守信 + 说真话，是做人的根</strong><br/><br/><strong>一句话：开口见人品。</strong></p></div>
<!-- 4. 凡出言信为先·诈与妄奚可焉 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>凡出言，信为先；诈与妄，奚可焉</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>信：信用；为先：放在第一位</strong><br/>② <strong>诈 zhà：骗；妄 wàng：不实；奚 xī：怎么</strong><br/><br/><strong>一句话：开口先想「真不真」。</strong></p><p><strong>凡出言，信为先</strong><br/>① <strong>答应别人的事，就要做到</strong><br/>② <strong>说出口的话，让人信得过</strong><br/><br/><strong>一句话：说话算数。</strong></p><p><strong>诈与妄，奚可焉</strong><br/>① <strong>骗人的话、夸大的话，都不可以说</strong><br/>② <strong>一次撒谎，就要用更多谎去圆</strong><br/><br/><strong>一句话：假话一句都别开口。</strong></p></div>
<!-- 5. 话说多不如少·惟其是勿佞巧 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>话说多，不如少；惟其是，勿佞巧</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>惟 wéi：只要；是：对、正确</strong><br/>② <strong>佞 nìng 巧：花言巧语</strong><br/><br/><strong>一句话：话要少，更要对。</strong></p><p><strong>话说多，不如少</strong><br/>① <strong>话多容易出错，也说不到点上</strong><br/>② <strong>想清楚再说，一句顶一句</strong><br/><br/><strong>一句话：少说，说到位。</strong></p><p><strong>惟其是，勿佞巧</strong><br/>① <strong>只要说得对、说得实在</strong><br/>② <strong>不靠甜言蜜语讨人喜欢</strong><br/><br/><strong>一句话：真话最有分量。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 真与少</h2><p style="margin:0"><strong>前四句讲「真」</strong><br/>① <strong>说话守信，不骗不妄</strong><br/>② <strong>真，是让人信得过</strong><br/><br/><strong>一句话：不说假话。</strong></p><p><strong>后四句讲「少」</strong><br/>① <strong>话不在多，贵在说对</strong><br/>② <strong>实在，不耍花腔</strong><br/><br/><strong>一句话：不说废话。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>答应同学的事做到，做不到就先别说</strong><br/>② <strong>发言想清楚再说，不抢话不吹牛</strong><br/><br/><strong>一句话：开口见人品。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：说话要守信</strong><br/>① <strong>凡出言，信为先——开口先守信</strong><br/>② <strong>诈与妄，奚可焉——假话不可说</strong><br/><br/><strong>一句话：真。</strong></p><p><strong>后四句：话要少而真</strong><br/>① <strong>话说多，不如少——话多不如话少</strong><br/>② <strong>惟其是，勿佞巧——要对不要花</strong><br/><br/><strong>一句话：准。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>开口讲信用，假话不说</strong><br/>② <strong>话少说得对，不耍嘴皮</strong><br/><br/><strong>一句话：真话、少话、对话。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>说话要守信，不骗人；话要少而真。</p><p>📖 守信</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>信是做人的根，开口见人品。</p><p>💡 言而有信</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 凡出言，信为先</p>
<p>这是「弟子规课堂」第二十四课：信第一段（开篇）。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 为什么说话要把「信」放在第一位？</h3><p><strong>因为说话算数，别人才信你。</strong><br/><br/>① <strong>答应了就做到，做不到的先别答应</strong><br/>② <strong>一次守信，攒一分信任</strong><br/>③ <strong>记法：开口之前，先想做不做得到。</strong></p><h3>❓ 「诈与妄」是什么意思？</h3><p><strong>骗人的话和不实的话。</strong><br/><br/>① <strong>诈读 zhà，是欺骗；妄读 wàng，是虚妄</strong><br/>② <strong>撒一个谎，要用更多谎去圆，越陷越深</strong><br/>③ <strong>记法：假话一句都别说。</strong></p><h3>❓ 「话说多，不如少」是叫人少说话吗？</h3><p><strong>不是不说话，是别说废话。</strong><br/><br/>① <strong>话多容易说错，也说不到点上</strong><br/>② <strong>想清楚再说，一句顶一句</strong><br/>③ <strong>记法：话不在多，说到点上。</strong></p><h3>❓ 「惟其是，勿佞巧」怎么理解？</h3><p><strong>只要说得对，不耍花言巧语。</strong><br/><br/>① <strong>惟是只要，是是对；佞读 nìng</strong><br/>② <strong>靠甜言蜜语讨好，不如一句实在话</strong><br/>③ <strong>记法：真话最有分量。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 答应了就做到</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>答应同学带书，就别忘；做不到先别答应</strong>；<strong>这就是「凡出言，信为先」</strong>。</p><p>💡 不说假话</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>没做的事不吹牛，错了就老实承认</strong>；<strong>这就是「诈与妄，奚可焉」</strong>。</p><p>🌱 想清楚再说</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>发言说到点上，不抢话、不耍嘴皮</strong>；<strong>这就是「话说多，不如少」</strong><br/><br/><strong>本课的落点：开口见人品。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲信第一段，也是信门的开篇。记牢：<strong>凡出言，信为先</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>信门开篇 · 开口见人品。<strong>言而有信</strong>。</p><p>凡出言，信为先 · 说话先守信。<strong>说话算数</strong>。</p><p>诈与妄，奚可焉 · 假话不可说。<strong>不骗不妄</strong>。</p><p>话说多，不如少 · 话少说得对。<strong>不说废话</strong>。</p><p>惟其是，勿佞巧 · 要实在不花巧。<strong>真话最重</strong>。</p><p><strong>在全篇中的位置:</strong>信第一段（开篇）；谨门讲完了日常小节，这一门讲说话守信，从开口第一句教起。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「诈」「妄」「佞」怎么读。② 今天答应的一件事，一定做到。③ 发言前先想清楚，说一句实在话。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「凡出言，信为先」的「信」是什么意思？', opts: ['信用、诚实', '信件', '相信别人'], ans: 0, exp: '信是信用诚实'},
  {q: '2. 开口说话，应该先讲什么？', opts: ['信用', '声音大', '说得快'], ans: 0, exp: '信为先'},
  {q: '3. 「诈与妄」的「诈」怎么读？', opts: ['zhà，欺骗', 'zhá，扎', 'zuò，做'], ans: 0, exp: '诈读 zhà，是欺骗'},
  {q: '4. 「妄」是什么意思？', opts: ['虚妄、不实', '忘记', '盼望'], ans: 0, exp: '妄是不实'},
  {q: '5. 「奚可焉」的「奚」是什么意思？', opts: ['怎么、哪里', '拖延', '高兴'], ans: 0, exp: '奚读 xī，是怎么'},
  {q: '6. 「话说多，不如少」告诉我们什么？', opts: ['话不在多，贵在说对', '一句话都不说', '说得越多越好'], ans: 0, exp: '话少而真'},
  {q: '7. 「惟其是」的「是」是什么意思？', opts: ['对、正确', '是不是', '这样'], ans: 0, exp: '是对、正确'},
  {q: '8. 「勿佞巧」的「佞」怎么读？', opts: ['nìng', 'nín', 'qiàn'], ans: 0, exp: '佞读 nìng'},
  {q: '9. 「佞巧」指什么？', opts: ['花言巧语', '声音好听', '写字漂亮'], ans: 0, exp: '佞巧是花言巧语'},
  {q: '10. 这一段总的讲什么？', opts: ['说话要守信、说真话', '怎么多说话', '怎么讨好人'], ans: 0, exp: '开口见人品'},
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
s = s.replace('《弟子规》第二十二课', '《弟子规》第二十四课')
s = s.replace('谨第八段', '信第一段')
s = s.replace("window.GUOXUE_COURSE_ID = '562-ren-wen-shei';", "window.GUOXUE_COURSE_ID = '564-fan-chu-yan';")
s = s.replace('yaoyue564', 'yaoyue566')

# ---- 校验 ----
for w in ['人问谁，对以名', '吾与我，不分明', '用人物，须明求', '倘不问，即为偷',
          '谨第八段', '562-ren-wen-shei', 'yaoyue564', '第二十二课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
expect = {'slide': s.count('class="slide'), 'ruby': s.count('<ruby'), 'rt': s.count('<rt>'),
          'quiz': s.count("{q: '"), 'page_max': len(re.findall(r'data-page="', s))}
if expect['slide'] != 26 or expect['ruby'] != 24 or expect['rt'] != 24 or expect['quiz'] != 10 or expect['page_max'] != 24:
    print('[FAIL] 结构计数不符（slide 含 viewport/container 两个前缀，应为 24 页 + 2；原文 4 行 24 字，ruby 应为 24）:', expect)
    sys.exit(1)
print('[OK] 结构计数:', expect)
print('[OK] 章节锚点: 讲义区 %d→%d, 答疑区 %d→%d' % (i1, i2, j1, j2))

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(s)
print('[OK] 已生成', DST)
