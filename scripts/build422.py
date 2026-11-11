# -*- coding: utf-8 -*-
"""生成第 422 课《季氏》第七章「君子有三戒」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
孔kǒng 子zǐ 曰yuē ： 「 君jūn 子zǐ 有yǒu 三sān 戒jiè ： ||
少shào 之zhī 时shí ， 血xuè 气qì 未wèi 定dìng ， 戒jiè 之zhī 在zài 色sè ； ||
及jí 其qí 壮zhuàng 也yě ， 血xuè 气qì 方fāng 刚gāng ， 戒jiè 之zhī 在zài 斗dòu ； ||
及jí 其qí 老lǎo 也yě ， 血xuè 气qì 既jì 衰shuāi ， 戒jiè 之zhī 在zài 得dé 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.2rem'  # 本科原文四行且句长，字号行距收紧、段间不留隙，与三行原文版面观感一致
LH = '1.68'


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
                     'width:100%%;max-width:none;margin:0' % (FS, LH))
        out.append('<p style="%s">%s</p>' % (style, ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="《论语·季氏》第七章精讲：君子有三戒。少之时，血气未定，戒之在色；及其壮也，血气方刚，戒之在斗；及其老也，血气既衰，戒之在得。孔子按人生三段各点一戒——少年戒色，壮年戒斗，老年戒贪。" name="description"/>
<meta content="君子有三戒 · 什么年纪，戒什么 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第七章精讲：什么年纪，戒什么" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/422-jun-zi-you-san-jie/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/422-jun-zi-you-san-jie/index.html" rel="canonical"/>
<title>君子有三戒 · 什么年纪戒什么 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi422" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi422" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">君子有三戒</h2><div class="cover-ornament"></div><p class="cover-subtitle">什么年纪，戒什么</p><p class="cover-desc">这是<strong>《论语·季氏》第七章</strong>。上一章说怎么开口，这一章说<strong>怎么管住自己</strong>。孔子把人一辈子分成三段，每段点一样最该防的：<strong>少年戒色，壮年戒斗，老年戒贪</strong>。不是血气坏，是<strong>什么年纪有力气，就容易栽在哪儿</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:8px;">原文呈现</h2><div class="ds-quote" style="margin:10px 0;padding:26px 30px 24px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>孔子说：君子有三种要警戒的事：年轻的时候，血气还没定下来，要警戒的是女色；到了壮年，血气正旺，要警戒的是争强好斗；到了老年，血气已经衰退，要警戒的是贪得无厌</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第七章</strong>；<strong>合章本多作 16.7</strong>；<strong>"得"是贪得、舍不得</strong>；<strong>上一章讲怎么开口，这一章讲怎么管住自己</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>小记</strong>：<strong>毛病跟着年纪走，防要防在前头</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">戒</span>：<strong>警戒、提防</strong>——<strong>不是"不许有"，是"防着点"</strong>。</p><p><span class="ds-highlight">少（shào）</span>：<strong>年轻</strong>——<strong>不是"多少"的少</strong>。</p><p><span class="ds-highlight">血气</span>：<strong>身上的劲、火气</strong>——<strong>古人说的肉体里的力气</strong>。</p><p><span class="ds-highlight">未定 / 方刚 / 既衰</span>：<strong>还没定 / 正旺 / 已衰退</strong>——<strong>三段身体光景</strong>。</p><p><span class="ds-highlight">色</span>：<strong>女色、情欲</strong>——<strong>少年最容易栽的坑</strong>。</p><p><span class="ds-highlight">斗</span>：<strong>争胜、好胜</strong>——<strong>壮年最容易栽的坑</strong>。</p><p><span class="ds-highlight">得</span>：<strong>贪得、舍不得</strong>——<strong>老年最容易栽的坑</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>什么年纪，戒什么</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：君子有三戒</h2><h3>“ 君 子 有 三 戒 ”</h3><p style="margin:0"><strong>为什么用"戒"这个字？</strong><br/><br/>① <strong>戒是提防，不是禁令</strong><br/>② <strong>说的是"防着点"，不是"不许有"</strong><br/><br/><strong>一句话：戒是防，不是绝。</strong></p><p><strong>为什么分三段说？</strong><br/><br/>① <strong>人这一身的劲，一辈子在变</strong><br/>② <strong>什么年纪有力气，就容易栽在哪</strong><br/><br/><strong>一句话：毛病跟着年纪走。</strong></p><p><strong>三戒是给谁说的？</strong><br/><br/>① <strong>君子——想做正事的人</strong><br/>② <strong>不是骂人，是给人提个醒</strong><br/><br/><strong>一句话：想走得远，就得防着点。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：少之时，戒之在色</h2><h3>“ 少 之 时 ， 血 气 未 定 ， 戒 之 在 色 ”</h3><p style="margin:0"><strong>「血气未定」是什么意思？</strong><br/><br/>① <strong>身子还没长定，心也还没定</strong><br/>② <strong>这时候最容易跟着感觉走</strong><br/><br/><strong>一句话：没定的时候，最容易被牵走。</strong></p><p><strong>为什么少年戒"色"？</strong><br/><br/>① <strong>这时候心思最活，最容易被情欲拖住</strong><br/>② <strong>拖住了，学业身子一起垮</strong><br/><br/><strong>一句话：少年栽在色上，栽的是根。</strong></p><p><strong>今天该怎么理解？</strong><br/><br/>① <strong>不只男女之事，凡叫人上瘾、耗身子的都算</strong><br/>② <strong>手机、游戏、熬夜，一样在耗血气</strong><br/><br/><strong>一句话：耗身子的，都归这一类。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：壮戒斗，老戒得</h2><h3>“ 血 气 方 刚 ， 戒 之 在 斗 ； 血 气 既 衰 ， 戒 之 在 得 ”</h3><p style="margin:0"><strong>壮年为什么戒"斗"？</strong><br/><br/>① <strong>力气正足，最不服人</strong><br/>② <strong>一争高下，正事就办不成</strong><br/><br/><strong>一句话：力气大的时候，别用在争上。</strong></p><p><strong>老年为什么戒"得"？</strong><br/><br/>① <strong>力气退了，心里反而更怕失去</strong><br/>② <strong>越到晚年，越容易抓着不放</strong><br/><br/><strong>一句话：拿不动了还想拿，最伤人。</strong></p><p><strong>三戒有共同的理吗？</strong><br/><br/>① <strong>都是"顺着血气走"就出错</strong><br/>② <strong>旺的时候放纵，衰的时候贪恋</strong><br/><br/><strong>一句话：不是血气坏，是没管住。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：为什么是"戒"</h2><h3>“ 戒 之 在 色 。 戒 之 在 斗 。 戒 之 在 得 ”</h3><p style="margin:0"><strong>为什么说"戒"，不说"改"？</strong><br/><br/>① <strong>戒在事前，改在事后</strong><br/>② <strong>事前防一句，胜过事后改十句</strong><br/><br/><strong>一句话：戒得上，就不用改。</strong></p><p><strong>三戒里哪一条最难？</strong><br/><br/>① <strong>老年戒得最难，因为舍不得</strong><br/>② <strong>少年戒色最难，因为不觉得是错</strong><br/><br/><strong>一句话：最难的是不觉得难的那一条。</strong></p><p><strong>这一章跟上一章什么关系？</strong><br/><br/>① <strong>上一章讲怎么开口</strong><br/>② <strong>这一章讲怎么管自己</strong><br/><br/><strong>一句话：嘴管住了，还得管心。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看一生</h2><p>这一章说的是管自己，一层比一层深——</p><h3>“君子有三戒”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>分段：</strong>人生分三段。</p><p>📜 少年、壮年、老年，各有各的坎</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看气：</strong>哪样最旺，最容易栽。</p><p>⏳ 未定戒色，方刚戒斗，既衰戒得</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>防前：</strong>戒在事前。</p><p>🤐 事前防一句，胜过事后改十句</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第七章，<strong>承上章讲怎么管自己</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「戒之在色」只是说男女之事吗？</h3><p><strong>不止，凡耗身子、勾着心的都算。</strong><br/><br/>① <strong>少年人最怕两个字：上瘾</strong><br/>② <strong>手机、游戏、熬夜，一样在耗血气</strong><br/>③ <strong>戒的不是哪件事，是"收不住"</strong><br/><br/><strong>记法：看它耗不耗身子，就知道该不该戒。</strong></p><h3>❓ 老年戒"得"，是不许攒钱吗？</h3><p><strong>不是不许有，是不许贪。</strong><br/><br/>① <strong>该有的有，够用就行</strong><br/>② <strong>贪的是"还要更多"，不是"已经有了"</strong><br/>③ <strong>到了晚年还放不下，累的是自己</strong><br/><br/><strong>记法：够用是福，贪多成累。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>从"别耗身子"学起。</strong><br/><br/>① <strong>早睡，就是最实在的戒色</strong><br/>② <strong>不跟人争高低，是提前学戒斗</strong><br/>③ <strong>好东西肯分人，是提前学戒得</strong><br/><br/><strong>记法：小时候把身子养好，一辈子受用。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📜 先认清自己在哪一段</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>少年防上瘾</strong>，<strong>壮年防争胜</strong>，<strong>老年防贪多</strong>；<strong>看清了，才知道防什么</strong>。</p><p>⏳ 戒要戒在前面</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>别等栽了才后悔</strong>；<strong>事前一句提醒自己，省十次补救</strong>。</p><p>🤝 其实三戒是一件事</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>都是别让血气牵着走</strong>；<strong>身子管住了，心才安</strong><br/><br/><strong>本章的落点：什么年纪，戒什么。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「君子有三戒」。记牢：<strong>什么年纪，戒什么。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                少之时，血气未定，戒之在色；及其老也，血气既衰，戒之在得。
            </p><p>回顾本课要点:</p><p>三戒 · 色、斗、得</p><br/><p><strong>少年、壮年、老年，各有一坎。</strong></p><p>同一个理 · 顺着血气走就出错</p><br/><p><strong>不是血气坏，是没管住。</strong></p><p>一个「戒」字 · 防在事前</p><br/><p><strong>戒得上，就不用改。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第七章</strong>；与 421 课连读——<strong>那课讲怎么开口，这课讲怎么管自己</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>君子有三戒：少之时，血气未定，戒之在色。</p>
</div><p><strong>课后小挑战:</strong>① 想一想自己现在最该防哪一样。② 背一句：少之时，血气未定，戒之在色。</p><p><strong>把这一章记在心里:</strong><strong>什么年纪，戒什么。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “少之时，血气未定，戒之在色；及其老也，血气既衰，戒之在得！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '422-jun-zi-you-san-jie';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《阳货》'], ans: 0, exp: '按站内分法，这是《季氏》第七章'},
  {q: '2. 「君子有三戒」的「戒」是什么意思？', opts: ['警戒、提防', '戒掉不吃', '告诫别人'], ans: 0, exp: '戒是防，不是绝'},
  {q: '3. 「少之时」的「少」读什么？', opts: ['shào，指年轻', 'shǎo，指不多', 'shào，指官职'], ans: 0, exp: '这里是年纪小，读 shào'},
  {q: '4. 「血气未定」是什么意思？', opts: ['身子和心都还没长定', '血不够用', '气还没喘匀'], ans: 0, exp: '没定的时候，最容易被牵走'},
  {q: '5. 少年之时该戒什么？', opts: ['色', '斗', '得'], ans: 0, exp: '少之时，血气未定，戒之在色'},
  {q: '6. 「血气方刚」形容的是什么时候？', opts: ['壮年，力气正旺', '少年，血气未定', '老年，血气已衰'], ans: 0, exp: '方刚是正旺，说的是壮年'},
  {q: '7. 壮年之时该戒什么？', opts: ['斗', '色', '得'], ans: 0, exp: '力气大的时候，别用在争上'},
  {q: '8. 「戒之在得」的「得」是什么意思？', opts: ['贪得、舍不得', '得到的东西', '心得、体会'], ans: 0, exp: '拿不动了还想拿，最伤人'},
  {q: '9. 老年之时该戒什么？', opts: ['得', '斗', '色'], ans: 0, exp: '到了晚年，最怕抓着不放'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['什么年纪，戒什么', '君子有三戒', '戒之在斗'], ans: 0, exp: '毛病跟着年纪走，防要防在前头'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi422"></script><script src="../../assets/js/slide-engine.js?v=jishi422"></script>
<script src="../../assets/js/speech.js?v=jishi422"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi422"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi422"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi422"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '422-jun-zi-you-san-jie')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
