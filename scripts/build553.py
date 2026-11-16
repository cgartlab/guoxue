#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build553: 以 552 课件为模板生成第 553 课《出则悌·尊长前，声要低》。
「出则悌」第五段，讲在长辈跟前的声音、进退与应答。
讲义 8 页（原文页在第 2 页）：
  0 封面 / 1 原文 ruby / 2 总说（声音、进退、应答）/ 3 尊长前声要低·低不闻却非宜 /
  4 进必趋退必迟·问起对视勿移 / 5 两句合看（声音与身体）/ 6 逐句解读 / 7 核心思想；
测验 12 页、答疑 4 页沿用模板，总 24 页。付费课。
"""
import io, os, re, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = ROOT + "/lessons/552-qi-xia-ma/index.html"
DST = ROOT + "/lessons/553-zun-zhang-qian/index.html"

TITLE = '出则悌 · 尊长前，声要低，低不闻，却非宜 ·《弟子规》国学问答 · 国学课堂'
OG_TITLE = '尊长前，声要低；问起对，视勿移 · 弟子规课堂'
DESC = ('《弟子规》第十三课，出则悌第五段。原文：「尊长前，声要低。低不闻，却非宜。'
        '进必趋，退必迟。问起对，视勿移。」讲在长辈跟前怎么办：说话声音要放低，'
        '但不能低到长辈听不见；长辈叫你就快些过去，退出来要慢；长辈问话，站起来回答，'
        '目光看着长辈，不东张西望。声音、脚步、眼睛，三处都藏着分寸。')
OG_DESC = '《弟子规》第十三课：尊长前声要低、低不闻却非宜、进必趋退必迟、问起对视勿移。'

CANON = 'https://guoxue.8023laozhanshi.cc/lessons/553-zun-zhang-qian/index.html'

ORIG = '尊长前，声要低。低不闻，却非宜。进必趋，退必迟。问起对，视勿移。'
ORIG_COMMA = '尊长前，声要低；低不闻，却非宜；进必趋，退必迟；问起对，视勿移。'
OLD_ORIG = '骑下马，乘下车。过犹待，百步余。长者立，幼勿坐。长者坐，命乃坐。'
OLD_ORIG_COMMA = '骑下马，乘下车；过犹待，百步余；长者立，幼勿坐；长者坐，命乃坐。'

P1 = '<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0">'
P2 = '<p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0">'


def rb(ch, py):
    return '<ruby lang="zh-Hans">' + ch + '<rt>' + py + '</rt></ruby>'


def ju(chars, pys, first):
    return (P1 if first else P2) + rb(chars[0], pys[0]) + rb(chars[1], pys[1]) + rb(chars[2], pys[2]) + '，' \
           + rb(chars[3], pys[3]) + rb(chars[4], pys[4]) + rb(chars[5], pys[5]) + '。</p>'


RUBY_LINE = (ju('尊长前声要低', ['zūn', 'zhǎng', 'qián', 'shēng', 'yào', 'dī'], True)
             + ju('低不闻却非宜', ['dī', 'bù', 'wén', 'què', 'fēi', 'yí'], False)
             + ju('进必趋退必迟', ['jìn', 'bì', 'qū', 'tuì', 'bì', 'chí'], False)
             + ju('问起对视勿移', ['wèn', 'qǐ', 'duì', 'shì', 'wù', 'yí'], False))

LECTURE = '''<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">声要低</h2><div class="cover-ornament"></div><p class="cover-subtitle">《弟子规》出则悌第五段：尊长前，声要低</p><p class="cover-desc">上一段讲路上怎么停下来、怎么等，这一段讲在长辈跟前怎么办：声音要放低，但不能低到听不见；叫你就快些过去，退出来要慢；长辈问话，站起来答，眼睛看着长辈。</p><div class="cover-seal">出则悌</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文 · 出则悌第五段</h2><div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">
''' + RUBY_LINE + '''
</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>在长辈面前，说话的声音要放低。可是低到长辈听不见，也不合适。长辈叫你的时候，要快步上前；退出来的时候，要慢一些。长辈问话，要站起来回答，目光看着长辈，不要东张西望。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>「尊长」指辈分高、年纪长的人；「闻」是听见；「却」是反而；「非宜」是不合适；「趋」读 qū，是快步上前；「迟」是慢；「起」是站起来；「对」是回答；「视」是目光；「移」是挪开。前四句讲声音，后四句讲脚步与答话。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>''' + ORIG_COMMA + '''</strong></p></div>
<!-- 3. 总说 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>总说 · 声音、进退、应答</h2><p style="margin:0"><strong>先说声音</strong><br/>① <strong>长辈跟前，声音放低</strong><br/>② <strong>低到听不见，也不对</strong><br/><br/><strong>一句话：不高不哑。</strong></p><p><strong>再说进退</strong><br/>① <strong>进去要快</strong><br/>② <strong>退出要慢</strong><br/><br/><strong>一句话：进得干脆，退得稳当。</strong></p><p><strong>一句话看全段</strong><br/>① <strong>声音、脚步、眼睛，三处都在替你说敬</strong><br/>② <strong>礼不是背出来的，是做出来的</strong><br/><br/><strong>一句话：处处有分寸。</strong></p></div>
<!-- 4. 尊长前声要低·低不闻却非宜 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>尊长前，声要低；低不闻，却非宜</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>闻 wén：听见；却：反而</strong><br/>② <strong>非宜：不合适</strong><br/><br/><strong>一句话：低，不等于没声。</strong></p><p><strong>尊长前，声要低</strong><br/>① <strong>长辈跟前不大喊、不尖叫、不嚷嚷</strong><br/>② <strong>声音放低，是心里装着别人</strong><br/><br/><strong>一句话：先想到他在听。</strong></p><p><strong>低不闻，却非宜</strong><br/>① <strong>小到长辈听不见，是失礼不是恭敬</strong><br/>② <strong>问话要答得清楚，不必扭扭捏捏</strong><br/><br/><strong>一句话：听得见，才算敬。</strong></p></div>
<!-- 5. 进必趋退必迟·问起对视勿移 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>进必趋，退必迟；问起对，视勿移</h2><p style="margin:0"><strong>先认字</strong><br/>① <strong>趋 qū：快步上前；迟：慢</strong><br/>② <strong>起：站起来；对：回答；视：目光</strong><br/><br/><strong>一句话：快与慢，都是礼。</strong></p><p><strong>进必趋，退必迟</strong><br/>① <strong>长辈叫你，脚步快一点，别让人等</strong><br/>② <strong>退出来慢一点，不转身就跑</strong><br/><br/><strong>一句话：来得快，退得慢。</strong></p><p><strong>问起对，视勿移</strong><br/>① <strong>长辈问话，站起来回答</strong><br/>② <strong>答话时看着长辈，眼睛不东张西望</strong><br/><br/><strong>一句话：答得正，看得住。</strong></p></div>
<!-- 6. 两句合看 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>两句合看 · 声音与身体</h2><p style="margin:0"><strong>前四句讲「声音」</strong><br/>① <strong>放低，是敬</strong><br/>② <strong>低到听不见，是过了头</strong><br/><br/><strong>一句话：低而有声。</strong></p><p><strong>后四句讲「身体」</strong><br/>① <strong>进快退慢，是知道分寸</strong><br/>② <strong>起身看人答话，是心里有底</strong><br/><br/><strong>一句话：动而有节。</strong></p><p><strong>今天怎么做</strong><br/>① <strong>家里有人休息，说话先压低</strong><br/>② <strong>长辈问话，站起来、看着人答</strong><br/><br/><strong>一句话：三处都做到，才叫懂礼。</strong></p></div>
<!-- 7. 逐句解读 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四句两两成对</h2><p style="margin:0"><strong>前四句：怎么说</strong><br/>① <strong>尊长前，声要低——不高声</strong><br/>② <strong>低不闻，却非宜——也不能没声</strong><br/><br/><strong>一句话：不高不哑。</strong></p><p><strong>后四句：怎么动</strong><br/>① <strong>进必趋，退必迟——进快退慢</strong><br/>② <strong>问起对，视勿移——起身看人答</strong><br/><br/><strong>一句话：进退有节，答话有眼。</strong></p><p><strong>一句口诀记住</strong><br/>① <strong>声放低，话答清</strong><br/>② <strong>进去快，退得慢，答话看人</strong><br/><br/><strong>一句话：分寸，就在这三处。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · ''' + ORIG + '''</h2><p>一句话，两层意思——</p><h3>"''' + ORIG + '''"</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>声放低、进快退慢、起身看人答话。</p><p>📖 声、步、眼</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>把人放在心上，处处有分寸。</p><p>💡 心里有人，才有分寸</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>''' + ORIG_COMMA + '''</p><p>🌱 尊长前，声要低</p>
<p>这是「弟子规课堂」第十三课：出则悌第五段。</p></div>
'''

REVIEW = '''<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 在长辈跟前一定要小声说话吗？</h3><p><strong>是「放低」，不是咬着耳朵说。</strong><br/><br/>① <strong>不嚷嚷、不尖叫、不当着人背后喊</strong><br/>② <strong>以长辈听得清楚为准，说清就行</strong><br/>③ <strong>记法：低一点，不是哑一点。</strong></p><h3>❓ 「低不闻，却非宜」不是和上一句矛盾吗？</h3><p><strong>不矛盾：低是态度，听得见是分寸。</strong><br/><br/>① <strong>太大声，吵人</strong><br/>② <strong>太小声，长辈要侧着耳朵听，是给人添累</strong><br/>③ <strong>记法：不高不哑，正好。</strong></p><h3>❓ 「进必趋，退必迟」今天怎么用？</h3><p><strong>叫到你快去，走的时候慢一点。</strong><br/><br/>① <strong>长辈喊你，手上事放一放，快点过去</strong><br/>② <strong>要走时先说一声「我去了」，慢慢退开</strong><br/>③ <strong>记法：来得快，退得稳。</strong></p><h3>❓ 和长辈说话要一直盯着眼睛吗？</h3><p><strong>是目光稳，不是瞪人。</strong><br/><br/>① <strong>看着长辈答话，就是「视勿移」</strong><br/>② <strong>紧张可以看鼻尖、下巴，别东张西望、别低头看手机</strong><br/>③ <strong>记法：眼睛在，人就在。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 有人休息就压低声音</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>家里有人睡觉、图书馆、公交车上</strong>；<strong>说话先放低，别喊着玩，这就是「声要低」</strong>。</p><p>💡 叫到就快去，走时说一声</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>长辈喊你，快点过去，别让人等</strong>；<strong>要走时先打招呼，再慢慢退开</strong>。</p><p>🌱 长辈问话，站起来看着答</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>放下手机，站起来，看着人把话答清</strong>；<strong>这就是「问起对，视勿移」</strong><br/><br/><strong>本课的落点：尊长前，声要低。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天讲出则悌第五段。记牢：<strong>尊长前，声要低</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">''' + ORIG + '''</p><p>回顾本课要点:</p><p>声音、进退、应答 · 高低有度，快慢有节。<strong>处处有分寸</strong>。</p><p>尊长前，声要低 · 不大喊、不嚷嚷。<strong>心里装着别人</strong>。</p><p>低不闻，却非宜 · 太小也是失礼。<strong>听得见才算敬</strong>。</p><p>进必趋，退必迟 · 叫到就快去，走时慢退。<strong>进快退慢</strong>。</p><p>问起对，视勿移 · 站起来答，看着人。<strong>答得正看得住</strong>。</p><p><strong>在全篇中的位置:</strong>出则悌第五段；上一课讲路上相遇与陪坐，这一课讲长辈跟前的说话、进退与应答。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>''' + ORIG + '''</p>
</div><p><strong>课后小挑战:</strong>① 说出「低不闻」的「闻」是什么意思。② 今天长辈叫你，立刻放下手上的事过去。③ 长辈问话，站起来看着人答一次。</p><p><strong>把这一课记在心里:</strong><strong>''' + ORIG_COMMA + '''</strong></p></div>
'''

QUIZ = '''const QUIZ = [
  {q: '1. 「尊长前」的「长」怎么读？', opts: ['zhǎng，长辈', 'cháng，长短', 'zhàng，多余'], ans: 0, exp: '长者读 zhǎng'},
  {q: '2. 「低不闻」的「闻」是什么意思？', opts: ['听见', '闻气味', '消息'], ans: 0, exp: '闻是听见'},
  {q: '3. 「却非宜」的「宜」是什么意思？', opts: ['合适', '便宜', '应该做官'], ans: 0, exp: '非宜是不合适'},
  {q: '4. 「尊长前，声要低」是什么意思？', opts: ['在长辈跟前说话声音要放低', '在长辈跟前不能说话', '在长辈跟前要小声哭'], ans: 0, exp: '声音放低是敬'},
  {q: '5. 「低不闻，却非宜」讲的是什么？', opts: ['低到长辈听不见，也不合适', '声音越低越好', '长辈听不见就再说一遍'], ans: 0, exp: '低也得听得见'},
  {q: '6. 「进必趋」的「趋」是什么意思？', opts: ['快步上前', '慢慢走', '往后退'], ans: 0, exp: '趋读 qū，快步'},
  {q: '7. 「退必迟」的「迟」是什么意思？', opts: ['慢', '迟到', '天黑'], ans: 0, exp: '迟是慢'},
  {q: '8. 「问起对」的「起」是什么意思？', opts: ['站起来', '起床', '起名字'], ans: 0, exp: '起是起身'},
  {q: '9. 「视勿移」讲答话时应该怎样？', opts: ['目光看着长辈，不东张西望', '眼睛一直眨', '低着头不说话'], ans: 0, exp: '视是目光'},
  {q: '10. 这一段总的讲什么？', opts: ['在长辈跟前的说话、进退与应答之礼', '怎么大声说话', '怎么快走'], ans: 0, exp: '声、步、眼的分寸'},
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
s = s.replace('《弟子规》第十二课', '《弟子规》第十三课')
s = s.replace("window.GUOXUE_COURSE_ID = '552-qi-xia-ma';", "window.GUOXUE_COURSE_ID = '553-zun-zhang-qian';")
s = s.replace('yaoyue553', 'yaoyue554')

# ---- 校验 ----
for w in ['骑下马', '乘下车', '过犹待', '百步余', '幼勿坐', '命乃坐',
          '出则悌第四段', '552-qi-xia-ma', 'yaoyue553', '第十二课']:
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
