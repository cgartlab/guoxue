# -*- coding: utf-8 -*-
"""第 434 课四处清单同步（字节级替换，兼容 CRLF）。"""
import io
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def rw(rel, fn):
    path = os.path.join(ROOT, rel)
    with io.open(path, 'r', encoding='utf-8', newline='') as f:
        src = f.read()
    out = fn(src)
    assert out != src, 'no change: ' + rel
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(out)
    print('ok', rel)


ENTRY = """    },
    {
        id: '434-gong-shan-fu-rao-yi-fei-pan',
        num: '434',
        title: '公山弗扰以费畔 · 有个地方用我，我就去',
        subtitle: '有个地方用我，我就去',
        path: 'lessons/434-gong-shan-fu-rao-yi-fei-pan/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·阳货》第五章精讲：公山弗扰以费畔，召，子欲往。叛臣来请，孔子动了心；子路不高兴，说没地方去就算了，何必去他那儿。孔子答：肯召我的人，难道是白召？真有人用我，我就在东方把周道做起来。讲的是想做事的心，和护名声的理。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'yanghuo',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/434-gong-shan-fu-rao-yi-fei-pan/index.html</loc>
    <lastmod>2026-11-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
"""


def manifest(s):
    tail = "    }\n];\n"
    assert s.count(tail) == 1, 'manifest tail not unique: %d' % s.count(tail)
    return s.replace(tail, ENTRY)


def index(s):
    n_count = s.count('共 433 课')
    n_v = s.count('yanghuo433')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    s = s.replace('共 433 课', '共 434 课').replace('yanghuo433', 'yanghuo434')
    old_desc = '卫灵公 · 季氏篇目精讲'
    assert s.count(old_desc) == 1, 'index desc: %d' % s.count(old_desc)
    return s.replace(old_desc, '卫灵公 · 季氏 · 阳货篇目精讲')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('433') >= 10, 'tests: 433 count=%d' % s.count('433')
    old_c = '季氏=14、阳货=4、蒙学=1（合计 433）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '季氏=14、阳货=5、蒙学=1（合计 434）')
    old_arr = '46, 41, 14, 4, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    s = s.replace(old_arr, '46, 41, 14, 5, 1]')
    assert '46, 41, 14, 5, 1]' in s
    s = s.replace('433', '434')
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
