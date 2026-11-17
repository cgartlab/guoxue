#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build584: 以 583 为骨架，按行号替换文字生成第 584 课
《弟子规·余力学文》第三段：宽为限，紧用功。工夫到，滞塞通。心有疑，随札记。就人问，求确义。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/583-du-shu-fa-san-dao/index.html"
DST_DIR = f"{ROOT}/lessons/584-kuan-wei-xian"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十四课，余力学文第三段。原文：「宽为限，紧用功。工夫到，滞塞通。'
        '心有疑，随札记。就人问，求确义。」前两句讲读书的期限定得宽一点、功夫抓得紧一点，'
        '功夫下够了，卡住的地方自然通开；后两句讲心里有疑问就随手记下，去请教人，问到确切的意思。'
        '合起来：功夫要够，疑问要问。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("宽","kuān"),("为","wéi"),("限","xiàn")]) + "，" + _r([("紧","jǐn"),("用","yòng"),("功","gōng")]) + "。", True)
 + _p(_r([("工","gōng"),("夫","fu"),("到","dào")]) + "，" + _r([("滞","zhì"),("塞","sè"),("通","tōng")]) + "。")
 + _p(_r([("心","xīn"),("有","yǒu"),("疑","yí")]) + "，" + _r([("随","suí"),("札","zhá"),("记","jì")]) + "。")
 + _p(_r([("就","jiù"),("人","rén"),("问","wèn")]) + "，" + _r([("求","qiú"),("确","què"),("义","yì")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="宽为限紧用功，心有疑随札记 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十四课：期限放宽、功夫抓紧，功夫到了卡住的地方就通；有疑问随手记，去问明白。余力学文第三段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/584-kuan-wei-xian/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/584-kuan-wei-xian/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 宽为限紧用功 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">功夫</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文第三段：宽为限，紧用功</p>'
      '<p class="cover-desc">期限别逼太死，功夫要天天抓；功夫下够了，卡住的地方自己就通开。'
      '心里有疑问，随手记下来，去问人，问到确实的意思。'
      '一句话：功夫要够，疑问要问。</p><div class="cover-seal">功</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文第三段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>定读书的期限要放宽一点，用功夫要抓紧一点。功夫下够了，卡住不通的地方自然就通开了。'
      '心里有了疑问，随手记在本子上；再去找人请教，问出个确确实实的意思来。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「宽为限」是期限定得宽一些，不是不用功；「为」读 wéi，是定；「限」是期限；'
      '「紧」是抓紧；「工夫」是下的功夫、花的时间；「滞」是卡住不通；'
      '「塞」读 sè，是堵住，不读 sāi；「通」是通开；「疑」是疑问；'
      '「札」读 zhá，札记就是随手记的笔记；「就」是走到、去请教；「确」是确实、准确；「义」是意思。'
      '这一段接着上一段讲：三到、一本一本来之后，还要讲用功和问学。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>宽为限，紧用功；工夫到，滞塞通；心有疑，随札记；就人问，求确义。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 两件事：下功夫、把疑问清掉</h2>'
      '<p style="margin:0"><strong>头一件：功夫</strong><br/>'
      '① <strong>期限放宽，功夫抓紧</strong><br/>'
      '② <strong>下够了，卡住的地方会通</strong><br/><br/>'
      '<strong>一句话：不怕慢，怕不练。</strong></p>'
      '<p><strong>第二件：疑问</strong><br/>'
      '① <strong>有疑问随手记下来</strong><br/>'
      '② <strong>去问人，问到确实的意思</strong><br/><br/>'
      '<strong>一句话：不懂就问。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「怎么用功」</strong><br/>'
      '② <strong>后两句讲「怎么解疑」</strong><br/><br/>'
      '<strong>一句话：功夫加问学。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>宽为限，紧用功；工夫到，滞塞通</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>宽为限：期限定宽些；为 wéi：定</strong><br/>'
      '② <strong>滞 zhì：卡住；塞 sè：堵住，不读 sāi</strong><br/><br/>'
      '<strong>一句话：慢一点定，紧一点做。</strong></p>'
      '<p><strong>宽为限，紧用功</strong><br/>'
      '① <strong>不逼一天读一本，但天天要读</strong><br/>'
      '② <strong>宽是留余地，紧是不松手</strong><br/><br/>'
      '<strong>一句话：日子够长，功夫够密。</strong></p>'
      '<p><strong>工夫到，滞塞通</strong><br/>'
      '① <strong>读不懂的地方，多读两遍就透了</strong><br/>'
      '② <strong>功夫不到，急也没用</strong><br/><br/>'
      '<strong>一句话：水到渠成。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>心有疑，随札记；就人问，求确义</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>札 zhá 记：随手记的笔记</strong><br/>'
      '② <strong>就：走到、去请教；确：确实准确</strong><br/><br/>'
      '<strong>一句话：不懂就记，记了就去问。</strong></p>'
      '<p><strong>心有疑，随札记</strong><br/>'
      '① <strong>读到不懂的，先记在本子上</strong><br/>'
      '② <strong>不记，过一天就忘了问什么</strong><br/><br/>'
      '<strong>一句话：疑问不过夜。</strong></p>'
      '<p><strong>就人问，求确义</strong><br/>'
      '① <strong>问老师、问家长、问同学都行</strong><br/>'
      '② <strong>问到明白为止，别停在「差不多」</strong><br/><br/>'
      '<strong>一句话：一问到底。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 功夫深，疑问清</h2>'
      '<p style="margin:0"><strong>功夫要天天有</strong><br/>'
      '① <strong>每天读一点，比一天猛读强</strong><br/>'
      '② <strong>定得住，才下得去</strong><br/><br/>'
      '<strong>一句话：积少成多。</strong></p>'
      '<p><strong>疑问要清干净</strong><br/>'
      '① <strong>一个疑问留着，后面越读越糊涂</strong><br/>'
      '② <strong>问一个清一个，路才走得下去</strong><br/><br/>'
      '<strong>一句话：不留疙瘩。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>准备一个小本，专门记不懂的</strong><br/>'
      '② <strong>每周把那几条问明白、划掉</strong><br/><br/>'
      '<strong>一句话：本子在，疑问就散。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两件事</h2>'
      '<p style="margin:0"><strong>前两句：用功</strong><br/>'
      '① <strong>宽为限，紧用功——期限宽、功夫紧</strong><br/>'
      '② <strong>工夫到，滞塞通——够了就通</strong><br/><br/>'
      '<strong>一句话：练。</strong></p>'
      '<p><strong>后两句：问学</strong><br/>'
      '① <strong>心有疑，随札记——先记下</strong><br/>'
      '② <strong>就人问，求确义——再问清</strong><br/><br/>'
      '<strong>一句话：问。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>日子放宽，功夫抓紧</strong><br/>'
      '② <strong>疑问记下，问个明白</strong><br/><br/>'
      '<strong>一句话：练加问。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 功夫到了就通</h2>'
      '<p>四句话，两条路——</p>'
      '<h3>"宽为限，紧用功。工夫到，滞塞通。心有疑，随札记。就人问，求确义。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>期限放宽、功夫抓紧，'
      '有疑问记下来去问明白。</p><p>📖 功夫</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>进步靠日子攒，不靠一时猛；'
      '卡住不是笨，是功夫还没到。</p><p>💡 问学</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>功夫到了就通；'
      '不懂就问到底。</p><p>🌱 水到渠成</p>'),
 72: '<p>这是「余力学文课堂」第四十四课：余力学文第三段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「宽为限」是不是让我慢慢来、不用急？</h3>'
       '<p><strong>不是慢，是期限定得合理。</strong><br/><br/>'
       '① <strong>一口吃不成胖子，期限太紧只会放弃</strong><br/>'
       '② <strong>期限宽了，功夫反而要抓紧，天天有</strong><br/>'
       '③ <strong>记法：宽是留得住，紧是不松手。</strong></p>'
       '<h3>❓ 读不进去、卡住了怎么办？</h3>'
       '<p><strong>「滞塞通」：先加功夫，别硬磕。</strong><br/><br/>'
       '① <strong>多读两遍、换个说法讲讲、回头看前面</strong><br/>'
       '② <strong>还不行就先放下，明天再来，往往就通了</strong><br/>'
       '③ <strong>记法：不是笨，是功夫还差一点。</strong></p>'
       '<h3>❓ 疑问记下来了，可不好意思问？</h3>'
       '<p><strong>问不丢人，糊过去才丢人。</strong><br/><br/>'
       '① <strong>问老师、问家长、问同学都可以</strong><br/>'
       '② <strong>一个疑问留着，后面越读越糊涂</strong><br/>'
       '③ <strong>记法：问一句，省半天。</strong></p>'
       '<h3>❓ 「求确义」是不是每个字都要查到底？</h3>'
       '<p><strong>抓关键的，别钻牛角尖。</strong><br/><br/>'
       '① <strong>不懂的词、不懂的句子，问到懂</strong><br/>'
       '② <strong>细枝末节知道大概就行，不必纠缠</strong><br/>'
       '③ <strong>记法：大字问清楚，小字放过去。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 备一个疑问本</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>专门记读不懂的词和句子，一天写一条也好</strong>；'
       '<strong>这就是「心有疑，随札记」</strong>。</p><p>💡 每天读一点</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>不贪一天读很多，天天读十分钟</strong>；'
       '<strong>这就是「宽为限，紧用功」</strong>。</p><p>🌱 一周清一次</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把本子上的疑问一个个问明白、划掉</strong>；'
       '<strong>这就是「就人问，求确义」</strong><br/><br/>'
       '<strong>本课的落点：功夫到了就通。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲用功和问学：期限宽、功夫紧，疑问记、问明白。记牢：<strong>功夫到了就通</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">宽为限，紧用功。工夫到，滞塞通。'
       '心有疑，随札记。就人问，求确义。</p><p>回顾本课要点:</p>'
       '<p>余力学文第三段 · 练与问两条路。<strong>功夫</strong>。</p>'
       '<p>宽为限，紧用功 · 期限宽、功夫紧。<strong>不怕慢怕不练</strong>。</p>'
       '<p>工夫到，滞塞通 · 够了就通。<strong>水到渠成</strong>。</p>'
       '<p>心有疑，随札记 · 先记下来。<strong>疑问不过夜</strong>。</p>'
       '<p>就人问，求确义 · 问到明白。<strong>一问到底</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>余力学文第三段；上一段讲怎么读，'
       '这一段讲用功和问学。</p>'
       '<div class="ds-quote">'),

 111: '<p>宽为限，紧用功。工夫到，滞塞通。心有疑，随札记。就人问，求确义。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「限」「滞塞」「札记」「就」怎么讲。'
       '② 今天准备一个疑问本，写上第一条。'
       '③ 想一想：你有哪个问题一直没问明白。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>宽为限，紧用功；工夫到，滞塞通；'
       '心有疑，随札记；就人问，求确义。</strong></p></div>'),

 119: '            "宽为限，紧用功。工夫到，滞塞通。心有疑，随札记。就人问，求确义。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '584-kuan-wei-xian';",

 59: '<!-- 4. 宽为限紧用功·工夫到滞塞通 -->',
 61: '<!-- 5. 心有疑随札记·就人问求确义 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「宽为限」的「限」是什么意思？', opts: ['期限、进度', '限制别人', '有限'], ans: 0, exp: '限是期限'},",
 "  {q: '2. 「宽为限」讲的是什么？', opts: ['期限定宽一点，别贪快', '不用读书了', '把书放宽'], ans: 0, exp: '限是期限，宽是放宽'},",
 "  {q: '3. 「紧用功」的「紧」是什么意思？', opts: ['抓紧', '紧张', '太紧'], ans: 0, exp: '紧是抓紧'},",
 "  {q: '4. 「工夫到」的「工夫」是什么意思？', opts: ['下的功夫、花的时间', '工人和丈夫', '空工夫'], ans: 0, exp: '工夫是功夫'},",
 "  {q: '5. 「滞塞」的「塞」怎么读？', opts: ['sè，堵住', 'sāi，塞住', 'sài，边塞'], ans: 0, exp: '塞读 sè'},",
 "  {q: '6. 「滞塞通」是什么意思？', opts: ['卡住的地方功夫够了就通开', '路上堵车通了', '书读通了'], ans: 0, exp: '工夫到，自然通'},",
 "  {q: '7. 「随札记」的「札记」是什么？', opts: ['随手记的笔记', '一本好书', '写信'], ans: 0, exp: '札记是随手记的笔记'},",
 "  {q: '8. 「就人问」的「就」是什么意思？', opts: ['走到、去请教', '就是', '马上'], ans: 0, exp: '就是去、走向'},",
 "  {q: '9. 「求确义」的「确」是什么意思？', opts: ['确实、准确', '确定要', '确实难'], ans: 0, exp: '确是确实准确'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['功夫要够，有疑问要问明白', '读书越快越好', '读书不用问人'], ans: 0, exp: '练加问'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("583-du-shu-fa-san-dao", "584-kuan-wei-xian")
    out = out.replace("yaoyue583", "yaoyue584")
    out = out.replace("第四十三课", "第四十四课")
    out = out.replace("余力学文第二段", "余力学文第三段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
