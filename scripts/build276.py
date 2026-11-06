# -*- coding: utf-8 -*-
"""生成第 276 课《颜渊》第一章「颜渊问仁 · 克己复礼」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
颜yán 渊yuān 问wèn 仁rén 。 子zǐ 曰yuē ： 克kè 己jǐ 复fù 礼lǐ 为wéi 仁rén 。 一yī 日rì 克kè 己jǐ 复fù 礼lǐ ， 天tiān 下xià 归guī 仁rén 焉yān 。 为wéi 仁rén 由yóu 己jǐ ， 而ér 由yóu 人rén 乎hū 哉zāi ？
||
颜yán 渊yuān 曰yuē ： 请qǐng 问wèn 其qí 目mù 。 子zǐ 曰yuē ： 非fēi 礼lǐ 勿wù 视shì ， 非fēi 礼lǐ 勿wù 听tīng ， 非fēi 礼lǐ 勿wù 言yán ， 非fēi 礼lǐ 勿wù 动dòng 。
||
颜yán 渊yuān 曰yuē ： 回huí 虽suī 不bù 敏mǐn ， 请qǐng 事shì 斯sī 语yǔ 矣yǐ 。
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

P_STYLES = [
    'padding-top:0.1em;text-align:left;text-indent:0;font-size:1.55rem;line-height:2.9;width:100%;max-width:none',
    'margin:0.7em 0 0.7em;font-size:1.55rem;line-height:2.9;width:100%;max-width:none',
    'margin:0.7em 0 0.7em;font-size:1.55rem;line-height:2.9;width:100%;max-width:none',
]


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
        out.append('<p style="%s">%s</p>' % (P_STYLES[idx], ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="八〇二三老战士" name="author"/>
<meta content="《论语·颜渊》第一章精讲：颜渊问仁，孔子答克己复礼为仁。一日克己复礼，天下归仁焉。为仁由己，而由人乎哉。颜渊再问条目，孔子答非礼勿视、勿听、勿言、勿动。" name="description"/>
<meta content="克己复礼 · 天下归仁 · 国学课堂" property="og:title"/>
<meta content="《论语·颜渊》第一章精讲：颜渊问仁。孔子说「克己复礼为仁」，又说「为仁由己，而由人乎哉」。颜渊追问条目，孔子给四条：非礼勿视，非礼勿听，非礼勿言，非礼勿动。" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/276-yan-yuan-wen-ren/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/276-yan-yuan-wen-ren/index.html" rel="canonical"/>
<title>克己复礼 · 天下归仁 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=xiangdang276" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=xiangdang276" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">克己复礼<br/>天下归仁</h2><div class="cover-ornament"></div><p class="cover-subtitle">仁不在别处，在自己身上</p><p class="cover-desc">这是<strong>《论语·颜渊》第一章</strong>，也是<strong>讲“仁”最实在的一章</strong>。<strong>颜渊问什么是仁</strong>，孔子只答六个字：<strong>克己复礼为仁</strong>。<strong>又补一句：为仁由己，而由人乎哉</strong>。<strong>颜渊追问具体条目，孔子给了四条：非礼勿视，非礼勿听，非礼勿言，非礼勿动</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:12px;">原文呈现</h2><div class="ds-quote" style="margin:18px 0;padding:26px 32px 22px;line-height:1.85;">
__RUBY__
</div><p style="font-size:0.88rem;line-height:1.6;width:100%;max-width:none;margin-top:var(--ds-space-2)"><strong>通译</strong>：<strong>颜渊问什么是仁</strong>。<strong>孔子说：管住自己，回到礼上，这就是仁</strong>。<strong>一旦做到了，天下都归到仁上</strong>。<strong>行仁靠自己，难道靠别人</strong>？<strong>颜渊说：请问具体条目</strong>。<strong>孔子说：不合礼的不看、不听、不说、不动</strong>。<strong>颜渊说：我虽不聪明，就照这几句话去做</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">克（kè）己</span>：<strong>约束自己</strong>——<strong>克，是管住，不是硬压</strong>。</p><p><span class="ds-highlight">复（fù）礼</span>：<strong>回到礼上</strong>——<strong>复，返回；礼，分寸规矩</strong>。</p><p><span class="ds-highlight">天下归仁</span>：<strong>天下都归到仁上</strong>——<strong>一说天下人称许你仁，一说天下人心归向仁，都通</strong>。</p><p><span class="ds-highlight">目</span>：<strong>条目、细则</strong>——<strong>“请问其目”＝请讲讲具体哪几条</strong>。</p><p><span class="ds-highlight">四勿</span>：<strong>勿＝不要</strong>——<strong>视、听、言、动，四道关口</strong>。</p><p><span class="ds-highlight">不敏 · 请事斯语</span>：<strong>不聪明；请照着这话去做</strong>——<strong>敏，聪敏；事，从事、实行</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>“克己”是管住自己，“复礼”是回到分寸——仁就从这一管一回里来</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：克己复礼为仁</h2><h3>“ 什 么 是 仁 ”</h3><p style="margin:0"><strong>颜渊问的是最大的题目。</strong><br/><br/>① <strong>颜渊是孔子最得意的学生</strong>——<strong>他问的“仁”，是孔门全部学问的总纲</strong><br/>② <strong>孔子没讲大道理</strong>——<strong>只给六个字：克己复礼为仁</strong><br/>③ <strong>克己是管住自己</strong>——<strong>复礼是回到规矩上</strong><br/><br/><strong>一句话：仁不是天生的好心肠，是管出来的。</strong></p><p><strong>这两个字，一里一外。</strong><br/><br/>① <strong>克己是里子</strong>——<strong>脾气、欲望、那张要抢话的嘴</strong><br/>② <strong>复礼是面子</strong>——<strong>该在什么位置，说什么话，办什么事</strong><br/>③ <strong>只管自己不管礼</strong>——<strong>容易变成自我感动</strong><br/><br/><strong>一句话：心里管得住，行动合得上，才叫仁。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>想改脾气</strong>——<strong>不是等心情好了再说，是先管住那一句要冲出口的话</strong><br/>② <strong>遇到不讲理的人</strong>——<strong>先管住自己的脸，再讲道理</strong><br/><br/><strong>一句话：管住自己那一分，比要求别人那一分有用。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：一日克己复礼</h2><h3>“ 就 从 这 一 天 算 起 ”</h3><p style="margin:0"><strong>“一日”两个字最要紧。</strong><br/><br/>① <strong>不是“一辈子”</strong>——<strong>孔子没让你许大愿</strong><br/>② <strong>是“一旦做到”</strong>——<strong>真做到的那一天</strong><br/>③ <strong>这一天，人人都有</strong>——<strong>难的是天天都有</strong><br/><br/><strong>一句话：大道不远，就在今天这一天里。</strong></p><p><strong>“天下归仁”怎么讲？</strong><br/><br/>① <strong>一说天下人都称许你是仁人</strong>——<strong>你的分量，别人看得见</strong><br/>② <strong>一说天下人心都归向仁</strong>——<strong>一人做好，带起一片</strong><br/>③ <strong>两种讲法都通</strong>——<strong>孔子要说的都是：先从你这一分起</strong><br/><br/><strong>一句话：别等天下先变好，先把自己这一分做正。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>别定“以后我要做个好人”</strong>——<strong>这种话十年也落不了地</strong><br/>② <strong>定“今天不说一句刻薄话”</strong>——<strong>晚上就能验收</strong><br/><br/><strong>一句话：把一辈子的事，拆成一天的事。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：为仁由己</h2><h3>“ 这 事 全 在 自 己 ”</h3><p style="margin:0"><strong>这一句是全章的骨头。</strong><br/><br/>① <strong>“为仁由己”</strong>——<strong>做不做，全在自己</strong><br/>② <strong>“而由人乎哉”</strong>——<strong>难道靠别人</strong><br/>③ <strong>孔子把责任一句话放回颜渊手里</strong><br/><br/><strong>一句话：仁这件事，没有谁能替你，也没有谁能拦你。</strong></p><p><strong>为什么单说这一句？</strong><br/><br/>① <strong>人最爱找理由</strong>——<strong>环境不好、没人带我、别人先不仁</strong><br/>② <strong>孔子把理由一条条堵住</strong>——<strong>仁在你身上，不在别人身上</strong><br/>③ <strong>这不是苛求</strong>——<strong>这是把最大的自由交给你</strong><br/><br/><strong>一句话：能怪别人的事，都不是仁的事。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>凡是“我做不到，是因为……”</strong>——<strong>先停一下，多半是自己不肯</strong><br/>② <strong>凡是“等他们先改”</strong>——<strong>那就是把日子交给了别人</strong><br/><br/><strong>一句话：自己这一关过了，别人才拦不住你。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：请问其目</h2><h3>“ 四 道 关 口 ”</h3><p style="margin:0"><strong>颜渊不满足于大道理。</strong><br/><br/>① <strong>“请问其目”</strong>——<strong>请讲讲具体哪几条</strong><br/>② <strong>这是好学生的问法</strong>——<strong>大道理听懂了，还要问到能下手的地方</strong><br/>③ <strong>孔子也真给了四条</strong>——<strong>不含糊，不打太极</strong><br/><br/><strong>一句话：问到大道理落了地，才算真问。</strong></p><p><strong>四勿的顺序有讲究。</strong><br/><br/>① <strong>先管眼睛</strong>——<strong>非礼勿视，看见什么最要紧</strong><br/>② <strong>再管耳朵</strong>——<strong>非礼勿听，闲话少进耳朵</strong><br/>③ <strong>然后才是嘴和身子</strong>——<strong>非礼勿言，非礼勿动</strong><br/><br/><strong>一句话：眼耳是入口，口身是出口，先堵入口。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>手机里那些不该看的</strong>——<strong>先不看，比后来忍住容易十倍</strong><br/>② <strong>别人递过来的闲话</strong>——<strong>不听，就没得传</strong><br/><br/><strong>一句话：管住入口，出口自然就干净。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 仁由己出</h2><p>本章四层意思——</p><h3>“克己复礼为仁。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>仁是管出来的。</strong>心里管得住，行动合得上规矩。</p><p>📖 “一日克己复礼，天下归仁焉。”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>从今天这一天算起。</strong>把一辈子的事，拆成一天的事。</p><p>🧭 “为仁由己，而由人乎哉？”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>责任在自己手里。</strong>能怪别人的事，都不是仁的事。</p><p>🎯 “非礼勿视，非礼勿听，非礼勿言，非礼勿动。”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>四道关口，先堵入口。</strong>眼耳是入口，口身是出口。</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>一条理：</strong>仁不在天上，也不在别人身上，就在自己这一管一回里。<strong>位置：</strong>《颜渊》首章，讲仁最实在的一章。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ “克己”是不是要委屈自己、什么都忍着？</h3><p><strong>不是忍，是管。</strong><br/><br/>① <strong>克是约束</strong>——<strong>不是把自己压死</strong><br/>② <strong>复礼是回到分寸</strong>——<strong>不是回到拘束里</strong><br/>③ <strong>孔子后面给的四勿</strong>——<strong>管的是四道具体关口，不是把人管死</strong><br/><br/><strong>记法：管住的是那一下冲动，不是你的性情。</strong></p><h3>❓ “天下归仁”是说天下人都变好了吗？</h3><p><strong>两说都通，重点不在这。</strong><br/><br/>① <strong>一说：天下人都称许你是仁人</strong>——<strong>你的分量，别人看得见</strong><br/>② <strong>一说：天下人心都归向仁</strong>——<strong>一人做好，能带起一片</strong><br/>③ <strong>孔子真正要说的</strong>——<strong>这事从你一个人做起，不靠天下先变好</strong><br/><br/><strong>记法：先把自己这一分做好，天下那一分不归你管。</strong></p><h3>❓ 这一章在《论语》里是什么位置？</h3><p><strong>《颜渊》首章，也是讲仁最实在的一章。</strong><br/><br/>① <strong>上一篇《先进》</strong>——<strong>讲的是孔门弟子各人的性情长短</strong><br/>② <strong>这一篇开头</strong>——<strong>颜渊问仁、仲弓问仁、司马牛问仁，一路问下去</strong><br/>③ <strong>“己所不欲，勿施于人”</strong>——<strong>也在这一篇里，和这一章是一路的</strong><br/><br/><strong>记法：《颜渊》开篇就立规矩——仁从管住自己开始。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>💧 管住第一下</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“克己复礼为仁”</strong>——<strong>克己不是叫你没脾气，是脾气上来那一下管得住</strong>。<strong>那一下管住了，后面都省事；那一下没管住，后面全是赔不是</strong>。</p><p>⚖️ 别把责任推给环境</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“为仁由己，而由人乎哉”</strong>——<strong>孔子把话说到最硬：这事不靠别人</strong>。<strong>“等他们先改”，就是把日子交到别人手里</strong>。</p><p>📖 从今天这一天算起</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“一日克己复礼，天下归仁焉”</strong>——<strong>不用等一辈子才叫做到</strong>。<strong>今天这一天做到了，就是做到了</strong>。<strong>四勿也不必全做到，先守一道：不该看的先不看</strong>。<br/><br/><strong>本章的落点：管住自己这一分，日子就顺了八分。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天我们一起学习了《论语·颜渊》篇的第一章——颜渊问仁，孔子答“克己复礼为仁”，又答“为仁由己”，最后给出四勿。<strong>这是《论语》里讲“仁”最实在、最能下手的一章。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                克己复礼为仁。
            </p><p>回顾本课要点:</p><p>克己复礼为仁</p><br/><p><strong>仁是管出来的。</strong>心里管得住，行动合得上规矩</p><p>一日克己复礼，天下归仁焉</p><br/><p><strong>从今天这一天算起。</strong>把一辈子的事，拆成一天的事</p><p>为仁由己，而由人乎哉</p><br/><p><strong>责任在自己手里。</strong>能怪别人的事，都不是仁的事</p><p>非礼勿视，非礼勿听，非礼勿言，非礼勿动</p><br/><p><strong>四道关口，先堵入口。</strong>眼耳是入口，口身是出口</p><p><strong>在全篇中的位置:</strong>这是<strong>《颜渊》首章</strong>。上一篇《先进》讲孔门弟子各人的性情长短，<strong>这一篇一开头就问仁——仁怎么下手，孔子给了最实在的答法</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>为仁由己，而由人乎哉？</p>
</div><p><strong>课后小挑战:</strong>① 想一想：你最容易在哪一道关口上失守——眼、耳、口，还是身？② 学一句实在话：这一下我管住。③ 讲给家人听：<strong>孔子为什么说“为仁由己”</strong>？</p><p><strong>把这一章记在心里:</strong><strong>管住自己这一分，日子就顺了八分。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “为仁由己，而由人乎哉？”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·颜渊》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '276-yan-yuan-wen-ren';
const QUIZ = [
  {q: '1. “颜渊问仁”中的颜渊，是孔子的什么人？', opts: ['孔子最得意的学生', '孔子的儿子', '鲁国的国君'], ans: 0, exp: '颜渊名回，字子渊，是孔子最得意的学生。他问的“仁”，是孔门全部学问的总纲'},
  {q: '2. “克己复礼为仁”中的“克”是什么意思？', opts: ['战胜敌人', '约束、克制', '能够'], ans: 1, exp: '克是约束、管住。克己是管住自己的脾气欲望，不是硬压，也不是把自己委屈死'},
  {q: '3. “复礼”的“复”是什么意思？', opts: ['重复', '返回、回到', '报复'], ans: 1, exp: '复是返回。复礼就是回到礼上——该在什么位置、说什么话、办什么事，都有分寸'},
  {q: '4. “一日克己复礼，天下归仁焉”的“一日”强调什么？', opts: ['只做一天就够了', '一旦做到的那一天，就从今天算起', '日子过得太快'], ans: 1, exp: '孔子不许你许大愿，只跟你算今天这一天。把一辈子的事，拆成一天的事'},
  {q: '5. “为仁由己，而由人乎哉”是什么意思？', opts: ['行仁要靠自己，不能靠别人', '行仁要别人带着做', '行仁要看出身门第'], ans: 0, exp: '这是全章的骨头：做不做，全在自己。孔子把责任一句话放回颜渊手里'},
  {q: '6. 颜渊说“请问其目”，“目”是什么意思？', opts: ['眼睛', '条目、细则', '目标'], ans: 1, exp: '目在这里是条目、细则。“请问其目”＝请讲讲具体哪几条。这是好学生的问法'},
  {q: '7. 孔子答的“四勿”，不包括下面哪一项？', opts: ['非礼勿视', '非礼勿思', '非礼勿动'], ans: 1, exp: '四勿是非礼勿视、非礼勿听、非礼勿言、非礼勿动。管的是眼、耳、口、身四道关口'},
  {q: '8. 四勿的次序，头一道关口管的是哪里？', opts: ['眼睛（视）', '嘴巴（言）', '身体（动）'], ans: 0, exp: '先管眼睛：非礼勿视。眼耳是入口，口身是出口，孔子让你先堵入口'},
  {q: '9. “回虽不敏”中的“敏”是什么意思？', opts: ['勤快', '聪敏、聪明', '敏捷地跑'], ans: 1, exp: '敏是聪敏。“不敏”是谦辞，颜渊说自己不聪明——可他是孔门最聪明的学生'},
  {q: '10. “请事斯语矣”中的“事”是什么意思？', opts: ['事情', '从事、实行', '侍奉'], ans: 1, exp: '事是从事、实行。颜渊这句话的意思是：我虽不聪明，就照这几句话去做'}
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=xiangdang276"></script><script src="../../assets/js/slide-engine.js?v=xiangdang276"></script>
<script src="../../assets/js/speech.js?v=xiangdang276"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
</div>
<script defer="" src="../../assets/js/auth-email.js?v=xiangdang276"></script>
<script defer="" src="../../assets/js/auth.js?v=xiangdang276"></script>
<script defer="" src="../../assets/js/api-client.js?v=xiangdang276"></script>
</body>
</html>
'''

out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lessons', '276-yan-yuan-wen-ren')
os.makedirs(out_dir, exist_ok=True)
html = TEMPLATE.replace('__RUBY__', build_ruby_paragraphs())
with io.open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('written:', os.path.join(out_dir, 'index.html'))
print('chars:', len(html))
