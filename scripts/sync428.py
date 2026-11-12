# -*- coding: utf-8 -*-
"""第 428 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '428-chen-kang-wen-yu-bo-yu',
        num: '428',
        title: '陈亢问于伯鱼 · 问一句，得三样',
        subtitle: '不学诗，无以言；不学礼，无以立',
        path: 'lessons/428-chen-kang-wen-yu-bo-yu/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·季氏》第十三章精讲：陈亢问于伯鱼曰：子亦有异闻乎？对曰：未也。尝独立，鲤趋而过庭。曰：学诗乎？不学诗，无以言。不学礼，无以立。陈亢退而喜曰：问一得三，闻诗，闻礼，又闻君子之远其子也。陈亢以为老师的儿子有私房话，结果发现孔子教儿子跟教学生一样。学诗才会说话，学礼才站得住，好家教不偏私。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'jishi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/428-chen-kang-wen-yu-bo-yu/index.html</loc>
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
    n_count = s.count('共 427 课')
    n_v = s.count('jishi427')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 427 课', '共 428 课').replace('jishi427', 'jishi428')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    n = s.count('427')
    assert n >= 10, 'tests: 427 count=%d' % n
    s = s.replace('427', '428')
    s = s.replace('季氏=12、蒙学=1', '季氏=13、蒙学=1')
    s = s.replace('46, 41, 12, 1]', '46, 41, 13, 1]')
    assert '季氏=13' in s and '46, 41, 13, 1]' in s
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
