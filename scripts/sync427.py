# -*- coding: utf-8 -*-
"""第 427 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '427-qi-jing-gong-you-ma-qian-si',
        num: '427',
        title: '齐景公有马千驷 · 有钱没念想，饿死有人记',
        subtitle: '齐景公有马千驷，死之日，民无德而称焉',
        path: 'lessons/427-qi-jing-gong-you-ma-qian-si/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第十二章精讲：齐景公有马千驷，死之日，民无德而称焉。伯夷、叔齐饿于首阳之下，民到于今称之。齐景公富到四千匹马，死了没人念他好；伯夷叔齐饿死在山下，百姓到今天还称赞。孔子比的不是钱，是人留下什么。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/427-qi-jing-gong-you-ma-qian-si/index.html</loc>
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
    n_count = s.count('共 426 课')
    n_v = s.count('jishi426')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 426 课', '共 427 课').replace('jishi426', 'jishi427')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('426')
    assert n >= 10, 'tests: 426 count=%d' % n
    s = s.replace('426', '427')
    s = s.replace('季氏=11、蒙学=1', '季氏=12、蒙学=1')
    s = s.replace('46, 41, 11, 1]', '46, 41, 12, 1]')
    assert '季氏=12' in s and '46, 41, 12, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
