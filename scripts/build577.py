#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build577: 以 576 为骨架，按行号替换文字生成第 577 课
《弟子规·泛爱众》第六段：凡取与，贵分晓。与宜多，取宜少。将加人，先问己。己不欲，即速已。
只换文字，不动任何 HTML 标签；生成后校验行数与标签计数必须与 576 全等。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/576-yang-ren-e/index.html"
DST_DIR = f"{ROOT}/lessons/577-qu-yu-fen-xiao"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第三十七课，泛爱众第六段。原文：「凡取与，贵分晓。与宜多，取宜少。'
        '将加人，先问己。己不欲，即速已。」前两句讲拿和给要清清楚楚，给别人宁可多些，'
        '拿别人的宁可少些；后两句讲要把什么加到别人身上，先问自己愿不愿意，自己不愿意就赶紧停。'
        '合起来：取与分明，将心比心。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("凡","fán"),("取","qǔ"),("与","yǔ")]) + "，" + _r([("贵","guì"),("分","fēn"),("晓","xiǎo")]) + "。", True)
 + _p(_r([("与","yǔ"),("宜","yí"),("多","duō")]) + "，" + _r([("取","qǔ"),("宜","yí"),("少","shǎo")]) + "。")
 + _p(_r([("将","jiāng"),("加","jiā"),("人","rén")]) + "，" + _r([("先","xiān"),("问","wèn"),("己","jǐ")]) + "。")
 + _p(_r([("己","jǐ"),("不","bù"),("欲","yù")]) + "，" + _r([("即","jí"),("速","sù"),("已","yǐ")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="凡取与，贵分晓；己不欲，即速已 · 弟子规课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第三十七课：拿和给要清清楚楚，给别人多、拿别人少；不愿人那样待你，就别那样待人。泛爱众第六段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/577-qu-yu-fen-xiao/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/577-qu-yu-fen-xiao/index.html" rel="canonical"/>',
 12: '<title>泛爱众 · 凡取与贵分晓，己不欲即速已 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">贵分晓</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》泛爱众第六段：凡取与，贵分晓</p>'
      '<p class="cover-desc">拿人家的、给人的，都要清清楚楚；给人宁可多些，拿人宁可少些。'
      '要把什么加到别人身上，先问问自己愿不愿意，不愿意就赶紧停下。'
      '一句话：取与分明，将心比心。</p><div class="cover-seal">与</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 泛爱众第六段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>凡是拿人家的和给人的，最要紧的是清清楚楚；给人家宁可多给些，拿人家的宁可少拿些。'
      '要把什么加到别人身上，先问问自己愿不愿意；自己不愿意的，就赶紧停下。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「取」是拿、得到；「与」是给人家；「贵」是最要紧；「分晓」是清楚明白；'
      '「宜」读 yí，是应该、宜于；「加人」是加到别人身上，让人做、施加于人；'
      '「欲」是想要、愿意；「即速已」是赶紧停，「已」是停止。这是《弟子规》第四门「泛爱众」的第六段。'
      '上一段讲嘴上的分寸，这一段讲手上和心上的分寸：东西上取与分明，事情上将心比心——'
      '一句话，取与分明，将心比心。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>凡取与，贵分晓；与宜多，取宜少；将加人，先问己；己不欲，即速已。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 取与分明，将心比心</h2>'
      '<p style="margin:0"><strong>先说「东西上」</strong><br/>'
      '① <strong>拿多少、给多少，说清楚</strong><br/>'
      '② <strong>给的多一点，拿的少一点</strong><br/><br/>'
      '<strong>一句话：账要明，手要松。</strong></p>'
      '<p><strong>再说「事情上」</strong><br/>'
      '① <strong>要别人做的，自己先试一遍</strong><br/>'
      '② <strong>自己受不了的，别往人身上加</strong><br/><br/>'
      '<strong>一句话：先想自己，再想别人。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「物」</strong><br/>'
      '② <strong>后两句讲「心」</strong><br/><br/>'
      '<strong>一句话：物上分明，心上公道。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>凡取与，贵分晓；与宜多，取宜少</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>取：拿、得到；与：给人家</strong><br/>'
      '② <strong>分晓：清楚明白；宜 yí：应该</strong><br/><br/>'
      '<strong>一句话：拿和给，要说明白。</strong></p>'
      '<p><strong>凡取与，贵分晓</strong><br/>'
      '① <strong>借了多久、还多少，一句话说清</strong><br/>'
      '② <strong>含含糊糊最伤感情，账清才长久</strong><br/><br/>'
      '<strong>一句话：先明后不争。</strong></p>'
      '<p><strong>与宜多，取宜少</strong><br/>'
      '① <strong>分东西，自己拿小的那份</strong><br/>'
      '② <strong>让人一分，攒下一分人缘</strong><br/><br/>'
      '<strong>一句话：宁可自己少点。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>将加人，先问己；己不欲，即速已</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>加人：加到别人身上，让人做</strong><br/>'
      '② <strong>欲：想要、愿意；已：停止</strong><br/><br/>'
      '<strong>一句话：先拿自己试一遍。</strong></p>'
      '<p><strong>将加人，先问己</strong><br/>'
      '① <strong>想让人帮你跑腿，先想你愿不愿意跑</strong><br/>'
      '② <strong>想开个玩笑，先想这玩笑开在你身上好不好受</strong><br/><br/>'
      '<strong>一句话：先当一回别人。</strong></p>'
      '<p><strong>己不欲，即速已</strong><br/>'
      '① <strong>自己都嫌难受的事，别推给别人</strong><br/>'
      '② <strong>话到嘴边先停一停，停得住才是本事</strong><br/><br/>'
      '<strong>一句话：不愿受，就别加。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 一取一与，一己一人</h2>'
      '<p style="margin:0"><strong>前两句讲「物上的公道」</strong><br/>'
      '① <strong>账清：谁的谁的，说明白</strong><br/>'
      '② <strong>手松：给的比拿的多一点</strong><br/><br/>'
      '<strong>一句话：不占人便宜。</strong></p>'
      '<p><strong>后两句讲「心上的公道」</strong><br/>'
      '① <strong>先问己：换我受不受得了</strong><br/>'
      '② <strong>即速已：受不了就别说别做</strong><br/><br/>'
      '<strong>一句话：不给人添苦。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>借同学的东西，说清啥时候还，还得干净</strong><br/>'
      '② <strong>分东西自己拿小的；想损人一句，先咽下去</strong><br/><br/>'
      '<strong>一句话：物清，心善。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两两成对</h2>'
      '<p style="margin:0"><strong>前两句：东西怎么处</strong><br/>'
      '① <strong>凡取与，贵分晓——拿给要清楚</strong><br/>'
      '② <strong>与宜多，取宜少——给多拿少</strong><br/><br/>'
      '<strong>一句话：明。</strong></p>'
      '<p><strong>后两句：事情怎么办</strong><br/>'
      '① <strong>将加人，先问己——先拿自己试</strong><br/>'
      '② <strong>己不欲，即速已——不愿就停手</strong><br/><br/>'
      '<strong>一句话：恕。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>账要清，手要松</strong><br/>'
      '② <strong>先想己，再及人</strong><br/><br/>'
      '<strong>一句话：明明白白，将心比心。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 取与分明，将心比心</h2>'
      '<p>四句话，两层意思——</p>'
      '<h3>"凡取与，贵分晓。与宜多，取宜少。将加人，先问己。己不欲，即速已。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>拿和给要清楚，给的比拿的多；'
      '要加到别人身上的，先问自己愿不愿意。</p><p>📖 分明恕道</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>账清，是敬人；让利，是厚道；'
      '先问己，是把别人当自己——一句话，己所不欲，勿施于人。</p><p>💡 恕</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>取与分明，将心比心；'
      '给多拿少，不愿不加。</p><p>🌱 将心比心</p>'),
 72: '<p>这是「弟子规课堂」第三十七课：泛爱众第六段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 借东西、分东西怎么算「分晓」？</h3>'
       '<p><strong>说清三样：什么时候还、还多少、坏了怎么办。</strong><br/><br/>'
       '① <strong>开头说一句，省得后来红脸</strong><br/>'
       '② <strong>还得干净、还得齐整，比说什么都管用</strong><br/>'
       '③ <strong>记法：先说清，后不争。</strong></p>'
       '<h3>❓ 「与宜多」是不是吃亏？</h3>'
       '<p><strong>让人一分，攒下一分人缘。</strong><br/><br/>'
       '① <strong>眼前少了一点，往后有人愿意帮你</strong><br/>'
       '② <strong>处处占先的人，最后没人跟他打交道</strong><br/>'
       '③ <strong>记法：小处让人，大处有人。</strong></p>'
       '<h3>❓ 自己不愿意的事，就一定不做吗？</h3>'
       '<p><strong>分清「不愿做」和「不该做」。</strong><br/><br/>'
       '① <strong>该做的（值日、功课、让座），不愿意也得做</strong><br/>'
       '② <strong>这四句管的是「加到别人身上」的事，不是逃避责任</strong><br/>'
       '③ <strong>记法：责己从严，待人不强。</strong></p>'
       '<h3>❓ 别人硬要我干我不愿的事，怎么办？</h3>'
       '<p><strong>说清理由，不硬顶也不硬扛。</strong><br/><br/>'
       '① <strong>先说「这事我为难，因为……」</strong><br/>'
       '② <strong>再给个能做的替代办法</strong><br/>'
       '③ <strong>记法：不忍着，也不吵。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 账要清</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>借东西说清什么时候还，还得干净齐整</strong>；'
       '<strong>这就是「凡取与，贵分晓」</strong>。</p><p>💡 多给一点</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>分东西自己拿小的那份，别人缺了先给他</strong>；'
       '<strong>这就是「与宜多，取宜少」</strong>。</p><p>🌱 先想自己</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>想开玩笑、想推事给人之前，先想自己被这样待是什么滋味</strong>；'
       '<strong>这就是「己不欲，即速已」</strong><br/><br/>'
       '<strong>本课的落点：取与分明，将心比心。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲泛爱众第六段，账要清，心要公。记牢：<strong>取与分明</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">凡取与，贵分晓。与宜多，取宜少。'
       '将加人，先问己。己不欲，即速已。</p><p>回顾本课要点:</p>'
       '<p>泛爱众第六段 · 物上分明，心上公道。<strong>取与分明</strong>。</p>'
       '<p>凡取与，贵分晓 · 拿给要清楚。<strong>先说清</strong>。</p>'
       '<p>与宜多，取宜少 · 给多拿少。<strong>宁可自己少</strong>。</p>'
       '<p>将加人，先问己 · 先拿自己试。<strong>先当别人</strong>。</p>'
       '<p>己不欲，即速已 · 不愿就别加。<strong>停得住</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>泛爱众第六段；上一段讲嘴上分寸，'
       '这一段讲东西上和事情上的分寸。</p>'
       '<div class="ds-quote">'),

 111: '<p>凡取与，贵分晓。与宜多，取宜少。将加人，先问己。己不欲，即速已。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「取」「与」「分晓」「已」怎么讲。'
       '② 今天把一件借的东西还干净。'
       '③ 想一想：你被人硬加过什么事，什么滋味。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>凡取与，贵分晓；与宜多，取宜少；'
       '将加人，先问己；己不欲，即速已。</strong></p></div>'),

 119: '            "凡取与，贵分晓。与宜多，取宜少。将加人，先问己。己不欲，即速已。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '577-qu-yu-fen-xiao';",

 59: '<!-- 4. 凡取与贵分晓·与宜多取宜少 -->',
 61: '<!-- 5. 将加人先问己·己不欲即速已 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「凡取与」的「与」是什么意思？', opts: ['给人家', '和、跟', '参与'], ans: 0, exp: '与是给人家'},",
 "  {q: '2. 「贵分晓」的「分晓」是什么意思？', opts: ['清楚明白', '天亮', '分开生活'], ans: 0, exp: '分晓是清楚明白'},",
 "  {q: '3. 「与宜多」的「宜」怎么读、什么意思？', opts: ['yí，应该、宜于', 'yì，友谊', 'yǐ，已经'], ans: 0, exp: '宜读 yí，是应该'},",
 "  {q: '4. 「即速已」的「已」是什么意思？', opts: ['停止、罢手', '已经', '自己'], ans: 0, exp: '已是停止'},",
 "  {q: '5. 「将加人」的「加人」是什么意思？', opts: ['加到别人身上，让人做', '增加人数', '参加人家'], ans: 0, exp: '加人是加到别人身上'},",
 "  {q: '6. 「先问己」的「问己」是什么意思？', opts: ['先问问自己', '先问自己的名字', '问过自己家人'], ans: 0, exp: '先问问自己'},",
 "  {q: '7. 「己不欲」的「欲」是什么意思？', opts: ['想要、愿意', '洗澡', '欲望太多'], ans: 0, exp: '欲是想要、愿意'},",
 "  {q: '8. 「与宜多，取宜少」是说什么？', opts: ['给别人宁可多，拿别人宁可少', '给得越少越好', '要拿就多拿'], ans: 0, exp: '给多拿少'},",
 "  {q: '9. 「己不欲，即速已」是说什么？', opts: ['自己不愿意的，就赶紧停下，别加给别人', '自己不愿就别干', '愿不愿意都得干'], ans: 0, exp: '己所不欲，勿施于人'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['取与分明、将心比心：账要清，给多拿少，先问自己', '怎么借到东西', '怎么不被占便宜'], ans: 0, exp: '取与分明，将心比心'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("576-yang-ren-e", "577-qu-yu-fen-xiao")
    out = out.replace("yaoyue577", "yaoyue578")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
