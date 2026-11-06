# -*- coding: utf-8 -*-
"""第275课原文排版第二版：按四轮问答分段，段内连排，字号放大"""
import re, io, os

GROUPS = [
"子zǐ路lù、曾zēng皙xī、冉rǎn有yǒu、公gōng西xī华huá侍shì坐zuò。子zǐ曰yuē：以yǐ吾wú一yī日rì长zhǎng乎hū尔ěr，毋wú吾wú以yǐ也yě。居jū则zé曰yuē：不bù吾wú知zhī也yě。如rú或huò知zhī尔ěr，则zé何hé以yǐ哉zāi？",
"子zǐ路lù率shuài尔ěr而ér对duì曰yuē：千qiān乘shèng之zhī国guó，摄shè乎hū大dà国guó之zhī间jiān，加jiā之zhī以yǐ师shī旅lǚ，因yīn之zhī以yǐ饥jī馑jǐn；由yóu也yě为wéi之zhī，比bǐ及jí三sān年nián，可kě使shǐ有yǒu勇yǒng，且qiě知zhī方fāng也yě。夫fū子zǐ哂shěn之zhī。求qiú！尔ěr何hé如rú？对duì曰yuē：方fāng六liù七qī十shí，如rú五wǔ六liù十shí，求qiú也yě为wéi之zhī，比bǐ及jí三sān年nián，可kě使shǐ足zú民mín。如rú其qí礼lǐ乐yuè，以yǐ俟sì君jūn子zǐ。",
"赤chì！尔ěr何hé如rú？对duì曰yuē：非fēi曰yuē能néng之zhī，愿yuàn学xué焉yān。宗zōng庙miào之zhī事shì，如rú会huì同tóng，端duān章zhāng甫fǔ，愿yuàn为wéi小xiǎo相xiàng焉yān。点diǎn！尔ěr何hé如rú？鼓gǔ瑟sè希xī，铿kēng尔ěr，舍shě瑟sè而ér作zuò，对duì曰yuē：异yì乎hū三sān子zǐ者zhě之zhī撰zhuàn。子zǐ曰yuē：何hé伤shāng乎hū？亦yì各gè言yán其qí志zhì也yě。",
"曰yuē：莫mù春chūn者zhě，春chūn服fú既jì成chéng，冠guàn者zhě五wǔ六liù人rén，童tóng子zǐ六liù七qī人rén，浴yù乎hū沂yí，风fēng乎hū舞wǔ雩yú，咏yǒng而ér归guī。夫fū子zǐ喟kuì然rán叹tàn曰yuē：吾wú与yǔ点diǎn也yě！三sān子zǐ者zhě出chū，曾zēng皙xī后hòu。曾zēng皙xī曰yuē：夫fú三sān子zǐ者zhě之zhī言yán何hé如rú？子zǐ曰yuē：亦yì各gè言yán其qí志zhì也yě已yǐ矣yǐ。曰yuē：夫fū子zǐ何hé哂shěn由yóu也yě？曰yuē：为wéi国guó以yǐ礼lǐ，其qí言yán不bù让ràng，是shì故gù哂shěn之zhī。唯wéi求qiú则zé非fēi邦bāng也yě与yú？安ān见jiàn方fāng六liù七qī十shí，如rú五wǔ六liù十shí，而ér非fēi邦bāng也yě者zhě？唯wéi赤chì则zé非fēi邦bāng也yě与yú？宗zōng庙miào会huì同tóng，非fēi诸zhū侯hóu而ér何hé？赤chì也yě为wéi之zhī小xiǎo，孰shú能néng为wéi之zhī大dà？",
]

PIN = "a-zāáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜü"
PAT = re.compile("([\u4e00-\u9fff])([" + PIN + "]+)")

def to_ruby(line):
    return PAT.sub(lambda m: '<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (m.group(1), m.group(2)), line)

html = "</p>\n<p style=\"margin:0 0 0.55em\">".join(to_ruby(g) for g in GROUPS)

p = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lessons", "275-shi-zuo-yan-zhi", "index.html"))
s = io.open(p, encoding="utf-8").read()
i = s.index('<p style="padding-top:0.1em')
j = s.index("</p>", i)
newp = '<p style="padding-top:0.1em;line-height:1.95;font-size:0.86rem;text-align:left;text-indent:0">' + html + "</p>"
s = s[:i] + newp + s[j + 4:]
io.open(p, "w", encoding="utf-8", newline="").write(s)

plain = re.sub("<[^>]+>", "", newp)
cjk = sum(1 for c in plain if "\u4e00" <= c <= "\u9fff")
print("汉字:", cjk, "ruby:", newp.count("<ruby"), "一致:", cjk == newp.count("<ruby"))
