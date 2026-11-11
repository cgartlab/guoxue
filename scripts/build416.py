# -*- coding: utf-8 -*-
"""生成第 416 课《季氏》第一章「季氏将伐颛臾」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
季jì 氏shì 将jiāng 伐fá 颛zhuān 臾yú 。 冉rǎn 有yǒu 、 季jì 路lù 见jiàn 于yú 孔kǒng 子zǐ 曰yuē ： 「 季jì 氏shì 将jiāng 有yǒu 事shì 于yú 颛zhuān 臾yú 。 」
||
孔kǒng 子zǐ 曰yuē ： 「 求qiú ！ 无wú 乃nǎi 尔ěr 是shì 过guò 与yú ？ 夫fú 颛zhuān 臾yú ， 昔xī 者zhě 先xiān 王wáng 以yǐ 为wéi 东dōng 蒙méng 主zhǔ ， 且qiě 在zài 邦bāng 域yù 之zhī 中zhōng 矣yǐ ， 是shì 社shè 稷jì 之zhī 臣chén 也yě 。 何hé 以yǐ 伐fá 为wéi ？ 」
||
冉rǎn 有yǒu 曰yuē ： 「 夫fū 子zǐ 欲yù 之zhī ， 吾wú 二èr 臣chén 者zhě 皆jiē 不bù 欲yù 也yě 。 」
||
孔kǒng 子zǐ 曰yuē ： 「 求qiú ！ 周zhōu 任rén 有yǒu 言yán 曰yuē ： 『 陈chén 力lì 就jiù 列liè ， 不bù 能néng 者zhě 止zhǐ 。 』 危wēi 而ér 不bù 持chí ， 颠diān 而ér 不bù 扶fú ， 则zé 将jiāng 焉yān 用yòng 彼bǐ 相xiàng 矣yǐ ？ 且qiě 尔ěr 言yán 过guò 矣yǐ ！ 虎hǔ 兕sì 出chū 于yú 柙xiá ， 龟guī 玉yù 毁huǐ 于yú 椟dú 中zhōng ， 是shì 谁shuí 之zhī 过guò 与yú ？ 」
||
冉rǎn 有yǒu 曰yuē ： 「 今jīn 夫fú 颛zhuān 臾yú ， 固gù 而ér 近jìn 于yú 费bì 。 今jīn 不bù 取qǔ ， 后hòu 世shì 必bì 为wéi 子zǐ 孙sūn 忧yōu 。 」
||
孔kǒng 子zǐ 曰yuē ： 「 求qiú ！ 君jūn 子zǐ 疾jí 夫fú 舍shě 曰yuē 『 欲yù 之zhī 』 而ér 必bì 为wéi 之zhī 辞cí 。 丘qiū 也yě 闻wén 有yǒu 国guó 有yǒu 家jiā 者zhě ， 不bù 患huàn 寡guǎ 而ér 患huàn 不bù 均jūn ， 不bù 患huàn 贫pín 而ér 患huàn 不bù 安ān 。 盖gài 均jūn 无wú 贫pín ， 和hé 无wú 寡guǎ ， 安ān 无wú 倾qīng 。 夫fú 如rú 是shì ， 故gù 远yuǎn 人rén 不bù 服fú ， 则zé 修xiū 文wén 德dé 以yǐ 来lái 之zhī 。 既jì 来lái 之zhī ， 则zé 安ān 之zhī 。 今jīn 由yóu 与yú 求qiú 也yě ， 相xiàng 夫fū 子zǐ ， 远yuǎn 人rén 不bù 服fú 而ér 不bù 能néng 来lái 也yě ， 邦bāng 分fēn 崩bēng 离lí 析xī 而ér 不bù 能néng 守shǒu 也yě ， 而ér 谋móu 动dòng 干gān 戈gē 于yú 邦bāng 内nèi 。 吾wú 恐kǒng 季jì 孙sūn 之zhī 忧yōu ， 不bù 在zài 颛zhuān 臾yú ， 而ér 在zài 萧xiāo 墙qiáng 之zhī 内nèi 也yě 。 」
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '0.95rem'
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
                     'width:100%%;max-width:none;margin:0.1em 0 0' % (FS, LH))
        out.append('<p style="%s">%s</p>' % (style, ''.join(html)))
    return '\n'.join(out)


TEMPLATE = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="《论语·季氏》第一章精讲：季氏将伐颛臾。冉有、季路来见孔子，孔子先责二人失职，再讲治国之道——不患寡而患不均，不患贫而患不安；远人不服则修文德以来之，既来之则安之。最后点破：季孙之忧不在颛臾，而在萧墙之内。" name="description"/>
<meta content="均无贫 · 不患寡而患不均 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第一章精讲：不怕少，就怕不公" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/416-ji-shi-jiang-fa-zhuan-yu/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/416-ji-shi-jiang-fa-zhuan-yu/index.html" rel="canonical"/>
<title>均无贫 · 不患寡而患不均 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi416" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi416" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">均无贫</h2><div class="cover-ornament"></div><p class="cover-subtitle">不怕少，就怕不公</p><p class="cover-desc">这是<strong>《论语·季氏》第一章</strong>。季氏要打<strong>颛臾</strong>，冉有、子路跑来解释"不是我们的意思"。孔子连驳三次，最后说：<strong>不患寡而患不均</strong>——不怕人少，就怕分不公；<strong>季孙的忧患不在颛臾，而在萧墙之内</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:12px 22px 12px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>季氏要打颛臾，冉有、子路推说不是自己的意思。孔子连驳三次：这事该你们管；扶助的人不扶，要你何用；虎兕出笼、龟玉毁匣，谁的过错？最后说：不怕人少只怕不均，不怕穷只怕不安，均了、和了、安了，就没有贫、没有寡、没有倾覆。远方不服就修文德招来，来了就让他们安定。你们辅佐季氏，远方不来、国家要散，反倒在国内动武——季孙的忧患不在颛臾，在萧墙之内</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第一章</strong>；<strong>合章本多作 16.1</strong>；<strong>季氏指季康子，颛臾是鲁国境内的一个小国</strong>；<strong>冉有、子路当时是季氏的家臣</strong>；<strong>自此进入《季氏》篇</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>不怕少，就怕不公</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">有事</span>：<strong>用兵、打仗的委婉说法</strong>——<strong>不是"有事情要做"</strong>。</p><p><span class="ds-highlight">无乃……与</span>：<strong>恐怕……吧</strong>——<strong>委婉的反问，其实是责备</strong>。</p><p><span class="ds-highlight">社稷之臣</span>：<strong>国家的臣属</strong>——<strong>社稷＝国家，不是"会社"</strong>。</p><p><span class="ds-highlight">陈力就列</span>：<strong>尽力做好本职，就任这个位子</strong>——<strong>不能者止：干不了就辞</strong>。</p><p><span class="ds-highlight">相</span>：<strong>读 xiàng，扶助、辅佐的人</strong>——<strong>扶着走的人，不是看相貌</strong>。</p><p><span class="ds-highlight">兕、柙、椟</span>：<strong>兕 sì 犀牛；柙 xiá 笼子；椟 dú 匣子</strong>。</p><p><span class="ds-highlight">萧墙</span>：<strong>宫室门内的照壁</strong>——<strong>比喻自己家里、内部</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>不怕少，就怕不公</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：将伐颛臾</h2><h3>“ 无 乃 尔 是 过 与 ”</h3><p style="margin:0"><strong>季氏是谁？颛臾是什么地方？</strong><br/><br/>① <strong>季氏＝季康子，鲁国掌权的卿大夫</strong><br/>② <strong>颛臾是鲁国境内的小国，附属于鲁</strong><br/><br/><strong>一句话：先进攻自己的附属国。</strong></p><p><strong>冉有、子路是什么身份？</strong><br/><br/>① <strong>孔子的学生，同时是季氏的家臣</strong><br/>② <strong>主人要动手，他们来探老师口气</strong><br/><br/><strong>一句话：这事跟他们脱不了干系。</strong></p><p><strong>孔子第一句为什么直接点「求」？</strong><br/><br/>① <strong>无乃尔是过与＝恐怕是你的过错吧</strong><br/>② <strong>不骂季氏，先问学生：你尽到责任没有</strong><br/><br/><strong>一句话：先问自己有没有拦住。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：陈力就列</h2><h3>“ 危 而 不 持 · 颠 而 不 扶 ”</h3><p style="margin:0"><strong>「陈力就列，不能者止」怎么讲？</strong><br/><br/>① <strong>有多大本事就担多大位子</strong><br/>② <strong>干不了，就该辞</strong><br/><br/><strong>一句话：占着位子，就得担事。</strong></p><p><strong>「焉用彼相矣」在说什么？</strong><br/><br/>① <strong>相＝扶着走的人、辅佐的人</strong><br/>② <strong>危险不扶、跌倒不搀，要这个人干什么</strong><br/><br/><strong>一句话：白拿俸禄，不如不在。</strong></p><p><strong>「虎兕出于柙，龟玉毁于椟中」比什么？</strong><br/><br/>① <strong>虎兕跑出笼子，龟玉碎在匣里</strong><br/>② <strong>东西交给谁看管，出了事就是谁的责任</strong><br/><br/><strong>一句话：看管的人，推不掉。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：均无贫</h2><h3>“ 不 患 寡 而 患 不 均 ”</h3><p style="margin:0"><strong>「患」是什么意思？</strong><br/><br/>① <strong>担忧、发愁——不是「患病」</strong><br/><br/><strong>一句话：怕的不是少，是分不匀。</strong></p><p><strong>「均无贫，和无寡，安无倾」三层？</strong><br/><br/>① <strong>均：分得公，就没有真穷</strong><br/>② <strong>和：上下和，就不怕人少</strong><br/>③ <strong>安：内部安，就不会倾覆</strong><br/><br/><strong>一句话：公、和、安，三根柱子。</strong></p><p><strong>「既来之，则安之」今天怎么用？</strong><br/><br/>① <strong>本义：招来了，就让他们安定</strong><br/>② <strong>不是「既然来了，就安心待着」</strong><br/><br/><strong>一句话：来了要安顿。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：萧墙之内</h2><h3>“ 而 在 萧 墙 之 内 也 ”</h3><p style="margin:0"><strong>「必为之辞」批评什么？</strong><br/><br/>① <strong>心里想要，嘴上另找一套说法</strong><br/>② <strong>君子最恨这种绕弯子的借口</strong><br/><br/><strong>一句话：要就说要，别编理由。</strong></p><p><strong>「邦分崩离析」是什么局面？</strong><br/><br/>① <strong>国家四分五裂，守不住</strong><br/>② <strong>这种时候还对外动武，是雪上加霜</strong><br/><br/><strong>一句话：家里漏水，别去挑邻家的事。</strong></p><p><strong>为什么说忧在「萧墙之内」？</strong><br/><br/>① <strong>萧墙＝宫门内的照壁，指自家内部</strong><br/>② <strong>季氏真正的麻烦，是自己家里权力坐不稳</strong><br/><br/><strong>一句话：祸不在外面，在自己家里。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看这件事</h2><p>这一章层层往下，一层比一层深——</p><h3>“均无贫 · 和无寡 · 安无倾”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>职分：</strong>在其位就得担其责。</p><p>🔧 不能者止，拦不住就直说，别替主人找借口</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>分配：</strong>不怕少，就怕不公。</p><p>⚖️ 均了就没有真穷，和了就不怕人少</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>内忧：</strong>忧在萧墙之内。</p><p>🏠 家里不齐，外面再稳也是空的</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第一章，<strong>新开一篇</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「不患寡而患不均」是讲平均主义吗？</h3><p><strong>不是人人一样多，是分得让人服气。</strong><br/><br/>① <strong>「均」讲的是分得公，不是分得一样</strong><br/>② <strong>差距大得人心不服，再多也是乱的根子</strong><br/>③ <strong>记住：公，不是平</strong><br/><br/><strong>记法：怕不公，不怕有差。</strong></p><h3>❓ 孔子为什么反对打颛臾？</h3><p><strong>三条理由，一条比一条实。</strong><br/><br/>① <strong>名分上：颛臾是先王封的主祭，是社稷之臣</strong><br/>② <strong>道理上：它在鲁国疆域之内，不是敌国</strong><br/>③ <strong>后果上：家里本就要散，动武只会更快</strong><br/><br/><strong>记法：不该打、不用打、打不得。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>从分东西和担责任学起。</strong><br/><br/>① <strong>分东西先讲清规则，别让谁觉得吃亏</strong><br/>② <strong>答应了的事就做到，做不到要早说</strong><br/>③ <strong>家里的矛盾，先在家里说开</strong><br/><br/><strong>记法：分得公、担得起、家里说。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>⚖️ 分东西先讲公平</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>规则说在前头，过程摆在明处</strong>；<strong>人人心里服，日子才安稳</strong>。</p><p>🔧 在其位就担其责</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>干不了就说干不了，别占着位子找借口</strong>；<strong>拦不住的事，也要把话说清楚</strong>。</p><p>🏠 家里的事家里解决</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>外面再有面子，屋里不齐也是空的</strong>；<strong>先把自己家理顺，再谈别的</strong><br/><br/><strong>本章的落点：不怕少，就怕不公。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「将伐颛臾」。记牢：<strong>不怕少，就怕不公。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                不患寡而患不均，不患贫而患不安。
            </p><p>回顾本课要点:</p><p>无乃尔是过与 · 先问自己</p><br/><p><strong>占着位子，就得担事。</strong></p><p>均无贫 · 和无寡 · 安无倾</p><br/><p><strong>公、和、安，三根柱子。</strong></p><p>忧在萧墙之内 · 祸从家里起</p><br/><p><strong>家里不齐，外面白忙。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第一章</strong>，<strong>新开一篇</strong>；与 415 课连读——<strong>那课讲待人的细节，这课讲治事的道理</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>丘也闻有国有家者，不患寡而患不均，不患贫而患不安。</p>
</div><p><strong>课后小挑战:</strong>① 今天分一次东西，先把规则说清楚。② 背一句：不患寡而患不均。</p><p><strong>把这一章记在心里:</strong><strong>不怕少，就怕不公。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “不患寡而患不均！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '416-ji-shi-jiang-fa-zhuan-yu';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《阳货》'], ans: 0, exp: '按站内分法，这是《季氏》第一章，新开一篇'},
  {q: '2. 「季氏将有事于颛臾」的「有事」是什么意思？', opts: ['发动军事行动、用兵', '有事情要商量', '要派人去办事'], ans: 0, exp: '古书里「有事」常是打仗的委婉说法'},
  {q: '3. 孔子说颛臾是「社稷之臣」，理由是什么？', opts: ['先王封它做东蒙山主祭，又在鲁国邦域之内', '颛臾兵强马壮', '颛臾和季氏有仇'], ans: 0, exp: '名分和地理位置都摆在那里，不该伐'},
  {q: '4. 冉有说「吾二臣者皆不欲也」，孔子怎么驳？', opts: ['陈力就列，不能者止；危而不持，颠而不扶，焉用彼相', '让他别再说话', '说季氏一定听他的'], ans: 0, exp: '占了位子就得担责，拦不住也要说'},
  {q: '5. 「虎兕出于柙，龟玉毁于椟中」比喻什么？', opts: ['东西交给谁看管，出了事就是谁的责任', '野兽很危险', '宝贝要好好收藏'], ans: 0, exp: '看管的人推不掉'},
  {q: '6. 「不患寡而患不均」的「患」是什么意思？', opts: ['担忧、发愁', '生病', '得罪'], ans: 0, exp: '怕的不是人少，是分不公'},
  {q: '7. 「均无贫，和无寡，安无倾」讲的是哪三层？', opts: ['分得公就没有真穷、上下和就不怕人少、内部安就不会倾覆', '地均、人和、天安', '平均分钱、人多、房子稳'], ans: 0, exp: '公、和、安，三根柱子'},
  {q: '8. 「既来之，则安之」的本义是？', opts: ['招来了，就让他们安定下来', '既然来了，就安心待着', '来了就安排住处'], ans: 0, exp: '这是治国的话，不是劝人认命'},
  {q: '9. 「萧墙之内」指什么？', opts: ['宫室门内的照壁，比喻自己家里、内部', '一道城墙', '鲁国的边境'], ans: 0, exp: '祸不在外面，在自己家里'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['不患寡而患不均，不患贫而患不安', '远人不服则修文德', '君子疾夫舍曰欲之'], ans: 0, exp: '不怕少，就怕不公'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi416"></script><script src="../../assets/js/slide-engine.js?v=jishi416"></script>
<script src="../../assets/js/speech.js?v=jishi416"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi416"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi416"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi416"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '416-ji-shi-jiang-fa-zhuan-yu')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
