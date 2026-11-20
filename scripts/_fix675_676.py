# -*- coding: utf-8 -*-
"""修正675/676两课出处：原文属《笠翁对韵》下卷十一真其一，误标为《声律启蒙》。"""
import io, os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SUBS_LESSON = [
    ('见《声律启蒙》上卷十一真第一段前六句。', '见《笠翁对韵》下卷十一真第一段前六句。'),
    ('见《声律启蒙》上卷十一真第一段后四句，接675课。', '见《笠翁对韵》下卷十一真第一段后四句，接675课。'),
    ('《声律启蒙》十一真（第一段前六句）。', '《笠翁对韵》十一真（第一段前六句）。'),
    ('《声律启蒙》十一真（第一段后四句）。', '《笠翁对韵》十一真（第一段后四句）。'),
    ('声律启蒙 · 十一真》', '笠翁对韵 · 十一真》'),
]

def patch(path, subs, expect_absent='声律启蒙上卷十一真'):
    p = os.path.join(root, path)
    s = io.open(p, encoding='utf-8', newline='').read()
    hit = 0
    for old, new in subs:
        if old in s:
            s = s.replace(old, new)
            hit += 1
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    left = s.count('声律启蒙')
    print('%-40s 替换 %d 处，剩余「声律启蒙」%d 处' % (path, hit, left))
    return left

l1 = patch('lessons/675-lian-dui-ju/index.html', SUBS_LESSON)
l2 = patch('lessons/676-luo-yue-sou/index.html', SUBS_LESSON)
assert l1 == 0 and l2 == 0, '课件仍残留声律启蒙'

# manifest 两条 description
p = os.path.join(root, 'assets/js/lessons-manifest.js')
s = io.open(p, encoding='utf-8', newline='').read()
old = '接674课，同属《声律启蒙》十一真第一段。'
new = '接674课，同属《笠翁对韵》下卷十一真第一段。'
assert old in s
s = s.replace(old, new)
old2 = '接675课，同属《声律启蒙》十一真第一段。'
new2 = '接675课，同属《笠翁对韵》下卷十一真第一段。'
assert old2 in s
s = s.replace(old2, new2)
io.open(p, 'w', encoding='utf-8', newline='').write(s)
print('manifest 改 2 条，剩余「声律启蒙」%d 处（应为 3：672/673/674 正当引用）' % s.count('声律启蒙'))
