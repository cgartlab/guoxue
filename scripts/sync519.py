import io

C = '\r\n'  # manifest & tests: CRLF
L = '\n'    # index.html & sitemap: LF

# ---------- 1. manifest (CRLF) ----------
m = io.open('assets/js/lessons-manifest.js', 'r', newline='').read()
assert '519-zhou-che-dong' not in m, '519 already in manifest'
old_tail = "        featured: false" + C + "    }" + C + "];"
entry = (
    "        featured: false" + C +
    "    }," + C +
    "    {" + C +
    "        id: '519-zhou-che-dong'," + C +
    "        num: '519'," + C +
    "        title: '周辙东 · 王纲坠'," + C +
    "        subtitle: '逞干戈，尚游说；始春秋，终战国，五霸强，七雄出'," + C +
    "        path: 'lessons/519-zhou-che-dong/index.html'," + C +
    "        grade: '小学低中年级'," + C +
    "        description: '《三字经》第二十六课精讲：周辙东，王纲坠。逞干戈，尚游说。始春秋，终战国。五霸强，七雄出。上一课讲了周朝八百年最长久——西周礼乐征伐自天子出。这一课接着讲：周平王东迁洛邑（辙东），王室衰微、纲纪坠落（王纲坠）；诸侯逞强动干戈、游说之士盛行（逞干戈，尚游说）；历史进入春秋（始春秋）到战国（终战国）；春秋五霸强盛（五霸强），战国七雄并出（七雄出）。八句六言，讲完东周衰微与春秋战国的乱象。'," + C +
    "        status: 'ready'," + C +
    "        duration: '约 15 分钟'," + C +
    "        subject: 'sanzijing'," + C +
    "        tier: 'core'," + C +
    "        featured: false" + C +
    "    }" + C +
    "];"
)
assert old_tail in m, 'manifest tail pattern not found'
m = m.replace(old_tail, entry, 1)
io.open('assets/js/lessons-manifest.js', 'w', newline='').write(m)
print('manifest: 519 条目已插入')

# ---------- 2. index.html (LF) ----------
ix = io.open('index.html', 'r', newline='').read()
assert '519' not in ix.replace('yaoyue519', ''), 'unexpected 519 in index.html'
ix = ix.replace('518', '519')  # yaoyue518->yaoyue519, 共 518 课->共 519 课
io.open('index.html', 'w', newline='').write(ix)
print('index.html: 共518->519, yaoyue518->yaoyue519')

# ---------- 3. tests (CRLF) ----------
t = io.open('tests/homepage.spec.js', 'r', newline='').read()
t = t.replace('518', '519')            # 注释 + 所有计数 toHaveCount(518)->519, chips.last toHaveText('519')
t = t.replace('8, 1, 25]', '8, 1, 26]')   # expectedChipCounts 末项 三字经课堂 25->26
t = t.replace('三字经课堂=25', '三字经课堂=26')  # 注释 chip 数
io.open('tests/homepage.spec.js', 'w', newline='').write(t)
print('tests: 518->519, 三字经 chip 25->26')

# ---------- 4. sitemap (LF) ----------
s = io.open('sitemap.xml', 'r', newline='').read()
assert '519-zhou-che-dong' not in s, '519 already in sitemap'
newurl = (
    "  <url>" + L +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/519-zhou-che-dong/index.html</loc>" + L +
    "    <lastmod>2026-11-15</lastmod>" + L +
    "    <changefreq>weekly</changefreq>" + L +
    "    <priority>0.8</priority>" + L +
    "  </url>" + L
)
assert '</urlset>' in s, 'urlset close not found'
s = s.replace('</urlset>', newurl + '</urlset>', 1)
io.open('sitemap.xml', 'w', newline='').write(s)
print('sitemap: 519 条目已插入')
print('DONE')
