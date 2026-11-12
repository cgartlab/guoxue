# -*- coding: utf-8 -*-
"""第 431 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '431-xing-xiang-jin-xi-xiang-yuan',
        num: '431',
        title: '性相近也，习相远也 · 天生的差不多，后来的差很多',
        subtitle: '起点差不多，路自己走',
        path: 'lessons/431-xing-xiang-jin-xi-xiang-yuan/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·阳货》第二章精讲：子曰，性相近也，习相远也。人的天性是相近的，后来习惯不同，就相差很远了。这一句只有十个字，却讲清了人的差别从哪儿来：起点差不多，差距靠后天攒。全篇最短的一章，讲人的同与不同。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'yanghuo',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/431-xing-xiang-jin-xi-xiang-yuan/index.html</loc>
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
    n_count = s.count('共 430 课')
    n_v = s.count('yanghuo430')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 430 课', '共 431 课').replace('yanghuo430', 'yanghuo431')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('430') >= 10, 'tests: 430 count=%d' % s.count('430')
    # 阳货 chip 1 → 2，合计 430 → 431
    old_c = '季氏=14、阳货=1、蒙学=1（合计 430）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '季氏=14、阳货=2、蒙学=1（合计 431）')
    old_arr = '46, 41, 14, 1, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    s = s.replace(old_arr, '46, 41, 14, 2, 1]')
    assert '46, 41, 14, 2, 1]' in s
    # 其余 430 → 431
    s = s.replace('430', '431')
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
