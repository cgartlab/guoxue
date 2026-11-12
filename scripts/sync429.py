# -*- coding: utf-8 -*-
"""第 429 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '429-bang-jun-zhi-qi',
        num: '429',
        title: '邦君之妻 · 一个人，五种叫法',
        subtitle: '君称之曰夫人，夫人自称曰小童',
        path: 'lessons/429-bang-jun-zhi-qi/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第十四章精讲：邦君之妻，君称之曰夫人，夫人自称曰小童；邦人称之曰君夫人，称诸异邦曰寡小君；异邦人称之亦曰君夫人。国君的正妻，国君叫她夫人，她自己称小童，本国人叫君夫人，对别国叫寡小君，别国人也叫君夫人。一个人五种叫法，各有各的分寸，这就是名分。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/429-bang-jun-zhi-qi/index.html</loc>
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
    n_count = s.count('共 428 课')
    n_v = s.count('jishi428')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 428 课', '共 429 课').replace('jishi428', 'jishi429')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('428')
    assert n >= 10, 'tests: 428 count=%d' % n
    s = s.replace('428', '429')
    s = s.replace('季氏=13、蒙学=1', '季氏=14、蒙学=1')
    s = s.replace('46, 41, 13, 1]', '46, 41, 14, 1]')
    assert '季氏=14' in s and '46, 41, 14, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
