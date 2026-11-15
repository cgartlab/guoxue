#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build541: 以 540 课件为模板生成第 541 课《走近弟子规·作者与时代》。

本课是新门类「弟子规课堂」第一课（导论课），讲义 8 页排布为：
  0 封面 / 1 作者 / 2 成书 / 3 时代背景 / 4 全书结构 / 5 总叙原文 /
  6 总叙解读 / 7 核心思想；测验 12 页、答疑 4 页沿用模板，总 24 页。
区域替换法：讲义区整块换、答疑区整块换、QUIZ 数组整块换、头部 meta 正则换。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/540-ren-yi-zi/index.html"
DST = ROOT + "/lessons/541-dizigui-kaipian/index.html"

TITLE = '走近弟子规 · 作者与时代，清初蒙学 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '走近弟子规 · 作者与时代，清初蒙学与全书结构 · 弟子规课堂'
DESC = ('《弟子规》第一课（导论）：先认书，不急着背句子。作者李毓秀（1647—1729），字子潜，'
        '号采三，山西绛州人，康熙年间的秀才，一生没做官，在乡里教书，人称「李夫子」，'
        '写下启蒙课本《训蒙文》；后来清代山西浮山人贾存仁修订改编，改名《弟子规》。'
        '时代背景是康熙年间天下初定、朝廷重教化，各地办社学义学，村塾需要浅近易诵的规矩书。'
        '全书三字一句、两句一韵，360 句 1080 字，分总叙与七门：入则孝、出则弟、谨、信、'
        '泛爱众、亲仁、余力学文。总叙八句「弟子规，圣人训。首孝弟，次谨信。泛爱众，而亲仁。'
        '有余力，则学文。」出自《论语·学而》，全书纲目即由此而来。')
OG_DESC = '《弟子规》第一课：作者李毓秀、《训蒙文》改名经过、康熙年间的蒙学背景、全书七门结构，并串讲总叙八句。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/541-dizigui-kaipian/index.html'

ORIG = '弟子规，圣人训。首孝弟，次谨信。泛爱众，而亲仁。有余力，则学文。'
ORIG_COMMA = '弟子规，圣人训，首孝弟，次谨信；泛爱众，而亲仁，有余力，则学文。'
OLD_ORIG = '人遗子，金满籝。我教子，惟一经。勤有功，戏无益。戒之哉，宜勉力。'
OLD_ORIG_COMMA = '人遗子，金满籝，我教子，惟一经；勤有功，戏无益，戒之哉，宜勉力。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('弟子规圣人训', ['dì', 'zǐ', 'guī', 'shèng', 'rén', 'xùn'], True)
             + ju('首孝弟次谨信', ['shǒu', 'xiào', 'tì', 'cì', 'jǐn', 'xìn'], False)
             + ju('泛爱众而亲仁', ['fàn', 'ài', 'zhòng', 'ér', 'qīn', 'rén'], False)
             + ju('有余力则学文', ['yǒu', 'yú', 'lì', 'zé', 'xué', 'wén'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">弟子规</h2><div class="cover-ornament"></div><p class="cover-subtitle">李毓秀原著，康熙年间成书；先认书，再读书</p><p class="cover-desc">《三字经》讲完了，今天开一部新的蒙学书。第一课不急着背句子，先把这部书认清楚：谁写的、什么时候写的、为什么写、全书怎么排。认清了门路，后面一句一句读才不糊涂。</p><div class="cover-seal">弟子规</div></div>
<!-- 2. 作者 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>作者 · 清初教书先生李毓秀</h2><p style="margin:0"><strong>李毓秀（1647—1729）</strong><br/>① <strong>字子潜，号采三</strong><br/>② <strong>山西绛州人，即今天的新绛</strong><br/><br/><strong>一句话：清初山西的读书人。</strong></p><p><strong>他的身份</strong><br/>① <strong>康熙年间的秀才</strong><br/>② <strong>一生没做官，在乡里教书</strong><br/>③ <strong>学生敬他，称「李夫子」</strong><br/><br/><strong>一句话：教了一辈子书。</strong></p></div>
<!-- 3. 成书 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>成书 · 从《训蒙文》到《弟子规》</h2><p style="margin:0"><strong>原名《训蒙文》</strong><br/>① <strong>教书先生为学生编的启蒙课本</strong><br/>② <strong>「训蒙」就是教小孩子</strong><br/><br/><strong>一句话：本来叫训蒙文。</strong></p><p><strong>谁改了名</strong><br/>① <strong>清代山西浮山人贾存仁</strong><br/>② <strong>整理修订，改名《弟子规》</strong><br/><br/><strong>一句话：修订后才叫弟子规。</strong></p><p><strong>篇幅与体例</strong><br/>① <strong>三字一句，两句一韵</strong><br/>② <strong>360 句，1080 字</strong><br/><br/><strong>一句话：好念、好背、好记。</strong></p></div>
<!-- 4. 时代背景 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>时代背景 · 康熙年间的蒙学</h2><p style="margin:0"><strong>天下初定</strong><br/>① <strong>清初战乱刚过，人心要安</strong><br/>② <strong>朝廷讲教化，先正家风</strong><br/><br/><strong>一句话：乱后思治。</strong></p><p><strong>朝廷重教化</strong><br/>① <strong>康熙颁《圣谕十六条》，劝人孝亲守礼</strong><br/>② <strong>各地办社学、义学，学堂渐多</strong><br/><br/><strong>一句话：上面提倡读书守礼。</strong></p><p><strong>蒙书的需求</strong><br/>① <strong>村塾孩子多，缺浅近易诵的课本</strong><br/>② <strong>《弟子规》正好补上这一块</strong><br/><br/><strong>一句话：应运而生。</strong></p></div>
<!-- 5. 全书结构 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>全书结构 · 总叙加七门</h2><p style="margin:0"><strong>开头是总叙</strong><br/>① <strong>最前面八句，是全篇总纲</strong><br/>② <strong>后面各段都由它生出来</strong><br/><br/><strong>一句话：先立总纲。</strong></p><p><strong>正文分七门</strong><br/>① <strong>入则孝、出则弟、谨、信</strong><br/>② <strong>泛爱众、亲仁、余力学文</strong><br/><br/><strong>一句话：一门一门往下讲。</strong></p><p><strong>一条主线</strong><br/>① <strong>先在家孝弟，再对外谨信、爱众亲仁</strong><br/>② <strong>最后才是读书学文</strong><br/><br/><strong>一句话：做人在前，学问在后。</strong></p></div>
<!-- 6. 原文呈现 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">总叙原文</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>这是圣人的教诲：第一要孝顺父母、敬爱兄长，其次做事谨慎、说话守信；要广泛爱人、亲近仁德的人；这些做到了还有余力，再去学诗书文章。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>总叙八句出自《论语·学而》「弟子入则孝，出则弟，谨而信，泛爱众，而亲仁，行有余力，则以学文」，《弟子规》全书纲目由此而来。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 7. 总叙解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总叙解读 · 四句串起来</h2><p style="margin:0"><strong>「弟子规，圣人训」</strong><br/>① <strong>弟子：做学生的人</strong><br/>② <strong>规：规矩；训：教诲</strong><br/><br/><strong>一句话：孩子的规矩，本于圣人之言。</strong></p><p><strong>「首孝弟，次谨信」</strong><br/>① <strong>首：第一；次：其次</strong><br/>② <strong>弟读 tì，同「悌」，敬爱兄长</strong><br/><br/><strong>一句话：先在家孝顺，再在外谨慎守信。</strong></p><p><strong>「泛爱众…则学文」</strong><br/>① <strong>泛：广泛；亲仁：亲近有德的人</strong><br/>② <strong>余力：剩下的精力；学文：学诗书</strong><br/><br/><strong>一句话：做人够了，再读书。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>先说孝弟谨信，再说爱众亲仁，最后才说学文。</p><p>📖 做人在前</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>不是不要学问，是先把根扎稳，读书才读得住。</p><p>💡 根深叶茂</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 先做人</p>
<p>这是「弟子规课堂」第一课：走近《弟子规》。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 《弟子规》是孔子写的吗？</h3><p><strong>不是，是清代人编的。</strong><br/><br/>① <strong>作者李毓秀，康熙年间秀才</strong><br/>② <strong>纲目取自《论语·学而》孔子的话</strong><br/>③ <strong>后经贾存仁修订改名</strong><br/><br/><strong>记法：清朝人编，孔子之意。</strong></p><h3>❓ 为什么叫「弟子」？</h3><p><strong>指做学生的人。</strong><br/><br/>① <strong>在家是子弟</strong><br/>② <strong>在学塾是学生</strong><br/>③ <strong>总之是正在学做人的后辈</strong><br/><br/><strong>记法：弟子就是后生。</strong></p><h3>❓ 1080 字要不要全背？</h3><p><strong>先懂再做，背是后一步。</strong><br/><br/>① <strong>先从总叙八句起</strong><br/>② <strong>再读「入则孝」</strong><br/>③ <strong>背一句，照着做一句</strong><br/><br/><strong>记法：懂了再做。</strong></p><h3>❓ 和《三字经》有什么不同？</h3><p><strong>都是蒙学书，讲的侧重不同。</strong><br/><br/>① <strong>《三字经》讲常识、历史、劝学</strong><br/>② <strong>《弟子规》讲日常规矩怎么做</strong><br/>③ <strong>一本讲道理，一本讲做法</strong><br/><br/><strong>记法：一理一行。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课虽是认书，也有三样可做——</p><p>📖 先认住作者与书名</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>李毓秀写《训蒙文》，贾存仁改成《弟子规》</strong>；<strong>一问一答，能说清来历</strong>。</p><p>💡 记住先做人后学文</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>「首孝弟，次谨信」</strong>；<strong>回家先做一件孝顺的小事，比背十句强</strong>。</p><p>🌱 把总叙念顺口</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>八句 24 字，念三遍就能上口</strong>；<strong>念顺了，再一句一句往下学</strong><br/><br/><strong>本课的落点：弟子规，圣人训。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天开了「弟子规课堂」第一课。记牢：<strong>弟子规，圣人训</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>作者李毓秀 · 康熙年间山西绛州教书先生。<strong>清朝人编</strong>。</p><p>原名《训蒙文》 · 贾存仁修订改名《弟子规》。<strong>改名成书</strong>。</p><p>时代背景 · 天下初定、朝廷重教化、村塾需要蒙书。<strong>应运而生</strong>。</p><p>全书结构 · 总叙加七门，孝弟谨信爱众亲仁学文。<strong>做人在前</strong>。</p><p><strong>在全篇中的位置:</strong>这是《弟子规》开篇导论，认作者、认成书、认结构，下一课开始读正文「入则孝」。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出作者和朝代。② 说出原名和改名人。③ 把总叙八句念顺口，讲清「弟」为什么读 tì。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 《弟子规》的作者是谁？', opts: ['李毓秀', '王应麟', '朱熹'], ans: 0, exp: '清代李毓秀'},
  {q: '2. 李毓秀是哪个朝代的人？', opts: ['清朝康熙年间', '唐朝', '宋朝'], ans: 0, exp: '1647—1729'},
  {q: '3. 这部书原来的名字是什么？', opts: ['《训蒙文》', '《千字文》', '《童蒙须知》'], ans: 0, exp: '原名训蒙文'},
  {q: '4. 谁修订并改名为《弟子规》？', opts: ['贾存仁', '李毓秀', '王应麟'], ans: 0, exp: '山西浮山人贾存仁'},
  {q: '5. 总叙的纲目取自哪部书？', opts: ['《论语·学而》', '《孟子》', '《孝经》'], ans: 0, exp: '孔子的话'},
  {q: '6. 全书大约多少字？', opts: ['1080 字', '360 字', '5000 字'], ans: 0, exp: '360 句 1080 字'},
  {q: '7. 「首孝弟」的「弟」怎么读？', opts: ['tì，同「悌」', 'dì，弟弟', 'dī，低头'], ans: 0, exp: '敬爱兄长'},
  {q: '8. 「圣人训」的「训」是什么意思？', opts: ['教诲', '训练身体', '解释字义'], ans: 0, exp: '训是教诲'},
  {q: '9. 「有余力，则学文」是什么意思？', opts: ['做人做好了，剩下精力再学诗书', '有力气就干活', '学文比做人重要'], ans: 0, exp: '做人在前'},
  {q: '10. 七门的顺序是怎样的？', opts: ['孝、弟、谨、信、爱众、亲仁、学文', '学文、孝、弟、谨、信', '谨、信、孝、弟、学文'], ans: 0, exp: '做人在前'},
];'''

raw = io.open(SRC, 'r', encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
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
s = s.replace('《三字经》第四十七课', '《弟子规》第一课')
s = s.replace('「三字经课堂」', '「弟子规课堂」')
s = s.replace('—— 《三字经》', '—— 《弟子规》')
s = s.replace("window.GUOXUE_COURSE_ID = '540-ren-yi-zi';", "window.GUOXUE_COURSE_ID = '541-dizigui-kaipian';")
s = s.replace("window.GUOXUE_COURSE_SUBJECT = 'sanzijing';", "window.GUOXUE_COURSE_SUBJECT = 'dizigui';")
s = s.replace('yaoyue541', 'yaoyue542')

# ---- 校验 ----
# 「三字经」二字允许出现在承接语与 FAQ 对比中；真正要防的是上一课文字残留
for w in ['人遗子', '金满籝', '惟一经', '戒之哉', '第四十七课', '三字经课堂', '540-ren-yi-zi', 'yaoyue541']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 上一课残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
        sys.exit(1)
if 'sanzijing' in s:
    print('[FAIL] subject 未切换')
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
