#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build571: 以 570 为骨架，按行号替换文字生成第 571 课（弟子规·信 末段，仅 12 字）
《弟子规·信》第八段：过能改，归于无。倘揜饰，增一辜。
只换文字，不动任何 HTML 标签；原文只有 2 行（12 个注音），行数仍与 570 相同。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/570-wen-yu-kong/index.html"
DST_DIR = f"{ROOT}/lessons/571-guo-neng-gai"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十一课，信第八段（信门末段）。原文：「过能改，归于无。倘揜饰，增一辜。」'
        '前两句讲有了过错肯改，就像没有过错一样；后两句讲如果犯了错还遮盖掩饰，'
        '就等于又添了一条罪。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("过","guò"),("能","néng"),("改","gǎi")]) + "，" + _r([("归","guī"),("于","yú"),("无","wú")]) + "。", True)
 + _p(_r([("倘","tǎng"),("揜","yǎn"),("饰","shì")]) + "，" + _r([("增","zēng"),("一","yī"),("辜","gū")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="过能改，归于无；倘揜饰，增一辜 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十一课：错了就改，别遮别盖。信门末段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/571-guo-neng-gai/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/571-guo-neng-gai/index.html" rel="canonical"/>',
 12: '<title>信 · 过能改，归于无，倘揜饰增一辜 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">过能改</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》信第八段：过能改，归于无</p>'
      '<p class="cover-desc">犯了错，肯认肯改，这个错就不算数了；犯了错还遮着盖着，'
      '等于又给自己添一条。这是信门最后一段。'
      '一句话：错了就改，别遮。</p><div class="cover-seal">信</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 信第八段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>有了过错能够改正，就像没有过错一样；如果犯了过错还遮盖掩饰，'
      '那就等于又多添了一条罪。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「过」是过错；「归」是回到；「无」是没有，这里指回到没有过错的状态；'
      '「倘」是如果；「揜」读 yǎn，同「掩」，是遮盖；「饰」是粉饰、掩饰；'
      '「增」是增加；「辜」读 gū，是罪。这一段是《弟子规》「信」篇的最后一段，'
      '只有十二个字，却把「改过」的道理说透了：前面讲改过的好处，后面讲掩饰的坏处，'
      '一正一反，逼着人当场认账。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>过能改，归于无；倘揜饰，增一辜。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 错了就改，别遮</h2>'
      '<p style="margin:0"><strong>先说「改了会怎样」</strong><br/>'
      '① <strong>过错认了、改了，就不算数了</strong><br/>'
      '② <strong>心里不背着，人才往前走得动</strong><br/><br/>'
      '<strong>一句话：改过归零。</strong></p>'
      '<p><strong>再说「遮了会怎样」</strong><br/>'
      '① <strong>遮着盖着，就得再撒谎，错上加错</strong><br/>'
      '② <strong>被人看破，错还在，信誉也没了</strong><br/><br/>'
      '<strong>一句话：遮一分，重一分。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句给条路：改了就好</strong><br/>'
      '② <strong>后两句堵条路：遮了更糟</strong><br/><br/>'
      '<strong>一句话：改则无，饰则辜。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>过能改，归于无</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>过：过错</strong><br/>'
      '② <strong>归：回到；无：没有，指回到没有过错的样子</strong><br/><br/>'
      '<strong>一句话：改过就归零。</strong></p>'
      '<p><strong>过能改</strong><br/>'
      '① <strong>「能」是肯、做得到，关键在一个「肯」字</strong><br/>'
      '② <strong>认了不算完，真改了才算</strong><br/><br/>'
      '<strong>一句话：认了还要改。</strong></p>'
      '<p><strong>归于无</strong><br/>'
      '① <strong>改了，这个错就不再跟着你</strong><br/>'
      '② <strong>也不是叫你天天翻旧账骂自己</strong><br/><br/>'
      '<strong>一句话：改了放下。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>倘揜饰，增一辜</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>倘：如果；揜 yǎn：同「掩」，遮盖</strong><br/>'
      '② <strong>饰：粉饰、掩饰；辜 gū：罪</strong><br/><br/>'
      '<strong>一句话：遮着不认，又添一条。</strong></p>'
      '<p><strong>倘揜饰</strong><br/>'
      '① <strong>错了先想着藏起来、赖过去</strong><br/>'
      '② <strong>一遮就得再说假话，错上摞错</strong><br/><br/>'
      '<strong>一句话：遮就是加。</strong></p>'
      '<p><strong>增一辜</strong><br/>'
      '① <strong>原本一条错，变成两条：错加欺</strong><br/>'
      '② <strong>不是别人罚你，是自己给自己记上</strong><br/><br/>'
      '<strong>一句话：越遮越重。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 改与遮</h2>'
      '<p style="margin:0"><strong>前两句讲「改」</strong><br/>'
      '① <strong>认了、改了，账就清了</strong><br/>'
      '② <strong>心里轻松，路好走</strong><br/><br/>'
      '<strong>一句话：改则无。</strong></p>'
      '<p><strong>后两句讲「遮」</strong><br/>'
      '① <strong>藏着掖着，账越记越多</strong><br/>'
      '② <strong>还落个不诚实的名声</strong><br/><br/>'
      '<strong>一句话：饰则辜。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>做错了，头一句话就说「是我错了」</strong><br/>'
      '② <strong>不找理由、不推别人、不悄悄改掉</strong><br/><br/>'
      '<strong>一句话：认得快，改得实。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 一正一反</h2>'
      '<p style="margin:0"><strong>正面：过能改，归于无</strong><br/>'
      '① <strong>「能改」重在肯改，肯改就还有路</strong><br/>'
      '② <strong>「归于无」是改完就放下，不再背着</strong><br/><br/>'
      '<strong>一句话：给路。</strong></p>'
      '<p><strong>反面：倘揜饰，增一辜</strong><br/>'
      '① <strong>「揜饰」是遮，遮了就得再骗</strong><br/>'
      '② <strong>「增一辜」是一条变两条</strong><br/><br/>'
      '<strong>一句话：堵路。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>错了就认，认了就改</strong><br/>'
      '② <strong>改了放下，不遮不盖</strong><br/><br/>'
      '<strong>一句话：改则无，饰则辜。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 过能改，归于无。倘揜饰，增一辜。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"过能改，归于无。倘揜饰，增一辜。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>改了就像没犯；遮着盖着，又添一条。</p>'
      '<p>📖 改遮</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>肯认错的人有出路；护短的人，越护越沉。</p>'
      '<p>💡 认账</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>过能改，归于无；倘揜饰，增一辜。</p>'
      '<p>🌱 改则无，饰则辜</p>'),
 72: '<p>这是「弟子规课堂」第三十一课：信第八段（信门末段）。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 改了，真能「归于无」吗？</h3>'
       '<p><strong>是说这个错不再压着你。</strong><br/><br/>'
       '① <strong>认了、改了，账就清了</strong><br/>'
       '② <strong>天天自责也走不动路</strong><br/>'
       '③ <strong>记法：改过就归零。</strong></p>'
       '<h3>❓ 「揜」这个字怎么读？</h3>'
       '<p><strong>读 yǎn，就是「掩」，遮住。</strong><br/><br/>'
       '① <strong>揜＝掩，用手盖住</strong><br/>'
       '② <strong>揜饰：遮着盖着不认</strong><br/>'
       '③ <strong>记法：揜饰＝不认错。</strong></p>'
       '<h3>❓ 掩饰一下也不行吗？</h3>'
       '<p><strong>掩饰不是护自己，是加一条。</strong><br/><br/>'
       '① <strong>要遮就得再说假话，错上加错</strong><br/>'
       '② <strong>被人看破，错还在，信誉也没了</strong><br/>'
       '③ <strong>记法：遮一分，重一分。</strong></p>'
       '<h3>❓ 「辜」是什么意思？</h3>'
       '<p><strong>辜读 gū，是罪。</strong><br/><br/>'
       '① <strong>增一辜＝又添一条罪</strong><br/>'
       '② <strong>不是别人罚你，是自己记上的</strong><br/>'
       '③ <strong>记法：改则无，饰则辜。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 错了就认</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>作业抄错了题，直接说「我抄错了，重抄」，不偷偷改掉</strong>；'
       '<strong>这就是「过能改」</strong>。</p><p>💡 不遮不盖</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>打碎了东西、忘了带书，头一时就说，不藏起来等人发现</strong>；'
       '<strong>这就是「倘揜饰，增一辜」的反面</strong>。</p><p>🌱 改完放下</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>认了、改了，就不再翻旧账骂自己</strong>；'
       '<strong>这就是「归于无」</strong><br/><br/>'
       '<strong>本课的落点：错了就改，别遮。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲信第八段，也是信门最后一段。记牢：<strong>改则无，饰则辜</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">过能改，归于无。倘揜饰，增一辜。</p>'
       '<p>回顾本课要点:</p>'
       '<p>信第八段 · 错了就改别遮。<strong>改则无，饰则辜</strong>。</p>'
       '<p>过能改，归于无 · 改了就像没犯。<strong>改过归零</strong>。</p>'
       '<p>倘揜饰，增一辜 · 遮着盖着又添一条。<strong>遮就是加</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>信门末段；上一段讲夸我不飘批我不恼、'
       '错恶分在有心没心，这一段讲错了肯改就归零、遮着盖着反而罪加一等。'
       '信门八段到此讲完。</p><div class="ds-quote">'),

 111: '<p>过能改，归于无。倘揜饰，增一辜。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「揜」「辜」怎么读、怎么讲。'
       '② 今天做错一件事，当场说出来。'
       '③ 想一想：有没有遮着没认的错。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>过能改，归于无；倘揜饰，增一辜。</strong></p></div>'),

 119: '            "过能改，归于无。倘揜饰，增一辜。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '571-guo-neng-gai';",

 59: '<!-- 4. 过能改归于无 -->',
 61: '<!-- 5. 倘揜饰增一辜 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「过能改」的「过」是什么意思？', opts: ['过错', '经过', '过分'], ans: 0, exp: '过是过错'},",
 "  {q: '2. 「归于无」的「归」是什么意思？', opts: ['回到', '回家', '归还'], ans: 0, exp: '归是回到'},",
 "  {q: '3. 「过能改，归于无」是说什么？', opts: ['改了就像没有过错', '过错永远跟着人', '改不改都一样'], ans: 0, exp: '改了就不算数了'},",
 "  {q: '4. 「倘揜饰」的「倘」是什么意思？', opts: ['如果', '倘若不来', '偷偷'], ans: 0, exp: '倘是如果'},",
 "  {q: '5. 「揜」这个字怎么读？', opts: ['yǎn，同「掩」，遮盖', 'yān，烟', 'àn，暗'], ans: 0, exp: '揜读 yǎn，同「掩」'},",
 "  {q: '6. 「揜饰」是什么意思？', opts: ['遮盖掩饰', '打扮整齐', '装饰房间'], ans: 0, exp: '揜饰＝遮盖掩饰'},",
 "  {q: '7. 「增一辜」的「辜」怎么读、什么意思？', opts: ['gū，罪', 'gù，故', 'kū，哭'], ans: 0, exp: '辜读 gū，是罪'},",
 "  {q: '8. 「增一辜」是什么意思？', opts: ['又添了一条罪', '多了一个人', '增加一分功劳'], ans: 0, exp: '增一辜＝又添一条罪'},",
 "  {q: '9. 犯了错还去掩饰，结果怎样？', opts: ['错上加错，等于罪加一等', '就没人知道了', '错会自己消失'], ans: 0, exp: '掩饰反而加重'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['有错肯改就归零，遮着盖着反而加重', '怎么避免犯错', '怎么瞒住错事'], ans: 0, exp: '改则无，饰则辜'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("570-wen-yu-kong", "571-guo-neng-gai")
    out = out.replace("yaoyue571", "yaoyue572")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
