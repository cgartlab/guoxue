#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build589: 以 588 为骨架，按行号替换文字生成第 589 课
《笠翁对韵》一东第一段（天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。）
只换文字，不动任何 HTML 标签。行号与 588 完全一致。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/588-li-weng-dui-yun/index.html"
DST_DIR = f"{ROOT}/lessons/589-yi-dong"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》一东第一段。原文：「天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。」'
        '天与地、雨与风、大陆与长空、山花与海树、赤日与苍穹，五组对句；句尾风、空、穹同属东韵，'
        '一口韵到底。学对仗，从一东开始。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("天","tiān"),("对","duì"),("地","dì")]) + "，" + _r([("雨","yǔ"),("对","duì"),("风","fēng")]) + "。", True)
 + _p(_r([("大","dà"),("陆","lù"),("对","duì"),("长","cháng"),("空","kōng")]) + "。")
 + _p(_r([("山","shān"),("花","huā"),("对","duì"),("海","hǎi"),("树","shù")]) + "，")
 + _p(_r([("赤","chì"),("日","rì"),("对","duì"),("苍","cāng"),("穹","qióng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 一东（天对地，雨对风） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》一东第一段：天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。五组对句，句尾风空穹同属东韵。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/589-yi-dong/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/589-yi-dong/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 一东（天对地，雨对风）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">一东</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》上卷第一韵 · 第一段</p>'
      '<p class="cover-desc">全书从这四个字开头：天对地，雨对风。'
      '往下五个对句，句句成双；句尾「风、空、穹」都落在同一个韵里。'
      '一句话：一口韵到底。</p><div class="cover-seal">东</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 一东（第一段）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>天对着地，雨对着风；广阔的大地对辽阔的长空；山上的花对海边的树，红红的太阳对青蓝的天空。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>上卷第一个韵部叫「一东」。「东」是这个韵的名字，不是「东边」：凡古音跟「东」同韵的字都归在这里。'
      '这一段五个对句，句尾「风、空、穹」三个字同属东韵——所以念起来一口韵到底，像唱歌一样顺。'
      '先不必记韵部名称，先把这份「顺」念出来。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>天对地，雨对风；大陆对长空；山花对海树，赤日对苍穹。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话读这一段</h2>'
      '<p style="margin:0"><strong>第一个韵</strong><br/>'
      '① <strong>一东＝上卷第一韵</strong><br/>'
      '② <strong>「东」是韵的名字，不是方向</strong><br/><br/>'
      '<strong>一句话：全书从这儿开头。</strong></p>'
      '<p><strong>五个对句</strong><br/>'
      '① <strong>天地、雨风、大陆长空</strong><br/>'
      '② <strong>山花海树、赤日苍穹</strong><br/><br/>'
      '<strong>一句话：句句成双。</strong></p>'
      '<p><strong>三个韵脚</strong><br/>'
      '① <strong>风、空、穹 落在句尾</strong><br/>'
      '② <strong>三个字同属东韵</strong><br/><br/>'
      '<strong>一句话：一口韵到底。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>天对地，雨对风 · 最大的两对</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>对 duì：相对、成双</strong><br/>'
      '② <strong>地 dì；风 fēng</strong><br/><br/>'
      '<strong>一句话：一个字对一个字。</strong></p>'
      '<p><strong>天对地</strong><br/>'
      '① <strong>一个在上，一个在下</strong><br/>'
      '② <strong>世界最大的一对</strong><br/><br/>'
      '<strong>一句话：先说天地。</strong></p>'
      '<p><strong>雨对风</strong><br/>'
      '① <strong>雨看得见，风看不见</strong><br/>'
      '② <strong>一实一虚，正好成对</strong><br/><br/>'
      '<strong>一句话：再说风雨。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>大陆对长空 · 山花对海树，赤日对苍穹</h2>'
      '<p style="margin:0"><strong>大陆 对 长空</strong><br/>'
      '① <strong>大陆：广阔的大地</strong><br/>'
      '② <strong>长空：辽阔的天空</strong><br/><br/>'
      '<strong>一句话：地面对天空。</strong></p>'
      '<p><strong>山花 对 海树</strong><br/>'
      '① <strong>山对海，一山一海</strong><br/>'
      '② <strong>花对树，一花一树</strong><br/><br/>'
      '<strong>一句话：山上的花对海边的树。</strong></p>'
      '<p><strong>赤日 对 苍穹</strong><br/>'
      '① <strong>赤 chì＝红；苍穹＝青蓝的天</strong><br/>'
      '② <strong>红日对青天，颜色对颜色</strong><br/><br/>'
      '<strong>一句话：一句一幅景。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三块合看 · 一东为什么念着顺</h2>'
      '<p style="margin:0"><strong>三个韵脚</strong><br/>'
      '① <strong>风 fēng、空 kōng、穹 qióng</strong><br/>'
      '② <strong>三个字都排在句尾</strong><br/><br/>'
      '<strong>一句话：句尾押上了。</strong></p>'
      '<p><strong>为什么能押</strong><br/>'
      '① <strong>古音里三个字同属东韵</strong><br/>'
      '② <strong>「风」今天念 fēng，古音近 fōng</strong><br/><br/>'
      '<strong>一句话：押韵看古音，不看拼音。</strong></p>'
      '<p><strong>怎么听出来</strong><br/>'
      '① <strong>念的时候句尾三个字念重一点</strong><br/>'
      '② <strong>连念三遍，就听出「一口韵」</strong><br/><br/>'
      '<strong>一句话：耳朵比眼睛先懂。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 从对字到一幅画</h2>'
      '<p style="margin:0"><strong>第一层：对字</strong><br/>'
      '① <strong>天—地、雨—风、山—海</strong><br/>'
      '② <strong>花—树、赤—苍，一字对一字</strong><br/><br/>'
      '<strong>一句话：单字成双。</strong></p>'
      '<p><strong>第二层：对句</strong><br/>'
      '① <strong>大陆对长空，五字对五字</strong><br/>'
      '② <strong>山花对海树、赤日对苍穹，都是五字</strong><br/><br/>'
      '<strong>一句话：字数一样才叫对。</strong></p>'
      '<p><strong>第三层：成画</strong><br/>'
      '① <strong>上有日月风雨，下有山海花树</strong><br/>'
      '② <strong>五组连起来，是一整片天地</strong><br/><br/>'
      '<strong>一句话：对到最后成了画。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 万物成双</h2>'
      '<p>一段话，一幅天地——</p>'
      '<h3>"天对地，雨对风。大陆对长空。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>五个对句，'
      '写天地、风雨、山海、日月。</p><p>📖 一幅天地</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>它让你看见世界是成双成对的——'
      '有天就有地，有山就有海。</p><p>💡 成双</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>念的时候留意句尾的「风、空、穹」，'
      '一口韵到底。</p><p>🌱 韵脚</p>'),
 72: '<p>这是「笠翁对韵课堂」第二课：一东第一段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「一东」的「东」是什么意思？</h3>'
       '<p><strong>是韵部的名字，不是「东边」。</strong><br/><br/>'
       '① <strong>凡古音跟「东」同韵的字都归在这里</strong><br/>'
       '② <strong>风、空、穹、中、红 都是</strong><br/>'
       '③ <strong>记法：取这一韵里最有代表性的一个字当名字。</strong></p>'
       '<h3>❓ 为什么「风」和「空」能押韵？</h3>'
       '<p><strong>古音里它们同属一东。</strong><br/><br/>'
       '① <strong>今天「风」念 fēng，古音更接近 fōng</strong><br/>'
       '② <strong>押韵看古音，不看今天的拼音</strong><br/>'
       '③ <strong>记法：念着顺，就是押上了。</strong></p>'
       '<h3>❓ 「大陆对长空」为什么是五个字？</h3>'
       '<p><strong>对仗要求字数相同。</strong><br/><br/>'
       '① <strong>三字对三字，五字对五字</strong><br/>'
       '② <strong>大陆（地）对长空（天），都是五字</strong><br/>'
       '③ <strong>记法：字数不对，就不叫对句。</strong></p>'
       '<h3>❓ 这一段要背下来吗？</h3>'
       '<p><strong>先念顺，不必硬背。</strong><br/><br/>'
       '① <strong>四句一天，念三遍，念出声</strong><br/>'
       '② <strong>念到能接下句，比硬背管用</strong><br/>'
       '③ <strong>记法：语感是念出来的。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念四句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>今天把「天对地，雨对风」四句念三遍，念出声</strong>；'
       '<strong>句尾三个字念重一点</strong>。</p><p>💡 找韵脚</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>从里面找出三个押韵的句尾字：风、空、穹</strong>；'
       '<strong>这就是「一口韵到底」</strong>。</p><p>🌱 自己配一对</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>给「山花」配一个五字的下句，字数要一样</strong>；'
       '<strong>这就是「对仗先数字数」</strong><br/><br/>'
       '<strong>本课的落点：学对仗。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天读一东第一段：五个对句，三个韵脚。<strong>风、空、穹</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">天对地，雨对风。大陆对长空。'
       '山花对海树，赤日对苍穹。</p><p>回顾本课要点:</p>'
       '<p>一东 · 第一段。<strong>上卷第一韵</strong>。</p>'
       '<p>天对地、雨对风、大陆对长空。<strong>先大后小</strong>。</p>'
       '<p>山花对海树、赤日对苍穹。<strong>五字对五字</strong>。</p>'
       '<p>风、空、穹 同属东韵。<strong>一口韵到底</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>笠翁对韵第二课，一东第一段；'
       '下一课接「雷隐隐，雾蒙蒙」。</p>'
       '<div class="ds-quote">'),

 111: '<p>天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 把四句背出来，背给家里人听。'
       '② 说出三个押韵的句尾字。'
       '③ 给「山花」配一个五字的下句。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>一东第一段：天对地，雨对风；'
       '五句成双，一口韵到底。</strong></p></div>'),

 119: '            "天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。"<br/>',
 120: '<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《笠翁对韵·一东》</span>',

 127: "    window.GUOXUE_COURSE_ID = '589-yi-dong';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 天对地，雨对风·最大的两对 -->',
 61: '<!-- 5. 大陆对长空·山花对海树，赤日对苍穹 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「一东」的「东」指的是什么？', opts: ['韵部的名字', '东边的方向', '作者的姓'], ans: 0, exp: '东是韵部名'},",
 "  {q: '2. 「天对地，雨对风」中，与「天」相对的是？', opts: ['地', '海', '日'], ans: 0, exp: '天对地'},",
 "  {q: '3. 「大陆对长空」的「长空」是什么意思？', opts: ['辽阔的天空', '很长的路', '空着的地方'], ans: 0, exp: '长空是辽阔的天空'},",
 "  {q: '4. 「山花对海树」中，与「山」相对的是？', opts: ['海', '花', '树'], ans: 0, exp: '山对海'},",
 "  {q: '5. 「赤日」的「赤」是什么颜色？', opts: ['红色', '黑色', '青色'], ans: 0, exp: '赤是红色'},",
 "  {q: '6. 「苍穹」指的是什么？', opts: ['青蓝色的天空', '苍老的树', '高高的山'], ans: 0, exp: '苍穹是青蓝的天'},",
 "  {q: '7. 这一段句尾押韵的三个字是？', opts: ['风、空、穹', '地、空、树', '天、雨、山'], ans: 0, exp: '风空穹同属东韵'},",
 "  {q: '8. 「大陆对长空」为什么上下都是五个字？', opts: ['对仗要求字数相同', '碰巧一样', '为了押韵'], ans: 0, exp: '字数相同才叫对句'},",
 "  {q: '9. 「一东」是全书哪一部分的第一韵？', opts: ['上卷', '下卷', '附录'], ans: 0, exp: '上卷第一韵'},",
 "  {q: '10. 读这一段最好的方法是？', opts: ['念出声，句尾念重一点', '抄十遍再说', '先背韵部名称'], ans: 0, exp: '先上口，再上讲'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("588-li-weng-dui-yun", "589-yi-dong")
    out = out.replace("yaoyue588", "yaoyue589")
    out = out.replace("开篇简介", "一东")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
