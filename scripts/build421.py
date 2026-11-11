# -*- coding: utf-8 -*-
"""生成第 421 课《季氏》第六章「侍于君子有三愆」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
孔kǒng 子zǐ 曰yuē ： 「 侍shì 于yú 君jūn 子zǐ 有yǒu 三sān 愆qiān ： ||
言yán 未wèi 及jí 之zhī 而ér 言yán 谓wèi 之zhī 躁zào ， ||
言yán 及jí 之zhī 而ér 不bù 言yán 谓wèi 之zhī 隐yǐn ， ||
未wèi 见jiàn 颜yán 色sè 而ér 言yán 谓wèi 之zhī 瞽gǔ 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.2rem'
LH = '1.68'  # 本科原文四行，行距略收紧，与三行原文版面观感一致


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
                     'width:100%%;max-width:none;margin:0.2em 0 0' % (FS, LH))
        out.append('<p style="%s">%s</p>' % (style, ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="《论语·季氏》第六章精讲：侍于君子有三愆。言未及之而言谓之躁，言及之而不言谓之隐，未见颜色而言谓之瞽。孔子点出说话的三种病——抢话是躁，该说不说是隐，不看脸色就开口是瞽。三种都不错在话上，错在时候上。" name="description"/>
<meta content="侍于君子有三愆 · 话不看时候，就是病 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第六章精讲：话不看时候，就是病" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/421-shi-yu-jun-zi-you-san-qian/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/421-shi-yu-jun-zi-you-san-qian/index.html" rel="canonical"/>
<title>侍于君子有三愆 · 话不看时候就是病 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi421" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi421" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">侍于君子有三愆</h2><div class="cover-ornament"></div><p class="cover-subtitle">话不看时候，就是病</p><p class="cover-desc">这是<strong>《论语·季氏》第六章</strong>。上一章说挑什么乐，这一章说<strong>怎么开口</strong>。孔子点了三样最容易犯的病：<strong>还没轮到你，抢着说，是躁</strong>；<strong>该你说了，却不说，是隐</strong>；<strong>不看脸色就张口，是瞽</strong>。三样都不是错在话上，是<strong>错在时候上</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:8px;">原文呈现</h2><div class="ds-quote" style="margin:10px 0;padding:26px 30px 24px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>孔子说：陪着君子说话，容易犯三种过失：话还没说到那儿就抢着开口，这叫急躁；话该说了却不说，这叫隐瞒；不看对方脸色就开口，这叫瞎说</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第六章</strong>；<strong>合章本多作 16.6</strong>；<strong>"愆"就是过失</strong>；<strong>"颜色"指脸色，不是色彩</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>小记</strong>：<strong>话本身没错，时候错了就是错</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">侍</span>：<strong>陪侍、陪着</strong>——<strong>不是端茶送水，是陪着说话</strong>。</p><p><span class="ds-highlight">愆（qiān）</span>：<strong>过失、毛病</strong>——<strong>三愆＝三种说话的病</strong>。</p><p><span class="ds-highlight">言未及之</span>：<strong>话还没到这儿</strong>——<strong>时机没到</strong>。</p><p><span class="ds-highlight">躁</span>：<strong>急躁、抢话</strong>——<strong>抢的不是理，是位置</strong>。</p><p><span class="ds-highlight">隐</span>：<strong>藏着不说</strong>——<strong>该说时闭嘴，也是错</strong>。</p><p><span class="ds-highlight">颜色</span>：<strong>脸色、神情</strong>——<strong>不是"色彩"</strong>。</p><p><span class="ds-highlight">瞽（gǔ）</span>：<strong>瞎子</strong>——<strong>不是真瞎，是眼里没别人</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>话不看时候，就是病</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：侍于君子有三愆</h2><h3>“ 侍 于 君 子 有 三 愆 ”</h3><p style="margin:0"><strong>为什么先讲"三愆"，不讲"三善"？</strong><br/><br/>① <strong>毛病好认，好处难说</strong><br/>② <strong>先让人知道哪儿容易错，比讲大道理实在</strong><br/><br/><strong>一句话：先讲病，再讲药。</strong></p><p><strong>为什么单提"侍于君子"？</strong><br/><br/>① <strong>跟长辈、上级说话，最容易失分寸</strong><br/>② <strong>位置差一层，紧了就慌，松了就乱</strong><br/><br/><strong>一句话：越是高下有别，越要守时候。</strong></p><p><strong>三种病有共同处吗？</strong><br/><br/>① <strong>都不在"说什么"，在"什么时候说"</strong><br/>② <strong>话本身没错，时候错了</strong><br/><br/><strong>一句话：一样病，三样相。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：言未及之而言谓之躁</h2><h3>“ 言 未 及 之 而 言 谓 之 躁 ”</h3><p style="margin:0"><strong>「躁」只是性子急吗？</strong><br/><br/>① <strong>不只是急，是抢</strong><br/>② <strong>抢话的人，图的是让人知道自己知道</strong><br/><br/><strong>一句话：抢着说，抢的不是理，是位置。</strong></p><p><strong>抢话有什么坏处？</strong><br/><br/>① <strong>打断别人，话说不到点上</strong><br/>② <strong>说早了，答的往往不是人家要问的</strong><br/><br/><strong>一句话：话说早了，等于白说。</strong></p><p><strong>忍不住怎么办？</strong><br/><br/>① <strong>先听三句，再开口</strong><br/>② <strong>心里过一遍：这话非此刻说不可吗</strong><br/><br/><strong>一句话：忍三句，话就值钱了。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：不说，和不看</h2><h3>“ 言 及 之 而 不 言 谓 之 隐 ， 未 见 颜 色 而 言 谓 之 瞽 ”</h3><p style="margin:0"><strong>「隐」为什么也算过失？</strong><br/><br/>① <strong>该说时不说，人家就当你没话说</strong><br/>② <strong>藏着看着稳妥，其实误事</strong><br/><br/><strong>一句话：该说时闭嘴，也是错。</strong></p><p><strong>「未见颜色」是什么意思？</strong><br/><br/>① <strong>不看对方脸色，不看他听进去没有</strong><br/>② <strong>人家已经不耐烦，你还在往下讲</strong><br/><br/><strong>一句话：不看脸，就是蒙着眼说话。</strong></p><p><strong>「瞽」说得重不重？</strong><br/><br/>① <strong>瞽是瞎子，这个字很重</strong><br/>② <strong>不是骂人，是提醒：眼里没别人，跟瞎一样</strong><br/><br/><strong>一句话：看不见人，话就落不到人心里。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：三个"谓之"</h2><h3>“ 谓 之 躁 。 谓 之 隐 。 谓 之 瞽 ”</h3><p style="margin:0"><strong>连用三个"谓之"，有什么讲究？</strong><br/><br/>① <strong>谓之＝这叫做，是给病起个名</strong><br/>② <strong>起了名，才认得出、改得掉</strong><br/><br/><strong>一句话：有了名，才好治。</strong></p><p><strong>三样里哪样最常见？</strong><br/><br/>① <strong>躁最常见，年轻人尤甚</strong><br/>② <strong>隐最不易觉察，因为不出声</strong><br/><br/><strong>一句话：抢话惹眼，藏话误事。</strong></p><p><strong>这一章跟上一章什么关系？</strong><br/><br/>① <strong>上一章讲图什么乐</strong><br/>② <strong>这一章讲怎么开口</strong><br/><br/><strong>一句话：乐要有节，话也要有节。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 四层看说话</h2><p>这一章说的是开口，一层比一层实——</p><h3>“侍于君子有三愆”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>分向：</strong>说话先分时候。</p><p>📜 三愆都不在内容，在时机</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>辨躁：</strong>早说叫抢。</p><p>⏳ 话没轮到你，先开口，是躁</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>辨隐：</strong>不说也叫错。</p><p>🤐 该你说时闭嘴，是隐</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>辨瞽：</strong>不看脸叫瞎。</p><p>👀 眼里没别人，话就白说</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第六章，<strong>承上章讲怎么开口</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 该说的时候不说，为什么也算错？</h3><p><strong>不出声，也是一种回答。</strong><br/><br/>① <strong>人家问你，你不说，人家只能猜</strong><br/>② <strong>猜错了，事就坏了，还怪不到你头上</strong><br/>③ <strong>藏着看着稳，其实最误事</strong><br/><br/><strong>记法：该开口时开口，是责任。</strong></p><h3>❓ 「未见颜色」是要学着看人下菜吗？</h3><p><strong>不是看人下菜，是看人在不在听。</strong><br/><br/>① <strong>看脸色，是看他听懂没有、还有没有耐心</strong><br/>② <strong>不是讨好，是别白费口舌</strong><br/>③ <strong>该说的，脸色再难看也要说；不该说的，脸色再好也别多说</strong><br/><br/><strong>记法：看脸是为了说准，不是为了讨好。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>从"等别人说完"学起。</strong><br/><br/>① <strong>上课举手，等老师点到再说，就不躁</strong><br/>② <strong>会答的问题，敢说出来，就不隐</strong><br/>③ <strong>看老师讲到哪儿，再问，就不瞽</strong><br/><br/><strong>记法：等一等、敢开口、看时机。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📜 开口前先过三问</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>轮没轮到我</strong>；<strong>该不该我说</strong>；<strong>人家在不在听</strong>。<strong>三问都过了，再说</strong>。</p><p>⏳ 把"忍三句"当习惯</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>忍不住的时候，默数三句</strong>；<strong>数完还想说，那多半是该说的</strong>。</p><p>👀 该说的，别藏着</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>该你担的那句话，藏着不说</strong>；<strong>比说错更误事</strong><br/><br/><strong>本章的落点：话不看时候，就是病。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「侍于君子有三愆」。记牢：<strong>话不看时候，就是病。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                言未及之而言谓之躁，言及之而不言谓之隐，未见颜色而言谓之瞽。
            </p><p>回顾本课要点:</p><p>三愆 · 躁、隐、瞽</p><br/><p><strong>抢话、藏话、瞎说。</strong></p><p>共同处 · 不在内容，在时候</p><br/><p><strong>话没错，时候错了就是错。</strong></p><p>一个「谓之」 · 给病起名</p><br/><p><strong>有了名，才认得出、改得掉。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第六章</strong>；与 420 课连读——<strong>那课讲图什么乐，这课讲怎么开口</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>侍于君子有三愆：言未及之而言谓之躁，言及之而不言谓之隐，未见颜色而言谓之瞽。</p>
</div><p><strong>课后小挑战:</strong>① 今天听人说话，数一数自己插了几次嘴。② 背一句：言未及之而言谓之躁。</p><p><strong>把这一章记在心里:</strong><strong>话不看时候，就是病。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “言未及之而言谓之躁，言及之而不言谓之隐，未见颜色而言谓之瞽！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '421-shi-yu-jun-zi-you-san-qian';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《子路》'], ans: 0, exp: '按站内分法，这是《季氏》第六章'},
  {q: '2. 「侍于君子」的「侍」是什么意思？', opts: ['陪侍、陪着', '伺候起居', '等着候着'], ans: 0, exp: '侍是陪着，重点是陪着说话'},
  {q: '3. 「三愆」的「愆」是什么意思？', opts: ['过失、毛病', '谦虚', '期盼'], ans: 0, exp: '三愆就是三种说话的病'},
  {q: '4. 「言未及之而言」这种毛病叫什么？', opts: ['躁', '隐', '瞽'], ans: 0, exp: '话没轮到你，先开口，是躁'},
  {q: '5. 「躁」具体指什么行为？', opts: ['话没轮到你就抢着说', '说得又快又乱', '脾气急，爱发火'], ans: 0, exp: '抢着说，抢的不是理，是位置'},
  {q: '6. 「言及之而不言」这种毛病叫什么？', opts: ['隐', '躁', '瞽'], ans: 0, exp: '该你说时闭嘴，是隐'},
  {q: '7. 「隐」为什么也算过失？', opts: ['该说时不说，误了事', '话说得太含蓄', '藏着别人的功劳不说'], ans: 0, exp: '不出声，也是一种回答'},
  {q: '8. 「未见颜色而言」的「颜色」指什么？', opts: ['脸色、神情', '色彩、颜料', '衣服的颜色'], ans: 0, exp: '颜色在这里指脸色，不是色彩'},
  {q: '9. 「瞽」的本义是什么？', opts: ['瞎子', '耳朵聋', '嗓子哑'], ans: 0, exp: '不是骂人，是说眼里没别人'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['话不看时候，就是病', '侍于君子有三愆', '未见颜色而言谓之瞽'], ans: 0, exp: '三愆都不在内容，在时机'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi421"></script><script src="../../assets/js/slide-engine.js?v=jishi421"></script>
<script src="../../assets/js/speech.js?v=jishi421"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi421"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi421"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi421"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '421-shi-yu-jun-zi-you-san-qian')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
