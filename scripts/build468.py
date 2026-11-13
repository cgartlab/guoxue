# -*- coding: utf-8 -*-
"""生成第 468 课《子张》第七章「子夏曰：小人之过也必文。」课件。
全章约 9 字、一句；短章大字版式（与 467 同基准）。
"""
import io
import os
import re

PY = """
子zǐ 夏xià 曰yuē ： ||
小xiǎo 人rén 之zhī 过guò 也yě 必bì 文wén 。 ||
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
<meta content="《论语·子张》第七章精讲：子夏曰：小人之过也必文。子夏说：小人有了过错，一定要加以掩饰。「文」读 wén，是掩饰、修饰。错不会因为遮住就消失，遮一层，错就多一层。认错不丢人，遮错才丢人。" name="description"/>
<meta content="小人之过也必文 · 有错就遮，越遮越丑 · 国学课堂" property="og:title"/>
<meta content="《论语·子张》第七章精讲：错不怕，怕的是不认" property="og:description"/>
<meta content="website" property="og:type"/>
<meta content="https://guoxue.8023laozhanshi.cc/lessons/468-xiao-ren-zhi-guo/index.html" property="og:url"/>
<link href="https://guoxue.8023laozhanshi.cc/lessons/468-xiao-ren-zhi-guo/index.html" rel="canonical"/>
<title>小人之过也必文 · 有错就遮，越遮越丑 ·《论语》国学问答 · 国学课堂</title>
<link href="../../assets/img/favicon.svg?v=zhangz468" rel="icon" type="image/svg+xml"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="../../assets/css/ds-design-system.css?v=zhangz468" rel="stylesheet"/>
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
<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">小人之过也必文</h2><div class="cover-ornament"></div><p class="cover-subtitle">有错就遮，越遮越丑</p><p class="cover-desc">这是<strong>《论语·子张》第七章</strong>。<strong>子夏</strong>说：<strong>小人</strong>有了<strong>过错</strong>，一定要加以<strong>掩饰</strong>。<strong>「文」读 wén，是修饰、遮掩</strong>。<strong>错不怕，怕的是不认。</strong></p><div class="cover-seal">论语</div></div>
<!-- 2. 原文呈现 -->
<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2 style="margin-bottom:6px;">原文呈现</h2><div class="ds-quote" style="margin:6px 0;padding:20px 18px 16px;line-height:1.7;">
{{RUBY}}
</div><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>子夏说：小人有了过错，一定要加以掩饰。</strong></p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：<strong>这是《子张》第七章</strong>；<strong>合章本作 19.7</strong>；<strong>「文」读 wén，是掩饰、修饰</strong>；<strong>「过」是过错、做错的事</strong>。</p><p style="font-size:0.78rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：<strong>错要认，遮不住。</strong></p></div>
<!-- 3. 字词梳理 -->
<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>字词梳理 · 六个关节</h2><p><span class="ds-highlight">小人</span>：<strong>不是骂人的话</strong>——<strong>指只顾面子、不肯修德的人</strong>。</p><p><span class="ds-highlight">之</span>：<strong>结构助词「的」</strong>——<strong>「小人之过」就是小人的过错</strong>。</p><p><span class="ds-highlight">过</span>：<strong>过错、做错的事</strong>——<strong>不是「经过」</strong>。</p><p><span class="ds-highlight">也</span>：<strong>语气词，停一下</strong>——<strong>把「过」字单独提出来说</strong>。</p><p><span class="ds-highlight">必</span>：<strong>一定、逃不掉</strong>——<strong>不是偶尔，是习气</strong>。</p><p><span class="ds-highlight">文</span>：<strong>读 wén，掩饰、修饰</strong>——<strong>「文过」就是给错刷层漆</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>给错刷漆，越刷越黑。</strong></p></div>
<!-- 4. 解读一 -->
<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 一：小人之过也必文</h2><h3>“ 小 人 之 过 也 必 文 ”</h3><p style="margin:0"><strong>「文」是什么意思？</strong><br/><br/>① <strong>读 wén，掩饰、修饰</strong><br/>② <strong>不是写文章，是给错找个说法</strong><br/><br/><strong>一句话：错上加一层漆。</strong></p><p><strong>为什么要「文」？</strong><br/><br/>① <strong>怕丢面子</strong><br/>② <strong>不肯认，就想法子圆过去</strong><br/><br/><strong>一句话：怕丢脸，丢得更凶。</strong></p><p><strong>「必」字说明什么？</strong><br/><br/>① <strong>一定、逃不掉</strong><br/>② <strong>这是老毛病，不是偶然一次</strong><br/><br/><strong>一句话：改不了，就成了习气。</strong></p></div>
<!-- 5. 解读二 -->
<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 二：什么叫「小人」</h2><h3>“ 小 人 之 过 ”</h3><p style="margin:0"><strong>「小人」指谁？</strong><br/><br/>① <strong>不是骂人穷，是说格局小</strong><br/>② <strong>与君子相对：君子认错，小人遮错</strong><br/><br/><strong>一句话：看认不认错，就分得清。</strong></p><p><strong>君子怎么对待过错？</strong><br/><br/>① <strong>孔子说「过则勿惮改」</strong><br/>② <strong>子贡说「君子之过，如日月之食」</strong><br/><br/><strong>一句话：错了让人看得见，改了人人仰头。</strong></p><p><strong>遮错有什么后果？</strong><br/><br/>① <strong>小错遮成大错</strong><br/>② <strong>别人再不敢信你</strong><br/><br/><strong>一句话：遮一次，信就少一分。</strong></p></div>
<!-- 6. 解读三 -->
<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 三：遮错为什么最坏事</h2><h3>“ 文 过 ”</h3><p style="margin:0"><strong>遮住了，错就没了吗？</strong><br/><br/>① <strong>错还在，只是藏起来了</strong><br/>② <strong>藏着的错，还会再犯</strong><br/><br/><strong>一句话：遮不是改。</strong></p><p><strong>别人看不出来吗？</strong><br/><br/>① <strong>话说不实，日久人人看得出</strong><br/>② <strong>纸包不住火</strong><br/><br/><strong>一句话：遮得住一时，遮不住一世。</strong></p><p><strong>那该怎么办？</strong><br/><br/>① <strong>认错、改错</strong><br/>② <strong>认得越快，改得越早</strong><br/><br/><strong>一句话：认了，才有改的机会。</strong></p></div>
<!-- 7. 解读四 -->
<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>逐句解读 · 四：整章连起来读</h2><h3>“ 小 人 之 过 也 必 文 ”</h3><p style="margin:0"><strong>一句话讲什么？</strong><br/><br/>① <strong>小人有错必遮</strong><br/>② <strong>病根在不肯认</strong><br/><br/><strong>一句话：过不在错，在遮。</strong></p><p><strong>和 467 课怎么呼应？</strong><br/><br/>① <strong>467 讲守着干才成事</strong><br/>② <strong>这章讲有了错别遮</strong><br/><br/><strong>一句话：成事靠实，做人更靠实。</strong></p><p><strong>整章记一句什么？</strong><br/><br/>① <strong>错要认，遮不住</strong><br/>② <strong>认错不丢人，遮错才丢人</strong><br/><br/><strong>一句话：认了就好。</strong></p></div>
<!-- 8. 核心思想 -->
<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span><h2>核心思想 · 三层看「过」</h2><p>一句话，三层意思——</p><h3>“错不怕，怕的是不认。”</h3>
<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>小人有错必遮——一遮，错就成了双份。</p><p>🎭 遮比错更糟</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>遮错是怕丢脸，结果脸丢得更多。</p><p>🪞 面子越护越破</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>认错是本事，改错才是收场。</p><p>🧹 落点是「认了改」</p>
<p>接 467 课：<strong>上一章讲守着本业才成事，这一章讲犯了错别遮</strong>。</p></div>
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
<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>常见问题</h2><h3>❓ 「文」是文章的文吗？</h3><p><strong>同一个字，这里当「掩饰」讲，读 wén。</strong><br/><br/>① <strong>文过，就是给过错刷层漆</strong><br/>② <strong>把黑的刷成白的</strong><br/>③ <strong>字是文的字，意思不是文章</strong><br/><br/><strong>记法：文过，就是给错化妆。</strong></p><h3>❓ 认错会不会丢面子？</h3><p><strong>遮才丢面子。</strong><br/><br/>① <strong>认错的人，别人佩服</strong><br/>② <strong>遮错的人，别人防着</strong><br/>③ <strong>认了一时难受，遮了一世不安</strong><br/><br/><strong>记法：脸是自己的，别拿它换谎话。</strong></p><h3>❓ 小错也要认吗？</h3><p><strong>越早认越省事。</strong><br/><br/>① <strong>小错不遮，大错不生</strong><br/>② <strong>小错一遮，就长出大错</strong><br/>③ <strong>认错要快，改错要实</strong><br/><br/><strong>记法：早认早轻松。</strong></p></div>
<!-- 21. 生活应用 -->
<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>生活应用</h2><p>这一章，给我们的日子三样提醒——</p><p>🙋 先认</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>错了先说「我错了」</strong>；<strong>不找理由，不绕弯子</strong>。</p><p>🔍 找根</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>问自己为什么会错</strong>；<strong>光赔个不是，下次照旧</strong>。</p><p>🚫 不刷漆</p>
<p style="margin:var(--ds-space-1) 0 0"><strong>不把错解释成「其实没错」</strong>；<strong>只想着下次不错</strong><br/><br/><strong>本章的落点：错不怕，怕的是不认。</strong></p></div>
<!-- 22. 课程总结 -->
<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span><h2>课程总结</h2><p>今天学了「小人之过也必文」。记牢：<strong>错不怕，怕的是不认。</strong></p><p style="text-align:center;margin:var(--ds-space-4) 0">
                小人之过也必文。
            </p><p>回顾本课要点:</p><p>小人之过 · 有错先想遮</p><br/><p><strong>遮比错更糟。</strong></p><p>必文 · 一定找说法</p><br/><p><strong>怕丢脸，丢得更凶。</strong></p><p>君子相反 · 认了再改</p><br/><strong>认了，才有改的机会。</strong><p><strong>在全篇中的位置:</strong>这是<strong>《子张》第七章</strong>。接 467 课：上一章讲守着本业，这一章讲犯了错别遮。</p><div class="ds-quote">
<p>📜 原文重温</p>
<p>小人之过也必文。</p>
</div><p><strong>课后小挑战:</strong>① 今天就为一件小错认个错，不解释。② 背一句：小人之过也必文。</p><p><strong>把这一章记在心里:</strong><strong>认了，才改得掉。</strong></p></div>
<!-- ====== 结束页 ====== -->
<div class="slide end-slide" data-page="23" data-section="review">
<div class="cover-ornament"></div>
<h2 class="ds-display">谢谢大家</h2>
<div class="cover-ornament"></div>
<div class="end-quote">
            “小人之过也必文。”<br/>
<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《论语·子张》</span>
</div>
<div class="cover-seal">国学</div>
</div>
</div>
</div><!-- slide-viewport -->
<script>
    window.GUOXUE_COURSE_ID = '468-xiao-ren-zhi-guo';
const QUIZ = [
  {q: '1. 本章出自《论语》的哪一篇？', opts: ['《子张》', '《卫灵公》', '《季氏》'], ans: 0, exp: '这是《子张》第七章，子夏的话'},
  {q: '2. 「必文」的「文」读什么？', opts: ['wén，掩饰', 'wèn，文章', 'mín，纹理'], ans: 0, exp: '文读 wén，这里是掩饰、修饰'},
  {q: '3. 「文」在这里的意思是什么？', opts: ['掩饰、修饰', '写文章', '有文化'], ans: 0, exp: '文过就是给过错刷层漆'},
  {q: '4. 「小人之过也必文」的「过」指什么？', opts: ['过错', '经过', '过分'], ans: 0, exp: '过是过错、做错的事'},
  {q: '5. 本章的「小人」指什么人？', opts: ['只顾面子、不肯认错的人', '个子小的人', '穷人'], ans: 0, exp: '小人不是骂人穷，是说格局小、不肯修德'},
  {q: '6. 「必」字说明什么？', opts: ['小人有错一定遮，是改不掉的习气', '偶尔遮一次', '一定会改正'], ans: 0, exp: '必是一定，遮错成了老毛病'},
  {q: '7. 「文过」这种做法错在哪？', opts: ['错没改，还添了不说实话', '字写错了', '话说得太重'], ans: 0, exp: '遮住的错还在，还会再犯'},
  {q: '8. 君子对待过错的态度是？', opts: ['认错改错，不怕人看见', '先遮住再说', '推给别人'], ans: 0, exp: '孔子说过则勿惮改，子贡说君子之过如日月之食'},
  {q: '9. 本章与 467 课的关系是？', opts: ['467 讲守着干成事，468 讲错了别遮', '是同一章的两半', '都在讲手艺'], ans: 0, exp: '467 说守本业，468 说老实做人，都讲一个实字'},
  {q: '10. 这一章给我们的提醒是？', opts: ['犯错先认，认了才改得掉', '能遮就遮', '等别人忘了就好'], ans: 0, exp: '错不怕，怕的是不认'},
];
window.GUOXUE_QUIZ_OVERRIDE = QUIZ;
</script>
<script src="../../assets/js/unlock.js?v=zhangz468"></script><script src="../../assets/js/slide-engine.js?v=zhangz468"></script>
<script src="../../assets/js/speech.js?v=zhangz468"></script>
<!-- 底部进度条 -->
<div class="progress-bar-bottom">
<div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>
<!-- 键盘提示 -->
<div class="kbd-hint">
<span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
  </div>
<script defer="" src="../../assets/js/auth-email.js?v=zhangz468"></script>
<script defer="" src="../../assets/js/auth.js?v=zhangz468"></script>
<script defer="" src="../../assets/js/api-client.js?v=zhangz468"></script>
</body>
</html>
'''


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    outdir = os.path.join(root, 'lessons', '468-xiao-ren-zhi-guo')
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    html = TEMPLATE.replace('{{RUBY}}', build_ruby_paragraphs())
    path = os.path.join(outdir, 'index.html')
    io.open(path, 'w', encoding='utf-8', newline='\n').write(html)
    print('written', path, len(html))


if __name__ == '__main__':
    main()
