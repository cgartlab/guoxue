# -*- coding: utf-8 -*-
"""第 423 课四处清单同步（字节级替换，兼容 CRLF）。"""
import io
import os
import sys

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
        id: '423-jun-zi-you-san-wei',
        num: '423',
        title: '君子有三畏 · 怕该怕的',
        subtitle: '畏天命，畏大人，畏圣人之言',
        path: 'lessons/423-jun-zi-you-san-wei/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第八章精讲：君子有三畏。畏天命，畏大人，畏圣人之言。小人不知天命而不畏也，狎大人，侮圣人之言。孔子说君子心里有三样该敬的，小人正相反——该怕的不怕，该敬的不敬。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/423-jun-zi-you-san-wei/index.html</loc>
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
    n_count = s.count('共 422 课')
    n_v = s.count('jishi422')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    s = s.replace('共 422 课', '共 423 课').replace('jishi422', 'jishi423')
    return s


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('422')
    assert n >= 10, 'tests: 422 count=%d' % n
    s = s.replace('422', '423')
    s = s.replace('季氏=7、蒙学=1', '季氏=8、蒙学=1')
    s = s.replace('46, 41, 7, 1]', '46, 41, 8, 1]')
    assert '季氏=8' in s and '46, 41, 8, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
