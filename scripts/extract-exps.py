#!/usr/bin/env python3
"""从讲义文本自动提取测验解析 (exp) v3 — 三级匹配"""
import re, json, sys

def clean(s):
    return re.sub(r'[^\u4e00-\u9fff]', '', s or '')

STOP = {'为什么','是什么','什么','怎么','正确','意思','揭示','表明','说明','以下','哪句','哪种','哪一项',
        '最接近','最重要','核心','含义','作用','特征','道理','选择','的说法','如何理解','的理解','中','了一',
        '本章','下列','不是','属于','关于','主要','而言','本句','则','与','指','指的是','应该','可以','的是',
        '一个','一种','孔子','有子','的话','的说法','所谓','就是','就会','进行','学习','说的','有着','其中',
        '第一个','第二个','第三个','第四个','以及','还有','另外','此外','甚至','但是','然而','这种','那个',
        '哪种','哪项','哪个','项','句话'}

def split_sents(text):
    return [p for p in re.split(r'[。！？；\n]', text) if len(clean(p)) >= 10]

def word_pieces(text, minlen, maxlen):
    """从原始文本提取中文字段切片 (按原标点边界)"""
    out = []
    for run in re.findall(r'[\u4e00-\u9fff]{' + str(minlen) + ',' + str(maxlen) + '}', text or ''):
        if len(run) >= minlen:
            out.append(run)
    return out

def find_exp(lecture, q, opts, ans):
    correct = opts[ans] if ans < len(opts) else ''
    sents = split_sents(lecture)

    # 候选: 答案片(4-12字, 长→短) + 题干片(3-8字)
    c_pieces = [p for p in word_pieces(correct, 4, 12) if p not in STOP]
    q_pieces = [p for p in word_pieces(q, 3, 8) if p not in STOP]
    c_pieces.sort(key=len, reverse=True)
    q_pieces.sort(key=len, reverse=True)

    # ── 级别1: 答案片命中 ──
    for c in c_pieces[:6]:
        cc = clean(c)
        if len(cc) < 4: continue
        for s in sents:
            if cc in clean(s):
                return s

    # ── 级别2: 滑动窗口打分 (答案词×3 + 题干词×1) ──
    best, best_score = None, 1  # require >1
    for i, s in enumerate(sents):
        sc_ = clean(s)
        sc = sum(3 for c in c_pieces[:5] if c and clean(c) in sc_)
        sc += sum(1 for p_ in q_pieces[:6] if p_ and clean(p_) in sc_)
        if sc > best_score:
            best, best_score = s, sc

    # ── 级别3: 宽松匹配 — 任一题干主词 (>=4字) 命中 ──
    if best is None:
        for p_ in q_pieces[:8]:
            if len(p_) < 3: continue
            pp = clean(p_)
            for s in sents:
                if pp in clean(s):
                    best = s
                    break
            if best: break
    return best

def trim(p, maxlen=95):
    p = re.sub(r'\s+', '', p)
    if len(p) <= maxlen:
        return p
    cut = p[:maxlen]
    for end in ['——', '，，', '，', '。']:
        i = cut.rfind(end)
        if i > 25:
            return cut[:i] + '……'
    return cut + '……'

def process_pack(path):
    data = json.load(open(path, encoding='utf-8'))
    lecture = data['lecture']
    return [trim(find_exp(lecture, it['q'], it.get('opts', []), it['ans'])) if find_exp(lecture, it['q'], it.get('opts', []), it['ans']) else '' for it in data['quiz']]

if __name__ == '__main__':
    data = json.load(open(sys.argv[1], encoding='utf-8'))
    for i, it in enumerate(data['quiz']):
        exp = find_exp(data['lecture'], it['q'], it.get('opts', []), it['ans'])
        t = trim(exp) if exp else ''
        print(f"Q{i+1} ans={chr(65+it['ans'])}: {'✓ ' + t[:75] if t else '✗ 未找到'}")