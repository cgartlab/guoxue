#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build569: 以 568 为骨架，按行号替换文字生成第 569 课
《弟子规·信》第六段：若衣服，若饮食。不如人，勿生戚。闻过怒，闻誉乐。损友来，益友却。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 568 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/568-jian-ren-e/index.html"
DST_DIR = f"{ROOT}/lessons/569-ruo-yi-fu"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第二十九课，信第六段。原文：「若衣服，若饮食。不如人，勿生戚。'
        '闻过怒，闻誉乐。损友来，益友却。」前四句讲穿的吃的比不上别人，不必忧愁难过；'
        '后四句讲一听批评就发怒、一听称赞就高兴，坏朋友就会凑上来，好朋友就会走开。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("若","ruò"),("衣","yī"),("服","fú")]) + "，" + _r([("若","ruò"),("饮","yǐn"),("食","shí")]) + "。", True)
 + _p(_r([("不","bù"),("如","rú"),("人","rén")]) + "，" + _r([("勿","wù"),("生","shēng"),("戚","qī")]) + "。")
 + _p(_r([("闻","wén"),("过","guò"),("怒","nù")]) + "，" + _r([("闻","wén"),("誉","yù"),("乐","lè")]) + "。")
 + _p(_r([("损","sǔn"),("友","yǒu"),("来","lái")]) + "，" + _r([("益","yì"),("友","yǒu"),("却","què")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="若衣服，若饮食；闻过怒，闻誉乐 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第二十九课：吃穿不比人，批评要听得进。信第六段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/569-ruo-yi-fu/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/569-ruo-yi-fu/index.html" rel="canonical"/>',
 12: '<title>信 · 若衣服，若饮食，闻过怒，闻誉乐 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">若衣服</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》信第六段：若衣服，若饮食</p>'
      '<p class="cover-desc">穿的吃的比不上别人，不必难过。真正要留心的是听不听得进批评：'
      '一听批评就恼，一听好话就笑，坏朋友就凑上来，好朋友就走远了。'
      '一句话：不慕吃穿，能受批评。</p><div class="cover-seal">信</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 信第六段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>至于衣服饮食，比不上别人，不要忧愁难过。听到别人指出过错就发怒，听到别人称赞就欢喜；'
      '这样一来，坏朋友就会凑过来，好朋友就会离开。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「若」是至于；「衣服」「饮食」指穿的吃的；「戚」读 qī，是忧愁、悲伤；「闻」是听到；'
      '「过」是过错；「誉」是称赞；「乐」读 lè，是高兴；「损友」是对自己有害的朋友；'
      '「益友」是对自己有益的朋友；「却」是退去、离开。'
      '这一段接着上一段：上一段讲只比德学才艺，这一段讲吃穿不如人别难过，又讲听批评的态度决定交到什么朋友。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>若衣服，若饮食；不如人，勿生戚；闻过怒，闻誉乐；损友来，益友却。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 不慕吃穿，能受批评</h2>'
      '<p style="margin:0"><strong>先说「吃穿不如人，别难过」</strong><br/>'
      '① <strong>衣服饮食是父母给的，不是自己的本事</strong><br/>'
      '② <strong>不如人不生愁，心才不歪</strong><br/><br/>'
      '<strong>一句话：不慕吃穿。</strong></p>'
      '<p><strong>再说「听批评的态度，决定朋友」</strong><br/>'
      '① <strong>闻过就怒、闻誉就乐，人就不敢跟你说真话</strong><br/>'
      '② <strong>真话走了，凑上来的多是顺着你的人</strong><br/><br/>'
      '<strong>一句话：能受批评。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前半段讲身外之物不必比，后半段讲心里的话要听</strong><br/>'
      '② <strong>吃穿看淡，批评听进，人就正、朋友就真</strong><br/><br/>'
      '<strong>一句话：看淡吃穿，看重真话。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>若衣服，若饮食；不如人，勿生戚</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>若：至于；衣服、饮食：穿的吃的</strong><br/>'
      '② <strong>戚 qī：忧愁、悲伤；生戚＝心里难过</strong><br/><br/>'
      '<strong>一句话：吃穿比不上，不必难过。</strong></p>'
      '<p><strong>若衣服，若饮食</strong><br/>'
      '① <strong>穿得好坏、吃得好坏，是家里的条件</strong><br/>'
      '② <strong>拿这个比高低，比的是父母，不是自己</strong><br/><br/>'
      '<strong>一句话：吃穿不比。</strong></p>'
      '<p><strong>不如人，勿生戚</strong><br/>'
      '① <strong>不如人不丢人，难过反倒乱了心</strong><br/>'
      '② <strong>心思放在德学才艺上，才有着落</strong><br/><br/>'
      '<strong>一句话：不如人，别难过。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>闻过怒，闻誉乐；损友来，益友却</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>闻：听到；过：过错；誉：称赞；乐 lè：高兴</strong><br/>'
      '② <strong>损友：有害的朋友；益友：有益的朋友；却：退去、离开</strong><br/><br/>'
      '<strong>一句话：一听批评就恼，朋友就变。</strong></p>'
      '<p><strong>闻过怒，闻誉乐</strong><br/>'
      '① <strong>一听批评就发火，谁还敢跟你说真话</strong><br/>'
      '② <strong>一听好话就笑，顺着你的人越来越多</strong><br/><br/>'
      '<strong>一句话：爱听好话，听不到真话。</strong></p>'
      '<p><strong>损友来，益友却</strong><br/>'
      '① <strong>损友专挑你爱听的说</strong><br/>'
      '② <strong>益友说真话，你不爱听，他就走了</strong><br/><br/>'
      '<strong>一句话：态度定朋友。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 淡与听</h2>'
      '<p style="margin:0"><strong>前四句讲「淡」</strong><br/>'
      '① <strong>吃穿不如人不难过</strong><br/>'
      '② <strong>心思放在本事上</strong><br/><br/>'
      '<strong>一句话：看淡身外。</strong></p>'
      '<p><strong>后四句讲「听」</strong><br/>'
      '① <strong>批评听得进，称赞不飘飘</strong><br/>'
      '② <strong>真朋友才留得住</strong><br/><br/>'
      '<strong>一句话：听得进话。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>同学穿新鞋新衣，你替他高兴，不眼热</strong><br/>'
      '② <strong>有人指出你的错，先说「谢谢，我改」</strong><br/><br/>'
      '<strong>一句话：不眼热，不护短。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前四句：身外看淡</strong><br/>'
      '① <strong>若衣服，若饮食——说的就是穿的吃的</strong><br/>'
      '② <strong>不如人，勿生戚——不如人别难过</strong><br/><br/>'
      '<strong>一句话：淡。</strong></p>'
      '<p><strong>后四句：真话听进</strong><br/>'
      '① <strong>闻过怒，闻誉乐——怕听错话，爱听好话</strong><br/>'
      '② <strong>损友来，益友却——坏朋友来，好朋友走</strong><br/><br/>'
      '<strong>一句话：听。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>吃穿不如人不难过，心思放在本事上</strong><br/>'
      '② <strong>批评听得进，称赞不飘飘</strong><br/><br/>'
      '<strong>一句话：淡吃穿，听真话。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 若衣服，若饮食。不如人，勿生戚。闻过怒，闻誉乐。损友来，益友却。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"若衣服，若饮食。不如人，勿生戚。闻过怒，闻誉乐。损友来，益友却。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>吃穿不如人别难过；批评听得进，好话不飘。</p>'
      '<p>📖 淡听</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>身外之物看淡，心里的真话听进，人才立得住。</p>'
      '<p>💡 真话</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>若衣服，若饮食；不如人，勿生戚；'
      '闻过怒，闻誉乐；损友来，益友却。</p><p>🌱 勿生戚，留益友</p>'),
 72: '<p>这是「弟子规课堂」第二十九课：信第六段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 吃穿不如人，为什么不能难过？</h3>'
       '<p><strong>难过不解决问题，还乱了心。</strong><br/><br/>'
       '① <strong>衣服饮食是父母给的，不是自己挣的</strong><br/>'
       '② <strong>心一乱，书也读不进去</strong><br/>'
       '③ <strong>记法：不如人，别生戚。</strong></p>'
       '<h3>❓ 「闻过怒」有什么不好？</h3>'
       '<p><strong>一发火，真话就没人说了。</strong><br/><br/>'
       '① <strong>肯指出你错的人，多半是为你好</strong><br/>'
       '② <strong>你一恼，他就再不开口</strong><br/>'
       '③ <strong>记法：闻过先谢，别先恼。</strong></p>'
       '<h3>❓ 「闻誉乐」也要警惕吗？</h3>'
       '<p><strong>要。只爱听好话，就分不清真假。</strong><br/><br/>'
       '① <strong>称赞听着舒服，但容易让人飘</strong><br/>'
       '② <strong>顺着你说的人，不一定真帮你</strong><br/>'
       '③ <strong>记法：好话听一半，真话听全。</strong></p>'
       '<h3>❓ 「损友」「益友」怎么分？</h3>'
       '<p><strong>看他跟你说真话，还是只说好话。</strong><br/><br/>'
       '① <strong>益友：你错了他敢讲</strong><br/>'
       '② <strong>损友：你错了他也说对</strong><br/>'
       '③ <strong>记法：敢说你错的，才是真朋友。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 不眼热</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学换了新衣新鞋，你替他高兴，不攀不比</strong>；'
       '<strong>这就是「若衣服，若饮食；不如人，勿生戚」</strong>。</p><p>💡 听得进批评</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>有人指出你的错，先说「谢谢，我改」，不顶嘴不赌气</strong>；'
       '<strong>这就是「闻过怒，闻誉乐」的反面</strong>。</p><p>🌱 交真朋友</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>多跟敢说你错的人在一块，少跟一味夸你的人混</strong>；'
       '<strong>这就是「损友来，益友却」</strong><br/><br/>'
       '<strong>本课的落点：不慕吃穿，能受批评。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲信第六段，从吃穿说到朋友。记牢：<strong>勿生戚，留益友</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">若衣服，若饮食。不如人，勿生戚。'
       '闻过怒，闻誉乐。损友来，益友却。</p><p>回顾本课要点:</p>'
       '<p>信第六段 · 淡身外、听真话。<strong>不慕吃穿，能受批评</strong>。</p>'
       '<p>若衣服，若饮食 · 穿的吃的比不上。<strong>不比吃穿</strong>。</p>'
       '<p>不如人，勿生戚 · 不如人别难过。<strong>心思放本事</strong>。</p>'
       '<p>闻过怒，闻誉乐 · 怕听错话爱听好话。<strong>闻过先谢</strong>。</p>'
       '<p>损友来，益友却 · 坏朋友来，好朋友走。<strong>态度定朋友</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>信第六段；上一段（见人恶，即内省）讲见人坏处先照自己、'
       '不如人就自己磨，这一段讲吃穿不如人别难过、批评听得进才留得住真朋友。</p><div class="ds-quote">'),
 111: '<p>若衣服，若饮食。不如人，勿生戚。闻过怒，闻誉乐。损友来，益友却。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「戚」「誉」「却」怎么讲。'
       '② 今天有人指出你的错，说一句「谢谢」。'
       '③ 想一想身边谁最敢说你错，跟他多亲近。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>若衣服，若饮食；不如人，勿生戚；'
       '闻过怒，闻誉乐；损友来，益友却。</strong></p></div>'),

 119: '            "若衣服，若饮食。不如人，勿生戚。闻过怒，闻誉乐。损友来，益友却。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '569-ruo-yi-fu';",

 59: '<!-- 4. 若衣服若饮食·不如人勿生戚 -->',
 61: '<!-- 5. 闻过怒闻誉乐·损友来益友却 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「勿生戚」的「戚」怎么读、什么意思？', opts: ['qī，忧愁、悲伤', 'qì，亲戚', 'qí，亲密'], ans: 0, exp: '戚读 qī，是忧愁、悲伤'},",
 "  {q: '2. 「若衣服」的「若」是什么意思？', opts: ['至于', '如果', '好像'], ans: 0, exp: '若是至于'},",
 "  {q: '3. 「不如人，勿生戚」是说什么？', opts: ['吃穿不如人不要难过', '成绩不如人要哭', '不如人就该生气'], ans: 0, exp: '不如人不必忧愁'},",
 "  {q: '4. 「闻过」的「过」是什么意思？', opts: ['过错', '经过', '过分'], ans: 0, exp: '过是过错'},",
 "  {q: '5. 「闻誉乐」的「誉」是什么意思？', opts: ['称赞', '名誉', '荣誉证书'], ans: 0, exp: '誉是称赞'},",
 "  {q: '6. 「闻誉乐」的「乐」怎么读？', opts: ['lè，高兴', 'yuè，音乐', 'yào，喜欢'], ans: 0, exp: '乐读 lè，是高兴'},",
 "  {q: '7. 「损友」指什么？', opts: ['对自己有害的朋友', '破了财的朋友', '生病的朋友'], ans: 0, exp: '损友＝有害的朋友'},",
 "  {q: '8. 「益友」指什么？', opts: ['对自己有益的朋友', '有钱的朋友', '朋友很多'], ans: 0, exp: '益友＝有益的朋友'},",
 "  {q: '9. 「益友却」的「却」是什么意思？', opts: ['退去、离开', '但是', '推辞'], ans: 0, exp: '却是退去、离开'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['吃穿不比、不如人别难过，能听批评才留得住真朋友', '怎么挑衣裳', '怎么交有钱的朋友'], ans: 0, exp: '不慕吃穿，能受批评'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("568-jian-ren-e", "569-ruo-yi-fu")
    out = out.replace("yaoyue569", "yaoyue570")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
