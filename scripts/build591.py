#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build591: 以 590 为骨架，按行号替换文字生成第 591 课
《笠翁对韵》一东·其二前四句（河对汉，绿对红。雨伯对雷公。烟楼对雪洞，月殿对天宫。）
只换文字，不动任何 HTML 标签。行号与 590 完全一致。"""
import io, os

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SRC = f"{ROOT}/lessons/590-lei-yin-yin/index.html"
DST_DIR = f"{ROOT}/lessons/591-he-dui-han"
DST = f"{DST_DIR}/index.html"

DESC = ('《笠翁对韵》一东其二前四句。原文：「河对汉，绿对红。雨伯对雷公。烟楼对雪洞，月殿对天宫。」'
        '黄河对汉水，绿色对红色，雨神对雷神，烟雾里的楼阁对积雪的山洞，月宫对天宫。'
        '句尾红、公、宫同属东韵。')

def _p(first, style_first=False):
    st = ('padding-top:0;' if style_first else '') + 'text-align:left;text-indent:0;letter-spacing:0.06em;font-size:1.75rem;line-height:1.8;width:100%;max-width:none;'
    st += 'margin:0' if style_first else 'margin:0.05em 0 0'
    return '<p style="' + st + '">' + first + '</p>'

def _r(chars):
    return "".join('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, p) for c, p in chars)

RAW = (
 _p(_r([("河","hé"),("对","duì"),("汉","hàn")]) + "，" + _r([("绿","lǜ"),("对","duì"),("红","hóng")]) + "。", True)
 + _p(_r([("雨","yǔ"),("伯","bó"),("对","duì"),("雷","léi"),("公","gōng")]) + "。")
 + _p(_r([("烟","yān"),("楼","lóu"),("对","duì"),("雪","xuě"),("洞","dòng")]) + "，")
 + _p(_r([("月","yuè"),("殿","diàn"),("对","duì"),("天","tiān"),("宫","gōng")]) + "。")
)

NEW = {
 6: '<meta content="' + DESC + '" name="description"/>',
 7: '<meta content="笠翁对韵 · 一东（河对汉，绿对红） · 笠翁对韵课堂" property="og:title"/>',
 8: '<meta content="《笠翁对韵》一东其二前四句：河对汉，绿对红。雨伯对雷公。烟楼对雪洞，月殿对天宫。黄河对汉水、颜色对颜色、雨神对雷神。" property="og:description"/>',
 10: '<meta content="https://guoxue.8023laozhanshi.cc/lessons/591-he-dui-han/index.html" property="og:url"/>',
 11: '<link href="https://guoxue.8023laozhanshi.cc/lessons/591-he-dui-han/index.html" rel="canonical"/>',
 12: '<title>笠翁对韵 · 一东（河对汉，绿对红）· 国学问答 · 国学课堂</title>',

 52: ('<div class="slide active cover-slide" data-page="0" data-section="lecture"><div class="cover-ornament"></div>'
      '<h2 class="ds-display">一东</h2><div class="cover-ornament"></div>'
      '<p class="cover-subtitle">《笠翁对韵》上卷第一韵 · 其二前四句</p>'
      '<p class="cover-desc">一东开了第二段：黄河对汉水，绿色对红色；'
      '管雨的雨伯对管雷的雷公；烟里的楼对雪里的洞，月亮上的宫殿对天上的宫殿。'
      '一句话：从地上对到天上。</p><div class="cover-seal">红</div></div>'),

 54: ('<div class="slide" data-page="1" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2 style="margin-bottom:6px;">原文 · 一东（其二前四句）</h2>'
      '<div class="ds-quote" style="margin:6px 0;padding:14px 16px 10px;line-height:1.6;">'),

 55: RAW,

 56: ('</div><p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none;margin-top:var(--ds-space-1)"><strong>通译</strong>：'
      '<strong>黄河对着汉水，绿色对着红色；雨神对着雷神；烟雾里的楼阁对着积雪的山洞，'
      '月亮上的宫殿对着天上的宫殿。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>背景</strong>：'
      '<strong>「其一」讲天地日月，「其二」换个开头，从两条大河说起，一路对到神仙住的宫殿。'
      '这一段越往后越「虚」：河和汉是看得见的，绿和红是颜色，雨伯雷公是神话里的神，'
      '月殿天宫是想出来的地方。句尾「红、公、宫」三个字同属东韵，还是一口韵到底。</strong></p>'
      '<p style="font-size:0.78rem;line-height:1.45;width:100%;max-width:none"><strong>小记</strong>：'
      '<strong>河对汉，绿对红；雨伯对雷公；烟楼对雪洞，月殿对天宫。</strong></p></div>'),

 58: ('<div class="slide" data-page="2" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>总说 · 三句话读这四句</h2>'
      '<p style="margin:0"><strong>先说两条河</strong><br/>'
      '① <strong>河＝黄河，汉＝汉水</strong><br/>'
      '② <strong>都是中国的大河</strong><br/><br/>'
      '<strong>一句话：大河对大河。</strong></p>'
      '<p><strong>再说两样色</strong><br/>'
      '① <strong>绿对红，纯颜色对纯颜色</strong><br/>'
      '② <strong>没有别的东西，就是色</strong><br/><br/>'
      '<strong>一句话：色对色，最见功夫。</strong></p>'
      '<p><strong>后说神与仙</strong><br/>'
      '① <strong>雨伯、雷公：管雨管雷的神</strong><br/>'
      '② <strong>月殿、天宫：神仙住的地方</strong><br/><br/>'
      '<strong>一句话：从地上说到天上。</strong></p></div>'),

 60: ('<div class="slide" data-page="3" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>河对汉，绿对红 · 两条河一对色</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>河 hé：黄河</strong><br/>'
      '② <strong>汉 hàn：汉水；绿 lǜ；红 hóng</strong><br/><br/>'
      '<strong>一句话：河与汉，都是大水。</strong></p>'
      '<p><strong>河对汉</strong><br/>'
      '① <strong>黄河在北方，汉水在南方</strong><br/>'
      '② <strong>一浊一清，一北一南，正好成对</strong><br/><br/>'
      '<strong>一句话：大河对大河。</strong></p>'
      '<p><strong>绿对红</strong><br/>'
      '① <strong>绿是叶，红是花</strong><br/>'
      '② <strong>上一课「秋月白、晚霞红」也是这个法子</strong><br/><br/>'
      '<strong>一句话：颜色对颜色。</strong></p></div>'),

 62: ('<div class="slide" data-page="4" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>雨伯对雷公 · 两位天神</h2>'
      '<p style="margin:0"><strong>先认字</strong><br/>'
      '① <strong>伯 bó：这里是对神的尊称</strong><br/>'
      '② <strong>公 gōng：也是尊称，如「雷公」</strong><br/><br/>'
      '<strong>一句话：伯和公，都是敬称。</strong></p>'
      '<p><strong>雨伯</strong><br/>'
      '① <strong>管下雨的雨神，又叫「雨师」</strong><br/>'
      '② <strong>古人想：雨总得有人管</strong><br/><br/>'
      '<strong>一句话：雨有主。</strong></p>'
      '<p><strong>雷公</strong><br/>'
      '① <strong>管打雷的雷神</strong><br/>'
      '② <strong>民间画像里是鸟嘴翅膀、拿锤拿凿</strong><br/><br/>'
      '<strong>一句话：雷也有主。</strong></p></div>'),

 64: ('<div class="slide" data-page="5" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>三块合看 · 烟楼雪洞，月殿天宫</h2>'
      '<p style="margin:0"><strong>烟楼 对 雪洞</strong><br/>'
      '① <strong>烟楼：烟雾里的楼阁</strong><br/>'
      '② <strong>雪洞：积雪的山洞</strong><br/><br/>'
      '<strong>一句话：一个在云里，一个在山里。</strong></p>'
      '<p><strong>月殿 对 天宫</strong><br/>'
      '① <strong>月殿：月亮上的宫殿，嫦娥住处</strong><br/>'
      '② <strong>天宫：天上的宫殿，玉皇住处</strong><br/><br/>'
      '<strong>一句话：一个在月，一个在天。</strong></p>'
      '<p><strong>三个韵脚</strong><br/>'
      '① <strong>红 hóng、公 gōng、宫 gōng</strong><br/>'
      '② <strong>三个都在句尾，尾巴都是「ong」</strong><br/><br/>'
      '<strong>一句话：一口韵到底。</strong></p></div>'),

 66: ('<div class="slide" data-page="6" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>逐层解读 · 越对越远</h2>'
      '<p style="margin:0"><strong>第一层：实的</strong><br/>'
      '① <strong>河对汉——真有的两条大河</strong><br/>'
      '② <strong>看得见，走得到</strong><br/><br/>'
      '<strong>一句话：从身边说起。</strong></p>'
      '<p><strong>第二层：虚的</strong><br/>'
      '① <strong>绿对红——只剩颜色</strong><br/>'
      '② <strong>烟楼雪洞——想出来的景</strong><br/><br/>'
      '<strong>一句话：从实往虚走。</strong></p>'
      '<p><strong>第三层：天上的</strong><br/>'
      '① <strong>雨伯雷公——神话里的神</strong><br/>'
      '② <strong>月殿天宫——神仙住的地方</strong><br/><br/>'
      '<strong>一句话：一路对到天上。</strong></p></div>'),

 68: ('<div class="slide" data-page="7" data-section="lecture"><span class="ds-badge ds-badge--accent">讲义</span>'
      '<h2>核心思想 · 从地上对到天上</h2>'
      '<p>四句一程，越对越远——</p>'
      '<h3>"河对汉，绿对红。雨伯对雷公。" ——《笠翁对韵·一东》</h3>'),
 69: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看表面：</strong>四句写两条河、两种颜色、'
      '两位神、两处仙宫。</p><p>📖 一路对上去</p>'),
 70: ('<p style="margin:var(--ds-space-1) 0 0"><strong>看内里：</strong>对仗不止对眼前的东西，'
      '连想出来的、传说中的都能对。</p><p>💡 虚实都能对</p>'),
 71: ('<p style="margin:var(--ds-space-1) 0 0"><strong>落点：</strong>试着把身边一物对到天上——'
      '地对天，河对汉。</p><p>🌱 敢想</p>'),
 72: '<p>这是「笠翁对韵课堂」第四课：一东其二前四句。</p></div>',

 102: ('<div class="slide" data-page="20" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>常见问题</h2>'
       '<h3>❓ 「河对汉」的「汉」是什么？</h3>'
       '<p><strong>指汉水，一条大河。</strong><br/><br/>'
       '① <strong>黄河在北，汉水在南，一大一小配成对</strong><br/>'
       '② <strong>「汉」也能指天河（银汉），但这里说的是汉水</strong><br/>'
       '③ <strong>记法：河、汉都是水名，才对得上。</strong></p>'
       '<h3>❓ 雨伯、雷公是真有其人吗？</h3>'
       '<p><strong>不是人，是神话里的神。</strong><br/><br/>'
       '① <strong>雨伯又叫雨师，管下雨</strong><br/>'
       '② <strong>雷公管打雷，民间画成鸟嘴拿锤凿</strong><br/>'
       '③ <strong>记法：古人把风雨雷电想成有神在管。</strong></p>'
       '<h3>❓ 「烟楼」「雪洞」是真地方吗？</h3>'
       '<p><strong>不是地名，是想象出来的景。</strong><br/><br/>'
       '① <strong>烟楼：云雾里若隐若现的楼阁</strong><br/>'
       '② <strong>雪洞：积雪覆盖的山洞</strong><br/>'
       '③ <strong>记法：一在云里，一在山里，正好一对。</strong></p>'
       '<h3>❓ 「月殿」和「天宫」有什么不同？</h3>'
       '<p><strong>一个在月亮上，一个在天上。</strong><br/><br/>'
       '① <strong>月殿是嫦娥住的地方</strong><br/>'
       '② <strong>天宫是玉皇住的地方</strong><br/>'
       '③ <strong>记法：都在天上，却不在一处，所以能对。</strong></p></div>'),

 104: ('<div class="slide" data-page="21" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>生活应用</h2><p>这一课练三样本事——</p><p>📖 念四句</p>'),
 105: ('<p style="margin:var(--ds-space-1) 0 0"><strong>把「河对汉，绿对红」四句念三遍，念出声</strong>；'
       '<strong>「绿对红」念得脆一点</strong>。</p><p>💡 找颜色</p>'),
 106: ('<p style="margin:var(--ds-space-1) 0 0"><strong>在屋里找出三对颜色：红对绿、黑对白</strong>；'
       '<strong>这就是「色对色」</strong>。</p><p>🌱 自己对一句</p>'),
 107: ('<p style="margin:var(--ds-space-1) 0 0"><strong>照着「烟楼对雪洞」说一对：雨窗对风户</strong>；'
       '<strong>字数一样，末字押东韵更好</strong><br/><br/>'
       '<strong>本课的落点：虚实都能对。</strong></p></div>'),

 109: ('<div class="slide" data-page="22" data-section="review"><span class="ds-badge ds-badge--accent">答疑解惑</span>'
       '<h2>课程总结</h2><p>四句从地上对到天上。<strong>红、公、宫</strong>三个韵脚。</p>'
       '<p style="text-align:center;margin:var(--ds-space-4) 0">河对汉，绿对红。雨伯对雷公。'
       '烟楼对雪洞，月殿对天宫。</p><p>回顾本课要点:</p>'
       '<p>河对汉。<strong>黄河对汉水，大河对大河</strong>。</p>'
       '<p>绿对红。<strong>纯颜色对纯颜色</strong>。</p>'
       '<p>雨伯对雷公。<strong>雨神对雷神</strong>。</p>'
       '<p>烟楼雪洞、月殿天宫。<strong>一在云山，一在月天</strong>。</p>'
       '<p><strong>在全篇中的位置:</strong>一东其二开头；'
       '下一课「云叆叇，日曈曚」。</p>'
       '<div class="ds-quote">'),

 111: '<p>河对汉，绿对红。雨伯对雷公。烟楼对雪洞，月殿对天宫。</p>',
 112: ('</div><p><strong>课后小挑战:</strong>① 把四句背出来。'
       '② 说出「汉」「雨伯」各指什么。'
       '③ 自己配一对带颜色的三字对。</p>'
       '<p><strong>把这一课记在心里:</strong><strong>一东其二：河汉是水，绿红是色；'
       '雨伯雷公是神，月殿天宫是仙。</strong></p></div>'),

 119: '            "河对汉，绿对红。雨伯对雷公。烟楼对雪洞，月殿对天宫。"<br/>',
 120: '<span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 《笠翁对韵·一东》</span>',

 127: "    window.GUOXUE_COURSE_ID = '591-he-dui-han';",
 128: "    window.GUOXUE_COURSE_SUBJECT = 'liwengduiyun';",

 59: '<!-- 4. 河对汉，绿对红·两条河一对色 -->',
 61: '<!-- 5. 雨伯对雷公·两位天神 -->',
}

QUIZ_LINES = [
 "  {q: '1. 「河对汉」的「汉」指的是？', opts: ['汉水', '汉朝', '汉子'], ans: 0, exp: '汉指汉水'},",
 "  {q: '2. 「河对汉」中的「河」指的是？', opts: ['黄河', '小河', '银河'], ans: 0, exp: '河指黄河'},",
 "  {q: '3. 「绿对红」对的是什么？', opts: ['颜色', '花草', '衣服'], ans: 0, exp: '颜色对颜色'},",
 "  {q: '4. 「雨伯」是什么？', opts: ['管下雨的雨神', '下大雨的人', '一位诗人'], ans: 0, exp: '雨伯是雨神'},",
 "  {q: '5. 「雷公」管什么？', opts: ['打雷', '下雨', '刮风'], ans: 0, exp: '雷公是雷神'},",
 "  {q: '6. 「烟楼」是什么意思？', opts: ['烟雾里的楼阁', '烧烟的楼', '卖烟的店'], ans: 0, exp: '烟雾中的楼阁'},",
 "  {q: '7. 「月殿」是谁住的地方？', opts: ['嫦娥', '玉皇', '雷公'], ans: 0, exp: '月殿是嫦娥住处'},",
 "  {q: '8. 「天宫」是谁住的地方？', opts: ['玉皇', '嫦娥', '雨伯'], ans: 0, exp: '天宫是玉皇住处'},",
 "  {q: '9. 这一段句尾押韵的三个字是？', opts: ['红、公、宫', '汉、绿、红', '楼、洞、殿'], ans: 0, exp: '红公宫同属东韵'},",
 "  {q: '10. 这四句的对法有什么特别？', opts: ['从实的对到虚的，一直对到天上', '全写实物', '全写神仙'], ans: 0, exp: '由实到虚，越对越远'},",
]
for i, ln in enumerate(QUIZ_LINES):
    NEW[130 + i] = ln

if __name__ == "__main__":
    src = io.open(SRC, "r", encoding="utf-8", newline="").read().split("\n")
    buf = list(src)
    for no, txt in NEW.items():
        buf[no - 1] = txt
    out = "\n".join(buf)
    out = out.replace("590-lei-yin-yin", "591-he-dui-han")
    out = out.replace("yaoyue590", "yaoyue591")
    os.makedirs(DST_DIR, exist_ok=True)
    io.open(DST, "w", encoding="utf-8", newline="").write(out)
    print("written:", DST, "lines:", len(buf), "src lines:", len(src))
