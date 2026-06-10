# 修复课件页：恢复被误删的课程工具栏
$root = "C:\Users\Chenzhigang\.qclaw\workspace-54nuktoh8cd83kjj\guoxue"
$lessonPages = Get-ChildItem -Path "$root\lessons" -Recurse -Filter "index.html" |
    Where-Object { $_.DirectoryName -notmatch 'template' } |
    Select-Object -ExpandProperty FullName

# 工具栏 HTML 模板（page-indicator 由 slide-engine.js 动态更新）
$toolbarHtml = @'
<!-- ===== 课程工具栏 ===== -->
<nav class="ds-toolbar" aria-label="课程工具栏">
    <a class="ds-btn-nav ds-btn-nav--ghost" href="../../index.html">← 返回目录</a>
    <div class="ds-tabs">
        <button class="ds-tab active" data-section="lecture">讲义</button>
        <button class="ds-tab" data-section="quiz">测验</button>
        <button class="ds-tab" data-section="review">答疑解惑</button>
    </div>
    <div class="ds-toolbar__right">
        <span class="page-indicator" id="page-indicator">1 / 1</span>
        <div class="dots-row" id="dots-row"></div>
        <button class="ds-btn-nav" id="nav-prev" disabled>← 上一页</button>
        <button class="ds-btn-nav" id="nav-next">下一页 →</button>
        <button class="ds-btn-nav ds-btn-nav--icon" id="fullscreen-btn" title="切换全屏显示" aria-label="切换全屏显示"><span class="ds-btn-nav__icon">⛶</span><span class="ds-btn-nav__text">全屏</span></button>
    </div>
</nav>
'@

foreach ($f in $lessonPages) {
    $content = Get-Content $f -Raw

    # 检查是否已经存在 toolbar
    if ($content -match 'class="ds-toolbar"') {
        Write-Host "⏭️  工具栏已存在,跳过: $f"
        continue
    }

    # 检查是否包含 navbar placeholder（应该都有）
    if ($content -match 'data-navbar="global"') {
        # 在 navbar placeholder 的 </nav> 之后插入 toolbar
        # 匹配模式: `<nav data-navbar="global" ...></nav>` 后面的空白 + 下一行
        $pattern = '(<nav data-navbar="global" class="ds-navbar" aria-label="主导航"></nav>\s*)'
        if ($content -match $pattern) {
            $content = $content -replace $pattern, "`$1`r`n$toolbarHtml`r`n"
            $content | Set-Content $f -Encoding UTF8 -NoNewline
            Write-Host "✅ 已恢复工具栏: $f"
        } else {
            Write-Host "❌ 匹配失败: $f"
        }
    } else {
        Write-Host "❌ 未找到 navbar placeholder: $f"
    }
}
