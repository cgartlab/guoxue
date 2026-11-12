# -*- coding: utf-8 -*-
"""第 425 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '425-jun-zi-you-jiu-si',
        num: '425',
        title: '君子有九思 · 起念之前，先想一想',
        subtitle: '视思明，听思聪，色思温，貌思恭，言思忠，事思敬',
        path: 'lessons/425-jun-zi-you-jiu-si/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第十章精讲：君子有九思。视思明，听思聪，色思温，貌思恭，言思忠，事思敬，疑思问，忿思难，见得思义。孔子说君子在九个地方都要先过一遍心，九条路一个理——别急着来，先想一想。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/425-jun-zi-you-jiu-si/index.html</loc>
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
    n_count = s.count('共 424 课')
    n_v = s.count('jishi424')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 424 课', '共 425 课').replace('jishi424', 'jishi425')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('424')
    assert n >= 10, 'tests: 424 count=%d' % n
    s = s.replace('424', '425')
    s = s.replace('季氏=9、蒙学=1', '季氏=10、蒙学=1')
    s = s.replace('46, 41, 9, 1]', '46, 41, 10, 1]')
    assert '季氏=10' in s and '46, 41, 10, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
