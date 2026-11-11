# -*- coding: utf-8 -*-
"""生成第 420 课《季氏》第五章「益者三乐，损者三乐」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
孔kǒng 子zǐ 曰yuē ： 「 益yì 者zhě 三sān 乐lè ， 损sǔn 者zhě 三sān 乐lè 。 ||
乐lè 节jié 礼lǐ 乐yuè ， 乐lè 道dào 人rén 之zhī 善shàn ， 乐lè 多duō 贤xián 友yǒu ， 益yì 矣yǐ 。 ||
乐lè 骄jiāo 乐lè ， 乐lè 佚yì 游yóu ， 乐lè 宴yàn 乐lè ， 损sǔn 矣yǐ 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.3rem'
LH = '1.85'


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
<meta content="《论语·季氏》第五章精讲：益者三乐，损者三乐。乐节礼乐，乐道人之善，乐多贤友，益矣；乐骄乐，乐佚游，乐宴乐，损矣。孔子把乐子分两类——有节制、说人好、多贤友的三种乐养人，骄纵享乐、放纵游荡、宴饮作乐的三种乐耗人。" name="description"/>
<meta content="益者三乐 · 什么乐子养人，什么乐子耗人 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第五章精讲：什么乐子养人，什么乐子耗人" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/420-yi-zhe-san-le/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/420-yi-zhe-san-le/index.html" rel="canonical"/>
<title>益者三乐 · 什么乐子养人什么乐子耗人 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi420" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi420" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">益者三乐</h2><div class="cover-ornament"></div><p class="cover-subtitle">什么乐子养人，什么乐子耗人</p><p class="cover-desc">这是<strong>《论语·季氏》第五章</strong>。上一章说交什么人，这一章说<strong>图什么乐</strong>。孔子把乐子分成两类，每类三样：<strong>乐节礼乐、乐道人之善、乐多贤友</strong>，这三种乐养人；<strong>乐骄乐、乐佚游、乐宴乐</strong>，这三种乐耗人。<strong>玩完更足还是更空</strong>——这一章，是教人挑乐子。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:8px;">原文呈现</h2><div class="ds-quote" style="margin:10px 0;padding:26px 30px 24px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>孔子说：有益的快乐有三种，有害的快乐有三种。以用礼乐节制自己为乐，以称道别人的好处为乐，以多交贤良的朋友为乐，这是有益的；以骄纵享乐为乐，以放纵游荡为乐，以宴饮作乐为乐，这是有害的</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第五章</strong>；<strong>合章本多作 16.5</strong>；<strong>这里的"乐"多作动词，是"以……为乐"</strong>；<strong>上一章讲跟谁在一起，这一章讲在一起做什么</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>小记</strong>：<strong>乐子躲不开，就看挑哪个</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">益 / 损</span>：<strong>有益 / 有害</strong>——<strong>对自己是养还是耗</strong>。</p><p><span class="ds-highlight">乐（lè）</span>：<strong>动词，以……为乐</strong>——<strong>不是"快乐"这个名词</strong>。</p><p><span class="ds-highlight">节礼乐（yuè）</span>：<strong>用礼乐来节制自己</strong>——<strong>「节」是划个边，「乐」这里读 yuè</strong>。</p><p><span class="ds-highlight">道人之善</span>：<strong>说别人的好处</strong>——<strong>不是揭人的短</strong>。</p><p><span class="ds-highlight">多贤友</span>：<strong>多交贤良的朋友</strong>——<strong>重在"贤"，不在"多"</strong>。</p><p><span class="ds-highlight">骄乐 / 佚游 / 宴乐</span>：<strong>骄纵享乐 / 放纵游荡 / 宴饮作乐</strong>——<strong>三种耗人的乐</strong>。</p><p><span class="ds-highlight">益矣 / 损矣</span>：<strong>就受益了 / 就吃亏了</strong>——<strong>「矣」是断语，说得很定</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>什么乐子养人，什么乐子耗人</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：益者三乐</h2><h3>“ 益 者 三 乐 ， 损 者 三 乐 ”</h3><p style="margin:0"><strong>为什么把"乐"分两类？</strong><br/><br/>① <strong>人总要找乐子，躲不开</strong><br/>② <strong>躲不开，就得挑：挑养人的，弃耗人的</strong><br/><br/><strong>一句话：乐子不是有没有，是挑哪个。</strong></p><p><strong>三种算多吗？</strong><br/><br/>① <strong>三是举其大要，挑最要紧的说</strong><br/>② <strong>两类各三样，一一对得上</strong><br/><br/><strong>一句话：记三样，别当账本。</strong></p><p><strong>这一句说给谁听？</strong><br/><br/>① <strong>说给所有人：当官的、念书的、种地的</strong><br/>② <strong>谁都有闲下来的时候</strong><br/><br/><strong>一句话：闲处最见人。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：乐节礼乐、乐道人之善、乐多贤友</h2><h3>“ 乐 节 礼 乐 ， 乐 道 人 之 善 ， 乐 多 贤 友 ”</h3><p style="margin:0"><strong>「乐节礼乐」怎么讲？</strong><br/><br/>① <strong>用礼乐来管住自己，不使性子</strong><br/>② <strong>「节」是节制，是给自己划个边</strong><br/><br/><strong>一句话：有节制的乐，才长久。</strong></p><p><strong>「道人之善」难在哪？</strong><br/><br/>① <strong>说人好处，比揭人短处难</strong><br/>② <strong>难在肯承认别人好</strong><br/><br/><strong>一句话：嘴里有善，心里才有。</strong></p><p><strong>「多贤友」为什么算一乐？</strong><br/><br/>① <strong>好人是最大的乐子</strong><br/>② <strong>跟贤人在一起，自己也在往上走</strong><br/><br/><strong>一句话：跟好人在一起，就是享福。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：乐骄乐、乐佚游、乐宴乐</h2><h3>“ 乐 骄 乐 ， 乐 佚 游 ， 乐 宴 乐 ”</h3><p style="margin:0"><strong>「骄乐」是什么？</strong><br/><br/>① <strong>摆阔、逞强、压人一头</strong><br/>② <strong>一时痛快，过后更空</strong><br/><br/><strong>一句话：拿别人垫脚的乐，不算乐。</strong></p><p><strong>「佚游」坏在哪？</strong><br/><br/>① <strong>佚＝放纵，游＝闲荡，无所事事</strong><br/>② <strong>一天两天看不出，久了人就散了</strong><br/><br/><strong>一句话：闲得没边，人就废了。</strong></p><p><strong>「宴乐」只是吃饭喝酒吗？</strong><br/><br/>① <strong>吃喝到没了分寸，就是它</strong><br/>② <strong>不是不许聚，是不许沉</strong><br/><br/><strong>一句话：桌上失了度，事就做不成。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：益矣、损矣</h2><h3>“ 益 矣 。 损 矣 ”</h3><p style="margin:0"><strong>一个「矣」字有什么分量？</strong><br/><br/>① <strong>矣＝了，是断语，不是商量</strong><br/>② <strong>不是"也许"，是"就是这样"</strong><br/><br/><strong>一句话：说得干脆，才记得住。</strong></p><p><strong>怎么知道自己在耗？</strong><br/><br/>① <strong>玩完了更累，那是耗</strong><br/>② <strong>玩完了更足，那是养</strong><br/><br/><strong>一句话：看结果，不看热闹。</strong></p><p><strong>这一章跟上一章什么关系？</strong><br/><br/>① <strong>上一章讲跟谁在一起</strong><br/>② <strong>这一章讲在一起做什么</strong><br/><br/><strong>一句话：人选对了，事也得选对。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层挑乐子</h2><p>这一章说的是挑乐子，一层比一层实——</p><h3>“益者三乐 · 损者三乐”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>分向：</strong>乐子先分益损。</p><p>📜 乐子不是都一样，有养人的，有耗人的</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>有节：</strong>乐要有边。</p><p>⏳ 节礼乐，是给自己划个边，不是不玩</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>向善：</strong>乐要往人身上去。</p><p>🤝 道人之善、多贤友，乐在人与人之间</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第五章，<strong>承上章讲人怎么乐</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 玩一玩也算"损"吗？</h3><p><strong>玩本身不算，沉进去才算。</strong><br/><br/>① <strong>有分寸的玩，是歇息</strong><br/>② <strong>玩到误了正事、伤了身子，就是佚游、宴乐</strong><br/>③ <strong>分界不在玩不玩，在收不收得住</strong><br/><br/><strong>记法：能停下来的玩，放心玩。</strong></p><h3>❓ 「乐」到底读什么音？</h3><p><strong>两个音，看位置。</strong><br/><br/>① <strong>当动词"以……为乐"，读 lè</strong><br/>② <strong>指礼乐、音乐，读 yuè</strong><br/>③ <strong>「乐节礼乐」四个字，前一个 lè，后一个 yuè</strong><br/><br/><strong>记法：说乐子读 lè，说礼乐读 yuè。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>从"玩完什么感觉"学起。</strong><br/><br/>① <strong>玩完更精神，那是好乐子</strong><br/>② <strong>玩完更累更烦，那就少碰</strong><br/>③ <strong>找一件能一直玩下去的正事</strong><br/><br/><strong>记法：玩完看感觉，感觉最诚实。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📜 挑乐子，先看收不收得住</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>能说停就停的，放心玩</strong>；<strong>一说停就翻脸的，趁早远</strong>。</p><p>⏳ 把"说人好"当乐子</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>一天说一句别人的好处</strong>；<strong>比一天挑一句短处，日子舒坦得多</strong>。</p><p>🤝 把朋友当选出来的乐子</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>贤友不是碰上的，是挑出来的</strong>；<strong>你挑谁，就成了谁</strong><br/><br/><strong>本章的落点：什么乐子养人，什么乐子耗人。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「益者三乐」。记牢：<strong>什么乐子养人，什么乐子耗人。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                乐节礼乐，乐道人之善，乐多贤友，益矣。
            </p><p>回顾本课要点:</p><p>益者三乐 · 有节、向善、交贤</p><br/><p><strong>有节制、说人好、跟好人在一起。</strong></p><p>损者三乐 · 骄纵、游荡、宴饮</p><br/><p><strong>一时痛快，过后更空。</strong></p><p>一个「矣」字 · 说得干脆</p><br/><p><strong>不是也许，就是这样。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第五章</strong>；与 419 课连读——<strong>那课讲交什么人，这课讲图什么乐</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>益者三乐，损者三乐。乐节礼乐，乐道人之善，乐多贤友，益矣。</p>
</div><p><strong>课后小挑战:</strong>① 数一数今天哪段时间玩完更累。② 背一句：乐节礼乐，乐道人之善，乐多贤友，益矣。</p><p><strong>把这一章记在心里:</strong><strong>什么乐子养人，什么乐子耗人。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “乐节礼乐，乐道人之善，乐多贤友，益矣！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '420-yi-zhe-san-le';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《先进》'], ans: 0, exp: '按站内分法，这是《季氏》第五章'},
  {q: '2. 「益者三乐」的「乐」是什么意思？', opts: ['以……为乐，爱好', '音乐', '快乐的样子'], ans: 0, exp: '这里是动词，是"以什么为乐"'},
  {q: '3. 「乐节礼乐」的「节」是什么意思？', opts: ['节制，划个边', '节日', '节奏'], ans: 0, exp: '节是节制，是给自己定个分寸'},
  {q: '4. 「乐节礼乐」中后一个「乐」读什么？', opts: ['yuè，指礼乐', 'lè，指快乐', 'yào，指喜好'], ans: 0, exp: '说乐子读 lè，说礼乐读 yuè'},
  {q: '5. 「乐道人之善」是什么意思？', opts: ['喜欢称道别人的好处', '喜欢给人讲道理', '喜欢议论别人的事'], ans: 0, exp: '说人好处，比揭人短处难'},
  {q: '6. 「乐多贤友」看重的是什么？', opts: ['朋友贤良，不在数量', '朋友越多越好', '朋友有钱有势'], ans: 0, exp: '重在"贤"，不在"多"'},
  {q: '7. 「乐骄乐」的「骄乐」指什么？', opts: ['骄纵享乐，逞强摆阔', '为功课好而高兴', '高兴地唱歌奏乐'], ans: 0, exp: '一时痛快，过后更空'},
  {q: '8. 「乐佚游」的「佚游」指什么？', opts: ['放纵游荡，无所事事', '出门远游', '游泳打猎'], ans: 0, exp: '闲得没边，人就废了'},
  {q: '9. 三种有益的快乐是哪三样？', opts: ['节礼乐、道人之善、多贤友', '骄乐、佚游、宴乐', '读书、写字、算数'], ans: 0, exp: '乐节礼乐，乐道人之善，乐多贤友'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['什么乐子养人，什么乐子耗人', '益者三乐，损者三乐', '乐骄乐，损矣'], ans: 0, exp: '玩完看感觉，感觉最诚实'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi420"></script><script src="../../assets/js/slide-engine.js?v=jishi420"></script>
<script src="../../assets/js/speech.js?v=jishi420"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi420"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi420"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi420"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '420-yi-zhe-san-le')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
