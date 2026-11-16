#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build548: 以 547 课件为模板生成第 548 课《入则孝·丧三年，常悲咽》。
本课是「入则孝」一门第七段，也是第一门收官课。
讲义 8 页（承 542 新排版：原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（父母身后的事）/ 3 丧三年常悲咽·居处变酒肉绝 /
  4 丧尽礼祭尽诚·事死者如事生 / 5 两句合看（情与礼、今天怎么做）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/547-jian-bu-ru/index.html"
DST = ROOT + "/lessons/548-sang-san-nian/index.html"

TITLE = '入则孝 · 丧三年，常悲咽，事死如事生 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '丧尽礼，祭尽诚；事死者，如事生 · 弟子规课堂'
DESC = ('《弟子规》第八课，入则孝第七段，也是「入则孝」一门的收官课。原文：「丧三年，常悲咽。'
        '居处变，酒肉绝。丧尽礼，祭尽诚。事死者，如事生。」讲父母身后的事：守丧三年，'
        '想起父母就难过，日子过得简朴，不图酒肉享乐；办丧事礼数要做全，祭祀时心里要真，'
        '对待去世的父母像他们活着时一样。孝从生前一直走到身后——情在心里，礼在事上。')
OG_DESC = '《弟子规》第八课：丧三年常悲咽、丧尽礼祭尽诚、事死者如事生——孝不止于生前，入则孝收官。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/548-sang-san-nian/index.html'

ORIG = '丧三年，常悲咽。居处变，酒肉绝。丧尽礼，祭尽诚。事死者，如事生。'
ORIG_COMMA = '丧三年，常悲咽，居处变，酒肉绝；丧尽礼，祭尽诚，事死者，如事生。'
OLD_ORIG = '谏不入，悦复谏。号泣随，挞无怨。亲有疾，药先尝。昼夜侍，不离床。'
OLD_ORIG_COMMA = '谏不入，悦复谏，号泣随，挞无怨；亲有疾，药先尝，昼夜侍，不离床。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('丧三年常悲咽', ['sāng', 'sān', 'nián', 'cháng', 'bēi', 'yè'], True)
             + ju('居处变酒肉绝', ['jū', 'chǔ', 'biàn', 'jiǔ', 'ròu', 'jué'], False)
             + ju('丧尽礼祭尽诚', ['sāng', 'jìn', 'lǐ', 'jì', 'jìn', 'chéng'], False)
             + ju('事死者如事生', ['shì', 'sǐ', 'zhě', 'rú', 'shì', 'shēng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">如事生</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》入则孝第七段：丧三年，常悲咽</p><p class="cover-desc">上一段讲劝到底、守在床边，这一段讲父母身后的事：丧、祭和思念。前四句讲心里的痛和日子的简，后四句讲礼数要全、心意要真。这一段讲完，「入则孝」这一门就讲完了。</p><div class="cover-seal">入则孝</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 入则孝第七段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>父母去世，守丧三年，常常悲从中来、哽咽难止。住的地方改得简朴，酒和肉都断了。办丧事礼数要做全，祭祀时心里要真诚。对待去世的父母，就像他们还活着时一样。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「丧」读 sāng，指丧事；「咽」读 yè，是哭泣哽咽；「居处」读 jū chǔ，是住处、日常起居；「绝」是断绝；「尽」是竭尽、做到；「祭」是祭祀。前四句讲丧中的哀与简，后四句讲丧祭的礼与诚。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 父母身后的事</h2><p style="margin:0"><strong>入则孝讲到最后一程</strong><br/>① <strong>前几段讲父母在世：听呼唤、照料起居、劝过错、侍病</strong><br/>② <strong>这一段讲父母不在了：丧、祭、思念</strong><br/><br/><strong>一句话：孝不止于生前。</strong></p><p><strong>这一段分两层</strong><br/>① <strong>丧中怎么做：久久悲咽、日子从简</strong><br/>② <strong>丧祭怎么做：礼要做全、心要真</strong><br/><br/><strong>一句话：一层在情，一层在礼。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>心里真有悲，礼才有分量</strong><br/>② <strong>礼数不亏，情才落得下来</strong><br/><br/><strong>一句话：情与礼一起走。</strong></p></div>
<!-- 4. 丧三年常悲咽·居处变酒肉绝 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>丧三年，常悲咽；居处变，酒肉绝</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>丧 sāng：丧事；咽 yè：哭泣哽咽</strong><br/>② <strong>居处 chǔ：住处、起居；绝：断绝</strong><br/><br/><strong>一句话：守丧三年，日子从简。</strong></p><p><strong>常悲咽</strong><br/>① <strong>想起父母就难过，不是装给外人看</strong><br/>② <strong>古人守三年，因为父母抱养子女也是三年</strong><br/><br/><strong>一句话：悲从心里来。</strong></p><p><strong>居处变，酒肉绝</strong><br/>① <strong>住得简朴些，不图享受</strong><br/>② <strong>不喝酒不吃肉，把日子收一收</strong><br/><br/><strong>一句话：用日子表达心意。</strong></p></div>
<!-- 5. 丧尽礼祭尽诚·事死者如事生 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>丧尽礼，祭尽诚；事死者，如事生</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>尽：竭尽、做到；礼：礼数、规矩</strong><br/>② <strong>祭 jì：祭祀；诚：真心</strong><br/><br/><strong>一句话：礼要做全，心要真。</strong></p><p><strong>丧尽礼，祭尽诚</strong><br/>① <strong>该有的礼数，一样不缺</strong><br/>② <strong>祭祀不摆样子，心里真有父母</strong><br/><br/><strong>一句话：礼是壳，诚是核。</strong></p><p><strong>事死者，如事生</strong><br/>① <strong>对待去世的父母，像他们活着时一样</strong><br/>② <strong>该敬的敬，该念的念，不改那份心</strong><br/><br/><strong>一句话：人走了，心不走。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 情与礼</h2><p style="margin:0"><strong>前四句讲「情」</strong><br/>① <strong>悲咽，是心里的痛</strong><br/>② <strong>日子从简，是把自己的享受让出来</strong><br/><br/><strong>一句话：痛在心里，落在日子上。</strong></p><p><strong>后四句讲「礼」</strong><br/>① <strong>丧要尽礼，祭要尽诚</strong><br/>② <strong>如事生，是把礼做到心里去</strong><br/><br/><strong>一句话：礼不到，情无处落。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>三年守丧的老规矩，今天不必照搬</strong><br/>② <strong>但「尽礼、尽诚、不忘」三样，一样不能少</strong><br/><br/><strong>一句话：形式可改，心不能改。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句一组</h2><p style="margin:0"><strong>前四句：丧中之痛</strong><br/>① <strong>丧三年，常悲咽——久久不忘</strong><br/>② <strong>居处变，酒肉绝——日子从简</strong><br/><br/><strong>一句话：以简寄哀。</strong></p><p><strong>后四句：丧祭之诚</strong><br/>① <strong>丧尽礼，祭尽诚——礼全、心真</strong><br/>② <strong>事死者，如事生——事死如生</strong><br/><br/><strong>一句话：以诚尽礼。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>悲在心里，简在日子</strong><br/>② <strong>礼不亏，诚不减</strong><br/><br/><strong>一句话：不忘，就是孝。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>守丧常悲，日子从简；丧祭尽礼尽诚，事死如生。</p><p>📖 情与礼</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>孝从生前走到身后，心不忘、礼不缺。</p><p>💡 不止生前</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 不忘，就是孝</p>
<p>这是「弟子规课堂」第八课：入则孝第七段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 现在还要守三年丧吗？</h3><p><strong>老礼不必照搬。</strong><br/><br/>① <strong>古时守三年，是因为父母抱养子女三年</strong><br/>② <strong>今天要上学、要做事，形式可以改</strong><br/>③ <strong>记法：礼可简，心不可减。</strong></p><h3>❓ 「居处变、酒肉绝」今天怎么理解？</h3><p><strong>收一收自己的享受。</strong><br/><br/>① <strong>丧期不办喜事、不图热闹</strong><br/>② <strong>家里人难过时，别只顾自己开心</strong><br/>③ <strong>记法：让一让，是体谅。</strong></p><h3>❓ 没见过的祖辈，也要祭吗？</h3><p><strong>祭的是那份传承。</strong><br/><br/>① <strong>听父母讲祖辈的事，就是「不忘」</strong><br/>② <strong>上坟、扫墓、说说话，都是祭</strong><br/>③ <strong>记法：记得来处。</strong></p><h3>❓ 「事死者，如事生」怎么做？</h3><p><strong>把生前的规矩留下来。</strong><br/><br/>① <strong>父母在时的好习惯，接着做下去</strong><br/>② <strong>父母惦记的人，替他照看</strong><br/>③ <strong>记法：人不在了，事还照着做。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 记住长辈的故事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>问问父母：爷爷奶奶当年是什么样的人</strong>；<strong>记住了，人就还在</strong>。</p><p>💡 该祭的时候去一去</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>清明、忌日跟着家里去，认真行礼</strong>；<strong>不低头玩手机，就是「尽诚」</strong>。</p><p>🌱 把好习惯接过来</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>长辈的勤俭、守信、待人有礼，学着做</strong>；<strong>这就是「如事生」</strong><br/><br/><strong>本课的落点：事死者，如事生。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲入则孝第七段。记牢：<strong>事死者，如事生</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>父母身后的事 · 孝不止于生前。<strong>一直走到身后</strong>。</p><p>丧三年，常悲咽 · 想起就难过，不是装的。<strong>悲从心里来</strong>。</p><p>居处变，酒肉绝 · 日子收一收，不图享受。<strong>以简寄哀</strong>。</p><p>丧尽礼，祭尽诚 · 礼数做全，心里要真。<strong>礼是壳，诚是核</strong>。</p><p>事死者，如事生 · 像他们活着时一样。<strong>人不在了，心还在</strong>。</p><p><strong>在全篇中的位置:</strong>入则孝第七段，第一门到此讲完；下一门讲「出则悌」——兄道友，弟道恭。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「丧」和「咽」在这里各读什么音。② 说一说今天可以怎么「尽诚」。③ 问父母一件祖辈的旧事，记住它。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「丧三年」的「丧」怎么读？', opts: ['sāng，指丧事', 'sàng，丧失', 'sāng，丧气'], ans: 0, exp: '丧读 sāng，丧事'},
  {q: '2. 「常悲咽」的「咽」怎么读？', opts: ['yè，哭泣哽咽', 'yān，咽喉', 'yàn，吞咽'], ans: 0, exp: '咽读 yè，哽咽'},
  {q: '3. 「居处变」的「居处」是什么意思？', opts: ['住处、日常起居', '居住的地方搬家', '与人相处'], ans: 0, exp: '居处读 jū chǔ'},
  {q: '4. 「酒肉绝」的「绝」是什么意思？', opts: ['断绝', '绝顶好', '拒绝别人'], ans: 0, exp: '绝是断绝'},
  {q: '5. 「丧尽礼」的「尽」是什么意思？', opts: ['竭尽、做到', '尽管', '完了'], ans: 0, exp: '尽是做到'},
  {q: '6. 「祭尽诚」重在什么？', opts: ['心里的真诚', '供品要多', '场面要大'], ans: 0, exp: '诚是核心'},
  {q: '7. 「事死者，如事生」是什么意思？', opts: ['对待去世的父母像活着时一样', '把丧事办得像喜事', '生前死后都要花钱'], ans: 0, exp: '事死如事生'},
  {q: '8. 古人为什么守丧三年？', opts: ['父母抱养子女也是三年', '三年才办得完丧事', '怕别人说不孝'], ans: 0, exp: '报三年之怀'},
  {q: '9. 今天的「居处变、酒肉绝」该怎样理解？', opts: ['收一收自己的享受，体谅家人', '必须三年不喝酒', '搬家住得远些'], ans: 0, exp: '让一让，是体谅'},
  {q: '10. 这一段总的讲什么？', opts: ['父母身后要尽哀、尽礼、尽诚', '怎么操办丧事省钱', '怎么教养下一代'], ans: 0, exp: '哀、礼、诚'},
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
s = s.replace('《弟子规》第七课', '《弟子规》第八课')
s = s.replace("window.GUOXUE_COURSE_ID = '547-jian-bu-ru';", "window.GUOXUE_COURSE_ID = '548-sang-san-nian';")
s = s.replace('yaoyue548', 'yaoyue549')

# ---- 校验 ----
for w in ['谏不入', '悦复谏', '号泣随', '挞无怨', '亲有疾', '药先尝', '昼夜侍', '不离床',
          '547-jian-bu-ru', 'yaoyue548', '第七课']:
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
