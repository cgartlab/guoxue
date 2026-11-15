# -*- coding: utf-8 -*-
"""第 516 课《自羲农·三皇五帝》：以 515 为骨架，逐行替换内容生成新课件。
原文四句话（两组，每组六言两句，共四句24字）：
  自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。
"""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '515-wu-zi-zhe', 'index.html')
DST_DIR = os.path.join(BASE, 'lessons', '516-zi-xi-nong')
DST = os.path.join(DST_DIR, 'index.html')

with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

R = {}

# ---------- meta ----------
R[6] = '''<meta content="《三字经》第二十三课精讲：自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。上一课讲了「考世系，知终始」，这一课顺着读史的开端，讲中华远古的圣王——伏羲、神农、黄帝号「三皇」，唐尧、虞舜号「二帝」，他们禅让天下、共创盛世。八句话，讲完远古的「三皇五帝」。" name="description"/>'''
R[7] = '''<meta content="自羲农 · 至黄帝，号三皇，居上世 · 唐有虞，号二帝 · 三字经课堂" property="og:title"/>'''
R[8] = '''<meta content="《三字经》第二十三课：自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。" property="og:description"/>'''
R[10] = '''<meta content="https://guoxue.8023laozhanshi.cc/lessons/516-zi-xi-nong/index.html" property="og:url"/>'''
R[11] = '''<link href="https://guoxue.8023laozhanshi.cc/lessons/516-zi-xi-nong/index.html" rel="canonical"/>'''
R[12] = '''<title>自羲农 · 至黄帝，号三皇，居上世 · 唐有虞，号二帝 ·《三字经》国学问答 · 国学课堂</title>'''

# ---------- 1. 封面 ----------
R[52] = '''<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">自羲农</h2><div class="cover-ornament"></div><p class="cover-subtitle">至黄帝，号三皇，居上世；唐有虞，号二帝，相揖逊，称盛世</p><p class="cover-desc">上一课讲了「考世系，知终始」——读史要先明世代统系。这一课顺着读史的开端，讲中华远古的圣王：伏羲、神农、黄帝，被尊为「三皇」，位居上古之世；唐尧、虞舜，被尊为「二帝」，他们彼此禅让、礼让天下，共创一段太平盛世。八句话，讲完远古的「三皇五帝」。</p><div class="cover-seal">三字经</div></div>'''

# ---------- 2. 原文四句（两句一组，共四句） ----------
STYLE_A = 'padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0'
STYLE_B = 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0'


def ruby_line(style, chars):
    body = ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[:3])
    body += '，'
    body += ''.join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars[3:])
    return '<p style="%s">%s。</p>' % (style, body)


# 原文共四句（两组），合并成四行
R[55] = ruby_line(STYLE_A, [('自', 'zì'), ('羲', 'xī'), ('农', 'nóng'), ('至', 'zhì'), ('黄', 'huáng'), ('帝', 'dì')]) \
     + ruby_line(STYLE_B, [('号', 'hào'), ('三', 'sān'), ('皇', 'huáng'), ('居', 'jū'), ('上', 'shàng'), ('世', 'shì')]) \
     + ruby_line(STYLE_B, [('唐', 'táng'), ('有', 'yǒu'), ('虞', 'yú'), ('号', 'hào'), ('二', 'èr'), ('帝', 'dì')]) \
     + ruby_line(STYLE_B, [('相', 'xiāng'), ('揖', 'yī'), ('逊', 'xùn'), ('称', 'chēng'), ('盛', 'shèng'), ('世', 'shì')])
R[56] = ''
R[57] = ''
R[58] = ''
R[59] = '''</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>远古的帝王，从伏羲、神农到黄帝，三人被尊为「三皇」，位居上古之世；后来唐尧、虞舜，被称为「二帝」，他们彼此禅让、礼让天下，成就一段太平盛世。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》在「考世系，知终始」之后，紧接着讲读史要从远古的圣王说起——先有三皇，再有二帝，这是中华文明的源头。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>三皇开天，二帝禅让。</strong></p></div>'''

# ---------- 3. 字词梳理 · 九关节 ----------
R[61] = '''<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">自羲农</span>：<strong>自是从，羲是伏羲，农是神农</strong>——<strong>伏羲与神农，是上古的两位圣王</strong>。</p><p><span class="ds-highlight">至黄帝</span>：<strong>至是到，黄帝是姬姓部落首领</strong>——<strong>被尊为中华民族的人文初祖</strong>。</p><p><span class="ds-highlight">号三皇</span>：<strong>号是称作，三皇是伏羲、神农、黄帝三位远古圣王的总称</strong>——<strong>三人并称「三皇」</strong>。</p><p><span class="ds-highlight">居上世</span>：<strong>居是处于，上世是上古之世</strong>——<strong>三位圣王处在上古时代</strong>。</p><p><span class="ds-highlight">唐有虞</span>：<strong>唐是陶唐氏（尧），虞是有虞氏（舜）</strong>——<strong>尧舜两位圣王</strong>。</p><p><span class="ds-highlight">号二帝</span>：<strong>二帝是唐尧、虞舜</strong>——<strong>后世尊称他们为「二帝」</strong>。</p><p><span class="ds-highlight">相揖逊</span>：<strong>相是互相，揖逊是拱手礼让</strong>——<strong>尧舜彼此禅让，不把天下当作私有</strong>。</p><p><span class="ds-highlight">称盛世</span>：<strong>称是被称作，盛世是太平昌盛之世</strong>——<strong>禅让之下，天下大治</strong>。</p><p><span class="ds-highlight">三皇二帝</span>：<strong>三皇开天创物，二帝禅让共治</strong>——<strong>远古圣王，为后世立下榜样</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>三皇伏羲、神农、黄帝；二帝尧舜，禅让称盛。</strong></p></div>'''

# ---------- 4~7. 逐句解读 ----------
def interp(page, idx, title, quote, blocks):
    ps = []
    for n, (q, a, b, tail) in enumerate(blocks):
        margin = ' style="margin:0"' if n == 0 else ''
        ps.append('<p%s><strong>%s</strong><br/><br/>① <strong>%s</strong><br/>② <strong>%s</strong><br/><br/><strong>一句话：%s。</strong></p>' % (margin, q, a, b, tail))
    return ('<div class="slide" data-page="%d" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
            '<h2>逐句解读 · %s：%s</h2><h3>“ %s ”</h3>%s</div>') % (page, idx, title, quote, ''.join(ps))


R[63] = interp(3, '一', '自羲农，至黄帝', '自 羲 农 ， 至 黄 帝', [
    ('「自羲农」指谁？', '伏羲与神农两位圣王', '上古为民谋福的始祖', '三皇之二'),
    ('「至黄帝」的黄帝是谁？', '姬姓部落首领，人文初祖', '统一部落、奠基华夏', '三皇之一'),
    ('这句讲什么？', '从伏羲神农到黄帝，三位圣王位列上古', '三皇相继，开天创物', '三皇开世'),
])
R[65] = interp(4, '二', '号三皇，居上世', '号 三 皇 ， 居 上 世', [
    ('「三皇」是哪三位？', '伏羲、神农、黄帝', '上古三位最伟大的圣王', '三皇并称'),
    ('「居上世」什么意思？', '处在上古之世', '年代最为久远', '上世为尊'),
    ('这句的落点？', '三皇居上古，是中华文明的源头', '先有三皇，后有百代', '三皇居上'),
])
R[67] = interp(5, '三', '唐有虞，号二帝', '唐 有 虞 ， 号 二 帝', [
    ('「唐」「虞」是谁？', '唐是陶唐氏尧，虞是有虞氏舜', '两位圣王', '二帝本名'),
    ('为何称「二帝」？', '尧舜德配天地，后世尊为二帝', '功在天下，万世景仰', '二帝并称'),
    ('与前句的关系？', '三皇之后是二帝，谱系依次而下', '皇后是帝，承前启后', '皇帝相承'),
])
R[69] = interp(6, '四', '相揖逊，称盛世', '相 揖 逊 ， 称 盛 世', [
    ('「相揖逊」讲什么？', '尧舜彼此禅让，拱手让贤', '不把天下当私有', '禅让为美'),
    ('「称盛世」何解？', '禅让之下天下大治，被称为盛世', '公天下方得太平', '禅让盛世'),
    ('这一句的落点？', '三皇开天，二帝禅让，远古足为后世法', '公天下，世所称', '盛世之源'),
])

# ---------- 8. 核心思想 ----------
R[71] = '''<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世</h2><p>一句话，两层意思——</p><h3>"自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。"</h3>'''
R[72] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前四句讲三皇——伏羲、神农、黄帝位居上古；后四句讲二帝——唐尧、虞舜禅让天下，成就盛世。</p><p>📜 三皇二帝</p>'''
R[73] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>三皇开天创物，二帝以禅让共治；公天下、不私其位，是中华政治理想的源头。</p><p>🏛️ 禅让共治</p>'''
R[74] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>三皇二帝，以德立世；他们把天下让给贤人，为后世立下「公」的榜样。</p><p>🌿 公天下</p>'''
R[75] = '''<p>这是「三字经课堂」第二十三课：自羲农，至黄帝。</p></div>'''

# ---------- 20. FAQ ----------
R[105] = '''<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「三皇」是哪三位？</h3><p><strong>是伏羲、神农、黄帝。</strong><br/><br/>① <strong>伏羲画卦、神农尝草、黄帝奠基</strong><br/>② <strong>三人被尊为「三皇」</strong><br/>③ <strong>居上古之世，是文明源头</strong><br/><br/><strong>记法：三皇开天。</strong></p><h3>❓ 「二帝」是谁？</h3><p><strong>是唐尧、虞舜。</strong><br/><br/>① <strong>尧为陶唐氏，舜为有虞氏</strong><br/>② <strong>德配天地，尊为「二帝」</strong><br/>③ <strong>非本名，是尊称</strong><br/><br/><strong>记法：二帝禅让。</strong></p><h3>❓ 「相揖逊」是什么意思？</h3><p><strong>是尧舜彼此拱手禅让、把天下让给贤人。</strong><br/><br/>① <strong>不把天下当作私有</strong><br/>② <strong>传贤不传子</strong><br/>③ <strong>公天下之始</strong><br/><br/><strong>记法：禅让为美。</strong></p><h3>❓ 为什么说「称盛世」？</h3><p><strong>禅让之下天下大治，被称为太平盛世。</strong><br/><br/>① <strong>二帝共治，百姓安乐</strong><br/>② <strong>以德服人，不以力取</strong><br/>③ <strong>后世向往的治世典范</strong><br/><br/><strong>记法：禅让盛世。</strong></p></div>'''

# ---------- 21. 生活应用 ----------
R[107] = '''<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这八句，给我们三样提醒——</p><p>🏛️ 饮水思源</p>'''
R[108] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「自羲农，至黄帝」</strong>；<strong>中华文明的源头要记得，知来处方知去处</strong>。</p><p>🤝 谦让为美</p>'''
R[109] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>「相揖逊」提醒我们</strong>；<strong>与人相处要谦让，把机会让给更合适的人</strong>。</p><p>🌿 公心为上</p>'''
R[110] = '''<p style="margin:var(--ds-space-1) 0 0"><strong>禅让共治</strong>；<strong>把公心放在私心前，团队与家庭都更和睦</strong><br/><br/><strong>本课的落点：自羲农，至黄帝。</strong></p></div>'''

# ---------- 22. 课程总结 ----------
R[112] = '''<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《三字经》第二十三课。记牢：<strong>自羲农，至黄帝</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">'''
R[113] = '''                自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。'''
R[114] = '''            </p><p>回顾本课要点:</p><p>自羲农，至黄帝 · 伏羲、神农到黄帝，三皇位列上古。<strong>三皇开世。</strong></p><p>号三皇，居上世 · 三位圣王居上古之世，文明之源。<strong>三皇居上。</strong></p><p>唐有虞，号二帝 · 尧舜二帝，德配天地。<strong>二帝并称。</strong></p><p>相揖逊，称盛世 · 禅让天下，成就盛世。<strong>禅让盛世。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲「考世系，知终始」，这一课讲远古三皇五帝，下一课接着讲夏商周三代（三王）。</p><div class="ds-quote">'''
R[115] = '''<p>📜 原文重温</p>'''
R[116] = '''<p>自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。</p>'''
R[117] = '''</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「三皇」是哪三位。③ 讲清「相揖逊」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>自羲农，至黄帝，号三皇，居上世，唐有虞，号二帝，相揖逊，称盛世。</strong></p></div>'''

# ---------- 23. 结束页 ----------
R[124] = '''            "自羲农，至黄帝。号三皇，居上世。唐有虞，号二帝。相揖逊，称盛世。"<br/>'''

# ---------- course id ----------
R[132] = """    window.GUOXUE_COURSE_ID = '516-zi-xi-nong';"""

# ---------- QUIZ 10 题 ----------
QUIZ = [
    ('1. 「三皇」指哪三位？', ['伏羲、神农、黄帝', '尧、舜、禹', '天、地、人'], '三皇是上古三位圣王'),
    ('2. 「自羲农，至黄帝」中「羲」「农」是谁？', ['伏羲、神农', '羲和、农神', '尧、舜'], '伏羲画卦，神农尝百草'),
    ('3. 被尊为「人文初祖」的是谁？', ['黄帝', '伏羲', '神农'], '黄帝统一部落、奠基华夏'),
    ('4. 「居上世」什么意思？', ['处在上古之世', '住在山上', '在世上第一'], '三皇年代最古'),
    ('5. 「唐有虞」中的「唐」「虞」指谁？', ['尧、舜', '唐尧、虞舜（即尧舜）', '商汤、周武'], '陶唐氏尧、有虞氏舜'),
    ('6. 「二帝」是哪两位？', ['唐尧、虞舜', '伏羲、神农', '夏禹、商汤'], '尧舜被尊为二帝'),
    ('7. 「相揖逊」讲的是什么？', ['尧舜彼此禅让、让贤于能', '互相作揖行礼', '打仗争胜'], '公天下，传贤不传子'),
    ('8. 为什么说「称盛世」？', ['禅让之下天下大治', '国力最强', '疆域最大'], '二帝共治，太平昌盛'),
    ('9. 三皇与二帝的关系是？', ['三皇在前，二帝在后，谱系依次', '同时并称', '互相争斗'], '皇后是帝，承前启后'),
    ('10. 这一课八句合起来讲什么？', ['远古三皇五帝、禅让盛世', '三代开国', '朝代更替'], '三皇开天，二帝禅让'),
]
for i, (q, opts, exp) in enumerate(QUIZ):
    R[135 + i] = "  {q: '%s', opts: ['%s', '%s', '%s'], ans: 0, exp: '%s'}," % (q, opts[0], opts[1], opts[2], exp)

for n, text in R.items():
    assert 1 <= n <= len(lines), '行号越界: %d' % n
    lines[n - 1] = text

s = '\n'.join(lines)
s = s.replace('515-wu-zi-zhe', '516-zi-xi-nong')
s = s.replace('yaoyue517', 'yaoyue518')
s = s.replace('第二十二课', '第二十三课')
assert '515-wu-zi-zhe' not in s and 'yaoyue517' not in s and '第二十二课' not in s

os.makedirs(DST_DIR, exist_ok=True)
with open(DST, 'w', encoding='utf-8') as f:
    f.write(s)
print('OK', DST, len(s), 'chars,', len(s.split('\n')), 'lines')
