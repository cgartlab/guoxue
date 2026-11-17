#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build590: 以 589 为骨架，按行号替换文字生成第 590 课
《笠翁对韵》一东·其一后四句（雷隐隐，雾蒙蒙。日下对天中。风高秋月白，雨霁晚霞红。）
只换文字，不动任何 HTML 标签。行号与 589 完全一致。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/589-yi-dong/index.html"
DST_DIR = f"{ROOT}/lessons/590-lei-yin-yin"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》一东其一后四句。原文：「雷隐隐，雾蒙蒙。日下对天中。风高秋月白，雨霁晚霞红。」'
        '前两句叠字写雷与雾，后两句方位对方位、颜色对颜色；句尾蒙、中、红同属东韵。'
        '一东其一，至此讲完。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("雷","léi"),("隐","yǐn"),("隐","yǐn")]) + "，" + _r([("雾","wù"),("蒙","méng"),("蒙","méng")]) + "。", True)
 + _p(_r([("日","rì"),("下","xià"),("对","duì"),("天","tiān"),("中","zhōng")]) + "。")
 + _p(_r([("风","fēng"),("高","gāo"),("秋","qiū"),("月","yuè"),("白","bái")]) + "，")
 + _p(_r([("雨","yǔ"),("霁","jì"),("晚","wǎn"),("霞","xiá"),("红","hóng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 一东（雷隐隐，雾蒙蒙） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》一东其一后四句：雷隐隐，雾蒙蒙。日下对天中。风高秋月白，雨霁晚霞红。叠字成对、方位对方位、颜色对颜色。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/590-lei-yin-yin/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/590-lei-yin-yin/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 一东（雷隐隐，雾蒙蒙）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">一东</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》上卷第一韵 · 其一后四句</p>'
      '<p class="cover-desc">上一课说了天和地，这一课抬头看天：雷声隐隐，雾气蒙蒙；'
      '太阳西下对着天空正中，秋风里月色白对着雨后晚霞红。'
      '一句话：四句全是天上的景。</p><div class="cover-seal">雾</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 一东（其一后四句）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>雷声隐隐地响，雾气蒙蒙地飘；太阳落下的天边对着天空正中；'
      '秋风起了，月色发白；雨停了，晚霞通红。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>这是「一东」其一的第二段，接着上一课的天对地往下说。四句全写天上的景：'
      '雷、雾、日、月、雨、霞，一样一样对起来。句尾「蒙、中、红」三个字同属东韵，念着还是一口韵到底。'
      '古音里「蒙」近 méng、「中」近 zhōng、「红」近 hóng，尾巴都是「ong」，所以押得上。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>雷隐隐，雾蒙蒙；日下对天中；风高秋月白，雨霁晚霞红。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话读这四句</h2>'
      '<p style="margin:0"><strong>全是天象</strong><br/>'
      '① <strong>雷、雾、日、月、雨、霞</strong><br/>'
      '② <strong>抬头就能看见的东西</strong><br/><br/>'
      '<strong>一句话：一节课都在看天。</strong></p>'
      '<p><strong>两组对法</strong><br/>'
      '① <strong>叠字成对：雷隐隐 对 雾蒙蒙</strong><br/>'
      '② <strong>方位对方位：日下 对 天中</strong><br/><br/>'
      '<strong>一句话：对得越来越讲究。</strong></p>'
      '<p><strong>三个韵脚</strong><br/>'
      '① <strong>蒙、中、红 落在句尾</strong><br/>'
      '② <strong>三个字同属东韵</strong><br/><br/>'
      '<strong>一句话：还是一口韵到底。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>雷隐隐，雾蒙蒙 · 叠字成对</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>隐隐 yǐn：听不太清，若有若无</strong><br/>'
      '② <strong>蒙蒙 méng：细密、看不清</strong><br/><br/>'
      '<strong>一句话：两个叠字，都是「不太分明」。</strong></p>'
      '<p><strong>雷隐隐</strong><br/>'
      '① <strong>雷在远处响，闷闷地滚过来</strong><br/>'
      '② <strong>写的是「听」</strong><br/><br/>'
      '<strong>一句话：耳朵听见的。</strong></p>'
      '<p><strong>雾蒙蒙</strong><br/>'
      '① <strong>雾很细，前面的东西看不清</strong><br/>'
      '② <strong>写的是「看」</strong><br/><br/>'
      '<strong>一句话：眼睛看见的。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>日下对天中 · 风高秋月白</h2>'
      '<p style="margin:0"><strong>日下 对 天中</strong><br/>'
      '① <strong>日下：太阳落下的天边</strong><br/>'
      '② <strong>天中：天空的正中</strong><br/><br/>'
      '<strong>一句话：下对中，方位对方位。</strong></p>'
      '<p><strong>为什么工整</strong><br/>'
      '① <strong>日对天，都是天上的东西</strong><br/>'
      '② <strong>下对中，都是方位</strong><br/><br/>'
      '<strong>一句话：两样都对上了。</strong></p>'
      '<p><strong>风高 秋月白</strong><br/>'
      '① <strong>风高＝风大、风起</strong><br/>'
      '② <strong>秋月白：秋天的月亮亮得发白</strong><br/><br/>'
      '<strong>一句话：一个写风，一个写月。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三块合看 · 白对红，蒙中红一口韵</h2>'
      '<p style="margin:0"><strong>雨霁晚霞红</strong><br/>'
      '① <strong>霁 jì：雨停了，天放晴</strong><br/>'
      '② <strong>晚霞红：傍晚的云霞通红</strong><br/><br/>'
      '<strong>一句话：雨一停，天就红了。</strong></p>'
      '<p><strong>颜色对颜色</strong><br/>'
      '① <strong>秋月白 对 晚霞红</strong><br/>'
      '② <strong>和上一课「赤日对苍穹」一个手法</strong><br/><br/>'
      '<strong>一句话：白对红，最见功夫。</strong></p>'
      '<p><strong>三个韵脚</strong><br/>'
      '① <strong>蒙 méng、中 zhōng、红 hóng</strong><br/>'
      '② <strong>三个都在句尾，尾巴都是「ong」</strong><br/><br/>'
      '<strong>一句话：念着还是一口韵。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 一天的天气</h2>'
      '<p style="margin:0"><strong>第一层：听</strong><br/>'
      '① <strong>雷隐隐——先听见</strong><br/>'
      '② <strong>雾蒙蒙——再看不清</strong><br/><br/>'
      '<strong>一句话：风雨要来。</strong></p>'
      '<p><strong>第二层：看</strong><br/>'
      '① <strong>日下天中——太阳偏西</strong><br/>'
      '② <strong>风高月白——天黑了，月上来</strong><br/><br/>'
      '<strong>一句话：从下午到夜里。</strong></p>'
      '<p><strong>第三层：收</strong><br/>'
      '① <strong>雨霁晚霞红——雨过天晴</strong><br/>'
      '② <strong>四句连起来，是一整天的天色</strong><br/><br/>'
      '<strong>一句话：一句一景，连成一幅。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 天上的东西也成双</h2>'
      '<p>抬头看天，处处成对——</p>'
      '<h3>"雷隐隐，雾蒙蒙。日下对天中。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>四句写雷、雾、日、月、雨、霞，'
      '一句一景。</p><p>📖 一天的天气</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>连天上的东西都两两成对——'
      '雷对雾，日对天，白对红。</p><p>💡 处处成双</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>出门看看今天的天，'
      '自己试着对一句。</p><p>🌱 学会看</p>'),
 72: '<p>这是「笠翁对韵课堂」第三课：一东其一，到这儿讲完。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「隐隐」和「蒙蒙」是什么意思？</h3>'
       '<p><strong>都是「不太分明」的样子。</strong><br/><br/>'
       '① <strong>隐隐：听不清、若有若无，多写声音</strong><br/>'
       '② <strong>蒙蒙：细密、看不清，多写雾气雨丝</strong><br/>'
       '③ <strong>记法：隐隐靠耳，蒙蒙靠眼。</strong></p>'
       '<h3>❓ 「雨霁」的「霁」怎么念？</h3>'
       '<p><strong>念 jì，意思是雨雪停了、天放晴。</strong><br/><br/>'
       '① <strong>不读 qí，也不读 jī</strong><br/>'
       '② <strong>「雪霁」「雨霁」都是天刚放晴</strong><br/>'
       '③ <strong>记法：霁＝雨收云散。</strong></p>'
       '<h3>❓ 「日下对天中」怎么就对上了？</h3>'
       '<p><strong>两处都对：日对天，下对中。</strong><br/><br/>'
       '① <strong>日、天 都是天上的东西</strong><br/>'
       '② <strong>下、中 都是方位</strong><br/>'
       '③ <strong>记法：先看名目对不对，再看字数等不等。</strong></p>'
       '<h3>❓ 「风高秋月白」的「白」好在哪里？</h3>'
       '<p><strong>好在跟下句的「红」正对。</strong><br/><br/>'
       '① <strong>月色白 对 晚霞红，颜色对颜色</strong><br/>'
       '② <strong>白是冷色，红是暖色，一冷一暖更见功夫</strong><br/>'
       '③ <strong>记法：写景时抓住颜色，最容易对上。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念四句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把「雷隐隐，雾蒙蒙」四句念三遍，念出声</strong>；'
       '<strong>叠字要念得慢一点</strong>。</p><p>💡 看今天的天</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>放学抬头看看：有云没云，什么颜色</strong>；'
       '<strong>这就是「学会看」</strong>。</p><p>🌱 自己配一对</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>给「秋月白」配一个下句，末字要押「红」的韵</strong>；'
       '<strong>这就是「颜色对颜色」</strong><br/><br/>'
       '<strong>本课的落点：学对仗。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天抬头看天：雷雾、日月、雨霞。<strong>蒙、中、红</strong>三个韵脚。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">雷隐隐，雾蒙蒙。日下对天中。'
       '风高秋月白，雨霁晚霞红。</p><p>回顾本课要点:</p>'
       '<p>雷隐隐、雾蒙蒙。<strong>叠字成对，一听一看</strong>。</p>'
       '<p>日下对天中。<strong>日对天，下对中</strong>。</p>'
       '<p>风高秋月白、雨霁晚霞红。<strong>白对红</strong>。</p>'
       '<p>蒙、中、红 同属东韵。<strong>一口韵到底</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>一东其一讲完；'
       '下一课「河对汉，绿对红」。</p>'
       '<div class="ds-quote">'),

 111: '<p>雷隐隐，雾蒙蒙。日下对天中。风高秋月白，雨霁晚霞红。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 把四句背出来。'
       '② 说出「霁」的意思和读音。'
       '③ 给「秋月白」配一个下句，末字押东韵。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>一东其一后四句：雷雾成对，日月成双；'
       '白对红，蒙中红押韵。</strong></p></div>'),

 119: '            "雷隐隐，雾蒙蒙。日下对天中。风高秋月白，雨霁晚霞红。"<br/>',
 120: '<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《笠翁对韵·一东》</span>',

 127: "    window.GUOXUE_COURSE_ID = '590-lei-yin-yin';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 雷隐隐，雾蒙蒙·叠字成对 -->',
 61: '<!-- 5. 日下对天中·风高秋月白 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「雷隐隐」的「隐隐」是什么意思？', opts: ['听不太清、若有若无', '很响亮', '看不见'], ans: 0, exp: '隐隐是听不太清'},",
 "  {q: '2. 「雾蒙蒙」主要写的是什么？', opts: ['眼睛看不清', '耳朵听见的', '鼻子闻到的'], ans: 0, exp: '蒙蒙写看不清的样子'},",
 "  {q: '3. 「雨霁」的「霁」是什么意思？', opts: ['雨停了，天放晴', '下雨了', '雨很大'], ans: 0, exp: '霁是雨雪停止'},",
 "  {q: '4. 「霁」的读音是？', opts: ['jì', 'qí', 'jī'], ans: 0, exp: '霁读 jì'},",
 "  {q: '5. 「日下对天中」中，与「下」相对的是？', opts: ['中', '天', '日'], ans: 0, exp: '下对中，方位对方位'},",
 "  {q: '6. 「风高」是什么意思？', opts: ['风大、风起', '风很小', '风停了'], ans: 0, exp: '风高是风大'},",
 "  {q: '7. 「雨霁晚霞红」的「红」与上句哪个字正对？', opts: ['白', '月', '秋'], ans: 0, exp: '白对红，颜色对颜色'},",
 "  {q: '8. 这一段句尾押韵的三个字是？', opts: ['蒙、中、红', '隐、蒙、白', '日、风、雨'], ans: 0, exp: '蒙中红同属东韵'},",
 "  {q: '9. 这四句合起来写的是什么？', opts: ['一整天的天色', '一年四季', '一座山的样子'], ans: 0, exp: '从雷雾到日月到晚霞'},",
 "  {q: '10. 这一段属于「一东」的哪一部分？', opts: ['其一的后四句', '其二的开头', '下卷第一韵'], ans: 0, exp: '一东其一后四句'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("589-yi-dong", "590-lei-yin-yin")
    out = out.replace("yaoyue589", "yaoyue590")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
