# -*- coding: utf-8 -*-
"""第 452 课四处清单同步 + 新开「微子」门类（字节级替换，兼容 CRLF）。"""
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
        id: '452-yin-you-san-ren-yan',
        num: '452',
        title: '殷有三仁焉',
        subtitle: '三个人的活法，一个仁字',
        path: 'lessons/452-yin-you-san-ren-yan/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·微子》第一章精讲：微子去之，箕子为之奴，比干谏而死。孔子曰：殷有三仁焉。同是一个烂摊子，一个走了，一个装疯忍下来，一个把命送了。三条路做法全不一样，孔子一个都没挑毛病——他认的是那颗不肯跟着坏的心。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'weizi',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/452-yin-you-san-ren-yan/index.html</loc>
    <lastmod>2026-11-13</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
"""

CAT_BLOCK = """    {
        key: 'weizi',
        label: '微子',
        num: '19',
        description: '《论语·微子篇》各章精讲',
        status: 'ready',
        order: 19
    },
    {
        key: 'mengxue',
        label: '蒙学',
        num: '20',
        description: '蒙学经典 · 三字经 · 百家姓 · 千字文',
        status: 'ready',
        order: 20
    }
];
"""


def categories(s):
    blk = """    {
        key: 'mengxue',
        label: '蒙学',
        num: '19',
        description: '蒙学经典 · 三字经 · 百家姓 · 千字文',
        status: 'ready',
        order: 19
    }
];
"""
    nl = "\r\n" if "\r\n" in s else "\n"
    blk = blk.replace("\n", nl)
    new = CAT_BLOCK.replace("\n", nl)
    assert s.count(blk) == 1, 'categories tail: %d' % s.count(blk)
    return s.replace(blk, new)


def manifest(s):
    tail = "    }\n];\n"
    assert s.count(tail) == 1, 'manifest tail not unique: %d' % s.count(tail)
    return s.replace(tail, ENTRY)


def index(s):
    n_count = s.count('共 451 课')
    n_v = s.count('yanghuo451')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 451 课', '共 452 课').replace('yanghuo451', 'weizi452')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('451') >= 10, 'tests: 451 count=%d' % s.count('451')
    s = s.replace('451', '452')
    # 门类数 19 → 20（含新开的微子）
    assert s.count('toHaveCount(19)') == 5, 'toHaveCount(19): %d' % s.count('toHaveCount(19)')
    s = s.replace('toHaveCount(19)', 'toHaveCount(20)')
    s = s.replace("'sidebar renders 19 ready categories", "'sidebar renders 20 ready categories")
    s = s.replace('(452/0/19)', '(452/0/20)')
    s = s.replace("expect(vals[2]).toBe('19'); // 学科门类", "expect(vals[2]).toBe('20'); // 学科门类")
    # 门类序号 01..20
    assert s.count("'17', '18', '19']);") == 1
    s = s.replace("'17', '18', '19']);", "'17', '18', '19', '20']);")
    # 门类标签：微子插在蒙学之前（两处）
    old = "'季氏', '阳货', '蒙学']);"
    assert s.count(old) == 2, 'labelTexts: %d' % s.count(old)
    s = s.replace(old, "'季氏', '阳货', '微子', '蒙学']);")
    # 组织 chip 数：阳货=22 之后加 微子=1
    old_c = '季氏=14、阳货=22、蒙学=1（合计 452）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '季氏=14、阳货=22、微子=1、蒙学=1（合计 452）')
    old_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    new_arr = '[2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 1, 1]'
    s = s.replace(old_arr, new_arr)
    assert new_arr in s
    return s


if __name__ == '__main__':
    rw('assets/data/categories.js', categories)
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
