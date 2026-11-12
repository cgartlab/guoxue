# -*- coding: utf-8 -*-
"""第 424 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '424-xue-yu-bu-xue',
        num: '424',
        title: '学与不学 · 四等人，差在哪儿',
        subtitle: '生而知之，学而知之，困而学之，困而不学',
        path: 'lessons/424-xue-yu-bu-xue/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第九章精讲：生而知之者，上也；学而知之者，次也；困而学之，又其次也；困而不学，民斯为下矣。孔子按学不学分四等，顶上的那一等是理想，学而知之才是常路，只有困而不学才落到下等。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/424-xue-yu-bu-xue/index.html</loc>
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
    n_count = s.count('共 423 课')
    n_v = s.count('jishi423')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    s = s.replace('共 423 课', '共 424 课').replace('jishi423', 'jishi424')
    return s


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('423')
    assert n >= 10, 'tests: 423 count=%d' % n
    s = s.replace('423', '424')
    s = s.replace('季氏=8、蒙学=1', '季氏=9、蒙学=1')
    s = s.replace('46, 41, 8, 1]', '46, 41, 9, 1]')
    assert '季氏=9' in s and '46, 41, 9, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
