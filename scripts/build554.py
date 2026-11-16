#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build554: 以 553 课件为模板生成第 554 课《出则悌·事诸父，如事父》。
「出则悌」第六段（收官），讲把敬放大一圈：诸父如父、诸兄如兄。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（把敬放大一圈）/ 3 事诸父如事父 /
  4 事诸兄如事兄 / 5 两句合看（敬与让）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。出则悌一门至此收官。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/553-zun-zhang-qian/index.html"
DST = ROOT + "/lessons/554-shi-zhu-fu/index.html"

TITLE = '出则悌 · 事诸父，如事父，事诸兄，如事兄 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '事诸父，如事父；事诸兄，如事兄 · 弟子规课堂'
DESC = ('《弟子规》第十四课，出则悌第六段（收官）。原文：「事诸父，如事父。事诸兄，如事兄。」'
        '讲把敬放大一圈：对待叔叔伯伯这些长辈，像对待父亲一样；对待堂哥表哥这些兄长，'
        '像对待哥哥一样。家里的礼练熟了，带到门外，见谁都自然。出则悌至此完结。')
OG_DESC = '《弟子规》第十四课：事诸父如事父，事诸兄如事兄。出则悌收官。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/554-shi-zhu-fu/index.html'

ORIG = '事诸父，如事父。事诸兄，如事兄。'
ORIG_COMMA = '事诸父，如事父；事诸兄，如事兄。'
OLD_ORIG = '尊长前，声要低。低不闻，却非宜。进必趋，退必迟。问起对，视勿移。'
OLD_ORIG_COMMA = '尊长前，声要低；低不闻，却非宜；进必趋，退必迟；问起对，视勿移。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('事诸父如事父', ['shì', 'zhū', 'fù', 'rú', 'shì', 'fù'], True)
             + ju('事诸兄如事兄', ['shì', 'zhū', 'xiōng', 'rú', 'shì', 'xiōng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">如事父</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第六段：事诸父，如事父</p><p class="cover-desc">出则悌的收官一段。前面几段讲的都是对自家长辈的礼，这一段把圈子放大：对叔叔伯伯，像对父亲一样敬；对堂哥表哥，像对哥哥一样让。敬不论亲疏，礼不挑场合。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第六段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>对待叔叔、伯伯这些长辈，就像对待自己的父亲一样；对待堂哥、表哥这些兄长，就像对待自己的哥哥一样。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「事」是侍奉、对待；「诸」读 zhū，是众、各位；「诸父」指叔叔、伯伯等父辈；「诸兄」指堂哥、表哥等同辈兄长；「如」是像……一样。家里的礼练熟了，带到门外，见谁都自然。出则悌到这里收官。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 把敬放大一圈</h2><p style="margin:0"><strong>先看「诸父」</strong><br/>① <strong>叔叔伯伯，都是父辈</strong><br/>② <strong>对他们的敬，和对父亲一个样</strong><br/><br/><strong>一句话：长辈不分自家外人。</strong></p><p><strong>再看「诸兄」</strong><br/>① <strong>堂哥表哥，都是兄长</strong><br/>② <strong>对他们的让，和对哥哥一个样</strong><br/><br/><strong>一句话：同辈也不挑。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>出则悌到此收官，敬与让带出门</strong><br/>② <strong>礼随人走，见谁都自然</strong><br/><br/><strong>一句话：礼不挑人。</strong></p></div>
<!-- 4. 事诸父，如事父 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>事诸父，如事父</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>事：侍奉、对待；诸：众、各位</strong><br/>② <strong>如：像……一样</strong><br/><br/><strong>一句话：像对自己的父亲。</strong></p><p><strong>事诸父，如事父</strong><br/>① <strong>叔叔伯伯来家里，起身相迎、端茶让座</strong><br/>② <strong>在外遇到长辈，也一样有礼</strong><br/><br/><strong>一句话：父辈都是「父」。</strong></p><p><strong>为什么这样</strong><br/>① <strong>父辈辛劳一辈子，值得敬</strong><br/>② <strong>把敬练成习惯，见谁都自然</strong><br/><br/><strong>一句话：敬成了习惯。</strong></p></div>
<!-- 5. 事诸兄，如事兄 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>事诸兄，如事兄</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>诸兄：堂哥表哥等同辈兄长</strong><br/>② <strong>让：谦让、礼让</strong><br/><br/><strong>一句话：兄长都是「兄」。</strong></p><p><strong>事诸兄，如事兄</strong><br/>① <strong>对堂哥表哥，像对自己的哥哥</strong><br/>② <strong>东西先让、说话客气</strong><br/><br/><strong>一句话：同辈也有礼。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>表哥来了，好玩的先让他挑</strong><br/>② <strong>排队、上车，先让哥哥姐姐</strong><br/><br/><strong>一句话：让出好家风。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 敬与让</h2><p style="margin:0"><strong>前一句讲「敬」</strong><br/>① <strong>对父辈，敬如父</strong><br/>② <strong>长辈面前有规矩</strong><br/><br/><strong>一句话：敬长辈。</strong></p><p><strong>后一句讲「让」</strong><br/>① <strong>对兄长，让如兄</strong><br/>② <strong>同辈之间不争抢</strong><br/><br/><strong>一句话：让同辈。</strong></p><p><strong>出则悌收官</strong><br/>① <strong>前面五段：路上、称呼、进退、声音</strong><br/>② <strong>这一段把敬放大到所有人</strong><br/><br/><strong>一句话：悌，不止在一家里。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 两句一对</h2><p style="margin:0"><strong>前一句：对长辈</strong><br/>① <strong>事诸父，如事父——敬如敬父</strong><br/>② <strong>不论自家外人，父辈一律敬</strong><br/><br/><strong>一句话：敬长辈。</strong></p><p><strong>后一句：对同辈</strong><br/>① <strong>事诸兄，如事兄——让如让兄</strong><br/>② <strong>堂表兄长，一律礼让</strong><br/><br/><strong>一句话：让同辈。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>见长辈，敬如父</strong><br/>② <strong>见兄长，让如兄</strong><br/><br/><strong>一句话：敬与让，带到门外。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>对叔伯像对父亲，对堂表兄长像对哥哥。</p><p>📖 敬及诸父</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>把家里的礼放大成一辈子的习惯。</p><p>💡 礼随人走</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 事诸父，如事父</p>
<p>这是「弟子规课堂」第十四课：出则悌第六段（收官）。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「诸父」「诸兄」到底指谁？</h3><p><strong>父辈和兄辈的统称。</strong><br/><br/>① <strong>诸父：叔叔、伯伯等父辈</strong><br/>② <strong>诸兄：堂哥、表哥等同辈兄长</strong><br/>③ <strong>记法：父辈都称父，兄辈都称兄。</strong></p><h3>❓ 对外人家的人也要这么敬吗？</h3><p><strong>要，这正是这一段的意思。</strong><br/><br/>① <strong>礼不是只给自家人的</strong><br/>② <strong>见谁都一样有礼，人家才敬你</strong><br/>③ <strong>记法：礼不挑人。</strong></p><h3>❓ 出则悌讲完了，到底讲了什么？</h3><p><strong>出门在外怎么守孝悌。</strong><br/><br/>① <strong>路上怎么走、怎么称呼、声音多高</strong><br/>② <strong>还有最后这句：把敬放大到所有人</strong><br/>③ <strong>记法：出门也一样守礼。</strong></p><h3>❓ 这一段怎么练？</h3><p><strong>两件事：问好、让一步。</strong><br/><br/>① <strong>遇到长辈主动问好，就是「如事父」</strong><br/>② <strong>见到哥哥姐姐先让一步，就是「如事兄」</strong><br/>③ <strong>记法：一步一让。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 遇到长辈就问好</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>叔叔伯伯、邻居爷爷，都起身问好</strong>；<strong>这就是「事诸父，如事父」</strong>。</p><p>💡 好东西先让兄长</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>堂哥表哥来做客，零食玩具先让他挑</strong>；<strong>这就是「事诸兄，如事兄」</strong>。</p><p>🌱 出门在外也一样</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>公交车上让座给长辈，见谁都有礼</strong>；<strong>家里的礼练熟了，带到门外</strong><br/><br/><strong>本课的落点：事诸父，如事父。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第六段，也是出则悌的收官一段。记牢：<strong>事诸父，如事父</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>出则悌收官 · 敬与让带出门。<strong>礼随人走</strong>。</p><p>事诸父，如事父 · 叔伯如父。<strong>敬长辈</strong>。</p><p>事诸兄，如事兄 · 堂表如兄。<strong>让同辈</strong>。</p><p>礼不挑人 · 自家外人一个样。<strong>敬不论亲疏</strong>。</p><p>练成习惯 · 见谁都自然。<strong>礼随人走</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第六段（收官）；上一课讲长辈跟前的说话、进退与应答，这一课把敬放大到诸父诸兄，出则悌至此完结，下一课开新的一门。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「诸」是什么意思。② 今天遇到一位长辈，主动问好。③ 把好东西让给哥哥姐姐一次。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「事诸父」的「事」是什么意思？', opts: ['侍奉、对待', '事情', '上班'], ans: 0, exp: '事是侍奉、对待'},
  {q: '2. 「诸父」指的是谁？', opts: ['叔叔、伯伯等父辈', '只有自己的父亲', '老师的父亲'], ans: 0, exp: '父辈都称诸父'},
  {q: '3. 「如事父」的「如」是什么意思？', opts: ['像……一样', '如果', '如何'], ans: 0, exp: '如是像'},
  {q: '4. 「事诸父，如事父」讲什么？', opts: ['对待叔伯长辈，像对待父亲一样', '让叔叔当爸爸', '父亲的事都要替他做'], ans: 0, exp: '敬如敬父'},
  {q: '5. 「诸兄」指的是谁？', opts: ['堂哥、表哥等同辈兄长', '只有自己的哥哥', '邻居家的孩子'], ans: 0, exp: '兄辈都称诸兄'},
  {q: '6. 「事诸兄，如事兄」讲什么？', opts: ['对待堂表兄长，像对待哥哥一样', '跟哥哥吵架', '哥哥说什么都对'], ans: 0, exp: '让如让兄'},
  {q: '7. 遇到不认识的老人家，应该怎样？', opts: ['像对待自家长辈一样有礼', '装作没看见', '躲得远远的'], ans: 0, exp: '礼不挑人'},
  {q: '8. 这一段把礼的范围怎么了？', opts: ['放大了，从自家放到众人', '缩小到只有爸爸', '取消了'], ans: 0, exp: '敬放大一圈'},
  {q: '9. 表哥来做客，好玩的应该？', opts: ['先让表哥挑', '自己藏起来', '全部抢到手'], ans: 0, exp: '让如让兄'},
  {q: '10. 出则悌这一门总的讲什么？', opts: ['出门在外对长辈同辈的孝悌之礼', '在家怎么刷牙', '怎么考试拿高分'], ans: 0, exp: '出则悌收官'},
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
s = s.replace('《弟子规》第十三课', '《弟子规》第十四课')
s = s.replace('出则悌第五段', '出则悌第六段')
s = s.replace("window.GUOXUE_COURSE_ID = '553-zun-zhang-qian';", "window.GUOXUE_COURSE_ID = '554-shi-zhu-fu';")
s = s.replace('yaoyue554', 'yaoyue555')

# ---- 校验 ----
for w in ['尊长前', '声要低', '低不闻', '却非宜', '进必趋', '退必迟', '问起对', '视勿移',
          '出则悌第五段', '553-zun-zhang-qian', 'yaoyue554', '第十三课']:
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
