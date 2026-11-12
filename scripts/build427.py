# -*- coding: utf-8 -*-
"""生成第 427 课《季氏》第十二章「齐景公有马千驷」课件。
原文逐字 ruby 由拼音表生成，避免手写漏字。
"""
import io
import os
import re

PY = """
齐qí 景jǐng 公gōng 有yǒu 马mǎ 千qiān 驷sì ， ||
死sǐ 之zhī 日rì ， 民mín 无wú 德dé 而ér 称chēng 焉yān 。 ||
伯bó 夷yí 、 叔shū 齐qí 饿è 于yú 首shǒu 阳yáng 之zhī 下xià ， ||
民mín 到dào 于yú 今jīn 称chēng 之zhī 。 其qí 斯sī 之zhī 谓wèi 与yú ？
"""

HAN_RT = re.compile(r'^([\u4e00-\u9fff])([a-zA-Zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜüńňǹ]+)$')

FS = '2.2rem'  # 本科原文四行，字号行距与 422~426 课一致
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
<meta content="《论语·季氏》第十二章精讲：齐景公有马千驷，死之日，民无德而称焉。伯夷、叔齐饿于首阳之下，民到于今称之。齐景公富到四千匹马，死了没人念他好；伯夷叔齐饿死在山下，百姓到今天还称赞。孔子在这里比的不是钱，是人留下什么。" name="description"/>
<meta content="齐景公有马千驷 · 有钱没念想，饿死有人记 · 国学课堂" property="og:title"/>
<meta content="《论语·季氏》第十二章精讲：有钱没念想，饿死有人记" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/427-qi-jing-gong-you-ma-qian-si/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/427-qi-jing-gong-you-ma-qian-si/index.html" rel="canonical"/>
<title>齐景公有马千驷 · 有钱没念想饿死有人记 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=jishi427" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=jishi427" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">齐景公有马千驷</h2><div class="cover-ornament"></div><p class="cover-subtitle">有钱没念想，饿死有人记</p><p class="cover-desc">这是<strong>《论语·季氏》第十二章</strong>。前一章说学好要急，这一章讲<strong>人走了以后留下什么</strong>。齐国国君有四千匹马，死的那天百姓想不出他有什么好；伯夷、叔齐饿死在首阳山下，百姓到今天还念着他们。<strong>孔子没讲大道理，就摆了两件实事</strong>。</p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:8px;">原文呈现</h2><div class="ds-quote" style="margin:10px 0;padding:26px 30px 24px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>齐景公有四千匹马，他死的那天，百姓找不出他有什么德行可以称赞。伯夷、叔齐饿死在首阳山下，百姓到今天还称赞他们。说的就是这个意思吧</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>背景</strong>：<strong>按站内分法，这是《季氏》第十二章</strong>；<strong>合章本多作 16.12</strong>；<strong>「驷」是四匹马，千驷就是四千匹</strong>；<strong>上一章讲追赶，这一章讲留下</strong>。</p><p style="font-size:0.85rem;line-height:1.55;width:100%;max-width:none"><strong>小记</strong>：<strong>有钱不等于有人念</strong>。</p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 七个关节</h2><p><span class="ds-highlight">千驷</span>：<strong>四匹马驾一辆车叫一驷</strong>——<strong>千驷就是四千匹马</strong>。</p><p><span class="ds-highlight">无德而称</span>：<strong>没有德行可以称赞</strong>——<strong>不是百姓恨他，是没得可念</strong>。</p><p><span class="ds-highlight">伯夷、叔齐</span>：<strong>商朝末年孤竹君的两个儿子</strong>——<strong>让位、拦车、不食周粟</strong>。</p><p><span class="ds-highlight">饿于首阳之下</span>：<strong>饿死在首阳山下</strong>——<strong>不是被杀，是自己不肯吃</strong>。</p><p><span class="ds-highlight">到于今</span>：<strong>一直到今天</strong>——<strong>从商末到孔子，五百多年</strong>。</p><p><span class="ds-highlight">称之</span>：<strong>称赞他们</strong>——<strong>念的是他们的志</strong>。</p><p><span class="ds-highlight">其斯之谓与</span>：<strong>大概说的就是这个吧</strong>——<strong>「与」读 yú，同「欤」</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>比的是身后，不是身前</strong>。</p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：齐景公有马千驷</h2><h3>“ 齐 景 公 有 马 千 驷 ”</h3><p style="margin:0"><strong>「千驷」是多少？</strong><br/><br/>① <strong>四匹马驾一辆车，叫一驷</strong><br/>② <strong>千驷就是四千匹马</strong><br/><br/><strong>一句话：这是极言其富，不是数马。</strong></p><p><strong>齐景公是谁？</strong><br/><br/>① <strong>齐国国君，在位五十八年</strong><br/>② <strong>有国、有兵、有宫室，日子极阔</strong><br/><br/><strong>一句话：论阔，当时没几个人比得上他。</strong></p><p><strong>为什么先摆他的富？</strong><br/><br/>① <strong>先把最让人羡慕的摆出来</strong><br/>② <strong>后面才好反衬</strong><br/><br/><strong>一句话：先说有多少，再说留下什么。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：民无德而称焉</h2><h3>“ 死 之 日 ， 民 无 德 而 称 焉 ”</h3><p style="margin:0"><strong>「无德而称」怎么讲？</strong><br/><br/>① <strong>百姓找不出他有什么德行可称赞</strong><br/>② <strong>不是骂他坏，是没得可念</strong><br/><br/><strong>一句话：不是招人恨，是没人想得起。</strong></p><p><strong>有钱为什么没人念？</strong><br/><br/>① <strong>钱是他自己的，跟百姓不相干</strong><br/>② <strong>能被人记住的，是对人的好</strong><br/><br/><strong>一句话：富不等于恩。</strong></p><p><strong>这句重不重？</strong><br/><br/>① <strong>一国之君，死后无声</strong><br/>② <strong>孔子不下评语，只讲事实</strong><br/><br/><strong>一句话：人走了，念想留下来才算数。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：饿于首阳之下</h2><h3>“ 伯 夷 、 叔 齐 饿 于 首 阳 之 下 ”</h3><p style="margin:0"><strong>这两个人是谁？</strong><br/><br/>① <strong>商朝末年孤竹君的两个儿子</strong><br/>② <strong>一个让国，一个拦车，都不食周粟</strong><br/><br/><strong>一句话：让国、谏君、守志，一样没让。</strong></p><p><strong>「饿」是什么结局？</strong><br/><br/>① <strong>躲进首阳山，采野菜，最后饿死</strong><br/>② <strong>不是被杀，是自己不肯吃</strong><br/><br/><strong>一句话：他们不是没饭吃，是不肯吃。</strong></p><p><strong>一个国君、两个饿死的人，怎么比？</strong><br/><br/>① <strong>不比活着，比死后</strong><br/>② <strong>不比手里有多少，比心里有什么</strong><br/><br/><strong>一句话：活着谁高谁低，走了才见分晓。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：民到于今称之</h2><h3>“ 民 到 于 今 称 之 。 其 斯 之 谓 与 ？ ”</h3><p style="margin:0"><strong>「到于今」有多久？</strong><br/><br/>① <strong>从商末到孔子，五百多年</strong><br/>② <strong>到孔子那时候，百姓还念着</strong><br/><br/><strong>一句话：念得越久，越见分量。</strong></p><p><strong>「其斯之谓与」是什么意思？</strong><br/><br/>① <strong>大概说的就是这个吧</strong><br/>② <strong>「与」读 yú，同「欤」，是推测的语气</strong><br/><br/><strong>一句话：孔子不下断语，让人自己想。</strong></p><p><strong>孔子到底在比什么？</strong><br/><br/>① <strong>比富与德，谁留得住</strong><br/>② <strong>比一时的势与长久的名</strong><br/><br/><strong>一句话：留钱不如留德。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看留下</h2><p>这一章摆了两件事，一层比一层明白——</p><h3>“齐景公有马千驷，民无德而称焉”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>富：</strong>四千匹马，死后无声。</p><p>📜 有钱是他自己的，跟旁人无关</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>德：</strong>饿死山下，至今被称。</p><p>⏳ 让国守志，百姓记了五百多年</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>问：</strong>「其斯之谓与」。</p><p>🤐 孔子不点破，留一句反问</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>位置：</strong>《季氏》第十二章，<strong>承上章讲什么留得住</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 齐景公真有四千匹马吗？</h3><p><strong>不必当实数看。</strong><br/><br/>① <strong>古书里讲富，常用整数形容</strong><br/>② <strong>重点不在马数，在「极富」二字</strong><br/>③ <strong>他确实是一国之君，日子极阔</strong><br/><br/><strong>记法：读这一句，读的是「富」，不是账。</strong></p><h3>❓ 伯夷、叔齐为什么不吃饭？</h3><p><strong>不是不吃，是不肯吃周朝的粮。</strong><br/><br/>① <strong>他们认为武王伐纣是以暴易暴</strong><br/>② <strong>劝不住，就躲进首阳山</strong><br/>③ <strong>采野菜过日子，最后饿死</strong><br/><br/><strong>记法：守的是心里的那条线。</strong></p><h3>❓ 小孩怎么用这一章？</h3><p><strong>记住一句话就够。</strong><br/><br/>① <strong>别人记住你的，不会是你有多少</strong><br/>② <strong>是你帮过谁、说过什么话</strong><br/>③ <strong>想让人念着，先做让人念的事</strong><br/><br/><strong>记法：留下好，比留下多更要紧。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>📜 别拿家底当脸面</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>日子过得好，是好事</strong>；<strong>但别把「我有什么」挂在嘴边</strong>。</p><p>⏳ 想想自己留下什么</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>帮过人、教过人、说过暖话</strong>；<strong>这些才是别人记得住的</strong>。</p><p>🤝 守得住的那条线，别松</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>伯夷、叔齐穷到饿死也没松口</strong>；<strong>我们不至此，但道理一样</strong><br/><br/><strong>本章的落点：留钱不如留德。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了《季氏》「齐景公有马千驷」。记牢：<strong>留钱不如留德。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                齐景公有马千驷，死之日，民无德而称焉。
            </p><p>回顾本课要点:</p><p>富 · 死后无声</p><br/><p><strong>有钱是他自己的，跟旁人无关。</strong></p><p>德 · 至今被称</p><br/><p><strong>让国守志，百姓记了五百多年。</strong></p><p>问 · 其斯之谓与</p><br/><p><strong>孔子不点破，留一句反问。</strong></p><p><strong>在全篇中的位置:</strong>这是<strong>《季氏》第十二章</strong>；与 426 课连读——<strong>那课讲追着学，这课讲留得下</strong>。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>齐景公有马千驷，死之日，民无德而称焉。</p>
</div><p><strong>课后小挑战:</strong>① 想一想：今年你帮过谁，谁还记得。② 背一句：民到于今称之。</p><p><strong>把这一章记在心里:</strong><strong>有钱不等于有人念。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “齐景公有马千驷，死之日，民无德而称焉！”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·季氏》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '427-qi-jing-gong-you-ma-qian-si';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《季氏》', '《卫灵公》', '《阳货》'], ans: 0, exp: '按站内分法，这是《季氏》第十二章'},
  {q: '2. 「千驷」的「驷」是什么意思？', opts: ['四匹马驾一辆车', '一匹马', '马厩'], ans: 0, exp: '千驷就是四千匹马'},
  {q: '3. 「齐景公有马千驷」说的是什么？', opts: ['他极富', '他会养马', '他爱打仗'], ans: 0, exp: '这是极言其富，不是数马'},
  {q: '4. 「民无德而称焉」是什么意思？', opts: ['百姓找不出他有什么德行可称赞', '百姓不给他谥号', '百姓没有德行称赞他'], ans: 0, exp: '不是招人恨，是没人想得起'},
  {q: '5. 伯夷、叔齐是什么人？', opts: ['商朝末年孤竹君的两个儿子', '齐景公的两个臣子', '孔子的两个学生'], ans: 0, exp: '让国、谏君、守志'},
  {q: '6. 「饿于首阳之下」的结局是什么？', opts: ['饿死在首阳山下', '被周武王杀了', '逃到别国去了'], ans: 0, exp: '不是没饭吃，是不肯吃'},
  {q: '7. 「民到于今称之」的「称」是什么意思？', opts: ['称赞', '称呼', '称量'], ans: 0, exp: '念的是他们的志'},
  {q: '8. 「其斯之谓与」的「与」怎么读？', opts: ['yú，同「欤」，表推测', 'yǔ，和、跟', 'yù，参与'], ans: 0, exp: '大概说的就是这个吧'},
  {q: '9. 孔子把齐景公和伯夷、叔齐放在一起，比的是什么？', opts: ['比死后谁被记住', '比谁的马多', '比谁活得久'], ans: 0, exp: '不比活着，比身后'},
  {q: '10. 本章最该记住的一句话是什么？', opts: ['留钱不如留德', '齐景公有马千驷', '伯夷叔齐饿死了'], ans: 0, exp: '有钱不等于有人念'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=jishi427"></script><script src="../../assets/js/slide-engine.js?v=jishi427"></script>
<script src="../../assets/js/speech.js?v=jishi427"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=jishi427"></script>
<script defer="" src="../../assets/js/auth.js?v=jishi427"></script>
<script defer="" src="../../assets/js/api-client.js?v=jishi427"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '427-qi-jing-gong-you-ma-qian-si')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
