#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build592: 以 591 为骨架，按行号替换文字生成第 592 课
《笠翁对韵》一东·其二中段（云叆叇，日曈曚。蜡屐对渔篷。过天星似箭，吐魄月如弓。）
只换文字，不动任何 HTML 标签。行号与 591 完全一致。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/591-he-dui-han/index.html"
DST_DIR = f"{ROOT}/lessons/592-yun-ai-dai"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》一东其二中段。原文：「云叆叇，日曈曚。蜡屐对渔篷。过天星似箭，吐魄月如弓。」'
        '云厚日暗，涂蜡的木屐对渔船的篷，流星像箭对弯月像弓。句尾曚、篷、弓同属东韵。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("云","yún"),("叆","ài"),("叇","dài")]) + "，" + _r([("日","rì"),("曈","tóng"),("曚","méng")]) + "。", True)
 + _p(_r([("蜡","là"),("屐","jī"),("对","duì"),("渔","yú"),("篷","péng")]) + "。")
 + _p(_r([("过","guò"),("天","tiān"),("星","xīng"),("似","sì"),("箭","jiàn")]) + "，")
 + _p(_r([("吐","tǔ"),("魄","pò"),("月","yuè"),("如","rú"),("弓","gōng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 一东（云叆叇，日曈曚） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》一东其二中段：云叆叇，日曈曚。蜡屐对渔篷。过天星似箭，吐魄月如弓。云厚日暗，木屐对船篷，流星像箭对弯月像弓。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/592-yun-ai-dai/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/592-yun-ai-dai/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 一东（云叆叇，日曈曚）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">一东</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》上卷第一韵 · 其二中段</p>'
      '<p class="cover-desc">云厚得看不见天，太阳出来也昏昏的；'
      '脚上涂蜡的木屐，对着船上遮雨的篷；流星划过像一支箭，弯月挂起像一张弓。'
      '一句话：最后两句，越比越好看。</p><div class="cover-seal">弓</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 一东（其二中段）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>云层厚厚的，太阳出来了天还昏昏的；涂了蜡的木屐对着渔船上的篷；'
      '流星划过天空快得像箭，刚露出光的弯月弯得像弓。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>这是「其一」讲完天地日月之后，「其二」中间的四句，专挑稀奇的词和好看的比方。'
      '开头两句「叆叇」「曈曚」都是古书里形容云和日的词，今天不常说，念起来却很有味道。'
      '末两句把星比成箭、把月比成弓，箭和弓本来就是一对，比得又准又巧。'
      '句尾「曚、篷、弓」三个字同属东韵。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>云叆叇，日曈曚；蜡屐对渔篷；过天星似箭，吐魄月如弓。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话读这四句</h2>'
      '<p style="margin:0"><strong>两句写天气</strong><br/>'
      '① <strong>云叆叇：云厚得遮天</strong><br/>'
      '② <strong>日曈曚：太阳出来也不亮</strong><br/><br/>'
      '<strong>一句话：一个阴天。</strong></p>'
      '<p><strong>一组陆对水</strong><br/>'
      '① <strong>蜡屐：脚上穿的</strong><br/>'
      '② <strong>渔篷：船上遮的</strong><br/><br/>'
      '<strong>一句话：走路对打鱼。</strong></p>'
      '<p><strong>两个好比方</strong><br/>'
      '① <strong>星似箭、月如弓</strong><br/>'
      '② <strong>箭和弓，本来是一套</strong><br/><br/>'
      '<strong>一句话：比得又准又巧。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>云叆叇，日曈曚 · 两个难认的词</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>叆叇 ài dài：云很多很厚</strong><br/>'
      '② <strong>曈曚 tóng méng：日刚出不亮</strong><br/><br/>'
      '<strong>一句话：两个词都写「不明」。 </strong></p>'
      '<p><strong>云叆叇</strong><br/>'
      '① <strong>云一层压一层，天被遮住</strong><br/>'
      '② <strong>像要下雨又没下</strong><br/><br/>'
      '<strong>一句话：抬头看不见蓝。</strong></p>'
      '<p><strong>日曈曚</strong><br/>'
      '① <strong>太阳出来了，光还是昏黄的</strong><br/>'
      '② <strong>天将明未明那一刻</strong><br/><br/>'
      '<strong>一句话：有日头，不亮堂。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>蜡屐对渔篷 · 一个在陆，一个在水</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>屐 jī：木底鞋</strong><br/>'
      '② <strong>篷 péng：船上遮雨遮阳的棚</strong><br/><br/>'
      '<strong>一句话：一样穿，一样遮。</strong></p>'
      '<p><strong>蜡屐</strong><br/>'
      '① <strong>木屐上涂一层蜡，不怕水</strong><br/>'
      '② <strong>古人游山玩水常穿它</strong><br/><br/>'
      '<strong>一句话：走路的鞋。</strong></p>'
      '<p><strong>渔篷</strong><br/>'
      '① <strong>打鱼船上那个弯弯的篷</strong><br/>'
      '② <strong>下雨遮雨，出太阳遮阳</strong><br/><br/>'
      '<strong>一句话：船上像鞋的棚。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三块合看 · 星似箭，月如弓</h2>'
      '<p style="margin:0"><strong>过天星似箭</strong><br/>'
      '① <strong>流星划过天空，一眨眼就没了</strong><br/>'
      '② <strong>所以比作箭</strong><br/><br/>'
      '<strong>一句话：快。 </strong></p>'
      '<p><strong>吐魄月如弓</strong><br/>'
      '① <strong>魄：月亮的光；吐魄＝刚露出光</strong><br/>'
      '② <strong>弯弯的新月，正像一张弓</strong><br/><br/>'
      '<strong>一句话：弯。</strong></p>'
      '<p><strong>三个韵脚</strong><br/>'
      '① <strong>曚 méng、篷 péng、弓 gōng</strong><br/>'
      '② <strong>三个都在句尾</strong><br/><br/>'
      '<strong>一句话：一口韵到底。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 一句一层</h2>'
      '<p style="margin:0"><strong>第一层：天</strong><br/>'
      '① <strong>云叆叇、日曈曚——抬头一片昏</strong><br/>'
      '② <strong>先定下一个阴天的底子</strong><br/><br/>'
      '<strong>一句话：先写天色。</strong></p>'
      '<p><strong>第二层：人</strong><br/>'
      '① <strong>蜡屐、渔篷——人走路、人打鱼</strong><br/>'
      '② <strong>一在岸上，一在水上</strong><br/><br/>'
      '<strong>一句话：再写人怎么过日子。</strong></p>'
      '<p><strong>第三层：夜空</strong><br/>'
      '① <strong>星似箭、月如弓——天上动起来了</strong><br/>'
      '② <strong>箭和弓，明明是一套家什</strong><br/><br/>'
      '<strong>一句话：最后落到天上。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 比方也要成对</h2>'
      '<p>不只字要成对，比方也要成对——</p>'
      '<h3>"过天星似箭，吐魄月如弓。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>四句写阴天、木屐、船篷、'
      '流星和弯月。</p><p>📖 一天的景</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>连比方都成对——'
      '星比箭、月比弓，箭和弓原本就是一套。</p><p>💡 比方成双</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>晚上抬头看月亮，'
      '自己想一个比方。</p><p>🌱 会比方</p>'),
 72: '<p>这是「笠翁对韵课堂」第五课：一东其二中段。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「叆叇」怎么念，什么意思？</h3>'
       '<p><strong>念 ài dài，云厚的样子。</strong><br/><br/>'
       '① <strong>两个字都是云字旁加音</strong><br/>'
       '② <strong>云一层压一层，把天遮住了</strong><br/>'
       '③ <strong>记法：看到这两个字，就想到满天厚云。</strong></p>'
       '<h3>❓ 「曈曚」和「朦胧」是一回事吗？</h3>'
       '<p><strong>意思相近，写法不同。</strong><br/><br/>'
       '① <strong>曈曚 tóng méng：日字旁，专写太阳将出未亮</strong><br/>'
       '② <strong>朦胧 méng lóng：月字旁，多写月色模糊</strong><br/>'
       '③ <strong>记法：日字旁管太阳，月字旁管月亮。</strong></p>'
       '<h3>❓ 「蜡屐」为什么要涂蜡？</h3>'
       '<p><strong>为了防水防滑。</strong><br/><br/>'
       '① <strong>木底鞋怕水，涂一层蜡就不怕了</strong><br/>'
       '② <strong>古人游山玩水常穿，走湿路不湿脚</strong><br/>'
       '③ <strong>记法：屐是木鞋，蜡是雨衣。</strong></p>'
       '<h3>❓ 「吐魄月如弓」的「魄」是什么？</h3>'
       '<p><strong>指月亮的光。</strong><br/><br/>'
       '① <strong>吐魄＝月刚露出一点光</strong><br/>'
       '② <strong>刚露光的弯月，正像一张弓</strong><br/>'
       '③ <strong>记法：魄是月光，不是魂魄。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念四句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把「云叆叇，日曈曚」四句念三遍</strong>；'
       '<strong>前两句念慢，末两句念快</strong>。</p><p>💡 认两个词</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>记住「叆叇」是云厚、「曈曚」是日暗</strong>；'
       '<strong>这就叫「认词」</strong>。</p><p>🌱 自己比一个</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看天上的云，说一句「云像什么」</strong>；'
       '<strong>再说一句「月像什么」，两句要对得上</strong><br/><br/>'
       '<strong>本课的落点：比方也要成对。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>四句一句一层：天色、人家、夜空。<strong>曚、篷、弓</strong>三个韵脚。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">云叆叇，日曈曚。蜡屐对渔篷。'
       '过天星似箭，吐魄月如弓。</p><p>回顾本课要点:</p>'
       '<p>云叆叇、日曈曚。<strong>云厚、日不亮</strong>。</p>'
       '<p>蜡屐对渔篷。<strong>陆上走，水上住</strong>。</p>'
       '<p>过天星似箭。<strong>星比箭，写快</strong>。</p>'
       '<p>吐魄月如弓。<strong>月比弓，写弯；箭对弓成套</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>一东其二中段；'
       '下一课「驿旅客逢梅子雨」。</p>'
       '<div class="ds-quote">'),

 111: '<p>云叆叇，日曈曚。蜡屐对渔篷。过天星似箭，吐魄月如弓。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 把四句背出来。'
       '② 说出「叆叇」「曈曚」各写什么。'
       '③ 自己想两个比方，让它们成一对。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>云厚日暗，屐对篷，星似箭，月如弓；'
       '比方也要成双。</strong></p></div>'),

 119: '            "云叆叇，日曈曚。蜡屐对渔篷。过天星似箭，吐魄月如弓。"<br/>',
 120: '<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《笠翁对韵·一东》</span>',

 127: "    window.GUOXUE_COURSE_ID = '592-yun-ai-dai';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 云叆叇，日曈曚·两个难认的词 -->',
 61: '<!-- 5. 蜡屐对渔篷·一个在陆一个在水 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「叆叇」怎么念？', opts: ['ài dài', 'ài dì', 'ái dài'], ans: 0, exp: '叆叇读 ài dài'},",
 "  {q: '2. 「云叆叇」写的是什么？', opts: ['云很多很厚，遮住天', '云很白很轻', '没有云'], ans: 0, exp: '叆叇是云厚'},",
 "  {q: '3. 「日曈曚」写的是什么？', opts: ['太阳出来了但天还昏', '太阳很亮', '天黑了'], ans: 0, exp: '曈曚是日将明未亮'},",
 "  {q: '4. 「蜡屐」的「屐」是什么？', opts: ['木底鞋', '一种帽子', '雨伞'], ans: 0, exp: '屐是木底鞋'},",
 "  {q: '5. 木屐上涂蜡是为了什么？', opts: ['防水防滑', '好看', '防虫'], ans: 0, exp: '涂蜡防湿'},",
 "  {q: '6. 「渔篷」装在哪儿？', opts: ['渔船上', '屋檐上', '马背上'], ans: 0, exp: '渔篷是船篷'},",
 "  {q: '7. 「过天星似箭」把流星比作什么？', opts: ['箭', '弓', '灯'], ans: 0, exp: '比作箭，写快'},",
 "  {q: '8. 「吐魄月如弓」中的「魄」指什么？', opts: ['月亮的光', '魂魄', '月亮本身'], ans: 0, exp: '魄指月光'},",
 "  {q: '9. 这一段句尾押韵的三个字是？', opts: ['曚、篷、弓', '叇、曚、箭', '云、日、月'], ans: 0, exp: '曚篷弓同属东韵'},",
 "  {q: '10. 「星似箭，月如弓」妙在哪里？', opts: ['两个比方正好成对，箭和弓本是一套', '写得长', '用了生字'], ans: 0, exp: '比方也成双'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("591-he-dui-han", "592-yun-ai-dai")
    out = out.replace("yaoyue591", "yaoyue592")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
