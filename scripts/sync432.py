# -*- coding: utf-8 -*-
"""第 432 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '432-wei-shang-zhi-yu-xia-yu-bu-yi',
        num: '432',
        title: '唯上知与下愚不移 · 两头改不动，中间靠教养',
        subtitle: '中间靠教养',
        path: 'lessons/432-wei-shang-zhi-yu-xia-yu-bu-yi/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·阳货》第三章精讲：子曰，唯上知与下愚不移。只有最聪明的人和最不开窍的人，是教也改不动的。上一章说性相近、习相远，这一句补上两个极端：中间大多数人都靠后天。全章只有十个字，讲的是教育到底对谁有用。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'yanghuo',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/432-wei-shang-zhi-yu-xia-yu-bu-yi/index.html</loc>
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
    n_count = s.count('共 431 课')
    n_v = s.count('yanghuo431')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 431 课', '共 432 课').replace('yanghuo431', 'yanghuo432')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('431') >= 10, 'tests: 431 count=%d' % s.count('431')
    old_c = '季氏=14、阳货=2、蒙学=1（合计 431）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '季氏=14、阳货=3、蒙学=1（合计 432）')
    old_arr = '46, 41, 14, 2, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    s = s.replace(old_arr, '46, 41, 14, 3, 1]')
    assert '46, 41, 14, 3, 1]' in s
    s = s.replace('431', '432')
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
