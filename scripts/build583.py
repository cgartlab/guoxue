#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build583: 以 582 为骨架，按行号替换文字生成第 583 课
《弟子规·余力学文》第二段：读书法，有三到。心眼口，信皆要。方读此，勿慕彼。此未终，彼勿起。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/582-bu-li-xing/index.html"
DST_DIR = f"{ROOT}/lessons/583-du-shu-fa-san-dao"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十三课，余力学文第二段。原文：「读书法，有三到。心眼口，信皆要。'
        '方读此，勿慕彼。此未终，彼勿起。」前两句讲读书的方法：心到、眼到、口到，三样都要紧；'
        '后两句讲手里这本没读完，别急着开另一本。合起来：读书要专心，一本一本读。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("读","dú"),("书","shū"),("法","fǎ")]) + "，" + _r([("有","yǒu"),("三","sān"),("到","dào")]) + "。", True)
 + _p(_r([("心","xīn"),("眼","yǎn"),("口","kǒu")]) + "，" + _r([("信","xìn"),("皆","jiē"),("要","yào")]) + "。")
 + _p(_r([("方","fāng"),("读","dú"),("此","cǐ")]) + "，" + _r([("勿","wù"),("慕","mù"),("彼","bǐ")]) + "。")
 + _p(_r([("此","cǐ"),("未","wèi"),("终","zhōng")]) + "，" + _r([("彼","bǐ"),("勿","wù"),("起","qǐ")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="读书法有三到，此未终彼勿起 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十三课：心到眼到口到，三到都要紧；一本没读完，别忙开另一本。读书要专心。余力学文第二段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/583-du-shu-fa-san-dao/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/583-du-shu-fa-san-dao/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 读书法有三到 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">三到</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文第二段：读书法，有三到</p>'
      '<p class="cover-desc">读书有方法：心跟着想、眼跟着看、嘴跟着念，三样缺一样都读不进去。'
      '还有一条：手里这本没读完，别忙着开另一本。'
      '一句话：读书要专心，一本一本读。</p><div class="cover-seal">读</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文第二段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>读书的方法是：要做到「三到」。心要到、眼要到、口要到，这三样确实都要紧，缺一样都不算读到。'
      '正在读这一本，就别惦记那一本；这一本还没读完，那一本先不要开头。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「读书法」是读书的方法；「三到」是心到、眼到、口到；'
      '「信」读 xìn，这里是「确实、真的」，不是「信用」；「皆」是都；「要」是要紧；'
      '「方」是正、正在；「慕」是想着、羡慕；「彼」是那一本；'
      '「终」是读完；「起」是开头。这一课紧接上一课：学要和做并进，可学和做都要有章法——'
      '读书的章法，就是「三到」和「一本一本读」。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>读书法，有三到；心眼口，信皆要；方读此，勿慕彼；此未终，彼勿起。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 读书的两条规矩</h2>'
      '<p style="margin:0"><strong>第一条：三到</strong><br/>'
      '① <strong>心到：心里跟着想</strong><br/>'
      '② <strong>眼到、口到：看着、念着</strong><br/><br/>'
      '<strong>一句话：三样都要紧。</strong></p>'
      '<p><strong>第二条：一本一本来</strong><br/>'
      '① <strong>这本没读完，别开头那本</strong><br/>'
      '② <strong>读一半换一本，两本都没读成</strong><br/><br/>'
      '<strong>一句话：读完整一本。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「怎么读」</strong><br/>'
      '② <strong>后两句讲「读哪本」</strong><br/><br/>'
      '<strong>一句话：专心，读完整。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>读书法，有三到；心眼口，信皆要</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>读书法：读书的方法；三到：心到、眼到、口到</strong><br/>'
      '② <strong>信 xìn：确实、真的；皆：都</strong><br/><br/>'
      '<strong>一句话：三到，缺一不可。</strong></p>'
      '<p><strong>读书法，有三到</strong><br/>'
      '① <strong>眼看字，心想着意思，嘴念着声</strong><br/>'
      '② <strong>光看不念容易走神，光念不想等于没读</strong><br/><br/>'
      '<strong>一句话：读书有章法。</strong></p>'
      '<p><strong>心眼口，信皆要</strong><br/>'
      '① <strong>三到里，心到最要紧</strong><br/>'
      '② <strong>心不在，看十遍也白看</strong><br/><br/>'
      '<strong>一句话：心到，才算读到。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>方读此，勿慕彼；此未终，彼勿起</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>方：正、正在；慕：想着、羡慕</strong><br/>'
      '② <strong>终：读完；起：开头</strong><br/><br/>'
      '<strong>一句话：一本一本来。</strong></p>'
      '<p><strong>方读此，勿慕彼</strong><br/>'
      '① <strong>手里这本才翻几页，眼睛已看下一本</strong><br/>'
      '② <strong>这本翻翻，那本翻翻，都是半截</strong><br/><br/>'
      '<strong>一句话：贪多嚼不烂。</strong></p>'
      '<p><strong>此未终，彼勿起</strong><br/>'
      '① <strong>这本没读完，那本先别开头</strong><br/>'
      '② <strong>读完一本，心里才有一整块</strong><br/><br/>'
      '<strong>一句话：读完，再开新的。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 读得进去的两个条件</h2>'
      '<p style="margin:0"><strong>心要到</strong><br/>'
      '① <strong>读的时候只想这一件事</strong><br/>'
      '② <strong>手机、电视先放一边</strong><br/><br/>'
      '<strong>一句话：专心，才进得去。</strong></p>'
      '<p><strong>一本一本来</strong><br/>'
      '① <strong>读完一本，再开下一本</strong><br/>'
      '② <strong>同时在读的，最好只有一本</strong><br/><br/>'
      '<strong>一句话：读完，才连得上。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>读书前先定读几页，读完再合书</strong><br/>'
      '② <strong>念出声、划重点，让眼口都跟上</strong><br/><br/>'
      '<strong>一句话：三到加一本。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两件事</h2>'
      '<p style="margin:0"><strong>前两句：怎么读</strong><br/>'
      '① <strong>读书法，有三到——先讲方法</strong><br/>'
      '② <strong>心眼口，信皆要——三到都要</strong><br/><br/>'
      '<strong>一句话：专心。</strong></p>'
      '<p><strong>后两句：读哪本</strong><br/>'
      '① <strong>方读此，勿慕彼——别看那本</strong><br/>'
      '② <strong>此未终，彼勿起——读完再开</strong><br/><br/>'
      '<strong>一句话：专一。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>心到眼到口到，三样都要</strong><br/>'
      '② <strong>一本没读完，另一本不开</strong><br/><br/>'
      '<strong>一句话：读书要专。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 读到心里</h2>'
      '<p>四句话，两条规矩——</p>'
      '<h3>"读书法，有三到。心眼口，信皆要。方读此，勿慕彼。此未终，彼勿起。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>心到、眼到、口到都要紧，'
      '一本没读完别开下一本。</p><p>📖 三到</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>读书不是眼睛过一遍，'
      '是把心放进去；一次只读一本，才读得完整。</p><p>💡 专心</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>读得进、读得完；'
      '心到，一本一本读。</p><p>🌱 读到心里</p>'),
 72: '<p>这是「余力学文课堂」第四十三课：余力学文第二段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「三到」为什么没有「手到」？</h3>'
       '<p><strong>原话只有三到，手到是后人添的。</strong><br/><br/>'
       '① <strong>「三到」出自宋代朱熹讲读书的话</strong><br/>'
       '② <strong>后来有人补一句「手到」：做笔记、划重点</strong><br/>'
       '③ <strong>记法：手到是帮手，心到才是根。</strong></p>'
       '<h3>❓ 不出声念，算不算「口到」？</h3>'
       '<p><strong>低年级念出声最好。</strong><br/><br/>'
       '① <strong>念出声，眼睛和耳朵一起盯着字，跑不掉</strong><br/>'
       '② <strong>高年级可以不出声，嘴上要跟着动、心里跟着念</strong><br/>'
       '③ <strong>记法：口到是让字从嘴里过一遍。</strong></p>'
       '<h3>❓ 「勿慕彼」是不是不许看别的书？</h3>'
       '<p><strong>不是不许，是别同时开好几本。</strong><br/><br/>'
       '① <strong>课外想读什么都可以，一本读完再换</strong><br/>'
       '② <strong>同时开五本，五本都是半截，心里都是乱的</strong><br/>'
       '③ <strong>记法：换书可以，别半途换。</strong></p>'
       '<h3>❓ 一本书实在读不下去怎么办？</h3>'
       '<p><strong>先看是太难还是太长。</strong><br/><br/>'
       '① <strong>太难：换一本浅一点的，不算半途而废</strong><br/>'
       '② <strong>太长：定好每天读几页，分几天读完</strong><br/>'
       '③ <strong>记法：说清楚再换，不是随手丢。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 读前先定页数</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>打开书先说一句「今天读到第几页」</strong>；'
       '<strong>这就是「方读此」的定心</strong>。</p><p>💡 念出声划一划</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>难懂的地方念出声、划上线</strong>；'
       '<strong>这就是「心眼口，信皆要」</strong>。</p><p>🌱 读完再开新的</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>一本读完，合上书说一句「讲的是什么」</strong>；'
       '<strong>这就是「此未终，彼勿起」</strong><br/><br/>'
       '<strong>本课的落点：读到心里。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲读书的两条规矩：三到，一本一本。记牢：<strong>读到心里</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">读书法，有三到。心眼口，信皆要。'
       '方读此，勿慕彼。此未终，彼勿起。</p><p>回顾本课要点:</p>'
       '<p>余力学文第二段 · 两条规矩。<strong>专一</strong>。</p>'
       '<p>读书法，有三到 · 心到眼到口到。<strong>缺一不可</strong>。</p>'
       '<p>心眼口，信皆要 · 心到最要紧。<strong>心不在白看</strong>。</p>'
       '<p>方读此，勿慕彼 · 别惦记那一本。<strong>贪多嚼不烂</strong>。</p>'
       '<p>此未终，彼勿起 · 读完再开。<strong>完整一本</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>余力学文第二段；上一段讲学与做并进，'
       '这一段讲读书怎么读。</p>'
       '<div class="ds-quote">'),

 111: '<p>读书法，有三到。心眼口，信皆要。方读此，勿慕彼。此未终，彼勿起。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「三到」「信」「方」「慕」怎么讲。'
       '② 今天读书只用三到，读完一本再换。'
       '③ 想一想：你有没有一本书读一半就丢下的。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>读书法，有三到；心眼口，信皆要；'
       '方读此，勿慕彼；此未终，彼勿起。</strong></p></div>'),

 119: '            "读书法，有三到。心眼口，信皆要。方读此，勿慕彼。此未终，彼勿起。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '583-du-shu-fa-san-dao';",

 59: '<!-- 4. 读书法有三到·心眼口信皆要 -->',
 61: '<!-- 5. 方读此勿慕彼·此未终彼勿起 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「读书法」的「法」是什么意思？', opts: ['方法', '法术', '办法多'], ans: 0, exp: '法是方法'},",
 "  {q: '2. 「有三到」指哪三到？', opts: ['心到、眼到、口到', '手到、脚到、眼到', '耳到、眼到、手到'], ans: 0, exp: '三到是心眼口'},",
 "  {q: '3. 「心眼口，信皆要」的「信」是什么意思？', opts: ['确实、真的', '信用', '写信'], ans: 0, exp: '信是确实'},",
 "  {q: '4. 「信皆要」的「皆」是什么意思？', opts: ['都', '只', '全不'], ans: 0, exp: '皆是都'},",
 "  {q: '5. 三到里最要紧的是哪一到？', opts: ['心到', '眼到', '口到'], ans: 0, exp: '心到最要紧'},",
 "  {q: '6. 「方读此」的「方」是什么意思？', opts: ['正、正在', '方形', '方法'], ans: 0, exp: '方是正在'},",
 "  {q: '7. 「勿慕彼」的「慕」是什么意思？', opts: ['想着、羡慕', '爱慕的人', '仰慕老师'], ans: 0, exp: '慕是想着'},",
 "  {q: '8. 「此未终」的「终」是什么意思？', opts: ['读完', '最后', '死'], ans: 0, exp: '终是读完'},",
 "  {q: '9. 「彼勿起」的「起」是什么意思？', opts: ['开头', '起来', '起床'], ans: 0, exp: '起是开头'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['读书要三到，一本读完再读下一本', '读书要读得快', '读书要读得多'], ans: 0, exp: '三到加一本一本来'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("582-bu-li-xing", "583-du-shu-fa-san-dao")
    out = out.replace("yaoyue582", "yaoyue583")
    out = out.replace("第四十二课", "第四十三课")
    out = out.replace("余力学文第一段", "余力学文第二段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
