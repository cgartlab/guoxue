# -*- coding: utf-8 -*-
"""生成第 466 课《子张》第五章「子夏曰：日知其所亡，月无忘其所能……」课件。
全章约 24 字、三段；短章大字版式（与 463 同基准）。
"""
import io
import os
import re

PY = """
子zǐ 夏xià 曰yuē ： ||
日rì 知zhī 其qí 所suǒ 亡wú ， 月yuè 无wú 忘wàng 其qí 所suǒ 能néng ， ||
可kě 谓wèi 好hào 学xué 也yě 已yǐ 矣yǐ 。
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
<meta content="《论语·子张》第五章精讲：子夏曰：日知其所亡，月无忘其所能，可谓好学也已矣。子夏说：每天知道自己所没有学会的东西，每月不忘记已经学会的东西，这样就可以称得上好学了。「亡」通「无」读 wú，指还没学会的。天天进一点新的，月月守一点旧的，学问才留得住。学新如进账，温故如存钱。" name="description"/>
<meta content="日知其所亡 · 天天学新的，月月别丢旧的 · 国学课堂" property="og:title"/>
<meta content="《论语·子张》第五章精讲：学新如进账，温故如存钱" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/466-ri-zhi-qi-suo-wang/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/466-ri-zhi-qi-suo-wang/index.html" rel="canonical"/>
<title>日知其所亡 · 天天学新的，月月别丢旧的 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=zhangz466" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=zhangz466" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">日知其所亡</h2><div class="cover-ornament"></div><p class="cover-subtitle">天天学新的，月月别丢旧的</p><p class="cover-desc">这是<strong>《论语·子张》第五章</strong>。<strong>子夏</strong>说：<strong>每天</strong>知道一点自己<strong>还没学会的</strong>，<strong>每月</strong>不忘记自己<strong>已经学会的</strong>，这样就能称得上<strong>好学</strong>了。<strong>学新如进账，温故如存钱。</strong></p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:20px 18px 16px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>子夏说：每天知道自己所没有学会的东西，每月不忘记自己已经学会的东西，这样就可以称得上好学了。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《子张》第五章</strong>；<strong>合章本作 19.5</strong>；<strong>「亡」通「无」，读 wú，指还没学会的</strong>；<strong>「好」读 hào，是爱好</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>天天进，月月存。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">日知其所亡</span>：<strong>每天知道自己所没有的</strong>——<strong>「亡」通「无」，读 wú</strong>。</p><p><span class="ds-highlight">月无忘其所能</span>：<strong>每月不忘记已经学会的</strong>——<strong>会的东西也要保养</strong>。</p><p><span class="ds-highlight">可谓</span>：<strong>可以称得上</strong>——<strong>「谓」是叫作、称作</strong>。</p><p><span class="ds-highlight">好学</span>：<strong>爱好学习</strong>——<strong>「好」读 hào</strong>。</p><p><span class="ds-highlight">也已矣</span>：<strong>三个语气词连用</strong>——<strong>把肯定的口气说足</strong>。</p><p><span class="ds-highlight">所亡 / 所能</span>：<strong>一对相对的词</strong>——<strong>一个是没学会的，一个是已学会的</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>进了账，还得存得住。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：日知其所亡</h2><h3>“ 日 知 其 所 亡 ”</h3><p style="margin:0"><strong>「所亡」指什么？</strong><br/><br/>① <strong>「亡」通「无」，还没学会的东西</strong><br/>② <strong>不是丢失，是还没有</strong><br/><br/><strong>一句话：先知道自己缺什么。</strong></p><p><strong>「日知」要紧在哪？</strong><br/><br/>① <strong>每天添一点新的，不欠账</strong><br/>② <strong>今天的事今天清</strong><br/><br/><strong>一句话：账天天清，才不积压。</strong></p><p><strong>怎么做到？</strong><br/><br/>① <strong>记下不会的，去弄懂</strong><br/>② <strong>不懂装懂，账越欠越多</strong><br/><br/><strong>一句话：承认不会，是学会的第一步。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：月无忘其所能</h2><h3>“ 月 无 忘 其 所 能 ”</h3><p style="margin:0"><strong>「所能」指什么？</strong><br/><br/>① <strong>已经学会、能做到的</strong><br/>② <strong>学过不等于留着</strong><br/><br/><strong>一句话：学到手，还会溜走。</strong></p><p><strong>为什么用「月」？</strong><br/><br/>① <strong>每月盘一次账</strong><br/>② <strong>学了就忘，等于没学</strong><br/><br/><strong>一句话：温故不是虚话，是每月的功课。</strong></p><p><strong>怎么温？</strong><br/><br/>① <strong>隔段时间回头背一背、做一做</strong><br/>② <strong>能教别人一遍，记得最牢</strong><br/><br/><strong>一句话：会的东西也要保养。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：可谓好学也已矣</h2><h3>“ 可 谓 好 学 也 已 矣 ”</h3><p style="margin:0"><strong>什么叫「好学」？</strong><br/><br/>① <strong>「好」读 hào，是爱好</strong><br/>② <strong>不是读得多，是进得来、留得住</strong><br/><br/><strong>一句话：好学看的是日积月累。</strong></p><p><strong>孔门怎么评「好学」？</strong><br/><br/>① <strong>孔子夸颜回「不迁怒，不贰过」</strong><br/>② <strong>夸的都是习惯，不是聪明</strong><br/><br/><strong>一句话：好学是管住自己，天天做。</strong></p><p><strong>为什么加三个语气词？</strong><br/><br/>① <strong>「也已矣」把口气说足</strong><br/>② <strong>子夏说得斩钉截铁，没有第二条</strong><br/><br/><strong>一句话：做到这两条，就配叫好学。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：整章连起来读</h2><h3>“ 日 知 所 亡 …… 好 学 也 已 矣 ”</h3><p style="margin:0"><strong>一进一出怎么连？</strong><br/><br/>① <strong>日知是进，月无忘是守</strong><br/>② <strong>只进不守会漏，只守不进会停</strong><br/><br/><strong>一句话：进和守，缺一样都不算。</strong></p><p><strong>和颜回那课怎么呼应？</strong><br/><br/>① <strong>颜回「不贰过」，是不重犯错</strong><br/>② <strong>子夏「日知月无忘」，是不漏账</strong><br/><br/><strong>一句话：好学都是管自己。</strong></p><p><strong>整章记一句什么？</strong><br/><br/>① <strong>学新如进账，温故如存钱</strong><br/>② <strong>光赚不存，到手就漏</strong><br/><br/><strong>一句话：天天进，月月存。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「学」</h2><p>一句话，三层意思——</p><h3>“学新的，守旧的，才算好学。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>一进一出——日知添新，月无忘守旧。</p><p>🔁 一进一出</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>学问像钱袋，光赚不存，到手就漏。</p><p>👛 光赚还得存</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>好学不是读得多，是进得来、留得住。</p><p>🧮 落点是「留得住」</p>
<p>接 465 课：<strong>上一章讲做事要拣，这一章讲学了怎么留住</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「亡」是死亡的亡吗？</h3><p><strong>不是。这里通「无」，读 wú。</strong><br/><br/>① <strong>指还没学会的东西</strong><br/>② <strong>不是丢掉了什么</strong><br/>③ <strong>先知道自己缺什么，才谈得上补</strong><br/><br/><strong>记法：亡是无，不是死。</strong></p><h3>❓ 每天学多少算够？</h3><p><strong>不在多，在不断。</strong><br/><br/>① <strong>一天弄懂一点就够</strong><br/>② <strong>怕的是三天打鱼两天晒网</strong><br/>③ <strong>账天天清，才不积压</strong><br/><br/><strong>记法：天天进，不怕少。</strong></p><h3>❓ 学过又忘了怎么办？</h3><p><strong>定期回头盘账。</strong><br/><br/>① <strong>「月无忘」就是每月温一次</strong><br/>② <strong>背一背、做一做、教教别人</strong><br/>③ <strong>忘了再捡，比不捡强</strong><br/><br/><strong>记法：忘了就捡，别嫌麻烦。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📥 天天进一点</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>每天弄懂一个新词、一道题</strong>；<strong>不懂就记下来去弄懂</strong>。</p><p>💾 月月盘一次</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>隔一阵把学过的回头背背做做</strong>；<strong>会的东西也要保养</strong>。</p><p>🎯 别懂装懂</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不会装会，账越欠越多</strong>；<strong>承认不会，才是学的第一步</strong><br/><br/><strong>本章的落点：进了账，还得存得住。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「日知其所亡」。记牢：<strong>学新的，守旧的，才算好学。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                日知其所亡，月无忘其所能，可谓好学也已矣。
            </p><p>回顾本课要点:</p><p>日知所亡 · 天天进一点</p><br/><p><strong>先知道自己缺什么。</strong></p><p>月无忘所能 · 月月存一次</p><br/><p><strong>会的东西也要保养。</strong></p><p>可谓好学 · 进得来留得住</p><br/><strong>好学看的是日积月累。</strong><p><strong>在全篇中的位置:</strong>这是<strong>《子张》第五章</strong>。接 465 课：上一章讲做事要拣，这一章讲学了怎么留住。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>日知其所亡，月无忘其所能，可谓好学也已矣。</p>
</div><p><strong>课后小挑战:</strong>① 今天就记下一个你不会的东西，去弄懂它。② 背一句：日知其所亡，月无忘其所能。</p><p><strong>把这一章记在心里:</strong><strong>天天进，月月存。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “日知其所亡，月无忘其所能。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·子张》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '466-ri-zhi-qi-suo-wang';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《子张》', '《微子》', '《泰伯》'], ans: 0, exp: '这是《子张》第五章，子夏的话'},
  {q: '2. 「日知其所亡」的「亡」读什么？', opts: ['wú，通「无」', 'wáng，死亡', 'fāng，逃亡'], ans: 0, exp: '亡通无，指还没学会的东西'},
  {q: '3. 「所亡」指什么？', opts: ['还没学会的东西', '丢失的东西', '死亡的人'], ans: 0, exp: '亡通无，所亡就是自己所没有学会的'},
  {q: '4. 「月无忘其所能」的「所能」指什么？', opts: ['已经学会的', '还没学会的', '别人的本领'], ans: 0, exp: '所能是自己已经学会、能做到的'},
  {q: '5. 「好学」的「好」读什么？', opts: ['hào，爱好', 'hǎo，好的', 'háo，号叫'], ans: 0, exp: '好读 hào，是爱好的意思'},
  {q: '6. 「也已矣」是什么？', opts: ['三个语气词连用', '一个人名', '一句话的意思'], ans: 0, exp: '也已矣是语气词连用，把肯定的口气说足'},
  {q: '7. 子夏认为怎样才算好学？', opts: ['每天学点新的，每月温习旧的', '书读得越多越好', '只学喜欢的'], ans: 0, exp: '日知所亡加月无忘所能，进得来留得住'},
  {q: '8. 「日知其所亡」的意思是？', opts: ['每天知道自己所没有学会的', '每天知道自己丢了什么', '每天都要知道结果'], ans: 0, exp: '日知是每天知道，所亡是没学会的东西'},
  {q: '9. 本章与 125 课颜回「好学」的呼应在哪？', opts: ['都在讲日积月累、管住自己', '都在讲祭祀', '都在讲交朋友'], ans: 0, exp: '颜回不贰过是改错，日知月无忘是不漏账，好学都是管自己'},
  {q: '10. 本章与 465 课的关系是？', opts: ['465 讲拣事，466 讲留住学问', '是同一章的两半', '都在讲手艺'], ans: 0, exp: '465 说不钻小道，466 说学新温故，接着讲治学'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=zhangz466"></script><script src="../../assets/js/slide-engine.js?v=zhangz466"></script>
<script src="../../assets/js/speech.js?v=zhangz466"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=zhangz466"></script>
<script defer="" src="../../assets/js/auth.js?v=zhangz466"></script>
<script defer="" src="../../assets/js/api-client.js?v=zhangz466"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '466-ri-zhi-qi-suo-wang')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
