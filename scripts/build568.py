#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build568: 以 567 为骨架，按行号替换文字生成第 568 课
《弟子规·信》第五段：见人恶，即内省。有则改，无加警。唯德学，唯才艺。不如人，当自砺。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 567 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/567-bei-shuo-chang/index.html"
DST_DIR = f"{ROOT}/lessons/568-jian-ren-e"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第二十八课，信第五段。原文：「见人恶，即内省。有则改，无加警。'
        '唯德学，唯才艺。不如人，当自砺。」前四句讲看见别人的坏处，先回头反省自己有没有，'
        '有的就改，没有也要加倍警惕；后四句讲要比的只有品德学问和才能技艺，'
        '这些不如别人，就该自己下功夫磨炼。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("见","jiàn"),("人","rén"),("恶","è")]) + "，" + _r([("即","jí"),("内","nèi"),("省","xǐng")]) + "。", True)
 + _p(_r([("有","yǒu"),("则","zé"),("改","gǎi")]) + "，" + _r([("无","wú"),("加","jiā"),("警","jǐng")]) + "。")
 + _p(_r([("唯","wéi"),("德","dé"),("学","xué")]) + "，" + _r([("唯","wéi"),("才","cái"),("艺","yì")]) + "。")
 + _p(_r([("不","bù"),("如","rú"),("人","rén")]) + "，" + _r([("当","dāng"),("自","zì"),("砺","lì")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="见人恶，即内省；不如人，当自砺 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第二十八课：见人坏处先照自己，不如人就自己磨。信第五段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/568-jian-ren-e/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/568-jian-ren-e/index.html" rel="canonical"/>',
 12: '<title>信 · 见人恶，即内省，不如人，当自砺 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">见人恶</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》信第五段：见人恶，即内省</p>'
      '<p class="cover-desc">看见别人身上的毛病，先回头照一照自己：有就改，没有也要提防。'
      '要比就比品德、学问、本事，这些不如人，就自己下功夫磨。'
      '一句话：照自己，磨自己。</p><div class="cover-seal">信</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 信第五段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>看见别人的坏处，就马上反省自己有没有；有的就改掉，没有的也要加倍警惕。'
      '要比的只有品德学问、才能技艺；这些不如别人，就该自己下功夫磨炼。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「恶」读 è，是坏处、坏事；「内省」的「省」读 xǐng，是反省、检查自己；「则」是就；'
      '「加警」是加倍警惕；「唯」读 wéi，是只有；「德学」是品德和学问；「才艺」是才能和技艺；'
      '「当」是应当；「砺」读 lì，本指磨刀石，这里是磨炼、下功夫。'
      '这一段接着上一段：上一段讲见人好就学，这一段讲见人不好先照自己。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>见人恶，即内省；有则改，无加警；唯德学，唯才艺；不如人，当自砺。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 照自己，磨自己</h2>'
      '<p style="margin:0"><strong>先说「见人不好，先照自己」</strong><br/>'
      '① <strong>看见别人的毛病，第一反应是「我有没有」</strong><br/>'
      '② <strong>有就改；没有也别松劲，加倍提防</strong><br/><br/>'
      '<strong>一句话：拿别人当镜子。</strong></p>'
      '<p><strong>再说「该比什么」</strong><br/>'
      '① <strong>比品德、比学问、比本事，不比穿戴吃用</strong><br/>'
      '② <strong>不如人不丢人，不下功夫才丢人</strong><br/><br/>'
      '<strong>一句话：不如人就自己磨。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>上一段讲见人好就学，这一段讲见人坏就自省</strong><br/>'
      '② <strong>好样子学过来，坏样子照回去，人就一天天正</strong><br/><br/>'
      '<strong>一句话：学人好，照己过。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>见人恶，即内省；有则改，无加警</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>恶 è：坏处、坏事；内省 xǐng：回头检查自己</strong><br/>'
      '② <strong>则：就；加警：加倍警惕</strong><br/><br/>'
      '<strong>一句话：别人身上有毛病，先看自己。</strong></p>'
      '<p><strong>见人恶，即内省</strong><br/>'
      '① <strong>看别人不顺眼时，先问「我是不是也这样」</strong><br/>'
      '② <strong>拿别人当镜子，比拿别人当笑话有用</strong><br/><br/>'
      '<strong>一句话：见人不好，先照己。</strong></p>'
      '<p><strong>有则改，无加警</strong><br/>'
      '① <strong>有这毛病，改掉就好，不必遮</strong><br/>'
      '② <strong>没有也别得意，提防着别犯</strong><br/><br/>'
      '<strong>一句话：有则改，无则防。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>唯德学，唯才艺；不如人，当自砺</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>唯 wéi：只有；德学：品德和学问</strong><br/>'
      '② <strong>才艺：才能和技艺；砺 lì：磨刀石，引申为磨炼</strong><br/><br/>'
      '<strong>一句话：要比就比这几样。</strong></p>'
      '<p><strong>唯德学，唯才艺</strong><br/>'
      '① <strong>该比的是人品、学问、本事</strong><br/>'
      '② <strong>穿的吃的用的，不比</strong><br/><br/>'
      '<strong>一句话：比德、比学、比本事。</strong></p>'
      '<p><strong>不如人，当自砺</strong><br/>'
      '① <strong>不如人不丢人，那只是眼下</strong><br/>'
      '② <strong>自己磨，才磨得出来</strong><br/><br/>'
      '<strong>一句话：不如人，就自己磨。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 镜与磨</h2>'
      '<p style="margin:0"><strong>前四句讲「照」</strong><br/>'
      '① <strong>见人坏处，先反省自己</strong><br/>'
      '② <strong>有则改，无则防</strong><br/><br/>'
      '<strong>一句话：拿人当镜子。</strong></p>'
      '<p><strong>后四句讲「磨」</strong><br/>'
      '① <strong>只比德学才艺</strong><br/>'
      '② <strong>不如人就自己下功夫</strong><br/><br/>'
      '<strong>一句话：自己磨自己。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>同学犯了错被批评，你想「我有没有这一条」</strong><br/>'
      '② <strong>成绩不如人，先定个小目标，天天磨一点</strong><br/><br/>'
      '<strong>一句话：照得清，磨得动。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前四句：向内照</strong><br/>'
      '① <strong>见人恶，即内省——见人毛病先查自己</strong><br/>'
      '② <strong>有则改，无加警——有就改，无从防</strong><br/><br/>'
      '<strong>一句话：省。</strong></p>'
      '<p><strong>后四句：向内磨</strong><br/>'
      '① <strong>唯德学，唯才艺——只比品德学问本事</strong><br/>'
      '② <strong>不如人，当自砺——不如人就自己磨</strong><br/><br/>'
      '<strong>一句话：砺。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>见人毛病先照己，有则改之无则防</strong><br/>'
      '② <strong>只比德学才艺，不如就自己磨</strong><br/><br/>'
      '<strong>一句话：照自己，磨自己。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 见人恶，即内省。有则改，无加警。唯德学，唯才艺。不如人，当自砺。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"见人恶，即内省。有则改，无加警。唯德学，唯才艺。不如人，当自砺。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>见人毛病先照自己；不如人就自己磨。</p>'
      '<p>📖 省砺</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>眼睛往外看人，功夫往自己身上使。</p>'
      '<p>💡 内省</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>见人恶，即内省；有则改，无加警；'
      '唯德学，唯才艺；不如人，当自砺。</p><p>🌱 即内省，当自砺</p>'),
 72: '<p>这是「弟子规课堂」第二十八课：信第五段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「见人恶」是叫我去挑别人的毛病吗？</h3>'
       '<p><strong>不是。看见别人的毛病，是拿来照自己的。</strong><br/><br/>'
       '① <strong>挑毛病只会让自己刻薄</strong><br/>'
       '② <strong>照自己才让自己长进</strong><br/>'
       '③ <strong>记法：见人恶，先内省。</strong></p>'
       '<h3>❓ 既然「无」，为什么还要「加警」？</h3>'
       '<p><strong>因为没有，不等于不会犯。</strong><br/><br/>'
       '① <strong>今天没有，明天可能就有</strong><br/>'
       '② <strong>加倍警惕，是给自己上一把锁</strong><br/>'
       '③ <strong>记法：有则改，无从防。</strong></p>'
       '<h3>❓ 「唯德学，唯才艺」是不许比吃穿吗？</h3>'
       '<p><strong>是不拿吃穿当本事。</strong><br/><br/>'
       '① <strong>衣服吃用是父母给的，不比高低</strong><br/>'
       '② <strong>德学才艺是自己练的，这才该比</strong><br/>'
       '③ <strong>记法：比本事，不比排场。</strong></p>'
       '<h3>❓ 「当自砺」的「砺」怎么讲？</h3>'
       '<p><strong>读 lì，本是磨刀石，这里是磨自己。</strong><br/><br/>'
       '① <strong>刀要磨才快，人要磨才成</strong><br/>'
       '② <strong>磨是天天的事，不是一天的事</strong><br/>'
       '③ <strong>记法：不如人，就自己磨。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 拿人当镜子</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学被批评时，你先想「我有没有这一条」</strong>；'
       '<strong>这就是「见人恶，即内省」</strong>。</p><p>💡 有错就改</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>发现自己也有那毛病，当天就改一点，不遮不躲</strong>；'
       '<strong>这就是「有则改，无加警」</strong>。</p><p>🌱 只比本事</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>不比穿戴吃用，成绩不如人就天天练一点</strong>；'
       '<strong>这就是「唯德学，唯才艺；不如人，当自砺」</strong><br/><br/>'
       '<strong>本课的落点：照自己，磨自己。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲信第五段，还是看人，看完就往自己身上看。记牢：<strong>即内省，当自砺</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">见人恶，即内省。有则改，无加警。'
       '唯德学，唯才艺。不如人，当自砺。</p><p>回顾本课要点:</p>'
       '<p>信第五段 · 照己磨己。<strong>见恶内省，不如自砺</strong>。</p>'
       '<p>见人恶，即内省 · 见人毛病先查自己。<strong>拿人当镜子</strong>。</p>'
       '<p>有则改，无加警 · 有就改，无从防。<strong>改了就好</strong>。</p>'
       '<p>唯德学，唯才艺 · 只比品德学问本事。<strong>比本事不比排场</strong>。</p>'
       '<p>不如人，当自砺 · 不如人就自己磨。<strong>天天磨一点</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>信第五段；上一段（彼说长，此说短）讲不传是非、多看人长处，'
       '这一段讲见人坏处先照自己、不如人就自己磨——学了人好，再照己过。</p><div class="ds-quote">'),
 111: '<p>见人恶，即内省。有则改，无加警。唯德学，唯才艺。不如人，当自砺。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「省」「砺」怎么读。'
       '② 今天看见同学一个毛病，先想想自己有没有。'
       '③ 找一样不如人的本事，定个天天练的小目标。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>见人恶，即内省；有则改，无加警；'
       '唯德学，唯才艺；不如人，当自砺。</strong></p></div>'),

 119: '            "见人恶，即内省。有则改，无加警。唯德学，唯才艺。不如人，当自砺。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '568-jian-ren-e';",

 59: '<!-- 4. 见人恶即内省·有则改无加警 -->',
 61: '<!-- 5. 唯德学唯才艺·不如人当自砺 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「见人恶」的「恶」怎么读？', opts: ['è，坏处、坏事', 'wù，厌恶', 'ě，恶心'], ans: 0, exp: '恶读 è，指坏处、坏事'},",
 "  {q: '2. 「即内省」的「省」怎么读？', opts: ['xǐng，反省', 'shěng，省份', 'shěng，节省'], ans: 0, exp: '省读 xǐng，是反省'},",
 "  {q: '3. 「内省」是什么意思？', opts: ['回头检查自己', '心里难受', '把东西省下来'], ans: 0, exp: '内省＝检查自己'},",
 "  {q: '4. 「有则改」的「则」是什么意思？', opts: ['就', '规则', '准则'], ans: 0, exp: '则是就'},",
 "  {q: '5. 「无加警」是什么意思？', opts: ['没有这毛病也要加倍警惕', '不用警察', '不需要警告'], ans: 0, exp: '无加警＝加倍警惕'},",
 "  {q: '6. 「唯德学」的「唯」是什么意思？', opts: ['只有', '唯一的一个', '思考'], ans: 0, exp: '唯读 wéi，是只有'},",
 "  {q: '7. 「德学」指什么？', opts: ['品德和学问', '道德课和学问课', '德国的学问'], ans: 0, exp: '德学＝品德和学问'},",
 "  {q: '8. 「当自砺」的「砺」怎么讲？', opts: ['磨炼、下功夫', '厉害', '石头'], ans: 0, exp: '砺读 lì，本是磨刀石，引申为磨炼'},",
 "  {q: '9. 「才艺」指什么？', opts: ['才能和技艺', '才华与艺术课', '有才的艺人'], ans: 0, exp: '才艺＝才能和技艺'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['见人坏处先反省自己，不如人就自己磨', '怎么挑别人的毛病', '怎么比吃穿高低'], ans: 0, exp: '照自己，磨自己'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("567-bei-shuo-chang", "568-jian-ren-e")
    out = out.replace("yaoyue568", "yaoyue569")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
