# -*- coding: utf-8 -*-
"""生成第 470 课《子张》第九章「君子信而后劳其民」课件。
全章约 31 字、五段；短章大字版式（与 467/468/469 同结构）。
"""
import io
import os
import re

PY = """
子zǐ 夏xià 曰yuē ： ||
君jūn 子zǐ 信xìn 而ér 后hòu 劳láo 其qí 民mín ； ||
未wèi 信xìn ， 则zé 以yǐ 为wéi 厉lì 己jǐ 也yě 。 ||
信xìn 而ér 后hòu 谏jiàn ； ||
未wèi 信xìn ， 则zé 以yǐ 为wéi 谤bàng 己jǐ 也yě 。 ||
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
<meta content="《论语·子张》第九章精讲：子夏曰：君子信而后劳其民；未信，则以为厉己也。信而后谏；未信，则以为谤己也。要先取得信任，再派活、再劝谏；没取得信任就动手，人家以为你在坑他、在毁他。「厉」在这里是折磨，「谏」是下级劝上级。" name="description"/>
<meta content="信而后劳其民 · 先让人信你，再让人听你 · 国学课堂" property="og:title"/>
<meta content="《论语·子张》第九章精讲：先立信，再开口" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/470-xin-er-hou-lao-qi-min/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/470-xin-er-hou-lao-qi-min/index.html" rel="canonical"/>
<title>信而后劳其民 · 先让人信你，再让人听你 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=zhangz470" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=zhangz470" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">信而后劳其民</h2><div class="cover-ornament"></div><p class="cover-subtitle">先让人信你，再让人听你</p><p class="cover-desc">这是<strong>《论语·子张》第九章</strong>。<strong>子夏</strong>说：<strong>要先取得信任，再去派活</strong>；<strong>没取得信任就派活，人家以为你在坑他</strong>。<strong>要先取得信任，再去劝谏</strong>；<strong>没取得信任就劝谏，人家以为你在毁他</strong>。<strong>先立信，再开口——这是办事的次序。</strong></p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:18px 16px 14px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>子夏说：君子先取得信任，再役使百姓；没取得信任就役使，百姓以为你在折磨他。先取得信任，再去劝谏；没取得信任就劝谏，人家以为你在毁谤他。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《子张》第九章</strong>；<strong>合章本作 19.10</strong>；<strong>「厉」在这里是折磨，不是严厉</strong>；<strong>「谏」读 jiàn，下级劝上级</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>信没立住，好心也成坏心。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">信</span>：<strong>让人信得过</strong>——<strong>不是写信，是信用</strong>。</p><p><span class="ds-highlight">劳其民</span>：<strong>劳 是役使、派活</strong>——<strong>不是自己受累</strong>。</p><p><span class="ds-highlight">未信</span>：<strong>还没让人信你</strong>——<strong>四个字是全章的关键</strong>。</p><p><span class="ds-highlight">厉己</span>：<strong>厉 是折磨、坑害</strong>——<strong>和 469 课的「厉」不是一个意思</strong>。</p><p><span class="ds-highlight">谏</span>：<strong>谏 读 jiàn，下级劝上级</strong>——<strong>话不好听，得有底气</strong>。</p><p><span class="ds-highlight">谤</span>：<strong>谤 读 bàng，毁谤、说坏话</strong>——<strong>同一句劝，被当成坏话</strong>。</p><p><span class="ds-highlight">而后</span>：<strong>先……然后才……</strong>——<strong>次序不能倒过来</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>信在前，事在后；次序一倒，全是错。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：信而后劳其民</h2><h3>“ 信 而 后 劳 其 民 ”</h3><p style="margin:0"><strong>为什么先要「信」？</strong><br/><br/>① <strong>信是人心里的底，没底就疑</strong><br/>② <strong>你说一句话，他先掂量你有几分真</strong><br/><br/><strong>一句话：信没立住，话就轻。</strong></p><p><strong>「劳其民」劳的是什么？</strong><br/><br/>① <strong>派活、出工、服役</strong><br/>② <strong>不是叫百姓白受累</strong><br/><br/><strong>一句话：劳是办事，不是坑人。</strong></p><p><strong>「而后」两个字重在哪？</strong><br/><br/>① <strong>重次序——先信，再劳</strong><br/>② <strong>倒过来，好事也办成坏事</strong><br/><br/><strong>一句话：不是不做，是先做哪一样。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：未信则以为厉己也</h2><h3>“ 未 信 ， 则 以 为 厉 己 也 ”</h3><p style="margin:0"><strong>「厉己」是怎么个厉法？</strong><br/><br/>① <strong>厉 是折磨、是坑</strong><br/>② <strong>百姓以为你在害他，不是派活</strong><br/><br/><strong>一句话：同一样活，看谁派的。</strong></p><p><strong>为什么没信就变味？</strong><br/><br/>① <strong>不知道你的心，只好往坏处想</strong><br/>② <strong>你越卖力，他越当你图什么</strong><br/><br/><strong>一句话：心里的底没有，好心也像算计。</strong></p><p><strong>这和 469 课的「厉」一样吗？</strong><br/><br/>① <strong>不一样——469 是话有分量，这里是折磨</strong><br/>② <strong>同一个字，两处读法不一样</strong><br/><br/><strong>一句话：看字看上下文，别死记。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：信而后谏</h2><h3>“ 信 而 后 谏 ； 未 信 ， 谤 己 也 ”</h3><p style="margin:0"><strong>「谏」是劝谁？</strong><br/><br/>① <strong>下劝上，臣劝君</strong><br/>② <strong>话说得直，风险也大</strong><br/><br/><strong>一句话：谏是硬话，得有人信你才敢说。</strong></p><p><strong>「谤」和「谏」差在哪里？</strong><br/><br/>① <strong>谏 是好话，谤 是坏话</strong><br/>② <strong>同一句，看听的人怎么想</strong><br/><br/><strong>一句话：不是话变了，是人心变了。</strong></p><p><strong>信为什么这么要紧？</strong><br/><br/>① <strong>信是通行证，没它寸步难行</strong><br/>② <strong>有了信，直话才有人受</strong><br/><br/><strong>一句话：先做人，再说话。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：整章连起来读</h2><h3>“ 君 子 信 而 后 劳 其 民 ”</h3><p style="margin:0"><strong>一句话讲什么？</strong><br/><br/>① <strong>办事有次序：先立信，再动手</strong><br/>② <strong>派活是这样，劝人也是这样</strong><br/><br/><strong>一句话：信是根，事和话是枝叶。</strong></p><p><strong>和 469 课怎么呼应？</strong><br/><br/>① <strong>469 讲君子的三副模样</strong><br/>② <strong>这章讲君子办事的次序</strong><br/><br/><strong>一句话：先有那副样子，才有那份信任。</strong></p><p><strong>整章记一句什么？</strong><br/><br/>① <strong>信立不住，好事也办成坏事</strong><br/>② <strong>先让人信你，再让人听你</strong><br/><br/><strong>一句话：信在前，话在后。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「信」</h2><p>一句话，三层意思——</p><h3>“信在前，事在后；次序一倒，全是错。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>信而后劳——先让人信你，再派活。</p><p>🏛 信是底</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>未信则厉己——没信就动手，人家以为你坑他。</p><p>🔥 疑心最伤人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>信而后谏——信立住了，直话才有人受。</p><p>⚖ 落点是「先做人，再说话」</p>
<p>接 469 课：<strong>上一章讲君子的三副模样，这一章讲君子办事的次序</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「厉」是严厉吗？</h3><p><strong>这里不是。这里的「厉」是折磨、是坑。</strong><br/><br/>① <strong>「以为厉己」＝以为你在害他</strong><br/>② <strong>469 课的「厉」是话有分量，两处不一样</strong><br/>③ <strong>同一个字，得看上下文</strong><br/><br/><strong>记法：这章的厉，是让人难受的厉。</strong></p><h3>❓ 为什么先信才能开口？</h3><p><strong>因为人心先认人，再认话。</strong><br/><br/>① <strong>信你的人，直话也听得进</strong><br/>② <strong>不信你的人，好话也当坏话</strong><br/>③ <strong>同样一句，落在不同的心上，两样结果</strong><br/><br/><strong>记法：先做人，再说话。</strong></p><h3>❓ 这话今天还用得上吗？</h3><p><strong>天天用得上。</strong><br/><br/>① <strong>当老师的、当班干部的，先让学生信你</strong><br/>② <strong>刚到一个新地方，别急着提意见</strong><br/>③ <strong>先做几件靠得住的事，再开口</strong><br/><br/><strong>记法：把信攒够了，话才有分量。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🏛 先立信</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>答应的事，一件一件做到</strong>；<strong>信是靠一件件小事攒出来的</strong>。</p><p>🔥 别急着劝人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>人家还没信你，话说得越直越招嫌</strong>；<strong>先陪他走一段，再说重话</strong>。</p><p>⚖ 次序不能倒</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>先信，后劳；先信，后谏</strong>；<strong>倒过来，好心也成坏心</strong><br/><br/><strong>本章的落点：先让人信你，再让人听你。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「信而后劳其民」。记牢：<strong>信在前，事在后；次序一倒，全是错。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                君子信而后劳其民；未信，则以为厉己也。信而后谏；未信，则以为谤己也。
            </p><p>回顾本课要点:</p><p>信而后劳 · 先信再派活</p><br/><p><strong>信没立住，话就轻。</strong></p><p>未信则厉己 · 疑心最伤人</p><br/><p><strong>同一样活，看谁派的。</strong></p><p>信而后谏 · 先做人再说话</p><br/><strong>不是话变了，是人心变了。</strong><p><strong>在全篇中的位置:</strong>这是<strong>《子张》第九章</strong>。接 469 课：上一章讲君子的三副模样，这一章讲君子办事的次序。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>君子信而后劳其民；未信，则以为厉己也。信而后谏；未信，则以为谤己也。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：你身边谁最让人信得过？他做对了什么。② 背一句：信而后劳其民，信而后谏。</p><p><strong>把这一章记在心里:</strong><strong>先让人信你，再让人听你。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “君子信而后劳其民；未信，则以为厉己也。信而后谏；未信，则以为谤己也。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·子张》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '470-xin-er-hou-lao-qi-min';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《子张》', '《子路》', '《阳货》'], ans: 0, exp: '这是《子张》第九章，子夏的话'},
  {q: '2. 「劳其民」的「劳」是什么意思？', opts: ['役使、派活', '自己劳累', '慰问'], ans: 0, exp: '劳是役使百姓出工办事，不是自己受累'},
  {q: '3. 「未信，则以为厉己也」的「厉」是什么意思？', opts: ['折磨、坑害', '严厉、有分量', '厉害、本事大'], ans: 0, exp: '这里的厉是折磨，百姓以为你在害他'},
  {q: '4. 「信而后谏」的「谏」是劝谁？', opts: ['下级劝上级', '上级训下级', '平辈互相商量'], ans: 0, exp: '谏读 jiàn，是下劝上、臣劝君'},
  {q: '5. 「则以为谤己也」的「谤」是什么意思？', opts: ['毁谤、说坏话', '帮忙、夸赞', '报告、上报'], ans: 0, exp: '谤读 bàng，把好话听成坏话'},
  {q: '6. 子夏认为派活之前先要做到什么？', opts: ['先取得信任', '先立好规矩', '先给足好处'], ans: 0, exp: '信而后劳其民——信没立住，话就轻'},
  {q: '7. 没取得信任就劝谏，对方会怎么想？', opts: ['以为你在毁谤他', '以为你在夸他', '以为你在请示'], ans: 0, exp: '未信则以为谤己——同一句劝，被当成坏话'},
  {q: '8. 本章的「厉」与 469 课的「厉」有何不同？', opts: ['469 是话有分量，本章是折磨', '两处完全一样', '本章是严厉，469 是折磨'], ans: 0, exp: '同一个字，两处读法不一样，要看上下文'},
  {q: '9. 本章讲的中心是什么？', opts: ['办事有次序：先立信，再开口', '怎么管人最省力', '劝人要看脸色'], ans: 0, exp: '信是根，事和话是枝叶'},
  {q: '10. 这一章给我们的提醒是？', opts: ['先让人信你，再让人听你', '话越直越好', '先立规矩再谈交情'], ans: 0, exp: '信在前，事在后；次序一倒，全是错'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=zhangz470"></script><script src="../../assets/js/slide-engine.js?v=zhangz470"></script>
<script src="../../assets/js/speech.js?v=zhangz470"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=zhangz470"></script>
<script defer="" src="../../assets/js/auth.js?v=zhangz470"></script>
<script defer="" src="../../assets/js/api-client.js?v=zhangz470"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '470-xin-er-hou-lao-qi-min')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
