#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build586: 以 585 为骨架，按行号替换文字生成第 586 课
《弟子规·余力学文》第五段：列典籍，有定处。读看毕，还原处。虽有急，卷束齐。有缺坏，就补之。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/585-fang-shi-qing/index.html"
DST_DIR = f"{ROOT}/lessons/586-lie-dian-ji"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十六课，余力学文第五段。原文：「列典籍，有定处。读看毕，还原处。'
        '虽有急，卷束齐。有缺坏，就补之。」前两句讲书要摆在固定的地方，读完看完放回原处；'
        '后两句讲即使有急事，也要把书卷起捆整齐，书有破损就随手补好。'
        '合起来：书有定位，物有始终，还要爱惜。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("列","liè"),("典","diǎn"),("籍","jí")]) + "，" + _r([("有","yǒu"),("定","dìng"),("处","chù")]) + "。", True)
 + _p(_r([("读","dú"),("看","kàn"),("毕","bì")]) + "，" + _r([("还","huán"),("原","yuán"),("处","chù")]) + "。")
 + _p(_r([("虽","suī"),("有","yǒu"),("急","jí")]) + "，" + _r([("卷","juǎn"),("束","shù"),("齐","qí")]) + "。")
 + _p(_r([("有","yǒu"),("缺","quē"),("坏","huài")]) + "，" + _r([("就","jiù"),("补","bǔ"),("之","zhī")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="列典籍有定处，有缺坏就补之 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十六课：书有固定位置，读完放回原处；有急事也把书捆整齐，破了就补。物有定位。余力学文第五段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/586-lie-dian-ji/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/586-lie-dian-ji/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 列典籍有定处 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">归位</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文第五段：列典籍，有定处</p>'
      '<p class="cover-desc">书有固定位置，找得着、丢不了；读完看完，放回原处。'
      '就算有急事，也要把书卷好捆整齐；书破了，随手补一补。'
      '一句话：物有定位，用完归位。</p><div class="cover-seal">书</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文第五段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>书籍要摆放整齐，各有固定的地方。读完、看完了，放回原来那个地方。'
      '即使有急事，也要把书卷起来捆整齐；书有缺页破损，就随手补好它。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「列」是排列、摆放；「典籍」是重要的书籍；「定处」是固定的位置；'
      '「处」读 chù，是地方，不读 chǔ；「毕」是完；'
      '「还」读 huán，是放回，不是「还有」的 hái；'
      '「虽」是即使；「卷」读 juǎn，是卷起来；「束」是捆好；「齐」是整齐；'
      '「缺」是缺页；「就」是随手、立刻；「之」就是那本破损的书。'
      '这一段接着上一段：地方干净、字端正之后，连书怎么放、怎么收、怎么补，都有规矩。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>列典籍，有定处；读看毕，还原处；虽有急，卷束齐；有缺坏，就补之。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 书的三条规矩</h2>'
      '<p style="margin:0"><strong>第一条：有定处</strong><br/>'
      '① <strong>每本书都有它的位置</strong><br/>'
      '② <strong>位置固定，一伸手就找到</strong><br/><br/>'
      '<strong>一句话：有定位，不丢书。</strong></p>'
      '<p><strong>第二条：用完归位</strong><br/>'
      '① <strong>读完放回原处</strong><br/>'
      '② <strong>有急事也先收好</strong><br/><br/>'
      '<strong>一句话：有始有终。</strong></p>'
      '<p><strong>第三条：破了就补</strong><br/>'
      '① <strong>缺页、破皮，随手补</strong><br/>'
      '② <strong>不爱惜，下次就没了</strong><br/><br/>'
      '<strong>一句话：爱惜才有得用。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>列典籍，有定处；读看毕，还原处</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>典籍：书籍；定处：固定位置，处读 chù</strong><br/>'
      '② <strong>毕：完；还 huán：放回，不读 hái</strong><br/><br/>'
      '<strong>一句话：看完就归位。</strong></p>'
      '<p><strong>列典籍，有定处</strong><br/>'
      '① <strong>课本一堆、课外书一堆，各有各层</strong><br/>'
      '② <strong>定好位置，下次不用满屋找</strong><br/><br/>'
      '<strong>一句话：位置定，心不慌。</strong></p>'
      '<p><strong>读看毕，还原处</strong><br/>'
      '① <strong>看完随手一放，下回就找不着</strong><br/>'
      '② <strong>放回原处，是给下一个用的人留方便</strong><br/><br/>'
      '<strong>一句话：归位只需三秒。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>虽有急，卷束齐；有缺坏，就补之</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>虽：即使；卷 juǎn：卷起来；束：捆好</strong><br/>'
      '② <strong>缺：缺页破损；就：随手、立刻；之：那本书</strong><br/><br/>'
      '<strong>一句话：急也要收好。</strong></p>'
      '<p><strong>虽有急，卷束齐</strong><br/>'
      '① <strong>妈妈喊吃饭，书摊一桌就走</strong><br/>'
      '② <strong>回来一看，书折了、页卷了</strong><br/><br/>'
      '<strong>一句话：收一下，少损失。</strong></p>'
      '<p><strong>有缺坏，就补之</strong><br/>'
      '① <strong>角破了粘一粘，页掉了夹回去</strong><br/>'
      '② <strong>小破不补，越用越烂</strong><br/><br/>'
      '<strong>一句话：小补省大修。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 从放到补</h2>'
      '<p style="margin:0"><strong>放有定处</strong><br/>'
      '① <strong>书包分区：课本一层、本子一层</strong><br/>'
      '② <strong>书架分层：常用的放手边</strong><br/><br/>'
      '<strong>一句话：先定位置。</strong></p>'
      '<p><strong>收有始终</strong><br/>'
      '① <strong>看完一本，合上归位</strong><br/>'
      '② <strong>出门前看一眼桌子</strong><br/><br/>'
      '<strong>一句话：收尾三秒钟。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>今天给自己的书定三个位置</strong><br/>'
      '② <strong>找出最破的一本，把它补好</strong><br/><br/>'
      '<strong>一句话：定位、归位、补位。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句三步</h2>'
      '<p style="margin:0"><strong>前两句：放与还</strong><br/>'
      '① <strong>列典籍，有定处——摆有定位</strong><br/>'
      '② <strong>读看毕，还原处——用完归位</strong><br/><br/>'
      '<strong>一句话：定。</strong></p>'
      '<p><strong>后两句：收与补</strong><br/>'
      '① <strong>虽有急，卷束齐——急也收好</strong><br/>'
      '② <strong>有缺坏，就补之——破就补好</strong><br/><br/>'
      '<strong>一句话：惜。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>书有定处，用完归位</strong><br/>'
      '② <strong>急也收好，破就补好</strong><br/><br/>'
      '<strong>一句话：定位、归位、惜书。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 物有定位</h2>'
      '<p>四句话，三条规矩——</p>'
      '<h3>"列典籍，有定处。读看毕，还原处。虽有急，卷束齐。有缺坏，就补之。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>书有固定位置，'
      '读完放回，破了就补。</p><p>📖 定处</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>东西归位，是做事有头有尾；'
      '爱惜书本，是心里有分寸。</p><p>💡 归位</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>物有定位；'
      '用完归位，破了就补。</p><p>🌱 有始终</p>'),
 72: '<p>这是「余力学文课堂」第四十六课：余力学文第五段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 书放在固定位置，有什么好处？</h3>'
       '<p><strong>找得快，也丢不了。</strong><br/><br/>'
       '① <strong>书包分区：课本一层、本子一层、水杯一侧</strong><br/>'
       '② <strong>书架分层：常用的放手边，不常用的放高处</strong><br/>'
       '③ <strong>记法：位置定了，心就不乱。</strong></p>'
       '<h3>❓ 真有急事，来不及收怎么办？</h3>'
       '<p><strong>两三秒的事，做得到。</strong><br/><br/>'
       '① <strong>合上书、插回原位，转身就走</strong><br/>'
       '② <strong>真来不及，至少合上放平，别摊着</strong><br/>'
       '③ <strong>回来第一件事，就是归位</strong></p>'
       '<h3>❓ 书坏了谁来补？</h3>'
       '<p><strong>小的自己补，大的交老师。</strong><br/><br/>'
       '① <strong>角破了、页松了，胶带粘一粘</strong><br/>'
       '② <strong>缺页、脱胶，交给老师或图书馆，别自己硬撕</strong><br/>'
       '③ <strong>记法：能补就补，不能补就说。</strong></p>'
       '<h3>❓ 借来的书、电子的书怎么办？</h3>'
       '<p><strong>借的更要紧，更要不折角。</strong><br/><br/>'
       '① <strong>借的书看完按原样放回，不折角、不写字</strong><br/>'
       '② <strong>平板上的书：文件归到固定文件夹，别乱删</strong><br/>'
       '③ <strong>记法：不是自己的，更要经心。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 给书定位置</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>书包和书架都分好区，贴上小标签</strong>；'
       '<strong>这就是「列典籍，有定处」</strong>。</p><p>💡 看完就归位</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>每读完一本，立刻放回原处</strong>；'
       '<strong>这就是「读看毕，还原处」</strong>。</p><p>🌱 补一本破书</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>找出最破的一本，用胶带补好</strong>；'
       '<strong>这就是「有缺坏，就补之」</strong><br/><br/>'
       '<strong>本课的落点：物有定位。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲书的三条规矩：有定处、用完归位、破了就补。记牢：<strong>物有定位</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">列典籍，有定处。读看毕，还原处。'
       '虽有急，卷束齐。有缺坏，就补之。</p><p>回顾本课要点:</p>'
       '<p>余力学文第五段 · 三条规矩。<strong>物有定位</strong>。</p>'
       '<p>列典籍，有定处 · 书有固定位置。<strong>一伸手就找到</strong>。</p>'
       '<p>读看毕，还原处 · 用完归位。<strong>三秒钟的事</strong>。</p>'
       '<p>虽有急，卷束齐 · 急也收好。<strong>有始有终</strong>。</p>'
       '<p>有缺坏，就补之 · 破就补好。<strong>小补省大修</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>余力学文第五段；上一段讲地方和字，'
       '这一段讲书怎么放、怎么收、怎么补。</p>'
       '<div class="ds-quote">'),

 111: '<p>列典籍，有定处。读看毕，还原处。虽有急，卷束齐。有缺坏，就补之。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「定处」「毕」「还」「束」怎么讲。'
       '② 今天给书包和书架分区，定三个位置。'
       '③ 想一想：你有没有因为乱放而找不着的书。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>列典籍，有定处；读看毕，还原处；'
       '虽有急，卷束齐；有缺坏，就补之。</strong></p></div>'),

 119: '            "列典籍，有定处。读看毕，还原处。虽有急，卷束齐。有缺坏，就补之。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '586-lie-dian-ji';",

 59: '<!-- 4. 列典籍有定处·读看毕还原处 -->',
 61: '<!-- 5. 虽有急卷束齐·有缺坏就补之 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「列典籍」的「列」是什么意思？', opts: ['排列、摆放', '列举', '列队'], ans: 0, exp: '列是摆放'},",
 "  {q: '2. 「有定处」的「处」怎么读？', opts: ['chù，地方', 'chǔ，处理', 'chú，除去'], ans: 0, exp: '处读 chù，是地方'},",
 "  {q: '3. 「读看毕」的「毕」是什么意思？', opts: ['完', '毕业', '完毕费'], ans: 0, exp: '毕是完'},",
 "  {q: '4. 「还原处」的「还」怎么读？', opts: ['huán，放回', 'hái，还有', 'huàn，还债'], ans: 0, exp: '还读 huán，放回'},",
 "  {q: '5. 「虽有急」的「虽」是什么意思？', opts: ['即使', '虽然但是', '随便'], ans: 0, exp: '虽是即使'},",
 "  {q: '6. 「卷束齐」的「束」是什么意思？', opts: ['捆好', '结束', '约束'], ans: 0, exp: '束是捆好'},",
 "  {q: '7. 「有缺坏」的「缺」是什么意思？', opts: ['缺页、破损', '缺少什么', '缺席了'], ans: 0, exp: '缺是缺页破损'},",
 "  {q: '8. 「就补之」的「就」是什么意思？', opts: ['随手、立刻', '就是', '就近'], ans: 0, exp: '就是随手立刻'},",
 "  {q: '9. 「就补之」的「之」指的是什么？', opts: ['那本有破损的书', '自己', '别的东西'], ans: 0, exp: '之指那本书'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['书有定位、用完归位、急也收好、破了就补', '书越多越好', '书不能借给别人'], ans: 0, exp: '物有定位，爱惜书本'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("585-fang-shi-qing", "586-lie-dian-ji")
    out = out.replace("yaoyue585", "yaoyue586")
    out = out.replace("第四十五课", "第四十六课")
    out = out.replace("余力学文第四段", "余力学文第五段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
