# -*- coding: utf-8 -*-
"""生成第 277 课《颜渊》第二章「仲弓问仁 · 己所不欲勿施于人」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
仲zhòng 弓gōng 问wèn 仁rén 。 子zǐ 曰yuē ： 出chū 门mén 如rú 见jiàn 大dà 宾bīn ， 使shǐ 民mín 如rú 承chéng 大dà 祭jì 。
||
己jǐ 所suǒ 不bù 欲yù ， 勿wù 施shī 于yú 人rén 。 在zài 邦bāng 无wú 怨yuàn ， 在zài 家jiā 无wú 怨yuàn 。
||
仲zhòng 弓gōng 曰yuē ： 雍yōng 虽suī 不bù 敏mǐn ， 请qǐng 事shì 斯sī 语yǔ 矣yǐ 。
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

P_STYLES = [
    'padding-top:0.1em;text-align:left;text-indent:0;font-size:1.7rem;line-height:3;width:100%;max-width:none',
    'margin:0.7em 0 0.7em;font-size:1.7rem;line-height:3;width:100%;max-width:none',
    'margin:0.7em 0 0.7em;font-size:1.7rem;line-height:3;width:100%;max-width:none',
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
<meta content="《论语·颜渊》第二章精讲：仲弓问仁。孔子答出门如见大宾，使民如承大祭；己所不欲，勿施于人；在邦无怨，在家无怨。仲弓说：雍虽不敏，请事斯语矣。" name="description"/>
<meta content="出门如见大宾 · 己所不欲勿施于人 · 国学课堂" property="og:title"/>
<meta content="《论语·颜渊》第二章精讲：仲弓问仁。孔子给了三句话：出门如见大宾，使民如承大祭；己所不欲，勿施于人；在邦无怨，在家无怨。一句敬，一句慎，一句恕。" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/277-zhong-gong-wen-ren/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/277-zhong-gong-wen-ren/index.html" rel="canonical"/>
<title>出门如见大宾 · 己所不欲勿施于人 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=xiangdang277" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=xiangdang277" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">出门如见大宾<br/>己所不欲勿施于人</h2><div class="cover-ornament"></div><p class="cover-subtitle">敬一分，慎一分，恕一分</p><p class="cover-desc">这是<strong>《论语·颜渊》第二章</strong>。<strong>仲弓问仁</strong>，孔子没说大道理，只给了三句话：<strong>出门如见大宾，使民如承大祭</strong>；<strong>己所不欲，勿施于人</strong>；<strong>在邦无怨，在家无怨</strong>。<strong>一句讲敬，一句讲慎，一句讲恕</strong>。<strong>仲弓答的和上一章颜渊一模一样：雍虽不敏，请事斯语矣</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:12px;">原文呈现</h2><div class="ds-quote" style="margin:18px 0;padding:28px 34px 24px;line-height:1.85;">
__RUBY__
</div><p style="font-size:0.9rem;line-height:1.6;width:100%;max-width:none;margin-top:var(--ds-space-2)"><strong>通译</strong>：<strong>仲弓问什么是仁</strong>。<strong>孔子说：出门办事像接见贵宾一样恭敬，役使百姓像承办大祭一样慎重</strong>。<strong>自己不愿意的，不要加给别人</strong>。<strong>在诸侯之国做事没有怨恨，在卿大夫之家做事也没有怨恨</strong>。<strong>仲弓说：我虽不聪明，就照这几句话去做</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">大宾</span>：<strong>贵宾</strong>——<strong>诸侯朝聘往来之宾，最郑重的那一等客人</strong>。</p><p><span class="ds-highlight">承（chéng）大祭</span>：<strong>承办大祭祀</strong>——<strong>承，承当；祭天地祖先，一步都错不得</strong>。</p><p><span class="ds-highlight">己所不欲，勿施于人</span>：<strong>自己不愿的，别加给别人</strong>——<strong>这是“恕”的标准一句话</strong>。</p><p><span class="ds-highlight">邦 · 家</span>：<strong>诸侯之国 · 卿大夫之家</strong>——<strong>在邦＝在朝廷做事，在家＝在采邑做事</strong>。</p><p><span class="ds-highlight">无怨</span>：<strong>没有怨气</strong>——<strong>不怨上头不用我，也不怨下头不听话</strong>。</p><p><span class="ds-highlight">雍 · 不敏</span>：<strong>仲弓的名字；不聪明</strong>——<strong>冉雍，字仲弓；不敏是谦辞</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>敬在脸上，慎在手上，恕在心里——三样齐了，才叫仁</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：出门如见大宾</h2><h3>“ 敬 字 当 头 ”</h3><p style="margin:0"><strong>出门不是出门散步。</strong><br/><br/>① <strong>是出去办事、见人</strong>——<strong>见的是谁，都当贵宾待</strong><br/>② <strong>见大宾有个样子</strong>——<strong>衣裳整、说话慢、眼睛看着人</strong><br/>③ <strong>这份郑重不花钱</strong>——<strong>只看你肯不肯拿出来</strong><br/><br/><strong>一句话：敬，是先把人当人看。</strong></p><p><strong>“使民如承大祭”，重在慎。</strong><br/><br/>① <strong>承大祭</strong>——<strong>祭天地祖先，一步错不得</strong><br/>② <strong>使民</strong>——<strong>派人干活、摊派差事、动人家的力气</strong><br/>③ <strong>把这两件事放在一起</strong>——<strong>用人的时候，心里要有敬畏</strong><br/><br/><strong>一句话：手里有别人的力气，就得当大事办。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>见谁都当贵宾待</strong>——<strong>不论对方有没有用</strong><br/>② <strong>托人办事当大事办</strong>——<strong>别一句“你顺手帮我弄一下”就打发了</strong><br/><br/><strong>一句话：恭敬和慎重，是最省钱的教养。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：己所不欲</h2><h3>“ 拿 自 己 当 尺 子 ”</h3><p style="margin:0"><strong>全章最出名的一句。</strong><br/><br/>① <strong>“己所不欲”</strong>——<strong>自己不愿意受的那一份</strong><br/>② <strong>“勿施于人”</strong>——<strong>别加到别人身上</strong><br/>③ <strong>子贡问：有一言而可以终身行之者乎</strong>——<strong>孔子答的，就是这一句</strong><br/><br/><strong>一句话：这一条，够行一辈子。</strong></p><p><strong>它高明在不用猜别人心思。</strong><br/><br/>① <strong>你不知道别人喜欢什么</strong>——<strong>这很正常</strong><br/>② <strong>但你一定知道自己不愿什么</strong>——<strong>挨骂、被敷衍、被当众难堪</strong><br/>③ <strong>尺子在自己身上</strong>——<strong>谁也赖不掉</strong><br/><br/><strong>一句话：将心比心不是猜心，是拿自己比。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>一句刺人的话要说出口</strong>——<strong>先想自己听着什么滋味</strong><br/>② <strong>要催人办事</strong>——<strong>先想自己被这样催烦不烦</strong><br/><br/><strong>一句话：不想受的那一下，先别给人。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：在邦无怨</h2><h3>“ 两 处 都 没 怨 气 ”</h3><p style="margin:0"><strong>邦和家，是两个做事的地方。</strong><br/><br/>① <strong>在邦</strong>——<strong>在诸侯之国做事</strong><br/>② <strong>在家</strong>——<strong>在卿大夫之家做事</strong><br/>③ <strong>两处都无怨</strong>——<strong>换哪个地方，心里都不存怨</strong><br/><br/><strong>一句话：不是地方好，是人心里干净。</strong></p><p><strong>“无怨”有两层。</strong><br/><br/>① <strong>自己不怨</strong>——<strong>不怨上头不用我，不怨下头不听话</strong><br/>② <strong>别人也不怨你</strong>——<strong>做到敬和慎，做事就少结怨</strong><br/>③ <strong>孔子把这一条也归到仁里</strong>——<strong>心里存着怨，仁就进不来</strong><br/><br/><strong>一句话：怨气一起，道理就听不进去了。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>在单位有怨气</strong>——<strong>多半是“敬”和“慎”缺了一样</strong><br/>② <strong>觉得自己被亏待</strong>——<strong>先查一查手里的事办扎实没有</strong><br/><br/><strong>一句话：把事做正，怨气自己就淡了。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：雍虽不敏</h2><h3>“ 听 懂 就 做 ”</h3><p style="margin:0"><strong>这句话上一章刚出现过。</strong><br/><br/>① <strong>颜渊答的是这一句</strong>——<strong>“回虽不敏，请事斯语矣”</strong><br/>② <strong>仲弓答的还是这一句</strong>——<strong>只换了个名字</strong><br/>③ <strong>孔门的好学生都这样收尾</strong>——<strong>不问第二遍，先去做</strong><br/><br/><strong>一句话：学到了就去做，不评论、不发挥。</strong></p><p><strong>仲弓这个人，值得说一说。</strong><br/><br/>① <strong>他名叫冉雍</strong>——<strong>父亲出身低贱，当时人看不起他</strong><br/>② <strong>孔子照样说他“可使南面”</strong>——<strong>能当一国之君的那块料</strong><br/>③ <strong>孔子还说过：犁牛之子骍且角</strong>——<strong>出身不好，不碍着你好</strong><br/><br/><strong>一句话：孔子看的是人，不是门第。</strong></p><p><strong>今天怎么用？</strong><br/><br/>① <strong>听懂一条就做一条</strong>——<strong>别急着找第二条</strong><br/>② <strong>被人看轻过</strong>——<strong>把手里的事做出来，比争辩有用</strong><br/><br/><strong>一句话：出身不由己，做成什么样由己。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 敬慎恕</h2><p>本章三层意思——</p><h3>“出门如见大宾。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>敬在脸上。</strong>见谁都当贵宾待，不论对方有没有用。</p><p>⚖️ “使民如承大祭。”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>慎在手上。</strong>手里有别人的力气，就得当大事办。</p><p>💧 “己所不欲，勿施于人。”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>恕在心里。</strong>不用猜别人心思，拿自己当尺子。</p><p>🧭 “在邦无怨，在家无怨。”</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>怨气淡了，仁才进得来。</strong>把事做正，怨气自己就淡。</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>一条理：</strong>仁不玄，就是待人恭敬、用人慎重、心里拿自己当尺子。<strong>位置：</strong>《颜渊》第二章，紧接颜渊问仁之后。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ “己所不欲，勿施于人”就是“将心比心”吗？</h3><p><strong>是，但比将心比心更硬气。</strong><br/><br/>① <strong>不是问别人想要什么</strong>——<strong>是问自己不愿意什么</strong><br/>② <strong>拿自己当尺子</strong>——<strong>这条尺子谁也赖不掉</strong><br/>③ <strong>孔子说这一条可以终身行之</strong>——<strong>子贡问“有一言而可以终身行之者乎”，答的就是它</strong><br/><br/><strong>记法：不用猜别人心思，先管住自己不愿的那一份。</strong></p><h3>❓ “出门如见大宾”是教人见谁都巴结吗？</h3><p><strong>不是巴结，是敬。</strong><br/><br/>① <strong>敬是把人当人看</strong>——<strong>不是把人当靠山</strong><br/>② <strong>见大宾有个样子</strong>——<strong>衣裳整、说话慢、眼睛看着人</strong><br/>③ <strong>巴结是有求于人</strong>——<strong>敬是无所求</strong><br/><br/><strong>记法：恭敬不用花钱，只看你有没有那份心。</strong></p><h3>❓ 仲弓和颜渊答的一样，有什么讲究？</h3><p><strong>同一句话，两个学生。</strong><br/><br/>① <strong>颜渊最聪明</strong>——<strong>孔子最得意的门生</strong><br/>② <strong>仲弓出身低</strong>——<strong>父亲贱，当时人看不起他</strong><br/>③ <strong>两人答的都是“请事斯语”</strong>——<strong>路子不同，下手处一样</strong><br/><br/><strong>记法：聪明也好，出身低也好，听懂就做，才算学到。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🙋 见人拿出那份郑重</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“出门如见大宾”</strong>——<strong>不是让你低三下四，是让你把人当人看</strong>。<strong>衣裳整、说话慢、眼睛看着人，这三样一分钱不花</strong>。</p><p>⚖️ 拿自己当尺子</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“己所不欲，勿施于人”</strong>——<strong>不用研究别人爱听什么，只问自己受不受得了</strong>。<strong>受不了的那一句，就别说出口</strong>。</p><p>📖 把事做正，怨气自淡</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>“在邦无怨，在家无怨”</strong>——<strong>换哪个地方做事，心里都不存怨</strong>。<strong>怨气一起，道理就听不进去了</strong>。<br/><br/><strong>本章的落点：敬一分，慎一分，恕一分——三样齐了，才叫仁。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天我们一起学习了《论语·颜渊》篇的第二章——仲弓问仁，孔子给了三句话：出门如见大宾，使民如承大祭；己所不欲，勿施于人；在邦无怨，在家无怨。<strong>一句讲敬，一句讲慎，一句讲恕，是《论语》里最能把“仁”落到手上的一章。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                己所不欲，勿施于人。
            </p><p>回顾本课要点:</p><p>出门如见大宾</p><br/><p><strong>敬在脸上。</strong>见谁都当贵宾待，不论对方有没有用</p><p>使民如承大祭</p><br/><p><strong>慎在手上。</strong>手里有别人的力气，就得当大事办</p><p>己所不欲，勿施于人</p><br/><p><strong>恕在心里。</strong>不用猜别人心思，拿自己当尺子</p><p>在邦无怨，在家无怨</p><br/><p><strong>怨气淡了，仁才进得来。</strong>把事做正，怨气自己就淡</p><p><strong>在全篇中的位置:</strong>这是<strong>《颜渊》第二章</strong>。上一章讲<strong>克己复礼、四勿</strong>，这一章讲<strong>待人接物的敬、慎、恕</strong>——同一件事，两个学生，两种下手处。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>己所不欲，勿施于人。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：你今天有没有把不愿意受的那一下加给别人？② 学一句实在话：这一句我不说。③ 讲给家人听：<strong>为什么这条尺子谁也赖不掉</strong>？</p><p><strong>把这一章记在心里:</strong><strong>敬一分，慎一分，恕一分——三样齐了，才叫仁。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “己所不欲，勿施于人。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·颜渊》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '277-zhong-gong-wen-ren';
const QUIZ = [
  {q: '1. “仲弓问仁”中的仲弓，是孔子的哪位弟子？', opts: ['冉雍，字仲弓', '冉有，字子有', '仲由，字子路'], ans: 0, exp: '仲弓名冉雍，孔子弟子。他父亲出身低贱，当时人看不起他，孔子却说他“可使南面”'},
  {q: '2. “出门如见大宾”中的“大宾”指什么？', opts: ['自家长辈', '贵宾、诸侯朝聘之宾', '路过的客人'], ans: 1, exp: '大宾是最郑重的那一等客人。出门办事，见谁都当贵宾待——敬字当头'},
  {q: '3. “使民如承大祭”中的“承”是什么意思？', opts: ['承当、承办', '继承', '承认'], ans: 0, exp: '承是承当、承办。祭天地祖先一步都错不得，用人的时候心里也要有这份敬畏'},
  {q: '4. “使民如承大祭”强调的是哪种态度？', opts: ['热闹', '慎重、不敢轻慢', '节俭'], ans: 1, exp: '手里有别人的力气，就得当大事办。这一句讲的是“慎”'},
  {q: '5. “己所不欲，勿施于人”是什么意思？', opts: ['自己不愿意的就别去争', '自己不愿意的，不要加给别人', '自己不想要的就送给别人'], ans: 1, exp: '这是全章最出名的一句：自己不愿受的那一份，别加到别人身上'},
  {q: '6. “己所不欲，勿施于人”是哪个字的注解？', opts: ['忠', '恕', '孝'], ans: 1, exp: '这是“恕”的标准一句话。子贡问“有一言而可以终身行之者乎”，孔子答的就是它'},
  {q: '7. “在邦无怨，在家无怨”的“邦”和“家”各指什么？', opts: ['国家和自己的家', '诸侯之国、卿大夫之家', '城市和乡村'], ans: 1, exp: '邦是诸侯之国，家是卿大夫的采邑。两处都指做事的地方，不是今天的“小家”'},
  {q: '8. “雍虽不敏”中的“雍”指谁？', opts: ['仲弓的名字', '颜渊的名字', '子贡的名字'], ans: 0, exp: '雍是仲弓的名（冉雍）。不敏是谦辞，说自己不聪明'},
  {q: '9. 本章结尾“请事斯语矣”，和哪一章的说法相同？', opts: ['《颜渊》第一章颜渊说的', '《学而》第一章', '《先进》最后一章'], ans: 0, exp: '上一章颜渊说的是“回虽不敏，请事斯语矣”。孔门好学生都这样收尾：听懂就去做'},
  {q: '10. 本章讲“仁”，入手处是什么？', opts: ['读熟经典', '敬、慎、恕——从待人接物做起', '远离人群'], ans: 1, exp: '敬在脸上，慎在手上，恕在心里。仁不玄，就在一天里怎么待人、怎么用人'}
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=xiangdang277"></script><script src="../../assets/js/slide-engine.js?v=xiangdang277"></script>
<script src="../../assets/js/speech.js?v=xiangdang277"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
</div>
<script defer="" src="../../assets/js/auth-email.js?v=xiangdang277"></script>
<script defer="" src="../../assets/js/auth.js?v=xiangdang277"></script>
<script defer="" src="../../assets/js/api-client.js?v=xiangdang277"></script>
</body>
</html>
'''

out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'lessons', '277-zhong-gong-wen-ren')
os.makedirs(out_dir, exist_ok=True)
html = TEMPLATE.replace('__RUBY__', build_ruby_paragraphs())
with io.open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(html)
print('written:', os.path.join(out_dir, 'index.html'))
print('chars:', len(html))
