#!/usr/bin/env python3
"""
guoxue 旧课程统一迁移管线 (09-44 → 第一节课标准)
将旧标准课程迁移到 slide-engine.js 架构:
1. legacy 颜色 token → ds tokens (暗色模式自动适配)
2. 硬编码 border-radius/padding/margin/gap → ds tokens
3. quiz 硬编码 HTML → GUOXUE_QUIZ_OVERRIDE + 空占位
4. 容器 ds-slide-container → slide-viewport + slide-container
5. 内联导航脚本 → slide-engine.js
6. 补全页面骨架: 进度条 + kbd-hint + 成绩页 + 结束页 + auth 脚本
7. 首页 slide 加 active
"""
import re, sys, json, os

# ── 映射表 ────────────────────────────────────────────────────────────────
LEGACY_TO_DS = {
    '--blue-700':  '--ds-color-info',      # 文字/强调 (蓝=信息)
    '--blue-800':  '--ds-color-info',
    '--blue-100':  '--ds-color-info-bg',   # 信息底色
    '--amber-100': '--ds-color-warning-bg',# 警示/原文底色
    '--amber-700': '--ds-color-warning',   # 警示文字
    '--amber-800': '--ds-color-warning',
    '--green-100': '--ds-color-success-bg',# 正确底色
    '--green-200': '--ds-color-success-bg',
    '--green-300': '--ds-color-success',
    '--green-700': '--ds-color-success',
    '--green-800': '--ds-color-success',
    '--red-100':   '--ds-color-error-bg',  # 错误/对比底色
    '--red-300':   '--ds-color-error',
    '--red-700':   '--ds-color-error',
    '--purple-100':'--ds-accent-soft',     # 延伸思考底色
    '--purple-700':'--ds-accent',
    '--purple-800':'--ds-accent',
    '--gray-100':  '--ds-color-surface',   # 中性底色
    '--gray-200':  '--ds-color-surface',
}

# 硬编码值 → ds token (radius/padding/margin/gap)
VALUE_TO_TOKEN = [
    ('border-radius:12px',  'border-radius:var(--ds-radius-xl)'),
    ('border-radius: 12px', 'border-radius:var(--ds-radius-xl)'),
    ('border-radius:8px',   'border-radius:var(--ds-radius-md)'),
    ('border-radius: 8px',  'border-radius:var(--ds-radius-md)'),
    ('padding:1.5rem',      'padding:var(--ds-space-6)'),
    ('padding:1.2rem',      'padding:var(--ds-space-5)'),
    ('padding:1rem',        'padding:var(--ds-space-4)'),
    ('padding:0.8rem',      'padding:var(--ds-space-3)'),
    ('border-radius:10px',  'border-radius:var(--ds-radius-lg)'),
    ('border-radius: 10px',  'border-radius:var(--ds-radius-lg)'),
    ('padding:0.9rem',      'padding:var(--ds-space-3)'),
    ('padding:0.7rem',      'padding:var(--ds-space-2)'),
    ('padding:0.6rem',      'padding:var(--ds-space-2)'),
    ('margin:0.6rem',       'margin:var(--ds-space-2)'),
    ('margin-top:0.6rem',   'margin-top:var(--ds-space-2)'),
    ('margin-bottom:0.6rem','margin-bottom:var(--ds-space-2)'),
    ('gap:0.6rem',          'gap:var(--ds-space-2)'),
    ('gap:0.3rem',          'gap:var(--ds-space-1)'),
    ('padding:0.4rem',      'padding:var(--ds-space-2)'),
    ('padding:0.3rem',      'padding:var(--ds-space-1)'),
    ('padding:0.2rem',      'padding:var(--ds-space-1)'),
    ('margin:1.2rem',       'margin:var(--ds-space-5)'),
    ('margin:1rem',         'margin:var(--ds-space-4)'),
    ('margin:0.8rem',       'margin:var(--ds-space-3)'),
    ('margin:0.5rem',       'margin:var(--ds-space-2)'),
    ('margin:0.4rem',       'margin:var(--ds-space-2)'),
    ('margin:0.3rem',       'margin:var(--ds-space-1)'),
    ('margin:0.2rem',       'margin:var(--ds-space-1)'),
    ('margin-top:1.5rem',   'margin-top:var(--ds-space-6)'),
    ('margin-top:1.2rem',   'margin-top:var(--ds-space-5)'),
    ('margin-top:1.8rem',   'margin-top:var(--ds-space-7)'),
    ('margin-top:1rem',     'margin-top:var(--ds-space-4)'),
    ('margin-top:0.8rem',   'margin-top:var(--ds-space-3)'),
    ('margin-top:0.5rem',   'margin-top:var(--ds-space-2)'),
    ('margin-top:0.4rem',   'margin-top:var(--ds-space-2)'),
    ('margin-top:0.3rem',   'margin-top:var(--ds-space-1)'),
    ('margin-bottom:1.2rem','margin-bottom:var(--ds-space-5)'),
    ('margin-bottom:0.2rem','margin-bottom:0'),
    ('margin-bottom:1rem',  'margin-bottom:var(--ds-space-4)'),
    ('margin-bottom:0.8rem','margin-bottom:var(--ds-space-3)'),
    ('margin-bottom:0.5rem','margin-bottom:var(--ds-space-2)'),
    ('margin-bottom:0.3rem','margin-bottom:var(--ds-space-1)'),
    ('gap:1rem',            'gap:var(--ds-space-4)'),
    ('gap:0.8rem',          'gap:var(--ds-space-3)'),
    ('gap:0.5rem',          'gap:var(--ds-space-2)'),
    ('gap:0.4rem',          'gap:var(--ds-space-2)'),
]

def transform_lesson(path, dry=False):
    """迁移单门课。返回 True 成功 / False 跳过或失败。"""
    src = open(path, encoding='utf-8').read()
    orig = src
    name = path.split('/')[1]
    log = []

    def rep(old, new, expect=None, label=''):
        nonlocal src
        n = src.count(old)
        if expect is not None and n != expect:
            log.append(f'✗ [{name}] {label}: 期望{expect}实际{n}  {old[:50]}')
            return False
        src = src.replace(old, new)
        return True

    # 1. legacy 颜色 token → ds
    for legacy, ds in LEGACY_TO_DS.items():
        src = src.replace(f'var({legacy})', f'var({ds})')

    # 2. 硬编码值 → ds token (逐个, 统计)
    for old, new in VALUE_TO_TOKEN:
        src = src.replace(old, new)

    # 3. 提取 quiz 数据
    quiz_secs = re.findall(
        r'<section class="slide" data-section="quiz" data-index="(\d+)">(.*?)</section>',
        src, re.S)
    if not quiz_secs:
        log.append(f'✗ [{name}] 未找到 quiz section')
        return False

    quiz_items = []
    for idx, body in quiz_secs:
        qm = re.search(r'<p><strong>(.*?)</strong></p>', body)
        q = re.sub(r'<[^>]+>', '', qm.group(1)) if qm else ''
        opts = re.findall(
            r'<span class="quiz-option-key">([A-D])</span>\s*<span class="quiz-option-text">(.*?)</span>',
            body)
        # 用 div 位置对齐 data-correct
        ans = -1
        opt_divs = re.findall(r'<div class="quiz-option"((?: data-correct="true")?)[^>]*>', body)
        for oi, attrs in enumerate(opt_divs):
            if 'correct' in attrs:
                ans = oi
                break
        texts = [t for c, t in opts]
        if len(texts) != 4 or ans < 0:
            log.append(f'✗ [{name}] Q{idx}: opts={len(texts)} ans={ans}')
            return False
        quiz_items.append({'q': q, 'opts': texts, 'ans': ans, 'exp': ''})

    if len(quiz_items) != 10:
        log.append(f'✗ [{name}] 题数 {len(quiz_items)} != 10')
        return False

    # 4. 替换 quiz 区为占位 (整体替换测验块)
    i = src.find('<!-- ====== 测验部分')
    j = src.find('<!-- ====== 答疑解惑')
    if i < 0 or j <= i:
        # 容错: 查找 quiz section 起始
        first = re.search(r'data-section="quiz" data-index="0"', src)
        if first:
            i = src.rfind('<section', 0, first.start())
            j = src.find('答疑解惑', first.start())
            j = src.rfind('</section>', 0, j) + len('</section>')
        else:
            log.append(f'✗ [{name}] 找不到测验块边界')
            return False

    n_quiz = src[i:j].count('data-section="quiz"')
    if n_quiz != 10:
        log.append(f'✗ [{name}] 测验块内 quiz section {n_quiz} != 10')
        return False

    placeholders = ('<!-- ====== 测验部分（slide-engine.js 渲染） ====== -->\n\n'
        + '\n'.join(f'<section class="slide" data-section="quiz" id="quiz-{k}"></section>' for k in range(10))
        + '\n\n')
    src = src[:i] + placeholders + src[j:]

    # 5. 容器改造 (兼容有无注释两种结尾)
    if '<main class="ds-slide-container" id="slide-container">' in src:
        src = src.replace(
            '<main class="ds-slide-container" id="slide-container">',
            '<div class="slide-viewport">\n<main class="slide-container" id="slide-container">', 1)
    if '</main><!-- end slide-container -->' in src:
        src = src.replace('</main><!-- end slide-container -->', '</main>\n</div><!-- slide-viewport -->', 1)
    elif '</main>' in src:
        # 无注释结尾: 直接 </main> → 加闭合 div
        src = src.replace('</main>', '</main>\n</div><!-- slide-viewport -->', 1)
    elif '</main >' in src:
        src = src.replace('</main >', '</main>\n</div><!-- slide-viewport -->', 1)
    elif '</main\n>' in src:
        src = src.replace('</main\n>', '</main>\n</div><!-- slide-viewport -->', 1)

    # 5b. 补全页面骨架 (进度条 + kbd-hint + quiz-score 成绩页 + end-slide 结束页)
    src = add_skeleton(src, name)

    # 6. 首页 slide 加 active
    src = src.replace(
        '<section class="slide" data-section="lecture" data-index="0">',
        '<section class="slide active" data-section="lecture" data-index="0">', 1)

    # 7. 删除内联脚本, 插入引擎引用
    script_pat = re.compile(r'<script>\n// ===== 页面导航控制.*?</script>', re.S)
    m = script_pat.search(src)
    if not m:
        # 容错: 最后一个无 src 的 script
        m = re.search(r'<script>(?!.*src=).*?</script>', src, re.S)
    if not m:
        log.append(f'✗ [{name}] 找不到内联脚本')
        return False

    quiz_js = build_quiz_js(quiz_items)
    new_script = ('<script>\n'
                  f"    window.GUOXUE_COURSE_ID = '{name}';\n"
                  + quiz_js + '\n</script>\n'
                  + '<script src="../../assets/js/slide-engine.js?v=29f633f"></script>')
    src = src.replace(m.group(0), new_script, 1)

    # 8. 补 auth 脚本 (如果缺)
    if 'auth.js' not in src:
        src = src.replace('</body>',
            '<script src="../../assets/js/auth-email.js" defer></script>\n'
            '<script src="../../assets/js/auth.js" defer></script>\n'
            '<script src="../../assets/js/api-client.js" defer></script>\n</body>', 1)

    if dry:
        return True, src, log, quiz_items
    open(path, 'w', encoding='utf-8').write(src)
    print(f'✓ [{name}] 迁移完成 ({len(orig)} -> {len(src)} 字节)')
    return True, src, log, quiz_items


def build_quiz_js(items):
    """生成 GUOXUE_QUIZ_OVERRIDE 脚本(exp 留空由后续步骤填充)"""
    lines = ['const QUIZ = [']
    for it in items:
        opts = ', '.join(repr(o) for o in it['opts'])
        lines.append(f"  {{q: {repr(it['q'])}, opts: [{opts}], ans: {it['ans']}, exp: {repr(it['exp'])}}},")
    lines.append('];')
    lines.append('window.GUOXUE_QUIZ_OVERRIDE = QUIZ;')
    return '\n'.join(lines)


def add_skeleton(src, name):
    """补全页面骨架: 成绩页/结束页/进度条/kbd-hint（与 01 课一致）"""
    # 若已有则跳过
    if 'quiz-score' in src and 'progress-bar-bottom' in src and 'end-slide' in src:
        return src

    # 1. quiz-score 成绩页 — 插在最后一个 quiz 占位之后
    score_page = '''    <!-- ====== 测验得分页 ====== -->
    <section class="slide" data-section="quiz" id="quiz-score" style="align-items:center;text-align:center;">
        <span class="ds-badge ds-badge--success">测验得分</span>
        <h2 style="border:none;text-align:center;padding-bottom:0;">测验完成！</h2>
        <div style="margin-top:var(--ds-space-10);">
            <div style="font-size:5rem;color:var(--ds-accent);font-weight:700;font-family:var(--ds-font-display);line-height:1;" id="score-display">0</div>
            <div style="font-size:1.5rem;margin-top:var(--ds-space-4);color:var(--ds-color-fg-strong);font-weight:600;" id="score-message">正在计算得分...</div>
            <div style="margin-top:var(--ds-space-8);font-size:1.125rem;color:var(--ds-color-fg);background:var(--ds-color-surface);padding:var(--ds-space-6);border-radius:var(--ds-radius-xl);display:inline-block;text-align:left;">
                <p style="margin-bottom:var(--ds-space-3);">✅ 答对题数：<b id="correct-count" style="color:var(--ds-color-success);font-size:1.25rem;">0</b> / 10</p>
                <p style="margin-bottom:var(--ds-space-3);">📊 总得分：<b id="total-score" style="color:var(--ds-accent);font-size:1.25rem;">0</b> 分（满分 100 分）</p>
                <p>📈 正确率：<b id="score-percent" style="color:var(--ds-color-info);font-size:1.25rem;">0%</b></p>
            </div>
            <button class="retake-btn" id="retake-btn" aria-label="重新答题" style="margin-top:var(--ds-space-6);">↺ 重新答题</button>
        </div>
    </section>

'''
    # 插入到最后一个 quiz 占位之后
    last_quiz = re.search(r'(<section class="slide" data-section="quiz" id="quiz-9"></section>)', src)
    if last_quiz:
        src = src.replace(last_quiz.group(1), last_quiz.group(1) + '\n' + score_page, 1)

    # 2. end-slide 结束页 — 插在 </main> 前
    end_slide = '''    <!-- ====== 结束页 ====== -->
    <section class="slide end-slide" data-section="review">
        <div class="cover-ornament"></div>
        <h2 class="ds-display">谢谢大家</h2>
        <div class="cover-ornament"></div>
        <div class="end-quote">
            "学而时习之，不亦说乎"<br>
            <span style="font-size:0.875rem;color:var(--ds-color-muted);">—— 孔子</span>
        </div>
        <div class="cover-seal">国学</div>
    </section>

'''
    src = src.replace('</main>\n</div><!-- slide-viewport -->', end_slide + '</main>\n</div><!-- slide-viewport -->', 1)
    # 若上面未插入(结束页已在), 检查是否已存在 end-slide
    if 'end-slide' not in src:
        # 兜底: 在最后一个 </main> 前插入
        idx = src.rfind('</main>')
        if idx > 0:
            src = src[:idx] + end_slide + src[idx:]

    # 3. 进度条 + kbd-hint — 插在 </body> 前
    chrome = '''<!-- 底部进度条 -->
<div class="progress-bar-bottom">
    <div class="progress-bar-fill" id="progress-fill" style="width:4%"></div>
</div>

<!-- 键盘提示 -->
<div class="kbd-hint">
    <span class="kbd">←</span><span class="kbd">→</span> 翻页
    <span style="margin-left:8px"><span class="kbd">Space</span> 下一页</span>
</div>

'''
    src = src.replace('</body>', chrome + '</body>', 1)
    return src


if __name__ == '__main__':
    path = sys.argv[1]
    ok, src, log, quiz = transform_lesson(path, dry=('--dry' in sys.argv))
    for l in log:
        print(l)
    if ok:
        print(f"quiz 提取: {len(quiz)} 题")
        for i, q in enumerate(quiz):
            print(f"  Q{i+1}: {q['q'][:40]} ans={chr(65+q['ans'])}")
        if '--dump' in sys.argv:
            open('/tmp/migrated.html', 'w', encoding='utf-8').write(src)
            print('已输出 /tmp/migrated.html')
