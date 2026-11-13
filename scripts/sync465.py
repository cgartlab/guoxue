# -*- coding: utf-8 -*-
"""第 465 课五处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '465-zhi-yuan-kong-ni',
        num: '465',
        title: '致远恐泥',
        subtitle: '小处有可观，大处要走远',
        path: 'lessons/465-zhi-yuan-kong-ni/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·子张》第四章精讲：子夏曰：虽小道，必有可观者焉；致远恐泥，是以君子不为也。子夏说：哪怕是小的技艺，也一定有它值得看的地方；但要拿它去走远路、成大事，怕就怕陷在里面出不来，所以君子不把心思放在小道上。小处有可观，大处要走远。',
        status: 'ready',
        duration: '约 18 分钟',
        subject: 'zhangz',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/465-zhi-yuan-kong-ni/index.html</loc>
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
    n_count = s.count('共 464 课')
    n_v = s.count('zhangz464')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 464 课', '共 465 课').replace('zhangz464', 'zhangz465')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('464') >= 10, 'tests: 463 count=%d' % s.count('464')
    s = s.replace('464', '465')
    old_c = '子张=3、蒙学=1（合计 465）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '子张=4、蒙学=1（合计 465）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 3, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 4, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
