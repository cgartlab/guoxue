# -*- coding: utf-8 -*-
import io, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def read_text(p):
    with io.open(p, 'r', newline='') as f:
        return f.read()

def write_text(p, s):
    with io.open(p, 'w', newline='') as f:
        f.write(s)

def sep_of(s):
    return '\r\n' if '\r\n' in s else '\n'

def patch(p, repls, label):
    s = read_text(p)
    sep = sep_of(s)
    for old, new in repls:
        # 若 old 含占位符 {SEP} 则替换为该文件换行符
        old2 = old.replace('{SEP}', sep)
        new2 = new.replace('{SEP}', sep)
        if old2 not in s:
            sys.stderr.write('!! [%s] NOT FOUND:\n%s\n\n' % (label, old2[:160]))
            sys.exit(1)
        s = s.replace(old2, new2)
    write_text(p, s)
    sys.stderr.write('OK [%s] (%d bytes)\n' % (label, len(s)))

# 1) manifest (CRLF)
manifest = os.path.join(BASE, 'assets', 'js', 'lessons-manifest.js')
m_repls = [
    (
        "        featured: false{SEP}    }{SEP}];",
        "        featured: false{SEP}    },{SEP}    {{SEP}"
        "        id: '518-tang-fa-xia',{SEP}"
        "        num: '518',{SEP}"
        "        title: '汤伐夏 · 国号商',{SEP}"
        "        subtitle: '六百载，至纣亡',{SEP}"
        "        path: 'lessons/518-tang-fa-xia/index.html',{SEP}"
        "        grade: '小学低中年级',{SEP}"
        "        description: '《三字经》第二十五课精讲：汤伐夏，国号商。六百载，至纣亡。上一课讲了「家天下」——夏朝延续四百年后社稷迁移，亡于桀。这一课接着讲：商汤起兵讨伐夏桀，建立商朝；商朝历经约六百年，到纣王时灭亡。四句六言，讲完商朝的兴起与终结。',{SEP}"
        "        status: 'ready',{SEP}"
        "        duration: '约 15 分钟',{SEP}"
        "        subject: 'sanzijing',{SEP}"
        "        tier: 'core',{SEP}"
        "        featured: false{SEP}"
        "    }{SEP}];"
    ),
]
patch(manifest, m_repls, 'manifest')

# 2) index.html (lf) —— 全局缓存串 + 共N课
idx = os.path.join(BASE, 'index.html')
i_repls = [
    ('共 517 课', '共 518 课'),
    ('yaoyue517', 'yaoyue518'),
]
patch(idx, i_repls, 'index')

# 3) tests (lf) —— 517->518 全局 + chip 末项 24->25 + 注释
tst = os.path.join(BASE, 'tests', 'homepage.spec.js')
t_repls = [
    ('517', '518'),
    ('三字经课堂=24', '三字经课堂=25'),
    ('const expectedChipCounts = [2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 24];',
     'const expectedChipCounts = [2, 16, 24, 26, 26, 28, 30, 20, 21, 30, 26, 25, 23, 30, 46, 41, 14, 22, 10, 24, 8, 1, 25];'),
]
patch(tst, t_repls, 'tests')

# 4) sitemap (lf) —— 在 517 块后插入 518 块
sm = os.path.join(BASE, 'sitemap.xml')
s_repls = [
    (
        "    <loc>https://guoxue.8023laozhanshi.cc/lessons/517-xia-you-yu/index.html</loc>{SEP}"
        "    <lastmod>2026-11-15</lastmod>{SEP}"
        "    <changefreq>weekly</changefreq>{SEP}"
        "    <priority>0.8</priority>{SEP}"
        "  </url>{SEP}"
        "</urlset>",
        "    <loc>https://guoxue.8023laozhanshi.cc/lessons/517-xia-you-yu/index.html</loc>{SEP}"
        "    <lastmod>2026-11-15</lastmod>{SEP}"
        "    <changefreq>weekly</changefreq>{SEP}"
        "    <priority>0.8</priority>{SEP}"
        "  </url>{SEP}"
        "  <url>{SEP}"
        "    <loc>https://guoxue.8023laozhanshi.cc/lessons/518-tang-fa-xia/index.html</loc>{SEP}"
        "    <lastmod>2026-11-15</lastmod>{SEP}"
        "    <changefreq>weekly</changefreq>{SEP}"
        "    <priority>0.8</priority>{SEP}"
        "  </url>{SEP}"
        "</urlset>",
    ),
]
patch(sm, s_repls, 'sitemap')

# 校验
checks = [
    (manifest, "518-tang-fa-xia"),
    (idx, "共 518 课"),
    (idx, "yaoyue518"),
    (tst, "toHaveText('518')"),
    (sm, "518-tang-fa-xia/index.html"),
]
for p, token in checks:
    if token not in read_text(p):
        sys.stderr.write('!! verify FAIL: %s missing %s\n' % (p, token))
        sys.exit(3)
sys.stderr.write('ALL CHECKS PASSED\n')
