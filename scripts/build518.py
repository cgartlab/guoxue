# -*- coding: utf-8 -*-
import io, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, 'lessons', '517-xia-you-yu', 'index.html')
DST = os.path.join(BASE, 'lessons', '518-tang-fa-xia', 'index.html')

with io.open(SRC, encoding='utf-8') as f:
    html = f.read()

repls = []

# 全局：课程id 与 缓存串
repls.append(('517-xia-you-yu', '518-tang-fa-xia'))
repls.append(('yaoyue519', 'yaoyue520'))

# head description
repls.append((
'<meta content="《三字经》第二十四课精讲：夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。上一课讲了「三皇二帝」的禅让盛世，这一课顺着读史往下讲——夏商周三代的开国之君禹、汤、文王武王被称为「三王」；大禹把天下传给儿子启，「家天下」从此开始，夏朝四百年后社稷迁移。八句短语（四句六言），讲完三代的开端与「家天下」的由来。" name="description"/>',
'<meta content="《三字经》第二十五课精讲：汤伐夏，国号商。六百载，至纣亡。上一课讲了「家天下」——夏朝延续四百年后社稷迁移，亡于桀。这一课接着讲：商汤起兵讨伐夏桀，建立商朝；商朝历经约六百年，到纣王时灭亡。四句六言，讲完商朝的兴起与终结。" name="description"/>'
))

# og:title
repls.append((
'<meta content="夏有禹 · 商有汤，周文武，称三王 · 夏传子，家天下，四百载，迁夏社 · 三字经课堂" property="og:title"/>',
'<meta content="汤伐夏 · 国号商，六百载，至纣亡 · 三字经课堂" property="og:title"/>'
))

# og:description
repls.append((
'<meta content="《三字经》第二十四课：夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。" property="og:description"/>',
'<meta content="《三字经》第二十五课：汤伐夏，国号商。六百载，至纣亡。" property="og:description"/>'
))

# title
repls.append((
'<title>夏有禹 · 商有汤，周文武，称三王 · 夏传子，家天下，四百载，迁夏社 ·《三字经》国学问答 · 国学课堂</title>',
'<title>汤伐夏 · 国号商，六百载，至纣亡 ·《三字经》国学问答 · 国学课堂</title>'
))

# cover
repls.append((
'<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">夏有禹</h2><div class="cover-ornament"></div><p class="cover-subtitle">商有汤，周文武，称三王；夏传子，家天下，四百载，迁夏社</p><p class="cover-desc">上一课讲了「三皇二帝」——远古的禅让盛世。这一课顺着读史往下讲：夏朝有大禹，商朝有汤，周朝有文王武王，他们被称为「三王」，是三代的开国之君；大禹把天下传给儿子启，「家天下」从此开始，夏朝延续四百年后社稷迁移。八句短语，讲完三代的开端与世袭的由来。</p><div class="cover-seal">三字经</div></div>',
'<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div><h2 class="ds-display">汤伐夏</h2><div class="cover-ornament"></div><p class="cover-subtitle">国号商，六百载，至纣亡</p><p class="cover-desc">上一课讲了「家天下」——夏朝延续四百年后社稷迁移，亡于桀。这一课接着讲：商汤起兵讨伐夏桀，建立商朝；商朝历经约六百年，到纣王时灭亡。四句六言，讲完商朝的兴起与终结。</p><div class="cover-seal">三字经</div></div>'
))

# 原文 ruby
repls.append((
'<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0"><ruby lang="zh-Hans">夏<rt>xià</rt></ruby><ruby lang="zh-Hans">有<rt>yǒu</rt></ruby><ruby lang="zh-Hans">禹<rt>yǔ</rt></ruby>，<ruby lang="zh-Hans">商<rt>shāng</rt></ruby><ruby lang="zh-Hans">有<rt>yǒu</rt></ruby><ruby lang="zh-Hans">汤<rt>tāng</rt></ruby>。</p><p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0"><ruby lang="zh-Hans">周<rt>zhōu</rt></ruby><ruby lang="zh-Hans">文<rt>wén</rt></ruby><ruby lang="zh-Hans">武<rt>wǔ</rt></ruby>，<ruby lang="zh-Hans">称<rt>chēng</rt></ruby><ruby lang="zh-Hans">三<rt>sān</rt></ruby><ruby lang="zh-Hans">王<rt>wáng</rt></ruby>。</p><p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0"><ruby lang="zh-Hans">夏<rt>xià</rt></ruby><ruby lang="zh-Hans">传<rt>chuán</rt></ruby><ruby lang="zh-Hans">子<rt>zǐ</rt></ruby>，<ruby lang="zh-Hans">家<rt>jiā</rt></ruby><ruby lang="zh-Hans">天<rt>tiān</rt></ruby><ruby lang="zh-Hans">下<rt>xià</rt></ruby>。</p><p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0"><ruby lang="zh-Hans">四<rt>sì</rt></ruby><ruby lang="zh-Hans">百<rt>bǎi</rt></ruby><ruby lang="zh-Hans">载<rt>zǎi</rt></ruby>，<ruby lang="zh-Hans">迁<rt>qiān</rt></ruby><ruby lang="zh-Hans">夏<rt>xià</rt></ruby><ruby lang="zh-Hans">社<rt>shè</rt></ruby>。</p>',
'<p style="padding-top:0;text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0"><ruby lang="zh-Hans">汤<rt>tāng</rt></ruby><ruby lang="zh-Hans">伐<rt>fá</rt></ruby><ruby lang="zh-Hans">夏<rt>xià</rt></ruby>，<ruby lang="zh-Hans">国<rt>guó</rt></ruby><ruby lang="zh-Hans">号<rt>hào</rt></ruby><ruby lang="zh-Hans">商<rt>shāng</rt></ruby>。</p><p style="text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;margin:0.05em 0 0"><ruby lang="zh-Hans">六<rt>liù</rt></ruby><ruby lang="zh-Hans">百<rt>bǎi</rt></ruby><ruby lang="zh-Hans">载<rt>zǎi</rt></ruby>，<ruby lang="zh-Hans">至<rt>zhì</rt></ruby><ruby lang="zh-Hans">纣<rt>zhòu</rt></ruby><ruby lang="zh-Hans">亡<rt>wáng</rt></ruby>。</p>'
))

# 通译/背景/小记
repls.append((
'<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>夏朝有大禹，商朝有汤，周朝有文王武王，他们被尊为「三王」；大禹把王位传给儿子，天下成为一家的私有，夏朝历经四百年，最终社稷迁移（亡于桀）。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》在讲完三皇二帝之后，紧接着讲夏商周三代——先讲三代开国之君「三王」，再讲「家天下」的由来。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>三王开基，家天下始。</strong></p>',
'<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：<strong>商汤起兵讨伐夏桀，推翻夏朝，建立商朝；商朝历经约六百年，到纣王这一代灭亡。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：<strong>《三字经》讲完夏朝「家天下」之后，紧接着讲商朝——先讲商汤灭夏建商，再讲商朝六百年终亡于纣。</strong></p><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：<strong>汤武革命，商祚六百年。</strong></p>'
))

# 字词梳理
repls.append((
'<h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">夏有禹</span>：<strong>夏是夏朝，禹是大禹</strong>——<strong>夏朝的开国之君，治水的功臣</strong>。</p><p><span class="ds-highlight">商有汤</span>：<strong>商是商朝，汤是商汤</strong>——<strong>商朝的开国之君，灭夏建商</strong>。</p><p><span class="ds-highlight">周文武</span>：<strong>周是周朝，文是周文王，武是周武王</strong>——<strong>周朝两位开国之君</strong>。</p><p><span class="ds-highlight">称三王</span>：<strong>称是尊称，三王是夏禹、商汤、周文武</strong>——<strong>三代开国之君并称「三王」</strong>。</p><p><span class="ds-highlight">夏传子</span>：<strong>传是传给，子是儿子（启）</strong>——<strong>大禹把王位传给儿子启</strong>。</p><p><span class="ds-highlight">家天下</span>：<strong>家是当作自家，天下是江山</strong>——<strong>天下成为一姓的私有，世袭开始</strong>。</p><p><span class="ds-highlight">四百载</span>：<strong>载是年，四百载是约四百年</strong>——<strong>夏朝享国的年数</strong>。</p><p><span class="ds-highlight">迁夏社</span>：<strong>迁是迁移，社是社稷（国家）</strong>——<strong>夏朝灭亡，社稷随之迁移</strong>。</p><p><span class="ds-highlight">三王家天下</span>：<strong>三王开基，家天下承</strong>——<strong>从禅让到世袭，制度为之一变</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>夏禹商汤周文武，三代三王；禹传启，家天下。</strong></p>',
'<h2>字词梳理 · 九关节</h2><p><span class="ds-highlight">汤伐夏</span>：<strong>汤是商汤，伐是讨伐，夏是夏桀</strong>——<strong>商汤起兵讨伐夏桀</strong>。</p><p><span class="ds-highlight">国号商</span>：<strong>国号是国名，商是商朝</strong>——<strong>灭夏之后定国号为商</strong>。</p><p><span class="ds-highlight">六百载</span>：<strong>载是年，六百载是约六百年</strong>——<strong>商朝享国的年数</strong>。</p><p><span class="ds-highlight">至纣亡</span>：<strong>至是到，纣是纣王，亡是灭亡</strong>——<strong>到纣王时商朝灭亡</strong>。</p><p><span class="ds-highlight">商汤</span>：<strong>商朝开国之君</strong>——<strong>灭夏建商，顺天应人</strong>。</p><p><span class="ds-highlight">夏桀</span>：<strong>夏朝末代暴君</strong>——<strong>奢侈暴虐，失德亡国</strong>。</p><p><span class="ds-highlight">纣王</span>：<strong>商朝末代暴君</strong>——<strong>酒池肉林，重蹈桀辙</strong>。</p><p><span class="ds-highlight">汤武革命</span>：<strong>商汤周武变革天命</strong>——<strong>顺天应人，革故鼎新</strong>。</p><p><span class="ds-highlight">商祚六百年</span>：<strong>祚是国运，商朝国运约六百年</strong>——<strong>上古长寿之王朝</strong>。</p><p class="ds-caption"><strong>一句话记：</strong><strong>商汤伐桀建商，六百年至纣亡。</strong></p>'
))

# 解读一
repls.append((
'<h2>逐句解读 · 一：夏有禹，商有汤</h2><h3>“ 夏 有 禹 ， 商 有 汤 ”</h3><p style="margin:0"><strong>「夏有禹」指谁？</strong><br/><br/>① <strong>大禹，夏朝开国之君</strong><br/>② <strong>治水功成，奠定夏基</strong><br/><br/><strong>一句话：禹奠夏基。</strong></p><p><strong>「商有汤」的汤是谁？</strong><br/><br/>① <strong>商汤，商朝开国之君</strong><br/>② <strong>灭夏建商，开一代之业</strong><br/><br/><strong>一句话：汤建商基。</strong></p><p><strong>这句讲什么？</strong><br/><br/>① <strong>夏商两代，各有开基之君</strong><br/>② <strong>先举夏商，引出三王</strong><br/><br/><strong>一句话：夏商开基。</strong></p>',
'<h2>逐句解读 · 一：汤伐夏，国号商</h2><h3>“ 汤 伐 夏 ， 国 号 商 ”</h3><p style="margin:0"><strong>「汤伐夏」讲什么？</strong><br/><br/>① <strong>汤是商汤，夏是夏桀</strong><br/>② <strong>商汤起兵讨伐夏桀</strong><br/><br/><strong>一句话：汤伐夏桀。</strong></p><p><strong>「国号商」什么意思？</strong><br/><br/>① <strong>灭夏之后，定国号为商</strong><br/>② <strong>商朝由此建立</strong><br/><br/><strong>一句话：建号曰商。</strong></p><p><strong>两句的关系？</strong><br/><br/>① <strong>先灭夏，后建商</strong><br/>② <strong>因果相连，一朝既立</strong><br/><br/><strong>一句话：灭夏建商。</strong></p>'
))

# 解读二
repls.append((
'<h2>逐句解读 · 二：周文武，称三王</h2><h3>“ 周 文 武 ， 称 三 王 ”</h3><p style="margin:0"><strong>「周文武」是谁？</strong><br/><br/>① <strong>周文王、周武王</strong><br/>② <strong>周朝两位开国之君</strong><br/><br/><strong>一句话：周室开基。</strong></p><p><strong>为何称「三王」？</strong><br/><br/>① <strong>禹、汤、文武，三代开国之君并称</strong><br/>② <strong>功在天下，万世景仰</strong><br/><br/><strong>一句话：三王并称。</strong></p><p><strong>与前句的关系？</strong><br/><br/>① <strong>夏商周三代，各举其君，归于三王</strong><br/>② <strong>三代相继，同称三王</strong><br/><br/><strong>一句话：三代三王。</strong></p>',
'<h2>逐句解读 · 二：六百载</h2><h3>“ 六 百 载 ”</h3><p style="margin:0"><strong>「六百载」指谁？</strong><br/><br/>① <strong>商朝，享国约六百年</strong><br/>② <strong>历时久远</strong><br/><br/><strong>一句话：商祚六百年。</strong></p><p><strong>为什么用「载」？</strong><br/><br/>① <strong>载即年，文言记时</strong><br/>② <strong>六百年非确数，约举其长</strong><br/><br/><strong>一句话：以载纪年。</strong></p><p><strong>这句的落点？</strong><br/><br/>① <strong>再长的王朝也有终</strong><br/>② <strong>兴亡有数</strong><br/><br/><strong>一句话：长久亦亡。</strong></p>'
))

# 解读三
repls.append((
'<h2>逐句解读 · 三：夏传子，家天下</h2><h3>“ 夏 传 子 ， 家 天 下 ”</h3><p style="margin:0"><strong>「夏传子」传的是谁？</strong><br/><br/>① <strong>启，大禹的儿子</strong><br/>② <strong>禹传位给儿子启</strong><br/><br/><strong>一句话：禹传于启。</strong></p><p><strong>什么是「家天下」？</strong><br/><br/>① <strong>天下成为一家的私有</strong><br/>② <strong>世袭由此开始</strong><br/><br/><strong>一句话：家天下始。</strong></p><p><strong>这句的落点？</strong><br/><br/>① <strong>从禅让到世袭，制度一大变</strong><br/>② <strong>公天下变作家天下</strong><br/><br/><strong>一句话：世袭开端。</strong></p>',
'<h2>逐句解读 · 三：至纣亡</h2><h3>“ 至 纣 亡 ”</h3><p style="margin:0"><strong>「至纣亡」的纣是谁？</strong><br/><br/>① <strong>纣王，商朝末代暴君</strong><br/>② <strong>酒池肉林，失德亡国</strong><br/><br/><strong>一句话：纣王亡商。</strong></p><p><strong>为什么商会亡？</strong><br/><br/>① <strong>桀纣一脉，暴虐失民</strong><br/>② <strong>失民心者失天下</strong><br/><br/><strong>一句话：失民则亡。</strong></p><p><strong>这句的落点？</strong><br/><br/>① <strong>汤兴于德，纣亡于暴</strong><br/>② <strong>前后对照，因果昭然</strong><br/><br/><strong>一句话：兴亡对照。</strong></p>'
))

# 解读四
repls.append((
'<h2>逐句解读 · 四：四百载，迁夏社</h2><h3>“ 四 百 载 ， 迁 夏 社 ”</h3><p style="margin:0"><strong>「四百载」指谁？</strong><br/><br/>① <strong>夏朝，享国约四百年</strong><br/>② <strong>历时久远</strong><br/><br/><strong>一句话：夏祚四百年。</strong></p><p><strong>「迁夏社」什么意思？</strong><br/><br/>① <strong>夏亡，社稷迁移</strong><br/>② <strong>商汤灭夏，社稷易主</strong><br/><br/><strong>一句话：夏亡迁社。</strong></p><p><strong>这一句的落点？</strong><br/><br/>① <strong>再长的王朝也有终，兴衰有数</strong><br/>② <strong>居安思危，方得长久</strong><br/><br/><strong>一句话：兴衰有数。</strong></p>',
'<h2>逐句解读 · 四：合起来讲商朝兴亡</h2><h3>“ 汤 伐 夏 … 至 纣 亡 ”</h3><p style="margin:0"><strong>前两句讲什么？</strong><br/><br/>① <strong>商汤灭夏，建立商朝</strong><br/>② <strong>汤武革命，顺天应人</strong><br/><br/><strong>一句话：灭夏建商。</strong></p><p><strong>后两句讲什么？</strong><br/><br/>① <strong>商朝历经约六百年</strong><br/>② <strong>到纣王时灭亡</strong><br/><br/><strong>一句话：商祚六百年。</strong></p><p><strong>与上一课的关系？</strong><br/><br/>① <strong>上一课夏亡，这一课商兴</strong><br/>② <strong>夏商相继，兴衰有鉴</strong><br/><br/><strong>一句话：夏亡商兴。</strong></p>'
))

# 核心思想（行71-75）
repls.append((
'<h2>核心思想 · 夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社</h2><p>一句话，两层意思——</p><h3>"夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。"</h3>',
'<h2>核心思想 · 汤伐夏，国号商。六百载，至纣亡</h2><p>一句话，两层意思——</p><h3>"汤伐夏，国号商。六百载，至纣亡。"</h3>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前两句讲三代三王——禹、汤、文武，开基立业；后两句讲家天下——大禹传子，夏朝四百年后社稷迁移。</p><p>👑 三代三王</p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>前两句讲商汤灭夏、建立商朝；后两句讲商朝历经六百年，到纣王时灭亡。</p><p>👑 汤武革命</p>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>从三皇二帝的禅让，到夏的世袭，制度为之一变；兴亡有数，居安思危。</p><p>🏺 家天下</p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>从夏的世袭，到商的兴衰，王朝更迭、天命靡常；得民心者得天下。</p><p>🏺 商祚六百年</p>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>三王开基，家天下承；四百年终迁社，提醒后世居安思危。</p><p>⚖️ 兴衰有数</p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>汤兴于德，纣亡于暴；六百年终至纣亡，兴亡之鉴昭然。</p><p>⚖️ 兴亡有鉴</p>'
))
repls.append((
'<p>这是「三字经课堂」第二十四课：夏有禹，商有汤。</p>',
'<p>这是「三字经课堂」第二十五课：汤伐夏，国号商。</p>'
))

# FAQ
repls.append((
'<h2>常见问题</h2><h3>❓ 「三王」指哪三位？</h3><p><strong>是夏禹、商汤、周文王武王。</strong><br/><br/>① <strong>禹奠夏基、汤建商基、文武开周基</strong><br/>② <strong>三代开国之君并称「三王」</strong><br/>③ <strong>与「三皇二帝」不同，三王是三代之君</strong><br/><br/><strong>记法：三代三王。</strong></p><h3>❓ 「夏有禹」的禹是谁？</h3><p><strong>是大禹，夏朝的开国之君，治水的功臣。</strong><br/><br/>① <strong>禹治水十三年，三过家门不入</strong><br/>② <strong>功成受禅，奠定夏朝</strong><br/>③ <strong>非帝王本名，是尊称</strong><br/><br/><strong>记法：禹奠夏基。</strong></p><h3>❓ 什么是「家天下」？</h3><p><strong>是大禹把王位传给儿子启，天下成为一家的私有，世袭制度从此开始。</strong><br/><br/>① <strong>此前是禅让，传贤不传子</strong><br/>② <strong>此后是世袭，传子不传贤</strong><br/>③ <strong>公天下变成了家天下</strong><br/><br/><strong>记法：家天下始。</strong></p><h3>❓ 为什么要「迁夏社」？</h3><p><strong>夏桀暴虐，商汤起兵灭夏，夏的社稷随之迁移。</strong><br/><br/>① <strong>夏享国约四百年</strong><br/>② <strong>桀失德，汤顺天应人</strong><br/>③ <strong>社稷迁移，朝代易主</strong><br/><br/><strong>记法：夏亡迁社。</strong></p>',
'<h2>常见问题</h2><h3>❓ 「汤伐夏」是什么意思？</h3><p><strong>是商汤起兵讨伐夏桀，推翻夏朝。</strong><br/><br/>① <strong>汤是商朝开国之君</strong><br/>② <strong>桀是夏朝末代暴君</strong><br/>③ <strong>汤顺天应人，伐桀建商</strong><br/><br/><strong>记法：汤伐夏桀。</strong></p><h3>❓ 为什么汤能灭夏？</h3><p><strong>夏桀暴虐失德，商汤顺应民心起兵。</strong><br/><br/>① <strong>桀奢侈暴虐，众叛亲离</strong><br/>② <strong>汤宽厚得民，兵锋所指</strong><br/>③ <strong>天命靡常，唯德是辅</strong><br/><br/><strong>记法：顺天应人。</strong></p><h3>❓ 「六百载」有多长？</h3><p><strong>商朝享国约六百年。</strong><br/><br/>① <strong>非确数，约举其长</strong><br/>② <strong>商代是上古长寿王朝</strong><br/>③ <strong>历经十七世三十王</strong><br/><br/><strong>记法：商祚六百年。</strong></p><h3>❓ 「至纣亡」是什么意思？</h3><p><strong>商朝到纣王时灭亡。</strong><br/><br/>① <strong>纣是末代暴君</strong><br/>② <strong>酒池肉林，失德亡国</strong><br/>③ <strong>周武王伐纣，商亡</strong><br/><br/><strong>记法：纣亡商灭。</strong></p>'
))

# 生活应用
repls.append((
'<h2>生活应用</h2><p>这四句，给我们三样提醒——</p><p>👑 立业不易</p>',
'<h2>生活应用</h2><p>这四句，给我们三样提醒——</p><p>👑 顺天应人</p>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「夏有禹，商有汤」</strong>；<strong>三王开基不易，后人当饮水思源、敬重开创者</strong>。</p><p>🏺 公与私</p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>《三字经》说「汤伐夏，国号商」</strong>；<strong>得民心者得天下，汤以仁德取夏而代之</strong>。</p><p>🏺 兴亡有数</p>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>「家天下」提醒我们</strong>；<strong>从禅让到世袭，是制度的一大变迁，读史要懂其所以然</strong>。</p><p>⚖️ 居安思危</p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>「六百年，至纣亡」提醒我们</strong>；<strong>再长寿的王朝也会终，兴亡有数不可不察</strong>。</p><p>⚖️ 以史为鉴</p>'
))
repls.append((
'<p style="margin:var(--ds-space-1) 0 0"><strong>「四百载，迁夏社」</strong>；<strong>再稳固的位子也当警醒，居安思危方能长久</strong><br/><br/><strong>本课的落点：夏有禹，商有汤。</strong></p>',
'<p style="margin:var(--ds-space-1) 0 0"><strong>「汤伐夏，国号商」</strong>；<strong>夏桀商纣皆因暴虐亡国，读史知戒</strong><br/><br/><strong>本课的落点：汤伐夏，国号商。</strong></p>'
))

# 课程总结
repls.append((
'<h2>课程总结</h2><p>今天学了《三字经》第二十四课。记牢：<strong>夏有禹，商有汤</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">\n                夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。\n            </p><p>回顾本课要点:</p><p>夏有禹，商有汤 · 夏商两代的开国之君。<strong>三王开基。</strong></p><p>周文武，称三王 · 周朝文王武王，三代并称三王。<strong>三代三王。</strong></p><p>夏传子，家天下 · 禹传启，世袭开始。<strong>家天下始。</strong></p><p>四百载，迁夏社 · 夏亡，社稷迁移。<strong>夏亡迁社。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲「三皇二帝」，这一课讲三代三王与家天下，下一课接着讲「汤伐夏，国号商」。</p><div class="ds-quote">\n<p>📜 原文重温</p>\n<p>夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。</p>\n</div><p><strong>课后小挑战:</strong>① 把这八句背下来。② 说出「三王」是哪三位。③ 讲清「家天下」是什么意思。</p><p><strong>把这一课记在心里:</strong><strong>夏有禹，商有汤，周文武，称三王，夏传子，家天下，四百载，迁夏社。</strong></p>',
'<h2>课程总结</h2><p>今天学了《三字经》第二十五课。记牢：<strong>汤伐夏，国号商</strong>。</p><p style="text-align:center;margin:var(--ds-space-4) 0">\n                汤伐夏，国号商。六百载，至纣亡。\n            </p><p>回顾本课要点:</p><p>汤伐夏，国号商 · 商汤灭夏，建立商朝。<strong>汤武革命。</strong></p><p>六百载，至纣亡 · 商朝约六百年，到纣王灭亡。<strong>商祚六百年。</strong></p><p><strong>在全篇中的位置:</strong>上一课讲「家天下」夏亡，这一课讲商兴亡，下一课接着讲「周武王，始诛纣」。</p><div class="ds-quote">\n<p>📜 原文重温</p>\n<p>汤伐夏，国号商。六百载，至纣亡。</p>\n</div><p><strong>课后小挑战:</strong>① 把这四句背下来。② 说出商汤是谁。③ 讲清「六百载，至纣亡」的意思。</p><p><strong>把这一课记在心里:</strong><strong>汤伐夏，国号商，六百载，至纣亡。</strong></p>'
))

# 结束页
repls.append((
'            "夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。"<br/>',
'            "汤伐夏，国号商。六百载，至纣亡。"<br/>'
))

# QUIZ
repls.append((
'''const QUIZ = [
  {q: '1. 「三王」指哪三代的君主？', opts: ['夏禹、商汤、周文武', '尧、舜、禹', '天、地、人'], ans: 0, exp: '三王是夏商周开国之君'},
  {q: '2. 「夏有禹」中禹的故事？', opts: ['治水开国，夏朝始祖', '发明文字', '建立商朝'], ans: 0, exp: '大禹治水，奠定夏基'},
  {q: '3. 「周文武」是谁？', opts: ['周文王、周武王', '周成王、周康王', '周公、召公'], ans: 0, exp: '周朝两位开国之君'},
  {q: '4. 「称三王」的「王」指什么？', opts: ['三代开国之君的尊称', '皇帝', '神仙'], ans: 0, exp: '禹汤文武并称三王'},
  {q: '5. 「夏传子」传的是谁？', opts: ['启（禹的儿子）', '舜', '尧'], ans: 0, exp: '大禹传位给儿子启'},
  {q: '6. 什么是「家天下」？', opts: ['天下成一家私有，世袭开始', '天下是大家的', '分封诸侯'], ans: 0, exp: '禹传启，家天下始'},
  {q: '7. 「四百载」指哪个朝代？', opts: ['夏朝', '商朝', '周朝'], ans: 0, exp: '夏朝享国约四百年'},
  {q: '8. 「迁夏社」什么意思？', opts: ['夏亡，社稷迁移', '夏迁都', '夏建国'], ans: 0, exp: '商汤灭夏，社稷迁移'},
  {q: '9. 从上一课到这一课，制度有何变化？', opts: ['从禅让到世袭（家天下）', '从世袭到禅让', '没有变化'], ans: 0, exp: '三皇二帝禅让 → 夏家天下'},
  {q: '10. 这一课八句合起来讲什么？', opts: ['三代三王开国与家天下由来', '三皇二帝', '朝代更替全部'], ans: 0, exp: '三王开基，家天下始'},
];''',
'''const QUIZ = [
  {q: '1. 「汤伐夏」的汤是谁？', opts: ['商汤', '周武王', '尧帝'], ans: 0, exp: '商汤灭夏建商'},
  {q: '2. 「伐」是什么意思？', opts: ['讨伐、征讨', '建造', '祭祀'], ans: 0, exp: '汤起兵讨伐夏桀'},
  {q: '3. 「国号商」什么意思？', opts: ['建立商朝', '商朝的都城', '商朝的军队'], ans: 0, exp: '灭夏后定国号为商'},
  {q: '4. 夏朝被谁所灭？', opts: ['商汤', '周武王', '秦始皇'], ans: 0, exp: '汤伐夏，商取代夏'},
  {q: '5. 「六百载」指哪个朝代？', opts: ['商朝', '夏朝', '周朝'], ans: 0, exp: '商朝享国约六百年'},
  {q: '6. 「至纣亡」的纣是谁？', opts: ['商纣王（末代暴君）', '夏桀', '周幽王'], ans: 0, exp: '纣王是商朝末代暴君'},
  {q: '7. 商朝享国多久？', opts: ['约六百年', '约四百年', '约八百年'], ans: 0, exp: '六百载，约六百年'},
  {q: '8. 商朝亡于谁？', opts: ['纣王', '夏桀', '周文王'], ans: 0, exp: '至纣亡，商亡于纣'},
  {q: '9. 与上一课的关系？', opts: ['夏亡 → 商兴 → 商亡', '毫无关系', '商先夏后'], ans: 0, exp: '上一课夏亡，这一课商兴又亡'},
  {q: '10. 这四句合起来讲什么？', opts: ['商汤灭夏建商与商朝六百年兴亡', '周朝八百年', '三皇二帝'], ans: 0, exp: '汤伐夏，国号商；六百载，至纣亡'},
];'''))

# 执行替换，带断言
for i, (old, new) in enumerate(repls):
    if old not in html:
        sys.stderr.write('!! repl #%d NOT FOUND:\n%s\n\n' % (i, old[:120]))
        sys.exit(1)
    html = html.replace(old, new)

# 校验残留
for bad in ['第二十四课', '夏有禹', '商有汤', '周文武', '迁夏社', '517-xia-you-yu', 'yaoyue519']:
    if bad in html:
        sys.stderr.write('!! residual leftover: %s\n' % bad)
        sys.exit(2)

os.makedirs(os.path.dirname(DST), exist_ok=True)
with io.open(DST, 'w', encoding='utf-8') as f:
    f.write(html)
sys.stderr.write('OK wrote %s (%d bytes)\n' % (DST, len(html)))
