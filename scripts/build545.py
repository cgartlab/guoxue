#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build545: 以 544 课件为模板生成第 545 课《入则孝·亲所好，力为具》。

讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（四句都从「亲」说起）/ 3 亲所好力为具·亲所恶谨为去 /
  4 身有伤贻亲忧·德有伤贻亲羞 / 5 两句合看（力与谨、身与德）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。
区域替换法：讲义区整块换、答疑区整块换、QUIZ 数组整块换、头部 meta 正则换。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/544-shi-sui-xiao/index.html"
DST = ROOT + "/lessons/545-qin-suo-hao/index.html"

TITLE = '入则孝 · 亲所好，力为具，身德不亏 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '亲所好，力为具；身有伤，贻亲忧 · 弟子规课堂'
DESC = ('《弟子规》第五课，入则孝第四段。原文：「亲所好，力为具。亲所恶，谨为去。'
        '身有伤，贻亲忧。德有伤，贻亲羞。」讲两件事：父母喜欢的尽力备办，父母讨厌的'
        '小心避开；自己身上受了伤，父母先忧愁，品行有了亏，父母更羞愧。'
        '前一对讲顺着父母的心意，后一对讲护好自己的身心——孝不只是给吃给穿，'
        '还要不让父母操心、不让父母丢脸。')
OG_DESC = '《弟子规》第五课：亲所好力为具、亲所恶谨为去——顺父母心意；身有伤贻亲忧、德有伤贻亲羞——护好自己。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/545-qin-suo-hao/index.html'

ORIG = '亲所好，力为具。亲所恶，谨为去。身有伤，贻亲忧。德有伤，贻亲羞。'
ORIG_COMMA = '亲所好，力为具，亲所恶，谨为去；身有伤，贻亲忧，德有伤，贻亲羞。'
OLD_ORIG = '事虽小，勿擅为。苟擅为，子道亏。物虽小，勿私藏。苟私藏，亲心伤。'
OLD_ORIG_COMMA = '事虽小，勿擅为，苟擅为，子道亏；物虽小，勿私藏，苟私藏，亲心伤。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('亲所好力为具', ['qīn', 'suǒ', 'hào', 'lì', 'wèi', 'jù'], True)
             + ju('亲所恶谨为去', ['qīn', 'suǒ', 'wù', 'jǐn', 'wèi', 'qù'], False)
             + ju('身有伤贻亲忧', ['shēn', 'yǒu', 'shāng', 'yí', 'qīn', 'yōu'], False)
             + ju('德有伤贻亲羞', ['dé', 'yǒu', 'shāng', 'yí', 'qīn', 'xiū'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">亲所好</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第四段：亲所好，力为具</p><p class="cover-desc">上一段讲管住自己，这一段讲两件事：父母喜欢的、讨厌的，做子女的怎么应对；还有自己身上受了伤、品行有了亏，最难受的其实是父母。四句话里都有一个「亲」字，眼睛始终看着父母。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第四段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>父母喜欢的，尽力去备办；父母讨厌的，小心地去掉。身上受了伤，会让父母忧愁；品行有了亏，会让父母羞愧。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「好」在这里读 hào，是喜欢；「恶」读 wù，是讨厌；「为」读 wèi，是替、给；「具」是备办；「贻」是留给、带给。四句两两成对：前一对说父母的喜好，后一对说自己的身心。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 四句都从「亲」说起</h2><p style="margin:0"><strong>四句话都提到父母</strong><br/>① <strong>亲所好、亲所恶：说的是父母的心意</strong><br/>② <strong>贻亲忧、贻亲羞：说的是父母的忧和羞</strong><br/><br/><strong>一句话：眼睛一直看着父母。</strong></p><p><strong>一进一退</strong><br/>① <strong>好事用「力」：该办的尽力办</strong><br/>② <strong>坏事用「谨」：该避的小心避</strong><br/><br/><strong>一句话：有进有退才叫顺。</strong></p><p><strong>这一课管两处</strong><br/>① <strong>一处是父母的日子过得顺不顺</strong><br/>② <strong>一处是你自己站得正不正</strong><br/><br/><strong>一句话：一顺一护。</strong></p></div>
<!-- 4. 亲所好力为具·亲所恶谨为去 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>亲所好，力为具；亲所恶，谨为去</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>好 hào：喜欢；恶 wù：讨厌</strong><br/>② <strong>为 wèi：替、给；具：备办；去：除去</strong><br/><br/><strong>一句话：喜欢就办，讨厌就避。</strong></p><p><strong>什么叫力为具</strong><br/>① <strong>父母爱吃的、想用的，能办就办到</strong><br/>② <strong>「力」是尽力，不是拼命；尽了心就是孝</strong><br/><br/><strong>一句话：有心有力，就是具。</strong></p><p><strong>什么叫谨为去</strong><br/>① <strong>父母不喜欢的事，小心别去做</strong><br/>② <strong>「谨」是留心，不是害怕</strong><br/><br/><strong>一句话：避开，也是孝。</strong></p></div>
<!-- 5. 身有伤贻亲忧·德有伤贻亲羞 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>身有伤，贻亲忧；德有伤，贻亲羞</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>贻 yí：留给、带给</strong><br/>② <strong>忧：忧愁；羞：羞愧</strong><br/><br/><strong>一句话：伤在自己，痛在父母。</strong></p><p><strong>身有伤，贻亲忧</strong><br/>① <strong>磕了碰了、受凉生病，父母最先着急</strong><br/>② <strong>走路当心、天冷加衣，也是孝顺</strong><br/><br/><strong>一句话：护好身子，就是孝。</strong></p><p><strong>德有伤，贻亲羞</strong><br/>① <strong>说谎、占便宜、对人无礼，父母脸上无光</strong><br/>② <strong>身上伤看得见，德上伤看不见，更难补</strong><br/><br/><strong>一句话：品行不亏，才是大孝。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 力与谨、身与德</h2><p style="margin:0"><strong>前一对管「顺」</strong><br/>① <strong>力：该办的尽力办</strong><br/>② <strong>谨：该避的小心避</strong><br/><br/><strong>一句话：顺着父母的心。</strong></p><p><strong>后一对管「护」</strong><br/>① <strong>身：别让身体受伤，免得父母忧</strong><br/>② <strong>德：别让品行有亏，免得父母羞</strong><br/><br/><strong>一句话：别叫父母操心丢脸。</strong></p><p><strong>合起来一句</strong><br/>① <strong>孝不只是给吃给穿</strong><br/>② <strong>还有不叫父母操心、不叫父母丢脸</strong><br/><br/><strong>一句话：省心，就是孝。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前一对：父母的喜好</strong><br/>① <strong>亲所好，力为具——喜欢的，尽力办</strong><br/>② <strong>亲所恶，谨为去——不喜欢的，小心避</strong><br/><br/><strong>一句话：一办一避，顺着心。</strong></p><p><strong>后一对：自己的身心</strong><br/>① <strong>身有伤，贻亲忧——身子伤了父母忧</strong><br/>② <strong>德有伤，贻亲羞——品行亏了父母羞</strong><br/><br/><strong>一句话：一忧一羞，都在己。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>好则力办，恶则谨避</strong><br/>② <strong>身不妄伤，德不妄亏</strong><br/><br/><strong>一句话：顺心、护身、守德。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>喜欢的尽力办，讨厌的小心避；身不伤，德不亏。</p><p>📖 顺着父母的心</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>父母的心挂着两处：你待他们，你自己。</p><p>💡 两处都稳</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 顺心、护身、守德</p>
<p>这是「弟子规课堂」第五课：入则孝第四段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 父母喜欢的，我做不到怎么办？</h3><p><strong>「力」是尽力，不是全能。</strong><br/><br/>① <strong>做不到就说清楚，别硬撑也别糊弄</strong><br/>② <strong>能办一半办一半，父母要的是你的心</strong><br/>③ <strong>记法：尽力就是孝。</strong></p><h3>❓ 父母不喜欢的事，我觉得没错呢？</h3><p><strong>先避一避，过后慢慢说。</strong><br/><br/>① <strong>当面顶着来，父母更上火</strong><br/>② <strong>等气顺了再讲道理，父母多半会听</strong><br/>③ <strong>大是大非另说，日常小事从父母</strong><br/><br/><strong>记法：先顺后说。</strong></p><h3>❓ 身上受点小伤，父母至于着急吗？</h3><p><strong>在父母眼里没有小伤。</strong><br/><br/>① <strong>你受一分伤，父母担十分心</strong><br/>② <strong>受了伤赶紧说、报个平安，比瞒着强</strong><br/>③ <strong>记法：护身就是孝。</strong></p><h3>❓ 德有伤，怎么就叫父母羞了？</h3><p><strong>孩子是父母的脸面。</strong><br/><br/>① <strong>你在外头的言行，人家看在父母身上</strong><br/>② <strong>一句谎话、一次占便宜，比考砸更伤人</strong><br/>③ <strong>记法：品行正，才是真孝。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 记住父母的好恶</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>爱吃什么、不爱吃什么，怕什么、烦什么</strong>；<strong>记在心里，比问一句更贴心</strong>。</p><p>💡 出门报个平安</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>晚回来先说一声，受了伤当天就说</strong>；<strong>不让父母靠猜，就是护着他们的心</strong>。</p><p>🌱 说话做事想一秒</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>这句谎要不要说，这次便宜要不要占</strong>；<strong>想一想父母的脸面，手就收住了</strong><br/><br/><strong>本课的落点：亲所好，力为具。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第四段。记牢：<strong>亲所好，力为具</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>四句都从「亲」说起 · 顺心意，护身心。<strong>眼睛看着父母</strong>。</p><p>亲所好，力为具 · 喜欢的尽力办。<strong>尽力就是孝</strong>。</p><p>亲所恶，谨为去 · 讨厌的小心避。<strong>先顺后说</strong>。</p><p>身有伤，贻亲忧 · 护好身子。<strong>不叫父母操心</strong>。</p><p>德有伤，贻亲羞 · 品行不亏。<strong>不叫父母丢脸</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第四段，讲顺心护身；下一课讲「亲爱我，孝何难」、「亲有过，谏使更」。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「好」和「恶」在这里各读什么音。② 举一个「德有伤」的例子。③ 今天为父母办一件他喜欢的小事。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「亲所好」的「好」怎么读？', opts: ['hào，喜欢', 'hǎo，好坏', 'hào，好吃'], ans: 0, exp: '好读 hào，是喜欢'},
  {q: '2. 「力为具」的「为」在这里怎么讲？', opts: ['替、给', '因为', '成为'], ans: 0, exp: '为读 wèi，是替'},
  {q: '3. 「亲所好，力为具」是什么意思？', opts: ['父母喜欢的，尽力去备办', '父母喜欢的，随便买点', '自己喜欢什么就做什么'], ans: 0, exp: '尽力备办'},
  {q: '4. 「亲所恶」的「恶」怎么读？', opts: ['wù，讨厌', 'è，坏', 'ě，恶心'], ans: 0, exp: '恶读 wù，是讨厌'},
  {q: '5. 「谨为去」的「去」是什么意思？', opts: ['除去、避开', '走过去', '离开家'], ans: 0, exp: '去掉、避开'},
  {q: '6. 「贻亲忧」的「贻」是什么意思？', opts: ['留给、带给', '送给', '丢掉'], ans: 0, exp: '贻是带给'},
  {q: '7. 身有伤，父母会怎么样？', opts: ['忧愁、着急', '不理会', '让你自己处理'], ans: 0, exp: '贻亲忧'},
  {q: '8. 「德有伤，贻亲羞」说的是什么？', opts: ['品行有亏，父母脸上无光', '衣服破了，父母没面子', '读书不好，父母发愁'], ans: 0, exp: '羞在品行'},
  {q: '9. 「力为具」的「力」是什么意思？', opts: ['尽力，不是拼命', '拼上全部力气', '出钱最多'], ans: 0, exp: '尽心尽力'},
  {q: '10. 这一段总的讲什么？', opts: ['顺着父母的心意，护好自己的身心', '怎么读书做文章', '怎么和朋友相处'], ans: 0, exp: '一顺一护'},
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
s = s.replace('《弟子规》第四课', '《弟子规》第五课')
s = s.replace("window.GUOXUE_COURSE_ID = '544-shi-sui-xiao';", "window.GUOXUE_COURSE_ID = '545-qin-suo-hao';")
s = s.replace('yaoyue545', 'yaoyue546')

# ---- 校验 ----
for w in ['事虽小', '擅为', '子道亏', '私藏', '亲心伤', '544-shi-sui-xiao', 'yaoyue545', '第四课']:
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
