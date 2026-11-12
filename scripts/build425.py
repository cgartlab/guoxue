# -*- coding: utf-8 -*-
"""生成第 425 课《季氏》第十章「君子有九思」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
孔kǒng 子zǐ 曰yuē ： 「 君jūn 子zǐ 有yǒu 九jiǔ 思sī ： ||
视shì 思sī 明míng ， 听tīng 思sī 聪cōng ， 色sè 思sī 温wēn ， ||
貌mào 思sī 恭gōng ， 言yán 思sī 忠zhōng ， 事shì 思sī 敬jìng ， ||
疑yí 思sī 问wèn ， 忿fèn 思sī 难nàn ， 见jiàn 得dé 思sī 义yì 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.2rem'  # 本科原文四行九思，字号行距与 422~424 课一致
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
<meta content="《论语·季氏》第十章精讲：君子有九思。视思明，听思聪，色思温，貌思恭，言思忠，事思敬，疑思问，忿思难，见得思义。孔子说君子在九个地方都要先过一遍心——看、听、脸色、举止、说话、做事、疑惑、发怒、见利。" name="description"/>
<meta content="君子有九思 · 起念之前，先想一想 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第十章精讲：起念之前，先想一想" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/425-jun-zi-you-jiu-si/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/425-jun-zi-you-jiu-si/index.html" rel="canonical"/>
<title>君子有九思 · 起念之前先想一想 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi425" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi425" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">君子有九思</h2><div class="cover-ornament"></div><p class="cover-subtitle">起念之前，先想一想</p><p class="cover-desc">这是<strong>《论语·季氏》第十章</strong>。上一章说肯不肯学，这一章说<strong>做事之前先过一遍心</strong>。孔子点了九处：<strong>看、听、脸色、举止、说话、做事、疑惑、发怒、见利</strong>。九条路，一个理——<strong>别急着来，先想一想</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:8px;">原文呈现</h2><div class="ds-quote" style="margin:10px 0;padding:26px 30px 24px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>孔子说：君子在九个地方都要先想一想：看的时候想看清楚，听的时候想听明白，脸色要想到温和，举止要想到恭敬，说话要想到实在，做事要想到认真，有疑惑要想到问人，发怒要想到后果，见到好处要想到该不该得</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第十章</strong>；<strong>合章本多作 16.10</strong>；<strong>「忿思难」的「难」读 nàn，指后患</strong>；<strong>上一章讲肯不肯学，这一章讲起念前先想一想</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>小记</strong>：<strong>九处都过一遍心，人就少出错</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">思</span>：<strong>先想一想、过一遍心</strong>——<strong>不是空想发呆</strong>。</p><p><span class="ds-highlight">明</span>：<strong>看清楚</strong>——<strong>不是眼力好，是不看花</strong>。</p><p><span class="ds-highlight">聪</span>：<strong>听明白</strong>——<strong>不是耳朵灵，是听全了</strong>。</p><p><span class="ds-highlight">色</span>：<strong>脸色、神情</strong>——<strong>不是颜色，不是女色</strong>。</p><p><span class="ds-highlight">貌</span>：<strong>举止、样子</strong>——<strong>不是长相好看</strong>。</p><p><span class="ds-highlight">忿（fèn）</span>：<strong>生气、动火</strong>——<strong>越气越要先想</strong>。</p><p><span class="ds-highlight">难（nàn）</span>：<strong>后患、后果</strong>——<strong>不是「困难」的难</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>九个「思」，都是先想再做</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：九思是什么</h2><h3>“ 君 子 有 九 思 ”</h3><p style="margin:0"><strong>「思」是空想吗？</strong><br/><br/>① <strong>不是空想，是临事先过一遍心</strong><br/>② <strong>想的都是分寸：够不够、过不过</strong><br/><br/><strong>一句话：思是想分寸，不是发呆。</strong></p><p><strong>为什么正好九条？</strong><br/><br/>① <strong>九处都是人一天里要碰的</strong><br/>② <strong>眼耳脸身，嘴事疑怒，还有一样利</strong><br/><br/><strong>一句话：九处都过关，人就稳当。</strong></p><p><strong>九思是做给谁看的？</strong><br/><br/>① <strong>给自己，不是给别人看</strong><br/>② <strong>不是拘束，是少后悔</strong><br/><br/><strong>一句话：先想一句，省十句解释。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：眼耳脸身</h2><h3>“ 视 思 明 ， 听 思 聪 ， 色 思 温 ， 貌 思 恭 ”</h3><p style="margin:0"><strong>「视思明」是眼力好吗？</strong><br/><br/>① <strong>不是眼力，是不看花、不看半截</strong><br/>② <strong>该看的看全，不该看的别看</strong><br/><br/><strong>一句话：看明白，才算看见。</strong></p><p><strong>「听思聪」是耳朵灵吗？</strong><br/><br/>① <strong>是听全了再答，不抢话</strong><br/>② <strong>只听半句就发火，最容易冤人</strong><br/><br/><strong>一句话：听全了，才叫听见。</strong></p><p><strong>「色温」「貌恭」是装样子吗？</strong><br/><br/>① <strong>温是不过火，恭是不轻慢</strong><br/>② <strong>脸色比话先到，人家先看脸</strong><br/><br/><strong>一句话：脸和样子，先把话说了一半。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：嘴事疑怒</h2><h3>“ 言 思 忠 ， 事 思 敬 ， 疑 思 问 ， 忿 思 难 ”</h3><p style="margin:0"><strong>「言思忠」是什么？</strong><br/><br/>① <strong>说话实在，有交代，不糊弄</strong><br/>② <strong>答应的事，话里就得算数</strong><br/><br/><strong>一句话：话里要有人，不能只有声。</strong></p><p><strong>「事思敬」和「疑思问」呢？</strong><br/><br/>① <strong>做事当回事，不敷衍</strong><br/>② <strong>不懂就问，别硬撑装懂</strong><br/><br/><strong>一句话：事上认真，不懂就问。</strong></p><p><strong>为什么「忿思难」最难？</strong><br/><br/>① <strong>火一上来，脑子就熄了</strong><br/>② <strong>先想后果，火就小了一半</strong><br/><br/><strong>一句话：忍一口气，免一场祸。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：见得思义</h2><h3>“ 见 得 思 义 ”</h3><p style="margin:0"><strong>为什么最后一条压轴？</strong><br/><br/>① <strong>前面八条管日常，这条管关口</strong><br/>② <strong>好处当前，人最容易松</strong><br/><br/><strong>一句话：见利这一步，最见人品。</strong></p><p><strong>「义」是不要好处吗？</strong><br/><br/>① <strong>不是不要，是要问该不该得</strong><br/>② <strong>该得的拿，不该得的一分不取</strong><br/><br/><strong>一句话：拿得心安，才是你的。</strong></p><p><strong>这一章跟上一章什么关系？</strong><br/><br/>① <strong>上一章讲肯学，这一章讲肯想</strong><br/>② <strong>学了不照着做，等于没学</strong><br/><br/><strong>一句话：学到心里，还得落到事上。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看九思</h2><p>这一章说的是起念前先想一想，一层比一层紧——</p><h3>“君子有九思”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>见处：</strong>眼耳脸身先正。</p><p>📜 看明白、听清楚、脸色温和、举止恭敬</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>做处：</strong>嘴事疑怒要稳。</p><p>⏳ 话有交代、事当回事、不懂就问、发火想后果</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>关口：</strong>见得思义最重。</p><p>🤐 好处当前，先问该不该得</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第十章，<strong>承上章讲起念前先想一想</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 九条要一条条背吗？</h3><p><strong>不必死背，抓住一个「慢」字。</strong><br/><br/>① <strong>九条都是先想再做，不是先做再悔</strong><br/>② <strong>想的是分寸，不是瞻前顾后</strong><br/>③ <strong>练熟一条，其余跟着顺</strong><br/><br/><strong>记法：九思不是九条绳，是一个「等一等」。</strong></p><h3>❓ 「色思温」是不是要装笑脸？</h3><p><strong>不是装，是收。</strong><br/><br/>① <strong>温是不过火，不是永远笑</strong><br/>② <strong>该严的时候还得严</strong><br/>③ <strong>怕的是脸色比道理先到</strong><br/><br/><strong>记法：脸色别跑在道理前头。</strong></p><h3>❓ 小孩怎么用九思？</h3><p><strong>从「三思」练起。</strong><br/><br/>① <strong>听人说话，先听完</strong><br/>② <strong>有不懂，当场问</strong><br/>③ <strong>生气时数到十再开口</strong><br/><br/><strong>记法：慢半拍，少后悔。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📜 眼耳脸身：先管看得见的四样</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看明白、听清楚、脸色温和、举止恭敬</strong>；<strong>四样正了，人就稳了</strong>。</p><p>⏳ 嘴、事、疑、怒：管住容易出错的四样</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>话有交代，事当回事，不懂就问，发火先想后果</strong>；<strong>这四样守住，日子少一半麻烦</strong>。</p><p>🤝 见得思义：最后一条最要紧</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看见好处，先问该不该得</strong>；<strong>这一条守住了，前面八条才不白练</strong><br/><br/><strong>本章的落点：起念之前，先想一想。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「君子有九思」。记牢：<strong>起念之前，先想一想。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                视思明，听思聪，色思温，貌思恭，言思忠，事思敬。
            </p><p>回顾本课要点:</p><p>九处 · 眼耳脸身，嘴事疑怒，见利</p><br/><p><strong>都是先过一遍心，再动。</strong></p><p>关口 · 忿思难，见得思义</p><br/><p><strong>火头上、好处前，最见人品。</strong></p><p>一个「慢」字 · 先想再做</p><br/><p><strong>慢半拍，少后悔。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第十章</strong>；与 424 课连读——<strong>那课讲肯学，这课讲肯想</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>疑思问，忿思难，见得思义。</p>
</div><p><strong>课后小挑战:</strong>① 挑一条自己最容易忘的，练三天。② 背一句：见得思义。③ 想一想这周哪件事该先问再答。</p><p><strong>把这一章记在心里:</strong><strong>起念之前，先想一想。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “视思明，听思聪，色思温，貌思恭，言思忠，事思敬！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '425-jun-zi-you-jiu-si';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《阳货》'], ans: 0, exp: '按站内分法，这是《季氏》第十章'},
  {q: '2. 「君子有九思」的「思」是什么意思？', opts: ['先想一想、过一遍心', '空想、发呆', '思念别人'], ans: 0, exp: '思是想分寸，不是发呆'},
  {q: '3. 九思的第一条是什么？', opts: ['视思明', '听思聪', '色思温'], ans: 0, exp: '看明白，才算看见'},
  {q: '4. 「听思聪」的「聪」是什么意思？', opts: ['听得清楚、听全了', '耳朵特别灵', '人很聪明'], ans: 0, exp: '听全了，才叫听见'},
  {q: '5. 「色思温」的「色」指什么？', opts: ['脸色、神情', '颜色深浅', '女色'], ans: 0, exp: '脸和样子，先把话说了一半'},
  {q: '6. 「貌思恭」说的是什么？', opts: ['举止要恭敬', '相貌要好看', '衣服要整齐'], ans: 0, exp: '恭是不轻慢，不是长相'},
  {q: '7. 「疑思问」是什么意思？', opts: ['有疑惑就想到问人', '怀疑别人有坏心', '疑问先放心里'], ans: 0, exp: '不懂就问，别硬撑装懂'},
  {q: '8. 「忿思难」的「难」读什么、什么意思？', opts: ['nàn，指后患、后果', 'nán，指困难', 'nàn，指灾民'], ans: 0, exp: '忍一口气，免一场祸'},
  {q: '9. 九思的最后一条是什么？', opts: ['见得思义', '忿思难', '疑思问'], ans: 0, exp: '好处当前，先问该不该得'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['起念之前，先想一想', '君子有九思', '见得思义'], ans: 0, exp: '慢半拍，少后悔'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi425"></script><script src="../../assets/js/slide-engine.js?v=jishi425"></script>
<script src="../../assets/js/speech.js?v=jishi425"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi425"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi425"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi425"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '425-jun-zi-you-jiu-si')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
