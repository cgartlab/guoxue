#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build573: 以 572 为骨架，按行号替换文字生成第 573 课
《弟子规·泛爱众》第二段：才大者，望自大。人所服，非言大。己有能，勿自私。人所能，勿轻訾。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 572 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/572-fan-shi-ren/index.html"
DST_DIR = f"{ROOT}/lessons/573-cai-da-zhe"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十三课，泛爱众第二段。原文：「才大者，望自大。人所服，非言大。'
        '己有能，勿自私。人所能，勿轻訾。」前两句讲才能大的人声望自然大，别人佩服的是真本事，'
        '不是大话；后两句讲自己有本事别藏着，别人有本事别轻看、别说坏话。合起来：本事要真，心量要大。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("才","cái"),("大","dà"),("者","zhě")]) + "，" + _r([("望","wàng"),("自","zì"),("大","dà")]) + "。", True)
 + _p(_r([("人","rén"),("所","suǒ"),("服","fú")]) + "，" + _r([("非","fēi"),("言","yán"),("大","dà")]) + "。")
 + _p(_r([("己","jǐ"),("有","yǒu"),("能","néng")]) + "，" + _r([("勿","wù"),("自","zì"),("私","sī")]) + "。")
 + _p(_r([("人","rén"),("所","suǒ"),("能","néng")]) + "，" + _r([("勿","wù"),("轻","qīng"),("訾","zǐ")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="才大者，望自大；己有能，勿自私 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十三课：本事大声望自大，有本事别藏、别人强别踩。泛爱众第二段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/573-cai-da-zhe/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/573-cai-da-zhe/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 才大者望自大，己有能勿自私 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">才大者</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第二段：才大者，望自大</p>'
      '<p class="cover-desc">本事大的人，声望自然大，不用自己吹；别人真心服你，靠的是手上的真功夫，'
      '不是嘴上的大话。自己有本事，别藏着只顾自己；别人有本事，别撇嘴说坏话。'
      '一句话：本事要真，心量要大。</p><div class="cover-seal">才</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第二段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>才能大的人，声望自然就大；人们佩服他，是因为他真有本事，不是话说得大。'
      '自己有本事，不要只顾自己、藏着不给别人；别人有本事，不要看轻他、说他的坏话。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「才」是才能、本事；「望」是声望、名望；「服」是佩服、心服；「言大」是说大话；'
      '「己」是自己；「勿」是不要；「轻」是看轻；「訾」读 zǐ，是诋毁、说人坏话。'
      '这是《弟子规》第四门「泛爱众」的第二段，接着上一段「人所重，非貌高」往下讲：'
      '前两句说名声靠真本事不靠大话，后两句说本事要肯给人用、别人有本事要肯认。'
      '合起来就一句话——本事要真，心量要大。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>才大者，望自大；人所服，非言大；己有能，勿自私；人所能，勿轻訾。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 本事要真，心量要大</h2>'
      '<p style="margin:0"><strong>先说「名声从哪来」</strong><br/>'
      '① <strong>本事真，声望自己跟上来</strong><br/>'
      '② <strong>大话撑不起声望，一次就垮</strong><br/><br/>'
      '<strong>一句话：才真才有望。</strong></p>'
      '<p><strong>再说「本事怎么用」</strong><br/>'
      '① <strong>自己有，别捂着，拿出来帮人</strong><br/>'
      '② <strong>别人有，别撇嘴，说句公道话</strong><br/><br/>'
      '<strong>一句话：心宽才走得远。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「才与言」</strong><br/>'
      '② <strong>后两句讲「己与人」</strong><br/><br/>'
      '<strong>一句话：才要真，心要宽。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>才大者，望自大；人所服，非言大</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>才：才能、本事；望：声望、名望</strong><br/>'
      '② <strong>服：佩服、心服；言大：说大话、夸口</strong><br/><br/>'
      '<strong>一句话：名声看真本事。</strong></p>'
      '<p><strong>才大者，望自大</strong><br/>'
      '① <strong>本事是真练出来的，不是吹出来的</strong><br/>'
      '② <strong>大家心里那杆秤，自己会称</strong><br/><br/>'
      '<strong>一句话：有才自有望。</strong></p>'
      '<p><strong>人所服，非言大</strong><br/>'
      '① <strong>服你干成过的事，不服你说过的话</strong><br/>'
      '② <strong>说大话一次兑现不了，往后没人信</strong><br/><br/>'
      '<strong>一句话：服本事不服嘴。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>己有能，勿自私；人所能，勿轻訾</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>己：自己；勿：不要</strong><br/>'
      '② <strong>自私：只顾自己、藏着不给；轻訾 zǐ：看轻、说人坏话</strong><br/><br/>'
      '<strong>一句话：有本事别捂，别人强别踩。</strong></p>'
      '<p><strong>己有能，勿自私</strong><br/>'
      '① <strong>会的东西拿出来帮人，别揣着当宝贝</strong><br/>'
      '② <strong>越教人，自己越明白；藏着不用，本事也废了</strong><br/><br/>'
      '<strong>一句话：有本事要肯给。</strong></p>'
      '<p><strong>人所能，勿轻訾</strong><br/>'
      '① <strong>别人会你不会，别撇嘴、别翻白眼</strong><br/>'
      '② <strong>背后说人坏话，先掉的是自己的价</strong><br/><br/>'
      '<strong>一句话：容人强，自己才长。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 才与言，己与人</h2>'
      '<p style="margin:0"><strong>前两句讲「才」</strong><br/>'
      '① <strong>本事立得住，声望不用争</strong><br/>'
      '② <strong>大话撑场面，早晚露底</strong><br/><br/>'
      '<strong>一句话：才要真。</strong></p>'
      '<p><strong>后两句讲「人」</strong><br/>'
      '① <strong>自己有，肯给大家用</strong><br/>'
      '② <strong>别人有，肯心里认、嘴上夸</strong><br/><br/>'
      '<strong>一句话：心要宽。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>会做的题，给不会的同学讲一遍</strong><br/>'
      '② <strong>同学考得比你好，说句「你真行」，不撇嘴不酸话</strong><br/><br/>'
      '<strong>一句话：本事给人用，好话给人说。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：名声怎么来</strong><br/>'
      '① <strong>才大者，望自大——本事大声望大</strong><br/>'
      '② <strong>人所服，非言大——服人不服嘴</strong><br/><br/>'
      '<strong>一句话：真。</strong></p>'
      '<p><strong>后两句：本事怎么用</strong><br/>'
      '① <strong>己有能，勿自私——有本事别藏着</strong><br/>'
      '② <strong>人所能，勿轻訾——别人行别踩他</strong><br/><br/>'
      '<strong>一句话：宽。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>本事往身上攒，大话往回收</strong><br/>'
      '② <strong>会了就教人，人强别酸人</strong><br/><br/>'
      '<strong>一句话：才真，心宽。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 才要真，心要宽</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"才大者，望自大。人所服，非言大。己有能，勿自私。人所能，勿轻訾。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>本事大声望就大，服人靠真本事；'
      '自己有本事别藏着，别人有本事别看轻。</p><p>📖 才真心宽</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>声望是别人心里的秤，秤的是你干成了什么；'
      '本事越用越活，越藏越死；容得下别人强，自己才长得快。</p><p>💡 真宽</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>才要真，心要宽；'
      '有本事肯给人，别人强肯认。</p><p>🌱 才实心宽</p>'),
 72: '<p>这是「弟子规课堂」第三十三课：泛爱众第二段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 有本事就要让人知道吧？</h3>'
       '<p><strong>不用张扬，本事藏不住。</strong><br/><br/>'
       '① <strong>真会的人，一出手大家就看见了</strong><br/>'
       '② <strong>自己到处说，反倒显得心虚</strong><br/>'
       '③ <strong>记法：本事自己会说话。</strong></p>'
       '<h3>❓ 「望」和「名」有什么不一样？</h3>'
       '<p><strong>名是外面的称呼，望是心里的分量。</strong><br/><br/>'
       '① <strong>名可以靠热闹挣来，望只能靠本事攒下</strong><br/>'
       '② <strong>望比名实在，也更难挣</strong><br/>'
       '③ <strong>记法：名在外，望在心。</strong></p>'
       '<h3>❓ 「勿自私」是不是我的东西都得给人？</h3>'
       '<p><strong>不是白送，是别捂着不让人用。</strong><br/><br/>'
       '① <strong>会的方法、会的题，教给同学不算吃亏</strong><br/>'
       '② <strong>教一遍，你自己反倒更清楚</strong><br/>'
       '③ <strong>记法：本事越用越多。</strong></p>'
       '<h3>❓ 别人比我强，我心里不舒服怎么办？</h3>'
       '<p><strong>酸话最亏本，学过来才划算。</strong><br/><br/>'
       '① <strong>说人坏话，改不了他比你强</strong><br/>'
       '② <strong>问一句「你怎么练的」，本事就到你身上了</strong><br/>'
       '③ <strong>记法：不酸人，学人。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 会了就教人</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>会做的题，给不会的同学讲一遍</strong>；'
       '<strong>这就是「己有能，勿自私」</strong>。</p><p>💡 不酸不踩</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学考得好、球打得好，说句「你真行」，不撇嘴不说酸话</strong>；'
       '<strong>这就是「人所能，勿轻訾」</strong>。</p><p>🌱 靠本事挣脸</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把功课、把手艺练到拿得出手，说几分做几分</strong>；'
       '<strong>这就是「才大者，望自大」</strong><br/><br/>'
       '<strong>本课的落点：本事要真，心量要大。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第二段，名声靠本事，本事要肯给人用。记牢：<strong>才实心宽</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">才大者，望自大。人所服，非言大。'
       '己有能，勿自私。人所能，勿轻訾。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第二段 · 才要真，心要宽。<strong>才实心宽</strong>。</p>'
       '<p>才大者，望自大 · 本事大声望自大。<strong>有才自有望</strong>。</p>'
       '<p>人所服，非言大 · 服你干的事不服你的嘴。<strong>服本事不服嘴</strong>。</p>'
       '<p>己有能，勿自私 · 会了别捂着，教人。<strong>本事要肯给</strong>。</p>'
       '<p>人所能，勿轻訾 · 别人强别撇嘴。<strong>容人强自己长</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第二段；上一段看德不看貌，这一段看才不看嘴，'
       '德行和本事两样都得立住。</p>'
       '<div class="ds-quote">'),

 111: '<p>才大者，望自大。人所服，非言大。己有能，勿自私。人所能，勿轻訾。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「才」「望」「服」「訾」怎么讲。'
       '② 把你会的一道题教给一个不会的同学。'
       '③ 想一想：你身边最能干的那个人，别人为什么服他。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>才大者，望自大；人所服，非言大；'
       '己有能，勿自私；人所能，勿轻訾。</strong></p></div>'),

 119: '            "才大者，望自大。人所服，非言大。己有能，勿自私。人所能，勿轻訾。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '573-cai-da-zhe';",

 59: '<!-- 4. 才大者望自大·人所服非言大 -->',
 61: '<!-- 5. 己有能勿自私·人所能勿轻訾 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「才大者」的「才」是什么意思？', opts: ['才能、本事', '刚才', '木材'], ans: 0, exp: '才是才能、本事'},",
 "  {q: '2. 「望自大」的「望」是什么意思？', opts: ['声望、名望', '望见', '希望'], ans: 0, exp: '望是声望、名望'},",
 "  {q: '3. 「人所服」的「服」是什么意思？', opts: ['佩服、心服', '衣服', '服药'], ans: 0, exp: '服是佩服、心服'},",
 "  {q: '4. 「非言大」的「言大」是什么意思？', opts: ['说大话、夸口', '声音大', '话很多'], ans: 0, exp: '言大是说大话'},",
 "  {q: '5. 「己有能」的「己」是什么意思？', opts: ['自己', '已经', '吉利'], ans: 0, exp: '己是自己'},",
 "  {q: '6. 「勿自私」的「勿」是什么意思？', opts: ['不要', '务必', '忽然'], ans: 0, exp: '勿是不要'},",
 "  {q: '7. 「勿轻訾」的「訾」怎么读、什么意思？', opts: ['zǐ，诋毁、说人坏话', 'zī，钱财', 'cǐ，此时'], ans: 0, exp: '訾读 zǐ，是诋毁、说人坏话'},",
 "  {q: '8. 「己有能，勿自私」是说什么？', opts: ['自己有本事，要拿出来帮人，别只顾自己', '自己别学本事', '本事要藏好'], ans: 0, exp: '会了别捂着，教人'},",
 "  {q: '9. 「人所能，勿轻訾」是说什么？', opts: ['别人有本事，不要看轻、不要说坏话', '别人会的别学', '别人行了要躲开'], ans: 0, exp: '容人强，自己才长'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['本事要真、心量要大：名声靠真本事，有本事肯给人、别人强肯认', '怎么出名', '怎么说话好听'], ans: 0, exp: '才要真，心要宽'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("572-fan-shi-ren", "573-cai-da-zhe")
    out = out.replace("yaoyue573", "yaoyue574")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
