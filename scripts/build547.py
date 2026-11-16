#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build547: 以 546 课件为模板生成第 547 课《入则孝·谏不入，悦复谏》。

讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（劝不动了怎么办）/ 3 谏不入悦复谏·号泣随挞无怨 /
  4 亲有疾药先尝·昼夜侍不离床 / 5 两句合看（劝与侍）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课（546 起收费）。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/546-qin-ai-wo/index.html"
DST = ROOT + "/lessons/547-jian-bu-ru/index.html"

TITLE = '入则孝 · 谏不入，悦复谏，昼夜侍 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '谏不入，悦复谏；昼夜侍，不离床 · 弟子规课堂'
DESC = ('《弟子规》第七课，入则孝第六段。原文：「谏不入，悦复谏。号泣随，挞无怨。'
        '亲有疾，药先尝。昼夜侍，不离床。」两层意思：父母一时听不进劝，别赌气走开，'
        '等他气顺了再来一次，急到哭、挨了打也不记恨；父母病了，先替他尝药，'
        '白天黑夜守在床边。孝到难处才见真——劝要有耐心，守要有耐性。')
OG_DESC = '《弟子规》第七课：谏不入悦复谏、号泣随挞无怨——劝到底不记恨；亲有疾药先尝、昼夜侍不离床——守在床边。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/547-jian-bu-ru/index.html'

ORIG = '谏不入，悦复谏。号泣随，挞无怨。亲有疾，药先尝。昼夜侍，不离床。'
ORIG_COMMA = '谏不入，悦复谏，号泣随，挞无怨；亲有疾，药先尝，昼夜侍，不离床。'
OLD_ORIG = '亲爱我，孝何难。亲憎我，孝方贤。亲有过，谏使更。怡吾色，柔吾声。'
OLD_ORIG_COMMA = '亲爱我，孝何难，亲憎我，孝方贤；亲有过，谏使更，怡吾色，柔吾声。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('谏不入悦复谏', ['jiàn', 'bù', 'rù', 'yuè', 'fù', 'jiàn'], True)
             + ju('号泣随挞无怨', ['háo', 'qì', 'suí', 'tà', 'wú', 'yuàn'], False)
             + ju('亲有疾药先尝', ['qīn', 'yǒu', 'jí', 'yào', 'xiān', 'cháng'], False)
             + ju('昼夜侍不离床', ['zhòu', 'yè', 'shì', 'bù', 'lí', 'chuáng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">悦复谏</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第六段：谏不入，悦复谏</p><p class="cover-desc">上一段讲父母有错怎么劝，这一段接着往下走：劝了不听又该怎么办，父母病了又该怎么办。前四句讲劝到底的耐心，后四句讲守在床边的耐性——孝到难处才看得出真假。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第六段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>劝了父母还不听，就等他高兴的时候再劝。急得哭着跟着劝，因此挨了打，心里也不怨恨。父母生病了，药要自己先尝一尝；白天黑夜伺候着，不离开床边。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「入」是听得进去；「悦」是高兴、气顺；「复」是再；「号」读 háo，是大声哭；「挞」读 tà，是打；「疾」是病；「侍」是伺候。前四句讲再劝，后四句讲侍疾。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 劝不动了怎么办</h2><p style="margin:0"><strong>接上一段的话说</strong><br/>① <strong>上一段讲：父母有错要劝，脸色要和、声音要柔</strong><br/>② <strong>这一段讲：劝了不听，还要再来一次</strong><br/><br/><strong>一句话：一次不成，还有第二次。</strong></p><p><strong>办法只有两个字</strong><br/>① <strong>「悦」：等他高兴、气顺了再说</strong><br/>② <strong>「复」：一次不行就再来一次</strong><br/><br/><strong>一句话：不急，也不弃。</strong></p><p><strong>这一段分两半</strong><br/>① <strong>前四句：劝到底，受了委屈也不怨</strong><br/>② <strong>后四句：父母病了，守在床边</strong><br/><br/><strong>一句话：一个在嘴边，一个在床边。</strong></p></div>
<!-- 4. 谏不入悦复谏·号泣随挞无怨 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>谏不入，悦复谏；号泣随，挞无怨</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>入：听得进去；悦：高兴、气顺</strong><br/>② <strong>复：再；号 háo：大声哭；挞 tà：打</strong><br/><br/><strong>一句话：不听就再劝，挨打也不怨。</strong></p><p><strong>谏不入，悦复谏</strong><br/>① <strong>父母没听，别赌气走开</strong><br/>② <strong>等他高兴、气顺了，再好好说一遍</strong><br/><br/><strong>一句话：挑时候，说第二遍。</strong></p><p><strong>号泣随，挞无怨</strong><br/>① <strong>说不动，可以哭着跟着劝，是着急不是撒泼</strong><br/>② <strong>因此挨了打，心里也不怨恨</strong><br/><br/><strong>一句话：怨一上来，孝就断了。</strong></p></div>
<!-- 5. 亲有疾药先尝·昼夜侍不离床 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>亲有疾，药先尝；昼夜侍，不离床</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>疾：病；尝：尝一尝</strong><br/>② <strong>昼夜：白天黑夜；侍：伺候</strong><br/><br/><strong>一句话：病床前最见人心。</strong></p><p><strong>药先尝</strong><br/>① <strong>药烫不烫、苦不苦，自己先试一口</strong><br/>② <strong>是怕父母受罪，不是走个过场</strong><br/><br/><strong>一句话：先替父母试一口。</strong></p><p><strong>昼夜侍，不离床</strong><br/>① <strong>白天黑夜守着，不躲不推</strong><br/>② <strong>累是真的，可这时父母最需要人</strong><br/><br/><strong>一句话：守在床边，就是孝。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 劝与侍</h2><p style="margin:0"><strong>前一半讲「心不死」</strong><br/>① <strong>不听再劝，挨打不怨</strong><br/>② <strong>靠的是一股不肯放手的劲</strong><br/><br/><strong>一句话：难在坚持。</strong></p><p><strong>后一半讲「人不走」</strong><br/>① <strong>病了先尝药，夜了不离床</strong><br/>② <strong>靠的是肯花时间、肯受苦</strong><br/><br/><strong>一句话：难在守得住。</strong></p><p><strong>合起来一句</strong><br/>① <strong>孝有两副面孔：劝的时候有耐心，守的时候有耐性</strong><br/>② <strong>一副在嘴边，一副在床边</strong><br/><br/><strong>一句话：都不容易，都要做。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一组</h2><p style="margin:0"><strong>前四句：劝到底</strong><br/>① <strong>谏不入，悦复谏——等气顺了再说</strong><br/>② <strong>号泣随，挞无怨——劝到哭，挨打不怨</strong><br/><br/><strong>一句话：不放弃，不记恨。</strong></p><p><strong>后四句：守在旁</strong><br/>① <strong>亲有疾，药先尝——先替父母试</strong><br/>② <strong>昼夜侍，不离床——日夜不离开</strong><br/><br/><strong>一句话：不怕苦，不躲开。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>不听再劝，挨打不怨</strong><br/>② <strong>药先尝，床不离</strong><br/><br/><strong>一句话：耐心加耐性。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>劝不听再劝，挨打不怨；病中先尝药，日夜守着。</p><p>📖 难处见真</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>劝是替父母好，守是陪父母难。</p><p>💡 一劝一守</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 劝到底、守得住</p>
<p>这是「弟子规课堂」第七课：入则孝第六段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 父母打我，我也不怨，是不是太憋屈？</h3><p><strong>不记恨，不等于硬扛。</strong><br/><br/>① <strong>心里不怨恨，是修养</strong><br/>② <strong>真有危险，要告诉别的大人、护住自己</strong><br/>③ <strong>记法：不记恨，也不任人欺负。</strong></p><h3>❓ 一直劝，父母嫌我烦怎么办？</h3><p><strong>换法子，别加码。</strong><br/><br/>① <strong>说明白一次就停，比反复唠叨管用</strong><br/>② <strong>找父母信得过的人帮着说</strong><br/>③ <strong>记法：劝得巧，胜过劝得多。</strong></p><h3>❓ 「药先尝」现在还要做吗？</h3><p><strong>学的是那份心。</strong><br/><br/>① <strong>现在不必试药，可以试水温、看说明、盯住吃药</strong><br/>② <strong>陪诊、取药、记时间，都是「先尝」</strong><br/>③ <strong>记法：形式变了，心没变。</strong></p><h3>❓ 要上学，怎么昼夜守着？</h3><p><strong>尽力就好。</strong><br/><br/>① <strong>课不能缺，放学就往床边去</strong><br/>② <strong>端水、擦脸、说说话，都算侍</strong><br/>③ <strong>记法：能守多久守多久。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 劝不动就等一等</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>气头上别说，等他高兴了再来一次</strong>；<strong>同一句话，换个时候就进得去</strong>。</p><p>💡 家里有人病，先做一件小事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>倒杯温水、递个药、把被子掖一掖</strong>；<strong>小事做着，人就安心了</strong>。</p><p>🌱 挨了说，先不记恨</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>受了委屈，先缓一缓，别把怨气挂在脸上</strong>；<strong>怨气一挂，话就说不成了</strong><br/><br/><strong>本课的落点：谏不入，悦复谏。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第六段。记牢：<strong>谏不入，悦复谏</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>劝不动了怎么办 · 等他气顺再说，一次不行再来。<strong>不急也不弃</strong>。</p><p>谏不入，悦复谏 · 挑时候说第二遍。<strong>劝得巧</strong>。</p><p>号泣随，挞无怨 · 劝到哭，挨打不记恨。<strong>怨一上来孝就断</strong>。</p><p>亲有疾，药先尝 · 先替父母试一口。<strong>怕他受罪</strong>。</p><p>昼夜侍，不离床 · 日夜守着不躲开。<strong>守在床边就是孝</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第六段，讲再劝与侍疾；下一课讲「丧三年，常悲咽」、「事死者，如事生」，入则孝收官。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「悦」和「复」在这里的意思。② 说一说「药先尝」今天可以怎么做。③ 家里有人不舒服时，你今天能替谁做一件小事。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「谏不入」的「入」是什么意思？', opts: ['听得进去', '进门', '收入'], ans: 0, exp: '入是听得进去'},
  {q: '2. 「悦复谏」的「悦」是什么意思？', opts: ['高兴、气顺', '悦耳好听', '喜悦地笑'], ans: 0, exp: '悦是气顺'},
  {q: '3. 「悦复谏」的「复」是什么意思？', opts: ['再、又一次', '恢复原样', '重复啰嗦'], ans: 0, exp: '复是再'},
  {q: '4. 「号泣随」的「号」怎么读？', opts: ['háo，大声哭', 'hào，号码', 'háo，号叫骂人'], ans: 0, exp: '号读 háo，大声哭'},
  {q: '5. 「挞无怨」的「挞」是什么意思？', opts: ['打', '责备', '拉扯'], ans: 0, exp: '挞是打'},
  {q: '6. 「挞无怨」的「怨」是什么意思？', opts: ['心里记恨', '埋怨几句', '委屈地哭'], ans: 0, exp: '怨是记恨'},
  {q: '7. 「亲有疾」的「疾」是什么意思？', opts: ['病', '着急', '疼痛'], ans: 0, exp: '疾是病'},
  {q: '8. 「药先尝」为什么要先尝？', opts: ['怕父母烫着、苦着受罪', '看看药好不好喝', '怕药不够'], ans: 0, exp: '怕父母受罪'},
  {q: '9. 「昼夜侍，不离床」说的是什么？', opts: ['白天黑夜守着病床', '晚上才去守着', '请人代为照看'], ans: 0, exp: '昼夜不离'},
  {q: '10. 这一段总的讲什么？', opts: ['劝不动还要再劝，父母病了要守在床边', '怎么熬药看病', '怎么与兄弟相处'], ans: 0, exp: '再劝与侍疾'},
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
s = s.replace('《弟子规》第六课', '《弟子规》第七课')
s = s.replace("window.GUOXUE_COURSE_ID = '546-qin-ai-wo';", "window.GUOXUE_COURSE_ID = '547-jian-bu-ru';")
s = s.replace('yaoyue547', 'yaoyue548')

# ---- 校验 ----
for w in ['亲爱我', '孝何难', '亲憎我', '孝方贤', '亲有过', '谏使更', '怡吾色', '柔吾声',
          '546-qin-ai-wo', 'yaoyue547', '第六课']:
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
