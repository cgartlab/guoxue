#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build593: 以 592 为骨架，按行号替换文字生成第 593 课
《笠翁对韵》一东·其二后段（驿旅客逢梅子雨，池亭人挹藕花风。）
只换文字，不动任何 HTML 标签。行号与 592 完全一致。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/592-yun-ai-dai/index.html"
DST_DIR = f"{ROOT}/lessons/593-yi-lu-ke"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》一东其二后段。原文：「驿旅客逢梅子雨，池亭人挹藕花风。」'
        '赶路的人在驿站碰上梅雨，池边亭子里的人把荷花的香风舀过来。两句十字对十字，一苦一闲；'
        '上句「雨」不押、下句「风」押东韵。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("驿","yì"),("旅","lǚ"),("客","kè"),("逢","féng"),("梅","méi"),("子","zǐ"),("雨","yǔ")]) + "，", True)
 + _p(_r([("池","chí"),("亭","tíng"),("人","rén"),("挹","yì"),("藕","ǒu"),("花","huā"),("风","fēng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 一东（驿旅客逢梅子雨） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》一东其二后段：驿旅客逢梅子雨，池亭人挹藕花风。赶路的人碰上梅雨，亭里的人舀来荷香；十字对十字，一苦一闲。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/593-yi-lu-ke/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/593-yi-lu-ke/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 一东（驿旅客逢梅子雨）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">一东</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》上卷第一韵 · 其二后段</p>'
      '<p class="cover-desc">一个人在路上赶，正撞上江南的梅雨；一个人在池边亭子里坐着，'
      '把带荷花香的风舀过来闻。一样的天气，两种日子。'
      '一句话：十字对十字，一苦一闲。</p><div class="cover-seal">雨</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 一东（其二后段）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>出门在外的旅人，在驿站上碰上了梅子黄时的连阴雨；'
      '池边亭子里的人，正把带着荷花香的风舀过来。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>这是「一东」其二的倒数第三、四句，两个七字句，十个字对十个字，对得最整齐。'
      '上句写赶路的人：梅雨一下就是半个月，路烂、衣湿，是苦的；'
      '下句写闲坐的人：亭子临池，荷花开着，风带着香，是甜的。'
      '同一片天、同一个季节，只因站的地方不同，日子就两样。'
      '「挹」是舀，把风当水一样舀过来，写得极俏。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>驿旅客逢梅子雨，池亭人挹藕花风。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话读这两句</h2>'
      '<p style="margin:0"><strong>一个人在路上</strong><br/>'
      '① <strong>驿旅客：出门在外的人</strong><br/>'
      '② <strong>逢梅子雨：撞上连阴雨</strong><br/><br/>'
      '<strong>一句话：苦。</strong></p>'
      '<p><strong>一个人在亭里</strong><br/>'
      '① <strong>池亭人：池边乘凉的人</strong><br/>'
      '② <strong>挹藕花风：舀来荷香的风</strong><br/><br/>'
      '<strong>一句话：甜。</strong></p>'
      '<p><strong>两个字对两个字</strong><br/>'
      '① <strong>十字对十字，字字有对</strong><br/>'
      '② <strong>一苦一闲，正好成照</strong><br/><br/>'
      '<strong>一句话：对得工，也写得活。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>驿旅客逢梅子雨 · 路上的人</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>驿 yì：驿站，古人换马歇脚的地方</strong><br/>'
      '② <strong>旅客：出门在外的人</strong><br/><br/>'
      '<strong>一句话：驿旅客＝赶路的人。</strong></p>'
      '<p><strong>梅子雨</strong><br/>'
      '① <strong>梅子黄熟时下的连阴雨，又叫梅雨</strong><br/>'
      '② <strong>江南初夏，一下就是十天半月</strong><br/><br/>'
      '<strong>一句话：不是梅子下的雨。</strong></p>'
      '<p><strong>逢</strong><br/>'
      '① <strong>碰上、赶上，不是特意去等</strong><br/>'
      '② <strong>路烂、衣湿、走不动，都得受着</strong><br/><br/>'
      '<strong>一句话：躲不开的一场雨。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>池亭人挹藕花风 · 亭里的人</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>挹 yì：舀，用器物把液体取出来</strong><br/>'
      '② <strong>藕花：荷花（藕是它的根）</strong><br/><br/>'
      '<strong>一句话：把风当水舀。</strong></p>'
      '<p><strong>池亭人</strong><br/>'
      '① <strong>池边亭子里的人，正坐着乘凉</strong><br/>'
      '② <strong>不出门、不赶路，有闲工夫</strong><br/><br/>'
      '<strong>一句话：闲着的人。</strong></p>'
      '<p><strong>挹藕花风</strong><br/>'
      '① <strong>风里有荷花香，像水一样舀过来</strong><br/>'
      '② <strong>一个「挹」字，把香气写成了能盛的东西</strong><br/><br/>'
      '<strong>一句话：闻香也闻得讲究。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 十字对十字</h2>'
      '<p style="margin:0"><strong>字字有对</strong><br/>'
      '① <strong>驿旅客 —— 池亭人（都是三字，都是人）</strong><br/>'
      '② <strong>逢 —— 挹（都是动作）</strong><br/><br/>'
      '<strong>一句话：连数都对得上。</strong></p>'
      '<p><strong>雨对风</strong><br/>'
      '① <strong>梅子雨 —— 藕花风（都带花果名）</strong><br/>'
      '② <strong>一个是雨，一个是风</strong><br/><br/>'
      '<strong>一句话：同一个夏天，两样天气。</strong></p>'
      '<p><strong>只有一个韵脚</strong><br/>'
      '① <strong>上句收「雨」是仄声，不押</strong><br/>'
      '② <strong>下句收「风」是平声，押东韵</strong><br/><br/>'
      '<strong>一句话：出句收仄，对句收平。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 一句一层</h2>'
      '<p style="margin:0"><strong>第一层：人在路上</strong><br/>'
      '① <strong>驿旅客——离家的、赶路的</strong><br/>'
      '② <strong>先立一个辛苦的人</strong><br/><br/>'
      '<strong>一句话：先写苦。</strong></p>'
      '<p><strong>第二层：雨来了</strong><br/>'
      '① <strong>梅子雨——偏偏这时候下起来</strong><br/>'
      '② <strong>「逢」字带着没办法的意思</strong><br/><br/>'
      '<strong>一句话：苦上加苦。</strong></p>'
      '<p><strong>第三层：换一个人</strong><br/>'
      '① <strong>池亭人——同一天，正舀着荷香</strong><br/>'
      '② <strong>不写怨，只并排一放，意思就出来了</strong><br/><br/>'
      '<strong>一句话：对照比说理更有力。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 一样的天气，两样的日子</h2>'
      '<p>同样一场夏天的风雨，站的地方不同，滋味就不同——</p>'
      '<h3>"驿旅客逢梅子雨，池亭人挹藕花风。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>一个赶路的人遇上梅雨，'
      '一个闲坐的人舀着荷风。</p><p>📖 两个画面</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>十个字对十个字，字字工整；'
      '一苦一闲，不用评论就有了味道。</p><p>💡 对照成趣</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>下雨天，想想路上的人和'
      '窗边的人，各是什么心情。</p><p>🌱 会体谅</p>'),
 72: '<p>这是「笠翁对韵课堂」第六课：一东其二后段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「挹」怎么念，什么意思？</h3>'
       '<p><strong>念 yì，是「舀」。</strong><br/><br/>'
       '① <strong>用瓢、用勺把水取出来，就叫挹</strong><br/>'
       '② <strong>挹藕花风＝把带荷香的风舀过来</strong><br/>'
       '③ <strong>记法：提手旁，用手取。</strong></p>'
       '<h3>❓ 「梅子雨」是梅子下的雨吗？</h3>'
       '<p><strong>不是，是梅子黄时的连阴雨。</strong><br/><br/>'
       '① <strong>江南初夏梅子黄熟，雨一下十天半月</strong><br/>'
       '② <strong>又叫梅雨、黄梅雨，衣服都发潮</strong><br/>'
       '③ <strong>记法：梅子黄了，雨就来了。</strong></p>'
       '<h3>❓ 这两句为什么只有一个韵脚？</h3>'
       '<p><strong>上句不押，下句才押。</strong><br/><br/>'
       '① <strong>上句收「雨」，是仄声，不押韵</strong><br/>'
       '② <strong>下句收「风」，是平声，押东韵</strong><br/>'
       '③ <strong>记法：出句收仄，对句收平。</strong></p>'
       '<h3>❓ 「驿旅客」和「池亭人」差在哪儿？</h3>'
       '<p><strong>差在一个「动」一个「静」。</strong><br/><br/>'
       '① <strong>驿旅客在路上赶，风里雨里</strong><br/>'
       '② <strong>池亭人在亭里坐，闻着荷香</strong><br/>'
       '③ <strong>记法：字面对得工，日子过得两样。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念两句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把两句念三遍</strong>；'
       '<strong>「雨」念得短，「风」念得长，尾巴拖出去</strong>。</p><p>💡 认三个词</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>记住「驿」是驿站、「挹」是舀、'
       '「藕花」是荷花</strong>；<strong>三个词都认下来</strong>。</p><p>🌱 自己对一对</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>说一个「××客」、一个「××人」</strong>；'
       '<strong>再各配一个动作，看对不对得上</strong><br/><br/>'
       '<strong>本课的落点：一样的天气，两样的日子。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>一苦一闲，字字成对。<strong>只有一个韵脚「风」</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">驿旅客逢梅子雨，池亭人挹藕花风。</p>'
       '<p>回顾本课要点:</p>'
       '<p>驿旅客。<strong>出门赶路的人</strong>。</p>'
       '<p>梅子雨。<strong>初夏连阴雨，不是梅子下的</strong>。</p>'
       '<p>池亭人挹藕花风。<strong>「挹」是舀，把荷香舀过来</strong>。</p>'
       '<p>押韵。<strong>上句收仄不押，下句「风」押东韵</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>一东其二后段；'
       '下一课「茅店村前」。</p>'
       '<div class="ds-quote">'),

 111: '<p>驿旅客逢梅子雨，池亭人挹藕花风。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 把两句背出来。'
       '② 说说「挹」是做什么动作。'
       '③ 自己想一个「什么人」对「什么人」，配上一个动作。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>路上人挨雨，亭里人舀风；'
       '一样的天气，两样的日子。</strong></p></div>'),

 119: '            "驿旅客逢梅子雨，池亭人挹藕花风。"<br/>',
 120: '<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《笠翁对韵·一东》</span>',

 127: "    window.GUOXUE_COURSE_ID = '593-yi-lu-ke';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 驿旅客逢梅子雨·路上的人 -->',
 61: '<!-- 5. 池亭人挹藕花风·亭里的人 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「驿旅客」中的「驿」指什么？', opts: ['驿站，换马歇脚的地方', '一种马', '一座山'], ans: 0, exp: '驿是驿站'},",
 "  {q: '2. 「梅子雨」是什么雨？', opts: ['梅子黄熟时的连阴雨', '梅子做的雨', '秋天的雨'], ans: 0, exp: '梅雨是初夏连阴雨'},",
 "  {q: '3. 「挹」这个字念什么？', opts: ['yì', 'yí', 'yè'], ans: 0, exp: '挹读 yì'},",
 "  {q: '4. 「挹」的意思是？', opts: ['舀，用器物取', '扔掉', '挡住'], ans: 0, exp: '挹就是舀'},",
 "  {q: '5. 「藕花」指的是什么花？', opts: ['荷花', '梅花', '菊花'], ans: 0, exp: '藕花就是荷花'},",
 "  {q: '6. 「池亭人」在做什么？', opts: ['在池边亭里乘凉闻香', '在赶路', '在打鱼'], ans: 0, exp: '池亭人闲着'},",
 "  {q: '7. 「驿旅客」和「池亭人」最大的不同是？', opts: ['一个辛苦赶路，一个悠闲乘凉', '一个男一个女', '一个老一个少'], ans: 0, exp: '一苦一闲'},",
 "  {q: '8. 「逢」在这里是什么意思？', opts: ['碰上、赶上', '特意去等', '躲开'], ans: 0, exp: '逢是碰上'},",
 "  {q: '9. 这两句的韵脚是哪个字？', opts: ['风', '雨', '客'], ans: 0, exp: '只有「风」押韵'},",
 "  {q: '10. 上句收「雨」为什么不押韵？', opts: ['「雨」是仄声，出句收仄', '「雨」太短', '「雨」是生字'], ans: 0, exp: '出句收仄，对句收平'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("592-yun-ai-dai", "593-yi-lu-ke")
    out = out.replace("yaoyue592", "yaoyue593")
    # 门类副标题里的课序
    out = out.replace("「笠翁对韵课堂」第六课：一东其二后段", "「笠翁对韵课堂」第六课：一东其二后段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
