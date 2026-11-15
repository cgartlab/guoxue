#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build540: 以 539 为骨架（常规 8 句 24 字）生成第 540 课《人遗子·金满籝》。

《三字经》全篇收官课。稳定法同前：整行替换 + 逐行标签签名 + 全局计数双校验。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/539-you-er-xue/index.html"
DST = ROOT + "/lessons/540-ren-yi-zi/index.html"

DESC = ('《三字经》第四十七课精讲：人遗子，金满籝。我教子，惟一经。'
        '勤有功，戏无益。戒之哉，宜勉力。'
        '这是《三字经》的收尾一课：上一课讲幼学壮行、光前裕后，这一课把话说完——'
        '别人给子孙留的是满箱金银（人遗子，金满籝），我教子孙的只有一部经书（我教子，惟一经）；'
        '因为勤勉才有成效（勤有功），嬉戏贪玩没有好处（戏无益）；'
        '所以要警戒自己（戒之哉），好好用功（宜勉力）。'
        '八句三言告诉孩子：留给后人最要紧的不是钱财，是读书向学的道理。')

ORIG = '人遗子，金满籝。我教子，惟一经。勤有功，戏无益。戒之哉，宜勉力。'
ORIG_COMMA = '人遗子，金满籝，我教子，惟一经；勤有功，戏无益，戒之哉，宜勉力。'
COVER_SUB = '金满籝，我教子；惟一经，勤有功，戏无益，宜勉力'
COVER_DESC = ('上一课讲幼学壮行、光耀先人惠及后人，这一课是全篇收尾：'
              '别人给子孙留满箱金银，我教子孙的只有一部经书；勤勉才有成效，嬉戏没有好处；'
              '所以要警戒自己，好好用功。'
              '八句三言告诉孩子：留给后人最要紧的不是钱财，是读书向学的道理。')

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('人遗子金满籝', ['rén', 'yí', 'zǐ', 'jīn', 'mǎn', 'yíng'], True)
             + ju('我教子惟一经', ['wǒ', 'jiào', 'zǐ', 'wéi', 'yī', 'jīng'], False)
             + ju('勤有功戏无益', ['qín', 'yǒu', 'gōng', 'xì', 'wú', 'yì'], False)
             + ju('戒之哉宜勉力', ['jiè', 'zhī', 'zāi', 'yí', 'miǎn', 'lì'], False))

NEW = {
6: '''<meta content="''' + DESC + '''" name="description"/>''',
7: '''<meta content="人遗子 · 金满籝，我教子 · 惟一经，勤有功 · 戒之哉 · 三字经课堂" property="og:title"/>''',
8: '''<meta content="《三字经》第四十七课：''' + ORIG + '''" property="og:description"/>''',
10: '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/540-ren-yi-zi/index.html" property="og:url"/>''',
11: '''<link href="https://guoxue.8023laozhanshi.cc/lessons/540-ren-yi-zi/index.html" rel="canonical"/>''',
12: '''<title>人遗子 · 金满籝，我教子 · 惟一经，勤有功 · 戒之哉 ·《三字经》国学问答 · 国学课堂</title>''',
52: '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">人遗子</h2><div class="cover-ornament"></div><p class="cover-subtitle">''' + COVER_SUB + '''</p><p class="cover-desc">''' + COVER_DESC + '''</p><div class="cover-seal">三字经</div></div>''',
55: RUBY_LINE,
60: '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>别人给子孙留满箱金银，我教子孙的只有一部经书；勤勉才有成效，嬉戏没有好处；警戒自己，好好用功。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》全篇收尾，把「学」落到家教与勉力上；自此全篇讲完。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>''',
62: '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">人遗子</span>：<strong>遗是留给，人是别人</strong>——<strong>他人留财</strong>。</p><p><span class="ds-highlight">金满籝</span>：<strong>籝是竹箱，装金银的箱子</strong>——<strong>满箱财宝</strong>。</p><p><span class="ds-highlight">我教子</span>：<strong>教是教导，子指子孙</strong>——<strong>我的教法</strong>。</p><p><span class="ds-highlight">惟一经</span>：<strong>惟是只，经指经书</strong>——<strong>只传一经</strong>。</p><p><span class="ds-highlight">勤有功</span>：<strong>勤是勤勉，功是成效</strong>——<strong>勤则有成</strong>。</p><p><span class="ds-highlight">戏无益</span>：<strong>戏是嬉戏贪玩，益是好处</strong>——<strong>玩则无得</strong>。</p><p><span class="ds-highlight">戒之哉</span>：<strong>戒是警戒，哉是语气词</strong>——<strong>自我告诫</strong>。</p><p><span class="ds-highlight">宜勉力</span>：<strong>宜是应该，勉力是努力</strong>——<strong>好好用功</strong>。</p><p><span class="ds-highlight">收尾之意</span>：<strong>全篇最后四句，把劝学落到底</strong>——<strong>勉力向学</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>''',
64: '''<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：人遗子，金满籝</h2><h3>" 人 遗 子 ， 金 满 籝 "</h3><p style="margin:0"><strong>「人遗子」怎么讲？</strong><br/><br/>① <strong>遗是留给</strong><br/>② <strong>人指别人、世人</strong><br/><br/><strong>一句话：他人留财。</strong></p><p><strong>「金满籝」怎么讲？</strong><br/><br/>① <strong>籝是竹箱</strong><br/>② <strong>满箱金银，家产丰厚</strong><br/><br/><strong>一句话：满箱财宝。</strong></p><p><strong>两句的关系？</strong><br/><br/>① <strong>先说世人怎么留</strong><br/>② <strong>为下文作对比</strong><br/><br/><strong>一句话：先摆世情。</strong></p></div>''',
66: '''<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：我教子，惟一经</h2><h3>" 我 教 子 ， 惟 一 经 "</h3><p style="margin:0"><strong>「我教子」怎么讲？</strong><br/><br/>① <strong>教是教导</strong><br/>② <strong>子指子孙后人</strong><br/><br/><strong>一句话：我的教法。</strong></p><p><strong>「惟一经」指什么？</strong><br/><br/>① <strong>惟是只、仅</strong><br/>② <strong>一部经书，指圣贤之书</strong><br/><br/><strong>一句话：只传一经。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>留钱不如留学问</strong><br/>② <strong>读书明理才守得住家</strong><br/><br/><strong>一句话：遗经胜遗金。</strong></p></div>''',
68: '''<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：勤有功，戏无益</h2><h3>" 勤 有 功 ， 戏 无 益 "</h3><p style="margin:0"><strong>「勤有功」怎么讲？</strong><br/><br/>① <strong>勤是勤勉用功</strong><br/>② <strong>功是成效、长进</strong><br/><br/><strong>一句话：勤则有成。</strong></p><p><strong>「戏无益」怎么讲？</strong><br/><br/>① <strong>戏是嬉戏贪玩</strong><br/>② <strong>益是好处</strong><br/><br/><strong>一句话：玩则无得。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>一正一反说得明白</strong><br/>② <strong>不是不许玩，是别贪玩</strong><br/><br/><strong>一句话：勤戏分明。</strong></p></div>''',
70: '''<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：戒之哉，宜勉力</h2><h3>" 戒 之 哉 ， 宜 勉 力 "</h3><p style="margin:0"><strong>「戒之哉」怎么讲？</strong><br/><br/>① <strong>戒是警戒、告诫</strong><br/>② <strong>哉是语气词，加重口气</strong><br/><br/><strong>一句话：自我告诫。</strong></p><p><strong>「宜勉力」怎么讲？</strong><br/><br/>① <strong>宜是应该</strong><br/>② <strong>勉力是努力去做</strong><br/><br/><strong>一句话：好好用功。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>全篇最后一句是催人</strong><br/>② <strong>道理说完，就靠去做</strong><br/><br/><strong>一句话：勉力向学。</strong></p></div>''',
72: '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>''',
73: '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>先比「留金」与「留经」，再说勤有功、戏无益。</p><p>📖 遗经胜遗金</p>''',
74: '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>留给后人最要紧的不是钱财，是读书向学的道理。</p><p>💡 勤勉为本</p>''',
75: '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 勉力向学</p>''',
76: '''<p>这是「三字经课堂」第四十七课：人遗子，金满籝。</p></div>''',
106: '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「籝」是什么？</h3><p><strong>装东西的竹箱。</strong><br/><br/>① <strong>竹编的箱子</strong><br/>② <strong>「金满籝」指满箱金银</strong><br/>③ <strong>今天可解作家产</strong><br/><br/><strong>记法：满箱财宝。</strong></p><h3>❓ 「惟一经」是只读一本书吗？</h3><p><strong>是以一部经书为本。</strong><br/><br/>① <strong>惟是只、仅</strong><br/>② <strong>经指圣贤之书</strong><br/>③ <strong>意思是留学问不留钱财</strong><br/><br/><strong>记法：遗经胜遗金。</strong></p><h3>❓ 「戏无益」是不让孩子玩吗？</h3><p><strong>不是，是别因贪玩误了学。</strong><br/><br/>① <strong>戏指嬉戏贪玩</strong><br/>② <strong>益是好处</strong><br/>③ <strong>玩要有度，学要有恒</strong><br/><br/><strong>记法：勤戏分明。</strong></p><h3>❓ 为什么用「戒之哉」收尾？</h3><p><strong>全篇道理说完，最后催人去做。</strong><br/><br/>① <strong>戒是警戒自己</strong><br/>② <strong>哉是加重口气</strong><br/>③ <strong>宜勉力就是该用功了</strong><br/><br/><strong>记法：勉力向学。</strong></p></div>''',
108: '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这八句，给我们三样提醒——</p><p>📖 给孩子留本事，别只留东西</p>''',
109: '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「人遗子，金满籝；我教子，惟一经」</strong>；<strong>钱财会用尽，读书的本事跟一辈子</strong>。</p><p>💡 勤快比聪明更要紧</p>''',
110: '''<p style="margin:var(--ds-space-1) 0 0"><strong>「勤有功，戏无益」说得直白</strong>；<strong>每天读一点、练一点，长进就看得见</strong>。</p><p>🌱 从今天起就勉力</p>''',
111: '''<p style="margin:var(--ds-space-1) 0 0"><strong>「戒之哉，宜勉力」是全篇最后一句</strong>；<strong>道理听懂了不算完，动手去做才算</strong><br/><br/><strong>本课的落点：人遗子，金满籝。</strong></p></div>''',
113: '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第四十七课。记牢：<strong>人遗子，金满籝</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''',
114: '''            ''' + ORIG,
115: '''            </p><p>回顾本课要点:</p><p>人遗子，金满籝 · 别人给子孙留满箱金银。<strong>先摆世情。</strong></p><p>我教子，惟一经 · 我教子孙的只有一部经书。<strong>遗经胜遗金。</strong></p><p>勤有功，戏无益 · 勤勉才有成效，贪玩没有好处。<strong>勤戏分明。</strong></p><p>戒之哉，宜勉力 · 警戒自己，好好用功。<strong>勉力向学。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲小时候读书、长大把本事用出来，这一课是全篇收尾：留金不如留经，勤有功、戏无益，最后以「宜勉力」催人向学。《三字经》至此讲完。</p><div class="ds-quote">''',
117: '''<p>''' + ORIG + '''</p>''',
118: '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「籝」和「惟」怎么讲。③ 讲讲「遗经胜遗金」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>''',
125: '''            "''' + ORIG + '''"<br/>''',
133: '''    window.GUOXUE_COURSE_ID = '540-ren-yi-zi';''',
136: '''  {q: '1. 「人遗子，金满籝」怎么讲？', opts: ['别人给子孙留满箱金银', '人人都有金箱子', '金子装满了竹篮'], ans: 0, exp: '先摆世情'},''',
137: '''  {q: '2. 「籝」是什么？', opts: ['装东西的竹箱', '金子做的盆', '一种酒器'], ans: 0, exp: '籝是竹箱'},''',
138: '''  {q: '3. 「我教子，惟一经」的惟怎么讲？', opts: ['只、仅', '思考', '唯一的人'], ans: 0, exp: '惟是只'},''',
139: '''  {q: '4. 「惟一经」的经指什么？', opts: ['圣贤的经书', '经过的事', '经线'], ans: 0, exp: '经指经书'},''',
140: '''  {q: '5. 「遗经胜遗金」是什么意思？', opts: ['留学问比留钱财更要紧', '经书比金子贵', '把书换成钱'], ans: 0, exp: '留本事'},''',
141: '''  {q: '6. 「勤有功」的功怎么讲？', opts: ['成效、长进', '功劳簿', '功夫'], ans: 0, exp: '功是成效'},''',
142: '''  {q: '7. 「戏无益」的戏怎么讲？', opts: ['嬉戏贪玩', '唱戏', '游戏规则'], ans: 0, exp: '戏是贪玩'},''',
143: '''  {q: '8. 「戒之哉」的戒怎么讲？', opts: ['警戒、告诫', '戒尺', '戒指'], ans: 0, exp: '戒是警戒'},''',
144: '''  {q: '9. 「宜勉力」的宜怎么讲？', opts: ['应该', '便宜', '适宜的地方'], ans: 0, exp: '宜是应该'},''',
145: '''  {q: '10. 这一课在《三字经》里的位置？', opts: ['全篇收尾，催人勉力向学', '开头总纲', '讲历史朝代'], ans: 0, exp: '全篇收官'},''',
}


def tag_sig(line):
    """只比较标签名/属性名结构，属性值（含正文文案）归一化。"""
    out = []
    for t in re.findall(r'<[^>]*>', line):
        t = re.sub(r'="[^"]*"', '=""', t)
        t = re.sub(r"='[^']*'", "=''", t)
        out.append(t)
    return out


raw = io.open(SRC, 'r', encoding='utf-8', newline='').read()
nl = '\r\n' if '\r\n' in raw else '\n'
lines = raw.split(nl)

bad = []
for n, new in NEW.items():
    old = lines[n - 1]
    if tag_sig(old) != tag_sig(new):
        bad.append((n, len(tag_sig(old)), len(tag_sig(new))))
        o, w = tag_sig(old), tag_sig(new)
        for i in range(min(len(o), len(w))):
            if o[i] != w[i]:
                bad.append((n, 'first diff', i, o[i], w[i]))
                break
if bad:
    print('[FAIL] 逐行标签签名不一致:', bad[:8])
    sys.exit(1)
print('[OK] 逐行标签签名全部一致 (%d 行)' % len(NEW))

for n, new in NEW.items():
    lines[n - 1] = new
out = nl.join(lines)
out = out.replace('yaoyue540', 'yaoyue541')
out = out.replace('539-you-er-xue', '540-ren-yi-zi')


def counts(s):
    return {k: s.count(k) for k in ['<div', '</div>', '<p', '</p>', '<ruby', '<h2', '</h2>', '<h3', '</h3>',
                                    'data-page="', "{q: '", '<rt>']}
c1, c2 = counts(raw), counts(out)
if c1 != c2:
    print('[FAIL] 全局标签计数不一致:', c1, c2)
    sys.exit(1)
print('[OK] 全局标签计数一致:', c2)

resid = ['第四十六课', '幼而学', '壮而行', '上致君', '下泽民', '裕于后', 'yaoyue540', '539-you-er-xue']
left = {w: out.count(w) for w in resid if out.count(w)}
if left:
    print('[FAIL] 上一课残留:', left)
    sys.exit(1)
print('[OK] 上一课文字零残留')

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(out)
print('[OK] 已生成', DST)
