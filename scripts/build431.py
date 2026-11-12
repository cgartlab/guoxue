# -*- coding: utf-8 -*-
"""生成第 431 课《阳货》第二章「性相近也，习相远也」课件。
原文仅十字，字号放大作单页主打；逐字 ruby 由拼音表生成。
"""
import io
import os
import re

PY = """
子zǐ 曰yuē ： 「 性xìng 相xiāng 近jìn 也yě ， 习xí 相xiāng 远yuǎn 也yě 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '1.8rem'   # 本科仅十字一句，字号放大作版面主打
LH = '1.95'


def build_ruby_paragraphs():
    out = []
    for idx, para in enumerate(PY.strip().split('||')):
        html = []
        for tok in para.split():
            tok = tok.strip()
            if not tok:
                continue
            m = HAN_RT.match(tok)
            if m:
                html.append('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (m.group(1), m.group(2)))
            else:
                html.append(tok)
        if idx == 0:
            style = ('padding-top:0;text-align:left;text-indent:0;font-size:%s;'
                     'line-height:%s;width:100%%;max-width:none;margin:0' % (FS, LH))
        else:
            style = ('text-align:left;text-indent:0;font-size:%s;line-height:%s;'
                     'width:100%%;max-width:none;margin:0.12em 0 0' % (FS, LH))
        out.append('<p style="%s">%s</p>' % (style, ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="《论语·阳货》第二章精讲：子曰，性相近也，习相远也。人的天性是相近的，后来习惯不同，就相差很远了。这一句只有十个字，却讲清了人的差别从哪儿来：起点差不多，差距靠后天攒。全篇最短的一章，讲人的同与不同。" name="description"/>
<meta content="性相近也，习相远也 · 天生的差不多，后来的差很多 · 国学课堂" property="og:title"/>
<meta content="《论语·阳货》第二章精讲：天生的差不多，后来的差很多" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/431-xing-xiang-jin-xi-xiang-yuan/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/431-xing-xiang-jin-xi-xiang-yuan/index.html" rel="canonical"/>
<title>性相近也，习相远也 · 天生的差不多，后来的差很多 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=yanghuo431" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=yanghuo431" rel="stylesheet"/>
</head>
<body>
<a class="skip-link" href="#slide-container">跳转到主内容</a>
<div aria-hidden="true" class="bg-layer"></div>
<div aria-hidden="true" class="ink-dot ink-dot-1"></div>
<div aria-hidden="true" class="ink-dot ink-dot-2"></div>
<div aria-hidden="true" class="ink-dot ink-dot-3"></div>
<nav aria-label="主导航" class="ds-navbar ds-navbar--global">
<a class="ds-btn-nav ds-btn-nav--brand" href="../../index.html">国学课堂</a>
<a class="ds-btn-nav ds-btn-nav--ghost" href="../../index.html">首页</a>
<ul class="ds-navbar__menu" id="primary-menu">
<li><a class="ds-btn-nav ds-btn-nav--ghost" href="../../index.html#lesson-cards">课程</a></li>
<li><a class="ds-btn-nav ds-btn-nav--ghost" href="../../index.html#sidebar-nav">门类</a></li>
</ul>
<a class="ds-btn-nav" href="../../about.html">关于本站</a>
</nav>
<nav aria-label="课程工具栏" class="ds-toolbar">
<a class="ds-btn-nav ds-btn-nav--ghost" href="../../index.html">← 返回目录</a>
<div class="ds-tabs">
<button class="ds-tab active" data-section="lecture">讲义</button>
<button class="ds-tab" data-section="quiz">测验</button>
<button class="ds-tab" data-section="review">答疑解惑</button>
</div>
<div class="ds-toolbar__right">
<span class="page-indicator" id="page-indicator">1 / 24</span>
<div class="dots-row" id="dots-row"></div>
<button class="ds-btn-nav" disabled="" id="nav-prev">← 上一页</button>
<button class="ds-btn-nav" id="nav-next">下一页 →</button>
<button aria-label="切换全屏显示" class="ds-btn-nav ds-btn-nav--icon" id="fullscreen-btn" title="切换全屏显示"><span class="ds-btn-nav__icon">⛶</span><span class="ds-btn-nav__text">全屏</span></button>
</div>
</nav>
<div class="slide-viewport">
<div class="slide-container" id="slide-container">
<!-- ====== 讲义部分 ====== -->
<!-- 1. 标题页 -->
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">性相近也，习相远也</h2><div class="cover-ornament"></div><p class="cover-subtitle">天生的差不多，后来的差很多</p><p class="cover-desc">这是<strong>《论语·阳货》第二章</strong>，全篇最短的一章，只有<strong>十个字</strong>。孔子说：人的天性本来<strong>相近</strong>，后来习惯不同，就<strong>相差很远</strong>了。这一句讲清了人的差别从哪儿来——<strong>起点差不多，差距靠后天攒</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:14px 22px 12px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>孔子说：人的天性，本来是相近的；后来习染不同，就相差很远了</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《阳货》第二章</strong>；<strong>合章本作 17.2</strong>；<strong>全篇最短的一章，只有十个字</strong>；<strong>「性」是天生的资质，「习」是后天的习惯熏染</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>天生的差不多，后来的差很多</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">性</span>：<strong>天生的资质、底子</strong>——<strong>不只是「性格」这么窄</strong>。</p><p><span class="ds-highlight">相近</span>：<strong>差不了多少</strong>——<strong>刚落地时，谁也不比谁强出多少</strong>。</p><p><span class="ds-highlight">习</span>：<strong>后天的习惯、熏染</strong>——<strong>不是「复习」这一件事</strong>。</p><p><span class="ds-highlight">相远</span>：<strong>越走越远，差出一大截</strong>。</p><p><span class="ds-highlight">相近 · 相远</span>：<strong>一句对举，一头讲同，一头讲异</strong>。</p><p><span class="ds-highlight">也</span>：<strong>判断的语气</strong>——<strong>不是感慨，是平平地说一句实话</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>起点差不多，路自己走</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：性相近也</h2><h3>“ 性 相 近 也 ”</h3><p style="margin:0"><strong>「性」到底是什么？</strong><br/><br/>① <strong>天生的资质、底子</strong><br/>② <strong>不是「性格」两个字能盖住的</strong><br/><br/><strong>一句话：说的是人刚落地时那个底子。</strong></p><p><strong>「相近」近在哪里？</strong><br/><br/>① <strong>会哭会笑，知道疼，知道怕</strong><br/>② <strong>都想被人待好，都知道好歹</strong><br/><br/><strong>一句话：起点不悬殊。</strong></p><p><strong>相近是不是一样？</strong><br/><br/>① <strong>相近不等于相同</strong><br/>② <strong>孔子没说过人人一个模子</strong><br/><br/><strong>一句话：说的是「差不多」，不是「全一样」。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：习相远也</h2><h3>“ 习 相 远 也 ”</h3><p style="margin:0"><strong>「习」指什么？</strong><br/><br/>① <strong>后天的习惯、熏染</strong><br/>② <strong>跟什么人、在什么地方、天天做什么</strong><br/><br/><strong>一句话：习不是一次学习，是天天泡出来的。</strong></p><p><strong>「相远」能远到什么地步？</strong><br/><br/>① <strong>同一个起点，几十年后天上地下</strong><br/>② <strong>差的全是天天的小事</strong><br/><br/><strong>一句话：差距是攒出来的。</strong></p><p><strong>孔子在怪谁？</strong><br/><br/>① <strong>不怪天，不怪命</strong><br/>② <strong>把账算在「习」上</strong><br/><br/><strong>一句话：这一句把人自己的责任摆出来了。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：一句两面</h2><h3>“ 性 相 近 也 ， 习 相 远 也 ”</h3><p style="margin:0"><strong>头一面在说什么？</strong><br/><br/>① <strong>谁也不比谁高贵到哪儿去</strong><br/>② <strong>别轻看人</strong><br/><br/><strong>一句话：天生不悬殊，别拿出身压人。</strong></p><p><strong>第二面在说什么？</strong><br/><br/>① <strong>也别把自己钉死</strong><br/>② <strong>变好变坏，看后来怎么走</strong><br/><br/><strong>一句话：不认命，也不认死。</strong></p><p><strong>十个字，分量为什么重？</strong><br/><br/>① <strong>一句讲清「同」和「异」</strong><br/>② <strong>后来的教育、家教，全从这里长出来</strong><br/><br/><strong>一句话：起点论和宿命论，这一句都堵住了。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：这一句的分量</h2><h3>“ 性 相 近 也 ， 习 相 远 也 ”</h3><p style="margin:0"><strong>跟「人之初，性本善」是一回事吗？</strong><br/><br/>① <strong>《三字经》讲善恶，这里讲远近</strong><br/>② <strong>一个说「都是好的」，一个说「都差不多」</strong><br/><br/><strong>一句话：不是一个题目，别混着讲。</strong></p><p><strong>荀子说「性恶」，跟这句冲突吗？</strong><br/><br/>① <strong>荀子讲的是另一头</strong><br/>② <strong>但两边都认后天能改</strong><br/><br/><strong>一句话：争的是起点，认的是后天。</strong></p><p><strong>对今天有什么用？</strong><br/><br/>① <strong>教孩子：早年的习惯最要紧</strong><br/>② <strong>对自己：想变，从天天做的事改</strong><br/><br/><strong>一句话：习能把人拉远，也能把人拉近。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「性」与「习」</h2><p>十个字，一层比一层实在——</p><h3>“性相近也……习相远也”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>性：</strong>相近。</p><p>🌱 起点不悬殊，别轻看人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>习：</strong>相远。</p><p>👥 差距是后天攒的，别认命</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>用：</strong>教与养。</p><p>🔁 所以教育有用，择友择环境要紧</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《阳货》第二章，<strong>全篇最短的一章，讲人的差别从哪儿来</strong>。</p></div>
<!-- ====== 测验部分（slide-engine.js 渲染） ====== -->
<div class="slide" data-page="8" data-section="quiz"><span class="ds-badge ds-badge--success">测验</span><h2 style="border:none;text-align:center;padding-bottom:0;">测验说明</h2><ul style="text-align:left;margin-top:var(--ds-space-6);display:inline-block;"><li>共 10 道选择题，每题 3 个选项</li><li>每题 10 分，满分 100 分</li><li>点击选项即可作答，选择后会显示讲解</li><li>可以随时返回讲义部分复习</li></ul><p style="margin-top:var(--ds-space-10);text-align:center;font-size:1.25rem;color:var(--ds-accent);font-weight:700;">准备好了吗？</p></div>
<div class="slide" data-page="9" data-section="quiz" id="quiz-0"></div>
<div class="slide" data-page="10" data-section="quiz" id="quiz-1"></div>
<div class="slide" data-page="11" data-section="quiz" id="quiz-2"></div>
<div class="slide" data-page="12" data-section="quiz" id="quiz-3"></div>
<div class="slide" data-page="13" data-section="quiz" id="quiz-4"></div>
<div class="slide" data-page="14" data-section="quiz" id="quiz-5"></div>
<div class="slide" data-page="15" data-section="quiz" id="quiz-6"></div>
<div class="slide" data-page="16" data-section="quiz" id="quiz-7"></div>
<div class="slide" data-page="17" data-section="quiz" id="quiz-8"></div>
<div class="slide" data-page="18" data-section="quiz" id="quiz-9"></div>
<!-- ====== 测验得分页 ====== -->
<div class="slide score-page" data-page="19" data-section="quiz" id="quiz-score">
<span class="ds-badge ds-badge--success">测验得分</span>
<h2>测验完成！</h2>
<div class="score-hero">
<div class="score-hero__number" id="score-display">0</div>
<div class="score-hero__message" id="score-message">正在计算得分...</div>
<div class="score-summary">
<p>✅ 答对题数：<b class="b-correct" id="correct-count">0</b> / 10</p>
<p>📊 总得分：<b class="b-total" id="total-score">0</b> 分（满分 100 分）</p>
<p>📈 正确率：<b class="b-percent" id="score-percent">0%</b></p>
</div>
<button aria-label="重新答题" class="retake-btn" id="retake-btn">↺ 重新答题</button>
</div>
</div>
<!-- ====== 答疑解惑 ====== -->
<!-- 20. FAQ -->
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 这句跟「人之初，性本善」是一回事吗？</h3><p><strong>不是一回事，题目不同。</strong><br/><br/>① <strong>《三字经》讲的是善还是恶</strong><br/>② <strong>孔子这里讲的是差得远还是近</strong><br/>③ <strong>一个说天性都善，一个说天性都差不多</strong><br/><br/><strong>记法：一个问好坏，一个问差别。</strong></p><h3>❓ 孔子是说人天生都一样吗？</h3><p><strong>是「相近」，不是「一样」。</strong><br/><br/>① <strong>相近，是差不了多少</strong><br/>② <strong>差别主要在后来怎么走</strong><br/>③ <strong>所以他既不认命，也不许人轻看别人</strong><br/><br/><strong>记法：起点差不多，路自己走。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>学三样。</strong><br/><br/>① <strong>别拿「我天生就这样」当借口</strong><br/>② <strong>看身边交什么人、天天做什么</strong><br/>③ <strong>想变好，先改一件天天做的小事</strong><br/><br/><strong>记法：习惯是慢慢攒的。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一句，给我们的日子三样提醒——</p><p>🌱 别拿「天生」当借口</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>天生的只管开头一段</strong>；<strong>后来怎么走，多半看习惯</strong>。</p><p>👥 交什么人，天天做什么</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>「习」就是这两样</strong>；<strong>跟谁在一处、日日做什么，人就往哪儿去</strong>。</p><p>🔁 想变，从一件小事起</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不必发大誓</strong>；<strong>天天做的一件小事改了，路就慢慢偏过来了</strong><br/><br/><strong>本章的落点：天生的差不多，后来的差很多。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「性相近也，习相远也」。记牢：<strong>起点差不多，路自己走。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                性相近也，习相远也。
            </p><p>回顾本课要点:</p><p>性 · 相近</p><br/><p><strong>起点不悬殊，别轻看人。</strong></p><p>习 · 相远</p><br/><p><strong>差距是后天攒的，别认命。</strong></p><p>用 · 教与养</p><br/><p><strong>所以教育有用，择友择环境要紧。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《阳货》第二章</strong>，<strong>全篇最短的一章</strong>；承 430 课——<strong>那课讲处世，这课讲人为什么不同</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>性相近也，习相远也。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：你身上哪个习惯是后来养成的。② 背一句：性相近也，习相远也。</p><p><strong>把这一章记在心里:</strong><strong>起点差不多，路自己走。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “性相近也，习相远也。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·阳货》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '431-xing-xiang-jin-xi-xiang-yuan';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《阳货》', '《季氏》', '《微子》'], ans: 0, exp: '这是《阳货》第二章，全篇最短的一章'},
  {q: '2. 「性」在这里指什么？', opts: ['天生的资质、底子', '性格脾气', '姓名'], ans: 0, exp: '不只是「性格」这么窄'},
  {q: '3. 「习」在这里指什么？', opts: ['后天的习惯和熏染', '复习功课', '练习写字'], ans: 0, exp: '不是「复习」这一件事'},
  {q: '4. 「相近」是什么意思？', opts: ['差不了多少', '挨得很近', '互相亲近'], ans: 0, exp: '刚落地时，谁也不比谁强出多少'},
  {q: '5. 「相远」是什么意思？', opts: ['后来相差很远', '离得很远', '互相疏远'], ans: 0, exp: '越走越远，差出一大截'},
  {q: '6. 这一句主要在讲什么？', opts: ['人的差别主要是后天造成的', '人天生就分高低', '人天生完全一样'], ans: 0, exp: '起点差不多，差距靠后天攒'},
  {q: '7. 「相近」和「一样」有什么区别？', opts: ['相近是差不多，不完全相同', '没有区别', '相近比一样更整齐'], ans: 0, exp: '孔子没说过人人一个模子'},
  {q: '8. 这一句跟「人之初，性本善」是什么关系？', opts: ['题目不同：一个问好坏，一个问差别', '说的完全是一件事', '两句互相矛盾'], ans: 0, exp: '《三字经》讲善恶，孔子这里讲远近'},
  {q: '9. 这一句对教育意味着什么？', opts: ['后天教养有用，不能只看出身', '天资决定一切', '教不教都一样'], ans: 0, exp: '所以教育有用，择友择环境要紧'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['天生的差不多，后来的差很多', '性本善', '唯上知与下愚不移'], ans: 0, exp: '起点差不多，路自己走'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=yanghuo431"></script><script src="../../assets/js/slide-engine.js?v=yanghuo431"></script>
<script src="../../assets/js/speech.js?v=yanghuo431"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=yanghuo431"></script>
<script defer="" src="../../assets/js/auth.js?v=yanghuo431"></script>
<script defer="" src="../../assets/js/api-client.js?v=yanghuo431"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '431-xing-xiang-jin-xi-xiang-yuan')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
