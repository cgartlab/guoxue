#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""sync558_v2: 558 课重做为《年方少，勿饮酒》八句版后，
仅更新 manifest 中 558 条目的 title/subtitle/description（其余四处 558 已同步，无需再动）。"""
import io, sys

ROOT = "C:/Users/Chenzhigang/WorkBuddy/国学课堂/网站"

def read(p):
    return io.open(p, "r", encoding="utf-8", newline="").read()

def write(p, s):
    io.open(p, "w", encoding="utf-8", newline="").write(s)

def once(s, sub, where, repl):
    n = s.count(sub)
    if n != 1:
        print(f"  [FAIL] {where}: 期望 1 次, 实际 {n} 次 -> '{sub[:40]}'")
        return s, False
    return s.replace(sub, repl), True

ok = True

# ---------- manifest：更新 558 条目三个字段 ----------
p = f"{ROOT}/assets/js/lessons-manifest.js"
s = read(p)
s, g1 = once(s, "        title: '步从容 · 站走坐卧要端正（谨第四段）',", "manifest title",
             "        title: '年方少 · 不贪杯，站走端正（谨第四段）',")
s, g2 = once(s, "        subtitle: '《弟子规》谨第四段：步从容，立端正',", "manifest subtitle",
             "        subtitle: '《弟子规》谨第四段：年方少，勿饮酒',")
old_desc = ("        description: '《弟子规》第十八课，谨第四段。原文「步从容，立端正。揖深圆，拜恭敬。"
            "勿践阈，勿跛倚。勿箕踞，勿摇髀。」讲站走坐卧的姿势：走路从容、站得端正，作揖要深圆、"
            "行礼要恭敬；不踩门槛、不斜靠墙、不叉腿坐、不抖腿。',")
new_desc = ("        description: '《弟子规》第十八课，谨第四段。原文「年方少，勿饮酒。饮酒醉，最为丑。"
            "步从容，立端正。揖深圆，拜恭敬。」前四句讲小孩子不喝酒，喝醉了样子最难看；后四句讲走路从容、"
            "站得端正，作揖要深圆、行礼要恭敬。管住嘴，立起身。',")
s, g3 = once(s, old_desc, "manifest description", new_desc)
ok = ok and (g1 and g2 and g3)
if ok:
    write(p, s); print("  [OK] manifest: 558 条目 title/subtitle/description 已更新")

# ---------- 其余四处复核（不应有变化） ----------
idx = read(f"{ROOT}/index.html")
assert "共 558 课" in idx and "yaoyue558" in idx, "index 558 标记缺失"
assert "558-bu-cong-rong" in read(f"{ROOT}/sitemap.xml"), "sitemap 558 缺失"
t = read(f"{ROOT}/tests/homepage.spec.js")
assert "558" in t and "557" not in t.replace("558", "").replace("557", "557"), "tests 可疑"
print("  [OK] index/sitemap/tests 复核通过（本次无需改动）")

print("=== sync558_v2 完成, 全部通过" if ok else "=== sync558_v2 存在失败 ===")
sys.exit(0 if ok else 1)
