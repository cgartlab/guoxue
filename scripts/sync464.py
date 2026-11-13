# -*- coding: utf-8 -*-
"""第 464 课五处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '464-zun-xian-er-rong-zhong',
        num: '464',
        title: '尊贤而容众',
        subtitle: '该交的交，该容的容',
        path: 'lessons/464-zun-xian-er-rong-zhong/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·子张》第三章精讲：子夏之门人问交于子张。子夏教的是「可者与之，其不可者拒之」；子张说：君子尊贤而容众，嘉善而矜不能。我若是大贤，什么人容不下？我若不贤，别人先拒绝我，哪还轮得到我挑人。该交的交，该容的容。',
        status: 'ready',
        duration: '约 18 分钟',
        subject: 'zhangz',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/464-zun-xian-er-rong-zhong/index.html</loc>
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
    n_count = s.count('共 463 课')
    n_v = s.count('zhangz463')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 463 课', '共 464 课').replace('zhangz463', 'zhangz464')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('463') >= 10, 'tests: 463 count=%d' % s.count('463')
    s = s.replace('463', '464')
    old_c = '子张=2、蒙学=1（合计 464）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '子张=3、蒙学=1（合计 464）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 2, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 3, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
