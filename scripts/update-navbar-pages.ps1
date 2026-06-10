# Update all lesson pages to use navbar-component
$root = "C:\Users\Chenzhigang\.qclaw\workspace-54nuktoh8cd83kjj\guoxue"
$lessonPages = Get-ChildItem -Path "$root\lessons" -Recurse -Filter "index.html" | 
    Where-Object { $_.DirectoryName -notmatch 'template' } | 
    Select-Object -ExpandProperty FullName

foreach ($f in $lessonPages) {
    $content = Get-Content $f -Raw

    # 1. Replace the old global navbar with placeholder
    # Match: <nav class="ds-navbar ds-navbar--global" aria-label="主导航"> ... </nav>
    $startTag = '<nav class="ds-navbar ds-navbar--global" aria-label="主导航">'
    $idx = $content.IndexOf($startTag)
    if ($idx -ge 0) {
        $endIdx = $content.IndexOf("</nav>", $idx)
        if ($endIdx -ge 0) {
            $endIdx2 = $content.IndexOf("</nav>", $endIdx + 6)
            if ($endIdx2 -ge 0 -and ($endIdx2 - $idx) -lt 1500) {
                # Check if this is the right nav (the global one, not the toolbar)
                $navContent = $content.Substring($idx, $endIdx2 - $idx + 6)
                if ($navContent -match "ds-navbar--global") {
                    $newNav = '<nav data-navbar="global" class="ds-navbar" aria-label="主导航"></nav>'
                    $content = $content -replace [regex]::Escape($navContent), $newNav
                    Write-Host "✅ Updated navbar in: $f"
                } else {
                    Write-Host "⚠️ Found nav but not --global in: $f"
                }
            } else {
                Write-Host "⚠️ Could not find proper nav boundary in: $f"
            }
        } else {
            Write-Host "❌ No </nav> after start tag in: $f"
        }
    } else {
        Write-Host "❌ No ds-navbar--global found in: $f"
    }

    # 2. Add navbar-component script before </body> if not already present
    $scriptTag = '  <script src="../../assets/js/navbar-component.js" defer></script>'
    if ($content -notmatch 'navbar-component') {
        $content = $content -replace '</body>', "$scriptTag`r`n</body>"
        Write-Host "   + Added navbar script to: $f"
    }

    $content | Set-Content $f -Encoding UTF8 -NoNewline
}
