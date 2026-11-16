#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build546: 以 545 课件为模板生成第 546 课《入则孝·亲爱我，孝何难》。

讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（三种情形）/ 3 亲爱我孝何难·亲憎我孝方贤 /
  4 亲有过谏使更·怡吾色柔吾声 / 5 两句合看（难处与劝法）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。
本课是「弟子规课堂」第一课收费（前五课 541-545 免费）。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/545-qin-suo-hao/index.html"
DST = ROOT + "/lessons/546-qin-ai-wo/index.html"

TITLE = '入则孝 · 亲爱我，孝何难，谏使更 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '亲爱我，孝何难；亲有过，谏使更 · 弟子规课堂'
DESC = ('《弟子规》第六课，入则孝第五段。原文：「亲爱我，孝何难。亲憎我，孝方贤。'
        '亲有过，谏使更。怡吾色，柔吾声。」讲两层：父母疼我，孝顺不算难；父母不疼我，'
        '还能尽孝，才见修养。父母有了过错，做子女的要劝，但劝要有法子——脸色和缓、'
        '声音柔和，让父母听得进去、改得过来。顺境不骄、逆境不冷、劝不顶撞，敬字贯穿到底。')
OG_DESC = '《弟子规》第六课：亲爱我孝何难、亲憎我孝方贤——顺逆都要孝；亲有过谏使更、怡吾色柔吾声——劝要气和声柔。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/546-qin-ai-wo/index.html'

ORIG = '亲爱我，孝何难。亲憎我，孝方贤。亲有过，谏使更。怡吾色，柔吾声。'
ORIG_COMMA = '亲爱我，孝何难，亲憎我，孝方贤；亲有过，谏使更，怡吾色，柔吾声。'
OLD_ORIG = '亲所好，力为具。亲所恶，谨为去。身有伤，贻亲忧。德有伤，贻亲羞。'
OLD_ORIG_COMMA = '亲所好，力为具，亲所恶，谨为去；身有伤，贻亲忧，德有伤，贻亲羞。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('亲爱我孝何难', ['qīn', 'ài', 'wǒ', 'xiào', 'hé', 'nán'], True)
             + ju('亲憎我孝方贤', ['qīn', 'zēng', 'wǒ', 'xiào', 'fāng', 'xián'], False)
             + ju('亲有过谏使更', ['qīn', 'yǒu', 'guò', 'jiàn', 'shǐ', 'gēng'], False)
             + ju('怡吾色柔吾声', ['yí', 'wú', 'sè', 'róu', 'wú', 'shēng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">孝方贤</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第五段：亲爱我，孝何难</p><p class="cover-desc">上一段讲顺着父母的心、护好自己的身子，这一段讲更难的情形：父母待你不好时怎么孝，父母有了过错又怎么劝。四句话先论难易，再论法子——顺境里的孝是本分，逆境里的孝才是修养。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第五段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>父母疼爱我，孝顺有什么难呢？父母不喜爱我，还能尽孝，那才算得上好。父母有了过错，要劝他改正；劝的时候脸色要温和，声音要柔和。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「憎」是厌恶、不喜爱；「方」是才；「贤」是好、有德行；「过」是过错；「谏」是规劝；「更」读 gēng，是改正；「怡」是温和、和悦。四句两两成对：前一对论难易，后一对论劝法。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 三种情形</h2><p style="margin:0"><strong>四句讲三种情形</strong><br/>① <strong>父母爱我：孝不难，是顺境</strong><br/>② <strong>父母憎我：还肯孝，才是贤</strong><br/><br/><strong>一句话：顺境看不出深浅。</strong></p><p><strong>第三种最难</strong><br/>① <strong>父母有过：做子女的要劝</strong><br/>② <strong>劝还要有法子：气和、声柔</strong><br/><br/><strong>一句话：劝得进去才叫劝。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>顺的时候孝，是常情</strong><br/>② <strong>逆的时候孝、父母有错还能劝好，是本事</strong><br/><br/><strong>一句话：越难越见心。</strong></p></div>
<!-- 4. 亲爱我孝何难·亲憎我孝方贤 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>亲爱我，孝何难；亲憎我，孝方贤</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>憎 zēng：厌恶、不喜爱</strong><br/>② <strong>方：才；贤：好、有德行</strong><br/><br/><strong>一句话：难处做到，才叫贤。</strong></p><p><strong>亲爱我，孝何难</strong><br/>① <strong>父母疼你，孝顺是顺着走，不费劲</strong><br/>② <strong>「何难」是说这不算本事，别当成功劳</strong><br/><br/><strong>一句话：顺境里的孝，是本分。</strong></p><p><strong>亲憎我，孝方贤</strong><br/>① <strong>父母不待见你，还肯尽孝，才见修养</strong><br/>② <strong>不是忍气吞声，是不改做子女的本分</strong><br/><br/><strong>一句话：心不冷，孝不断。</strong></p></div>
<!-- 5. 亲有过谏使更·怡吾色柔吾声 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>亲有过，谏使更；怡吾色，柔吾声</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>过：过错；谏 jiàn：规劝</strong><br/>② <strong>更 gēng：改正；怡：和悦；柔：柔和</strong><br/><br/><strong>一句话：劝父母改，态度要好。</strong></p><p><strong>什么叫谏使更</strong><br/>① <strong>父母做得不对，做子女的要劝</strong><br/>② <strong>劝只有一个目的：让他改，不是让他难堪</strong><br/><br/><strong>一句话：为改而劝，不为赢而劝。</strong></p><p><strong>怡吾色，柔吾声</strong><br/>① <strong>脸色和缓，声音放低</strong><br/>② <strong>板着脸、提高声，道理再对也听不进</strong><br/><br/><strong>一句话：好话要好声说。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 难处与劝法</h2><p style="margin:0"><strong>前两句讲「难」</strong><br/>① <strong>顺境孝易，逆境孝难</strong><br/>② <strong>难在父母不给好脸时，你还不冷心</strong><br/><br/><strong>一句话：逆境看定力。</strong></p><p><strong>后两句讲「法」</strong><br/>① <strong>劝父母是分内事，怎么劝是本事</strong><br/>② <strong>气和声柔，是给父母留面子</strong><br/><br/><strong>一句话：有法才劝得动。</strong></p><p><strong>合起来一句</strong><br/>① <strong>孝不是一味顺从，也不是当面顶撞</strong><br/>② <strong>顺里有劝，劝里有敬</strong><br/><br/><strong>一句话：敬字贯穿到底。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前一对：论难易</strong><br/>① <strong>亲爱我，孝何难——顺境别自满</strong><br/>② <strong>亲憎我，孝方贤——逆境才见人</strong><br/><br/><strong>一句话：难易之间见真心。</strong></p><p><strong>后一对：论劝法</strong><br/>① <strong>亲有过，谏使更——该劝就劝</strong><br/>② <strong>怡吾色，柔吾声——劝要软着来</strong><br/><br/><strong>一句话：劝得进去才算数。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>顺不骄，逆不冷</strong><br/>② <strong>劝不顶，声不硬</strong><br/><br/><strong>一句话：敬在心里，柔在脸上。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>父母疼我孝不难；不疼我还孝；父母有错，柔声劝改。</p><p>📖 顺逆都孝</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>孝不看父母待我如何，只看我做到没有。</p><p>💡 只看自己</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 顺不骄、逆不冷、劝不顶</p>
<p>这是「弟子规课堂」第六课：入则孝第五段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 父母偏心、待我不好，还要孝吗？</h3><p><strong>孝是自己的本分。</strong><br/><br/>① <strong>父母的偏心你改不了，自己的本分你能守</strong><br/>② <strong>心不冷，日子久了父母看得见</strong><br/>③ <strong>记法：不拿父母的态度当条件。</strong></p><h3>❓ 劝父母，会不会被说不孝？</h3><p><strong>劝是分内的事。</strong><br/><br/>① <strong>古书里明写「亲有过，谏使更」</strong><br/>② <strong>劝不是驳面子，是怕父母走错路</strong><br/>③ <strong>记法：不劝才是不负责。</strong></p><h3>❓ 父母根本不听，还劝吗？</h3><p><strong>先缓一缓，别硬顶。</strong><br/><br/>① <strong>气头上说什么都进不去</strong><br/>② <strong>换个时候、换个说法再来</strong><br/>③ <strong>记法：不硬碰，不放弃。</strong></p><h3>❓ 「怡吾色，柔吾声」是不是要装？</h3><p><strong>是修养，不是装。</strong><br/><br/>① <strong>脸色和声音，父母最先感觉得到</strong><br/>② <strong>心里真敬，脸自然就软</strong><br/>③ <strong>记法：先顺气，再讲理。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 顺的时候别得意</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>父母疼你，别把孝顺当成给父母的面子</strong>；<strong>顺手做的事，也认真做</strong>。</p><p>💡 难的时候别冷心</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>挨了骂、受了委屈，该尽的还是要尽</strong>；<strong>心一冷，就什么都做不进去了</strong>。</p><p>🌱 劝的时候放低声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>发现父母做得不对，先缓一口气再开口</strong>；<strong>脸色和、声音软，话才落得下去</strong><br/><br/><strong>本课的落点：亲有过，谏使更。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第五段。记牢：<strong>亲憎我，孝方贤</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>三种情形 · 爱我、憎我、有过。<strong>越难越见心</strong>。</p><p>亲爱我，孝何难 · 顺境里的孝是本分。<strong>别当成功劳</strong>。</p><p>亲憎我，孝方贤 · 逆境里还肯孝，才见修养。<strong>心不冷</strong>。</p><p>亲有过，谏使更 · 该劝就劝，为改不为赢。<strong>不劝才是不负责</strong>。</p><p>怡吾色，柔吾声 · 脸色和、声音柔，话才进得去。<strong>好话好声说</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第五段，讲顺逆与规劝；下一课讲「谏不入，悦复谏」、「亲有疾，药先尝」。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「憎」和「更」是什么意思。② 举一个「怡吾色」的做法。③ 想一想：父母哪件事做错了，你该怎样开口劝。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「亲憎我」的「憎」是什么意思？', opts: ['厌恶、不喜爱', '憎恨得想报复', '害怕'], ans: 0, exp: '憎是不喜爱'},
  {q: '2. 「孝方贤」的「方」是什么意思？', opts: ['才', '方正', '方法'], ans: 0, exp: '方是才'},
  {q: '3. 「亲爱我，孝何难」是什么意思？', opts: ['父母疼我，孝顺不算难事', '父母疼我，就不用孝了', '孝顺很难做到'], ans: 0, exp: '顺境孝不难'},
  {q: '4. 「亲有过」的「过」是什么意思？', opts: ['过错', '经过', '过分'], ans: 0, exp: '过是过错'},
  {q: '5. 「谏使更」的「谏」是什么意思？', opts: ['规劝', '批评指责', '上书告状'], ans: 0, exp: '谏是规劝'},
  {q: '6. 「谏使更」的「更」怎么读？', opts: ['gēng，改正', 'gèng，更加', 'gēng，更换衣服'], ans: 0, exp: '更读 gēng，改正'},
  {q: '7. 「怡吾色」的「怡」是什么意思？', opts: ['温和、和悦', '高兴地大笑', '打扮得好看'], ans: 0, exp: '怡是和悦'},
  {q: '8. 「柔吾声」要求的是什么？', opts: ['声音放柔和', '少说话', '说话要响亮'], ans: 0, exp: '声要柔'},
  {q: '9. 劝父母最重要的是什么？', opts: ['让他改正，不是让他难堪', '把道理讲赢', '让父母认错'], ans: 0, exp: '为改不为赢'},
  {q: '10. 这一段总的讲什么？', opts: ['顺逆都要孝，劝父母要气和声柔', '怎么读书明理', '怎么与邻里相处'], ans: 0, exp: '顺逆与劝法'},
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
s = s.replace('《弟子规》第五课', '《弟子规》第六课')
s = s.replace("window.GUOXUE_COURSE_ID = '545-qin-suo-hao';", "window.GUOXUE_COURSE_ID = '546-qin-ai-wo';")
s = s.replace('yaoyue546', 'yaoyue547')

# ---- 校验 ----
for w in ['亲所好', '力为具', '亲所恶', '谨为去', '身有伤', '贻亲忧', '德有伤', '贻亲羞',
          '545-qin-suo-hao', 'yaoyue546', '第五课']:
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
