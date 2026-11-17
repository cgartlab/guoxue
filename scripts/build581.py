#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build581: 以 580 为骨架，按行号替换文字生成第 581 课
《弟子规·亲仁》第二段：能亲仁，无限好。德日进，过日少。不亲仁，无限害。小人进，百事坏。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/580-tong-shi-ren/index.html"
DST_DIR = f"{ROOT}/lessons/581-neng-qin-ren"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十一课，亲仁第二段。原文：「能亲仁，无限好。德日进，过日少。'
        '不亲仁，无限害。小人进，百事坏。」前两句讲肯跟仁者走近，好处说不完：德行天天长，'
        '过错天天少；后两句讲不肯亲近仁者，坏处也说不完：小人凑上来，件件事都办坏。'
        '合起来：跟着谁，慢慢就成了谁。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("能","néng"),("亲","qīn"),("仁","rén")]) + "，" + _r([("无","wú"),("限","xiàn"),("好","hǎo")]) + "。", True)
 + _p(_r([("德","dé"),("日","rì"),("进","jìn")]) + "，" + _r([("过","guò"),("日","rì"),("少","shǎo")]) + "。")
 + _p(_r([("不","bù"),("亲","qīn"),("仁","rén")]) + "，" + _r([("无","wú"),("限","xiàn"),("害","hài")]) + "。")
 + _p(_r([("小","xiǎo"),("人","rén"),("进","jìn")]) + "，" + _r([("百","bǎi"),("事","shì"),("坏","huài")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="能亲仁无限好，不亲仁无限害 · 亲仁课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十一课：跟仁者走近，德行天天长、过错天天少；不肯亲近，小人凑上来，事事办坏。亲仁第二段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/581-neng-qin-ren/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/581-neng-qin-ren/index.html" rel="canonical"/>',
 12: '<title>亲仁 · 能亲仁无限好，不亲仁无限害 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">亲仁则进</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》亲仁第二段：能亲仁，无限好</p>'
      '<p class="cover-desc">肯跟仁者走近，好处说不完：德行天天长，过错天天少。'
      '不肯亲近仁者，坏处也说不完：小人凑到身边，件件事都办坏。'
      '一句话：跟着谁，慢慢就成了谁。</p><div class="cover-seal">进</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 亲仁第二段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>肯亲近有仁德的人，好处没有穷尽：德行一天天长进，过错一天天减少。'
      '不肯亲近有仁德的人，害处也没有穷尽：小人一个个凑上来，什么好事都办坏。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「亲」是亲近、靠近；「无限」是没有尽头；「德」是德行；「日进」是天天长进；'
      '「过」是过错；「日少」是天天减少；「小人」是只顾私利、不讲道理的人；'
      '「进」是凑上来、往里钻；「百事坏」是件件事都办坏。'
      '这是《弟子规》第五门「亲仁」的第二段。上一段讲认得出仁者，这一段讲认出来以后怎么了：'
      '肯亲近就长进，不肯亲近就走下坡——一句话，跟着谁，慢慢就成了谁。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>能亲仁，无限好；德日进，过日少；不亲仁，无限害；小人进，百事坏。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 两条路，两个结果</h2>'
      '<p style="margin:0"><strong>第一条路：亲仁</strong><br/>'
      '① <strong>跟好人走近，学的是他的样子</strong><br/>'
      '② <strong>德天天长，过天天少</strong><br/><br/>'
      '<strong>一句话：越走越亮。</strong></p>'
      '<p><strong>第二条路：不亲仁</strong><br/>'
      '① <strong>身边没人扶一把，小人就钻空子</strong><br/>'
      '② <strong>一件件小事办歪，最后全坏</strong><br/><br/>'
      '<strong>一句话：越走越浑。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「亲」的好处</strong><br/>'
      '② <strong>后两句讲「不亲」的坏处</strong><br/><br/>'
      '<strong>一句话：择友就是择路。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>能亲仁，无限好；德日进，过日少</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>亲：亲近、靠近；无限：没有尽头</strong><br/>'
      '② <strong>德：德行；日进：天天长进；过：过错</strong><br/><br/>'
      '<strong>一句话：跟对了人，天天在长。</strong></p>'
      '<p><strong>能亲仁，无限好</strong><br/>'
      '① <strong>不用等人教，看人家怎么做就学会了</strong><br/>'
      '② <strong>遇事有人点一句，少走很多弯路</strong><br/><br/>'
      '<strong>一句话：好处不在眼前，在后面。</strong></p>'
      '<p><strong>德日进，过日少</strong><br/>'
      '① <strong>长进是一天一点，看不出来，攒出来</strong><br/>'
      '② <strong>过错少了，不是没人犯，是犯得少了</strong><br/><br/>'
      '<strong>一句话：慢慢变好，才靠得住。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>不亲仁，无限害；小人进，百事坏</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>小人：只顾私利、不讲道理的人</strong><br/>'
      '② <strong>进：凑上来、往里钻；百事坏：件件办坏</strong><br/><br/>'
      '<strong>一句话：不是没人教，是教的人不对。</strong></p>'
      '<p><strong>不亲仁，无限害</strong><br/>'
      '① <strong>身边没人拉你，往下滑没人拦</strong><br/>'
      '② <strong>坏习惯一旦上身，改起来费十年</strong><br/><br/>'
      '<strong>一句话：没人扶，才最险。</strong></p>'
      '<p><strong>小人进，百事坏</strong><br/>'
      '① <strong>他先给你甜头，再拉你下水</strong><br/>'
      '② <strong>你替他担了事，他还笑你傻</strong><br/><br/>'
      '<strong>一句话：交错了人，事就散了。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 一边往上长，一边往下滑</h2>'
      '<p style="margin:0"><strong>「亲仁」这条道</strong><br/>'
      '① <strong>学的都是正经本事</strong><br/>'
      '② <strong>日子越过越清亮</strong><br/><br/>'
      '<strong>一句话：往上长。</strong></p>'
      '<p><strong>「不亲仁」这条道</strong><br/>'
      '① <strong>学的都是偷懒、占便宜、耍滑</strong><br/>'
      '② <strong>日子越过越乱</strong><br/><br/>'
      '<strong>一句话：往下滑。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>身边挑一个「做得正」的人，多跟他一处</strong><br/>'
      '② <strong>谁总教你占便宜、说瞎话，慢慢离远点</strong><br/><br/>'
      '<strong>一句话：近正人，远滑人。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两正两反</h2>'
      '<p style="margin:0"><strong>前两句：正面</strong><br/>'
      '① <strong>能亲仁，无限好——跟对了人</strong><br/>'
      '② <strong>德日进，过日少——天天在长</strong><br/><br/>'
      '<strong>一句话：益。</strong></p>'
      '<p><strong>后两句：反面</strong><br/>'
      '① <strong>不亲仁，无限害——没人扶</strong><br/>'
      '② <strong>小人进，百事坏——事全歪</strong><br/><br/>'
      '<strong>一句话：损。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>亲仁一天，长一分</strong><br/>'
      '② <strong>远仁一天，退一分</strong><br/><br/>'
      '<strong>一句话：跟着谁，就成了谁。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 跟着谁，就成了谁</h2>'
      '<p>四句话，两条路——</p>'
      '<h3>"能亲仁，无限好。德日进，过日少。不亲仁，无限害。小人进，百事坏。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>亲近仁者好处多，德行天天长、过错天天少；'
      '不亲近就害处多，小人凑上来事事办坏。</p><p>📖 损益</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>人是被身边人带出来的；'
      '亲近谁，天天看谁，慢慢就像谁——所以不用急着立志，先把身边的人选对。</p><p>💡 择友</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>跟着谁，就成了谁；'
      '择友就是择路。</p><p>🌱 亲仁则进</p>'),
 72: '<p>这是「亲仁课堂」第四十一课：亲仁第二段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「无限好」是不是说得太夸张？</h3>'
       '<p><strong>不是夸张，是「说不完」。</strong><br/><br/>'
       '① <strong>好处一天一点，攒起来没有尽头</strong><br/>'
       '② <strong>急的是一时的便宜，好的是长久的底子</strong><br/>'
       '③ <strong>记法：不求马上见效，求天天有点。</strong></p>'
       '<h3>❓ 「亲仁」是要跟人家天天待着吗？</h3>'
       '<p><strong>是近，不是黏。</strong><br/><br/>'
       '① <strong>多听、多看、多问，比天天凑一块强</strong><br/>'
       '② <strong>书里也有仁者，读他的书就是亲他</strong><br/>'
       '③ <strong>记法：学他的样，比贴着他更有用。</strong></p>'
       '<h3>❓ 「小人进」是别人故意来害我吗？</h3>'
       '<p><strong>多半不是害你，是拉你。</strong><br/><br/>'
       '① <strong>先给你甜头：抄作业、说人坏话、一起去玩</strong><br/>'
       '② <strong>再让你担事：替你瞒、替你扛</strong><br/>'
       '③ <strong>记法：给甜头的朋友，先想三分。</strong></p>'
       '<h3>❓ 朋友不多，找不到「仁者」怎么办？</h3>'
       '<p><strong>一个人身上有一处正，就学那一处。</strong><br/><br/>'
       '① <strong>没人十全十美，别求完人</strong><br/>'
       '② <strong>先自己做一个「近仁」的人，好人自会靠近</strong><br/>'
       '③ <strong>记法：自己正了，圈子就正了。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 挑人</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>身边挑一个做得正的人，多跟他一处</strong>；'
       '<strong>这就是「能亲仁」</strong>。</p><p>💡 慢离</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>总教你占便宜、说瞎话的人，慢慢离远点</strong>；'
       '<strong>这就是「小人进，百事坏」</strong>。</p><p>🌱 天天一点</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>每天改一个小毛病，就是「过日少」</strong>；'
       '<strong>每天学人一个好样，就是「德日进」</strong><br/><br/>'
       '<strong>本课的落点：跟着谁，就成了谁。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲亲仁第二段，一边长，一边滑。记牢：<strong>择友就是择路</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">能亲仁，无限好。德日进，过日少。'
       '不亲仁，无限害。小人进，百事坏。</p><p>回顾本课要点:</p>'
       '<p>亲仁第二段 · 两条路，两个结果。<strong>择友即择路</strong>。</p>'
       '<p>能亲仁，无限好 · 好处说不完。<strong>越走越亮</strong>。</p>'
       '<p>德日进，过日少 · 一天一点。<strong>慢慢变好</strong>。</p>'
       '<p>不亲仁，无限害 · 没人扶最险。<strong>越走越浑</strong>。</p>'
       '<p>小人进，百事坏 · 交错了人事就散。<strong>先想三分</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>亲仁第二段；上一段讲认人，这一段讲认出来以后怎么走。</p>'
       '<div class="ds-quote">'),

 111: '<p>能亲仁，无限好。德日进，过日少。不亲仁，无限害。小人进，百事坏。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「亲」「日进」「过」「小人」怎么讲。'
       '② 今天找一个人，学他一个好样子。'
       '③ 想一想：谁总教你占便宜，你跟他走得多近。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>能亲仁，无限好；德日进，过日少；'
       '不亲仁，无限害；小人进，百事坏。</strong></p></div>'),

 119: '            "能亲仁，无限好。德日进，过日少。不亲仁，无限害。小人进，百事坏。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '581-neng-qin-ren';",

 59: '<!-- 4. 能亲仁无限好·德日进过日少 -->',
 61: '<!-- 5. 不亲仁无限害·小人进百事坏 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「能亲仁」的「亲」是什么意思？', opts: ['亲近、靠近', '亲人', '亲自'], ans: 0, exp: '亲是亲近'},",
 "  {q: '2. 「无限好」的「无限」是什么意思？', opts: ['没有尽头、说不完', '没有限制', '无线'], ans: 0, exp: '无限是没有尽头'},",
 "  {q: '3. 「德日进」的「日」是什么意思？', opts: ['天天、一天天', '太阳', '日子'], ans: 0, exp: '日是天天的意思'},",
 "  {q: '4. 「过日少」的「过」是什么意思？', opts: ['过错、毛病', '经过', '过分'], ans: 0, exp: '过是过错'},",
 "  {q: '5. 「小人进」的「小人」指什么人？', opts: ['只顾私利、不讲道理的人', '个子小的人', '小孩子'], ans: 0, exp: '小人指不讲道理的坏人'},",
 "  {q: '6. 「小人进」的「进」是什么意思？', opts: ['凑上来、往里钻', '进门', '进步'], ans: 0, exp: '进是凑上来'},",
 "  {q: '7. 「百事坏」是什么意思？', opts: ['件件事都办坏', '一百件事坏了', '事情很多'], ans: 0, exp: '百事坏是件件办坏'},",
 "  {q: '8. 「能亲仁，无限好」是说亲近仁者有什么好处？', opts: ['德行天天长进，过错天天减少', '马上就有好处', '别人会怕你'], ans: 0, exp: '德日进，过日少'},",
 "  {q: '9. 为什么说「不亲仁」害处大？', opts: ['身边没人拉你，小人凑上来把事搅坏', '没人陪你玩', '会被老师罚'], ans: 0, exp: '没人扶最险'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['亲仁就长进，不亲仁就下滑：跟着谁就成了谁', '怎么多交朋友', '怎么让小人走开'], ans: 0, exp: '跟着谁，就成了谁'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("580-tong-shi-ren", "581-neng-qin-ren")
    out = out.replace("yaoyue580", "yaoyue581")
    out = out.replace("第四十课", "第四十一课")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
