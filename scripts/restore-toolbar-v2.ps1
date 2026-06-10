# 修复课件页：恢复被误删的工具栏（直接字节操作，避免编码问题）
$root = "C:\Users\Chenzhigang\.qclaw\workspace-54nuktoh8cd83kjj\guoxue"

# 用字节数组模式读取工具栏HTML
$toolbarHtml = @"
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
"@

$lessonPages = Get-ChildItem -Path "$root\lessons" -Filter index.html -Recurse -ErrorAction SilentlyContinue |
    Where-Object { $_.DirectoryName -notmatch 'template' }

foreach ($f in $lessonPages) {
    Write-Host "处理: $($f.FullName)"

    # 以字节数组读取，避免编码问题
    $bytes = [System.IO.File]::ReadAllBytes($f.FullName)
    $text = [System.Text.Encoding]::UTF8.GetString($bytes)

    # 检查是否已有工具栏
    if ($text -match 'class="ds-toolbar"') {
        Write-Host "  ⏭️ 已有工具栏，跳过"
        continue
    }

    # 在导航栏 placeholder 后插入工具栏
    $marker = '<nav data-navbar="global" class="ds-navbar" aria-label="主导航"></nav>'
    $idx = $text.IndexOf($marker)
    if ($idx -ge 0) {
        $insertAt = $idx + $marker.Length
        $newText = $text.Substring(0, $insertAt) + "`r`n`r`n" + $toolbarHtml + "`r`n" + $text.Substring($insertAt)

        # 以字节数组写回
        [System.IO.File]::WriteAllBytes($f.FullName, [System.Text.Encoding]::UTF8.GetBytes($newText))
        Write-Host "  ✅ 已恢复工具栏"
    } else {
        Write-Host "  ❌ 未找到 navbar placeholder"
    }
}
