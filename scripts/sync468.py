# -*- coding: utf-8 -*-
"""第 468 课五处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '468-xiao-ren-zhi-guo',
        num: '468',
        title: '小人之过也必文',
        subtitle: '有错就遮，越遮越丑',
        path: 'lessons/468-xiao-ren-zhi-guo/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·子张》第七章精讲：子夏曰：小人之过也必文。子夏说：小人有了过错，一定要加以掩饰。「文」读 wén，是掩饰、修饰。错不会因为遮住就消失，遮一层，错就多一层。认错不丢人，遮错才丢人。',
        status: 'ready',
        duration: '约 18 分钟',
        subject: 'zhangz',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/468-xiao-ren-zhi-guo/index.html</loc>
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
    n_count = s.count('共 467 课')
    n_v = s.count('zhangz467')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 467 课', '共 468 课').replace('zhangz467', 'zhangz468')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('467') >= 10, 'tests: 467 count=%d' % s.count('467')
    s = s.replace('467', '468')
    old_c = '子张=6、蒙学=1（合计 468）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '子张=7、蒙学=1（合计 468）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 6, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 7, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
