# -*- coding: utf-8 -*-
"""生成第 452 课《微子》第一章「殷有三仁焉」课件。
原文 24 字、分四段，字号 2.0rem。
"""
import io
import os
import re

PY = """
微wēi 子zǐ 去qù 之zhī ， || 箕jī 子zǐ 为wéi 之zhī 奴nú ， || 比bǐ 干gān 谏jiàn 而ér 死sǐ 。 || 孔kǒng 子zǐ 曰yuē ： 殷yīn 有yǒu 三sān 仁rén 焉yān 。
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.0rem'
LH = '1.9'


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
<meta content="《论语·微子》第一章精讲：微子去之，箕子为之奴，比干谏而死。孔子曰：殷有三仁焉。同是一个烂摊子，一个走了，一个装疯忍下来，一个把命送了。三条路，孔子都认。" name="description"/>
<meta content="殷有三仁焉 · 三个人的活法，一个仁字 · 国学课堂" property="og:title"/>
<meta content="《论语·微子》第一章精讲：三个人的活法，一个仁字" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/452-yin-you-san-ren-yan/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/452-yin-you-san-ren-yan/index.html" rel="canonical"/>
<title>殷有三仁焉 · 三个人的活法，一个仁字 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=weizi452" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=weizi452" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">殷有三仁焉</h2><div class="cover-ornament"></div><p class="cover-subtitle">三个人的活法，一个「仁」字</p><p class="cover-desc">这是<strong>《论语·微子》第一章</strong>。商朝末年，纣王无道，三个人各走了一条路：<strong>一个走了，一个装疯做奴，一个把命丢在朝堂上</strong>。孔子只说了六个字——<strong>殷有三仁焉</strong>。<strong>三条路，他都认</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:20px 18px 16px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>微子离开了纣王，箕子装疯做了奴隶，比干强谏被剖心而死。孔子说：殷朝有三位仁人啊。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《微子》开篇第一章</strong>；<strong>合章本作 18.1</strong>；<strong>微子是纣王的同母兄，箕子、比干是纣王的叔父</strong>；<strong>三个人都是商朝宗室，看着同一个烂摊子</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>同一件事，三条路，孔子一个都没挑毛病。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 八个关节</h2><p><span class="ds-highlight">微子</span>：<strong>名启，纣王的同母兄，封在微</strong>——<strong>「子」是尊称，不是儿子</strong>。</p><p><span class="ds-highlight">去</span>：<strong>离开</strong>——<strong>不是「死去」，是走人</strong>。</p><p><span class="ds-highlight">之</span>：<strong>他，指纣王</strong>——<strong>「去之」就是离开他</strong>。</p><p><span class="ds-highlight">箕子</span>：<strong>名胥余，纣王的叔父，封在箕</strong>——<strong>箕 jī，不读 qí</strong>。</p><p><span class="ds-highlight">为</span>：<strong>做，读 wéi</strong>——<strong>「为之奴」是给他做奴，不读 wèi</strong>。</p><p><span class="ds-highlight">比干</span>：<strong>纣王的叔父，官至少师</strong>——<strong>干读 gān</strong>。</p><p><span class="ds-highlight">谏</span>：<strong>下对上直言相劝</strong>——<strong>不是「商量」，是明说「你错了」</strong>。</p><p><span class="ds-highlight">殷 · 焉</span>：<strong>殷就是商朝</strong>；<strong>「焉」是句末语气，等于「在其中」</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>走的是微子，忍的是箕子，死的是比干。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：微子去之</h2><h3>“ 微 子 去 之 ”</h3><p style="margin:0"><strong>微子为什么走？</strong><br/><br/>① <strong>劝过，劝不动；再劝，命也保不住</strong><br/>② <strong>走，是不陪着一起做坏事</strong><br/><br/><strong>一句话：走，不是不忠，是不肯同流。</strong></p><p><strong>走算不算躲？</strong><br/><br/>① <strong>他劝过，话都说尽了</strong><br/>② <strong>留下只会一起烂，也帮不上一个人</strong><br/><br/><strong>一句话：该说的说完了，走才是剩下的办法。</strong></p><p><strong>那他就不管殷商了？</strong><br/><br/>① <strong>后来武王伐纣，微子带着祭器归周</strong><br/>② <strong>他求的是保住殷商的香火，不是保住纣王</strong><br/><br/><strong>一句话：人走了，那点根还留着。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：箕子为之奴</h2><h3>“ 箕 子 为 之 奴 ”</h3><p style="margin:0"><strong>箕子为什么不走？</strong><br/><br/>① <strong>他是叔父，也是朝里的老臣</strong><br/>② <strong>他一走，就再没人能劝上一句</strong><br/><br/><strong>一句话：他留下，是替这个朝廷守着最后一点体面。</strong></p><p><strong>装疯做奴，这不是没骨气吗？</strong><br/><br/>① <strong>他不怕死，是知道死了没用</strong><br/>② <strong>装疯是把自己藏起来，等一个还能说话的时候</strong><br/><br/><strong>一句话：忍，不是为了活，是为了还有用。</strong></p><p><strong>后来怎么了？</strong><br/><br/>① <strong>武王灭商之后，专门向他请教治国之道</strong><br/>② <strong>《尚书·洪范》就是箕子讲给武王听的</strong><br/><br/><strong>一句话：一身学问留到了新朝，这才叫没白忍。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：比干谏而死</h2><h3>“ 比 干 谏 而 死 ”</h3><p style="margin:0"><strong>比干为什么非说不可？</strong><br/><br/>① <strong>他是叔父，也是少师，劝谏是本分</strong><br/>② <strong>纣王说「我听说圣人的心有七窍」，当场剖开看</strong><br/><br/><strong>一句话：他知道会死，还是把话说完了。</strong></p><p><strong>明知没用，说了不算白死？</strong><br/><br/>① <strong>他要的不是纣王听进去，是自己没把话咽回去</strong><br/>② <strong>一个人到死都不改口，这就是个样子</strong><br/><br/><strong>一句话：有些话，说出来比管用要紧。</strong></p><p><strong>孔子怎么看他？</strong><br/><br/>① <strong>一个「仁」字，给了他</strong><br/>② <strong>没说他笨，也没说他不量力</strong><br/><br/><strong>一句话：孔子不拿成败算账，只看那颗心。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：殷有三仁焉</h2><h3>“ 殷 有 三 仁 焉 ”</h3><p style="margin:0"><strong>三条路，怎么都算仁？</strong><br/><br/>① <strong>一个走、一个忍、一个死，做法全不一样</strong><br/>② <strong>可心里守的是同一样东西：不肯跟着坏</strong><br/><br/><strong>一句话：仁不是一个做法，是一个心。</strong></p><p><strong>孔子是不是在替三个人开脱？</strong><br/><br/>① <strong>不是。他一生最讲分寸，这话说得很实</strong><br/>② <strong>「三仁」是把三人放一处看：路子不同，底子一样</strong><br/><br/><strong>一句话：他认的是那个底子。</strong></p><p><strong>那我们遇上烂局面，学哪一条？</strong><br/><br/>① <strong>先看自己在那个位置上还能做什么</strong><br/>② <strong>能劝就劝，能守就守，该走就走——别学样，学心</strong><br/><br/><strong>一句话：路自己选，心别丢了。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「三仁」</h2><p>一句话，三层意思——</p><h3>“殷有三仁焉。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>走的、忍的、死的，三条路，三种结局。</p><p>🛤️ 路是自己挑的，命跟着路走</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>路不同，心一样——都不肯跟着坏下去。</p><p>❤️ 仁看的是心，不是做法</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>遇上改不了的局面，选哪条都行，心别丢。</p><p>🌱 学的是那份心，不是那个样</p>
<p>这一课<strong>接 451 课</strong>，也是<strong>《微子》的开篇</strong>——前一篇讲人心世道之病，这一篇第一句就摆出<strong>三个人的样子</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 微子、箕子、比干都是什么人？</h3><p><strong>都是商朝宗室，一家人。</strong><br/><br/>① <strong>微子名启，是纣王同母的哥哥</strong><br/>② <strong>箕子名胥余、比干，都是纣王的叔父</strong><br/>③ <strong>三个人劝的是同一个纣王，一个比一个亲</strong><br/><br/><strong>记法：一家人劝一个人，谁也没劝住。</strong></p><h3>❓ 箕子装疯做奴，不算没骨气吗？</h3><p><strong>不算。骨气看的是心里那根线，不是脸上的样子。</strong><br/><br/>① <strong>他不肯说一句软话，才被贬为奴、关了起来</strong><br/>② <strong>装疯是把自己藏住，好留着那条命做点事</strong><br/>③ <strong>后来他把治国的大法讲给了武王，一身学问没白留</strong><br/><br/><strong>记法：不怕死的人，才敢装疯活着。</strong></p><h3>❓ 这三条路，我们普通人学哪一条？</h3><p><strong>学心，不学样。</strong><br/><br/>① <strong>平常日子用不上死谏，也别拿「我要学比干」当脾气</strong><br/>② <strong>能劝的时候劝一句，能守的时候别撂挑子，该走的时候别恋着</strong><br/>③ <strong>要紧的是那句——不跟着坏</strong><br/><br/><strong>记法：路自己挑，底线别松。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🏃 该走的时候，别恋着</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>话劝尽了、理说透了，人家还是那样</strong>；<strong>就别把自己也搭进去</strong>。</p><p>🧱 该守的时候，别撂挑子</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>家里、班上，总有一摊事只有你还在</strong>；<strong>忍一忍、顶一顶，比甩手走人有用</strong>。</p><p>🗣 该说的时候，别把话咽回去</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>明知人家不听，该说的还是得说</strong>；<strong>说了不后悔，咽下去才后悔</strong><br/><br/><strong>本章的落点：路可以不同，心不能丢。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「殷有三仁焉」。记牢：<strong>三个人的活法，一个「仁」字。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                微子去之，箕子为之奴，比干谏而死。
            </p><p>回顾本课要点:</p><p>微子去之 · 劝不动就走，是不肯同流</p><br/><p><strong>走，不是不忠。</strong></p><p>箕子为之奴 · 装疯守着，是为留着有用</p><br/><p><strong>忍，不是为了活。</strong></p><p>比干谏而死 · 话说完再死，是没把话咽回去</p><br/><p><strong>有些话，说出来比管用要紧。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《微子》第一章</strong>；接 451 课，前一篇讲人心之病，<strong>这一篇开篇就摆出三个人的样子</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>微子去之，箕子为之奴，比干谏而死。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：身边有没有该说而没说的一句话？② 背一句：殷有三仁焉。③ 试一天：该说的话，说出口。</p><p><strong>把这一章记在心里:</strong><strong>路可以不同，心不能丢。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “微子去之，箕子为之奴，比干谏而死。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·微子》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '452-yin-you-san-ren-yan';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《微子》', '《阳货》', '《季氏》'], ans: 0, exp: '这是《微子》开篇第一章'},
  {q: '2. 「微子去之」的「去」是什么意思？', opts: ['离开', '死去', '前去'], ans: 0, exp: '「去」是走人，不是死去'},
  {q: '3. 微子和纣王是什么关系？', opts: ['同母的哥哥', '叔父', '外臣'], ans: 0, exp: '微子是纣王同母兄'},
  {q: '4. 「箕子为之奴」的「为」怎么读？', opts: ['wéi，做', 'wèi，为了', 'wéi，因为'], ans: 0, exp: '「为之奴」是给他做奴，读 wéi'},
  {q: '5. 箕子为什么要装疯？', opts: ['知道死了没用，要留着有用', '怕死', '想当官'], ans: 0, exp: '忍，是为了还有用'},
  {q: '6. 比干是怎么死的？', opts: ['强谏被剖心', '战死沙场', '病死家中'], ans: 0, exp: '纣王当场剖心，他还在说'},
  {q: '7. 「殷」指的是哪个朝代？', opts: ['商朝', '周朝', '夏朝'], ans: 0, exp: '盘庚迁殷后，商也称殷'},
  {q: '8. 孔子对这三人怎么评价？', opts: ['三个都算仁人', '只有比干算仁', '一个都不算'], ans: 0, exp: '「殷有三仁焉」'},
  {q: '9. 三人做法不同，相同的是什么？', opts: ['都不肯跟着坏下去', '都想做官', '都跑了'], ans: 0, exp: '仁不是一个做法，是一个心'},
  {q: '10. 这一章最要紧的落点是哪一句？', opts: ['路可以不同，心不能丢', '遇事就得死谏', '遇事就得走'], ans: 0, exp: '学心，不学样'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=weizi452"></script><script src="../../assets/js/slide-engine.js?v=weizi452"></script>
<script src="../../assets/js/speech.js?v=weizi452"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=weizi452"></script>
<script defer="" src="../../assets/js/auth.js?v=weizi452"></script>
<script defer="" src="../../assets/js/api-client.js?v=weizi452"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '452-yin-you-san-ren-yan')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
