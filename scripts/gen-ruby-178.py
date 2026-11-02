# -*- coding: utf-8 -*-
"""生成 178 课原文 ruby 标注"""
import re

lines = [
    ("曾子曰：以能问于不能，以多问于寡；有若无，实若虚，犯而不校。昔者吾友尝从事于斯矣。",
     "zēng zǐ yuē: yǐ néng wèn yú bù néng, yǐ duō wèn yú guǎ; yǒu ruò wú, shí ruò xū, fàn ér bù jiào. xī zhě wú yǒu cháng cóng shì yú sī yǐ."),
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
