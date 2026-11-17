#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build582: 以 581 为骨架，按行号替换文字生成第 582 课
《弟子规·余力学文》第一段：不力行，但学文。长浮华，成何人。但力行，不学文。任己见，昧理真。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/581-neng-qin-ren/index.html"
DST_DIR = f"{ROOT}/lessons/582-bu-li-xing"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十二课，余力学文第一段。原文：「不力行，但学文。长浮华，成何人。'
        '但力行，不学文。任己见，昧理真。」前两句讲光学不做，越长越浮，成了什么人呢；'
        '后两句讲光做不学，凭自己那点见识，看不明白真正的道理。合起来：学和做，两条腿走路。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("不","bù"),("力","lì"),("行","xíng")]) + "，" + _r([("但","dàn"),("学","xué"),("文","wén")]) + "。", True)
 + _p(_r([("长","zhǎng"),("浮","fú"),("华","huá")]) + "，" + _r([("成","chéng"),("何","hé"),("人","rén")]) + "。")
 + _p(_r([("但","dàn"),("力","lì"),("行","xíng")]) + "，" + _r([("不","bù"),("学","xué"),("文","wén")]) + "。")
 + _p(_r([("任","rèn"),("己","jǐ"),("见","jiàn")]) + "，" + _r([("昧","mèi"),("理","lǐ"),("真","zhēn")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="不力行但学文，但力行不学文 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十二课：光学不做越长越浮，光做不学凭己见昧真理。学和做，两条腿走路。余力学文第一段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/582-bu-li-xing/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/582-bu-li-xing/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 不力行但学文，但力行不学文 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">知行并进</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文第一段：不力行，但学文</p>'
      '<p class="cover-desc">光学不做，越学越浮，嘴上会说，手上不会；'
      '光做不学，凭自己那点见识，看不明白真正的道理。'
      '一句话：学和做，两条腿走路。</p><div class="cover-seal">行</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文第一段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>光学书本、不肯动手去做，只会越长越浮华，那能成个什么人呢？'
      '只管闷头做、不肯读书学习，就会凭自己的一点见解行事，辨不清真正的道理。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「力行」是实打实去做；「但」是只、光；「学文」是读书学文；'
      '「长」读 zhǎng，是增长；「浮华」是表面好看、内里空虚；「成何人」是能成什么人；'
      '「任己见」是凭自己一个人的看法；「昧」是看不清、不明白；「理真」是真正的道理。'
      '这是《弟子规》最后一门「余力学文」的第一段。前六门讲做人做事，这一门讲读书学习：'
      '为什么叫「余力」？先把人做好，有余力再学文——学和做，两条腿走路。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>不力行，但学文；长浮华，成何人；但力行，不学文；任己见，昧理真。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 一条腿，走不稳</h2>'
      '<p style="margin:0"><strong>只学不做</strong><br/>'
      '① <strong>书背得熟，事不会做</strong><br/>'
      '② <strong>嘴上讲道理，手上没本事</strong><br/><br/>'
      '<strong>一句话：越学越浮。</strong></p>'
      '<p><strong>只做不学</strong><br/>'
      '① <strong>肯下力，可不知道门道</strong><br/>'
      '② <strong>错了还以为自己有道理</strong><br/><br/>'
      '<strong>一句话：越做越窄。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句批「光说不练」</strong><br/>'
      '② <strong>后两句批「光练不学」</strong><br/><br/>'
      '<strong>一句话：学和做，缺一不可。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>不力行，但学文；长浮华，成何人</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>力行：实打实去做；但：只、光</strong><br/>'
      '② <strong>长 zhǎng：增长；浮华：表面好看内里空</strong><br/><br/>'
      '<strong>一句话：会说不会做，最误人。</strong></p>'
      '<p><strong>不力行，但学文</strong><br/>'
      '① <strong>「孝顺」背得滚瓜烂熟，回家碗都不端</strong><br/>'
      '② <strong>道理讲得头头是道，自己的事一团乱</strong><br/><br/>'
      '<strong>一句话：学问停在嘴上。</strong></p>'
      '<p><strong>长浮华，成何人</strong><br/>'
      '① <strong>越学越会摆样子，越不会办事</strong><br/>'
      '② <strong>这样长下去，能成个什么人呢</strong><br/><br/>'
      '<strong>一句话：浮华不长人。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>但力行，不学文；任己见，昧理真</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>任己见：凭自己一个人的看法</strong><br/>'
      '② <strong>昧 mèi：看不清；理真：真正的道理</strong><br/><br/>'
      '<strong>一句话：只凭自己，容易走偏。</strong></p>'
      '<p><strong>但力行，不学文</strong><br/>'
      '① <strong>肯干，可不知道别人怎么干更好</strong><br/>'
      '② <strong>同一个错犯十遍，还当是本事</strong><br/><br/>'
      '<strong>一句话：力气使在错处。</strong></p>'
      '<p><strong>任己见，昧理真</strong><br/>'
      '① <strong>只信自己那一套，听不进别人</strong><br/>'
      '② <strong>越走越偏，还以为自己最对</strong><br/><br/>'
      '<strong>一句话：不学，就看不见真道理。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 两条腿，才站得稳</h2>'
      '<p style="margin:0"><strong>学要跟做走</strong><br/>'
      '① <strong>学一句，回家做一句</strong><br/>'
      '② <strong>做不出来的，不算学会</strong><br/><br/>'
      '<strong>一句话：学了就用。</strong></p>'
      '<p><strong>做要跟学走</strong><br/>'
      '① <strong>做之前先问「该怎么做才对」</strong><br/>'
      '② <strong>做完想想「哪里能做得更好」</strong><br/><br/>'
      '<strong>一句话：做了就长。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>今天学的道理，找一件小事做出来</strong><br/>'
      '② <strong>做事遇上不会的，去问、去查、去看书</strong><br/><br/>'
      '<strong>一句话：学做合一。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句一正一反</h2>'
      '<p style="margin:0"><strong>前两句：光说不练</strong><br/>'
      '① <strong>不力行，但学文——只学不做</strong><br/>'
      '② <strong>长浮华，成何人——越长越空</strong><br/><br/>'
      '<strong>一句话：空。</strong></p>'
      '<p><strong>后两句：光练不学</strong><br/>'
      '① <strong>但力行，不学文——只做不学</strong><br/>'
      '② <strong>任己见，昧理真——越做越偏</strong><br/><br/>'
      '<strong>一句话：偏。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>光说不练，是空</strong><br/>'
      '② <strong>光练不学，是偏</strong><br/><br/>'
      '<strong>一句话：又学又做，才成。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 知行并进</h2>'
      '<p>四句话，两个偏——</p>'
      '<h3>"不力行，但学文。长浮华，成何人。但力行，不学文。任己见，昧理真。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>光学不做越学越浮，'
      '光做不学凭己见看不清道理。</p><p>📖 两条腿</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>学是眼睛，做是脚；'
      '没眼睛会走偏，没脚走不动——学问要从手上过一遍，才算自己的。</p><p>💡 知行</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>知行并进；'
      '学了就做，做了就学。</p><p>🌱 学做合一</p>'),
 72: '<p>这是「余力学文课堂」第四十二课：余力学文第一段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「长浮华」到底是什么意思？</h3>'
       '<p><strong>表面好看，里子是空的。</strong><br/><br/>'
       '① <strong>会背会讲，就是不会做</strong><br/>'
       '② <strong>说起来一套一套，做起来一样不行</strong><br/>'
       '③ <strong>记法：花架子，经不起事。</strong></p>'
       '<h3>❓ 小学生也要「力行」吗？</h3>'
       '<p><strong>最该力行的就是小学生。</strong><br/><br/>'
       '① <strong>学问是从小事上练出来的：收拾、让座、还东西</strong><br/>'
       '② <strong>年纪小，正好把手脚练顺</strong><br/>'
       '③ <strong>记法：先会做人，再谈学问。</strong></p>'
       '<h3>❓ 「任己见」为什么不好？</h3>'
       '<p><strong>一个人看见的，总是一个角。</strong><br/><br/>'
       '① <strong>你想到的办法，前人早试过</strong><br/>'
       '② <strong>听一句、看一页，能省很多弯路</strong><br/>'
       '③ <strong>记法：先学规矩，再谈自己的主意。</strong></p>'
       '<h3>❓ 读书和做事，时间怎么分？</h3>'
       '<p><strong>不用分得那么清，边做边学。</strong><br/><br/>'
       '① <strong>先做完该做的（功课、家务），再读书</strong><br/>'
       '② <strong>读的时候想着「这事我怎么做」，读完就试一次</strong><br/>'
       '③ <strong>记法：余力学文，不是不学，是别只顾学。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 学一句做一句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>今天学到一句道理，找一件小事做出来</strong>；'
       '<strong>这就是「不力行，但学文」的反面</strong>。</p><p>💡 做事前先问</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>不会做的，先问一句「该怎么做才对」</strong>；'
       '<strong>这就是「任己见，昧理真」的反面</strong>。</p><p>🌱 做完回头想</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>做完一件小事，回头想哪里能更好</strong>；'
       '<strong>这就是「学」与「行」接上了</strong><br/><br/>'
       '<strong>本课的落点：知行并进。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天开新门「余力学文」，学与做两条腿。记牢：<strong>知行并进</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">不力行，但学文。长浮华，成何人。'
       '但力行，不学文。任己见，昧理真。</p><p>回顾本课要点:</p>'
       '<p>余力学文第一段 · 两个偏，一条正路。<strong>知行并进</strong>。</p>'
       '<p>不力行，但学文 · 只学不做。<strong>学问停在嘴上</strong>。</p>'
       '<p>长浮华，成何人 · 越长越空。<strong>花架子</strong>。</p>'
       '<p>但力行，不学文 · 只做不学。<strong>力气使在错处</strong>。</p>'
       '<p>任己见，昧理真 · 越做越偏。<strong>看不见真道理</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>最后一门「余力学文」开头；'
       '前面讲做人做事，这一门讲读书学习。</p>'
       '<div class="ds-quote">'),

 111: '<p>不力行，但学文。长浮华，成何人。但力行，不学文。任己见，昧理真。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「力行」「浮华」「任己见」「昧」怎么讲。'
       '② 今天把学到的一句道理做出来。'
       '③ 想一想：你有没有「会说不会做」的事。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>不力行，但学文；长浮华，成何人；'
       '但力行，不学文；任己见，昧理真。</strong></p></div>'),

 119: '            "不力行，但学文。长浮华，成何人。但力行，不学文。任己见，昧理真。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '582-bu-li-xing';",

 59: '<!-- 4. 不力行但学文·长浮华成何人 -->',
 61: '<!-- 5. 但力行不学文·任己见昧理真 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「不力行」的「力行」是什么意思？', opts: ['实打实去做', '用力走路', '努力就行'], ans: 0, exp: '力行是实做'},",
 "  {q: '2. 「但学文」的「但」是什么意思？', opts: ['只、光', '但是', '不但'], ans: 0, exp: '但是只、光的意思'},",
 "  {q: '3. 「长浮华」的「长」怎么读、什么意思？', opts: ['zhǎng，增长', 'cháng，长短', 'zhàng，多余'], ans: 0, exp: '长读 zhǎng，是增长'},",
 "  {q: '4. 「浮华」是什么意思？', opts: ['表面好看、内里空虚', '水上有花', '华丽漂亮'], ans: 0, exp: '浮华是表面好看内里空'},",
 "  {q: '5. 「成何人」是什么意思？', opts: ['能成个什么人呢', '成了哪个人', '什么人成功了'], ans: 0, exp: '成何人是能成什么人'},",
 "  {q: '6. 「任己见」的「任」是什么意思？', opts: ['任凭、只凭', '任务', '信任别人'], ans: 0, exp: '任是只凭'},",
 "  {q: '7. 「昧理真」的「昧」是什么意思？', opts: ['看不清、不明白', '昧心', '愚昧无知的人'], ans: 0, exp: '昧是看不清'},",
 "  {q: '8. 「不力行，但学文」会怎样？', opts: ['越长越浮华，成了空架子', '学问越来越好', '身体越来越好'], ans: 0, exp: '长浮华，成何人'},",
 "  {q: '9. 「但力行，不学文」会怎样？', opts: ['凭自己一点见解，辨不清真道理', '力气越来越大', '做事更麻利'], ans: 0, exp: '任己见，昧理真'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['学和做两条腿走路：学了要做，做要学', '读书最重要', '做事最重要'], ans: 0, exp: '知行并进'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("581-neng-qin-ren", "582-bu-li-xing")
    out = out.replace("yaoyue581", "yaoyue582")
    out = out.replace("第四十一课", "第四十二课")
    out = out.replace("亲仁课堂", "余力学文课堂")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
