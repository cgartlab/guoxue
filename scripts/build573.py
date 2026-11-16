#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build573: 以 572 为骨架，按行号替换文字生成第 573 课
《弟子规·泛爱众》第二段：才大者，望自大。人所服，非言大。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 572 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/572-fan-shi-ren/index.html"
DST_DIR = f"{ROOT}/lessons/573-cai-da-zhe"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十三课，泛爱众第二段。原文：「才大者，望自大。人所服，非言大。」'
        '前两句讲才能大的人，声望自然就大，不用自己吹；后两句讲别人佩服你，靠的是真本事，'
        '不是话说得大。跟上一段「人所重，非貌高」连起来看：看人不看长相，也不听大话，要看德行和真本事。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("才","cái"),("大","dà"),("者","zhě")]) + "，" + _r([("望","wàng"),("自","zì"),("大","dà")]) + "。", True)
 + _p(_r([("人","rén"),("所","suǒ"),("服","fú")]) + "，" + _r([("非","fēi"),("言","yán"),("大","dà")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="才大者，望自大；人所服，非言大 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十三课：本事大声望自大，服人不靠嘴大。泛爱众第二段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/573-cai-da-zhe/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/573-cai-da-zhe/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 才大者望自大，人所服非言大 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">才大者</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第二段：才大者，望自大</p>'
      '<p class="cover-desc">本事大的人，声望自然大，不用自己吹；别人真心服你，'
      '靠的是手上的真功夫，不是嘴上的大话。一句话：本事说话，大话白说。</p><div class="cover-seal">才</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第二段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>才能大的人，声望自然就大；人们佩服他，是因为他真有本事，不是因为他话说得大。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「才」是才能、本事；「望」是声望、名望，是大家心里对他的敬重；「服」是佩服、心服；'
      '「言大」是说大话、夸口。这是《弟子规》第四门「泛爱众」的第二段，紧跟「行高者，名自高；'
      '人所重，非貌高」：上一段说名声靠德行、不靠长相，这一段说声望靠才能、不靠吹牛。'
      '德行和本事两条都立住了，人才真站得住；光会说、光会装，早晚被人看穿。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>才大者，望自大；人所服，非言大。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 本事说话，大话白说</h2>'
      '<p style="margin:0"><strong>先说「望从哪来」</strong><br/>'
      '① <strong>本事到了，声望自己跟上来</strong><br/>'
      '② <strong>不是求来的，也不是喊来的</strong><br/><br/>'
      '<strong>一句话：有才自有望。</strong></p>'
      '<p><strong>再说「人服什么」</strong><br/>'
      '① <strong>服你能干、干得成事</strong><br/>'
      '② <strong>不服你嗓门大、会说大话</strong><br/><br/>'
      '<strong>一句话：服本事不服嘴。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>上一段讲：不看长相看德行</strong><br/>'
      '② <strong>这一段讲：不听大话看本事</strong><br/><br/>'
      '<strong>一句话：看德看才，不看脸不看嘴。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>才大者，望自大</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>才：才能、本事；望：声望、名望</strong><br/>'
      '② <strong>自：自然、自己就来，不用争</strong><br/><br/>'
      '<strong>一句话：有本事的声望大。</strong></p>'
      '<p><strong>才大者</strong><br/>'
      '① <strong>本事是真练出来的，不是吹出来的</strong><br/>'
      '② <strong>会修、会算、会写、会种地，都是才</strong><br/><br/>'
      '<strong>一句话：手上得有活。</strong></p>'
      '<p><strong>望自大</strong><br/>'
      '① <strong>大家心里那杆秤，自己会称</strong><br/>'
      '② <strong>真能干的人，走到哪儿都被请着</strong><br/><br/>'
      '<strong>一句话：声望跟着本事走。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>人所服，非言大</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>服：佩服、心服口服</strong><br/>'
      '② <strong>非：不是；言大：说大话、夸口</strong><br/><br/>'
      '<strong>一句话：服你，不服你的嘴。</strong></p>'
      '<p><strong>人所服</strong><br/>'
      '① <strong>服你干成过的事，不服你说过的话</strong><br/>'
      '② <strong>心服是服在实处，嘴上服心里不服那不叫服</strong><br/><br/>'
      '<strong>一句话：服在实处。</strong></p>'
      '<p><strong>非言大</strong><br/>'
      '① <strong>说大话，一次兑现不了，往后就没人信</strong><br/>'
      '② <strong>话留三分，事做十分，人才服你</strong><br/><br/>'
      '<strong>一句话：少说大话，多做实事。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 才与言</h2>'
      '<p style="margin:0"><strong>前两句讲「才」</strong><br/>'
      '① <strong>先把本事练出来</strong><br/>'
      '② <strong>声望不用争，自己会来</strong><br/><br/>'
      '<strong>一句话：才立得住。</strong></p>'
      '<p><strong>后两句讲「言」</strong><br/>'
      '① <strong>说大话撑不起声望</strong><br/>'
      '② <strong>话大过本事，反被人笑</strong><br/><br/>'
      '<strong>一句话：嘴别大过手。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>把一门功课或一门手艺练到拿得出手</strong><br/>'
      '② <strong>答应别人的事，说几分就做到几分，甚至多做到一点</strong><br/><br/>'
      '<strong>一句话：练本事，说实话说。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 两句一反一正</h2>'
      '<p style="margin:0"><strong>前两句：望从才来</strong><br/>'
      '① <strong>才大者——本事大的人</strong><br/>'
      '② <strong>望自大——声望自然大</strong><br/><br/>'
      '<strong>一句话：才。</strong></p>'
      '<p><strong>后两句：不服大话</strong><br/>'
      '① <strong>人所服——人家心里服的</strong><br/>'
      '② <strong>非言大——不是你的大话</strong><br/><br/>'
      '<strong>一句话：实。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>本事往身上攒</strong><br/>'
      '② <strong>大话往回收</strong><br/><br/>'
      '<strong>一句话：才实，嘴收。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 才大者，望自大。人所服，非言大。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"才大者，望自大。人所服，非言大。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>本事大声望就大；服人靠真本事，不靠说大话。</p>'
      '<p>📖 才实</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>声望是别人心里的秤，秤的是你干成了什么；'
      '说大话是借来的脸面，早晚要还。</p><p>💡 实</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>才大者，望自大；人所服，非言大。</p><p>🌱 才实言实</p>'),
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
       '<h3>❓ 我只是个学生，没大本事，这段跟我有什么关系？</h3>'
       '<p><strong>本事是攒出来的，从小攒起。</strong><br/><br/>'
       '① <strong>把字写好、把题算对、把书读熟，都是才</strong><br/>'
       '② <strong>先在小事上让人信得过，长大才有大声望</strong><br/>'
       '③ <strong>记法：今天攒一点，明天多一点。</strong></p>'
       '<h3>❓ 为什么说「非言大」？说大话有什么不好？</h3>'
       '<p><strong>说大话兑现不了，一次就失信。</strong><br/><br/>'
       '① <strong>话说得太满，做不到，别人下次就不听你</strong><br/>'
       '② <strong>老实人说七分做十分，最让人服</strong><br/>'
       '③ <strong>记法：嘴小一点，手勤一点。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 把本事练出来</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>挑一门功课或一门手艺，练到拿得出手</strong>；'
       '<strong>这就是「才大者」</strong>。</p><p>💡 不吹不夸</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>会多少说多少，不把三分说成十分</strong>；'
       '<strong>这就是「非言大」</strong>。</p><p>🌱 做事让人服</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>答应的事按时做到，做不到就早说</strong>；'
       '<strong>这就是「人所服」</strong><br/><br/>'
       '<strong>本课的落点：本事说话，大话白说。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第二段，声望靠本事不靠大话。记牢：<strong>才实言实</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">才大者，望自大。人所服，非言大。</p>'
       '<p>回顾本课要点:</p>'
       '<p>泛爱众第二段 · 有才自有望，服人不服嘴。<strong>才实言实</strong>。</p>'
       '<p>才大者 · 本事是真练出来的。<strong>手上得有活</strong>。</p>'
       '<p>望自大 · 声望跟着本事走。<strong>不用自己争</strong>。</p>'
       '<p>人所服 · 服你干成的事。<strong>服在实处</strong>。</p>'
       '<p>非言大 · 说大话一次就失信。<strong>嘴别大过手</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第二段；上一段看德不看貌，这一段看才不看嘴，'
       '德行和本事两样都得立住。</p>'
       '<div class="ds-quote">'),

 111: '<p>才大者，望自大。人所服，非言大。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「才」「望」「服」「言大」怎么讲。'
       '② 想一想：你身边最能干的那个人，别人为什么服他。'
       '③ 这一周只说能做到的话，看看有没有人多信你一点。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>才大者，望自大；人所服，非言大。</strong></p></div>'),

 119: '            "才大者，望自大。人所服，非言大。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '573-cai-da-zhe';",

 59: '<!-- 4. 才大者望自大 -->',
 61: '<!-- 5. 人所服非言大 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「才大者」的「才」是什么意思？', opts: ['才能、本事', '刚才', '木材'], ans: 0, exp: '才是才能、本事'},",
 "  {q: '2. 「望自大」的「望」是什么意思？', opts: ['声望、名望', '望见', '希望'], ans: 0, exp: '望是声望、名望'},",
 "  {q: '3. 「望自大」的「自」是什么意思？', opts: ['自然、自己就来', '自己一个人', '自从'], ans: 0, exp: '自是自然、不用争'},",
 "  {q: '4. 「人所服」的「服」是什么意思？', opts: ['佩服、心服', '衣服', '服药'], ans: 0, exp: '服是佩服、心服'},",
 "  {q: '5. 「非言大」的「言大」是什么意思？', opts: ['说大话、夸口', '声音大', '话很多'], ans: 0, exp: '言大是说大话'},",
 "  {q: '6. 「才大者，望自大」是说什么？', opts: ['本事大，声望自然大', '眼睛望得远', '名字写得大'], ans: 0, exp: '有才自有望'},",
 "  {q: '7. 「人所服，非言大」是说什么？', opts: ['让人心服靠真本事，不靠吹牛', '说话声音要大', '最好别说话'], ans: 0, exp: '服本事不服嘴'},",
 "  {q: '8. 说大话最大的坏处是什么？', opts: ['兑现不了，一次就失信', '太费力气', '别人听不清'], ans: 0, exp: '大话兑现不了就失信'},",
 "  {q: '9. 跟上一段「人所重，非貌高」合起来看，看人先看什么？', opts: ['看德行和本事，不看外表和嘴', '看长相好不好', '看谁嗓门大'], ans: 0, exp: '看德看才'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['本事大就声望大，服人不靠说大话', '怎么出名', '怎么说话好听'], ans: 0, exp: '本事说话，大话白说'},",
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
