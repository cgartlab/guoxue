#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build549: 以 548 课件为模板生成第 549 课《出则悌·兄道友，弟道恭》。
本课是「出则悌」一门第一段（《弟子规》第二门开篇）。
讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（从家里走出来）/ 3 兄道友弟道恭·兄弟睦孝在中 /
  4 财物轻怨何生·言语忍忿自泯 / 5 两句合看（心与口）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/548-sang-san-nian/index.html"
DST = ROOT + "/lessons/549-xiong-dao-you/index.html"

TITLE = '出则悌 · 兄道友，弟道恭，兄弟睦孝在中 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '兄道友，弟道恭；兄弟睦，孝在中 · 弟子规课堂'
DESC = ('《弟子规》第九课，出则悌第一段，也是「出则悌」一门的开篇。原文：「兄道友，弟道恭。'
        '兄弟睦，孝在中。财物轻，怨何生。言语忍，忿自泯。」讲兄弟姐妹怎么相处：哥哥爱护弟弟，'
        '弟弟尊敬哥哥；兄弟和睦，父母最安心，孝就在里面了。不为一支笔一块橡皮争，怨气就生不出来；'
        '气头上把话放软，火自然就下去了。悌是把家里的敬爱，往外推一步。')
OG_DESC = '《弟子规》第九课：兄道友弟道恭、兄弟睦孝在中、财物轻怨何生、言语忍忿自泯——出则悌开篇。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/549-xiong-dao-you/index.html'

ORIG = '兄道友，弟道恭。兄弟睦，孝在中。财物轻，怨何生。言语忍，忿自泯。'
ORIG_COMMA = '兄道友，弟道恭，兄弟睦，孝在中；财物轻，怨何生，言语忍，忿自泯。'
OLD_ORIG = '丧三年，常悲咽。居处变，酒肉绝。丧尽礼，祭尽诚。事死者，如事生。'
OLD_ORIG_COMMA = '丧三年，常悲咽，居处变，酒肉绝；丧尽礼，祭尽诚，事死者，如事生。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('兄道友弟道恭', ['xiōng', 'dào', 'yǒu', 'dì', 'dào', 'gōng'], True)
             + ju('兄弟睦孝在中', ['xiōng', 'dì', 'mù', 'xiào', 'zài', 'zhōng'], False)
             + ju('财物轻怨何生', ['cái', 'wù', 'qīng', 'yuàn', 'hé', 'shēng'], False)
             + ju('言语忍忿自泯', ['yán', 'yǔ', 'rěn', 'fèn', 'zì', 'mǐn'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">弟道恭</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第一段：兄道友，弟道恭</p><p class="cover-desc">「入则孝」讲的是在家里怎么待父母，「出则悌」讲的是怎么待兄弟姐妹。哥哥爱护弟弟，弟弟尊敬哥哥；兄弟和睦，父母最放心。这一门就从这里开始。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第一段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>做哥哥的要有爱弟之心，做弟弟的要有敬兄之心。兄弟和睦相处，孝就在其中了。看轻钱财物品，怨恨从哪里生出来？说话能克制忍让，火气自然就消失了。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「悌」读 tì，就是敬爱兄长；「道」是本分、该守的道理；「睦」是和睦；「财物」是钱财东西；「忿」读 fèn，是愤怒、火气；「泯」读 mǐn，是消失。前四句讲兄弟相处之道，后四句讲争执从哪里来、怎么消。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 从家里走出来</h2><p style="margin:0"><strong>两门课，两步走</strong><br/>① <strong>入则孝：讲父母，在家里</strong><br/>② <strong>出则悌：讲兄弟姐妹，往外一步</strong><br/><br/><strong>一句话：先孝顺，再友爱。</strong></p><p><strong>这一段讲四件事</strong><br/>① <strong>哥哥要友爱，弟弟要恭敬</strong><br/>② <strong>兄弟和睦，就是孝顺父母</strong><br/><br/><strong>一句话：和气就是孝。</strong></p><p><strong>再讲两个争执的源头</strong><br/>① <strong>财物看轻，怨恨就没处生</strong><br/>② <strong>言语忍住，火气就自己消</strong><br/><br/><strong>一句话：不争钱，不争话。</strong></p></div>
<!-- 4. 兄道友弟道恭·兄弟睦孝在中 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>兄道友，弟道恭；兄弟睦，孝在中</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>悌 tì：敬爱兄长；道：本分</strong><br/>② <strong>友：友爱；恭：恭敬；睦：和睦</strong><br/><br/><strong>一句话：各有各的本分。</strong></p><p><strong>兄道友</strong><br/>① <strong>哥哥先让一步，带着、护着弟弟妹妹</strong><br/>② <strong>不是凶，也不是不管</strong><br/><br/><strong>一句话：大的先有样。</strong></p><p><strong>弟道恭，兄弟睦，孝在中</strong><br/>① <strong>小的听劝，不顶撞；兄弟不吵</strong><br/>② <strong>父母看见孩子和气，心里最安</strong><br/><br/><strong>一句话：兄弟和，就是孝。</strong></p></div>
<!-- 5. 财物轻怨何生·言语忍忿自泯 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>财物轻，怨何生；言语忍，忿自泯</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>轻：看轻、不看重；怨：怨恨</strong><br/>② <strong>忍：克制；忿 fèn：火气；泯 mǐn：消失</strong><br/><br/><strong>一句话：钱上让，话上缓。</strong></p><p><strong>财物轻，怨何生</strong><br/>① <strong>一支笔、一块橡皮、一个玩具，不值得翻脸</strong><br/>② <strong>争得越多，心里的疙瘩越多</strong><br/><br/><strong>一句话：让一让，省一场气。</strong></p><p><strong>言语忍，忿自泯</strong><br/>① <strong>一句狠话顶回去，火就点着了</strong><br/>② <strong>把话放软，说慢一点，火自己就灭</strong><br/><br/><strong>一句话：嘴上一缓，气就下去。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 心与口</h2><p style="margin:0"><strong>前四句讲「心」</strong><br/>① <strong>兄友弟恭，是心里的爱与敬</strong><br/>② <strong>心正了，兄弟自然和睦，孝就在里面</strong><br/><br/><strong>一句话：和从心里来。</strong></p><p><strong>后四句讲「口」和「手」</strong><br/>① <strong>手不争东西，口不逞气话</strong><br/>② <strong>两处一管住，怨和忿就生不出来</strong><br/><br/><strong>一句话：守住嘴和手。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>没有亲兄弟姐妹，堂表、同学一样用</strong><br/>② <strong>悌，就是把对家人的敬爱再推远一步</strong><br/><br/><strong>一句话：出门也照这个来。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一组</h2><p style="margin:0"><strong>前四句：和睦的根本</strong><br/>① <strong>兄道友，弟道恭——各有本分</strong><br/>② <strong>兄弟睦，孝在中——家和即孝</strong><br/><br/><strong>一句话：先有敬爱。</strong></p><p><strong>后四句：争端的源头</strong><br/>① <strong>财物轻，怨何生——不争东西</strong><br/>② <strong>言语忍，忿自泯——不逞气话</strong><br/><br/><strong>一句话：后患先除。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>哥哥带，弟弟敬</strong><br/>② <strong>钱看轻，话放软</strong><br/><br/><strong>一句话：和气，就是孝。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>兄友爱弟恭敬；兄弟和睦就是孝；轻财物、忍言语，怨忿不生。</p><p>📖 和与让</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>把家里的和气当成对父母的孝；把让和忍练成本事。</p><p>💡 孝在中</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 兄弟睦，孝在中</p>
<p>这是「弟子规课堂」第九课：出则悌第一段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 我没有兄弟姐妹，这一课白学了吗？</h3><p><strong>不白学。</strong><br/><br/>① <strong>堂表兄弟姐妹、同学、朋友，都用得上</strong><br/>② <strong>悌是把对家人的敬爱，往外推一步</strong><br/>③ <strong>记法：出门也讲和气。</strong></p><h3>❓ 弟弟妹妹总捣乱，我也要让着吗？</h3><p><strong>让，但要有分寸。</strong><br/><br/>① <strong>小来小去让一让，是爱护</strong><br/>② <strong>碰到危险、破坏东西，要拦，要找大人</strong><br/>③ <strong>记法：兄友是爱护，不是纵容。</strong></p><h3>❓ 「财物轻」是不是钱都不重要？</h3><p><strong>不是不要，是不为小东西伤和气。</strong><br/><br/>① <strong>该分清楚的分清楚，说清楚就好</strong><br/>② <strong>别为一块橡皮，吵一整天</strong><br/>③ <strong>记法：算得清，让得起。</strong></p><h3>❓ 「言语忍」是不是憋着不说？</h3><p><strong>是先把火压住，不是憋成心里堵。</strong><br/><br/>① <strong>气头上先停三秒，别急着顶回去</strong><br/>② <strong>过后好好说出来，别人才听得进</strong><br/>③ <strong>记法：忍住火，不憋住话。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 今天先让一步</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>哥哥姐姐要用东西，先给；弟弟妹妹想玩，先借</strong>；<strong>让一次，你就练了一次「兄友」</strong>。</p><p>💡 气头上停三秒</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>想顶回去的话，先在心里数三下</strong>；<strong>数完还想说，就好好说</strong>。</p><p>🌱 帮父母省一份心</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>兄弟姐妹不吵架，父母就少操一份心</strong>；<strong>这就是「兄弟睦，孝在中」</strong><br/><br/><strong>本课的落点：兄弟睦，孝在中。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第一段。记牢：<strong>兄弟睦，孝在中</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>从家里走出来 · 入则孝讲父母，出则悌讲兄弟。<strong>往外推一步</strong>。</p><p>兄道友，弟道恭 · 大的爱护，小的恭敬。<strong>各有本分</strong>。</p><p>兄弟睦，孝在中 · 兄弟和气，父母最安心。<strong>和气就是孝</strong>。</p><p>财物轻，怨何生 · 不为一支笔翻脸。<strong>让一让，省场气</strong>。</p><p>言语忍，忿自泯 · 话放软，火自己灭。<strong>嘴上一缓</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第一段，第二门开篇；上一门「入则孝」八课已讲完，下一课讲兄弟相处与长幼之礼。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「悌」和「忿」各读什么音。② 今天对兄弟姐妹让一步，说说心里怎么想。③ 想一句气话，把它改成软话。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「出则悌」的「悌」怎么读？', opts: ['tì，敬爱兄长', 'dì，弟弟', 'tí，啼哭'], ans: 0, exp: '悌读 tì'},
  {q: '2. 「兄道友」的「友」是什么意思？', opts: ['友爱、爱护', '朋友', '友好地握手'], ans: 0, exp: '友是友爱'},
  {q: '3. 「弟道恭」的「恭」是什么意思？', opts: ['恭敬', '恭维', '恭喜'], ans: 0, exp: '恭是恭敬'},
  {q: '4. 「兄弟睦」的「睦」是什么意思？', opts: ['和睦、相处得好', '严肃', '忙碌'], ans: 0, exp: '睦是和睦'},
  {q: '5. 为什么说「兄弟睦，孝在中」？', opts: ['兄弟和睦，父母最安心，这就是孝', '兄弟和睦能省钱', '父母看不见兄弟吵架'], ans: 0, exp: '家和即孝'},
  {q: '6. 「财物轻」是什么意思？', opts: ['把钱财东西看轻，不去争', '东西很轻', '轻视别人'], ans: 0, exp: '轻是看轻'},
  {q: '7. 「怨何生」的「怨」是什么？', opts: ['怨恨', '恩惠', '愿望'], ans: 0, exp: '怨是怨恨'},
  {q: '8. 「忿自泯」的「泯」是什么意思？', opts: ['消失、没有了', '抿嘴', '最小'], ans: 0, exp: '泯读 mǐn，消失'},
  {q: '9. 「言语忍」该怎么做？', opts: ['先压住火，再好好说话', '一句话都不说', '大声顶回去'], ans: 0, exp: '忍住火，不憋住话'},
  {q: '10. 这一段总的讲什么？', opts: ['兄弟姐妹要友爱和睦、不争财物、不逞口舌', '怎么分家里的财产', '怎么和同学交朋友'], ans: 0, exp: '和睦、让、忍'},
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
s = s.replace('《弟子规》第八课', '《弟子规》第九课')
s = s.replace('《弟子规》第九课，出则悌第七段', '《弟子规》第九课，出则悌第一段')
s = s.replace("window.GUOXUE_COURSE_ID = '548-sang-san-nian';", "window.GUOXUE_COURSE_ID = '549-xiong-dao-you';")
s = s.replace('yaoyue549', 'yaoyue550')

# ---- 校验 ----
for w in ['丧三年', '常悲咽', '居处变', '酒肉绝', '丧尽礼', '祭尽诚', '事死者', '如事生',
          '入则孝第七段', '入则孝收官', '548-sang-san-nian', 'yaoyue549', '第八课']:
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
