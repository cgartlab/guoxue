#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build539: 以 537 为骨架（常规 8 句 24 字）生成第 539 课《幼而学·壮而行》。

稳定法：按 1-based 行号整行替换文字，标签签名（属性值归一化）逐行比对；
生成后做逐行签名 + 全局标签计数双重校验。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/537-tang-liu-yan/index.html"
DST = ROOT + "/lessons/539-you-er-xue/index.html"

DESC = ('《三字经》第四十六课精讲：幼而学，壮而行。上致君，下泽民。'
        '扬名声，显父母。光于前，裕于后。'
        '上一课讲万物各守本分、人不学不如物，这一课接着讲学了做什么用：'
        '小时候用功读书（幼而学），长大把学的本事用出来（壮而行）；'
        '对上为国尽力、辅佐君上（上致君），对下施惠于百姓（下泽民）；'
        '名声传开，让父母也跟着荣耀（扬名声，显父母）；'
        '光耀先人，惠及后人（光于前，裕于后）。'
        '八句三言告诉孩子：读书不只是为自己，是立身的本分、做事的本事、对家国的担当。')

ORIG = '幼而学，壮而行。上致君，下泽民。扬名声，显父母。光于前，裕于后。'
ORIG_COMMA = '幼而学，壮而行，上致君，下泽民；扬名声，显父母，光于前，裕于后。'
COVER_SUB = '壮而行，上致君；下泽民，扬名声，显父母，裕于后'
COVER_DESC = ('上一课讲万物都尽本分、人不学不如物，这一课讲学了以后做什么：'
              '小时候读书，长大把本事用出来；对上为国尽力，对下惠及百姓；'
              '名声传开让父母荣耀，光耀先人也惠及后人。'
              '八句三言告诉孩子：学的用处，先从做人做事开始，再落到家与国。')

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('幼而学壮而行', ['yòu', 'ér', 'xué', 'zhuàng', 'ér', 'xíng'], True)
             + ju('上致君下泽民', ['shàng', 'zhì', 'jūn', 'xià', 'zé', 'mín'], False)
             + ju('扬名声显父母', ['yáng', 'míng', 'shēng', 'xiǎn', 'fù', 'mǔ'], False)
             + ju('光于前裕于后', ['guāng', 'yú', 'qián', 'yù', 'yú', 'hòu'], False))

NEW = {
6: '''<meta content="''' + DESC + '''" name="description"/>''',
7: '''<meta content="幼而学 · 壮而行，上致君 · 下泽民，扬名声 · 光于前 · 三字经课堂" property="og:title"/>''',
8: '''<meta content="《三字经》第四十六课：''' + ORIG + '''" property="og:description"/>''',
10: '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/539-you-er-xue/index.html" property="og:url"/>''',
11: '''<link href="https://guoxue.8023laozhanshi.cc/lessons/539-you-er-xue/index.html" rel="canonical"/>''',
12: '''<title>幼而学 · 壮而行，上致君 · 下泽民，扬名声 · 光于前 ·《三字经》国学问答 · 国学课堂</title>''',
52: '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">幼而学</h2><div class="cover-ornament"></div><p class="cover-subtitle">''' + COVER_SUB + '''</p><p class="cover-desc">''' + COVER_DESC + '''</p><div class="cover-seal">三字经</div></div>''',
55: RUBY_LINE,
60: '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>小时候用功读书，长大把学的用出来；对上为国尽力，对下惠及百姓；名声传开使父母荣耀，光耀先人也惠及后人。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》勤学段的收束处：由万物作比转到学的用处；后面讲「人遗子，金满籝」。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>''',
62: '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">幼而学</span>：<strong>幼是小时候，学是用功读书</strong>——<strong>学在幼时</strong>。</p><p><span class="ds-highlight">壮而行</span>：<strong>壮是壮年、成年，行是施行、做出来</strong>——<strong>学以致用</strong>。</p><p><span class="ds-highlight">上致君</span>：<strong>上是对上，致是尽力献上，君指君上国家</strong>——<strong>为国尽力</strong>。</p><p><span class="ds-highlight">下泽民</span>：<strong>下是对下，泽是恩惠、惠及</strong>——<strong>惠及百姓</strong>。</p><p><span class="ds-highlight">扬名声</span>：<strong>扬是传扬，名声是好的声誉</strong>——<strong>声誉远传</strong>。</p><p><span class="ds-highlight">显父母</span>：<strong>显是使父母荣耀</strong>——<strong>亲有所荣</strong>。</p><p><span class="ds-highlight">光于前</span>：<strong>光是光耀，前指先人前人</strong>——<strong>光耀先人</strong>。</p><p><span class="ds-highlight">裕于后</span>：<strong>裕是富足、遗惠，后指后人</strong>——<strong>惠及后人</strong>。</p><p><span class="ds-highlight">学为根本</span>：<strong>这几句全由「学」生出来</strong>——<strong>学以立身</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>''',
64: '''<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：幼而学，壮而行</h2><h3>" 幼 而 学 ， 壮 而 行 "</h3><p style="margin:0"><strong>「幼而学」怎么讲？</strong><br/><br/>① <strong>幼是小时候</strong><br/>② <strong>学是用功读书</strong><br/><br/><strong>一句话：学在幼时。</strong></p><p><strong>「壮而行」怎么讲？</strong><br/><br/>① <strong>壮是壮年、成年</strong><br/>② <strong>行是施行、做出来</strong><br/><br/><strong>一句话：学以致用。</strong></p><p><strong>两句的关系？</strong><br/><br/>① <strong>先学后用，前后相承</strong><br/>② <strong>学了不用，等于白学</strong><br/><br/><strong>一句话：学用相成。</strong></p></div>''',
66: '''<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：上致君，下泽民</h2><h3>" 上 致 君 ， 下 泽 民 "</h3><p style="margin:0"><strong>「上致君」怎么讲？</strong><br/><br/>① <strong>上是对上、对国</strong><br/>② <strong>致是尽力献上</strong><br/><br/><strong>一句话：为国尽力。</strong></p><p><strong>「下泽民」指什么？</strong><br/><br/>① <strong>下是对下、对百姓</strong><br/>② <strong>泽是恩惠、惠及</strong><br/><br/><strong>一句话：惠及百姓。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>学问不是关起门来的</strong><br/>② <strong>要落到做事、帮到人</strong><br/><br/><strong>一句话：学要济人。</strong></p></div>''',
68: '''<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：扬名声，显父母</h2><h3>" 扬 名 声 ， 显 父 母 "</h3><p style="margin:0"><strong>「扬名声」怎么讲？</strong><br/><br/>① <strong>扬是传扬</strong><br/>② <strong>名声是好的声誉</strong><br/><br/><strong>一句话：声誉远传。</strong></p><p><strong>「显父母」怎么讲？</strong><br/><br/>① <strong>显是使…荣耀</strong><br/>② <strong>不是给父母添名头</strong><br/><br/><strong>一句话：亲有所荣。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>做好人才有好名声</strong><br/>② <strong>名声先对得起自家</strong><br/><br/><strong>一句话：立身显亲。</strong></p></div>''',
70: '''<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：光于前，裕于后</h2><h3>" 光 于 前 ， 裕 于 后 "</h3><p style="margin:0"><strong>「光于前」怎么讲？</strong><br/><br/>① <strong>光是光耀</strong><br/>② <strong>前指先人、前人</strong><br/><br/><strong>一句话：光耀先人。</strong></p><p><strong>「裕于后」怎么讲？</strong><br/><br/>① <strong>裕是富足、遗惠</strong><br/>② <strong>后指后人、子孙</strong><br/><br/><strong>一句话：惠及后人。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>眼光要从自己看到前后</strong><br/>② <strong>学好做好，家国都受益</strong><br/><br/><strong>一句话：承前启后。</strong></p></div>''',
72: '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>''',
73: '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前四句讲幼学壮行、上致君下泽民，后四句讲扬名显亲、光前裕后。</p><p>📖 学以致用</p>''',
74: '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>读书不为装门面，要把本领用在做人和做事上。</p><p>💡 立身济人</p>''',
75: '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 学的用处</p>''',
76: '''<p>这是「三字经课堂」第四十六课：幼而学，壮而行。</p></div>''',
106: '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「壮而行」的壮是强壮吗？</h3><p><strong>不是，指壮年、成年。</strong><br/><br/>① <strong>壮是壮年</strong><br/>② <strong>行是施行、做出来</strong><br/>③ <strong>长大把学到的用上</strong><br/><br/><strong>记法：学以致用。</strong></p><h3>❓ 「上致君」今天怎么讲？</h3><p><strong>对国家社会尽自己的力量。</strong><br/><br/>① <strong>致是尽力献上</strong><br/>② <strong>君指君上国家</strong><br/>③ <strong>今天可解作为公家做事</strong><br/><br/><strong>记法：为国尽力。</strong></p><h3>❓ 「显父母」是让父母出名吗？</h3><p><strong>是让父母因你而光荣。</strong><br/><br/>① <strong>显是使…荣耀</strong><br/>② <strong>不是拿父母显摆</strong><br/>③ <strong>先做好人，名声才对</strong><br/><br/><strong>记法：立身显亲。</strong></p><h3>❓ 「光于前，裕于后」怎么理解？</h3><p><strong>对得起先人，也对得起后人。</strong><br/><br/>① <strong>光是光耀先人</strong><br/>② <strong>裕是遗惠后人</strong><br/>③ <strong>眼光看远一点</strong><br/><br/><strong>记法：承前启后。</strong></p></div>''',
108: '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这八句，给我们三样提醒——</p><p>📖 读书时就专心读书</p>''',
109: '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「幼而学」</strong>；<strong>小时候把该学的学到手，是给以后打底子</strong>。</p><p>💡 学了就要用出来</p>''',
110: '''<p style="margin:var(--ds-space-1) 0 0"><strong>「壮而行」讲的就是用</strong>；<strong>会背会写不算本事，能做出来才算</strong>。</p><p>🌱 做事想到别人</p>''',
111: '''<p style="margin:var(--ds-space-1) 0 0"><strong>「上致君，下泽民」教的是担当</strong>；<strong>能帮到人、对得住家国，学才不算白学</strong><br/><br/><strong>本课的落点：幼而学，壮而行。</strong></p></div>''',
113: '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第四十六课。记牢：<strong>幼而学，壮而行</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''',
114: '''            ''' + ORIG,
115: '''            </p><p>回顾本课要点:</p><p>幼而学，壮而行 · 小时候学，长大用出来。<strong>学以致用。</strong></p><p>上致君，下泽民 · 对上为国尽力，对下惠及百姓。<strong>学要济人。</strong></p><p>扬名声，显父母 · 名声传开，父母也荣耀。<strong>立身显亲。</strong></p><p>光于前，裕于后 · 光耀先人，惠及后人。<strong>承前启后。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲万物各守本分、人不学不如物，这一课讲幼学壮行、上致君下泽民，下一课接着讲「人遗子，金满籝」。</p><div class="ds-quote">''',
117: '''<p>''' + ORIG + '''</p>''',
118: '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「壮而行」的壮怎么讲。③ 讲讲「光于前，裕于后」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>''',
125: '''            "''' + ORIG + '''"<br/>''',
133: '''    window.GUOXUE_COURSE_ID = '539-you-er-xue';''',
136: '''  {q: '1. 「幼而学，壮而行」怎么讲？', opts: ['小时候读书，长大把学的用出来', '幼年玩耍，壮年读书', '年轻时学，老了忘'], ans: 0, exp: '学以致用'},''',
137: '''  {q: '2. 「壮而行」的壮怎么讲？', opts: ['壮年、成年', '强壮有力', '壮大'], ans: 0, exp: '壮指壮年'},''',
138: '''  {q: '3. 「壮而行」的行怎么讲？', opts: ['施行、做出来', '行走', '行列'], ans: 0, exp: '行是施行'},''',
139: '''  {q: '4. 「上致君」的致怎么讲？', opts: ['尽力献上', '送到', '细致'], ans: 0, exp: '致是尽力'},''',
140: '''  {q: '5. 「下泽民」的泽怎么讲？', opts: ['恩惠、惠及', '水泽湖泊', '光泽'], ans: 0, exp: '泽是恩惠'},''',
141: '''  {q: '6. 「扬名声」的扬怎么讲？', opts: ['传扬', '扬起尘土', '表扬别人'], ans: 0, exp: '扬是传扬'},''',
142: '''  {q: '7. 「显父母」的显怎么讲？', opts: ['使父母荣耀', '显露出来', '明显'], ans: 0, exp: '显是使…荣耀'},''',
143: '''  {q: '8. 「裕于后」的裕怎么讲？', opts: ['富足、遗惠后人', '宽裕有余', '富裕人家'], ans: 0, exp: '裕是遗惠'},''',
144: '''  {q: '9. 这八句讲的是学的什么？', opts: ['学的用处：做人做事、对家国担当', '读书的方法', '写字的要求'], ans: 0, exp: '讲学的用处'},''',
145: '''  {q: '10. 与上一课的关系？', opts: ['上节课讲不学不如物，这一课讲学了怎么用', '讲朝代更替', '讲三皇五帝'], ans: 0, exp: '劝学递进'},''',
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
out = out.replace('yaoyue539', 'yaoyue540')
out = out.replace('537-tang-liu-yan', '539-you-er-xue')


def counts(s):
    return {k: s.count(k) for k in ['<div', '</div>', '<p', '</p>', '<ruby', '<h2', '</h2>', '<h3', '</h3>',
                                    'data-page="', "{q: '", '<rt>']}
c1, c2 = counts(raw), counts(out)
if c1 != c2:
    print('[FAIL] 全局标签计数不一致:', c1, c2)
    sys.exit(1)
print('[OK] 全局标签计数一致:', c2)

resid = ['第四十四课', '唐刘晏', '方七岁', '举神童', '作正字', '勉而致', 'yaoyue539', '537-tang-liu-yan']
left = {w: out.count(w) for w in resid if out.count(w)}
if left:
    print('[FAIL] 上一课残留:', left)
    sys.exit(1)
print('[OK] 上一课文字零残留')

os.makedirs(os.path.dirname(DST), exist_ok=True)
io.open(DST, 'w', encoding='utf-8', newline='').write(out)
print('[OK] 已生成', DST)
