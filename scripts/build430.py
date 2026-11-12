# -*- coding: utf-8 -*-
"""生成第 430 课《阳货》第一章「阳货欲见孔子」课件（阳货篇开篇）。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
阳yáng 货huò 欲yù 见jiàn 孔kǒng 子zǐ ， 孔kǒng 子zǐ 不bù 见jiàn ， 归kuì 孔kǒng 子zǐ 豚tún 。 ||
孔kǒng 子zǐ 时shí 其qí 亡wáng 也yě ， 而ér 往wǎng 拜bài 之zhī ， 遇yù 诸zhū 涂tú 。 ||
谓wèi 孔kǒng 子zǐ 曰yuē ： 「 来lái ！ 予yú 与yǔ 尔ěr 言yán 。 」 ||
曰yuē ： 「 怀huái 其qí 宝bǎo 而ér 迷mí 其qí 邦bāng ， 可kě 谓wèi 仁rén 乎hū ？ 」 曰yuē ： 「 不bù 可kě 。 」 ||
「 好hào 从cóng 事shì 而ér 亟qì 失shī 时shí ， 可kě 谓wèi 知zhì 乎hū ？ 」 曰yuē ： 「 不bù 可kě 。 」 ||
「 日rì 月yuè 逝shì 矣yǐ ， 岁suì 不bù 我wǒ 与yǔ 。 」 ||
孔kǒng 子zǐ 曰yuē ： 「 诺nuò ， 吾wú 将jiāng 仕shì 矣yǐ 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '1.3rem'   # 本科原文七行、约 120 字，字号按 416 课长文标准
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
<meta content="《论语·阳货》第一章精讲：阳货欲见孔子，孔子不见，归孔子豚。孔子时其亡也，而往拜之，遇诸涂。阳货拿话堵他：怀其宝而迷其邦，可谓仁乎？好从事而亟失时，可谓知乎？日月逝矣，岁不我与。孔子只答：诺，吾将仕矣。这一章讲的是躲不开的见面，和一个不硬顶的回答。" name="description"/>
<meta content="阳货欲见孔子 · 躲不开的一场见面 · 国学课堂" property="og:title"/>
<meta content="《论语·阳货》第一章精讲：躲不开的一场见面" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/430-yang-huo-yu-jian-kong-zi/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/430-yang-huo-yu-jian-kong-zi/index.html" rel="canonical"/>
<title>阳货欲见孔子 · 躲不开的一场见面 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=yanghuo430" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=yanghuo430" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">阳货欲见孔子</h2><div class="cover-ornament"></div><p class="cover-subtitle">躲不开的一场见面</p><p class="cover-desc">这是<strong>《论语·阳货》第一章</strong>，新的一篇从这里开始。鲁国掌实权的<strong>阳货</strong>想拉孔子出来做事，孔子不见。阳货<strong>送了一头小猪</strong>——按礼，孔子得上门拜谢。孔子挑他不在家去，结果<strong>在路上撞上了</strong>。阳货拿话堵他，孔子只答四个字：<strong>诺，吾将仕矣</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:14px 22px 12px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>阳货想让孔子来见他，孔子不去，阳货就送孔子一头小猪。孔子趁他不在家的时候去拜谢，在路上撞见了他。阳货对孔子说：过来！我跟你讲。又说：揣着一身本事，眼看国家迷乱不管，这算仁吗？答：不算。喜欢做事，却一次次错过时机，这算聪明吗？答：不算。日子一天天过去，岁月不等人。孔子说：好，我准备出来做事了</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《阳货》第一章</strong>；<strong>合章本作 17.1</strong>；<strong>阳货是鲁国季氏的家臣，当时掌着国政</strong>；<strong>「归」通「馈」，赠送</strong>；<strong>自此进入《阳货》篇</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>话可以接，路自己走</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 八个关节</h2><p><span class="ds-highlight">阳货</span>：<strong>鲁国季氏的家臣，名虎</strong>——<strong>当时掌着实权</strong>。</p><p><span class="ds-highlight">欲见</span>：<strong>想让孔子来见他</strong>——<strong>不是「想见孔子一面」这么随便</strong>。</p><p><span class="ds-highlight">归孔子豚</span>：<strong>「归」通「馈」，赠送</strong>——<strong>豚是小猪</strong>。</p><p><span class="ds-highlight">时其亡也</span>：<strong>趁他不在家</strong>——<strong>「亡」是外出，不是死</strong>。</p><p><span class="ds-highlight">遇诸涂</span>：<strong>在路上撞见了</strong>——<strong>「诸」＝之于，「涂」通「途」</strong>。</p><p><span class="ds-highlight">怀其宝而迷其邦</span>：<strong>揣着本事，眼看国家迷乱不管</strong>。</p><p><span class="ds-highlight">亟失时</span>：<strong>一次次错过时机</strong>——<strong>「亟」读 qì，屡次</strong>。</p><p><span class="ds-highlight">岁不我与</span>：<strong>岁月不等人</strong>——<strong>「与」是等待</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>礼数躲不过，话也躲不过</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：孔子不见</h2><h3>“ 阳 货 欲 见 孔 子 ， 孔 子 不 见 ， 归 孔 子 豚 ”</h3><p style="margin:0"><strong>阳货是什么人？</strong><br/><br/>① <strong>鲁国季氏的家臣，名虎</strong><br/>② <strong>主人管不住他，国政落在他手里</strong><br/><br/><strong>一句话：有权，但名不正。</strong></p><p><strong>孔子为什么不见？</strong><br/><br/>① <strong>不愿跟这种路子的人来往</strong><br/>② <strong>不见，不是怕，是不认</strong><br/><br/><strong>一句话：不认这条路，就不上这道门。</strong></p><p><strong>送小猪是什么意思？</strong><br/><br/>① <strong>当时规矩：大夫送东西给士，士要上门拜谢</strong><br/>② <strong>一头小猪，把孔子堵在礼上</strong><br/><br/><strong>一句话：礼数一到，人就躲不开了。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：遇诸涂</h2><h3>“ 时 其 亡 也 ， 而 往 拜 之 ， 遇 诸 涂 ”</h3><p style="margin:0"><strong>「时其亡也」是算计吗？</strong><br/><br/>① <strong>挑他不在家的时候去</strong><br/>② <strong>礼走到了，人不必见</strong><br/><br/><strong>一句话：礼数照走，面不见。</strong></p><p><strong>为什么还是撞上了？</strong><br/><br/>① <strong>路上正好遇见</strong><br/>② <strong>躲得过家门，躲不过路上</strong><br/><br/><strong>一句话：该来的，绕不开。</strong></p><p><strong>这一遇，孔子慌不慌？</strong><br/><br/>① <strong>没躲，也没顶</strong><br/>② <strong>站住听他把话说完</strong><br/><br/><strong>一句话：见了面，礼还在。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：两问两答</h2><h3>“ 怀 其 宝 而 迷 其 邦 ， 可 谓 仁 乎 ？ …… 可 谓 知 乎 ？ ”</h3><p style="margin:0"><strong>第一问在说什么？</strong><br/><br/>① <strong>揣着一身本事，眼看国家迷乱不管</strong><br/>② <strong>这算仁吗？孔子答：不可</strong><br/><br/><strong>一句话：他不否认这话有道理。</strong></p><p><strong>第二问在说什么？</strong><br/><br/>① <strong>爱做事，却一次次错过时机</strong><br/>② <strong>这算聪明吗？孔子答：不可</strong><br/><br/><strong>一句话：机会错过，也是本事不够。</strong></p><p><strong>孔子为什么不辩？</strong><br/><br/>① <strong>阳货问的是「算不算」，不是「我做不做」</strong><br/>② <strong>答「不可」，是认道理，不是认人</strong><br/><br/><strong>一句话：认理不认人，这就是分寸。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：吾将仕矣</h2><h3>“ 日 月 逝 矣 ， 岁 不 我 与 。 孔 子 曰 ： 诺 ， 吾 将 仕 矣 ”</h3><p style="margin:0"><strong>「岁不我与」是什么意思？</strong><br/><br/>① <strong>岁月不等人</strong><br/>② <strong>这句打动了孔子</strong><br/><br/><strong>一句话：年纪不等人，这话是真的。</strong></p><p><strong>「诺」是什么答应？</strong><br/><br/>① <strong>轻轻一个「诺」，不是发誓</strong><br/>② <strong>只说「我准备出来做事了」</strong><br/><br/><strong>一句话：应了话，没应人。</strong></p><p><strong>孔子后来做官了吗？</strong><br/><br/>① <strong>做过，中都宰、司空、司寇</strong><br/>② <strong>可不是给阳货做，阳货后来也败了</strong><br/><br/><strong>一句话：答应的是做事，不是跟人。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看躲与应</h2><p>这一章一场见面，一层比一层难——</p><h3>“孔子不见……遇诸涂……诺，吾将仕矣”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>躲：</strong>孔子不见。</p><p>🚪 不认这条路，就不进这道门</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>遇：</strong>路上撞上。</p><p>🛣️ 躲得过家门，躲不过路上</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>应：</strong>诺，吾将仕矣。</p><p>🕊️ 认理不认人，话软立场硬</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《阳货》第一章，<strong>新篇开篇，讲一个人怎么在难处里守住分寸</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 阳货到底是个什么人？</h3><p><strong>有本事，也有野心的人。</strong><br/><br/>① <strong>鲁国季氏的家臣，名叫阳虎</strong><br/>② <strong>把主人架空，国政抓在手里</strong><br/>③ <strong>后来失势出逃，客死在外</strong><br/><br/><strong>记法：能人，但不是正路。</strong></p><h3>❓ 孔子答应出来做事，是不是服软了？</h3><p><strong>不是服软，是认理。</strong><br/><br/>① <strong>「岁不我与」这句，孔子认</strong><br/>② <strong>「诺」只说做事，没说跟你做</strong><br/>③ <strong>后来做官，走的是正路，不是阳货的路</strong><br/><br/><strong>记法：话可以接，路自己走。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>学两样本事。</strong><br/><br/>① <strong>不喜欢的人，礼数照样不缺</strong><br/>② <strong>别人说得对的，就认，别因为人不对就全否</strong><br/>③ <strong>答应事情要留分寸，别一口许到底</strong><br/><br/><strong>记法：认理不认人，才不吃亏。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🚪 不想来往的人，礼别失</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>孔子照样上门拜谢</strong>；<strong>人可以远，礼不能丢</strong>。</p><p>🛣️ 躲不过的场面，站直了听</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>路上撞见，他没转身就走</strong>；<strong>把话听完，再答自己的话</strong>。</p><p>🕊️ 认理不认人</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>话对就认，人不对就不跟</strong>；<strong>这是分寸，不是圆滑</strong><br/><br/><strong>本章的落点：话可以接，路自己走。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《阳货》「阳货欲见孔子」。记牢：<strong>话可以接，路自己走。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                日月逝矣，岁不我与。
            </p><p>回顾本课要点:</p><p>躲 · 孔子不见</p><br/><p><strong>不认这条路，就不进这道门。</strong></p><p>遇 · 遇诸涂</p><br/><p><strong>躲得过家门，躲不过路上。</strong></p><p>应 · 诺，吾将仕矣</p><br/><p><strong>认理不认人，话软立场硬。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《阳货》第一章</strong>，<strong>新篇开篇</strong>；承 429 课——<strong>那课讲怎么称人，这课讲怎么处世</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>日月逝矣，岁不我与。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：有没有你不喜欢、却必须客气的人。② 背一句：日月逝矣，岁不我与。</p><p><strong>把这一章记在心里:</strong><strong>认理不认人。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “日月逝矣，岁不我与。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·阳货》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '430-yang-huo-yu-jian-kong-zi';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《阳货》', '《季氏》', '《微子》'], ans: 0, exp: '这是《阳货》第一章，新篇开篇'},
  {q: '2. 阳货是什么人？', opts: ['鲁国季氏的家臣，掌着实权', '鲁国的国君', '孔子的学生'], ans: 0, exp: '名虎，把主人架空，国政抓在手里'},
  {q: '3. 「归孔子豚」的「归」是什么意思？', opts: ['赠送，通「馈」', '归还', '回家'], ans: 0, exp: '豚是小猪'},
  {q: '4. 阳货送小猪的目的是什么？', opts: ['让孔子按礼上门拜谢，好见面', '让孔子养着', '换孔子的书'], ans: 0, exp: '大夫送东西给士，士要上门拜谢'},
  {q: '5. 「时其亡也」是什么意思？', opts: ['趁他不在家', '等他死了以后', '趁天黑的时候'], ans: 0, exp: '「亡」是外出，不是死'},
  {q: '6. 「遇诸涂」的「涂」是什么意思？', opts: ['路上', '泥地', '城门口'], ans: 0, exp: '「涂」通「途」'},
  {q: '7. 「怀其宝而迷其邦」的「宝」指什么？', opts: ['才能、本事', '玉石宝物', '国宝'], ans: 0, exp: '揣着一身本事不管国家'},
  {q: '8. 「岁不我与」是什么意思？', opts: ['岁月不等人', '年成不好', '没人跟我一起'], ans: 0, exp: '「与」是等待'},
  {q: '9. 孔子最后怎么回答阳货？', opts: ['诺，吾将仕矣', '吾不为也', '子言之过矣'], ans: 0, exp: '轻轻一个诺，只说做事，没说跟你做'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['话可以接，路自己走', '日月逝矣', '阳货送小猪'], ans: 0, exp: '认理不认人'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=yanghuo430"></script><script src="../../assets/js/slide-engine.js?v=yanghuo430"></script>
<script src="../../assets/js/speech.js?v=yanghuo430"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=yanghuo430"></script>
<script defer="" src="../../assets/js/auth.js?v=yanghuo430"></script>
<script defer="" src="../../assets/js/api-client.js?v=yanghuo430"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '430-yang-huo-yu-jian-kong-zi')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
