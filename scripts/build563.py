#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build563: 以 562 课件为模板，套 554 两句版式，生成第 563 课《谨·借人物，及时还》。
「谨」第九段（收官），仅两句：借了及时还，急用时才借得到。
讲义 8 页（原文页在第 2 页），ruby=12；测验 12 页、答疑 4 页，总 24 页。付费课。
谨门至此收官。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/562-ren-wen-shei/index.html"
DST = ROOT + "/lessons/563-jie-ren-wu/index.html"

TITLE = '谨 · 借人物，及时还，后有急，借不难 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '借人物，及时还；后有急，借不难 · 弟子规课堂'
DESC = ('《弟子规》第二十三课，谨第九段（收官）。原文：「借人物，及时还。后有急，借不难。」'
        '借了别人的东西，用完及时归还；这样以后有急用再借，人家才愿意借给你。'
        '还东西讲信用，是谨门最后教的一课。谨门至此完结。')
OG_DESC = '《弟子规》第二十三课：借人物及时还，后有急借不难。谨门收官。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/563-jie-ren-wu/index.html'

ORIG = '借人物，及时还。后有急，借不难。'
ORIG_COMMA = '借人物，及时还；后有急，借不难。'
OLD_ORIG = '人问谁，对以名。吾与我，不分明。用人物，须明求。倘不问，即为偷。'
OLD_ORIG_COMMA = '人问谁，对以名；吾与我，不分明；用人物，须明求；倘不问，即为偷。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('借人物及时还', ['jiè', 'rén', 'wù', 'jí', 'shí', 'huán'], True)
             + ju('后有急借不难', ['hòu', 'yǒu', 'jí', 'jiè', 'bù', 'nán'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">借人物</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第九段：借人物，及时还</p><p class="cover-desc">谨门的收官一段。借了别人的东西，用完就及时还；还得快、还得守信用，以后自己有急用再开口，人家才乐意借。一个「还」字，攒的是信用。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第九段（收官）</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>借了别人的东西，用完了就及时归还；以后自己有了急用再借，人家就不会推辞。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「人物」指别人的东西；「及时」是马上、不拖延；「还」读 huán，是归还；「后」是以后；「急」是急用；「难」是借不到。借东西是常事，还不还是人品：还得快，信用就在；拖着不还，下次就没人敢借。谨门到这里收官。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 借了就还，再借不难</h2><p style="margin:0"><strong>先看「及时还」</strong><br/>① <strong>用完就还，不拖不欠</strong><br/>② <strong>东西完好，当面还回去</strong><br/><br/><strong>一句话：还东西要快。</strong></p><p><strong>再看「借不难」</strong><br/>① <strong>守信用的人，人家愿意借</strong><br/>② <strong>有急用时，别人才肯帮忙</strong><br/><br/><strong>一句话：信用是攒出来的。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>这一次还得快，下一次借得顺</strong><br/>② <strong>谨门收官，落在「守信」两个字</strong><br/><br/><strong>一句话：还得快，借得来。</strong></p></div>
<!-- 4. 借人物，及时还 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>借人物，及时还</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>人物：别人的东西；还 huán：归还</strong><br/>② <strong>及时：马上、不拖延</strong><br/><br/><strong>一句话：借了就要还。</strong></p><p><strong>借人物，及时还</strong><br/>① <strong>用完就还，说好的日子别忘了</strong><br/>② <strong>东西保持原样，不弄坏不弄丢</strong><br/><br/><strong>一句话：借得快，还得也快。</strong></p><p><strong>为什么及时</strong><br/>① <strong>人家也有要用的时候</strong><br/>② <strong>拖久了，信用就没了</strong><br/><br/><strong>一句话：还的是东西，攒的是信用。</strong></p></div>
<!-- 5. 后有急，借不难 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>后有急，借不难</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>后：以后；急：急用</strong><br/>② <strong>难：借不到、被推辞</strong><br/><br/><strong>一句话：信用管以后。</strong></p><p><strong>后有急，借不难</strong><br/>① <strong>这次按时还，下次开口人家放心</strong><br/>② <strong>真遇到急事，别人愿意帮</strong><br/><br/><strong>一句话：守信的人，路越走越宽。</strong></p><p><strong>反过来想</strong><br/>① <strong>借了拖着不还，谁还敢借</strong><br/>② <strong>一次失信，以后就难开口</strong><br/><br/><strong>一句话：别让一次拖欠，堵了以后的路。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 还与借</h2><p style="margin:0"><strong>前一句讲「还」</strong><br/>① <strong>借了及时还，不拖不欠</strong><br/>② <strong>这是眼前的本分</strong><br/><br/><strong>一句话：及时还。</strong></p><p><strong>后一句讲「借」</strong><br/>① <strong>有信用，以后借不难</strong><br/>② <strong>这是长远的好处</strong><br/><br/><strong>一句话：借得来。</strong></p><p><strong>谨门收官</strong><br/>① <strong>从晨起盥漱，到借物及时还</strong><br/>② <strong>谨，就是把每件小事做到位</strong><br/><br/><strong>一句话：小事守信，是大修养。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 两句一对</h2><p style="margin:0"><strong>前一句：及时还</strong><br/>① <strong>借人物，及时还——用完就归还</strong><br/>② <strong>不拖、不欠、不弄坏</strong><br/><br/><strong>一句话：还得快。</strong></p><p><strong>后一句：借不难</strong><br/>① <strong>后有急，借不难——急用时借得到</strong><br/>② <strong>信用好，人家肯帮</strong><br/><br/><strong>一句话：借得来。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>借了就还，别让人等</strong><br/>② <strong>守住信用，急有人帮</strong><br/><br/><strong>一句话：还得快，借得来。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>借了东西及时还，急用再借就不难。</p><p>📖 守信</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>还得快是守信，借得来是信用带来的方便。</p><p>💡 信用是攒的</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 借人物，及时还</p>
<p>这是「弟子规课堂」第二十三课：谨第九段（收官）。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「借人物」的「人物」是什么意思？</h3><p><strong>别人的东西。</strong><br/><br/>① <strong>「人」是别人，「物」是东西</strong><br/>② <strong>文具、书本、玩具都算</strong><br/>③ <strong>记法：别人的东西，借了要还。</strong></p><h3>❓ 为什么借了要「及时」还？</h3><p><strong>人家也有要用的时候。</strong><br/><br/>① <strong>用完就还，说好的日子不拖延</strong><br/>② <strong>拖久了，人家不好开口要，信用也没了</strong><br/>③ <strong>记法：借得快，还得也快。</strong></p><h3>❓ 「后有急，借不难」怎么理解？</h3><p><strong>这次守信，下次才好借。</strong><br/><br/>① <strong>按时还的人，人家放心再借</strong><br/>② <strong>真有急事，别人愿意帮</strong><br/>③ <strong>记法：信用是攒出来的。</strong></p><h3>❓ 谨门讲完了，到底讲了什么？</h3><p><strong>把日常小事一件件做到位。</strong><br/><br/>① <strong>从早起梳洗、穿戴吃饭，到走路坐卧、借物还物</strong><br/>② <strong>最后落在「守信」上——借了就还</strong><br/>③ <strong>记法：谨，就是小事不马虎。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 借东西先说清</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>借同学的文具，先问一声、说好什么时候还</strong>；<strong>先打招呼，再借用</strong>。</p><p>💡 用完及时还</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>用完当天就还回去，东西保持原样</strong>；<strong>这就是「借人物，及时还」</strong>。</p><p>🌱 攒下信用</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>每次都按时还，下次有急用，同学乐意借</strong>；<strong>这就是「后有急，借不难」</strong><br/><br/><strong>本课的落点：还得快，借得来。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第九段，也是谨门的收官一段。记牢：<strong>借人物，及时还</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨门收官 · 落在守信两个字。<strong>小事不马虎</strong>。</p><p>借人物，及时还 · 用完就归还。<strong>还得快</strong>。</p><p>后有急，借不难 · 信用好借得到。<strong>借得来</strong>。</p><p>不拖不欠 · 东西保持原样。<strong>守信用</strong>。</p><p>谨门全程 · 从晨起到借还，件件做到位。<strong>养成习惯</strong>。</p><p><strong>在全篇中的位置:</strong>谨第九段（收官）；上一课讲报名清楚、用物先问，这一课讲借了及时还，谨门至此完结，下一课开新的一门。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「还」读什么音。② 今天借了东西，用完当天就还。③ 下次借东西，说好归还的日子。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「借人物」的「人物」是什么意思？', opts: ['别人的东西', '有名的人', '人物画'], ans: 0, exp: '人物指别人的东西'},
  {q: '2. 「及时还」的「还」怎么读？', opts: ['huán', 'hái', 'xuán'], ans: 0, exp: '还读 huán，是归还'},
  {q: '3. 「借人物，及时还」讲什么？', opts: ['借了东西用完就还', '借了不用还', '东西借了就送人'], ans: 0, exp: '及时归还'},
  {q: '4. 为什么借了要及时还？', opts: ['人家也有要用的时侯，信用也要紧', '东西放着好看', '还了还能再借坏处'], ans: 0, exp: '为别人着想、守信用'},
  {q: '5. 「后有急」的「急」是什么意思？', opts: ['急用、着急的事', '快点', '生病'], ans: 0, exp: '急是急用'},
  {q: '6. 「借不难」是什么意思？', opts: ['借得到，不被推辞', '借东西很难', '不借钱'], ans: 0, exp: '借不难是借得到'},
  {q: '7. 怎样才能「后有急，借不难」？', opts: ['每次借了都按时还', '多借少还', '借了装忘'], ans: 0, exp: '守信才借得到'},
  {q: '8. 借同学的东西，用完应该怎样？', opts: ['及时还回去，保持原样', '拖着不还', '随便丢给他'], ans: 0, exp: '及时归还'},
  {q: '9. 借东西前应该先做什么？', opts: ['先问一声、说好归还时间', '直接拿走', '偷偷用'], ans: 0, exp: '须明求'},
  {q: '10. 谨门这一门总的教什么？', opts: ['把日常小事一件件做到位', '怎么考高分', '怎么挣大钱'], ans: 0, exp: '谨门收官'},
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
s = s.replace('《弟子规》第二十二课', '《弟子规》第二十三课')
s = s.replace('谨第八段', '谨第九段')
s = s.replace("window.GUOXUE_COURSE_ID = '562-ren-wen-shei';", "window.GUOXUE_COURSE_ID = '563-jie-ren-wu';")
s = s.replace('yaoyue564', 'yaoyue565')

# ---- 校验 ----
for w in ['人问谁，对以名', '吾与我，不分明', '用人物，须明求', '倘不问，即为偷',
          '谨第八段', '562-ren-wen-shei', 'yaoyue564', '第二十二课']:
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
