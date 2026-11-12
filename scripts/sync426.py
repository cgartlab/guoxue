# -*- coding: utf-8 -*-
"""第 426 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '426-jian-shan-ru-bu-ji',
        num: '426',
        title: '见善如不及 · 学好要急，避恶要快',
        subtitle: '见善如不及，见不善如探汤',
        path: 'lessons/426-jian-shan-ru-bu-ji/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第十一章精讲：见善如不及，见不善如探汤。见到好人好事，像赶不上一样急着去学；见到坏事，像手伸进滚水一样马上缩回。后段隐居以求其志、行义以达其道，孔子坦言这话听过，做到的人却没见过。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/426-jian-shan-ru-bu-ji/index.html</loc>
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
    n_count = s.count('共 425 课')
    n_v = s.count('jishi425')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 425 课', '共 426 课').replace('jishi425', 'jishi426')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('425')
    assert n >= 10, 'tests: 425 count=%d' % n
    s = s.replace('425', '426')
    s = s.replace('季氏=10、蒙学=1', '季氏=11、蒙学=1')
    s = s.replace('46, 41, 10, 1]', '46, 41, 11, 1]')
    assert '季氏=11' in s and '46, 41, 11, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
