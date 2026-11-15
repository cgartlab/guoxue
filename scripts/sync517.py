# -*- coding: utf-8 -*-
"""第 517 课：更新四处清单（manifest / index.html / tests / sitemap）。可重跑（已改则跳过）。"""
import os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read(p):
    with open(os.path.join(BASE, p), 'rb') as f:
        return f.read()
def write(p, b):
    with open(os.path.join(BASE, p), 'wb') as f:
        f.write(b)

# ---------- 1. manifest (CRLF) ----------
p = 'assets/js/lessons-manifest.js'
b = read(p).decode('utf-8')
if "'517-xia-you-yu'" not in b:
    NL = '\r\n'
    entry = (
        "featured: false" + NL +
        "    }," + NL +
        "    {" + NL +
        "        id: '517-xia-you-yu'," + NL +
        "        num: '517'," + NL +
        "        title: '夏有禹 · 商有汤'," + NL +
        "        subtitle: '周文武，称三王；夏传子，家天下，四百载，迁夏社'," + NL +
        "        path: 'lessons/517-xia-you-yu/index.html'," + NL +
        "        grade: '小学低中年级'," + NL +
        "        description: '《三字经》第二十四课精讲：夏有禹，商有汤。周文武，称三王。夏传子，家天下。四百载，迁夏社。上一课讲了「三皇二帝」的禅让盛世，这一课顺着读史往下讲——夏商周三代的开国之君禹、汤、文王武王被称为「三王」；大禹把天下传给儿子启，「家天下」从此开始，夏朝四百年后社稷迁移。八句短语（四句六言），讲完三代的开端与「家天下」的由来。'," + NL +
        "        status: 'ready'," + NL +
        "        duration: '约 15 分钟'," + NL +
        "        subject: 'sanzijing'," + NL +
        "        tier: 'core'," + NL +
        "        featured: false" + NL +
        "    }" + NL +
        "];"
    )
    b2, n = re.subn(r"featured: false[\r\n]+\s*\}[\r\n]+];", entry, b, count=1)
    assert n == 1, 'manifest 锚点未命中'
    write(p, b2.encode('utf-8'))
    print('manifest: +517 条目')
else:
    print('manifest: 517 已存在，跳过')

# ---------- 2. index.html (LF) ----------
p = 'index.html'
b = read(p).decode('utf-8')
if '共 516 课' in b:
    b = b.replace('共 516 课', '共 517 课')
    write(p, b.encode('utf-8'))
    print('index.html: 516->517')
else:
    print('index.html: 已为 517，跳过')

# ---------- 3. tests (CRLF) ----------
p = 'tests/homepage.spec.js'
b = read(p).decode('utf-8')
if '516' in b:
    b = b.replace('516', '517')
    b = b.replace('三字经课堂=23', '三字经课堂=24')
    b = b.replace(', 1, 23]', ', 1, 24]')
    write(p, b.encode('utf-8'))
    print('tests: 516->517, 三字经 23->24')
else:
    print('tests: 已为 517，跳过')

# ---------- 4. sitemap (LF) ----------
p = 'sitemap.xml'
b = read(p).decode('utf-8')
if '516-zi-xi-nong' not in b:
    block = (
        "  </url>\n"
        "  <url>\n"
        "    <loc>https://guoxue.8023laozhanshi.cc/lessons/516-zi-xi-nong/index.html</loc>\n"
        "    <lastmod>2026-11-15</lastmod>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>0.8</priority>\n"
        "  </url>\n"
        "  <url>\n"
        "    <loc>https://guoxue.8023laozhanshi.cc/lessons/517-xia-you-yu/index.html</loc>\n"
        "    <lastmod>2026-11-15</lastmod>\n"
        "    <changefreq>weekly</changefreq>\n"
        "    <priority>0.8</priority>\n"
        "  </url>\n"
        "</urlset>"
    )
    assert "  </url>\n</urlset>" in b, 'sitemap 锚点未命中'
    b = b.replace("  </url>\n</urlset>", block, 1)
    write(p, b.encode('utf-8'))
    print('sitemap: 补 516 + 加 517')
else:
    print('sitemap: 516 已存在，跳过')
print('ALL DONE')
