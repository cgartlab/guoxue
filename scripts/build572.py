#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build572: 以 570 为骨架，按行号替换文字生成第 572 课
《弟子规·泛爱众》第一段：凡是人，皆须爱。天同覆，地同载。行高者，名自高。人所重，非貌高。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 570 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/570-wen-yu-kong/index.html"
DST_DIR = f"{ROOT}/lessons/572-fan-shi-ren"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十二课，泛爱众第一段。原文：「凡是人，皆须爱。天同覆，地同载。'
        '行高者，名自高。人所重，非貌高。」前四句讲只要是人就该去爱，因为大家同顶一片天、'
        '同踩一块地；后四句讲品行高的人名声自然高，别人看重的是德行，不是相貌外表。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("凡","fán"),("是","shì"),("人","rén")]) + "，" + _r([("皆","jiē"),("须","xū"),("爱","ài")]) + "。", True)
 + _p(_r([("天","tiān"),("同","tóng"),("覆","fù")]) + "，" + _r([("地","dì"),("同","tóng"),("载","zài")]) + "。")
 + _p(_r([("行","xíng"),("高","gāo"),("者","zhě")]) + "，" + _r([("名","míng"),("自","zì"),("高","gāo")]) + "。")
 + _p(_r([("人","rén"),("所","suǒ"),("重","zhòng")]) + "，" + _r([("非","fēi"),("貌","mào"),("高","gāo")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="凡是人，皆须爱；天同覆，地同载 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十二课：人都要爱，名声靠德行不靠长相。泛爱众第一段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/572-fan-shi-ren/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/572-fan-shi-ren/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 凡是人皆须爱，行高者名自高 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">凡是人</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第一段：凡是人，皆须爱</p>'
      '<p class="cover-desc">只要是人，都该去爱——大家同顶一片天，同踩一块地。'
      '品行高的人，名声自然高；别人看重的是你的为人，不是你的脸面。'
      '一句话：爱人如己，重德不重貌。</p><div class="cover-seal">爱</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第一段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>只要是人，都应该去爱；因为大家同顶一片天，同踩一块地。'
      '品行高的人，名声自然就高；人们所看重的，是他的德行，不是他的相貌外表。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「凡」是所有、凡是；「皆」是都；「须」是应该；「覆」是遮盖，天覆盖万物；'
      '「载」读 zài，是承载，地承载万物；「行」读 xíng，指品行、德行；「名」是名声；'
      '「重」读 zhòng，是看重；「貌」是相貌、外表。这是《弟子规》第四门「泛爱众」的开篇：'
      '前三门讲孝、讲悌、讲谨、讲信，都是对家里人和自己的事；这一门把心量放开，'
      '从爱一家人扩到爱一切人，又把看人的标准摆正——看德行，不看外表。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>凡是人，皆须爱；天同覆，地同载；行高者，名自高；人所重，非貌高。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 爱人如己，重德不重貌</h2>'
      '<p style="margin:0"><strong>先说「爱谁」</strong><br/>'
      '① <strong>不只爱家里人，凡是人都要爱</strong><br/>'
      '② <strong>同顶一片天、同踩一块地，本是一体</strong><br/><br/>'
      '<strong>一句话：人都该爱。</strong></p>'
      '<p><strong>再说「重什么」</strong><br/>'
      '① <strong>名声高低看德行，不看长相排场</strong><br/>'
      '② <strong>别人心里敬的，是你的为人</strong><br/><br/>'
      '<strong>一句话：重德不重貌。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前四句把心量放宽</strong><br/>'
      '② <strong>后四句把尺子摆正</strong><br/><br/>'
      '<strong>一句话：爱要广，眼要正。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>凡是人，皆须爱；天同覆，地同载</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>凡：所有、凡是；皆：都；须：应该</strong><br/>'
      '② <strong>覆：遮盖；载 zài：承载，托着</strong><br/><br/>'
      '<strong>一句话：人都要爱。</strong></p>'
      '<p><strong>凡是人，皆须爱</strong><br/>'
      '① <strong>不分亲疏、穷富、好看不好看</strong><br/>'
      '② <strong>起码头一条：不去伤人，不看轻人</strong><br/><br/>'
      '<strong>一句话：把心放宽。</strong></p>'
      '<p><strong>天同覆，地同载</strong><br/>'
      '① <strong>头顶同一片天，脚踩同一块地</strong><br/>'
      '② <strong>谁也不是外人，本是同根</strong><br/><br/>'
      '<strong>一句话：本是一体。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>行高者，名自高；人所重，非貌高</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>行 xíng：品行、德行；名：名声</strong><br/>'
      '② <strong>重 zhòng：看重；貌：相貌、外表</strong><br/><br/>'
      '<strong>一句话：德高名自高。</strong></p>'
      '<p><strong>行高者，名自高</strong><br/>'
      '① <strong>品行立得住，名声不用争，自己就来</strong><br/>'
      '② <strong>靠吹靠装的，早晚露底</strong><br/><br/>'
      '<strong>一句话：名声跟着德行走。</strong></p>'
      '<p><strong>人所重，非貌高</strong><br/>'
      '① <strong>人敬的是你的为人，不是你的脸</strong><br/>'
      '② <strong>穿得好、长得俊，撑不了几天</strong><br/><br/>'
      '<strong>一句话：重人不重貌。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>两句合看 · 爱与重</h2>'
      '<p style="margin:0"><strong>前四句讲「爱」</strong><br/>'
      '① <strong>心量从一家放到天下</strong><br/>'
      '② <strong>对人有善意，不轻慢</strong><br/><br/>'
      '<strong>一句话：爱得广。</strong></p>'
      '<p><strong>后四句讲「重」</strong><br/>'
      '① <strong>名声靠德行挣</strong><br/>'
      '② <strong>不靠外表撑</strong><br/><br/>'
      '<strong>一句话：看得准。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>对扫地阿姨、门卫爷爷也问一声好</strong><br/>'
      '② <strong>同学穿得旧、长得不好看，不笑话、不起外号</strong><br/><br/>'
      '<strong>一句话：不轻慢，不看脸。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前四句：爱什么人</strong><br/>'
      '① <strong>凡是人，皆须爱——只要是人就要爱</strong><br/>'
      '② <strong>天同覆，地同载——同天同地本一体</strong><br/><br/>'
      '<strong>一句话：广。</strong></p>'
      '<p><strong>后四句：重什么人</strong><br/>'
      '① <strong>行高者，名自高——德高名自高</strong><br/>'
      '② <strong>人所重，非貌高——重德不重貌</strong><br/><br/>'
      '<strong>一句话：正。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>谁都别轻慢</strong><br/>'
      '② <strong>看人看德行</strong><br/><br/>'
      '<strong>一句话：爱广，眼正。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 凡是人，皆须爱。天同覆，地同载。行高者，名自高。人所重，非貌高。</h2>'
      '<p>一句话，两层意思——</p>'
      '<h3>"凡是人，皆须爱。天同覆，地同载。行高者，名自高。人所重，非貌高。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>人都要爱；名声靠德行，不靠长相。</p>'
      '<p>📖 爱正</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>天下人本是一体，敬人就是敬自己；尺子放在德行上，人才站得稳。</p>'
      '<p>💡 一体</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>凡是人，皆须爱；天同覆，地同载；'
      '行高者，名自高；人所重，非貌高。</p><p>🌱 爱人重德</p>'),
 72: '<p>这是「弟子规课堂」第三十二课：泛爱众第一段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 坏人也要爱吗？</h3>'
       '<p><strong>是爱人不害人，不是认同坏事。</strong><br/><br/>'
       '① <strong>对人有基本的善意，不去伤人</strong><br/>'
       '② <strong>他做坏事该说该管，但不看轻他这个人</strong><br/>'
       '③ <strong>记法：爱人不等于认同。</strong></p>'
       '<h3>❓ 「天同覆，地同载」什么意思？</h3>'
       '<p><strong>大家同顶一片天，同踩一块地。</strong><br/><br/>'
       '① <strong>覆：天盖着万物；载：地托着万物</strong><br/>'
       '② <strong>谁也不是外人，都是天地养的</strong><br/>'
       '③ <strong>记法：同天同地，本是一体。</strong></p>'
       '<h3>❓ 「行高者，名自高」是图名声吗？</h3>'
       '<p><strong>不是。是名声跟着德行走。</strong><br/><br/>'
       '① <strong>德行立得住，名声自己来</strong><br/>'
       '② <strong>靠吹靠装的，早晚露底</strong><br/>'
       '③ <strong>记法：先修德，再有名。</strong></p>'
       '<h3>❓ 为什么说「人所重，非貌高」？</h3>'
       '<p><strong>人敬的是你的为人，不是你的脸。</strong><br/><br/>'
       '① <strong>穿得好、长得俊，撑不了几天</strong><br/>'
       '② <strong>你帮过人、说过公道话，人记一辈子</strong><br/>'
       '③ <strong>记法：重人不重貌。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 谁都不轻慢</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>对扫地阿姨、门卫爷爷也问一声好</strong>；'
       '<strong>这就是「凡是人，皆须爱」</strong>。</p><p>💡 不看脸不看病</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>同学穿得旧、长得不好看，你不笑话、不起外号</strong>；'
       '<strong>这就是「人所重，非貌高」</strong>。</p><p>🌱 靠为人挣脸</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把功课做好、把话说实，让人服你的为人</strong>；'
       '<strong>这就是「行高者，名自高」</strong><br/><br/>'
       '<strong>本课的落点：爱人如己，重德不重貌。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第一段，心量从一家放到天下。记牢：<strong>爱人重德</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">凡是人，皆须爱。天同覆，地同载。'
       '行高者，名自高。人所重，非貌高。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第一段 · 爱得广，看得准。<strong>爱人重德</strong>。</p>'
       '<p>凡是人，皆须爱 · 只要是人就要爱。<strong>都得爱</strong>。</p>'
       '<p>天同覆，地同载 · 同顶天同踩地。<strong>本是一体</strong>。</p>'
       '<p>行高者，名自高 · 德高名声自高。<strong>名声跟德行</strong>。</p>'
       '<p>人所重，非貌高 · 看德行不看长相。<strong>重人不重貌</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第一段（第四门开篇）；前三门讲孝、讲悌、'
       '讲谨、讲信，都是对家里人和自己的事，这一门把心量放开，从爱一家人扩到爱一切人。</p>'
       '<div class="ds-quote">'),

 111: '<p>凡是人，皆须爱。天同覆，地同载。行高者，名自高。人所重，非貌高。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「覆」「载」「行」「貌」怎么讲。'
       '② 今天对三个人主动问好，其中一个是平时没说过话的。'
       '③ 想一想：你敬一个人，敬的是他的什么。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>凡是人，皆须爱；天同覆，地同载；'
       '行高者，名自高；人所重，非貌高。</strong></p></div>'),

 119: '            "凡是人，皆须爱。天同覆，地同载。行高者，名自高。人所重，非貌高。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '572-fan-shi-ren';",

 59: '<!-- 4. 凡是人皆须爱·天同覆地同载 -->',
 61: '<!-- 5. 行高者名自高·人所重非貌高 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「凡是人，皆须爱」的「皆」是什么意思？', opts: ['都', '一起', '将要'], ans: 0, exp: '皆是都'},",
 "  {q: '2. 「皆须爱」的「须」是什么意思？', opts: ['应该', '胡须', '必须等'], ans: 0, exp: '须是应该'},",
 "  {q: '3. 「天同覆」的「覆」是什么意思？', opts: ['遮盖', '翻倒', '恢复'], ans: 0, exp: '覆是遮盖'},",
 "  {q: '4. 「地同载」的「载」怎么读？', opts: ['zài，承载', 'zǎi，记载', 'zāi，栽种'], ans: 0, exp: '载读 zài，是承载'},",
 "  {q: '5. 「天同覆，地同载」是说什么？', opts: ['大家同顶一片天、同踩一块地', '天比地大', '天地会变'], ans: 0, exp: '同天同地，本是一体'},",
 "  {q: '6. 「行高者」的「行」怎么读、什么意思？', opts: ['xíng，品行、德行', 'háng，行业', 'hàng，排行'], ans: 0, exp: '行读 xíng，指品行'},",
 "  {q: '7. 「名自高」的「名」是什么意思？', opts: ['名声', '名字', '名额'], ans: 0, exp: '名是名声'},",
 "  {q: '8. 「人所重」的「重」怎么读？', opts: ['zhòng，看重', 'chóng，重复', 'zhǒng，种类'], ans: 0, exp: '重读 zhòng，是看重'},",
 "  {q: '9. 「非貌高」的「貌」是什么意思？', opts: ['相貌、外表', '礼貌', '面貌一新'], ans: 0, exp: '貌是相貌、外表'},",
 "  {q: '10. 这一段总的讲什么？', opts: ['人都要爱，名声靠德行不靠外表', '怎么长得好看', '怎么出名'], ans: 0, exp: '爱人如己，重德不重貌'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("570-wen-yu-kong", "572-fan-shi-ren")
    out = out.replace("yaoyue571", "yaoyue573")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
