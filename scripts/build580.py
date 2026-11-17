#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build580: 以 578 为骨架，按行号替换文字生成第 580 课
《弟子规·亲仁》第一段：同是人，类不齐。流俗众，仁者希。果仁者，人多畏。言不讳，色不媚。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/578-en-yu-bao/index.html"
DST_DIR = f"{ROOT}/lessons/580-tong-shi-ren"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十课，亲仁第一段。原文：「同是人，类不齐。流俗众，仁者希。'
        '果仁者，人多畏。言不讳，色不媚。」前两句讲一样是人，品类不一样，随大流的人多，'
        '真正讲仁的人少；后两句讲真正有仁德的人，人们敬重他——他说话直言不隐瞒，神色不讨好。'
        '合起来：先认得出仁者，才谈得上亲近。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("同","tóng"),("是","shì"),("人","rén")]) + "，" + _r([("类","lèi"),("不","bù"),("齐","qí")]) + "。", True)
 + _p(_r([("流","liú"),("俗","sú"),("众","zhòng")]) + "，" + _r([("仁","rén"),("者","zhě"),("希","xī")]) + "。")
 + _p(_r([("果","guǒ"),("仁","rén"),("者","zhě")]) + "，" + _r([("人","rén"),("多","duō"),("畏","wèi")]) + "。")
 + _p(_r([("言","yán"),("不","bù"),("讳","huì")]) + "，" + _r([("色","sè"),("不","bù"),("媚","mèi")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="同是人类不齐，仁者希 · 亲仁课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十课：一样是人，品类不齐；随大流的多，讲仁的少。真仁者让人敬——直言不讳，不讨好。亲仁第一段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/580-tong-shi-ren/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/580-tong-shi-ren/index.html" rel="canonical"/>',
 12: '<title>亲仁 · 同是人类不齐，仁者希 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">亲仁</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》亲仁第一段：同是人，类不齐</p>'
      '<p class="cover-desc">一样是人，可是品类不一样：随大流的多，真正讲仁的少。'
      '真正有仁德的人，人们反倒敬重他——因为他说话直，不藏着；神色正，不讨好。'
      '一句话：先认得出仁者，才谈得上亲近。</p><div class="cover-seal">仁</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 亲仁第一段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>同样都是人，品类却不一样。跟着流俗走的人多，讲仁德的人少。'
      '真要有仁德的人，人们自然敬重他：他说话不隐瞒、不绕弯，神色也不去讨好谁。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「类」是品类、种类；「不齐」是不一样、不整齐；「流俗」是随大流的风气；'
      '「众」是多；「仁者」是有仁德的人；「希」同「稀」，是少；「果」是果真、真个；'
      '「畏」是敬重、心里服气；「讳」是隐瞒、避讳；「媚」是讨好、巴结。'
      '这是《弟子规》第五门「亲仁」的第一段：前四门讲怎么做人做事，这一门讲跟谁走近——'
      '先认得出谁是仁者，才谈得上亲近。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>同是人，类不齐；流俗众，仁者希；果仁者，人多畏；言不讳，色不媚。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 人分几等，仁者难得</h2>'
      '<p style="margin:0"><strong>先说「人不一样」</strong><br/>'
      '① <strong>一样是两条腿走路，心里却差得远</strong><br/>'
      '② <strong>跟风的人多，有主见的人少</strong><br/><br/>'
      '<strong>一句话：人多不等于对。</strong></p>'
      '<p><strong>再说「仁者什么样」</strong><br/>'
      '① <strong>让人敬：不是凶，是正</strong><br/>'
      '② <strong>说话直，不藏；脸色正，不拍</strong><br/><br/>'
      '<strong>一句话：不讨好的人，才靠得住。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句：仁者少，所以难得</strong><br/>'
      '② <strong>后两句：认得出，才知道跟谁走</strong><br/><br/>'
      '<strong>一句话：先识人，再择友。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>同是人，类不齐；流俗众，仁者希</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>类：品类；不齐：不一样</strong><br/>'
      '② <strong>流俗：随大流的风气；希：同「稀」，少</strong><br/><br/>'
      '<strong>一句话：人跟人，差得远。</strong></p>'
      '<p><strong>同是人，类不齐</strong><br/>'
      '① <strong>同班的同学，有人帮人，有人使坏</strong><br/>'
      '② <strong>一样吃饭上学，心里装的不是一个东西</strong><br/><br/>'
      '<strong>一句话：先别把人想得一样。</strong></p>'
      '<p><strong>流俗众，仁者希</strong><br/>'
      '① <strong>随大流最省力，所以人多</strong><br/>'
      '② <strong>讲原则要费劲，所以人少</strong><br/><br/>'
      '<strong>一句话：少不等于错。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>果仁者，人多畏；言不讳，色不媚</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>果：果真；畏：敬重、心里服</strong><br/>'
      '② <strong>讳：隐瞒；媚：讨好巴结</strong><br/><br/>'
      '<strong>一句话：敬不是怕，是服。</strong></p>'
      '<p><strong>果仁者，人多畏</strong><br/>'
      '① <strong>真有德的人站在那儿，不用凶，人也敬他</strong><br/>'
      '② <strong>他的分量在自己身上，不在嗓门上</strong><br/><br/>'
      '<strong>一句话：正，就有威。</strong></p>'
      '<p><strong>言不讳，色不媚</strong><br/>'
      '① <strong>该说的当面说，不背后绕</strong><br/>'
      '② <strong>不为了讨好谁，笑成另一副脸</strong><br/><br/>'
      '<strong>一句话：嘴直，脸正。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 先认人，再择友</h2>'
      '<p style="margin:0"><strong>前两句讲「看清」</strong><br/>'
      '① <strong>人多的地方，未必是对的</strong><br/>'
      '② <strong>仁者少，所以遇上了要珍惜</strong><br/><br/>'
      '<strong>一句话：别拿人多当理。</strong></p>'
      '<p><strong>后两句讲「认法」</strong><br/>'
      '① <strong>看他敢不敢说实话</strong><br/>'
      '② <strong>看他会不会为了好处改脸色</strong><br/><br/>'
      '<strong>一句话：两条就能认人。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>身边谁说话直、心又正，多跟他来往</strong><br/>'
      '② <strong>谁总顺着你说好听的，留个心眼</strong><br/><br/>'
      '<strong>一句话：近正人，远滑人。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：世上的人</strong><br/>'
      '① <strong>同是人，类不齐——人不一样</strong><br/>'
      '② <strong>流俗众，仁者希——跟风的多，讲仁的少</strong><br/><br/>'
      '<strong>一句话：希。</strong></p>'
      '<p><strong>后两句：仁者的样子</strong><br/>'
      '① <strong>果仁者，人多畏——人敬他</strong><br/>'
      '② <strong>言不讳，色不媚——嘴直脸正</strong><br/><br/>'
      '<strong>一句话：正。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>人多人少，不是理</strong><br/>'
      '② <strong>嘴直脸正，才是仁</strong><br/><br/>'
      '<strong>一句话：先识人，再择友。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 先识人，再择友</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"同是人，类不齐。流俗众，仁者希。果仁者，人多畏。言不讳，色不媚。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>人品类不齐，跟风的多、讲仁的少；'
      '真仁者让人敬，因为他说话直、不讨好。</p><p>📖 仁者希</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>人多是风气，人少是操守；'
      '敬是从德性里长出来的，不是从嗓门里喊出来的——认人先看这两条：敢不敢直言，肯不肯讨好。</p><p>💡 识人</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>先识人，再择友；'
      '近正人，远滑人。</p><p>🌱 亲仁远俗</p>'),
 72: '<p>这是「亲仁课堂」第四十课：亲仁第一段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「流俗众」是说大多数人都不好吗？</h3>'
       '<p><strong>不是说人坏，是说「随大流」省力。</strong><br/><br/>'
       '① <strong>大家都这样，不等于这样对</strong><br/>'
       '② <strong>不必看不起人，只是别拿人多当理由</strong><br/>'
       '③ <strong>记法：人多是风气，不是道理。</strong></p>'
       '<h3>❓ 「人多畏」是让人怕他吗？</h3>'
       '<p><strong>是敬，不是怕。</strong><br/><br/>'
       '① <strong>怕，靠的是凶；敬，靠的是正</strong><br/>'
       '② <strong>真仁者不用喊，人自己就让一步</strong><br/>'
       '③ <strong>记法：让人怕的不算本事，让人敬的才算。</strong></p>'
       '<h3>❓ 「言不讳」是不是说话不顾别人脸面？</h3>'
       '<p><strong>直，不等于冲。</strong><br/><br/>'
       '① <strong>该说的当面说，不背后嘀咕</strong><br/>'
       '② <strong>说事不说人，留台阶也留分寸</strong><br/>'
       '③ <strong>记法：话直，心软。</strong></p>'
       '<h3>❓ 身边没有「仁者」怎么办？</h3>'
       '<p><strong>先找「哪件事上正」的人。</strong><br/><br/>'
       '① <strong>没人十全十美，看他最在意什么</strong><br/>'
       '② <strong>书里的人也能亲——读《论语》就是跟孔子来往</strong><br/>'
       '③ <strong>记法：找不到全仁，就学他那一处正。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 认人</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看他敢不敢当面说实话，还是只背后说</strong>；'
       '<strong>这就是「言不讳」</strong>。</p><p>💡 看脸色</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看他对有用的人和没用的人，脸色是不是一个样</strong>；'
       '<strong>这就是「色不媚」</strong>。</p><p>🌱 自己先做</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>想找仁者，自己先学一分：说话直一点，脸色正一点</strong>；'
       '<strong>这就是「果仁者」的样子</strong><br/><br/>'
       '<strong>本课的落点：先识人，再择友。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天开新门「亲仁」，先学认人。记牢：<strong>先识人，再择友</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">同是人，类不齐。流俗众，仁者希。'
       '果仁者，人多畏。言不讳，色不媚。</p><p>回顾本课要点:</p>'
       '<p>亲仁第一段 · 仁者难得。<strong>先识人</strong>。</p>'
       '<p>同是人，类不齐 · 人各不同。<strong>别想成一类</strong>。</p>'
       '<p>流俗众，仁者希 · 跟风的多。<strong>少不等于错</strong>。</p>'
       '<p>果仁者，人多畏 · 敬不是怕。<strong>正就有威</strong>。</p>'
       '<p>言不讳，色不媚 · 嘴直脸正。<strong>不讨好</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>第五门「亲仁」开头；前面讲做人做事，'
       '这一门讲跟谁走近。</p>'
       '<div class="ds-quote">'),

 111: '<p>同是人，类不齐。流俗众，仁者希。果仁者，人多畏。言不讳，色不媚。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「类」「流俗」「希」「讳」「媚」怎么讲。'
       '② 今天找一个「说话直、脸色正」的同学，多跟他说两句。'
       '③ 想一想：你有没有为了讨好谁，改过脸色。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>同是人，类不齐；流俗众，仁者希；'
       '果仁者，人多畏；言不讳，色不媚。</strong></p></div>'),

 119: '            "同是人，类不齐。流俗众，仁者希。果仁者，人多畏。言不讳，色不媚。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '580-tong-shi-ren';",

 59: '<!-- 4. 同是人类不齐·流俗众仁者希 -->',
 61: '<!-- 5. 果仁者人多畏·言不讳色不媚 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「同是人，类不齐」的「类」是什么意思？', opts: ['品类、种类', '类似', '分类整理'], ans: 0, exp: '类是品类'},",
 "  {q: '2. 「类不齐」的「不齐」是什么意思？', opts: ['不一样、不整齐', '不齐全', '不排队'], ans: 0, exp: '不齐是不一样'},",
 "  {q: '3. 「流俗众」的「流俗」是什么意思？', opts: ['随大流的风气', '流动的河水', '通俗的说法'], ans: 0, exp: '流俗是随大流'},",
 "  {q: '4. 「仁者希」的「希」是什么意思？', opts: ['同「稀」，少', '希望', '稀奇'], ans: 0, exp: '希同稀，是少'},",
 "  {q: '5. 「果仁者」的「果」是什么意思？', opts: ['果真、真个', '果子', '结果'], ans: 0, exp: '果是果真'},",
 "  {q: '6. 「人多畏」的「畏」是什么意思？', opts: ['敬重、心里服', '害怕躲开', '畏惧不敢说话'], ans: 0, exp: '畏是敬重'},",
 "  {q: '7. 「言不讳」的「讳」是什么意思？', opts: ['隐瞒、避讳', '后悔', '教诲'], ans: 0, exp: '讳是隐瞒'},",
 "  {q: '8. 「色不媚」的「媚」是什么意思？', opts: ['讨好、巴结', '好看', '明媚'], ans: 0, exp: '媚是讨好'},",
 "  {q: '9. 「言不讳，色不媚」是说什么？', opts: ['说话直不隐瞒，脸色正不讨好', '说话大声脸色难看', '不说话也不看人'], ans: 0, exp: '嘴直脸正'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['人品类不齐、仁者稀少，要先认得出仁者再亲近', '怎么说人坏话', '怎么让人怕自己'], ans: 0, exp: '先识人，再择友'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("578-en-yu-bao", "580-tong-shi-ren")
    out = out.replace("yaoyue579", "yaoyue580")
    out = out.replace("第三十八课", "第四十课")
    out = out.replace("弟子规课堂", "亲仁课堂")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
