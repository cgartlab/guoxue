#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build558_v2: 按陈老师指派重做第 558 课《谨·年方少，勿饮酒》。
「谨」第四段整段八句：前四句讲不贪杯（年方少、勿饮酒、饮酒醉、最为丑），
后四句讲站走行礼（步从容、立端正、揖深圆、拜恭敬）。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（管住嘴，立起身）/ 3 年方少勿饮酒·饮酒醉最为丑 /
  4 步从容立端正·揖深圆拜恭敬 / 5 两句合看（不贪杯与姿态正）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/557-yi-gui-jie/index.html"
DST = ROOT + "/lessons/558-bu-cong-rong/index.html"

TITLE = '谨 · 年方少，勿饮酒，步从容，立端正 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '年方少，勿饮酒；步从容，立端正 · 弟子规课堂'
DESC = ('《弟子规》第十八课，谨第四段。原文：「年方少，勿饮酒。饮酒醉，最为丑。'
        '步从容，立端正。揖深圆，拜恭敬。」前四句讲小孩子不喝酒，喝醉了样子最难看；'
        '后四句讲走路从容、站得端正，作揖要深圆、行礼要恭敬。管住嘴，立起身。')
OG_DESC = '《弟子规》第十八课：年方少勿饮酒，步从容立端正。谨第四段。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/558-bu-cong-rong/index.html'

ORIG = '年方少，勿饮酒。饮酒醉，最为丑。步从容，立端正。揖深圆，拜恭敬。'
ORIG_COMMA = '年方少，勿饮酒；饮酒醉，最为丑；步从容，立端正；揖深圆，拜恭敬。'
OLD_ORIG = '衣贵洁，不贵华。上循分，下称家。对饮食，勿拣择。食适可，勿过则。'
OLD_ORIG_COMMA = '衣贵洁，不贵华；上循分，下称家；对饮食，勿拣择；食适可，勿过则。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('年方少勿饮酒', ['nián', 'fāng', 'shào', 'wù', 'yǐn', 'jiǔ'], True)
             + ju('饮酒醉最为丑', ['yǐn', 'jiǔ', 'zuì', 'zuì', 'wéi', 'chǒu'], False)
             + ju('步从容立端正', ['bù', 'cóng', 'róng', 'lì', 'duān', 'zhèng'], False)
             + ju('揖深圆拜恭敬', ['yī', 'shēn', 'yuán', 'bài', 'gōng', 'jìng'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">年方少</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》谨第四段：年方少，勿饮酒</p><p class="cover-desc">谨门第四段讲两件事：管住嘴、立起身。小孩子不喝酒，喝醉了样子最难看；走路从容、站得端正，行礼要恭敬。嘴上不贪，身上有相。</p><div class="cover-seal">谨</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 谨第四段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>年纪还小，不要喝酒；喝醉了，样子最丑。走路要从容不慌，站立要端正；作揖要弯得深、抱得圆，行礼要恭恭敬敬。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「方」是正当；「少」读 shào，是年纪小；「醉」是喝酒过了头；「丑」是难看；「从容」是不慌不忙；「揖」读 yī，是作揖行礼；「深圆」是弯腰要深、抱手要圆；「拜」是跪拜行礼。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 管住嘴，立起身</h2><p style="margin:0"><strong>先说「管住嘴」</strong><br/>① <strong>小孩子不喝酒，身体还在长</strong><br/>② <strong>喝醉了失态，还容易闯祸</strong><br/><br/><strong>一句话：不贪杯。</strong></p><p><strong>再说「立起身」</strong><br/>① <strong>走要从容，站要端正</strong><br/>② <strong>行礼要弯得下去，敬在心里</strong><br/><br/><strong>一句话：稳当有敬。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>嘴上不贪，身上有相</strong><br/>② <strong>样子正，人就正</strong><br/><br/><strong>一句话：管住嘴，立起身。</strong></p></div>
<!-- 4. 年方少勿饮酒·饮酒醉最为丑 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>年方少，勿饮酒；饮酒醉，最为丑</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>少 shào：年纪小；醉：喝过了头</strong><br/>② <strong>丑：难看，是失态不是长相</strong><br/><br/><strong>一句话：小孩子不碰酒。</strong></p><p><strong>年方少，勿饮酒</strong><br/>① <strong>年纪小，身体在长，酒伤身体</strong><br/>② <strong>做客赴宴也不贪杯，以茶水代</strong><br/><br/><strong>一句话：不学大人喝酒。</strong></p><p><strong>饮酒醉，最为丑</strong><br/>① <strong>醉了说胡话、走路歪，最难看</strong><br/>② <strong>醉态失礼，还容易出事</strong><br/><br/><strong>一句话：醉态最失礼。</strong></p></div>
<!-- 5. 步从容立端正·揖深圆拜恭敬 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>步从容，立端正；揖深圆，拜恭敬</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>从容：不慌不忙；端正：直而不歪</strong><br/>② <strong>揖 yī：作揖；深圆：弯得深、抱得圆</strong><br/><br/><strong>一句话：动有动相。</strong></p><p><strong>步从容，立端正</strong><br/>① <strong>走路不追跑打闹，脚步稳当</strong><br/>② <strong>站着不东倒西歪，两脚站定</strong><br/><br/><strong>一句话：稳当，是练出来的。</strong></p><p><strong>揖深圆，拜恭敬</strong><br/>① <strong>作揖弯腰要有诚意，不敷衍</strong><br/>② <strong>行礼时心里存着敬意，动作才不浮</strong><br/><br/><strong>一句话：礼在心，不在样子。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 不贪杯与姿态正</h2><p style="margin:0"><strong>前四句讲「管住嘴」</strong><br/>① <strong>不喝酒、不失态</strong><br/>② <strong>护住身体，也护住体面</strong><br/><br/><strong>一句话：不贪杯。</strong></p><p><strong>后四句讲「立起身」</strong><br/>① <strong>从容、端正、深圆、恭敬</strong><br/>② <strong>四个词，讲的都是「稳」和「敬」</strong><br/><br/><strong>一句话：有精神。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>饭桌上有人逗酒，摇头说「我不喝」</strong><br/>② <strong>上课坐正、站队站直，行礼弯腰到位</strong><br/><br/><strong>一句话：嘴稳身正。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：管住嘴</strong><br/>① <strong>年方少，勿饮酒——小孩子不碰酒</strong><br/>② <strong>饮酒醉，最为丑——醉态最难看</strong><br/><br/><strong>一句话：惜身惜面。</strong></p><p><strong>后四句：立起身</strong><br/>① <strong>步从容，立端正——走站要稳</strong><br/>② <strong>揖深圆，拜恭敬——行礼要诚</strong><br/><br/><strong>一句话：稳与诚。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>不贪杯、走稳、站直、行礼诚</strong><br/>② <strong>嘴上有分寸，身上有模样</strong><br/><br/><strong>一句话：管住嘴，立起身。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>小孩子不喝酒，站走行礼都端正。</p><p>📖 管住嘴</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>不贪杯是惜身，站得正是存敬。</p><p>💡 形正心正</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 年方少，勿饮酒</p>
<p>这是「弟子规课堂」第十八课：谨第四段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 小孩子为什么不能喝酒？</h3><p><strong>身体还在长，酒最伤身。</strong><br/><br/>① <strong>酒伤大脑和身体，小孩承受不起</strong><br/>② <strong>喝醉了失态，还容易闯祸</strong><br/>③ <strong>记法：大人的酒杯，不是小孩的。</strong></p><h3>❓ 「最为丑」的「丑」是长相丑吗？</h3><p><strong>不是，是醉后失态的样子难看。</strong><br/><br/>① <strong>醉了胡言乱语、走路歪斜，很失礼</strong><br/>② <strong>「丑」说的是行为，不是长相</strong><br/>③ <strong>记法：醉态最丑，清醒最体面。</strong></p><h3>❓ 「步从容」是走得慢吗？</h3><p><strong>不是慢，是不慌。</strong><br/><br/>① <strong>脚步稳当，不追跑打闹、不东张西望</strong><br/>② <strong>急事可以快走，但不横冲直撞</strong><br/>③ <strong>记法：从容是有分寸的快慢。</strong></p><h3>❓ 「揖深圆」是什么意思？</h3><p><strong>作揖要弯得深、抱得圆。</strong><br/><br/>① <strong>揖读 yī，是古人见面行的礼</strong><br/>② <strong>弯腰到位、双手抱圆，才见诚意</strong><br/>③ <strong>记法：弯得下去，敬才立得住。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 饭桌上不碰酒</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>有人递酒也摇头，以茶水代</strong>；<strong>这就是「年方少，勿饮酒」</strong>。</p><p>💡 走路站稳</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>走廊里不追跑，站队站得直</strong>；<strong>这就是「步从容，立端正」</strong>。</p><p>🌱 见长辈行礼要诚</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>问好弯腰到位，眼睛看着人</strong>；<strong>这就是「揖深圆，拜恭敬」</strong><br/><br/><strong>本课的落点：管住嘴，立起身。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲谨第四段。记牢：<strong>年方少，勿饮酒</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>谨第四段 · 不贪杯又站得正。<strong>形正心正</strong>。</p><p>年方少，勿饮酒 · 小孩不碰酒。<strong>惜身</strong>。</p><p>饮酒醉，最为丑 · 醉态最难看。<strong>失礼</strong>。</p><p>步从容，立端正 · 走稳站直。<strong>脚下有分寸</strong>。</p><p>揖深圆，拜恭敬 · 行礼见诚意。<strong>弯得下去</strong>。</p><p><strong>在全篇中的位置:</strong>谨第四段；上一课讲穿衣吃饭的度，这一课讲不贪杯和站走行礼的端正。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说说「少」「揖」怎么读。② 饭桌上有人逗酒，大声说「我不喝」。③ 今天走路不跑、站队站直。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「年方少」的「少」怎么读？', opts: ['shào，年少', 'shǎo，多少', 'xiǎo，大小'], ans: 0, exp: '少读 shào，是年纪小'},
  {q: '2. 小孩子能不能喝酒？', opts: ['不能，身体还在长', '可以喝一点点', '过生日可以喝'], ans: 0, exp: '勿饮酒'},
  {q: '3. 「饮酒醉，最为丑」的「丑」指什么？', opts: ['醉后失态的样子难看', '长相不好看', '衣服穿得旧'], ans: 0, exp: '丑是失态'},
  {q: '4. 「步从容」的「从容」是什么意思？', opts: ['不慌不忙', '随便乱跑', '从前面走过'], ans: 0, exp: '从容是不慌不忙'},
  {q: '5. 「立端正」讲什么？', opts: ['站要站得直', '站着可以靠墙', '站累了就蹲下'], ans: 0, exp: '站得端正'},
  {q: '6. 「揖深圆」的「揖」怎么读？', opts: ['yī，作揖', 'jí，收集', 'yì，意思'], ans: 0, exp: '揖读 yī，是作揖'},
  {q: '7. 「拜恭敬」的「拜」是什么意思？', opts: ['行礼', '拜年拿红包', '拜访朋友'], ans: 0, exp: '拜是行礼'},
  {q: '8. 走路时应该怎样？', opts: ['脚步从容，不追跑打闹', '越快越好', '拖拖拉拉'], ans: 0, exp: '步从容'},
  {q: '9. 有人逗你喝酒，应该怎么办？', opts: ['摇头拒绝，以茶代酒', '不好意思拒绝', '尝一小口'], ans: 0, exp: '勿饮酒，要拒绝'},
  {q: '10. 这一段总的讲什么？', opts: ['不贪杯，站走行礼要端正', '怎么喝酒才对', '怎么跑得最快'], ans: 0, exp: '管住嘴，立起身'},
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
s = s.replace('《弟子规》第十七课', '《弟子规》第十八课')
s = s.replace('谨第三段', '谨第四段')
s = s.replace("window.GUOXUE_COURSE_ID = '557-yi-gui-jie';", "window.GUOXUE_COURSE_ID = '558-bu-cong-rong';")
s = s.replace('yaoyue559', 'yaoyue560')

# ---- 校验 ----
for w in ['衣贵洁', '不贵华', '上循分', '下称家', '对饮食', '勿拣择', '食适可', '勿过则',
          '勿践阈', '勿跛倚', '勿箕踞', '勿摇髀',
          '谨第三段', '557-yi-gui-jie', 'yaoyue559', '第十七课']:
    if w in s:
        idx = s.find(w)
        print('[FAIL] 残留 %r: %s' % (w, s[max(0, idx - 60):idx + 60].replace('\n', ' ')))
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
