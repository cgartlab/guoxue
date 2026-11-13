# -*- coding: utf-8 -*-
"""第 470 课五处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '470-xin-er-hou-lao-qi-min',
        num: '470',
        title: '信而后劳其民',
        subtitle: '先让人信你，再让人听你',
        path: 'lessons/470-xin-er-hou-lao-qi-min/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·子张》第九章精讲：子夏曰：君子信而后劳其民；未信，则以为厉己也。信而后谏；未信，则以为谤己也。要先取得信任，再派活、再劝谏；没取得信任就动手，人家以为你在坑他、在毁他。「厉」在这里是折磨，「谏」是下级劝上级。',
        status: 'ready',
        duration: '约 18 分钟',
        subject: 'zhangz',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/470-xin-er-hou-lao-qi-min/index.html</loc>
    <lastmod>2026-11-13</lastmod>
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
    n_count = s.count('共 469 课')
    n_v = s.count('zhangz469')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 469 课', '共 470 课').replace('zhangz469', 'zhangz470')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('469') >= 10, 'tests: 469 count=%d' % s.count('469')
    s = s.replace('469', '470')
    old_c = '子张=8、蒙学=1（合计 470）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '子张=9、蒙学=1（合计 470）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 8, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 9, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
