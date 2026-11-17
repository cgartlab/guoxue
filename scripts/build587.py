#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build587: 以 586 为骨架，按行号替换文字生成第 587 课（《弟子规》全篇收官课）
《弟子规·余力学文》末段：非圣书，屏勿视。蔽聪明，坏心志。勿自暴，勿自弃。圣与贤，可驯致。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/586-lie-dian-ji/index.html"
DST_DIR = f"{ROOT}/lessons/587-fei-sheng-shu"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十七课，余力学文末段，也是全篇最后一课。原文：「非圣书，屏勿视。蔽聪明，坏心志。'
        '勿自暴，勿自弃。圣与贤，可驯致。」前两句讲不是讲道理的好书就别看，它会蒙住你的聪明、败坏你的志向；'
        '后两句讲不要自己糟蹋自己、不要自己放弃自己，圣贤的境界是渐渐能到的。'
        '合起来：外面把好门，里面不认输。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("非","fēi"),("圣","shèng"),("书","shū")]) + "，" + _r([("屏","bǐng"),("勿","wù"),("视","shì")]) + "。", True)
 + _p(_r([("蔽","bì"),("聪","cōng"),("明","míng")]) + "，" + _r([("坏","huài"),("心","xīn"),("志","zhì")]) + "。")
 + _p(_r([("勿","wù"),("自","zì"),("暴","bào")]) + "，" + _r([("勿","wù"),("自","zì"),("弃","qì")]) + "。")
 + _p(_r([("圣","shèng"),("与","yǔ"),("贤","xián")]) + "，" + _r([("可","kě"),("驯","xún"),("致","zhì")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="非圣书屏勿视，圣与贤可驯致 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十七课：不讲道理的书别看，会蒙住聪明败坏志向；不糟蹋自己、不放弃自己，圣贤是渐渐能到的。《弟子规》全篇收官。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/587-fei-sheng-shu/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/587-fei-sheng-shu/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 非圣书屏勿视 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">向上</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文末段（全篇最后四句）</p>'
      '<p class="cover-desc">不是讲道理的好书，别看——它会蒙住你的聪明、败坏你的志向。'
      '更别自己看轻自己、自己放弃自己。圣贤不是天生的，是一天一天走上去的。'
      '一句话：外面把好门，里面不认输。</p><div class="cover-seal">贤</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文末段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>不是讲圣贤道理的书，推开别看；它会蒙住你的耳聪目明，败坏你的心志。'
      '不要自己糟蹋自己，不要自己放弃自己；圣贤那样的人，是可以渐渐做到的。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「圣书」是讲圣贤道理的书；「屏」读 bǐng，同「摒」，是挡住、推开，不读 píng（屏风才读 píng）；'
      '「蔽」是蒙住、遮住；「聪明」是耳聪目明，不是夸人机灵；「心志」是心里的志向；'
      '「暴」是糟蹋；「弃」是丢开、放弃；「驯」读 xún，是渐渐；「致」是达到。'
      '这是《弟子规》全篇的最后四句：前面讲怎么读书，最后讲读什么书、做一个什么样的人。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>非圣书，屏勿视；蔽聪明，坏心志；勿自暴，勿自弃；圣与贤，可驯致。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 两句管外面，两句管自己</h2>'
      '<p style="margin:0"><strong>外面：把好门</strong><br/>'
      '① <strong>不好的书、不好的片子，别看</strong><br/>'
      '② <strong>看了会糊涂，会学坏</strong><br/><br/>'
      '<strong>一句话：眼睛要挑。</strong></p>'
      '<p><strong>自己：不认输</strong><br/>'
      '① <strong>做错了别骂自己没用</strong><br/>'
      '② <strong>落后了别索性放弃</strong><br/><br/>'
      '<strong>一句话：别自己看轻自己。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「不看什么」</strong><br/>'
      '② <strong>后两句讲「怎么看自己」</strong><br/><br/>'
      '<strong>一句话：眼要清，心要立。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>非圣书，屏勿视；蔽聪明，坏心志</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>屏 bǐng：挡住、推开，不读 píng</strong><br/>'
      '② <strong>蔽：蒙住；心志：心里的志向</strong><br/><br/>'
      '<strong>一句话：坏东西别看。</strong></p>'
      '<p><strong>非圣书，屏勿视</strong><br/>'
      '① <strong>不是讲道理的书，翻一页就放下</strong><br/>'
      '② <strong>不是禁一切课外书，是禁「越看越糊涂」的</strong><br/><br/>'
      '<strong>一句话：读得明白，才是好书。</strong></p>'
      '<p><strong>蔽聪明，坏心志</strong><br/>'
      '① <strong>看多了，眼睛懒得想，脑子跟着乱</strong><br/>'
      '② <strong>该做的事不想做，志向一点点散掉</strong><br/><br/>'
      '<strong>一句话：看什么，就成什么。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>勿自暴，勿自弃；圣与贤，可驯致</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>暴：糟蹋自己；弃：放弃自己</strong><br/>'
      '② <strong>驯 xún：渐渐；致：达到</strong><br/><br/>'
      '<strong>一句话：别放弃，慢慢到。</strong></p>'
      '<p><strong>勿自暴，勿自弃</strong><br/>'
      '① <strong>考砸一次就说「我笨」，这是自暴</strong><br/>'
      '② <strong>落后了就「反正我不行」，这是自弃</strong><br/><br/>'
      '<strong>一句话：一次不算一辈子。</strong></p>'
      '<p><strong>圣与贤，可驯致</strong><br/>'
      '① <strong>圣贤不是天生的，是一天一点走上去的</strong><br/>'
      '② <strong>今天的你比昨天好一点，就在这条路上</strong><br/><br/>'
      '<strong>一句话：人人够得着。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 进门与走路</h2>'
      '<p style="margin:0"><strong>先把门看住</strong><br/>'
      '① <strong>手机上的东西先过一遍：教我什么</strong><br/>'
      '② <strong>让你心浮气躁的，关掉</strong><br/><br/>'
      '<strong>一句话：不看的，也是选择。</strong></p>'
      '<p><strong>再把自己扶住</strong><br/>'
      '① <strong>做错事说「下次怎么改」，不说「我不行」</strong><br/>'
      '② <strong>跟不上就补一点，别破罐破摔</strong><br/><br/>'
      '<strong>一句话：改了就是往前走。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>今天删掉一个让你上瘾又没用的内容源</strong><br/>'
      '② <strong>今天给自己定一个小目标，做到就记一笔</strong><br/><br/>'
      '<strong>一句话：眼清、心立、脚步不停。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两层</h2>'
      '<p style="margin:0"><strong>前两句：挑着看</strong><br/>'
      '① <strong>非圣书，屏勿视——不看坏的</strong><br/>'
      '② <strong>蔽聪明，坏心志——看了有害</strong><br/><br/>'
      '<strong>一句话：守眼。</strong></p>'
      '<p><strong>后两句：往上走</strong><br/>'
      '① <strong>勿自暴，勿自弃——不糟蹋不放弃</strong><br/>'
      '② <strong>圣与贤，可驯致——渐渐能到</strong><br/><br/>'
      '<strong>一句话：守心。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>坏书不看，坏话不听</strong><br/>'
      '② <strong>不轻看自己，天天向上</strong><br/><br/>'
      '<strong>一句话：守眼守心。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 向上</h2>'
      '<p>四句话，守眼守心——</p>'
      '<h3>"非圣书，屏勿视。蔽聪明，坏心志。勿自暴，勿自弃。圣与贤，可驯致。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>坏书别看，'
      '别糟蹋自己也别放弃自己。</p><p>📖 守门</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>人是一天天长成的；'
      '看得对、不认输，就往圣贤那边挪。</p><p>💡 向上</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>眼要清、心要立；'
      '圣与贤，可驯致。</p><p>🌱 天天向上</p>'),
 72: '<p>这是「余力学文课堂」第四十七课：余力学文末段，也是《弟子规》全篇最后一课。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「非圣书」是不是只能读古书？</h3>'
       '<p><strong>不是禁书单，是挑标准。</strong><br/><br/>'
       '① <strong>读完更明白、更有劲，就是好书</strong><br/>'
       '② <strong>读完更糊涂、更烦躁，就是「非圣书」</strong><br/>'
       '③ <strong>记法：看它把你往哪儿带。</strong></p>'
       '<h3>❓ 「屏」为什么读 bǐng？</h3>'
       '<p><strong>这里同「摒」，是推开。</strong><br/><br/>'
       '① <strong>屏 bǐng：屏弃、屏退，就是挡开</strong><br/>'
       '② <strong>屏 píng：屏风、屏幕，是那个物件</strong><br/>'
       '③ <strong>记法：推开读 bǐng，挡东西读 píng。</strong></p>'
       '<h3>❓ 「勿自暴自弃」是讲给差生听的？</h3>'
       '<p><strong>讲给每个人听。</strong><br/><br/>'
       '① <strong>做错题、考砸了，都不等于「我不行」</strong><br/>'
       '② <strong>「反正我就这样」才是真的输</strong><br/>'
       '③ <strong>记法：错了能改，就还在路上。</strong></p>'
       '<h3>❓ 「圣与贤，可驯致」是说人人成圣人？</h3>'
       '<p><strong>说的是方向，不是一天到位。</strong><br/><br/>'
       '① <strong>圣贤是品德学问做到极好的人</strong><br/>'
       '② <strong>他们也是一天一点长起来的</strong><br/>'
       '③ <strong>记法：今天比昨天好一点，就够得着。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 清一清眼睛</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>删掉一个让你停不下来又没用的内容</strong>；'
       '<strong>这就是「非圣书，屏勿视」</strong>。</p><p>💡 换一句话说自己</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把「我不行」改成「我下次怎么改」</strong>；'
       '<strong>这就是「勿自暴，勿自弃」</strong>。</p><p>🌱 每天记一笔</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>每天做一件让自己变好一点的小事，记下来</strong>；'
       '<strong>这就是「圣与贤，可驯致」</strong><br/><br/>'
       '<strong>本课的落点：向上。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>《弟子规》最后四句：守眼、守心、向上。<strong>可驯致</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">非圣书，屏勿视。蔽聪明，坏心志。'
       '勿自暴，勿自弃。圣与贤，可驯致。</p><p>回顾本课要点:</p>'
       '<p>余力学文末段 · 守眼守心。<strong>向上</strong>。</p>'
       '<p>非圣书，屏勿视 · 坏东西别看。<strong>眼睛要挑</strong>。</p>'
       '<p>蔽聪明，坏心志 · 看什么成什么。<strong>守眼</strong>。</p>'
       '<p>勿自暴，勿自弃 · 别放弃自己。<strong>一次不算一辈子</strong>。</p>'
       '<p>圣与贤，可驯致 · 渐渐能到。<strong>天天向上</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>《弟子规》收官——'
       '入则孝到余力学文七门讲完。</p>'
       '<div class="ds-quote">'),

 111: '<p>非圣书，屏勿视。蔽聪明，坏心志。勿自暴，勿自弃。圣与贤，可驯致。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「屏」「蔽」「驯致」怎么讲。'
       '② 今天删掉一个没用的内容源，写一句「我下次怎么改」。'
       '③ 想一想：《弟子规》这些话里，你最想做到哪一句。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>非圣书，屏勿视；蔽聪明，坏心志；'
       '勿自暴，勿自弃；圣与贤，可驯致。</strong></p></div>'),

 119: '            "非圣书，屏勿视。蔽聪明，坏心志。勿自暴，勿自弃。圣与贤，可驯致。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '587-fei-sheng-shu';",

 59: '<!-- 4. 非圣书屏勿视·蔽聪明坏心志 -->',
 61: '<!-- 5. 勿自暴勿自弃·圣与贤可驯致 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「非圣书」的「非」是什么意思？', opts: ['不是', '非常', '非要'], ans: 0, exp: '非是不是'},",
 "  {q: '2. 「屏勿视」的「屏」怎么读？', opts: ['bǐng，挡住、推开', 'píng，屏风', 'bīng，冰冷'], ans: 0, exp: '屏读 bǐng，同摒'},",
 "  {q: '3. 「蔽聪明」的「蔽」是什么意思？', opts: ['蒙住、遮住', '作弊', '隐蔽起来'], ans: 0, exp: '蔽是蒙住'},",
 "  {q: '4. 「坏心志」的「志」是什么意思？', opts: ['志向', '志气话', '杂志'], ans: 0, exp: '志是志向'},",
 "  {q: '5. 「勿自暴」的「暴」是什么意思？', opts: ['糟蹋自己', '暴脾气', '暴风雨'], ans: 0, exp: '暴是糟蹋'},",
 "  {q: '6. 「勿自弃」的「弃」是什么意思？', opts: ['放弃', '抛弃别人', '丢弃东西'], ans: 0, exp: '弃是放弃'},",
 "  {q: '7. 「可驯致」的「驯」是什么意思？', opts: ['渐渐', '驯服', '温顺'], ans: 0, exp: '驯是渐渐'},",
 "  {q: '8. 「圣与贤」指什么样的人？', opts: ['品德学问做到极好的人', '有钱的人', '当官的人'], ans: 0, exp: '圣贤是德才极好的人'},",
 "  {q: '9. 怎么判断一本书是不是「非圣书」？', opts: ['读了让人更糊涂、更烦躁的就别看', '不是古书的都别看', '字少的都别看'], ans: 0, exp: '看它把你往哪儿带'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['坏东西别看，别放弃自己，天天向上能成圣贤', '书读得越多越好', '人天生分好坏'], ans: 0, exp: '守眼守心向上'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("586-lie-dian-ji", "587-fei-sheng-shu")
    out = out.replace("yaoyue586", "yaoyue587")
    out = out.replace("第四十六课", "第四十七课")
    out = out.replace("余力学文第五段", "余力学文末段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
