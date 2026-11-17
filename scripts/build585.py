#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build585: 以 584 为骨架，按行号替换文字生成第 585 课
《弟子规·余力学文》第四段：房室清，墙壁净。几案洁，笔砚正。墨磨偏，心不端。字不敬，心先病。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/584-kuan-wei-xian/index.html"
DST_DIR = f"{ROOT}/lessons/585-fang-shi-qing"
DST = f"{DST_DIR}/index.html"

DESC = ('《弟子规》第四十五课，余力学文第四段。原文：「房室清，墙壁净。几案洁，笔砚正。'
        '墨磨偏，心不端。字不敬，心先病。」前两句讲房间、墙壁、书桌、笔砚都收拾得干净端正；'
        '后两句讲磨墨磨歪了，是心没在这儿；字写得潦草不认真，是心先出了毛病。'
        '合起来：地方干净，字才端正，心先要正。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("房","fáng"),("室","shì"),("清","qīng")]) + "，" + _r([("墙","qiáng"),("壁","bì"),("净","jìng")]) + "。", True)
 + _p(_r([("几","jī"),("案","àn"),("洁","jié")]) + "，" + _r([("笔","bǐ"),("砚","yàn"),("正","zhèng")]) + "。")
 + _p(_r([("墨","mò"),("磨","mó"),("偏","piān")]) + "，" + _r([("心","xīn"),("不","bù"),("端","duān")]) + "。")
 + _p(_r([("字","zì"),("不","bù"),("敬","jìng")]) + "，" + _r([("心","xīn"),("先","xiān"),("病","bìng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="房室清墙壁净，字不敬心先病 · 余力学文课堂" property="og:title"/>',
 8: '<meta content="《弟子规》第四十五课：房间清、书桌净、笔砚正；磨墨磨偏是心不在，字写潦草是心先病。字如其心。余力学文第四段。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/585-fang-shi-qing/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/585-fang-shi-qing/index.html" rel="canonical"/>',
 12: '<title>余力学文 · 房室清墙壁净 ·《弟子规》国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">心镜</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《弟子规》余力学文第四段：房室清，墙壁净</p>'
      '<p class="cover-desc">房间干净、书桌整齐、笔砚摆正——地方清清爽爽，心才定得下来。'
      '磨墨磨歪了，是心没在这儿；字写得糊里糊涂，是心先出了毛病。'
      '一句话：字是心的镜子。</p><div class="cover-seal">正</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 余力学文第四段</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>屋子要清爽，墙壁要干净；书桌要洁净，笔和砚台要摆端正。'
      '磨墨都磨歪了，说明心没放在这件事上；字写得潦草不认真，说明心先有了毛病。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「房室」是屋子、房间；「清」「净」「洁」都是干净；'
      '「几」读 jī，是小桌子，「几案」就是书桌；「砚」读 yàn，是磨墨的砚台；'
      '「正」是摆正；「偏」是歪了、偏了；「端」是端正；'
      '「敬」是认真、恭敬；「病」在这里不是生病，是出了毛病。'
      '这一段从读书、用功、问学，讲到读书的地方和写字——外面收拾干净，里面才静得下来。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>房室清，墙壁净；几案洁，笔砚正；墨磨偏，心不端；字不敬，心先病。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 外面干净，里面才静</h2>'
      '<p style="margin:0"><strong>头一件：收拾地方</strong><br/>'
      '① <strong>屋子净、桌子洁、笔砚正</strong><br/>'
      '② <strong>地方清爽，心就少乱</strong><br/><br/>'
      '<strong>一句话：桌净，心才定。</strong></p>'
      '<p><strong>第二件：看心</strong><br/>'
      '① <strong>墨磨偏了，是心跑了</strong><br/>'
      '② <strong>字写潦草，是心先乱</strong><br/><br/>'
      '<strong>一句话：字里见心。</strong></p>'
      '<p><strong>一句话看全段</strong><br/>'
      '① <strong>前两句讲「地方」</strong><br/>'
      '② <strong>后两句讲「心」</strong><br/><br/>'
      '<strong>一句话：地方清，心要正。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>房室清，墙壁净；几案洁，笔砚正</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>几案：书桌；几 jī，小桌子</strong><br/>'
      '② <strong>砚 yàn：磨墨的砚台；正：摆端正</strong><br/><br/>'
      '<strong>一句话：地方要有样子。</strong></p>'
      '<p><strong>房室清，墙壁净</strong><br/>'
      '① <strong>屋子不乱堆，墙上不乱贴</strong><br/>'
      '② <strong>眼睛看见的地方干净，脑子也清</strong><br/><br/>'
      '<strong>一句话：眼净，心不烦。</strong></p>'
      '<p><strong>几案洁，笔砚正</strong><br/>'
      '① <strong>桌面只留要用的书本文具</strong><br/>'
      '② <strong>笔归笔、本归本，一伸手就拿到</strong><br/><br/>'
      '<strong>一句话：摆得正，坐得住。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>墨磨偏，心不端；字不敬，心先病</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>偏：歪了；端：端正</strong><br/>'
      '② <strong>敬：认真恭敬；病：出毛病，不是生病</strong><br/><br/>'
      '<strong>一句话：小处见心。</strong></p>'
      '<p><strong>墨磨偏，心不端</strong><br/>'
      '① <strong>磨墨该慢慢转圈，他歪着乱蹭</strong><br/>'
      '② <strong>手在磨墨，心已经跑到别处</strong><br/><br/>'
      '<strong>一句话：手乱，是心乱。</strong></p>'
      '<p><strong>字不敬，心先病</strong><br/>'
      '① <strong>字糊成一片，连自己都认不出</strong><br/>'
      '② <strong>不是手笨，是心里先不当回事</strong><br/><br/>'
      '<strong>一句话：字见态度。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>四句合看 · 从桌子到心</h2>'
      '<p style="margin:0"><strong>先把桌面清出来</strong><br/>'
      '① <strong>每天写完作业，桌面归零</strong><br/>'
      '② <strong>书只留要用的那几本</strong><br/><br/>'
      '<strong>一句话：清一次，静一堂。</strong></p>'
      '<p><strong>再把字写端正</strong><br/>'
      '① <strong>一笔一笔写完，不糊不连</strong><br/>'
      '② <strong>写慢了不要紧，写清楚才算数</strong><br/><br/>'
      '<strong>一句话：字正，心也正。</strong></p>'
      '<p><strong>今天怎么做</strong><br/>'
      '① <strong>今天先收拾自己的书桌，再写作业</strong><br/>'
      '② <strong>写字前坐正、本子摆正</strong><br/><br/>'
      '<strong>一句话：先整地方，后整心。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐句解读 · 四句两层</h2>'
      '<p style="margin:0"><strong>前两句：地方</strong><br/>'
      '① <strong>房室清，墙壁净——屋子干净</strong><br/>'
      '② <strong>几案洁，笔砚正——桌上整齐</strong><br/><br/>'
      '<strong>一句话：外。</strong></p>'
      '<p><strong>后两句：心</strong><br/>'
      '① <strong>墨磨偏，心不端——心没在</strong><br/>'
      '② <strong>字不敬，心先病——心先乱</strong><br/><br/>'
      '<strong>一句话：内。</strong></p>'
      '<p><strong>一句口诀记住</strong><br/>'
      '① <strong>桌上干净，笔砚摆正</strong><br/>'
      '② <strong>字要清楚，心要端正</strong><br/><br/>'
      '<strong>一句话：内外一起整。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 字如其心</h2>'
      '<p>四句话，两层——</p>'
      '<h3>"房室清，墙壁净。几案洁，笔砚正。墨磨偏，心不端。字不敬，心先病。"</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>屋子净、桌子洁、笔砚正，'
      '字要写得清楚。</p><p>📖 地方</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>地方乱是心乱的样子，'
      '字潦草是心不在的样子。</p><p>💡 心镜</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>字如其心；'
      '先把心和桌子都收拾干净。</p><p>🌱 端正</p>'),
 72: '<p>这是「余力学文课堂」第四十五课：余力学文第四段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 桌子乱一点，就学不好吗？</h3>'
       '<p><strong>乱不是罪，乱会分心。</strong><br/><br/>'
       '① <strong>东西太多，眼睛总往别处跑</strong><br/>'
       '② <strong>只做三样就够：桌面留空、书只放要用的、用完归位</strong><br/>'
       '③ <strong>记法：不是洁癖，是给心让地方。</strong></p>'
       '<h3>❓ 现在没墨可磨，「墨磨偏」怎么讲？</h3>'
       '<p><strong>换成今天的事，是一样的。</strong><br/><br/>'
       '① <strong>笔尖歪了不修、本子卷边不管</strong><br/>'
       '② <strong>写字手在动，脑子在想别的</strong><br/>'
       '③ <strong>记法：手上的小事糊过去，就是「磨偏」。</strong></p>'
       '<h3>❓ 字写得不好看，算「心不敬」吗？</h3>'
       '<p><strong>不看好看，看认不认真。</strong><br/><br/>'
       '① <strong>一笔一笔写完、不糊不连，就是敬</strong><br/>'
       '② <strong>赶速度糊成一片、自己都不认得，就是不敬</strong><br/>'
       '③ <strong>记法：字是给自己和别人的交代。</strong></p>'
       '<h3>❓ 收拾房间是大人的事吗？</h3>'
       '<p><strong>先管自己那一张桌。</strong><br/><br/>'
       '① <strong>整间房不必你包，你的桌面归你</strong><br/>'
       '② <strong>每天收一次，比一周大扫除强</strong><br/>'
       '③ <strong>记法：自己的地方自己清。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 桌面归零</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>写完作业把桌面收干净，只留明天要用的</strong>；'
       '<strong>这就是「几案洁」</strong>。</p><p>💡 写字先坐正</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>本子摆正、笔握稳，一笔一笔写</strong>；'
       '<strong>这就是「字不敬，心先病」的反面</strong>。</p><p>🌱 回头看一眼</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>写完翻回去看：有没有糊、有没有连</strong>；'
       '<strong>这就是「字如其心」</strong><br/><br/>'
       '<strong>本课的落点：端正。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天讲两件事：地方要清，字要端正。记牢：<strong>字如其心</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">房室清，墙壁净。几案洁，笔砚正。'
       '墨磨偏，心不端。字不敬，心先病。</p><p>回顾本课要点:</p>'
       '<p>余力学文第四段 · 外整地方，内正其心。<strong>端正</strong>。</p>'
       '<p>房室清，墙壁净 · 屋子要清爽。<strong>眼净心不烦</strong>。</p>'
       '<p>几案洁，笔砚正 · 桌面整齐。<strong>摆得正坐得住</strong>。</p>'
       '<p>墨磨偏，心不端 · 手乱是心乱。<strong>小处见心</strong>。</p>'
       '<p>字不敬，心先病 · 字见态度。<strong>字如其心</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>余力学文第四段；上一段讲用功问学，'
       '这一段讲读书的环境和写字的心。</p>'
       '<div class="ds-quote">'),

 111: '<p>房室清，墙壁净。几案洁，笔砚正。墨磨偏，心不端。字不敬，心先病。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「几案」「砚」「端」「病」怎么讲。'
       '② 今天把书桌收拾干净，再写一页字。'
       '③ 想一想：你的字，能看出你当时的心情吗。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>房室清，墙壁净；几案洁，笔砚正；'
       '墨磨偏，心不端；字不敬，心先病。</strong></p></div>'),

 119: '            "房室清，墙壁净。几案洁，笔砚正。墨磨偏，心不端。字不敬，心先病。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '585-fang-shi-qing';",

 59: '<!-- 4. 房室清墙壁净·几案洁笔砚正 -->',
 61: '<!-- 5. 墨磨偏心不端·字不敬心先病 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「房室清」的「清」是什么意思？', opts: ['干净清爽', '清水', '清楚'], ans: 0, exp: '清是干净'},",
 "  {q: '2. 「几案」是什么？', opts: ['书桌、小桌子', '几个案子', '书架'], ans: 0, exp: '几案是书桌'},",
 "  {q: '3. 「几案」的「几」怎么读？', opts: ['jī', 'jǐ', 'jì'], ans: 0, exp: '几读 jī，小桌子'},",
 "  {q: '4. 「笔砚正」的「正」是什么意思？', opts: ['摆端正', '正好', '正月'], ans: 0, exp: '正是摆端正'},",
 "  {q: '5. 「砚」是什么东西？', opts: ['磨墨的砚台', '写字的纸', '装笔的盒子'], ans: 0, exp: '砚是砚台'},",
 "  {q: '6. 「墨磨偏」讲的是什么？', opts: ['磨墨磨歪了，心没在这儿', '墨太少了', '砚台偏了'], ans: 0, exp: '小处见心'},",
 "  {q: '7. 「心不端」的「端」是什么意思？', opts: ['端正', '端点', '端着'], ans: 0, exp: '端是端正'},",
 "  {q: '8. 「字不敬」的「敬」是什么意思？', opts: ['认真、恭敬', '敬礼', '尊敬长辈'], ans: 0, exp: '敬是认真'},",
 "  {q: '9. 「心先病」的「病」是什么意思？', opts: ['心先出了毛病', '身体生病', '病了一场'], ans: 0, exp: '病是出毛病'},",
 "  {q: '10. 这四句总的讲什么？', opts: ['地方要清、字要端正，字如其心', '屋子越大越好', '字要写得快'], ans: 0, exp: '外整地方内正心'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("584-kuan-wei-xian", "585-fang-shi-qing")
    out = out.replace("yaoyue584", "yaoyue585")
    out = out.replace("第四十四课", "第四十五课")
    out = out.replace("余力学文第三段", "余力学文第四段")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
