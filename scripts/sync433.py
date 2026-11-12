# -*- coding: utf-8 -*-
"""第 433 课四处清单同步（字节级替换，兼容 CRLF）。"""
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
        id: '433-zi-zhi-wu-cheng',
        num: '433',
        title: '子之武城 · 小地方也配讲礼乐',
        subtitle: '小地方也配讲礼乐',
        path: 'lessons/433-zi-zhi-wu-cheng/index.html',
        grade: '小学高年级·初中文言',
        description: '《论语·阳货》第四章精讲：子之武城，闻弦歌之声。孔子到武城，听见弹琴唱歌，笑着说「割鸡焉用牛刀」；学生子游拿老师自己的话回他，孔子当场认了——前言戏之耳。讲的是礼乐教化不分地方大小，说错了也要认。',
        status: 'ready',
        duration: '约 15 分钟',
        subject: 'yanghuo',
        tier: 'core',
        featured: false
    }
];
"""

URL_BLOCK = """  <url>
    <loc>https://guoxue.8023laozhanshi.cc/lessons/433-zi-zhi-wu-cheng/index.html</loc>
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
    n_count = s.count('共 432 课')
    n_v = s.count('yanghuo432')
    assert n_count == 1 and n_v == 9, 'index: count=%d v=%d' % (n_count, n_v)
    return s.replace('共 432 课', '共 433 课').replace('yanghuo432', 'yanghuo433')


def sitemap(s):
    assert s.count('</urlset>') == 1
    return s.replace('</urlset>', URL_BLOCK)


def tests(s):
    assert s.count('432') >= 10, 'tests: 432 count=%d' % s.count('432')
    old_c = '季氏=14、阳货=3、蒙学=1（合计 432）'
    assert s.count(old_c) == 1, 'chip comment: %d' % s.count(old_c)
    s = s.replace(old_c, '季氏=14、阳货=4、蒙学=1（合计 433）')
    old_arr = '46, 41, 14, 3, 1]'
    assert s.count(old_arr) == 1, 'chip arr: %d' % s.count(old_arr)
    s = s.replace(old_arr, '46, 41, 14, 4, 1]')
    assert '46, 41, 14, 4, 1]' in s
    s = s.replace('432', '433')
    return s


if __name__ == '__main__':
    rw('assets/js/lessons-manifest.js', manifest)
    rw('index.html', index)
    rw('sitemap.xml', sitemap)
    rw('tests/homepage.spec.js', tests)
    print('done')
