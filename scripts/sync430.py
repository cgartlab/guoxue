# -*- coding: utf-8 -*-
"""第 430 课四处清单同步 + 新开「阳货」门类（字节级替换，兼容 CRLF）。"""
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
        id: '430-yang-huo-yu-jian-kong-zi',
        num: '430',
        title: '阳货欲见孔子 · 躲不开的一场见面',
        subtitle: '日月逝矣，岁不我与',
        path: 'lessons/430-yang-huo-yu-jian-kong-zi/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·阳货》第一章精讲：阳货欲见孔子，孔子不见，归孔子豚。孔子时其亡也，而往拜之，遇诸涂。阳货拿话堵他：怀其宝而迷其邦，可谓仁乎？好从事而亟失时，可谓知乎？日月逝矣，岁不我与。孔子只答：诺，吾将仕矣。这一章讲的是躲不开的见面，和一个不硬顶的回答。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'yanghuo',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/430-yang-huo-yu-jian-kong-zi/index.html</loc>
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
    n_count = s.count('共 429 课')
    n_v = s.count('jishi429')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 429 课', '共 430 课').replace('jishi429', 'yanghuo430')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('429')
    assert n >= 10, 'tests: 429 count=%d' % n
    s = s.replace('429', '430')
    # 门类数 18 → 19（含新开的阳货）
    assert s.count('toHaveCount(18)') == 5, 'toHaveCount(18): %d' % s.count('toHaveCount(18)')
    s = s.replace('toHaveCount(18)', 'toHaveCount(19)')
    s = s.replace("'sidebar renders 18 ready categories", "'sidebar renders 19 ready categories")
    s = s.replace("(430/0/18)", "(430/0/19)")
    s = s.replace("expect(vals[2]).toBe('18'); // 学科门类", "expect(vals[2]).toBe('19'); // 学科门类")
    # 门类序号 01..19
    s = s.replace("'17', '18']);", "'17', '18', '19']);")
    # 门类标签：阳货插在蒙学之前（两处）
    old = "'卫灵公', '季氏', '蒙学']);"
    assert s.count(old) == 2, 'labelTexts: %d' % s.count(old)
    s = s.replace(old, "'卫灵公', '季氏', '阳货', '蒙学']);")
    # 组织 chip 数：季氏=14 之后加 阳货=1
    s = s.replace('季氏=14、蒙学=1（合计 430）', '季氏=14、阳货=1、蒙学=1（合计 430）')
    s = s.replace('46, 41, 14, 1]', '46, 41, 14, 1, 1]')
    assert '季氏=14、阳货=1' in s and '46, 41, 14, 1, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
