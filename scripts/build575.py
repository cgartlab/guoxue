#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build575: 以 574 为骨架，按行号替换文字生成第 575 课
《弟子规·泛爱众》第四段：人有短，切莫揭。人有私，切莫说。道人善，即是善。人知之，愈思勉。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 574 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/574-wu-chan-fu/index.html"
DST_DIR = f"{ROOT}/lessons/575-ren-you-duan"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十五课，泛爱众第四段。原文：「人有短，切莫揭。人有私，切莫说。'
        '道人善，即是善。人知之，愈思勉。」前两句讲别人有短处别当众揭，别人有私事别往外传；'
        '后两句讲多讲别人的好处，本身就是做好事，人家听见了会更想着往好里做。'
        '合起来：嘴上积德，揭短伤人，扬善养人。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("人","rén"),("有","yǒu"),("短","duǎn")]) + "，" + _r([("切","qiè"),("莫","mò"),("揭","jiē")]) + "。", True)
 + _p(_r([("人","rén"),("有","yǒu"),("私","sī")]) + "，" + _r([("切","qiè"),("莫","mò"),("说","shuō")]) + "。")
 + _p(_r([("道","dào"),("人","rén"),("善","shàn")]) + "，" + _r([("即","jí"),("是","shì"),("善","shàn")]) + "。")
 + _p(_r([("人","rén"),("知","zhī"),("之","zhī")]) + "，" + _r([("愈","yù"),("思","sī"),("勉","miǎn")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="人有短，切莫揭；道人善，即是善 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十五课：别人短处别揭，私事别传；多讲人好，就是行善。泛爱众第四段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/575-ren-you-duan/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/575-ren-you-duan/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 人有短切莫揭，道人善即是善 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">切莫揭</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第四段：人有短，切莫揭</p>'
      '<p class="cover-desc">别人有短处，别当众揭出来；别人有不愿人知的私事，别往外传。'
      '反过来，多讲别人的好处，本身就是做好事。'
      '一句话：嘴上积德，揭短伤人，扬善养人。</p><div class="cover-seal">善</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第四段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>别人有短处，千万不要当众揭出来；别人有不愿人知的私事，千万不要说出去。'
      '讲别人的好处，本身就是做好事；人家听见你夸他好，会更想着往好里做。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「短」是短处、缺点；「切莫」是千万不要；「揭」是揭出来、当众说出；'
      '「私」是隐私、不愿人知的事；「道」是说、讲；「即」就是；「愈」读 yù，是越、更加；'
      '「勉」是勉励、努力向善。这是《弟子规》第四门「泛爱众」的第四段。上一段讲待人的分寸，'
      '这一段专讲嘴上的分寸：别人的短处不揭，别人的私事不传，反过来多讲人好——'
      '一句话，嘴上积德。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>人有短，切莫揭；人有私，切莫说；道人善，即是善；人知之，愈思勉。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 嘴上积德</h2>'
      '<p style="margin:0"><strong>先说「别说什么」</strong><br/>'
      '① <strong>别人的短处，不当众揭</strong><br/>'
      '② <strong>别人的私事，不往外传</strong><br/><br/>'
      '<strong>一句话：嘴要严。</strong></p>'
      '<p><strong>再说「该说什么」</strong><br/>'
      '① <strong>别人的好处，多说几句</strong><br/>'
      '② <strong>好话传到他耳朵里，他更肯往好里做</strong><br/><br/>'
      '<strong>一句话：嘴要甜。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「守住别人的脸」</strong><br/>'
      '② <strong>后两句讲「成全别人的好」</strong><br/><br/>'
      '<strong>一句话：不揭短，多扬善。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>人有短，切莫揭；人有私，切莫说</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>短：短处、缺点；揭：揭出来、当众说</strong><br/>'
      '② <strong>私：隐私、不愿人知的事；切莫：千万不要</strong><br/><br/>'
      '<strong>一句话：别人的脸，别去揭。</strong></p>'
      '<p><strong>人有短，切莫揭</strong><br/>'
      '① <strong>同学答错题、摔一跤，别笑、别到处说</strong><br/>'
      '② <strong>当众揭人短，他记一辈子，你落个刻薄名</strong><br/><br/>'
      '<strong>一句话：留人一分面子。</strong></p>'
      '<p><strong>人有私，切莫说</strong><br/>'
      '① <strong>人家家里的事、心里的苦，说给你是信你</strong><br/>'
      '② <strong>你一传，信就断了，还添一堆闲话</strong><br/><br/>'
      '<strong>一句话：私事烂在肚子里。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>道人善，即是善；人知之，愈思勉</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>道：说、讲；即：就是</strong><br/>'
      '② <strong>愈 yù：越、更加；勉：勉励、努力向善</strong><br/><br/>'
      '<strong>一句话：说人好，就是做好事。</strong></p>'
      '<p><strong>道人善，即是善</strong><br/>'
      '① <strong>夸人不用花钱，却让人心里暖半天</strong><br/>'
      '② <strong>说真有的好，不是编，不是拍马屁</strong><br/><br/>'
      '<strong>一句话：好话也是功德。</strong></p>'
      '<p><strong>人知之，愈思勉</strong><br/>'
      '① <strong>他听见你夸，就想更对得起这句话</strong><br/>'
      '② <strong>越夸越肯做好，好人就这么长出来</strong><br/><br/>'
      '<strong>一句话：扬善，善更长。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 不说短，多说善</h2>'
      '<p style="margin:0"><strong>前两句讲「嘴要严」</strong><br/>'
      '① <strong>短处不揭，私事不传</strong><br/>'
      '② <strong>守住的是别人的脸面</strong><br/><br/>'
      '<strong>一句话：不伤人。</strong></p>'
      '<p><strong>后两句讲「嘴要甜」</strong><br/>'
      '① <strong>好处多说，说真不编</strong><br/>'
      '② <strong>成全的是别人的志气</strong><br/><br/>'
      '<strong>一句话：成全人。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>同学答错，不笑；他答对了，说一句「这题你真行」</strong><br/>'
      '② <strong>别人跟你说的家事，不跟第三个人讲</strong><br/><br/>'
      '<strong>一句话：嘴上有德。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：不该说的</strong><br/>'
      '① <strong>人有短，切莫揭——短处别当众说</strong><br/>'
      '② <strong>人有私，切莫说——私事别往外传</strong><br/><br/>'
      '<strong>一句话：守。</strong></p>'
      '<p><strong>后两句：该说的</strong><br/>'
      '① <strong>道人善，即是善——讲人好就是行善</strong><br/>'
      '② <strong>人知之，愈思勉——他听见更肯做好</strong><br/><br/>'
      '<strong>一句话：扬。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>短处不揭，私事不传</strong><br/>'
      '② <strong>好处多说，好话传开</strong><br/><br/>'
      '<strong>一句话：守住嘴，成全人。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 揭短伤人，扬善养人</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"人有短，切莫揭。人有私，切莫说。道人善，即是善。人知之，愈思勉。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>别人短处别揭，私事别传；'
      '多讲人好，就是行善。</p><p>📖 嘴上积德</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>揭人一分短，丢自己一分厚道；'
      '扬人一分善，添世间一分好人——嘴是自己的，福是自己攒的。</p><p>💡 厚道</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>不揭短，不传私；'
      '多讲人好。</p><p>🌱 嘴上积德</p>'),
 72: '<p>这是「弟子规课堂」第三十五课：泛爱众第四段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 他做得不对，也不能说吗？</h3>'
       '<p><strong>该说，但当面说、私下说。</strong><br/><br/>'
       '① <strong>为他好，就当面讲，不背后讲</strong><br/>'
       '② <strong>当众揭短是让他丢脸，不是帮他改</strong><br/>'
       '③ <strong>记法：当面说事，背后说好。</strong></p>'
       '<h3>❓ 「揭短」和「批评」有什么不一样？</h3>'
       '<p><strong>看是为他好，还是为看他丢脸。</strong><br/><br/>'
       '① <strong>批评：就事论事，说完给办法</strong><br/>'
       '② <strong>揭短：拿人痛处当笑话，说给一堆人听</strong><br/>'
       '③ <strong>记法：想帮他，就小声说。</strong></p>'
       '<h3>❓ 夸人会不会变成拍马屁？</h3>'
       '<p><strong>说真有的好，就不是。</strong><br/><br/>'
       '① <strong>他确实做得好，说出来，叫公道</strong><br/>'
       '② <strong>编出来的好话，叫奉承，一听就假</strong><br/>'
       '③ <strong>记法：真话才值钱。</strong></p>'
       '<h3>❓ 在群里、网上说人坏话，也算吗？</h3>'
       '<p><strong>一样算，还传得更快。</strong><br/><br/>'
       '① <strong>手指一点，几十人看见，收不回来</strong><br/>'
       '② <strong>伤了人，也把自己的名声搭进去</strong><br/>'
       '③ <strong>记法：网上也是嘴，一样要积德。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 不揭短</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学答错题、摔了跤，不笑、不学、不传</strong>；'
       '<strong>这就是「人有短，切莫揭」</strong>。</p><p>💡 不传私</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>别人跟你说的家里事、心里话，不跟第三个人讲</strong>；'
       '<strong>这就是「人有私，切莫说」</strong>。</p><p>🌱 多讲人好</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>谁做了什么好事，说给第三个人听，说真不编</strong>；'
       '<strong>这就是「道人善，即是善」</strong><br/><br/>'
       '<strong>本课的落点：嘴上积德，揭短伤人，扬善养人。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第四段，短处不揭，好话多说。记牢：<strong>嘴上积德</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">人有短，切莫揭。人有私，切莫说。'
       '道人善，即是善。人知之，愈思勉。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第四段 · 不揭短，多扬善。<strong>嘴上积德</strong>。</p>'
       '<p>人有短，切莫揭 · 缺点别当众说。<strong>留人面子</strong>。</p>'
       '<p>人有私，切莫说 · 私事烂在肚里。<strong>不外传</strong>。</p>'
       '<p>道人善，即是善 · 讲人好就是行善。<strong>好话是功德</strong>。</p>'
       '<p>人知之，愈思勉 · 听见夸奖更向上。<strong>越夸越好</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第四段；上一段讲待人的分寸，'
       '这一段专讲嘴上的分寸。</p>'
       '<div class="ds-quote">'),

 111: '<p>人有短，切莫揭。人有私，切莫说。道人善，即是善。人知之，愈思勉。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「揭」「私」「即」「愈」怎么讲。'
       '② 今天夸一个人，说他真做过的哪件事。'
       '③ 想一想：你听过谁传你的闲话，心里什么味儿。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>人有短，切莫揭；人有私，切莫说；'
       '道人善，即是善；人知之，愈思勉。</strong></p></div>'),

 119: '            "人有短，切莫揭。人有私，切莫说。道人善，即是善。人知之，愈思勉。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '575-ren-you-duan';",

 59: '<!-- 4. 人有短切莫揭·人有私切莫说 -->',
 61: '<!-- 5. 道人善即是善·人知之愈思勉 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「人有短」的「短」是什么意思？', opts: ['短处、缺点', '长短', '短裤'], ans: 0, exp: '短是短处、缺点'},",
 "  {q: '2. 「切莫揭」的「揭」是什么意思？', opts: ['揭出来、当众说出', '揭开锅盖', '揭开被子'], ans: 0, exp: '揭是揭出来、当众说出'},",
 "  {q: '3. 「人有私」的「私」是什么意思？', opts: ['隐私、不愿人知的事', '私人的钱', '私下说话'], ans: 0, exp: '私是隐私、不愿人知的事'},",
 "  {q: '4. 「道人善」的「道」是什么意思？', opts: ['说、讲', '道路', '道理'], ans: 0, exp: '道是说、讲'},",
 "  {q: '5. 「即是善」的「即」是什么意思？', opts: ['就是', '立刻', '即使'], ans: 0, exp: '即就是'},",
 "  {q: '6. 「愈思勉」的「愈」怎么读、什么意思？', opts: ['yù，越、更加', 'yǔ，痊愈', 'yú，愉快'], ans: 0, exp: '愈读 yù，是越、更加'},",
 "  {q: '7. 「愈思勉」的「勉」是什么意思？', opts: ['勉励、努力向善', '勉强', '免去'], ans: 0, exp: '勉是勉励、努力'},",
 "  {q: '8. 「人有短，切莫揭」是说什么？', opts: ['别人有缺点，别当众揭出来', '别人有缺点，要到处说', '别人没缺点'], ans: 0, exp: '留人一分面子'},",
 "  {q: '9. 「道人善，即是善」是说什么？', opts: ['讲别人的好处，本身就是做好事', '说人好是拍马屁', '好话别多说'], ans: 0, exp: '好话也是功德'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['嘴上积德：不揭短不传私，多讲人好', '怎么说话好听', '怎么让人怕你'], ans: 0, exp: '揭短伤人，扬善养人'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("574-wu-chan-fu", "575-ren-you-duan")
    out = out.replace("yaoyue575", "yaoyue576")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
