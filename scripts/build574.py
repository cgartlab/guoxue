#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build574: 以 573 为骨架，按行号替换文字生成第 574 课
《弟子规·泛爱众》第三段：勿谄富，勿骄贫。勿厌故，勿喜新。人不闲，勿事搅。人不安，勿话扰。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 573 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/573-cai-da-zhe/index.html"
DST_DIR = f"{ROOT}/lessons/574-wu-chan-fu"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十四课，泛爱众第三段。原文：「勿谄富，勿骄贫。勿厌故，勿喜新。'
        '人不闲，勿事搅。人不安，勿话扰。」前两句讲不看钱待人：不巴结有钱的，不看轻穷的；'
        '不嫌弃旧人旧物，也不一味贪新。后两句讲找人要挑时候：人家正忙别拿事去搅，人家心里不安别拿话去烦。'
        '合起来：待人有分寸。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("勿","wù"),("谄","chǎn"),("富","fù")]) + "，" + _r([("勿","wù"),("骄","jiāo"),("贫","pín")]) + "。", True)
 + _p(_r([("勿","wù"),("厌","yàn"),("故","gù")]) + "，" + _r([("勿","wù"),("喜","xǐ"),("新","xīn")]) + "。")
 + _p(_r([("人","rén"),("不","bù"),("闲","xián")]) + "，" + _r([("勿","wù"),("事","shì"),("搅","jiǎo")]) + "。")
 + _p(_r([("人","rén"),("不","bù"),("安","ān")]) + "，" + _r([("勿","wù"),("话","huà"),("扰","rǎo")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="勿谄富，勿骄贫；人不闲，勿事搅 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十四课：不看钱待人、不嫌旧不贪新，人家忙乱时别添乱。泛爱众第三段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/574-wu-chan-fu/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/574-wu-chan-fu/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 勿谄富勿骄贫，人不闲勿事搅 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">勿谄富</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第三段：勿谄富，勿骄贫</p>'
      '<p class="cover-desc">不巴结有钱的，不看轻穷的；不嫌弃旧的，不一味贪新。'
      '人家正忙着，别拿事去搅；人家心里不安，别拿话去烦。'
      '一句话：待人有分寸。</p><div class="cover-seal">礼</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第三段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>不要巴结有钱的人，不要看不起穷的人；不要嫌弃旧的、老的朋友和东西，不要一味贪新。'
      '别人正忙着没空闲，不要拿事情去搅他；别人心里不安宁，不要拿话去烦他。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「谄」读 chǎn，是巴结、讨好；「骄」是傲慢、看不起人；「厌」是厌弃、嫌弃；'
      '「故」是旧的、原来的，指老朋友老东西；「闲」是空闲；「搅」是打扰、搅扰；「扰」是打扰。'
      '这是《弟子规》第四门「泛爱众」的第三段。上一段讲有本事别藏、别人强别踩；'
      '这一段把待人接物的规矩摆出来：看人不看钱，不嫌旧、不贪新；找人要挑时候，'
      '别在人家忙、人家乱的时候添麻烦。一句话——待人有分寸。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>勿谄富，勿骄贫；勿厌故，勿喜新；人不闲，勿事搅；人不安，勿话扰。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 待人有分寸</h2>'
      '<p style="margin:0"><strong>先说「看人看什么」</strong><br/>'
      '① <strong>不看钱：富的不巴结，穷的不看轻</strong><br/>'
      '② <strong>不看新旧：老的旧的不嫌，新的不迷</strong><br/><br/>'
      '<strong>一句话：待人一个样。</strong></p>'
      '<p><strong>再说「什么时候说话」</strong><br/>'
      '① <strong>人家正忙，别拿事去搅</strong><br/>'
      '② <strong>人家心烦，别拿话去烦</strong><br/><br/>'
      '<strong>一句话：看时候开口。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「怎么待人」</strong><br/>'
      '② <strong>后两句讲「怎么识趣」</strong><br/><br/>'
      '<strong>一句话：心要平，眼要活。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>勿谄富，勿骄贫；勿厌故，勿喜新</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>谄 chǎn：巴结、讨好；骄：傲慢、看不起人</strong><br/>'
      '② <strong>厌：嫌弃；故：旧的、原来的</strong><br/><br/>'
      '<strong>一句话：看人不看钱，不嫌旧。</strong></p>'
      '<p><strong>勿谄富，勿骄贫</strong><br/>'
      '① <strong>巴结有钱人，是想占便宜，人一眼看穿</strong><br/>'
      '② <strong>看轻穷人，是自己没出息，不是他不好</strong><br/><br/>'
      '<strong>一句话：有钱没钱，人一样待。</strong></p>'
      '<p><strong>勿厌故，勿喜新</strong><br/>'
      '① <strong>旧朋友、旧东西，是攒下来的情分</strong><br/>'
      '② <strong>一味追新的，扔掉的往往是好东西</strong><br/><br/>'
      '<strong>一句话：旧的不嫌，新的不迷。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>人不闲，勿事搅；人不安，勿话扰</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>闲：空闲；搅 jiǎo：打扰、搅扰</strong><br/>'
      '② <strong>安：安宁、心安；扰 rǎo：打扰</strong><br/><br/>'
      '<strong>一句话：别在人家忙乱时添乱。</strong></p>'
      '<p><strong>人不闲，勿事搅</strong><br/>'
      '① <strong>大人打电话、同学做题，先等一等</strong><br/>'
      '② <strong>非要打断，先说一句「急事，一句话」</strong><br/><br/>'
      '<strong>一句话：看人忙不忙。</strong></p>'
      '<p><strong>人不安，勿话扰</strong><br/>'
      '① <strong>人家刚挨批评、家里有事，别追着问</strong><br/>'
      '② <strong>陪着就行，想说的时候他自己会说</strong><br/><br/>'
      '<strong>一句话：看人心乱不乱。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 看钱看旧，看忙看乱</h2>'
      '<p style="margin:0"><strong>前两句讲「待人的心」</strong><br/>'
      '① <strong>不看钱，一个样</strong><br/>'
      '② <strong>不嫌旧，不贪新</strong><br/><br/>'
      '<strong>一句话：心要平。</strong></p>'
      '<p><strong>后两句讲「待人的眼」</strong><br/>'
      '① <strong>看人家忙不忙</strong><br/>'
      '② <strong>看人家心乱不乱</strong><br/><br/>'
      '<strong>一句话：眼要活。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>对有钱的同学、家里紧的同学，说话一个样</strong><br/>'
      '② <strong>大人打电话、老师讲话，等完了再说自己的事</strong><br/><br/>'
      '<strong>一句话：心平，识趣。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：怎么看人</strong><br/>'
      '① <strong>勿谄富，勿骄贫——不看钱待人</strong><br/>'
      '② <strong>勿厌故，勿喜新——不嫌旧不贪新</strong><br/><br/>'
      '<strong>一句话：平。</strong></p>'
      '<p><strong>后两句：怎么开口</strong><br/>'
      '① <strong>人不闲，勿事搅——人家忙别添事</strong><br/>'
      '② <strong>人不安，勿话扰——人家乱别添话</strong><br/><br/>'
      '<strong>一句话：识趣。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>看人不看钱，处旧不贪新</strong><br/>'
      '② <strong>人忙先等等，人乱先闭嘴</strong><br/><br/>'
      '<strong>一句话：心平，识趣。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 心要平，眼要活</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"勿谄富，勿骄贫。勿厌故，勿喜新。人不闲，勿事搅。人不安，勿话扰。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>不巴结富人不看轻穷人，不嫌旧不贪新；'
      '人家忙、人家乱的时候别去搅别去扰。</p><p>📖 心平识趣</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>待人不分钱多钱少，是把自己放在平地上；'
      '会看时候开口，是把别人放在心上——敬人就是敬自己。</p><p>💡 敬</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>心要平，眼要活；'
      '不看钱，不添乱。</p><p>🌱 心平识趣</p>'),
 72: '<p>这是「弟子规课堂」第三十四课：泛爱众第三段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「谄富」只是拍马屁吗？</h3>'
       '<p><strong>是巴结有钱人，多半想占便宜。</strong><br/><br/>'
       '① <strong>话说得甜、腰弯得低，为的是好处</strong><br/>'
       '② <strong>旁人一眼看穿，反倒没人敬他</strong><br/>'
       '③ <strong>记法：巴结来的脸，不值钱。</strong></p>'
       '<h3>❓ 旧的为什么不能厌？</h3>'
       '<p><strong>旧朋友、旧物件，是攒下来的情分。</strong><br/><br/>'
       '① <strong>用得久的书包、修过的桌子，都有你的日子</strong><br/>'
       '② <strong>处得久的朋友，知道你的底细，肯说真话</strong><br/>'
       '③ <strong>记法：旧的不嫌，新的不迷。</strong></p>'
       '<h3>❓ 怎么知道别人「不闲」「不安」？</h3>'
       '<p><strong>看脸色、听语气，先问一句。</strong><br/><br/>'
       '① <strong>人家手上不停、眉头皱着，就是忙</strong><br/>'
       '② <strong>开口先说「现在方便吗」，不算多礼</strong><br/>'
       '③ <strong>记法：先看再开口。</strong></p>'
       '<h3>❓ 我有急事，他正忙也要说吗？</h3>'
       '<p><strong>急事说重点，一句话讲完。</strong><br/><br/>'
       '① <strong>先说「急事，两句」，人家会给你时间</strong><br/>'
       '② <strong>绕半天不说正事，才真叫搅人</strong><br/>'
       '③ <strong>记法：急话短说，闲话另找时候。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 不看钱看人</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>对家里宽裕的同学、家里紧的同学，说话一个样，不巴结不看轻</strong>；'
       '<strong>这就是「勿谄富，勿骄贫」</strong>。</p><p>💡 不嫌旧不贪新</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>旧书包修一修接着用，老朋友常来往，不因为有了新伙伴就冷落人</strong>；'
       '<strong>这就是「勿厌故，勿喜新」</strong>。</p><p>🌱 挑时候说话</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>大人打电话、同学做题，先等一等；人家心里不痛快，别追着问</strong>；'
       '<strong>这就是「人不闲，勿事搅；人不安，勿话扰」</strong><br/><br/>'
       '<strong>本课的落点：待人有分寸。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第三段，看人不看钱，说话看时候。记牢：<strong>心平识趣</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">勿谄富，勿骄贫。勿厌故，勿喜新。'
       '人不闲，勿事搅。人不安，勿话扰。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第三段 · 心要平，眼要活。<strong>心平识趣</strong>。</p>'
       '<p>勿谄富，勿骄贫 · 有钱没钱一样待。<strong>看人不看钱</strong>。</p>'
       '<p>勿厌故，勿喜新 · 旧的不嫌，新的不迷。<strong>不嫌旧</strong>。</p>'
       '<p>人不闲，勿事搅 · 人家忙别添事。<strong>先等一等</strong>。</p>'
       '<p>人不安，勿话扰 · 人家乱别添话。<strong>陪着别追问</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第三段；前两段讲心里怎么想，'
       '这一段讲嘴上手上怎么做。</p>'
       '<div class="ds-quote">'),

 111: '<p>勿谄富，勿骄贫。勿厌故，勿喜新。人不闲，勿事搅。人不安，勿话扰。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「谄」「骄」「故」「搅」怎么讲。'
       '② 找人说事前先问一句「方便吗」。'
       '③ 想一想：你有什么旧东西一直舍不得。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>勿谄富，勿骄贫；勿厌故，勿喜新；'
       '人不闲，勿事搅；人不安，勿话扰。</strong></p></div>'),

 119: '            "勿谄富，勿骄贫。勿厌故，勿喜新。人不闲，勿事搅。人不安，勿话扰。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '574-wu-chan-fu';",

 59: '<!-- 4. 勿谄富勿骄贫·勿厌故勿喜新 -->',
 61: '<!-- 5. 人不闲勿事搅·人不安勿话扰 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「勿谄富」的「谄」是什么意思？', opts: ['巴结、讨好', '说话快', '开玩笑'], ans: 0, exp: '谄是巴结、讨好'},",
 "  {q: '2. 「勿骄贫」的「骄」是什么意思？', opts: ['傲慢、看不起人', '骄傲自满于成绩', '太阳很骄'], ans: 0, exp: '骄是傲慢、看不起人'},",
 "  {q: '3. 「勿厌故」的「故」是什么意思？', opts: ['旧的、原来的', '故意', '故事'], ans: 0, exp: '故是旧的、原来的'},",
 "  {q: '4. 「勿喜新」的「喜新」是什么意思？', opts: ['一味贪新、只喜欢新的', '喜欢高兴的事', '喜欢新年'], ans: 0, exp: '喜新是一味贪新'},",
 "  {q: '5. 「人不闲」的「闲」是什么意思？', opts: ['空闲', '闲话', '清闲的人'], ans: 0, exp: '闲是空闲'},",
 "  {q: '6. 「勿事搅」的「搅」是什么意思？', opts: ['打扰、搅扰', '搅拌', '搅动水'], ans: 0, exp: '搅是打扰、搅扰'},",
 "  {q: '7. 「人不安」的「安」是什么意思？', opts: ['安宁、心安', '安全帽', '安排'], ans: 0, exp: '安是安宁、心安'},",
 "  {q: '8. 「勿谄富，勿骄贫」是说什么？', opts: ['不看钱待人：不巴结有钱的，不看轻穷的', '别跟有钱人说话', '穷人要多帮'], ans: 0, exp: '有钱没钱，人一样待'},",
 "  {q: '9. 「人不安，勿话扰」是说什么？', opts: ['别人心里不安，别拿话去烦他', '别人不安就别理他', '不安的时候要多说话'], ans: 0, exp: '看人心乱不乱'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['待人有分寸：不看钱不嫌旧，人家忙乱时别添乱', '怎么挣钱', '怎么交新朋友'], ans: 0, exp: '心要平，眼要活'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("573-cai-da-zhe", "574-wu-chan-fu")
    out = out.replace("yaoyue574", "yaoyue575")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
