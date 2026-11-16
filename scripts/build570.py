#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build570: 以 569 为骨架，按行号替换文字生成第 570 课
《弟子规·信》第七段：闻誉恐，闻过欣。直谅士，渐相亲。无心非，名为错。有心非，名为恶。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 569 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/569-ruo-yi-fu/index.html"
DST_DIR = f"{ROOT}/lessons/570-wen-yu-kong"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十课，信第七段。原文：「闻誉恐，闻过欣。直谅士，渐相亲。'
        '无心非，名为错。有心非，名为恶。」前四句讲听到称赞反而惶恐、听到批评反而欢喜，'
        '正直诚实的朋友就渐渐和你亲近；后四句讲不是存心做的过失叫「错」，'
        '存心做的坏事叫「恶」。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("闻","wén"),("誉","yù"),("恐","kǒng")]) + "，" + _r([("闻","wén"),("过","guò"),("欣","xīn")]) + "。", True)
 + _p(_r([("直","zhí"),("谅","liàng"),("士","shì")]) + "，" + _r([("渐","jiàn"),("相","xiāng"),("亲","qīn")]) + "。")
 + _p(_r([("无","wú"),("心","xīn"),("非","fēi")]) + "，" + _r([("名","míng"),("为","wéi"),("错","cuò")]) + "。")
 + _p(_r([("有","yǒu"),("心","xīn"),("非","fēi")]) + "，" + _r([("名","míng"),("为","wéi"),("恶","è")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="闻誉恐，闻过欣；直谅士，渐相亲 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十课：夸我不飘，批我不恼；错看有心没心。信第七段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/570-wen-yu-kong/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/570-wen-yu-kong/index.html" rel="canonical"/>',
 12: '<title>信 · 闻誉恐，闻过欣，直谅士渐相亲 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">闻誉恐</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》信第七段：闻誉恐，闻过欣</p>'
      '<p class="cover-desc">听到称赞心里发慌，听到批评心里欢喜，正直诚实的朋友就渐渐走近你。'
      '没留神做错叫「错」，存心做坏叫「恶」。'
      '一句话：夸我不飘，批我不恼。</p><div class="cover-seal">信</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 信第七段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>听到别人称赞自己就惶恐不安，听到别人指出过错就欢喜；这样正直诚实的朋友，'
      '就会渐渐和你亲近。不是存心做的过失，叫做「错」；存心做的坏事，叫做「恶」。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「誉」是称赞；「恐」是惶恐不安；「欣」是欢喜；「直谅士」指正直、诚实、能体谅人的朋友，'
      '「谅」是诚信；「渐」是渐渐；「相亲」是亲近；「非」是过失、不对的事；「为」读 wéi，是叫做；'
      '「恶」读 è，是坏。这一段接着上一段：上一段讲听批评的态度决定交到什么朋友，'
      '这一段讲听到称赞反而惶恐、听到批评反而欢喜，好朋友才肯靠近；又说错和恶的分界，'
      '在心里有没有故意。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>闻誉恐，闻过欣；直谅士，渐相亲；无心非，名为错；有心非，名为恶。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 夸我不飘，批我不恼</h2>'
      '<p style="margin:0"><strong>先说「怎么听别人的话」</strong><br/>'
      '① <strong>听到称赞不飘，听到批评不恼</strong><br/>'
      '② <strong>人肯说真话，正直的朋友才肯靠近</strong><br/><br/>'
      '<strong>一句话：爱听批评。</strong></p>'
      '<p><strong>再说「怎么看自己的错」</strong><br/>'
      '① <strong>没留神做错，是「错」，改了就好</strong><br/>'
      '② <strong>存心去干坏，是「恶」，不能拿「不小心」遮</strong><br/><br/>'
      '<strong>一句话：错恶看心。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前四句讲怎么听别人的话，后四句讲怎么看自己的错</strong><br/>'
      '② <strong>听得进批评，分得清错恶，人就往正路上走</strong><br/><br/>'
      '<strong>一句话：听真话，辨错恶。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>闻誉恐，闻过欣；直谅士，渐相亲</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>誉：称赞；恐：惶恐不安；欣：欢喜</strong><br/>'
      '② <strong>直谅士：正直诚实的朋友；渐：渐渐；相亲：亲近</strong><br/><br/>'
      '<strong>一句话：爱听批评，好人靠近。</strong></p>'
      '<p><strong>闻誉恐，闻过欣</strong><br/>'
      '① <strong>一听夸就高兴，人就容易飘</strong><br/>'
      '② <strong>一听批就恼，真话就没人说了</strong><br/><br/>'
      '<strong>一句话：夸不飘，批不恼。</strong></p>'
      '<p><strong>直谅士，渐相亲</strong><br/>'
      '① <strong>你敢听真话，敢说真话的人才肯来</strong><br/>'
      '② <strong>一味爱听好话，正直的人就慢慢走开</strong><br/><br/>'
      '<strong>一句话：听真话，交真人。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>无心非，名为错；有心非，名为恶</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>非：过失、不对的事</strong><br/>'
      '② <strong>为 wéi：叫做；恶 è：坏</strong><br/><br/>'
      '<strong>一句话：错看有心没心。</strong></p>'
      '<p><strong>无心非，名为错</strong><br/>'
      '① <strong>没留神、不知道，手上做错了</strong><br/>'
      '② <strong>这叫「错」，认了改了就好</strong><br/><br/>'
      '<strong>一句话：错能改。</strong></p>'
      '<p><strong>有心非，名为恶</strong><br/>'
      '① <strong>明知不对还去做</strong><br/>'
      '② <strong>这叫「恶」，不能拿「不小心」挡</strong><br/><br/>'
      '<strong>一句话：恶在存心。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 听与省</h2>'
      '<p style="margin:0"><strong>前四句讲「听」</strong><br/>'
      '① <strong>夸不飘，批不恼</strong><br/>'
      '② <strong>正直朋友才肯靠近</strong><br/><br/>'
      '<strong>一句话：听得进。</strong></p>'
      '<p><strong>后四句讲「省」</strong><br/>'
      '① <strong>没留神的错，认了改</strong><br/>'
      '② <strong>存心的恶，一次不碰</strong><br/><br/>'
      '<strong>一句话：认得清。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>有人夸你，说「还差得远」，别翘尾巴</strong><br/>'
      '② <strong>做错事，先说「是我没留神」，不推不赖</strong><br/><br/>'
      '<strong>一句话：不飘，不赖。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前四句：怎么听人话</strong><br/>'
      '① <strong>闻誉恐，闻过欣——夸我发慌，批我欢喜</strong><br/>'
      '② <strong>直谅士，渐相亲——正直朋友渐渐靠近</strong><br/><br/>'
      '<strong>一句话：听。</strong></p>'
      '<p><strong>后四句：怎么看己错</strong><br/>'
      '① <strong>无心非，名为错——没留神叫错</strong><br/>'
      '② <strong>有心非，名为恶——存心干叫恶</strong><br/><br/>'
      '<strong>一句话：省。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>夸我不飘，批我不恼</strong><br/>'
      '② <strong>错要认，恶不碰</strong><br/><br/>'
      '<strong>一句话：听真话，认己错。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 闻誉恐，闻过欣。直谅士，渐相亲。无心非，名为错。有心非，名为恶。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"闻誉恐，闻过欣。直谅士，渐相亲。无心非，名为错。有心非，名为恶。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>夸我不飘，批我不恼；没留神是错，存心干是恶。</p>'
      '<p>📖 听省</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>肯听真话才交得到真人；错恶的分界，就在心里那一点故意。</p>'
      '<p>💡 存心</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>闻誉恐，闻过欣；直谅士，渐相亲；'
      '无心非，名为错；有心非，名为恶。</p><p>🌱 闻过欣，辨错恶</p>'),
 72: '<p>这是「弟子规课堂」第三十课：信第七段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 听到称赞，为什么反而要「恐」？</h3>'
       '<p><strong>怕自己没那么好，一飘飘就退了。</strong><br/><br/>'
       '① <strong>称赞听着舒服，容易让人停下脚</strong><br/>'
       '② <strong>心里发慌，才会接着用功</strong><br/>'
       '③ <strong>记法：闻誉恐，不是装谦虚。</strong></p>'
       '<h3>❓ 「闻过欣」是不是喜欢挨骂？</h3>'
       '<p><strong>不是。是有人肯指出你的错，你心里感激。</strong><br/><br/>'
       '① <strong>肯说你错的人，多半是为你好</strong><br/>'
       '② <strong>你欢喜，他才肯再说</strong><br/>'
       '③ <strong>记法：闻过欣，是听得进。</strong></p>'
       '<h3>❓ 「直谅士」是什么样的人？</h3>'
       '<p><strong>正直、诚实、能体谅人的朋友。</strong><br/><br/>'
       '① <strong>直：有话当面直说</strong><br/>'
       '② <strong>谅：讲信用，也能容人</strong><br/>'
       '③ <strong>记法：敢说你错的，才是直谅士。</strong></p>'
       '<h3>❓ 「错」和「恶」差在哪？</h3>'
       '<p><strong>差在有心没心。</strong><br/><br/>'
       '① <strong>无心非：不知道、没留神，是错</strong><br/>'
       '② <strong>有心非：明知故犯，是恶</strong><br/>'
       '③ <strong>记法：错可改，恶在存心。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 夸我不飘</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>老师夸你考得好，你说「这回碰上了，还有不会的」</strong>；'
       '<strong>这就是「闻誉恐」</strong>。</p><p>💡 批我不恼</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>有人说你字写得乱，你先说「谢谢，我练」，不红脸不顶嘴</strong>；'
       '<strong>这就是「闻过欣」</strong>。</p><p>🌱 错认，恶不碰</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>做错事就说「是我没留神」，不推给别人；明知不对的事，一次也不干</strong>；'
       '<strong>这就是「无心非，名为错；有心非，名为恶」</strong><br/><br/>'
       '<strong>本课的落点：夸我不飘，批我不恼。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲信第七段，从听话说到认错。记牢：<strong>闻过欣，辨错恶</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">闻誉恐，闻过欣。直谅士，渐相亲。'
       '无心非，名为错。有心非，名为恶。</p><p>回顾本课要点:</p>'
       '<p>信第七段 · 夸不飘、批不恼。<strong>爱听批评，分清错恶</strong>。</p>'
       '<p>闻誉恐，闻过欣 · 夸我发慌批我欢喜。<strong>夸不飘，批不恼</strong>。</p>'
       '<p>直谅士，渐相亲 · 正直朋友渐渐靠近。<strong>听真话交真人</strong>。</p>'
       '<p>无心非，名为错 · 没留神做错叫错。<strong>错能改</strong>。</p>'
       '<p>有心非，名为恶 · 存心干坏叫恶。<strong>恶在存心</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>信第七段；上一段（若衣服，若饮食）讲吃穿不比人、'
       '能受批评才留得住真朋友，这一段讲听到称赞反而惶恐、听到批评反而欢喜，'
       '又说错和恶的分界在心有没有故意。</p><div class="ds-quote">'),

 111: '<p>闻誉恐，闻过欣。直谅士，渐相亲。无心非，名为错。有心非，名为恶。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「誉」「恐」「欣」「谅」怎么讲。'
       '② 今天有人夸你，回一句「还差得远」。'
       '③ 想一想：近来做的错事，是有心还是无心。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>闻誉恐，闻过欣；直谅士，渐相亲；'
       '无心非，名为错；有心非，名为恶。</strong></p></div>'),

 119: '            "闻誉恐，闻过欣。直谅士，渐相亲。无心非，名为错。有心非，名为恶。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '570-wen-yu-kong';",

 59: '<!-- 4. 闻誉恐闻过欣·直谅士渐相亲 -->',
 61: '<!-- 5. 无心非名为错·有心非名为恶 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「闻誉恐」的「誉」是什么意思？', opts: ['称赞', '名誉头衔', '荣誉证书'], ans: 0, exp: '誉是称赞'},",
 "  {q: '2. 「闻誉恐」的「恐」是什么意思？', opts: ['惶恐不安', '害怕黑', '恐怕'], ans: 0, exp: '恐是惶恐不安'},",
 "  {q: '3. 「闻过欣」的「欣」是什么意思？', opts: ['欢喜', '欣赏风景', '辛苦'], ans: 0, exp: '欣是欢喜'},",
 "  {q: '4. 「直谅士」指什么样的人？', opts: ['正直诚实的朋友', '当官的人', '读书很多的人'], ans: 0, exp: '直谅士＝正直诚实的朋友'},",
 "  {q: '5. 「渐相亲」的「渐」是什么意思？', opts: ['渐渐', '立刻', '很少'], ans: 0, exp: '渐是渐渐'},",
 "  {q: '6. 「无心非」的「非」是什么意思？', opts: ['过失、不对的事', '不是', '非要去'], ans: 0, exp: '非是过失、不对的事'},",
 "  {q: '7. 「名为错」的「为」怎么读？', opts: ['wéi，叫做', 'wèi，为了', 'wěi，虚伪'], ans: 0, exp: '为读 wéi，是叫做'},",
 "  {q: '8. 「名为恶」的「恶」怎么读？', opts: ['è，坏', 'wù，讨厌', 'ě，恶心'], ans: 0, exp: '恶读 è，是坏'},",
 "  {q: '9. 「错」和「恶」的分界在哪？', opts: ['有没有存心故意', '错得大不大', '有没有被人看见'], ans: 0, exp: '无心是错，有心是恶'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['夸不飘批不恼，分得清无心之错与有心之恶', '怎么当官', '怎么应付夸奖'], ans: 0, exp: '爱听批评，分清错恶'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("569-ruo-yi-fu", "570-wen-yu-kong")
    out = out.replace("yaoyue570", "yaoyue571")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
