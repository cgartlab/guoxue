# -*- coding: utf-8 -*-
"""生成第 473 课《子张》第十二章「仕而优则学」课件。
全章约 14 字、三小段；短章大字版式（与 471 同结构 1.75rem/1.8）。
"""
import io
import os
import re

PY = """
子zǐ 夏xià 曰yuē ： ||
仕shì 而ér 优yōu 则zé 学xué ， ||
学xué 而ér 优yōu 则zé 仕shì 。 ||
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '1.75rem'
LH = '1.8'


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
            style = ('padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:%s;'
                     'line-height:%s;width:100%%;max-width:none;margin:0' % (FS, LH))
        else:
            style = ('text-align:left;text-indent:0;letter-spacing:0.06em;font-size:%s;line-height:%s;'
                     'width:100%%;max-width:none;margin:0.1em 0 0' % (FS, LH))
        out.append('<p style="%s">%s</p>' % (style, ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="《论语·子张》第十二章精讲：子夏曰：仕而优则学，学而优则仕。「优」不是优秀，是有余力。做事做完了还有力气，就回头读书；读书读通了还有余力，就去做事。学和做不是两截，是来回倒的两条腿。" name="description"/>
<meta content="仕而优则学 · 有余力才学，学有余力再做 · 国学课堂" property="og:title"/>
<meta content="《论语·子张》第十二章精讲：学与做，是来回倒的两条腿" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/473-shi-er-you-ze-xue/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/473-shi-er-you-ze-xue/index.html" rel="canonical"/>
<title>仕而优则学 · 有余力才学，学有余力再做 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=zhangz473" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=zhangz473" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">仕而优则学</h2><div class="cover-ornament"></div><p class="cover-subtitle">有余力才学，学有余力再做</p><p class="cover-desc">这是<strong>《论语·子张》第十二章</strong>。<strong>子夏</strong>说：<strong>做事做完了还有余力，就回头读书</strong>；<strong>读书读通了还有余力，就去做事</strong>。<strong>注意「优」不是优秀，是有余力——学和做不是两截，是来回倒的两条腿。</strong></p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:18px 16px 14px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>子夏说：做官做事，做完了还有余力，就去学；学通了还有余力，就去做官做事。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《子张》第十二章</strong>；<strong>合章本作 19.13</strong>；<strong>「优」读 yōu，是有余力，不是优秀</strong>；<strong>「仕」读 shì，是做官、做事</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>学与做，两条腿轮流走。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">仕</span>：<strong>仕 读 shì，做官、做事</strong>——<strong>不是「读书人的特权」</strong>。</p><p><span class="ds-highlight">而</span>：<strong>而 是「做完了、然后」</strong>——<strong>一头在前，一头在后</strong>。</p><p><span class="ds-highlight">优</span>：<strong>优 读 yōu，本义是优裕、有余力</strong>——<strong>不是「优秀、考第一」</strong>，这是全章最容易错的一个字。</p><p><span class="ds-highlight">则</span>：<strong>则 是「就」</strong>——<strong>顺下来的一步，不是硬规定</strong>。</p><p><span class="ds-highlight">学</span>：<strong>读书、问明白</strong>——<strong>做事做得糊涂了，就回来学</strong>。</p><p><span class="ds-highlight">两头</span>：<strong>仕一头，学一头</strong>——<strong>不是先后的门槛，是来回的路</strong>。</p><p><span class="ds-highlight">留余力</span>：<strong>做事的余地</strong>——<strong>一点余力都不留，就学不进、也做不长</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>「优」是有余力，不是优秀；有劲才走得动下一段。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：仕而优则学</h2><h3>“ 仕 而 优 则 学 ”</h3><p style="margin:0"><strong>「仕」是什么？</strong><br/><br/>① <strong>做官，也泛指做事、担差事</strong><br/>② <strong>不是非当官不可</strong><br/><br/><strong>一句话：手上有一份正经差事，就叫仕。</strong></p><p><strong>「优」为什么不是优秀？</strong><br/><br/>① <strong>优是优裕，宽宽有余</strong><br/>② <strong>事情办完，人还有力气</strong><br/><br/><strong>一句话：优是「还有余」，不是「分数高」。</strong></p><p><strong>为什么有了余力才学？</strong><br/><br/>① <strong>忙到脚不沾地，书读进去也留不住</strong><br/>② <strong>有余力，心才装得下新东西</strong><br/><br/><strong>一句话：先留出一点空，才装得进学问。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：学而优则仕</h2><h3>“ 学 而 优 则 仕 ”</h3><p style="margin:0"><strong>这句是反过来讲的？</strong><br/><br/>① <strong>是。上一句做事回头看，这句读书向前走</strong><br/>② <strong>同一个「优」，两个方向</strong><br/><br/><strong>一句话：一句话去，一句话回。</strong></p><p><strong>「学而优」是学得好吗？</strong><br/><br/>① <strong>还是余力：书读通了，还有心力</strong><br/>② <strong>不是考第一才准出门</strong><br/><br/><strong>一句话：学有余力，就该下场试试。</strong></p><p><strong>为什么不让人一直读下去？</strong><br/><br/>① <strong>只读不做，学问发虚</strong><br/>② <strong>做一遍，才知道哪句是真懂</strong><br/><br/><strong>一句话：书要落地，才算读过。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：「优」这个字的分量</h2><h3>“ 优 ” 字 的 本 义</h3><p style="margin:0"><strong>「优」原来什么意思？</strong><br/><br/>① <strong>优裕、宽宽有余</strong><br/>② <strong>说人「优」，是说他从容、不紧巴</strong><br/><br/><strong>一句话：优是宽出来的那一截。</strong></p><p><strong>今义怎么变了？</strong><br/><br/>① <strong>今天说优，多是优秀、优良</strong><br/>② <strong>拿着今义读古书，这句话就读歪了</strong><br/><br/><strong>一句话：一字之差，整句都偏。</strong></p><p><strong>为什么单挑这个字讲？</strong><br/><br/>① <strong>不懂「优」，就成了「学好才能做官」</strong><br/>② <strong>懂了「优」，才知道他说的是有余力</strong><br/><br/><strong>一句话：抓住一个字，整章就通了。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：整章连起来读</h2><h3>“ 仕 而 优 则 学 ”</h3><p style="margin:0"><strong>一句话讲什么？</strong><br/><br/>① <strong>学和做，是一辈子的两件事</strong><br/>② <strong>哪一头有余力，就往另一头走一步</strong><br/><br/><strong>一句话：不是先后的门槛，是来回的路。</strong></p><p><strong>和 472 课怎么呼应？</strong><br/><br/>① <strong>472 讲打底子的活不能轻看</strong><br/>② <strong>这章讲做与学要接得上</strong><br/><br/><strong>一句话：前章讲别嫌小，这章讲别断开。</strong></p><p><strong>整章记一句什么？</strong><br/><br/>① <strong>做事的人别丢书，读书的人别怕动手</strong><br/>② <strong>两头都留余力，路就长</strong><br/><br/><strong>一句话：学做相济，才走得远。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「优」</h2><p>一句话，三层意思——</p><h3>“「优」是有余力，不是优秀；有劲才走得动下一段。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>仕而优则学——做完了还有劲，就回头读书。</p><p>📚 做完再读</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>学而优则仕——读通了还有心力，就下场做事。</p><p>🛠 读通再做</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>两头是一件事，来回倒着走。</p><p>⚖ 落点是「学做相济，别断开」</p>
<p>接 472 课：<strong>上一章讲基本功不能轻看，这一章讲做与学要接得上</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「优」是优秀吗？</h3><p><strong>不是。优是有余力、优裕。</strong><br/><br/>① <strong>做完了，人还剩力气</strong><br/>② <strong>不是考第一、评先进</strong><br/>③ <strong>拿今义去读，整句就歪了</strong><br/><br/><strong>记法：优＝有余，不是＝最好。</strong></p><h3>❓ 是不是「学好了才准做事」？</h3><p><strong>不是门槛，是来回。</strong><br/><br/>① <strong>做事有余力，就回去学</strong><br/>② <strong>学有余力，就下场做</strong><br/>③ <strong>子夏说的是两头接上，不是设关卡</strong><br/><br/><strong>记法：两条腿走路，不分先后高下。</strong></p><h3>❓ 今天这句话怎么用？</h3><p><strong>上班的人别丢书，读书的人别怕动手。</strong><br/><br/>① <strong>干久了要回头补课</strong><br/>② <strong>学久了要找个地方试</strong><br/>③ <strong>两头都留一点余力</strong><br/><br/><strong>记法：学一段、做一段，别一头到底。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📚 做事别做到没劲</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>忙得一点空不留，书就读不进去</strong>；<strong>留出余力，是给下一段路备干粮</strong>。</p><p>🛠 学别学成空转</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>学到能用才算会</strong>；<strong>只在纸上打转，容易发虚</strong>。</p><p>⚖ 两头轮流走</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>干一段、学一段，样样都长进</strong>；<strong>一头到底，人容易僵</strong><br/><br/><strong>本章的落点：有余力才学，学有余力再做。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「仕而优则学」。记牢：<strong>「优」是有余力，不是优秀</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">
                子夏曰：仕而优则学，学而优则仕。
            </p><p>回顾本课要点:</p><p>仕而优则学 · 做完再读</p><br/><p><strong>一点空不留，学问进不来。</strong></p><p>学而优则仕 · 读通再做</p><br/><p><strong>书要落地，才算真懂。</strong></p><p>优字本义 · 有余力不是优秀</p><br/><strong>一字读错，整章都偏。</strong><p><strong>在全篇中的位置:</strong>这是<strong>《子张》第十二章</strong>。接 472 课：上一章讲基本功不能轻看，这一章讲做与学要接得上。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>子夏曰：仕而优则学，学而优则仕。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：你手上哪件事做久了，该回头补一课？② 背一句：仕而优则学，学而优则仕。</p><p><strong>把这一章记在心里:</strong><strong>学做相济，别一头到底。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “子夏曰：仕而优则学，学而优则仕。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·子张》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '473-shi-er-you-ze-xue';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《子张》', '《子路》', '《宪问》'], ans: 0, exp: '这是《子张》第十二章，子夏的话'},
  {q: '2. 「仕」是什么意思？', opts: ['做官、做事', '读书', '退休'], ans: 0, exp: '仕读 shì，做官，也泛指担一份正经差事'},
  {q: '3. 「优」在这里是什么意思？', opts: ['有余力、优裕', '优秀、考第一', '优待、照顾'], ans: 0, exp: '优是有余力——事情办完，人还有劲，全章最关键的一个字'},
  {q: '4. 「仕而优则学」怎么讲？', opts: ['做完事还有余力，就回头读书', '做官优秀了才去读书', '做官的人不用读书'], ans: 0, exp: '做事做完了还有劲，心才装得下新东西'},
  {q: '5. 「学而优则仕」怎么讲？', opts: ['读通了还有余力，就去做事', '读书优秀才能做官', '读书人不能做事'], ans: 0, exp: '学有余力就下场试试——书要落地才算读过'},
  {q: '6. 这两句话是什么关系？', opts: ['一往一返，来回接上', '先学后做，一步不能乱', '只能选一条路'], ans: 0, exp: '不是门槛，是来回的路：哪头有余力就往另一头走'},
  {q: '7. 「则」是什么意思？', opts: ['就', '却', '如果'], ans: 0, exp: '则是「就」，顺着下来的下一步，不是硬规定'},
  {q: '8. 本章最容易读错的是哪个字？', opts: ['优（当成优秀）', '仕（当成读书）', '学（当成学校）'], ans: 0, exp: '拿着今义读古书，这一句就歪了'},
  {q: '9. 本章讲的中心是什么？', opts: ['学和做要接得上，不能断', '读书比做事高', '做事比读书实在'], ans: 0, exp: '两头是一件事，来回倒着走'},
  {q: '10. 这一章给我们的提醒是？', opts: ['做事留余力，学了要用得上', '先拼命干，没空读书', '一门心思读书，别动手'], ans: 0, exp: '学做相济，别一头到底'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=zhangz473"></script><script src="../../assets/js/slide-engine.js?v=zhangz473"></script>
<script src="../../assets/js/speech.js?v=zhangz473"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=zhangz473"></script>
<script defer="" src="../../assets/js/auth.js?v=zhangz473"></script>
<script defer="" src="../../assets/js/api-client.js?v=zhangz473"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '473-shi-er-you-ze-xue')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
