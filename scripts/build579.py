#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build579: 以 578 为骨架，按行号替换文字生成第 579 课
《弟子规·泛爱众》末段（单成一课）：势服人，心不然。理服人，方无言。
只换文字，不动任何 HTML 标签；两句话，原文页字号放大以撑住版面。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/578-en-yu-bao/index.html"
DST_DIR = f"{ROOT}/lessons/579-shi-fu-ren"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十九课，泛爱众末段。原文：「势服人，心不然。理服人，方无言。」'
        '前两句讲靠权势、力气、嗓门压人，人家表面点头，心里不服；后两句讲把道理讲清楚，'
        '人家自己想通了，才真没话说。合起来：以势服人服一时，以理服人服一生。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.08em;font-size:2.1rem;line-height:2.7;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("势","shì"),("服","fú"),("人","rén")]) + "，" + _r([("心","xīn"),("不","bù"),("然","rán")]) + "。", True)
 + _p(_r([("理","lǐ"),("服","fú"),("人","rén")]) + "，" + _r([("方","fāng"),("无","wú"),("言","yán")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="势服人心不然，理服人方无言 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十九课：靠权势压人，人家心里不服；把道理讲清，人家才真没话说。泛爱众末段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/579-shi-fu-ren/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/579-shi-fu-ren/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 势服人心不然，理服人方无言 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">以理服人</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众末段：势服人，心不然</p>'
      '<p class="cover-desc">靠权势、靠嗓门、靠人多压人，人家当面点头，心里不服，'
      '势一没了照样不听你的；把道理讲清楚，人家自己想通了，才是真服。'
      '一句话：以势服人服一时，以理服人服一生。</p><div class="cover-seal">理</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众末段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:18px 16px 12px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.82rem;line-height:1.5;width:100%;max-width:none;margin-top:var(--ds-space-2)"><strong>通译</strong>：'
      '<strong>靠权势、靠力气压人，人家心里并不服气；靠道理服人，人家才真的没有话说。</strong></p>'
      '<p style="font-size:0.82rem;line-height:1.5;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「势」是权势、力气、地位、人多势众；「服」是服气、听你的；「不然」是心里不这样想、'
      '嘴上认了心里不认；「理」是道理；「方」是才；「无言」是没有话说、驳不出来。'
      '这是《弟子规》第四门「泛爱众」的最后一段，也是全篇讲「怎么待人」的收尾：'
      '前面讲怎么对人好，这里讲凭什么让人听你——靠势，还是靠理。</strong></p>'
      '<p style="font-size:0.82rem;line-height:1.5;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>势服人，心不然；理服人，方无言。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 两种让人听话的法子</h2>'
      '<p style="margin:0"><strong>一种靠「势」</strong><br/>'
      '① <strong>拿身份压、拿嗓门压、拿人多压</strong><br/>'
      '② <strong>压得住嘴，压不住心</strong><br/><br/>'
      '<strong>一句话：口服，心不服。</strong></p>'
      '<p><strong>一种靠「理」</strong><br/>'
      '① <strong>把前因后果说清楚</strong><br/>'
      '② <strong>让他自己点头，不是被你按住头</strong><br/><br/>'
      '<strong>一句话：心服，才长久。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>势服人：管一时</strong><br/>'
      '② <strong>理服人：管一世</strong><br/><br/>'
      '<strong>一句话：以势服人服一时，以理服人服一生。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>势服人，心不然</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>势：权势、力气、地位、人多势众</strong><br/>'
      '② <strong>不然：心里不这样认为，嘴上认了心里不认</strong><br/><br/>'
      '<strong>一句话：压服不是服。</strong></p>'
      '<p><strong>生活里什么叫「势服人」</strong><br/>'
      '① <strong>嗓门大的赢，谁凶听谁的</strong><br/>'
      '② <strong>「我是哥哥你就得听」、几个人挤对人</strong><br/><br/>'
      '<strong>一句话：靠的是势，不是理。</strong></p>'
      '<p><strong>为什么「心不然」</strong><br/>'
      '① <strong>当面点头，转身照旧</strong><br/>'
      '② <strong>心里记着，等你势弱再说</strong><br/><br/>'
      '<strong>一句话：压得住人，压不住心。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>理服人，方无言</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>理：道理，事情的是非曲直</strong><br/>'
      '② <strong>方：才；无言：没有话说，驳不出来</strong><br/><br/>'
      '<strong>一句话：服在理上，才没话说。</strong></p>'
      '<p><strong>什么叫「理服人」</strong><br/>'
      '① <strong>说清「为什么」，别只说「就得这样」</strong><br/>'
      '② <strong>先听完人家，再讲自己的理；自己先做到</strong><br/><br/>'
      '<strong>一句话：讲得清，才服得久。</strong></p>'
      '<p><strong>「方无言」的分量</strong><br/>'
      '① <strong>不是被堵住嘴，是想通了、认了</strong><br/>'
      '② <strong>遇上同样的事，他自己会这么做</strong><br/><br/>'
      '<strong>一句话：真服，是自己点的头。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 势与理，差在哪</h2>'
      '<p style="margin:0"><strong>「势」管外面</strong><br/>'
      '① <strong>管住的是行为：不敢不听</strong><br/>'
      '② <strong>势一撤，人就散</strong><br/><br/>'
      '<strong>一句话：压出来的听话，靠不住。</strong></p>'
      '<p><strong>「理」管里面</strong><br/>'
      '① <strong>管住的是心思：想明白了</strong><br/>'
      '② <strong>没人看着，他也照做</strong><br/><br/>'
      '<strong>一句话：说服出来的认同，散不了。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>想让人听你的，先说清「为什么」</strong><br/>'
      '② <strong>说不清理由的，多半是你自己没理</strong><br/><br/>'
      '<strong>一句话：先讲理，再讲输赢。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 一句一正一反</h2>'
      '<p style="margin:0"><strong>第一句：反面</strong><br/>'
      '① <strong>势服人——拿势压</strong><br/>'
      '② <strong>心不然——心里不服</strong><br/><br/>'
      '<strong>一句话：白压。</strong></p>'
      '<p><strong>第二句：正面</strong><br/>'
      '① <strong>理服人——讲道理</strong><br/>'
      '② <strong>方无言——驳不出来</strong><br/><br/>'
      '<strong>一句话：真服。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>势，压得住嘴</strong><br/>'
      '② <strong>理，压得住心</strong><br/><br/>'
      '<strong>一句话：以理服人，服一生。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 以理服人，服一生</h2>'
      '<p>两句话，一正一反——</p>'
      '<h3>"势服人，心不然。理服人，方无言。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>靠势压人，人家心里不服；'
      '靠理服人，人家才没话说。</p><p>📖 服在理上</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>势是外面的力气，理是里面的公道；'
      '压人靠一时之强，服人靠一世之理——真本事不是让人怕你，是让人服你。</p><p>💡 理</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>以理服人，服一生；'
      '先讲道理，再论输赢。</p><p>🌱 讲理不压人</p>'),
 72: '<p>这是「弟子规课堂」第三十九课：泛爱众末段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 讲道理没人听，是不是还得靠凶？</h3>'
       '<p><strong>先查自己的理够不够硬。</strong><br/><br/>'
       '① <strong>说清「为什么」，别只说「就得这样」</strong><br/>'
       '② <strong>嗓门大不等于有理，凶一次丢一次人缘</strong><br/>'
       '③ <strong>记法：理不硬，才靠声大。</strong></p>'
       '<h3>❓ 当哥哥姐姐的，管弟弟妹妹不算「势服人」吧？</h3>'
       '<p><strong>看你怎么管。</strong><br/><br/>'
       '① <strong>「我是哥你就得听」——这是势</strong><br/>'
       '② <strong>「这样危险，因为……」——这是理</strong><br/>'
       '③ <strong>记法：身份能开口，道理才服人。</strong></p>'
       '<h3>❓ 碰上不讲理的人怎么办？</h3>'
       '<p><strong>不跟他比谁凶，先把事说清。</strong><br/><br/>'
       '① <strong>把事实摆出来，说完就停</strong><br/>'
       '② <strong>该找老师找老师，这不是告状，是讲理</strong><br/>'
       '③ <strong>记法：讲不通用规则，不用拳头。</strong></p>'
       '<h3>❓ 老师家长管我，也是「势服人」吗？</h3>'
       '<p><strong>不是，那是责任。</strong><br/><br/>'
       '① <strong>他们管你，是为你好，也担着责任</strong><br/>'
       '② <strong>你可以问理由，但不必当成欺压</strong><br/>'
       '③ <strong>记法：有爱的管，不算压。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 先讲为什么</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>想让人照你的做，先说清「因为什么」</strong>；'
       '<strong>这就是「理服人」</strong>。</p><p>💡 不拿身份压</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>「我是哥」「我人多」这类话，少说</strong>；'
       '<strong>这就是「势服人，心不然」</strong>。</p><p>🌱 自己先做到</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>要求别人做到的，自己先做到，道理才有分量</strong>；'
       '<strong>这就是「方无言」</strong><br/><br/>'
       '<strong>本课的落点：以理服人，服一生。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众末段，势压不住心，理才服得久。记牢：<strong>以理服人</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">势服人，心不然。理服人，方无言。</p>'
       '<p>回顾本课要点:</p>'
       '<p>泛爱众末段 · 一正一反，两种服人法。<strong>以理服人</strong>。</p>'
       '<p>势服人，心不然 · 压得住嘴压不住心。<strong>口服不算服</strong>。</p>'
       '<p>理服人，方无言 · 讲清了才真服。<strong>心服才算服</strong>。</p>'
       '<p>势管外面 · 势一撤人就散。<strong>靠不住</strong>。</p>'
       '<p>理管里面 · 没人看着也照做。<strong>散不了</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众末段，也是全篇讲待人的收尾；'
       '前面讲怎么对人好，这里讲凭什么让人听你。</p>'
       '<div class="ds-quote">'),

 111: '<p>势服人，心不然。理服人，方无言。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「势」「不然」「方」「无言」怎么讲。'
       '② 今天想让人听你的，先说清一个「为什么」。'
       '③ 想一想：你有没有拿身份、拿嗓门压过人。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>势服人，心不然；理服人，方无言。</strong></p></div>'),

 119: '            "势服人，心不然。理服人，方无言。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '579-shi-fu-ren';",

 59: '<!-- 4. 势服人·心不然 -->',
 61: '<!-- 5. 理服人·方无言 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「势服人」的「势」是什么意思？', opts: ['权势、力气、地位', '姿势', '形势好坏'], ans: 0, exp: '势是权势、力气、地位'},",
 "  {q: '2. 「心不然」的「不然」是什么意思？', opts: ['心里不这样认为、不服', '不是这样写的', '不然就算了'], ans: 0, exp: '不然是心里不认'},",
 "  {q: '3. 「理服人」的「理」是什么意思？', opts: ['道理、是非曲直', '整理', '理会'], ans: 0, exp: '理是道理'},",
 "  {q: '4. 「方无言」的「方」是什么意思？', opts: ['才', '方正', '地方'], ans: 0, exp: '方是才'},",
 "  {q: '5. 「无言」在这里是什么意思？', opts: ['没有话说、驳不出来', '不说话不理人', '无话可说很伤心'], ans: 0, exp: '无言是驳不出来'},",
 "  {q: '6. 「势服人，心不然」是说什么？', opts: ['靠权势压人，当面听话心里不服', '有势力的人心不好', '服人要用心'], ans: 0, exp: '压服不是真服'},",
 "  {q: '7. 「理服人，方无言」是说什么？', opts: ['讲清道理让人服，人家才真没话说', '有理就不用说话', '不说话最有理'], ans: 0, exp: '服在理上'},",
 "  {q: '8. 靠势压人最大的毛病是什么？', opts: ['势一没了人就不听，心里还结着怨', '太费力气', '容易得罪坏人'], ans: 0, exp: '势一撤人就散'},",
 "  {q: '9. 同学不听你的，最好怎么办？', opts: ['把道理讲清楚，让他自己想通', '嗓门比他更大', '找几个同学一起压他'], ans: 0, exp: '讲理不压人'},",
 "  {q: '10. 这两句总的讲什么？', opts: ['以理服人胜过以势压人：势服一时，理服一生', '怎么让自己更有势力', '怎么让人不敢反驳'], ans: 0, exp: '以理服人，服一生'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("578-en-yu-bao", "579-shi-fu-ren")
    out = out.replace("yaoyue579", "yaoyue580")
    out = out.replace("第三十八课", "第三十九课")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
