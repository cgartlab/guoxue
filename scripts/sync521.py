#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync521：把第 521 课同步到四处（manifest / index.html / tests / sitemap）。"""
import io

BASE = 'C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站'

# ---------- 1. lessons-manifest.js (CRLF) ----------
mp = f'{BASE}/assets/js/lessons-manifest.js'
s = io.open(mp, 'r', newline='').read()
SEP = '\r\n'
entry = (
    "        featured: false" + SEP +
    "    }," + SEP +
    "    {" + SEP +
    "        id: '521-guang-wu-xing'," + SEP +
    "        num: '521'," + SEP +
    "        title: '光武兴 · 为东汉'," + SEP +
    "        subtitle: '四百年，终于献；蜀魏吴，争汉鼎，号三国，迄两晋'," + SEP +
    "        path: 'lessons/521-guang-wu-xing/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《三字经》第二十八课精讲：光武兴，为东汉。四百年，终于献。蜀魏吴，争汉鼎。号三国，迄两晋。上一课讲了秦汉更替、王莽篡汉——西汉终结于新莽。这一课接着讲：汉光武帝刘秀兴起，建立东汉（为东汉）；汉朝延续约四百年，到汉献帝时终结（四百年，终于献）；蜀汉、曹魏、东吴三国鼎立，争夺天下（蜀魏吴，争汉鼎）；称为三国时代，到西晋东晋（号三国，迄两晋）。八句三言，讲完东汉中兴与终结、三国鼎立到两晋承继。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'sanzijing'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }" + SEP +
    "];"
)
old = "        featured: false" + SEP + "    }" + SEP + "];"
assert old in s, 'manifest old 未匹配'
s = s.replace(old, entry, 1)
io.open(mp, 'w', newline='').write(s)
print('manifest OK')

# ---------- 2. index.html (LF) ----------
ip = f'{BASE}/index.html'
s = io.open(ip, 'r', newline='').read()
assert '共 521 课' not in s
s = s.replace('共 520 课', '共 521 课')
s = s.replace('yaoyue520', 'yaoyue521')
io.open(ip, 'w', newline='').write(s)
print('index.html OK')

# ---------- 3. tests/homepage.spec.js (CRLF) ----------
tp = f'{BASE}/tests/homepage.spec.js'
s = io.open(tp, 'r', newline='').read()
assert '520' in s
s = s.replace('520', '521')                      # 所有课数引用
s = s.replace('三字经课堂=27', '三字经课堂=28')   # 注释 chip 计数
s = s.replace('27];', '28];')                      # expectedChipCounts 末项
io.open(tp, 'w', newline='').write(s)
print('tests OK')

# ---------- 4. sitemap.xml (LF) ----------
sp = f'{BASE}/sitemap.xml'
s = io.open(sp, 'r', newline='').read()
new_url = (
    "  <url>" + "\n" +
    "    <loc>https://guoxue.8023laozhanshi.cc/lessons/521-guang-wu-xing/index.html</loc>" + "\n" +
    "    <lastmod>2026-11-15</lastmod>" + "\n" +
    "    <changefreq>weekly</changefreq>" + "\n" +
    "    <priority>0.8</priority>" + "\n" +
    "  </url>" + "\n" +
    "</urlset>"
)
assert '</urlset>' in s
s = s.replace('</urlset>', new_url, 1)
io.open(sp, 'w', newline='').write(s)
print('sitemap OK')
print('ALL DONE')
