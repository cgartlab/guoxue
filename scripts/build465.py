# -*- coding: utf-8 -*-
"""生成第 465 课《子张》第四章「子夏曰：虽小道，必有可观者焉……」课件。
全章约 28 字、三段；短章大字版式（与 463 同基准）。
"""
import io
import os
import re

PY = """
子zǐ 夏xià 曰yuē ： ||
虽suī 小xiǎo 道dào ， 必bì 有yǒu 可kě 观guān 者zhě 焉yān ； ||
致zhì 远yuǎn 恐kǒng 泥nì ， 是shì 以yǐ 君jūn 子zǐ 不bù 为wéi 也yě 。
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
<meta content="《论语·子张》第四章精讲：子夏曰：虽小道，必有可观者焉；致远恐泥，是以君子不为也。子夏说：哪怕是小的技艺，也一定有它值得看的地方；但要拿它去走远路、成大事，怕就怕陷在里面出不来，所以君子不把心思放在小道上。小处有可观，大处要走远。小手艺有小看头，走远路别被绊住。" name="description"/>
<meta content="致远恐泥 · 小处有可观，大处要走远 · 国学课堂" property="og:title"/>
<meta content="《论语·子张》第四章精讲：小手艺有小看头，走远路别被绊住" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/465-zhi-yuan-kong-ni/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/465-zhi-yuan-kong-ni/index.html" rel="canonical"/>
<title>致远恐泥 · 小处有可观，大处要走远 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=zhangz465" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=zhangz465" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">致远恐泥</h2><div class="cover-ornament"></div><p class="cover-subtitle">小处有可观，大处要走远</p><p class="cover-desc">这是<strong>《论语·子张》第四章</strong>。<strong>子夏</strong>说：哪怕是<strong>小的技艺</strong>，也一定有它<strong>值得看的地方</strong>；但要拿它<strong>走远路、成大事</strong>，怕就怕<strong>陷在里面出不来</strong>，所以君子<strong>不把心思放在小道上</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:20px 18px 16px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>子夏说：即使是小的技艺，也一定有可取之处；但要用它去达到远大的目标，恐怕会陷在里面走不通，所以君子不做小道。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《子张》第四章</strong>；<strong>合章本作 19.4</strong>；<strong>「泥」读 nì，是陷住、走不通，不是泥巴</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>小道有可看，大道不回头。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">小道</span>：<strong>小的技艺、旁门小技</strong>——<strong>种花、木工这类手艺</strong>。</p><p><span class="ds-highlight">可观</span>：<strong>有值得看的地方</strong>——<strong>小处也有真功夫</strong>。</p><p><span class="ds-highlight">致远</span>：<strong>达到远大的目标</strong>——<strong>走远路、成大事</strong>。</p><p><span class="ds-highlight">恐泥</span>：<strong>怕陷住</strong>——<strong>「泥」读 nì，是陷在里头走不通</strong>。</p><p><span class="ds-highlight">是以</span>：<strong>所以</strong>——<strong>承上启下的说法</strong>。</p><p><span class="ds-highlight">不为</span>：<strong>不做、不把心思放在那</strong>——<strong>「为」读 wéi</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>小玩可以，别玩进去出不来。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：虽小道，必有可观者焉</h2><h3>“ 虽 小 道 ， 必 有 可 观 者 焉 ”</h3><p style="margin:0"><strong>「小道」是什么？</strong><br/><br/>① <strong>手艺、小技巧、旁门小技</strong><br/>② <strong>不是歪门邪道，是小的门道</strong><br/><br/><strong>一句话：小道是小事的本事。</strong></p><p><strong>为什么「必有可观」？</strong><br/><br/>① <strong>任何一门手艺做到精，都有它的道理</strong><br/>② <strong>小处也有真功夫，值得看</strong><br/><br/><strong>一句话：再小的门道，钻进去了也有讲究。</strong></p><p><strong>孔门轻视小手艺吗？</strong><br/><br/>① <strong>不轻视，是排先后</strong><br/>② <strong>先承认它有用，再说不能当主业</strong><br/><br/><strong>一句话：先给足面子，再讲清分寸。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：致远恐泥</h2><h3>“ 致 远 恐 泥 ”</h3><p style="margin:0"><strong>「致远」是什么？</strong><br/><br/>① <strong>走远路、成大器</strong><br/>② <strong>君子要担的是大事</strong><br/><br/><strong>一句话：远路要有大本钱。</strong></p><p><strong>「泥」为什么可怕？</strong><br/><br/>① <strong>像车轮陷进泥里，拔不出来</strong><br/>② <strong>精力有限，耗在小处，大处就没份</strong><br/><br/><strong>一句话：陷进去，出不来。</strong></p><p><strong>「恐」字见分寸？</strong><br/><br/>① <strong>不是说小道没用，是提醒代价</strong><br/>② <strong>怕的不是小道，是只顾小道</strong><br/><br/><strong>一句话：一个「恐」字，把话说得不绝对。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：是以君子不为也</h2><h3>“ 是 以 君 子 不 为 也 ”</h3><p style="margin:0"><strong>「不为」是不碰吗？</strong><br/><br/>① <strong>不是禁绝，是不把主业放这</strong><br/>② <strong>当消遣可以，当饭碗要掂量</strong><br/><br/><strong>一句话：不是不做，是不钻进去。</strong></p><p><strong>君子的算盘怎么打？</strong><br/><br/>① <strong>一天只有那么多时间</strong><br/>② <strong>先做能撑起一生的事</strong><br/><br/><strong>一句话：先拣后做，大事在前。</strong></p><p><strong>用来管自己怎么用？</strong><br/><br/>① <strong>刷小视频、玩小游戏，也算「小道」</strong><br/>② <strong>玩得起、放得下，才算「不为」</strong><br/><br/><strong>一句话：玩得起，别玩进去。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：整章连起来读</h2><h3>“ 虽 小 道 …… 君 子 不 为 也 ”</h3><p style="margin:0"><strong>三句怎么连？</strong><br/><br/>① <strong>先承认（可观）→ 再提醒（恐泥）→ 落点（不为）</strong><br/>② <strong>一句一转折，步步往后收</strong><br/><br/><strong>一句话：先给足面子，再讲清分寸。</strong></p><p><strong>和孔子哪句话呼应？</strong><br/><br/>① <strong>孔子说「游于艺」——艺可以游，不可溺</strong><br/>② <strong>游是逛一圈，溺是陷进去</strong><br/><br/><strong>一句话：逛一圈就出来。</strong></p><p><strong>整章记一句什么？</strong><br/><br/>① <strong>小道可以看，不可以泡</strong><br/>② <strong>主业要立得住，远路要走得到</strong><br/><br/><strong>一句话：看得开，收得住。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「拣」</h2><p>一句话，三层意思——</p><h3>“小处有可观，大处要走远。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>小道有可观，大道怕泥——承认小用，守住大路。</p><p>🚗 小用认，大路守</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>时间是本钱，花在小处多一分，大处就少一分。</p><p>⏳ 本钱只有一份</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>不为，不是瞧不起，是知道先做哪件。</p><p>🪜 落点是「排先后」</p>
<p>接 464 课：<strong>上一章讲待人要容，这一章讲做事要拣——什么该做、什么少碰</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 子夏是不是瞧不起手艺人？</h3><p><strong>不是。是排先后，不是骂没用。</strong><br/><br/>① <strong>原文先说「必有可观」，先承认它有用</strong><br/>② <strong>不为是排先后，不是禁绝</strong><br/>③ <strong>一天时间有限，先担大事</strong><br/><br/><strong>记法：不轻看，只排先后。</strong></p><h3>❓ 「泥」是泥巴的泥吗？</h3><p><strong>不是。这里读 nì，是陷住。</strong><br/><br/>① <strong>像车轮陷进泥里，拔不出来</strong><br/>② <strong>指人陷在小处，走不通、出不来</strong><br/>③ <strong>跟泥巴、泥土没关系</strong><br/><br/><strong>记法：泥是陷，不是土。</strong></p><h3>❓ 玩手机、刷视频算小道吗？</h3><p><strong>算。道理是一样的。</strong><br/><br/>① <strong>有它的乐趣，也算「可观」</strong><br/>② <strong>但耗时间，最容易陷进去</strong><br/>③ <strong>玩得起、放得下，才算「不为」</strong><br/><br/><strong>记法：玩得起，别玩进去。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🎨 小事也有看头</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>剪纸、折纸都有巧思</strong>；<strong>看到别人的小本事，别撇嘴</strong>。</p><p>⏳ 时间别耗空</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>小游戏刷个没完，大事就没了份</strong>；<strong>先做要紧的</strong>。</p><p>⚖️ 先拣后做</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>事情排个先后</strong>；<strong>能撑起日子的先做</strong><br/><br/><strong>本章的落点：小处有可观，大处要走远。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「致远恐泥」。记牢：<strong>小处有可观，大处要走远。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                虽小道，必有可观者焉；致远恐泥，是以君子不为也。
            </p><p>回顾本课要点:</p><p>虽小道 · 也有真功夫</p><br/><p><strong>再小的门道，钻进去了也有讲究。</strong></p><p>致远恐泥 · 泥是陷住</p><br/><p><strong>陷进去，出不来。</strong></p><p>君子不为 · 排先后，不当主业</p><br/><p><strong>不是不做，是不钻进去。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《子张》第四章</strong>。接 464 课：上一章讲待人要容，这一章讲做事要拣。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>虽小道，必有可观者焉；致远恐泥，是以君子不为也。</p>
</div><p><strong>课后小挑战:</strong>① 写下你花时间最多的一件小事，看看值不值。② 背一句：致远恐泥，是以君子不为也。</p><p><strong>把这一章记在心里:</strong><strong>小处有可观，大处要走远。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “致远恐泥，是以君子不为也。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·子张》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '465-zhi-yuan-kong-ni';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《子张》', '《微子》', '《雍也》'], ans: 0, exp: '这是《子张》第四章，子夏的话'},
  {q: '2. 「虽小道」的「小道」指什么？', opts: ['小的技艺、旁门小技', '小路', '坏门道'], ans: 0, exp: '小道是种花、木工这类小手艺，不是歪门邪道'},
  {q: '3. 「必有可观者焉」是什么意思？', opts: ['一定有值得看的地方', '一定很壮观', '一定有人围观'], ans: 0, exp: '小处也有真功夫，子夏先承认它有用'},
  {q: '4. 「致远恐泥」的「泥」读什么？', opts: ['nì', 'ní', 'mí'], ans: 0, exp: '这里读 nì，是陷住的意思'},
  {q: '5. 「泥」是什么意思？', opts: ['陷住、走不通', '泥巴', '拖延'], ans: 0, exp: '像车轮陷进泥里拔不出来，指陷在小处出不来'},
  {q: '6. 「是以」是什么意思？', opts: ['所以', '以为', '因此高兴'], ans: 0, exp: '是以就是所以，承上启下'},
  {q: '7. 「君子不为也」的「为」读什么？', opts: ['wéi，做', 'wèi，为了', 'wěi，以为'], ans: 0, exp: '为读 wéi，是做的意思'},
  {q: '8. 子夏这句话的意思是？', opts: ['小道有用但耗人，君子不把心思放那', '小道全是坏的要远离', '小道比大道还重要'], ans: 0, exp: '小处有可观，但要成大事，别陷在里面'},
  {q: '9. 子夏是在骂小手艺吗？', opts: ['不是，承认有用，只是不排在前', '是，全都该扔掉', '没提到手艺'], ans: 0, exp: '原文先说「必有可观」，不为只是排先后'},
  {q: '10. 本章与 464 课的关系是？', opts: ['464 讲待人要容，465 讲做事要拣', '是同一章的两半', '都在讲交友'], ans: 0, exp: '464 说容人，465 说拣事，一宽一拣'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=zhangz465"></script><script src="../../assets/js/slide-engine.js?v=zhangz465"></script>
<script src="../../assets/js/speech.js?v=zhangz465"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=zhangz465"></script>
<script defer="" src="../../assets/js/auth.js?v=zhangz465"></script>
<script defer="" src="../../assets/js/api-client.js?v=zhangz465"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '465-zhi-yuan-kong-ni')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
