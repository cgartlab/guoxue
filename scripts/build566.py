#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build566: 以 565 为骨架，按行号替换文字生成第 566 课
《弟子规·信》第三段：事非宜，勿轻诺。苟轻诺，进退错。凡道字，重且舒。勿急疾，勿模糊。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 565 全等。"""
import io, os, re, shutil

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/565-jian-qiao-yu/index.html"
DST_DIR = f"{ROOT}/lessons/566-shi-fei-yi"
DST = f"{DST_DIR}/index.html"

# ---------- 新文案 ----------
DESC = ('《弟子规》第二十六课，信第三段。原文：「事非宜，勿轻诺。苟轻诺，进退错。'
        '凡道字，重且舒。勿急疾，勿模糊。」前四句讲不合情理的事不要轻易答应，'
        '轻易答应了就会进退两难；后四句讲说话吐字要稳重舒缓，不要又急又快、含含糊糊。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("事","shì"),("非","fēi"),("宜","yí")]) + "，" + _r([("勿","wù"),("轻","qīng"),("诺","nuò")]) + "。", True)
 + _p(_r([("苟","gǒu"),("轻","qīng"),("诺","nuò")]) + "，" + _r([("进","jìn"),("退","tuì"),("错","cuò")]) + "。")
 + _p(_r([("凡","fán"),("道","dào"),("字","zì")]) + "，" + _r([("重","zhòng"),("且","qiě"),("舒","shū")]) + "。")
 + _p(_r([("勿","wù"),("急","jí"),("疾","jí")]) + "，" + _r([("勿","wù"),("模","mó"),("糊","hú")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="事非宜，勿轻诺；凡道字，重且舒 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第二十六课：答应要谨慎，说话要清楚。信第三段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/566-shi-fei-yi/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/566-shi-fei-yi/index.html" rel="canonical"/>',
 12: '<title>信 · 事非宜，勿轻诺，凡道字，重且舒 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">事非宜</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》信第三段：事非宜，勿轻诺</p>'
      '<p class="cover-desc">答应别人之前，先想一想。不合情理的事、自己办不到的事，别随口应下；'
      '应了却办不到，往前失信，退后食言，两头为难。说话也要稳重清楚：字字说稳，不急不糊。'
      '一句话：诺要慎，话要清。</p><div class="cover-seal">信</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 信第三段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>事情不合情理，不要轻易答应；如果轻易答应了，往前走办不到，往后退又说不出口，进退都是错。'
      '说话吐字，要稳重而舒缓；不要又急又快，不要含含糊糊。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「宜」读 yí，是合适、应当；「非宜」就是不合情理、不该做；「诺」读 nuò，是答应、许诺；'
      '「苟」读 gǒu，是如果、假使；「错」是错失、行不通；「道字」是说话吐字；「重」读 zhòng，是稳重、有分量；'
      '「且」是而且；「舒」是舒缓、从容；「急疾」是又急又快；「模糊」是含混不清。'
      '这一段接着上一段，讲嘴巴的两件事：一是答应要慎，二是吐字要清。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>事非宜，勿轻诺；苟轻诺，进退错；凡道字，重且舒；勿急疾，勿模糊。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 诺要慎，话要清</h2>'
      '<p style="margin:0"><strong>先说「管住嘴上的应」</strong><br/>'
      '① <strong>不合情理的事、做不到的事，别一口应下</strong><br/>'
      '② <strong>应下了办不到，两头都难受</strong><br/><br/>'
      '<strong>一句话：诺要慎。</strong></p>'
      '<p><strong>再说「管住嘴上的快」</strong><br/>'
      '① <strong>说话吐字要稳重舒缓</strong><br/>'
      '② <strong>不急不抢，不含含糊糊</strong><br/><br/>'
      '<strong>一句话：话要清。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>上一段讲说话要干净、要稳当，这一段讲答应要慎、吐字要清</strong><br/>'
      '② <strong>答应得稳，说得清楚，人才信得过</strong><br/><br/>'
      '<strong>一句话：诺重字清。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>事非宜，勿轻诺；苟轻诺，进退错</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>宜 yí：合适、应当；非宜＝不合情理、不该做</strong><br/>'
      '② <strong>诺 nuò：答应、许诺；苟 gǒu：如果、假使</strong><br/><br/>'
      '<strong>一句话：答应之前先掂量。</strong></p>'
      '<p><strong>事非宜，勿轻诺</strong><br/>'
      '① <strong>不该做的事、做不到的事，先别应</strong><br/>'
      '② <strong>一时碍于面子应下来，后面更难办</strong><br/><br/>'
      '<strong>一句话：不合宜的，别轻应。</strong></p>'
      '<p><strong>苟轻诺，进退错</strong><br/>'
      '① <strong>应了办不到，往前是失信，退后是食言</strong><br/>'
      '② <strong>「错」不是做错一件事，是把自己卡在中间</strong><br/><br/>'
      '<strong>一句话：轻诺一句，两头为难。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>凡道字，重且舒；勿急疾，勿模糊</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>道字：说话吐字；重 zhòng：稳重、有分量</strong><br/>'
      '② <strong>舒：舒缓、从容；急疾：又急又快；模糊：含混不清</strong><br/><br/>'
      '<strong>一句话：话要说清楚。</strong></p>'
      '<p><strong>凡道字，重且舒</strong><br/>'
      '① <strong>一个字一个字说稳，别人才听得进</strong><br/>'
      '② <strong>不急不抢，是心里有底的样子</strong><br/><br/>'
      '<strong>一句话：话要说得稳。</strong></p>'
      '<p><strong>勿急疾，勿模糊</strong><br/>'
      '① <strong>抢着说，别人听不清，还容易听错</strong><br/>'
      '② <strong>含含糊糊最误事，说不明白等于没说</strong><br/><br/>'
      '<strong>一句话：不抢不急，不含糊。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 慎与清</h2>'
      '<p style="margin:0"><strong>前四句讲「慎」</strong><br/>'
      '① <strong>不合情理的不轻应</strong><br/>'
      '② <strong>应下了就要办到</strong><br/><br/>'
      '<strong>一句话：诺要慎。</strong></p>'
      '<p><strong>后四句讲「清」</strong><br/>'
      '① <strong>吐字稳重、舒缓</strong><br/>'
      '② <strong>不急不糊，说得明白</strong><br/><br/>'
      '<strong>一句话：话要清。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>同学请你帮忙，先想「我做得到吗」，再答</strong><br/>'
      '② <strong>说话放慢一点，一个字一个字说清</strong><br/><br/>'
      '<strong>一句话：答应得稳，说得明白。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前四句：答应要慎</strong><br/>'
      '① <strong>事非宜，勿轻诺——不合情理的不应</strong><br/>'
      '② <strong>苟轻诺，进退错——轻应下，前后都难</strong><br/><br/>'
      '<strong>一句话：慎。</strong></p>'
      '<p><strong>后四句：吐字要清</strong><br/>'
      '① <strong>凡道字，重且舒——说话稳重舒缓</strong><br/>'
      '② <strong>勿急疾，勿模糊——不急不糊</strong><br/><br/>'
      '<strong>一句话：清。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>不合宜的事不轻应，应了就要办到</strong><br/>'
      '② <strong>说话放慢说清楚，不急不含糊</strong><br/><br/>'
      '<strong>一句话：诺要慎，话要清。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 事非宜，勿轻诺。苟轻诺，进退错。凡道字，重且舒。勿急疾，勿模糊。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"事非宜，勿轻诺。苟轻诺，进退错。凡道字，重且舒。勿急疾，勿模糊。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>不合情理的事不轻易答应；'
      '说话吐字稳重清楚，不急着抢，不含含糊糊。</p><p>📖 诺慎</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>答应得稳、说得清楚，别人才敢信你。</p>'
      '<p>💡 口信</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>事非宜，勿轻诺；苟轻诺，进退错；'
      '凡道字，重且舒；勿急疾，勿模糊。</p><p>🌱 勿轻诺，勿模糊</p>'),
 72: '<p>这是「弟子规课堂」第二十六课：信第三段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 为什么「事非宜」就不能答应？</h3>'
       '<p><strong>因为应了办不到，比不答应更伤人。</strong><br/><br/>'
       '① <strong>应下来，就是给人家一个盼头</strong><br/>'
       '② <strong>办不成，人家的事耽误了，你的信用也丢了</strong><br/>'
       '③ <strong>记法：不合情理、做不到的，先说「我看看」，别一口应。</strong></p>'
       '<h3>❓ 「进退错」的「错」是什么意思？</h3>'
       '<p><strong>不是做错一件具体的事，是把自己卡住了。</strong><br/><br/>'
       '① <strong>往前走办不到，是失信</strong><br/>'
       '② <strong>往后退不认账，是食言</strong><br/>'
       '③ <strong>记法：轻诺一句，两头为难。</strong></p>'
       '<h3>❓ 「重且舒」是要说话慢吗？</h3>'
       '<p><strong>是要说得稳、说得清，不是拖。</strong><br/><br/>'
       '① <strong>重读 zhòng，是字字有分量；舒是从容不慌</strong><br/>'
       '② <strong>太快就糊，太拖就让人着急</strong><br/>'
       '③ <strong>记法：慢一点，说清楚。</strong></p>'
       '<h3>❓ 「勿急疾，勿模糊」在今天怎么用？</h3>'
       '<p><strong>抢话和含糊，都会误事。</strong><br/><br/>'
       '① <strong>课堂上抢着答，容易答错</strong><br/>'
       '② <strong>含含糊糊传一句话，传到最后就拧了</strong><br/>'
       '③ <strong>记法：想好再说，说清为止。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 不轻易答应</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>答应前先想一句「我能不能做到」</strong>；'
       '<strong>这就是「事非宜，勿轻诺」</strong>。</p><p>💡 答应了就办到</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>应下的事记在本子上，按时做完</strong>；'
       '<strong>这就是「苟轻诺，进退错」的反面</strong>。</p><p>🌱 说话说清楚</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>放慢一点，一个字一个字说，别抢别糊</strong>；'
       '<strong>这就是「凡道字，重且舒；勿急疾，勿模糊」</strong><br/><br/>'
       '<strong>本课的落点：诺要慎，话要清。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲信第三段，接着上一课，还是说嘴巴。记牢：<strong>勿轻诺，勿模糊</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">事非宜，勿轻诺。苟轻诺，进退错。'
       '凡道字，重且舒。勿急疾，勿模糊。</p><p>回顾本课要点:</p>'
       '<p>信第三段 · 诺重字清。<strong>诺要慎，话要清</strong>。</p>'
       '<p>事非宜，勿轻诺 · 不合情理的不应。<strong>答应要慎</strong>。</p>'
       '<p>苟轻诺，进退错 · 轻应下两头难。<strong>诺出必践</strong>。</p>'
       '<p>凡道字，重且舒 · 说话稳重舒缓。<strong>字字说清</strong>。</p>'
       '<p>勿急疾，勿模糊 · 不急不糊。<strong>说清为止</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>信第三段；上一段（奸巧语，秽污词）讲说话要干净、要稳当，'
       '这一段讲答应要谨慎、吐字要清楚——先净口，再慎诺。</p><div class="ds-quote">'),
 111: '<p>事非宜，勿轻诺。苟轻诺，进退错。凡道字，重且舒。勿急疾，勿模糊。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「宜」「诺」「苟」怎么讲。'
       '② 今天答应别人之前，先停三秒想「我做到吗」。'
       '③ 说话放慢，让同桌听清每一个字。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>事非宜，勿轻诺；苟轻诺，进退错；'
       '凡道字，重且舒；勿急疾，勿模糊。</strong></p></div>'),

 119: '            "事非宜，勿轻诺。苟轻诺，进退错。凡道字，重且舒。勿急疾，勿模糊。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '566-shi-fei-yi';",
}

QUIZ_LINES = [
 "  {q: '1. 「事非宜」的「宜」是什么意思？', opts: ['合适、应当', '便宜', '应该做官'], ans: 0, exp: '宜读 yí，是合适、应当'},",
 "  {q: '2. 「勿轻诺」的「诺」是什么意思？', opts: ['答应、许诺', '署名', '文言虚词'], ans: 0, exp: '诺读 nuò，是答应'},",
 "  {q: '3. 「苟轻诺」的「苟」是什么意思？', opts: ['如果、假使', '随随便便', '苟且偷生'], ans: 0, exp: '苟读 gǒu，是如果'},",
 "  {q: '4. 「进退错」的「错」是什么意思？', opts: ['错失、行不通', '答错题', '交错在一起'], ans: 0, exp: '错是错失、行不通'},",
 "  {q: '5. 「凡道字」的「道字」指什么？', opts: ['说话吐字', '写字的道理', '念经文'], ans: 0, exp: '道字＝说话吐字'},",
 "  {q: '6. 「重且舒」的「重」怎么读、什么意思？', opts: ['zhòng，稳重、有分量', 'chóng，重复', 'zhòng，沉的东西'], ans: 0, exp: '重读 zhòng，稳重有分量'},",
 "  {q: '7. 「舒」是什么意思？', opts: ['舒缓、从容', '舒服', '展开'], ans: 0, exp: '舒是舒缓、从容'},",
 "  {q: '8. 「勿急疾」的「急疾」是什么意思？', opts: ['又急又快', '生了急病', '心里发急'], ans: 0, exp: '急疾＝又急又快'},",
 "  {q: '9. 「勿模糊」要求我们怎么说话？', opts: ['不含含糊糊，要说清楚', '声音越小越好', '拖得越慢越好'], ans: 0, exp: '模糊是含混不清'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['答应要谨慎，说话要清楚', '怎么讨好别人', '怎么记账算数'], ans: 0, exp: '诺要慎，话要清'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        idx = no - 1
        buf[idx] = txt
    out = "\n".join(buf)
    out = out.replace("565-jian-qiao-yu", "566-shi-fei-yi")
    out = out.replace("yaoyue566", "yaoyue567")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
