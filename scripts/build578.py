#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build578: 以 577 为骨架，按行号替换文字生成第 578 课
《弟子规·泛爱众》第七段：恩欲报，怨欲忘。报怨短，报恩长。待婢仆，身贵端。虽贵端，慈而宽。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 577 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/577-qu-yu-fen-xiao/index.html"
DST_DIR = f"{ROOT}/lessons/578-en-yu-bao"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十八课，泛爱众第七段。原文：「恩欲报，怨欲忘。报怨短，报恩长。'
        '待婢仆，身贵端。虽贵端，慈而宽。」前两句讲欠人的恩要记着还，心里的怨要学着放；'
        '报怨别拖长，报恩别嫌长。后两句讲对身边的人——端正是根本，光端不行，还要慈和宽厚。'
        '合起来：恩怨分明，宽严有度。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("恩","ēn"),("欲","yù"),("报","bào")]) + "，" + _r([("怨","yuàn"),("欲","yù"),("忘","wàng")]) + "。", True)
 + _p(_r([("报","bào"),("怨","yuàn"),("短","duǎn")]) + "，" + _r([("报","bào"),("恩","ēn"),("长","cháng")]) + "。")
 + _p(_r([("待","dài"),("婢","bì"),("仆","pú")]) + "，" + _r([("身","shēn"),("贵","guì"),("端","duān")]) + "。")
 + _p(_r([("虽","suī"),("贵","guì"),("端","duān")]) + "，" + _r([("慈","cí"),("而","ér"),("宽","kuān")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="恩欲报，怨欲忘；身贵端，慈而宽 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十八课：恩要记着还，怨要学着放；对身边人端正要紧，慈宽也要紧。泛爱众第七段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/578-en-yu-bao/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/578-en-yu-bao/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 恩欲报怨欲忘，身贵端慈而宽 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">恩怨宽严</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第七段：恩欲报，怨欲忘</p>'
      '<p class="cover-desc">人家给过的好处，记着还；心里存着的怨，学着放。'
      '对身边比自己弱的人，自己先站正，光正还不行，还要慈、还要宽。'
      '一句话：恩怨分明，宽严有度。</p><div class="cover-seal">恩</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第七段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>人家对我的恩，要想着报答；心里的怨，要学着忘掉。报怨的时间越短越好，报恩的时间越长越好。'
      '对待身边比自己弱的人，自己先要站得端正；光是端正还不够，还要慈和宽厚。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「恩」是人家给的好处；「报」是还报、报答；「怨」是心里的不满和恨；「忘」是放下、不记着；'
      '「婢仆」是旧时家里干活、地位低的人，今天可以理解成身边比自己弱、要靠你照顾的人；'
      '「贵」是最要紧；「端」是端正、自己站得正；「慈」是慈爱；「宽」是宽厚。'
      '这是《弟子规》第四门「泛爱众」的第七段。上一段讲取与和将心比心，这一段讲两件事：'
      '心里怎么处理恩怨，手上怎么对待比自己弱的人——一句话，恩怨分明，宽严有度。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>恩欲报，怨欲忘；报怨短，报恩长；待婢仆，身贵端；虽贵端，慈而宽。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 恩怨分明，宽严有度</h2>'
      '<p style="margin:0"><strong>先说「心里的账」</strong><br/>'
      '① <strong>恩要记：谁帮过我，别忘了</strong><br/>'
      '② <strong>怨要放：谁亏过我，别老想</strong><br/><br/>'
      '<strong>一句话：多记恩，少记仇。</strong></p>'
      '<p><strong>再说「手上的分寸」</strong><br/>'
      '① <strong>自己先站正，别人才服</strong><br/>'
      '② <strong>正了还要慈、还要宽，别只剩硬</strong><br/><br/>'
      '<strong>一句话：正得住，也软得下。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「心」</strong><br/>'
      '② <strong>后两句讲「待下人」</strong><br/><br/>'
      '<strong>一句话：心上宽，身上正。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>恩欲报，怨欲忘；报怨短，报恩长</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>恩：人家给的好处；报：还报</strong><br/>'
      '② <strong>怨：心里的不满；忘：放下不记</strong><br/><br/>'
      '<strong>一句话：恩记着，怨丢掉。</strong></p>'
      '<p><strong>恩欲报，怨欲忘</strong><br/>'
      '① <strong>别人帮过你一次，记一辈子</strong><br/>'
      '② <strong>别人亏过你一次，别翻来覆去嚼</strong><br/><br/>'
      '<strong>一句话：记好不记坏。</strong></p>'
      '<p><strong>报怨短，报恩长</strong><br/>'
      '① <strong>怨，早点过去；恩，久久记着</strong><br/>'
      '② <strong>心里装的多是恩，人就轻快</strong><br/><br/>'
      '<strong>一句话：短怨长恩。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>待婢仆，身贵端；虽贵端，慈而宽</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>婢仆 bì pú：旧时家里干活、地位低的人</strong><br/>'
      '② <strong>端：端正；慈：慈爱；宽：宽厚</strong><br/><br/>'
      '<strong>一句话：今天指比你弱、靠你照顾的人。</strong></p>'
      '<p><strong>待婢仆，身贵端</strong><br/>'
      '① <strong>你手上有点权，先把自己站正</strong><br/>'
      '② <strong>自己不贪不懒，说话才有分量</strong><br/><br/>'
      '<strong>一句话：先正己，再正人。</strong></p>'
      '<p><strong>虽贵端，慈而宽</strong><br/>'
      '① <strong>光正不慈，就成了冷硬刻薄</strong><br/>'
      '② <strong>该严的地方严，能容的地方容</strong><br/><br/>'
      '<strong>一句话：正而不刻。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 一恩一怨，一正一宽</h2>'
      '<p style="margin:0"><strong>前两句讲「心上的账」</strong><br/>'
      '① <strong>恩：记着、还着、久久不忘</strong><br/>'
      '② <strong>怨：放下、缩短、别放心上</strong><br/><br/>'
      '<strong>一句话：多存恩，少存怨。</strong></p>'
      '<p><strong>后两句讲「手上的权」</strong><br/>'
      '① <strong>端：自己有样子，才谈得上管人</strong><br/>'
      '② <strong>宽：有样子还要有温度</strong><br/><br/>'
      '<strong>一句话：正身，宽下。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>想起帮过你的人，说声谢、还个情</strong><br/>'
      '② <strong>对弟弟妹妹、同桌、值日的同学，别摆架子</strong><br/><br/>'
      '<strong>一句话：念恩，宽人。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：恩怨怎么处理</strong><br/>'
      '① <strong>恩欲报，怨欲忘——恩记着，怨放下</strong><br/>'
      '② <strong>报怨短，报恩长——怨要短，恩要长</strong><br/><br/>'
      '<strong>一句话：厚。</strong></p>'
      '<p><strong>后两句：弱于你的人怎么待</strong><br/>'
      '① <strong>身贵端——自己先站正</strong><br/>'
      '② <strong>慈而宽——再慈一点、宽一点</strong><br/><br/>'
      '<strong>一句话：仁。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>恩长怨短</strong><br/>'
      '② <strong>身正心宽</strong><br/><br/>'
      '<strong>一句话：恩怨分明，宽严有度。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 恩怨分明，宽严有度</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"恩欲报，怨欲忘。报怨短，报恩长。待婢仆，身贵端。虽贵端，慈而宽。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>受人恩要还，心里怨要放；'
      '报怨短、报恩长；对身边弱的人，自己先端正，还要慈宽。</p><p>📖 恩长怨短</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>记恩，是心里有光；忘怨，是心里腾空；'
      '身端是敬，慈宽是仁——对上不媚，对下不傲。</p><p>💡 仁</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>恩怨分明，宽严有度；'
      '恩记着，怨放开。</p><p>🌱 心宽身正</p>'),
 72: '<p>这是「弟子规课堂」第三十八课：泛爱众第七段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「怨欲忘」是不是受了委屈也不吭声？</h3>'
       '<p><strong>不是不吭声，是不记仇。</strong><br/><br/>'
       '① <strong>该说的当面说清，说完就放下</strong><br/>'
       '② <strong>忘的是心里的恨，不是事情的理</strong><br/>'
       '③ <strong>记法：事说清，心放开。</strong></p>'
       '<h3>❓ 「报恩长」是不是一辈子还不完？</h3>'
       '<p><strong>长，是长久记着，不是永远欠着。</strong><br/><br/>'
       '① <strong>能还的还，还不了的就传下去帮别人</strong><br/>'
       '② <strong>记着人家的好，本身就是一种还</strong><br/>'
       '③ <strong>记法：恩不断，心不欠。</strong></p>'
       '<h3>❓ 今天没有「婢仆」，这两句还有用吗？</h3>'
       '<p><strong>太有用了，讲的是「对下」的态度。</strong><br/><br/>'
       '① <strong>对弟弟妹妹、值日同学、比你小的孩子</strong><br/>'
       '② <strong>你有点权的时候，最容易露出真性情</strong><br/>'
       '③ <strong>记法：对下不傲，才算真好。</strong></p>'
       '<h3>❓ 「慈而宽」会不会变成没原则？</h3>'
       '<p><strong>宽是给人余地，不是没有底线。</strong><br/><br/>'
       '① <strong>该守的规矩照守，说话别伤人</strong><br/>'
       '② <strong>对人宽，对事不松</strong><br/>'
       '③ <strong>记法：心软，手不软。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 记恩</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>想起谁帮过你，说声谢、找机会还一下</strong>；'
       '<strong>这就是「恩欲报」</strong>。</p><p>💡 放怨</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>跟人闹了别扭，说清就放下，别在背后反复嚼</strong>；'
       '<strong>这就是「怨欲忘」</strong>。</p><p>🌱 对下宽</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>对弟弟妹妹、比你小的同学，自己有样子，也别摆架子</strong>；'
       '<strong>这就是「身贵端，慈而宽」</strong><br/><br/>'
       '<strong>本课的落点：恩怨分明，宽严有度。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第七段，记恩放怨，正身宽下。记牢：<strong>恩怨分明</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">恩欲报，怨欲忘。报怨短，报恩长。'
       '待婢仆，身贵端。虽贵端，慈而宽。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第七段 · 心上宽，身上正。<strong>恩怨分明</strong>。</p>'
       '<p>恩欲报，怨欲忘 · 恩记着怨放下。<strong>记好不记坏</strong>。</p>'
       '<p>报怨短，报恩长 · 怨早点过。<strong>短怨长恩</strong>。</p>'
       '<p>待婢仆，身贵端 · 自己先站正。<strong>先正己</strong>。</p>'
       '<p>虽贵端，慈而宽 · 正了还要慈。<strong>正而不刻</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第七段；上一段讲取与和将心比心，'
       '这一段讲恩怨怎么放、对下怎么待。</p>'
       '<div class="ds-quote">'),

 111: '<p>恩欲报，怨欲忘。报怨短，报恩长。待婢仆，身贵端。虽贵端，慈而宽。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「婢仆」「端」「慈」「宽」怎么讲。'
       '② 今天向一个帮过你的人道谢。'
       '③ 想一想：你对弟弟妹妹有没有摆过架子。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>恩欲报，怨欲忘；报怨短，报恩长；'
       '待婢仆，身贵端；虽贵端，慈而宽。</strong></p></div>'),

 119: '            "恩欲报，怨欲忘。报怨短，报恩长。待婢仆，身贵端。虽贵端，慈而宽。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '578-en-yu-bao';",

 59: '<!-- 4. 恩欲报怨欲忘·报怨短报恩长 -->',
 61: '<!-- 5. 待婢仆身贵端·虽贵端慈而宽 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「恩欲报」的「恩」是什么意思？', opts: ['人家给的好处', '恩人姓名', '恩爱的感情'], ans: 0, exp: '恩是人家给的好处'},",
 "  {q: '2. 「怨欲忘」的「怨」是什么意思？', opts: ['心里的不满和恨', '埋怨天气', '愿望'], ans: 0, exp: '怨是心里的不满'},",
 "  {q: '3. 「报怨短」的「短」是什么意思？', opts: ['时间短、早点过去', '长短的短', '说人短处'], ans: 0, exp: '短是早点过去'},",
 "  {q: '4. 「报恩长」的「长」怎么读，什么意思？', opts: ['cháng，长久记着', 'zhǎng，长大', 'zhàng，多余'], ans: 0, exp: '长读 cháng，是长久'},",
 "  {q: '5. 「待婢仆」的「婢仆」指什么？', opts: ['旧时家里干活、地位低的人', '奴婢的名字', '仆人穿的衣裳'], ans: 0, exp: '婢仆指地位低、干活的人'},",
 "  {q: '6. 「身贵端」的「端」是什么意思？', opts: ['端正，自己站得正', '端着碗', '两端'], ans: 0, exp: '端是端正'},",
 "  {q: '7. 「虽贵端，慈而宽」是说什么？', opts: ['光端正还不够，还要慈爱宽厚', '只要端正就够了', '要宽就别端正'], ans: 0, exp: '正还要慈宽'},",
 "  {q: '8. 「待婢仆，身贵端」今天怎么理解？', opts: ['对身边比自己弱的人，自己先做正', '不用管比自己弱的人', '让弱者自己端正'], ans: 0, exp: '对下要先正己'},",
 "  {q: '9. 「报怨短，报恩长」合起来是说什么？', opts: ['怨早点放下，恩长久记着', '恩早点还，怨记一辈子', '恩怨都不要管'], ans: 0, exp: '短怨长恩'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['恩怨分明、宽严有度：记恩放怨，正身宽下', '怎么管住下人', '怎么让别人报恩'], ans: 0, exp: '恩怨分明，宽严有度'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("577-qu-yu-fen-xiao", "578-en-yu-bao")
    out = out.replace("yaoyue578", "yaoyue579")
    out = out.replace("第三十七课", "第三十八课")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
