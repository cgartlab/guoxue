#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build588: 以 587 为骨架，按行号替换文字生成第 588 课
《笠翁对韵》开篇简介（清·李渔，上下两卷各 15 韵部，共三十韵）。新开「笠翁对韵课堂」门类。
只换文字，不动任何 HTML 标签。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/587-fei-sheng-shu/index.html"
DST_DIR = f"{ROOT}/lessons/588-li-weng-dui-yun"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》开篇简介。清·李渔（号笠翁）著，全书分上下两卷，每卷十五个韵部，共三十韵。'
        '这一课讲清楚：这本书是谁写的、为什么叫「笠翁对韵」、三十韵怎么排、小学生怎么用。'
        '一句话：学对仗、练语感、认韵部。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("天","tiān"),("对","duì"),("地","dì")]) + "，" + _r([("雨","yǔ"),("对","duì"),("风","fēng")]) + "。", True)
 + _p(_r([("河","hé"),("对","duì"),("汉","hàn")]) + "，" + _r([("绿","lǜ"),("对","duì"),("红","hóng")]) + "。")
 + _p(_r([("晨","chén"),("对","duì"),("午","wǔ")]) + "，" + _r([("夏","xià"),("对","duì"),("冬","dōng")]) + "。")
 + _p(_r([("雷","léi"),("隐","yǐn"),("隐","yǐn")]) + "，" + _r([("雾","wù"),("蒙","méng"),("蒙","méng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 开篇简介（清·李渔，三十韵） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》开篇简介：清·李渔著，上下两卷各十五韵部，共三十韵。讲清作者、书名、三十韵与怎么读。学对仗、练语感。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/588-li-weng-dui-yun/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/588-li-weng-dui-yun/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 开篇简介（清·李渔，三十韵）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">对韵</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》开篇简介 · 清·李渔</p>'
      '<p class="cover-desc">天对地，雨对风——这是三百多年前一位戴斗笠的老先生编的书。'
      '上下两卷，每卷十五个韵部，共三十韵。'
      '一句话：学对仗、练语感、认韵部。</p><div class="cover-seal">韵</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 开篇的样子（一东 / 二冬）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>天对着地，雨对着风；河对着汉（天河），绿对着红；早晨对着正午，夏天对着冬天；'
      '雷声隐隐，雾气蒙蒙。这本书通篇都是这样的对句——上一句和下一句，字数一样、意思相对、声音相和。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>《笠翁对韵》是清朝李渔编的一本蒙学书。李渔号「笠翁」，所以叫《笠翁对韵》。'
      '「对」是对仗：上下句字数相同、词性相对；「韵」是押韵：句尾的字落在同一个韵部里。'
      '全书按韵部分段，一个韵部一段，段里全是成双成对的词句——把「怎么对、怎么押」示范给你看。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>天对地，雨对风；河对汉，绿对红；晨对午，夏对冬；雷隐隐，雾蒙蒙。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话认识这本书</h2>'
      '<p style="margin:0"><strong>谁写的</strong><br/>'
      '① <strong>清朝人李渔，号笠翁</strong><br/>'
      '② <strong>写戏、写文章的高手，也编蒙学书</strong><br/><br/>'
      '<strong>一句话：老行家编给小孩的书。</strong></p>'
      '<p><strong>教什么</strong><br/>'
      '① <strong>对仗：怎么对上</strong><br/>'
      '② <strong>押韵：怎么押上</strong><br/><br/>'
      '<strong>一句话：教你说对句。</strong></p>'
      '<p><strong>有多少</strong><br/>'
      '① <strong>上下两卷，每卷十五韵</strong><br/>'
      '② <strong>合起来三十韵</strong><br/><br/>'
      '<strong>一句话：三十段，段段成双。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>李渔与书名 · 笠翁是谁</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>笠 lì：斗笠；翁：老人</strong><br/>'
      '② <strong>对：对仗；韵：押韵</strong><br/><br/>'
      '<strong>一句话：戴斗笠的老先生。</strong></p>'
      '<p><strong>李渔其人</strong><br/>'
      '① <strong>明末清初人，号笠翁，浙江兰溪人</strong><br/>'
      '② <strong>会写戏、懂生活，写过《闲情偶寄》</strong><br/><br/>'
      '<strong>一句话：懂文章的人编的书，靠得住。</strong></p>'
      '<p><strong>书名什么意思</strong><br/>'
      '① <strong>笠翁＝李渔自己</strong><br/>'
      '② <strong>对韵＝对仗加押韵</strong><br/><br/>'
      '<strong>一句话：笠翁编的对韵书。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三十韵 · 上卷十五，下卷十五</h2>'
      '<p style="margin:0"><strong>上卷十五韵</strong><br/>'
      '① <strong>一东 二冬 三江 四支 五微</strong><br/>'
      '② <strong>六鱼 七虞 八齐 九佳 十灰 十一真 十二文 十三元 十四寒 十五删</strong><br/><br/>'
      '<strong>一句话：上卷十五。</strong></p>'
      '<p><strong>下卷十五韵</strong><br/>'
      '① <strong>一先 二萧 三肴 四豪 五歌</strong><br/>'
      '② <strong>六麻 七阳 八庚 九青 十蒸 十一尤 十二侵 十三覃 十四盐 十五咸</strong><br/><br/>'
      '<strong>一句话：下卷十五。</strong></p>'
      '<p><strong>合起来</strong><br/>'
      '① <strong>三十韵＝平声三十个韵部</strong><br/>'
      '② <strong>押韵时，同一韵部的字才押得上</strong><br/><br/>'
      '<strong>一句话：三十段，一段一韵。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三块合看 · 小学生怎么用这本书</h2>'
      '<p style="margin:0"><strong>先念</strong><br/>'
      '① <strong>一天一段，念三遍，念到顺口</strong><br/>'
      '② <strong>不认得的字先圈出来</strong><br/><br/>'
      '<strong>一句话：先上口，再上讲。</strong></p>'
      '<p><strong>再看</strong><br/>'
      '① <strong>看它怎么对：天对地，雨对风</strong><br/>'
      '② <strong>想想为什么这样对：意思相对、字数相同</strong><br/><br/>'
      '<strong>一句话：看出门道。</strong></p>'
      '<p><strong>后仿</strong><br/>'
      '① <strong>自己试着对一句：花对草，日对星</strong><br/>'
      '② <strong>对得不好不要紧，对得上就成</strong><br/><br/>'
      '<strong>一句话：会仿，才算学会。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 从字到句到段</h2>'
      '<p style="margin:0"><strong>第一层：字对</strong><br/>'
      '① <strong>天对地，雨对风——一个字对一个字</strong><br/>'
      '② <strong>意思相对，词性相同</strong><br/><br/>'
      '<strong>一句话：单字成双。</strong></p>'
      '<p><strong>第二层：句对</strong><br/>'
      '① <strong>山花对海树，赤日对苍穹</strong><br/>'
      '② <strong>五个字对五个字，句子对句子</strong><br/><br/>'
      '<strong>一句话：整句成双。</strong></p>'
      '<p><strong>第三层：成段</strong><br/>'
      '① <strong>一东整段，全是「东」韵的字打底</strong><br/>'
      '② <strong>念起来像唱歌，越念越顺</strong><br/><br/>'
      '<strong>一句话：段段押韵。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 学对仗</h2>'
      '<p>一本书，一件事——</p>'
      '<h3>"天对地，雨对风。大陆对长空。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>一本教对仗押韵的蒙学书，'
      '上下两卷三十韵。</p><p>📖 三十韵</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>它教的不只是工整，'
      '是让你看见世界成双成对的样子。</p><p>💡 对仗</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>念得顺、对得上；'
      '先学看，再学写。</p><p>🌱 语感</p>'),
 72: '<p>这是「笠翁对韵课堂」第一课：全书开篇简介。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 《笠翁对韵》和《声律启蒙》有什么不同？</h3>'
       '<p><strong>都是教对仗押韵的蒙学书，作者不同。</strong><br/><br/>'
       '① <strong>《笠翁对韵》是清朝李渔编的</strong><br/>'
       '② <strong>《声律启蒙》是清朝车万育编的</strong><br/>'
       '③ <strong>记法：先学一本就够，别同时开两本。</strong></p>'
       '<h3>❓ 三十韵是什么？</h3>'
       '<p><strong>平声的三十个韵部。</strong><br/><br/>'
       '① <strong>上卷十五韵（一东到十五删）</strong><br/>'
       '② <strong>下卷十五韵（一先到十五咸）</strong><br/>'
       '③ <strong>记法：同一个韵部的字，读起来尾巴相近，才押得上。</strong></p>'
       '<h3>❓ 小学生读这个有什么用？</h3>'
       '<p><strong>学对仗、认词、练语感。</strong><br/><br/>'
       '① <strong>作文里的对比、排比，就靠这个底子</strong><br/>'
       '② <strong>念多了，句子会自己往外冒</strong><br/>'
       '③ <strong>记法：不要求写古诗，先把句子说漂亮。</strong></p>'
       '<h3>❓ 一定要背下来吗？</h3>'
       '<p><strong>不必硬背，念熟就够。</strong><br/><br/>'
       '① <strong>一天一段，念三遍，自然记住大半</strong><br/>'
       '② <strong>硬背伤兴趣，念顺才养语感</strong><br/>'
       '③ <strong>记法：念成习惯，比背成任务强。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念一段</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>今天把「一东」开头念三遍，念出声</strong>；'
       '<strong>这就是「先上口」</strong>。</p><p>💡 找一对</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>从里面挑一对最喜欢的，说说为什么对得上</strong>；'
       '<strong>这就是「看出门道」</strong>。</p><p>🌱 自己对一句</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>自己编一对三字对：花对草，日对星</strong>；'
       '<strong>这就是「会仿才算学会」</strong><br/><br/>'
       '<strong>本课的落点：学对仗。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>今天认识这本书：清·李渔，三十韵，学对仗。<strong>先念，再看，后仿</strong>。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">天对地，雨对风。大陆对长空。'
       '山花对海树，赤日对苍穹。</p><p>回顾本课要点:</p>'
       '<p>笠翁对韵 · 开篇简介。<strong>清·李渔</strong>。</p>'
       '<p>笠翁＝李渔的号；对韵＝对仗加押韵。<strong>书名有来历</strong>。</p>'
       '<p>上下两卷，每卷十五韵。<strong>共三十韵</strong>。</p>'
       '<p>一个字对一个字，一句话对一句话。<strong>由字到句到段</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>本书第一课；'
       '下一课进「一东」，一天一段。</p>'
       '<div class="ds-quote">'),

 111: '<p>天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 说说「笠翁」「对」「韵」各是什么意思。'
       '② 上下两卷各有多少韵部，合起来多少韵。'
       '③ 自己想一对三字对，明天念给同学听。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>笠翁对韵，清·李渔编；上下两卷，三十韵；'
       '学对仗，练语感。</strong></p></div>'),

 119: '            "天对地，雨对风。大陆对长空。山花对海树，赤日对苍穹。"<br/>',

 127: "    window.GUOXUE_COURSE_ID = '588-li-weng-dui-yun';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 李渔与书名·笠翁是谁 -->',
 61: '<!-- 5. 三十韵·上卷十五下卷十五 -->',
}

QUIZ_LINES = [
 "  {q: '1. 《笠翁对韵》的作者是谁？', opts: ['清·李渔', '清·车万育', '宋·朱熹'], ans: 0, exp: '作者是李渔'},",
 "  {q: '2. 「笠翁」是什么？', opts: ['李渔的号', '一种帽子', '地名'], ans: 0, exp: '笠翁是李渔的号'},",
 "  {q: '3. 全书分几卷？', opts: ['上下两卷', '上中下三卷', '只有一卷'], ans: 0, exp: '上下两卷'},",
 "  {q: '4. 每一卷有多少个韵部？', opts: ['十五个', '十个', '三十个'], ans: 0, exp: '每卷十五韵'},",
 "  {q: '5. 全书一共多少韵？', opts: ['三十韵', '十五韵', '六十韵'], ans: 0, exp: '十五加十五等于三十'},",
 "  {q: '6. 「对韵」的「对」是什么意思？', opts: ['对仗', '对面', '对错'], ans: 0, exp: '对是对仗'},",
 "  {q: '7. 「天对地，雨对风」出自哪一韵？', opts: ['一东', '一先', '十五咸'], ans: 0, exp: '一东开头'},",
 "  {q: '8. 这本书主要教什么？', opts: ['对仗和押韵', '写字和算数', '历史和地理'], ans: 0, exp: '教对仗押韵'},",
 "  {q: '9. 三十韵是怎么分的？', opts: ['上卷十五、下卷十五', '上卷十、下卷二十', '随机排的'], ans: 0, exp: '上十五下十五'},",
 "  {q: '10. 小学生读它最大的收获是什么？', opts: ['学对仗、认词、练语感', '会写古诗就能得奖', '认全所有生字'], ans: 0, exp: '先练语感，不求写诗'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("587-fei-sheng-shu", "588-li-weng-dui-yun")
    out = out.replace("yaoyue587", "yaoyue588")
    out = out.replace("第四十七课", "第一课")
    out = out.replace("余力学文末段", "笠翁对韵·开篇简介")
    out = out.replace("余力学文课堂」", "笠翁对韵课堂」")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
