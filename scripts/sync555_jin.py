#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync555_jin: 555 课由《信·凡出言》更换为《谨·朝起早》——
替换 manifest 条目、sitemap 条目，移除旧课程目录。
课程总数不变（仍 555），tests、index.html 不需要改。付费课，unlock.js 不动。"""
import io, os, shutil, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [WARN] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:26]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True
SEP = "\r\n"

OLD_ENTRY = (
    "    {" + SEP +
    "        id: '555-fan-chu-yan'," + SEP +
    "        num: '555'," + SEP +
    "        title: '信为先 · 开口不撒谎（信门开篇）'," + SEP +
    "        subtitle: '《弟子规》信第一段：凡出言，信为先'," + SEP +
    "        path: 'lessons/555-fan-chu-yan/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十五课，信第一段（开篇）。原文「凡出言，信为先。诈与妄，奚可焉。」讲说话以守信为先：开口答应的事就要说到做到；骗人撒谎、瞎说胡说，怎么能行呢？上一门出则悌已收官，从这一课起开新的一门「信」。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'dizigui'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }"
)

NEW_ENTRY = (
    "    {" + SEP +
    "        id: '555-zhao-qi-zao'," + SEP +
    "        num: '555'," + SEP +
    "        title: '惜此时 · 早起勤盥洗（谨门开篇）'," + SEP +
    "        subtitle: '《弟子规》谨第一段：朝起早，夜眠迟'," + SEP +
    "        path: 'lessons/555-zhao-qi-zao/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十五课，谨第一段（开篇）。原文「朝起早，夜眠迟。老易至，惜此时。晨必盥，兼漱口。便溺回，辄净手。」讲作息与卫生：早上早起、晚上不过早贪睡，珍惜少年时光；起床要洗脸漱口，上完厕所要洗手。管好自己，从每天睁眼开始。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'dizigui'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }"
)

# ---------- 1) manifest（CRLF）：整条替换 ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
s, good = once(s, OLD_ENTRY, "manifest 555 条目", NEW_ENTRY)
ok = ok and good
if good:
    write(p, s); print("  [OK] manifest: 555 信 -> 谨")

# ---------- 2) index.html：课程总数不变，仅核对 ----------
p = f"{ROOT}/index.html"
s = read(p)
if "共 555 课" not in s:
    print("  [WARN] index: 未找到「共 555 课」，请人工检查"); ok = False
else:
    print("  [OK] index: 共 555 课 保持不变")

# ---------- 3) tests：课程总数不变，仅核对 ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if "toHaveCount(555)" not in s or "弟子规课堂=15（合计 555）" not in s:
    print("  [WARN] tests: 555 计数异常，请人工检查"); ok = False
else:
    print("  [OK] tests: 555 计数保持不变")

# ---------- 4) sitemap：替换 555 条目 ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
old_url = ("  <url>" + "\n" +
           "    <loc>https://guoxue.8023laozhanshi.cc/lessons/555-fan-chu-yan/index.html</loc>" + "\n")
new_url = ("  <url>" + "\n" +
           "    <loc>https://guoxue.8023laozhanshi.cc/lessons/555-zhao-qi-zao/index.html</loc>" + "\n")
s, good = once(s, old_url, "sitemap 555 条目", new_url)
ok = ok and good
if good:
    write(p, s); print("  [OK] sitemap: 555 loc 已替换")

# ---------- 5) 移除旧课程目录 ----------
old_dir = f"{ROOT}/lessons/555-fan-chu-yan"
if os.path.isdir(old_dir):
    shutil.rmtree(old_dir)
    print("  [OK] 旧目录 lessons/555-fan-chu-yan 已移除（信课内容可由 scripts/build555.py 重新生成）")
else:
    print("  [WARN] 旧目录不存在")

# ---------- 6) 残留检查 ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
if "555-fan-chu-yan" in s:
    print("  [WARN] manifest 仍有 555-fan-chu-yan 残留"); ok = False

print("=== sync555_jin 完成, 全部通过" if ok else "=== sync555_jin 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
