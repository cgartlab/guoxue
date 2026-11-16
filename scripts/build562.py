#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build562: 以 561 课件（八句版式）为模板生成第 562 课《谨·人问谁，对以名》。
「谨」第八段整段八句：前四句讲报名姓（人问谁、对以名、吾与我、不分明），
后四句讲用物先问（用人物、须明求、倘不问、即为偷）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（说清楚，先征求）/ 3 人问谁对以名·吾与我不分明 /
  4 用人物须明求·倘不问即为偷 / 5 两句合看（报名与明求）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/561-dou-nao-chang/index.html"
DST = ROOT + "/lessons/562-ren-wen-shei/index.html"

TITLE = '谨 · 人问谁，对以名，用人物，须明求 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '人问谁，对以名；用人物，须明求 · 弟子规课堂'
DESC = ('《弟子规》第二十二课，谨第八段。原文：「人问谁，对以名。吾与我，不分明。'
        '用人物，须明求。倘不问，即为偷。」前四句讲报名姓：人家问是谁，要报出名字，'
        '光说「我」「吾」分不清；后四句讲用物有礼：用别人的东西要先明明白白请求，'
        '不问就拿，就跟偷一样。')
OG_DESC = '《弟子规》第二十二课：人问谁对以名，用人物须明求。谨第八段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/562-ren-wen-shei/index.html'

ORIG = '人问谁，对以名。吾与我，不分明。用人物，须明求。倘不问，即为偷。'
ORIG_COMMA = '人问谁，对以名；吾与我，不分明；用人物，须明求；倘不问，即为偷。'
OLD_ORIG = '斗闹场，绝勿近。邪僻事，绝勿问。将入门，问孰存。将上堂，声必扬。'
OLD_ORIG_COMMA = '斗闹场，绝勿近；邪僻事，绝勿问；将入门，问孰存；将上堂，声必扬。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('人问谁对以名', ['rén', 'wèn', 'shuí', 'duì', 'yǐ', 'míng'], True)
             + ju('吾与我不分明', ['wú', 'yǔ', 'wǒ', 'bù', 'fēn', 'míng'], False)
             + ju('用人物须明求', ['yòng', 'rén', 'wù', 'xū', 'míng', 'qiú'], False)
             + ju('倘不问即为偷', ['tǎng', 'bù', 'wèn', 'jí', 'wéi', 'tōu'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">人问谁</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第八段：人问谁，对以名</p><p class="cover-desc">谨门第八段讲两件事：说话说清楚、用东西先征求。人家问是谁就报出名字，光说「我」分不清；用别人的东西要先问一声，不问就拿跟偷一样。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第八段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>人家问「是谁」，要回答出名字；只说「我」啊「吾」啊，分不清是谁。用别人的东西，要先明明白白地说一声；不问一声就拿去用，那就跟偷一样了。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「吾」「我」都是「我」的意思，可光说这个，对方不知道到底是谁，所以要报名。「人物」的「物」指东西；「须」是必须；「明求」是明白地请求；「倘」读 tǎng，是假如；「即」是就。前四句教人说话清楚，后四句教人尊重别人的东西。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 说清楚，先征求</h2><p style="margin:0"><strong>先说「说清楚」</strong><br/>① <strong>人问是谁，就报出名字</strong><br/>② <strong>光说「我」，对方还是不明白</strong><br/><br/><strong>一句话：报名让人清楚。</strong></p><p><strong>再说「先征求」</strong><br/>① <strong>用别人的东西，先问一声</strong><br/>② <strong>不问就拿，跟偷没两样</strong><br/><br/><strong>一句话：尊重别人的东西。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>报名是尊重人，先问是尊重人的物</strong><br/>② <strong>都是替对方着想</strong><br/><br/><strong>一句话：说清楚，先征求。</strong></p></div>
<!-- 4. 人问谁对以名·吾与我不分明 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>人问谁，对以名；吾与我，不分明</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>对：回答；以名：用名字</strong><br/>② <strong>吾、我：都是「我」；分明：清楚</strong><br/><br/><strong>一句话：回答要让人听明白。</strong></p><p><strong>人问谁，对以名</strong><br/>① <strong>来人问「谁呀」，报出自己的名字</strong><br/>② <strong>接电话、敲门也应一声报个名</strong><br/><br/><strong>一句话：报名是礼貌。</strong></p><p><strong>吾与我，不分明</strong><br/>① <strong>光说「我」，对方不知道你是谁</strong><br/>② <strong>说清楚名字，别人才好称呼</strong><br/><br/><strong>一句话：别让人猜。</strong></p></div>
<!-- 5. 用人物须明求·倘不问即为偷 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>用人物，须明求；倘不问，即为偷</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>人物：别人的东西；须：必须</strong><br/>② <strong>明求：明白地请求；倘 tǎng：假如</strong><br/><br/><strong>一句话：先问再用，是规矩。</strong></p><p><strong>用人物，须明求</strong><br/>① <strong>拿别人的东西，先说「我用一下可以吗」</strong><br/>② <strong>得到同意再用，用完及时还</strong><br/><br/><strong>一句话：先问一声。</strong></p><p><strong>倘不问，即为偷</strong><br/>① <strong>不问就拿，跟偷没两样</strong><br/>② <strong>再小的东西也要先打招呼</strong><br/><br/><strong>一句话：不是自己的，别擅自动。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 报名与明求</h2><p style="margin:0"><strong>前四句讲「说清楚」</strong><br/>① <strong>人问是谁，报名字</strong><br/>② <strong>别只说「我」，让人明白</strong><br/><br/><strong>一句话：报名。</strong></p><p><strong>后四句讲「先征求」</strong><br/>① <strong>用别人的东西先问</strong><br/>② <strong>不问就拿，如同偷</strong><br/><br/><strong>一句话：明求。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>来人敲门、接电话，先报自己的名字</strong><br/>② <strong>用同学的东西先问一声，用完还回去</strong><br/><br/><strong>一句话：说清楚，先征求。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：说话清楚</strong><br/>① <strong>人问谁，对以名——报出名字</strong><br/>② <strong>吾与我，不分明——光说我不行</strong><br/><br/><strong>一句话：让人明白。</strong></p><p><strong>后四句：用物先问</strong><br/>① <strong>用人物，须明求——先问一声</strong><br/>② <strong>倘不问，即为偷——不问就拿不对</strong><br/><br/><strong>一句话：先征求。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>问谁报名，别只说「我」</strong><br/>② <strong>用人物件，先问再用</strong><br/><br/><strong>一句话：说清楚，先征求。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>问谁报名字，用东西先问一声。</p><p>📖 说清楚</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>报名是尊重人，先问是尊重人的东西。</p><p>💡 心里有别人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 人问谁，对以名</p>
<p>这是「弟子规课堂」第二十二课：谨第八段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 别人问「谁呀」，为什么不能只说「我」？</h3><p><strong>光说「我」，对方还是不知道你是谁。</strong><br/><br/>① <strong>报出名字，别人才好称呼你</strong><br/>② <strong>报名也是礼貌，让人心里有数</strong><br/>③ <strong>记法：问谁报名，别让人猜。</strong></p><h3>❓ 「吾与我，不分明」是什么意思？</h3><p><strong>「吾」「我」都是「我」，光说分不清。</strong><br/><br/>① <strong>两个词都指自己，听着一样</strong><br/>② <strong>所以要把名字说出来，才清楚</strong><br/>③ <strong>记法：说清楚，别含糊。</strong></p><h3>❓ 用别人的东西为什么要先问？</h3><p><strong>东西是别人的，要先征得同意。</strong><br/><br/>① <strong>先说「我用一下可以吗」</strong><br/>② <strong>得到同意再用，用完及时还</strong><br/>③ <strong>记法：先问一声，再动手。</strong></p><h3>❓ 「倘不问，即为偷」是不是说得太重了？</h3><p><strong>是提醒：再小的东西也要先问。</strong><br/><br/>① <strong>倘读 tǎng，是假如；即是就</strong><br/>② <strong>不问就拿，就是没尊重别人</strong><br/>③ <strong>记法：不是自己的，别擅自拿。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 问谁就报名</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>家里来人、接电话，报出自己的名字</strong>；<strong>这就是「人问谁，对以名」</strong>。</p><p>💡 用东西先问</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>用同学的橡皮、家里人的笔，先说「我用一下可以吗」</strong>；<strong>这就是「用人物，须明求」</strong>。</p><p>🌱 不问就不拿</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>再小的东西，没得到同意就不动</strong>；<strong>这就是「倘不问，即为偷」</strong><br/><br/><strong>本课的落点：说清楚，先征求。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第八段。记牢：<strong>人问谁，对以名</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第八段 · 说清楚，先征求。<strong>心里有别人</strong>。</p><p>人问谁，对以名 · 报出名字。<strong>说明白</strong>。</p><p>吾与我，不分明 · 光说我不行。<strong>别让人猜</strong>。</p><p>用人物，须明求 · 用前先问。<strong>先征求</strong>。</p><p>倘不问，即为偷 · 不问就拿不对。<strong>尊重人物</strong>。</p><p><strong>在全篇中的位置:</strong>谨第八段；上一课讲远离是非和进门有礼，这一课讲报名清楚和用物先问。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「吾」「倘」怎么读。② 有人问你，报出全名不说「我」。③ 今天用别人的东西，先问一声再用。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「人问谁，对以名」的「对」是什么意思？', opts: ['回答', '对着', '正确'], ans: 0, exp: '对是回答'},
  {q: '2. 别人问你是谁，应该怎样回答？', opts: ['报出自己的名字', '只说「我」', '不回答'], ans: 0, exp: '对以名'},
  {q: '3. 「吾与我，不分明」说什么？', opts: ['光说我不分不清是谁', '吾比我大', '两个都不能用'], ans: 0, exp: '要说清名字'},
  {q: '4. 「用人物」的「物」指什么？', opts: ['别人的东西', '动物', '事情'], ans: 0, exp: '物指东西'},
  {q: '5. 「须明求」的「须」是什么意思？', opts: ['必须', '胡须', '等待'], ans: 0, exp: '须是必须'},
  {q: '6. 「倘不问」的「倘」怎么读？', opts: ['tǎng，假如', 'táng，躺', 'chǎng，场'], ans: 0, exp: '倘读 tǎng，是假如'},
  {q: '7. 用别人的东西前应该先做什么？', opts: ['先问一声请求同意', '直接拿', '用完再说'], ans: 0, exp: '须明求'},
  {q: '8. 「倘不问，即为偷」是什么意思？', opts: ['不问就拿跟偷一样', '偷东西要问', '问了才算偷'], ans: 0, exp: '不问就拿不对'},
  {q: '9. 接电话时应该怎样？', opts: ['报出自己的名字', '只说「喂」', '不出声'], ans: 0, exp: '对以名'},
  {q: '10. 这一段总的讲什么？', opts: ['说清楚、用物先征求', '怎么藏东西', '怎么打电话'], ans: 0, exp: '说清楚，先征求'},
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
s = s.replace('《弟子规》第二十一课', '《弟子规》第二十二课')
s = s.replace('谨第七段', '谨第八段')
s = s.replace("window.GUOXUE_COURSE_ID = '561-dou-nao-chang';", "window.GUOXUE_COURSE_ID = '562-ren-wen-shei';")
s = s.replace('yaoyue563', 'yaoyue564')

# ---- 校验 ----
for w in ['斗闹场，绝勿近', '邪僻事，绝勿问', '将入门，问孰存', '将上堂，声必扬',
          '谨第七段', '561-dou-nao-chang', 'yaoyue563', '第二十一课']:
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
