# -*- coding: utf-8 -*-
"""第 466 课五处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '466-ri-zhi-qi-suo-wang',
        num: '466',
        title: '日知其所亡',
        subtitle: '天天学新的，月月别丢旧的',
        path: 'lessons/466-ri-zhi-qi-suo-wang/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·子张》第五章精讲：子夏曰：日知其所亡，月无忘其所能，可谓好学也已矣。子夏说：每天知道自己所没有学会的东西，每月不忘记已经学会的东西，这样就可以称得上好学了。「亡」通「无」读 wú，指还没学会的。天天进一点新的，月月守一点旧的，学问才留得住。学新如进账，温故如存钱。',
        status: 'ready',
        duration: '约 18 分钟',
        subject: 'zhangz',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/466-ri-zhi-qi-suo-wang/index.html</loc>
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
    n_count = s.count('共 465 课')
    n_v = s.count('zhangz465')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 465 课', '共 466 课').replace('zhangz465', 'zhangz466')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('465') >= 10, 'tests: 465 count=%d' % s.count('465')
    s = s.replace('465', '466')
    old_c = '子张=4、蒙学=1（合计 466）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '子张=5、蒙学=1（合计 466）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 4, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 5, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
