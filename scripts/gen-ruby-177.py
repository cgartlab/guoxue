# -*- coding: utf-8 -*-
"""生成 177 课原文 ruby 标注"""
import re

lines = [
    ("曾子有疾，孟敬子问之。",
     "zēng zǐ yǒu jí, mèng jìng zǐ wèn zhī."),
    ("曾子言曰：鸟之将死，其鸣也哀；人之将死，其言也善。",
     "zēng zǐ yán yuē: niǎo zhī jiāng sǐ, qí míng yě āi; rén zhī jiāng sǐ, qí yán yě shàn."),
    ("君子所贵乎道者三：动容貌，斯远暴慢矣；正颜色，斯近信矣；出辞气，斯远鄙倍矣。",
     "jūn zǐ suǒ guì hū dào zhě sān: dòng róng mào, sī yuǎn bào màn yǐ; zhèng yán sè, sī jìn xìn yǐ; chū cí qì, sī yuǎn bǐ bèi yǐ."),
    ("笾豆之事，则有司存。",
     "biān dòu zhī shì, zé yǒu sī cún."),
]


def han(ch):
    return '\u4e00' <= ch <= '\u9fff'


out = []
for text, py in lines:
    pys = [p for p in re.split(r'[\s,;:.!?]+', py) if p]
    chars = [c for c in text if han(c)]
    assert len(pys) == len(chars), (len(pys), len(chars), text, pys)
    pi = 0
    buf = []
    for c in text:
        if han(c):
            buf.append('<ruby lang="zh-Hans">%s<rt>%s</rt></ruby>' % (c, pys[pi]))
            pi += 1
        else:
            buf.append(c)
    out.append(''.join(buf))

print('\n'.join(out))
