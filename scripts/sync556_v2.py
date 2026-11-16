#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync556_v2: 556 课内容由「谨第二段后四句」补全为「谨第二段整段八句」——
仅替换 manifest 条目（标题、描述），课程总数/网址/课程 id 均不变，
tests、index.html、sitemap 不需要改。付费课，unlock.js 不动。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"
SEP = "\r\n"

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

OLD_ENTRY = (
    "    {" + SEP +
    "        id: '556-zhi-guan-fu'," + SEP +
    "        num: '556'," + SEP +
    "        title: '有定位 · 东西不乱放（谨第二段）'," + SEP +
    "        subtitle: '《弟子规》谨第二段：置冠服，有定位'," + SEP +
    "        path: 'lessons/556-zhi-guan-fu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十六课，谨第二段。原文「置冠服，有定位。勿乱顿，致污秽。」讲东西放好：帽子和衣服脱下来要放到固定的位置，不乱堆乱丢，免得弄脏弄坏。东西有自己的家，找起来快，也不会弄糟。'," + SEP +
    "        status: 'ready'," + SEP +
    "        duration: '约 15 分钟'," + SEP +
    "        subject: 'dizigui'," + SEP +
    "        tier: 'core'," + SEP +
    "        featured: false" + SEP +
    "    }"
)

NEW_ENTRY = (
    "    {" + SEP +
    "        id: '556-zhi-guan-fu'," + SEP +
    "        num: '556'," + SEP +
    "        title: '冠必正 · 穿戴整齐冠服归位（谨第二段）'," + SEP +
    "        subtitle: '《弟子规》谨第二段：冠必正，纽必结'," + SEP +
    "        path: 'lessons/556-zhi-guan-fu/index.html'," + SEP +
    "        grade: '小学低中年级'," + SEP +
    "        description: '《弟子规》第十六课，谨第二段。原文「冠必正，纽必结。袜与履，俱紧切。置冠服，有定位。勿乱顿，致污秽。」讲穿戴与归位：帽子戴正、纽扣系好，袜子和鞋穿得服帖；脱下来的冠服放到固定位置，不乱堆乱丢，免得弄脏弄坏。'," + SEP +
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
s, good = once(s, OLD_ENTRY, "manifest 556 条目", NEW_ENTRY)
ok = ok and good
if good:
    write(p, s); print("  [OK] manifest: 556 条目更新为八句整段")

# ---------- 2) index.html：仅核对 ----------
p = f"{ROOT}/index.html"
s = read(p)
if "共 556 课" not in s:
    print("  [WARN] index: 未找到「共 556 课」，请人工检查"); ok = False
else:
    print("  [OK] index: 共 556 课 保持不变")

# ---------- 3) tests：仅核对 ----------
p = f"{ROOT}/tests/homepage.spec.js"
s = read(p)
if "toHaveCount(556)" not in s or "弟子规课堂=16（合计 556）" not in s:
    print("  [WARN] tests: 556 计数异常，请人工检查"); ok = False
else:
    print("  [OK] tests: 556 计数保持不变")

# ---------- 4) sitemap：仅核对 ----------
p = f"{ROOT}/sitemap.xml"
s = read(p)
if "lessons/556-zhi-guan-fu/index.html" not in s:
    print("  [WARN] sitemap: 未找到 556 条目"); ok = False
else:
    print("  [OK] sitemap: 556 条目保持不变")

print("=== sync556_v2 完成, 全部通过" if ok else "=== sync556_v2 存在 WARN/失败 ===")
sys.exit(0 if ok else 1)
