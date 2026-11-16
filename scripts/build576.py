#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build576: 以 575 为骨架，按行号替换文字生成第 576 课
《弟子规·泛爱众》第五段：扬人恶，即是恶。疾之甚，祸且作。善相劝，德皆建。过不规，道两亏。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 575 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/575-ren-you-duan/index.html"
DST_DIR = f"{ROOT}/lessons/576-yang-ren-e"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十六课，泛爱众第五段。原文：「扬人恶，即是恶。疾之甚，祸且作。'
        '善相劝，德皆建。过不规，道两亏。」前两句讲到处宣扬别人的坏处，本身就是做坏事，'
        '恨得太狠，祸事就找上门；后两句讲见到好的互相勉励，双方的德行都立得住，'
        '有过错不规劝，两人的道义都亏损。合起来：扬恶招祸，规过成德。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("扬","yáng"),("人","rén"),("恶","è")]) + "，" + _r([("即","jí"),("是","shì"),("恶","è")]) + "。", True)
 + _p(_r([("疾","jí"),("之","zhī"),("甚","shèn")]) + "，" + _r([("祸","huò"),("且","qiě"),("作","zuò")]) + "。")
 + _p(_r([("善","shàn"),("相","xiāng"),("劝","quàn")]) + "，" + _r([("德","dé"),("皆","jiē"),("建","jiàn")]) + "。")
 + _p(_r([("过","guò"),("不","bù"),("规","guī")]) + "，" + _r([("道","dào"),("两","liǎng"),("亏","kuī")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="扬人恶，即是恶；过不规，道两亏 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十六课：说人坏处自己也是做坏事，恨太狠招祸；劝人好、规人过才是相劝成德。泛爱众第五段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/576-yang-ren-e/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/576-yang-ren-e/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 扬人恶即是恶，过不规道两亏 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">扬人恶</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第五段：扬人恶，即是恶</p>'
      '<p class="cover-desc">到处说别人的坏处，本身就是做坏事；恨得太狠，祸事就找上门。'
      '反过来，好的互相勉励，有过错互相规劝，两人的德行都立得住。'
      '一句话：扬恶招祸，规过成德。</p><div class="cover-seal">劝</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第五段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>到处宣扬别人的坏处，本身就是做坏事；恨得太狠，祸事就会找上门。'
      '见到好的地方互相勉励，双方的德行都立得起来；有过错不去规劝，两人的道义都亏损。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「扬」是宣扬、到处说；「恶」读 è，是坏处、坏事；「疾」是痛恨；「甚」是太、过分；'
      '「作」是兴起、发生；「相劝」是互相劝勉；「建」是建立、立起来；「规」是规劝、指出让人改；'
      '「两亏」是两边都亏损。这是《弟子规》第四门「泛爱众」的第五段，接上一段「道人善，即是善」'
      '往下说：扬善是善，扬恶就是恶；再往前走一步——光不揭短还不够，见人有过还得劝。'
      '一句话，扬恶招祸，规过成德。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>扬人恶，即是恶；疾之甚，祸且作；善相劝，德皆建；过不规，道两亏。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 扬恶招祸，规过成德</h2>'
      '<p style="margin:0"><strong>先说「扬恶的害」</strong><br/>'
      '① <strong>说人坏处，自己先成了坏人</strong><br/>'
      '② <strong>恨得太狠，火先烧自己</strong><br/><br/>'
      '<strong>一句话：扬恶招祸。</strong></p>'
      '<p><strong>再说「相劝的好」</strong><br/>'
      '① <strong>好的一起做，两人都长进</strong><br/>'
      '② <strong>有错悄悄劝，两人都站得住</strong><br/><br/>'
      '<strong>一句话：相劝成德。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「别做什么」</strong><br/>'
      '② <strong>后两句讲「该做什么」</strong><br/><br/>'
      '<strong>一句话：不扬恶，肯规过。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>扬人恶，即是恶；疾之甚，祸且作</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>扬：宣扬、到处说；恶 è：坏处、坏事</strong><br/>'
      '② <strong>疾：痛恨；甚：太、过分；作：兴起、发生</strong><br/><br/>'
      '<strong>一句话：说人坏，自己先坏。</strong></p>'
      '<p><strong>扬人恶，即是恶</strong><br/>'
      '① <strong>他做了错事，你到处传，你也在做错事</strong><br/>'
      '② <strong>传一句，添一句，最后变成一场是非</strong><br/><br/>'
      '<strong>一句话：传恶如做恶。</strong></p>'
      '<p><strong>疾之甚，祸且作</strong><br/>'
      '① <strong>恨一个人恨到牙痒，自己先睡不好</strong><br/>'
      '② <strong>恨过了头，容易做出后悔的事，祸就来了</strong><br/><br/>'
      '<strong>一句话：恨太狠，先伤己。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>善相劝，德皆建；过不规，道两亏</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>相劝：互相劝勉、互相鼓励做好</strong><br/>'
      '② <strong>建：立起来；规：规劝；两亏：两边都亏</strong><br/><br/>'
      '<strong>一句话：互相劝，两边好。</strong></p>'
      '<p><strong>善相劝，德皆建</strong><br/>'
      '① <strong>你想练字，我也练，互相看着，都练成了</strong><br/>'
      '② <strong>好的互相学、互相夸，德行一天天长</strong><br/><br/>'
      '<strong>一句话：一起好，才是真好。</strong></p>'
      '<p><strong>过不规，道两亏</strong><br/>'
      '① <strong>朋友要走歪路，你不吭声，他栽了你也亏心</strong><br/>'
      '② <strong>看着不说，不是厚道，是不负责任</strong><br/><br/>'
      '<strong>一句话：该劝不劝，两边都亏。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 一扬一劝</h2>'
      '<p style="margin:0"><strong>前两句讲「扬」</strong><br/>'
      '① <strong>扬恶：说人坏，自己坏</strong><br/>'
      '② <strong>恨太狠：祸先到自己门口</strong><br/><br/>'
      '<strong>一句话：嘴上别造祸。</strong></p>'
      '<p><strong>后两句讲「劝」</strong><br/>'
      '① <strong>相劝：好的互相推着走</strong><br/>'
      '② <strong>规过：有错私下点一句</strong><br/><br/>'
      '<strong>一句话：嘴上要积德。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>同学犯了错，不传、不起外号、不拉群说</strong><br/>'
      '② <strong>好朋友做错事，拉一边小声说「这么干不好」</strong><br/><br/>'
      '<strong>一句话：不扬恶，肯规过。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：扬恶的果</strong><br/>'
      '① <strong>扬人恶，即是恶——说人坏就是做坏</strong><br/>'
      '② <strong>疾之甚，祸且作——恨太狠招祸</strong><br/><br/>'
      '<strong>一句话：戒。</strong></p>'
      '<p><strong>后两句：相劝的果</strong><br/>'
      '① <strong>善相劝，德皆建——互相劝，都长进</strong><br/>'
      '② <strong>过不规，道两亏——不劝，两边亏</strong><br/><br/>'
      '<strong>一句话：劝。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>坏话不出门，好话多出门</strong><br/>'
      '② <strong>有错小声劝，好人一起做</strong><br/><br/>'
      '<strong>一句话：戒扬恶，勤相劝。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 扬恶招祸，规过成德</h2>'
      '<p>四句话，正反两面——</p>'
      '<h3>"扬人恶，即是恶。疾之甚，祸且作。善相劝，德皆建。过不规，道两亏。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>传人坏处自己也是做坏事，恨太狠招祸；'
      '互相劝好都长进，有错不劝两边亏。</p><p>📖 戒恶劝善</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>说人坏，先脏自己的嘴；'
      '劝人改，先立自己的德——一张嘴，能造祸也能积德。</p><p>💡 口德</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>不扬恶，肯规过；'
      '互相劝，一起好。</p><p>🌱 扬恶招祸</p>'),
 72: '<p>这是「弟子规课堂」第三十六课：泛爱众第五段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 他做的坏事是真的，说说也不行吗？</h3>'
       '<p><strong>真事也不必到处说。</strong><br/><br/>'
       '① <strong>该管的说给该管的人：老师、家长</strong><br/>'
       '② <strong>说给一群人听，是让人丢脸，不是解决问题</strong><br/>'
       '③ <strong>记法：说给能管的人，不说给看热闹的人。</strong></p>'
       '<h3>❓ 「疾之甚，祸且作」为什么招祸？</h3>'
       '<p><strong>恨太狠，自己先乱。</strong><br/><br/>'
       '① <strong>睡不好、想不开，书也读不进</strong><br/>'
       '② <strong>一冲动做出格的事，祸就跟着来</strong><br/>'
       '③ <strong>记法：恨要收着，理要讲清。</strong></p>'
       '<h3>❓ 劝人会不会得罪人？</h3>'
       '<p><strong>劝得对，不得罪；劝得难看，才得罪。</strong><br/><br/>'
       '① <strong>私下劝、就事论事、给办法</strong><br/>'
       '② <strong>当众数落，他下不来台，只会记恨</strong><br/>'
       '③ <strong>记法：小声说，给退路。</strong></p>'
       '<h3>❓ 别人劝我，我该怎么做？</h3>'
       '<p><strong>先谢一句，再想一想。</strong><br/><br/>'
       '① <strong>肯当面劝你的，是真心为你好</strong><br/>'
       '② <strong>当场顶回去，往后没人再跟你说实话</strong><br/>'
       '③ <strong>记法：闻过先谢，回头再改。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 不扬人恶</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学犯了错，不传、不起外号、不拉着别人说</strong>；'
       '<strong>这就是「扬人恶，即是恶」</strong>。</p><p>💡 有过要劝</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>好朋友做错事，拉一边小声说「这么干不好」</strong>；'
       '<strong>这就是「过不规，道两亏」</strong>。</p><p>🌱 互相劝好</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>和朋友定个小目标，每天互相提醒一句</strong>；'
       '<strong>这就是「善相劝，德皆建」</strong><br/><br/>'
       '<strong>本课的落点：扬恶招祸，规过成德。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第五段，不传人坏，肯劝人改。记牢：<strong>扬恶招祸</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">扬人恶，即是恶。疾之甚，祸且作。'
       '善相劝，德皆建。过不规，道两亏。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第五段 · 不扬恶，肯规过。<strong>扬恶招祸</strong>。</p>'
       '<p>扬人恶，即是恶 · 传人坏自己先坏。<strong>闭上嘴</strong>。</p>'
       '<p>疾之甚，祸且作 · 恨太狠招祸。<strong>恨要收着</strong>。</p>'
       '<p>善相劝，德皆建 · 互相劝都长进。<strong>一起好</strong>。</p>'
       '<p>过不规，道两亏 · 该劝不劝两边亏。<strong>小声劝</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第五段；上一段说不揭短，'
       '这一段进一步说还该劝人改。</p>'
       '<div class="ds-quote">'),

 111: '<p>扬人恶，即是恶。疾之甚，祸且作。善相劝，德皆建。过不规，道两亏。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「扬」「疾」「规」「两亏」怎么讲。'
       '② 找个好朋友，互相提一个能改的小毛病。'
       '③ 想一想：你恨过谁，现在心里松快了没有。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>扬人恶，即是恶；疾之甚，祸且作；'
       '善相劝，德皆建；过不规，道两亏。</strong></p></div>'),

 119: '            "扬人恶，即是恶。疾之甚，祸且作。善相劝，德皆建。过不规，道两亏。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '576-yang-ren-e';",

 59: '<!-- 4. 扬人恶即是恶·疾之甚祸且作 -->',
 61: '<!-- 5. 善相劝德皆建·过不规道两亏 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「扬人恶」的「扬」是什么意思？', opts: ['宣扬、到处说', '扬起手', '扬场'], ans: 0, exp: '扬是宣扬、到处说'},",
 "  {q: '2. 「即是恶」的「恶」怎么读、什么意思？', opts: ['è，坏处、坏事', 'ě，恶心', 'wù，厌恶'], ans: 0, exp: '恶读 è，是坏处、坏事'},",
 "  {q: '3. 「疾之甚」的「疾」是什么意思？', opts: ['痛恨、憎恨', '生病', '快速'], ans: 0, exp: '疾是痛恨'},",
 "  {q: '4. 「疾之甚」的「甚」是什么意思？', opts: ['太、过分', '甚至', '什么'], ans: 0, exp: '甚是太、过分'},",
 "  {q: '5. 「祸且作」的「作」是什么意思？', opts: ['兴起、发生', '做作业', '作家'], ans: 0, exp: '作是兴起、发生'},",
 "  {q: '6. 「善相劝」的「相劝」是什么意思？', opts: ['互相劝勉、互相鼓励做好', '互相吵架', '劝人分开'], ans: 0, exp: '相劝是互相劝勉'},",
 "  {q: '7. 「德皆建」的「建」是什么意思？', opts: ['建立、立起来', '建设房子', '建议'], ans: 0, exp: '建是建立、立起来'},",
 "  {q: '8. 「过不规」的「规」是什么意思？', opts: ['规劝、指出让人改', '圆规', '规矩'], ans: 0, exp: '规是规劝、指出让人改'},",
 "  {q: '9. 「扬人恶，即是恶」是说什么？', opts: ['到处说别人的坏处，本身就是做坏事', '别人做的坏事要传开', '坏事要记下来'], ans: 0, exp: '传恶如做恶'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['扬恶招祸，规过成德：不传人坏，肯劝人改', '怎么报仇', '怎么不吃亏'], ans: 0, exp: '扬恶招祸，规过成德'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("575-ren-you-duan", "576-yang-ren-e")
    out = out.replace("yaoyue576", "yaoyue577")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
