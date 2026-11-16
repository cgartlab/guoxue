#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build559: 以 558 课件（八句版式）为模板生成第 559 课《谨·勿践阈，勿跛倚》。
「谨」第五段整段八句：前四句讲坐立禁忌（勿践阈、勿跛倚、勿箕踞、勿摇髀），
后四句讲动作轻缓（缓揭帘、勿有声、宽转弯、勿触棱）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（姿势稳重，动作轻缓）/ 3 勿践阈勿跛倚·勿箕踞勿摇髀 /
  4 缓揭帘勿有声·宽转弯勿触棱 / 5 两句合看（稳与轻）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/558-bu-cong-rong/index.html"
DST = ROOT + "/lessons/559-wu-jian-yu/index.html"

TITLE = '谨 · 勿践阈，勿跛倚，缓揭帘，勿有声 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '勿践阈，勿跛倚；缓揭帘，勿有声 · 弟子规课堂'
DESC = ('《弟子规》第十九课，谨第五段。原文：「勿践阈，勿跛倚。勿箕踞，勿摇髀。'
        '缓揭帘，勿有声。宽转弯，勿触棱。」前四句讲坐立规矩：不踩门槛、不斜靠墙、'
        '不叉腿坐、不抖腿；后四句讲做事轻缓：掀帘开门都轻手轻脚，转弯绕大弯不碰棱角。')
OG_DESC = '《弟子规》第十九课：勿践阈勿跛倚，缓揭帘勿有声。谨第五段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/559-wu-jian-yu/index.html'

ORIG = '勿践阈，勿跛倚。勿箕踞，勿摇髀。缓揭帘，勿有声。宽转弯，勿触棱。'
ORIG_COMMA = '勿践阈，勿跛倚；勿箕踞，勿摇髀；缓揭帘，勿有声；宽转弯，勿触棱。'
OLD_ORIG = '年方少，勿饮酒。饮酒醉，最为丑。步从容，立端正。揖深圆，拜恭敬。'
OLD_ORIG_COMMA = '年方少，勿饮酒；饮酒醉，最为丑；步从容，立端正；揖深圆，拜恭敬。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('勿践阈勿跛倚', ['wù', 'jiàn', 'yù', 'wù', 'bǒ', 'yǐ'], True)
             + ju('勿箕踞勿摇髀', ['wù', 'jī', 'jù', 'wù', 'yáo', 'bì'], False)
             + ju('缓揭帘勿有声', ['huǎn', 'jiē', 'lián', 'wù', 'yǒu', 'shēng'], False)
             + ju('宽转弯勿触棱', ['kuān', 'zhuǎn', 'wān', 'wù', 'chù', 'léng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">勿践阈</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第五段：勿践阈，勿跛倚</p><p class="cover-desc">谨门第五段讲两件事：姿势稳重、动作轻缓。不踩门槛、不歪靠、不叉腿、不抖腿；掀帘子慢慢来，转弯绕大弯不碰棱角。稳稳当当，轻手轻脚。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第五段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>不要踩门槛，不要歪着身子斜靠；不要叉开腿坐，不要抖腿。掀帘子要慢慢来，不要弄出声响；转弯要绕大弯，不要碰到棱角。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「阈」读 yù，是门槛；「跛倚」是歪着身子斜靠；「箕踞」是叉开两腿坐着，像簸箕一样；「髀」读 bì，是大腿，「摇髀」就是抖腿；「缓」是慢；「帘」是门帘；「棱」读 léng，是桌角墙角这些棱角。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 姿势稳重，动作轻缓</h2><p style="margin:0"><strong>先说「坐立」</strong><br/>① <strong>四个「勿」，都是不雅的样子</strong><br/>② <strong>站有站相，坐有坐相</strong><br/><br/><strong>一句话：稳稳当当。</strong></p><p><strong>再说「动作」</strong><br/>① <strong>掀帘、开门、转弯都轻缓</strong><br/>② <strong>不打扰别人，也不碰伤自己</strong><br/><br/><strong>一句话：轻手轻脚。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>稳是自己的修养，轻是替别人着想</strong><br/>② <strong>样子稳、动静轻，人就有精神</strong><br/><br/><strong>一句话：稳中有轻。</strong></p></div>
<!-- 4. 勿践阈勿跛倚·勿箕踞勿摇髀 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>勿践阈，勿跛倚；勿箕踞，勿摇髀</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>阈 yù：门槛；跛倚：歪身斜靠</strong><br/>② <strong>箕踞：叉腿坐；髀 bì：大腿</strong><br/><br/><strong>一句话：四个「勿」，四个不雅。</strong></p><p><strong>勿践阈，勿跛倚</strong><br/>① <strong>进门抬脚跨过去，不踩门槛</strong><br/>② <strong>站着别歪着身子靠墙靠门</strong><br/><br/><strong>一句话：站要站得像样。</strong></p><p><strong>勿箕踞，勿摇髀</strong><br/>① <strong>坐着两腿并好，不叉开</strong><br/>② <strong>腿不抖、脚不晃，坐着也安静</strong><br/><br/><strong>一句话：坐相也是教养。</strong></p></div>
<!-- 5. 缓揭帘勿有声·宽转弯勿触棱 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>缓揭帘，勿有声；宽转弯，勿触棱</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>缓：慢慢来；帘：门帘</strong><br/>② <strong>棱 léng：桌角墙角的尖角</strong><br/><br/><strong>一句话：动作要轻，路线要宽。</strong></p><p><strong>缓揭帘，勿有声</strong><br/>① <strong>掀帘子慢慢掀，不啪的一声</strong><br/>② <strong>开门关门窗也一样，轻手轻脚</strong><br/><br/><strong>一句话：轻，是替别人着想。</strong></p><p><strong>宽转弯，勿触棱</strong><br/>① <strong>拐弯时绕大弯，离桌角墙角远些</strong><br/>② <strong>又碰不伤自己，也不撞翻东西</strong><br/><br/><strong>一句话：转弯留余地。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 稳与轻</h2><p style="margin:0"><strong>前四句讲「稳」</strong><br/>① <strong>不踩、不靠、不叉、不抖</strong><br/>② <strong>坐立都有规矩，样子才端正</strong><br/><br/><strong>一句话：稳稳当当。</strong></p><p><strong>后四句讲「轻」</strong><br/>① <strong>动作慢一点，路线宽一点</strong><br/>② <strong>不打扰人、不碰伤人</strong><br/><br/><strong>一句话：轻手轻脚。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>坐着两腿并好，走路拐弯慢下来</strong><br/>② <strong>开门掀帘都轻轻的，不摔不撞</strong><br/><br/><strong>一句话：稳中有轻。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：坐立要稳</strong><br/>① <strong>勿践阈，勿跛倚——不踩不靠</strong><br/>② <strong>勿箕踞，勿摇髀——不叉不抖</strong><br/><br/><strong>一句话：站坐像样。</strong></p><p><strong>后四句：动作要轻</strong><br/>① <strong>缓揭帘，勿有声——轻拿轻放</strong><br/>② <strong>宽转弯，勿触棱——绕大弯不碰角</strong><br/><br/><strong>一句话：轻缓有分寸。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>不踩门槛、不靠墙、不叉腿、不抖腿</strong><br/>② <strong>掀帘轻、转弯宽</strong><br/><br/><strong>一句话：稳稳当当，轻手轻脚。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>坐立姿势稳重，做事动作轻缓。</p><p>📖 举止有度</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>稳是自己的修养，轻是替别人着想。</p><p>💡 稳中有轻</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 勿践阈，勿跛倚</p>
<p>这是「弟子规课堂」第十九课：谨第五段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 为什么不能踩门槛？</h3><p><strong>门槛是界限，踩了不敬也不安全。</strong><br/><br/>① <strong>阈读 yù，就是门槛</strong><br/>② <strong>进门抬脚跨过去，是规矩也是礼貌</strong><br/>③ <strong>记法：抬脚过门，不踩不站。</strong></p><h3>❓ 「箕踞」「摇髀」说的是什么？</h3><p><strong>坐相的两条忌讳。</strong><br/><br/>① <strong>箕踞：叉开两腿坐，像簸箕，很失礼</strong><br/>② <strong>摇髀：抖腿，髀读 bì，是大腿</strong><br/>③ <strong>记法：腿并好，不抖不晃。</strong></p><h3>❓ 「缓揭帘」为什么要慢？</h3><p><strong>掀得太急，啪的一声吓人一跳。</strong><br/><br/>① <strong>急掀帘子会打到旁边的人</strong><br/>② <strong>开门摔门也一样，动静吵人</strong><br/>③ <strong>记法：慢一点，静一点，替别人着想。</strong></p><h3>❓ 「宽转弯，勿触棱」说什么？</h3><p><strong>转弯要绕大弯，离棱角远一点。</strong><br/><br/>① <strong>棱读 léng，是桌角墙角的尖角</strong><br/>② <strong>绕大弯，碰不伤自己也撞不翻东西</strong><br/>③ <strong>记法：转弯留余地。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 坐立都有坐相站相</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不踩门槛不靠墙，两腿并好不抖腿</strong>；<strong>这就是「勿践阈」到「勿摇髀」</strong>。</p><p>💡 开门掀帘轻手轻脚</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不摔门、慢慢掀帘子，不弄出怪声</strong>；<strong>这就是「缓揭帘，勿有声」</strong>。</p><p>🌱 拐弯慢下来绕大弯</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>走廊拐角离桌角墙角远些</strong>；<strong>这就是「宽转弯，勿触棱」</strong><br/><br/><strong>本课的落点：稳稳当当，轻手轻脚。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第五段。记牢：<strong>勿践阈，勿跛倚</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第五段 · 姿势稳重，动作轻缓。<strong>稳中有轻</strong>。</p><p>勿践阈，勿跛倚 · 不踩门槛不斜靠。<strong>站得像样</strong>。</p><p>勿箕踞，勿摇髀 · 不叉腿不抖腿。<strong>坐相是教养</strong>。</p><p>缓揭帘，勿有声 · 掀帘开门都轻缓。<strong>动静有分寸</strong>。</p><p>宽转弯，勿触棱 · 转弯绕大弯。<strong>不碰棱角</strong>。</p><p><strong>在全篇中的位置:</strong>谨第五段；上一课讲不贪杯和站走行礼的端正，这一课讲坐卧规矩和做事轻缓。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「阈」「髀」「棱」怎么读。② 开门关门轻手轻脚一次。③ 走廊拐角慢下来，绕个大弯。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「勿践阈」的「阈」是什么意思？', opts: ['门槛', '门框', '院子'], ans: 0, exp: '阈读 yù，是门槛'},
  {q: '2. 「勿跛倚」讲什么？', opts: ['不歪着身子靠墙站', '不瘸着腿走路', '不倚老卖老'], ans: 0, exp: '不斜靠'},
  {q: '3. 「勿箕踞」的「箕踞」是什么样的坐姿？', opts: ['叉开两腿坐', '盘腿坐', '跪着坐'], ans: 0, exp: '叉腿坐不雅'},
  {q: '4. 「勿摇髀」的「髀」是什么意思？', opts: ['大腿', '膝盖', '脚趾'], ans: 0, exp: '髀读 bì，是大腿'},
  {q: '5. 「缓揭帘」的「缓」是什么意思？', opts: ['缓慢、轻缓', '简单', '松开'], ans: 0, exp: '缓是慢慢来'},
  {q: '6. 「勿有声」讲什么？', opts: ['掀帘子不要弄出声响', '不许说话', '不许唱歌'], ans: 0, exp: '动作要轻不出声'},
  {q: '7. 「宽转弯」是什么意思？', opts: ['转弯时绕大一点', '路宽才好转弯', '转弯要快'], ans: 0, exp: '绕大弯留余地'},
  {q: '8. 「勿触棱」的「棱」指什么？', opts: ['桌角墙角等棱角', '屋檐', '栏杆'], ans: 0, exp: '棱读 léng，是尖角'},
  {q: '9. 开门关窗应该怎样？', opts: ['轻手轻脚，不摔不撞', '力气越大越好', '随手一甩'], ans: 0, exp: '轻手轻脚'},
  {q: '10. 这一段总的讲什么？', opts: ['坐立姿势稳重，做事动作轻缓', '怎么走路最快', '怎么坐最舒服'], ans: 0, exp: '稳中有轻'},
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
s = s.replace('《弟子规》第十八课', '《弟子规》第十九课')
s = s.replace('谨第四段', '谨第五段')
s = s.replace("window.GUOXUE_COURSE_ID = '558-bu-cong-rong';", "window.GUOXUE_COURSE_ID = '559-wu-jian-yu';")
s = s.replace('yaoyue560', 'yaoyue561')

# ---- 校验 ----
for w in ['年方少，勿饮酒', '饮酒醉，最为丑', '步从容，立端正', '揖深圆，拜恭敬',
          '年方少，勿饮酒；', '谨第四段', '558-bu-cong-rong', 'yaoyue560', '第十八课']:
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
