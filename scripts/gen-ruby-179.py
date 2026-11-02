# -*- coding: utf-8 -*-
"""生成 179 课原文 ruby 标注"""
import re

lines = [
    ("曾子曰：可以托六尺之孤，可以寄百里之命，临大节而不可夺也。君子人与？君子人也。",
     "zēng zǐ yuē: kě yǐ tuō liù chǐ zhī gū, kě yǐ jì bǎi lǐ zhī mìng, lín dà jié ér bù kě duó yě. jūn zǐ rén yú? jūn zǐ rén yě."),
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
