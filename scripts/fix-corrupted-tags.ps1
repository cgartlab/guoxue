# Fix corrupted HTML tags in all lesson pages
# The earlier PowerShell byte-level fixes turned `<` into `?` in many tag openings.
# Replace `?` followed by a tag indicator back to `<`.

$base = "C:\Users\Chenzhigang\.qclaw\workspace-54nuktoh8cd83kjj\guoxue"
$files = @(
    "lessons/01-lunyu/index.html",
    "lessons/01-lunyu-mixed/index.html",
    "lessons/02-sanzijing/index.html",
    "lessons/02-xueer/index.html",
    "lessons/03-xueer-xiaoti/index.html",
    "lessons/04-zengzi-sansheng/index.html",
    "lessons/05-dao-qiancheng-guo/index.html",
    "lessons/06-dizi-ruze-xiao/index.html",
    "lessons/07-xianxian-yise/index.html",
    "lessons/08-junzi-bu-zhong/index.html",
    "lessons/_template.html"
)

$totalFixed = 0

foreach ($f in $files) {
    $path = [System.IO.Path]::Combine($base, $f.Replace("/", "\"))
    if (-not (Test-Path $path)) {
        Write-Host ("{0}: NOT FOUND" -f $f)
        continue
    }
    
    $text = Get-Content $path -Raw
    
    # Fix corrupted HTML tags from the earlier byte-level restore script.
    # Two categories:
    # 1. Closing tags: `?/div>` `?/p>` `?/li>` `?/h2>` `?/h3>` `?/span>` `?/b>` → always safe
    # 2. Opening tags: `?b`, `?span`, `?strong`, `?a`, `?br`, `?u` → only when followed by `>` or space+attribute
    # NOT matched: `?vs`, `?tì`, `?dì`, `?lè` (Chinese text pronunciations — NOT corrupted tags)
    
    # Fix closing tags first (always safe)
    $fixed = $text -replace '\?/([a-z]+)', '</$1'
    
    # Fix known opening tags (whitelist approach to avoid false matches)
    $openingTags = @('b', 'span', 'a', 'br', 'strong', 'u')
    foreach ($tag in $openingTags) {
        $fixed = $fixed -replace ('\?' + $tag + '(?=[\s>])'), ('<' + $tag)
    }
    
    if ($fixed -ne $text) {
        $changes = 0
        for ($i = 0; $i -lt [Math]::Min($text.Length, $fixed.Length); $i++) {
            if ($text[$i] -ne $fixed[$i]) { $changes++ }
        }
        [System.IO.File]::WriteAllText($path, $fixed, [System.Text.UTF8Encoding]::new($false))
        Write-Host ("{0}: fixed {1} corruptions" -f $f, $changes)
        $totalFixed += $changes
    } else {
        Write-Host ("{0}: clean" -f $f)
    }
}

Write-Host ("`nTotal: {0} corruptions fixed across all files." -f $totalFixed)

# Verify HTML tag balance after fix
Write-Host "`n=== Post-fix div balance check ==="
foreach ($f in $files) {
    $path = [System.IO.Path]::Combine($base, $f.Replace("/", "\"))
    if (-not (Test-Path $path)) { continue }
    $text = Get-Content $path -Raw
    $noComments = $text -replace '<!--.*?-->', ''
    $openDivs = [regex]::Matches($noComments, '<div(?:\s+[^>]*)?>').Count
    $closeDivs = [regex]::Matches($noComments, '</div>').Count
    $diff = $openDivs - $closeDivs
    if ($diff -eq 0) {
        Write-Host ("{0}: ✅ BALANCED (div={1})" -f $f, $openDivs)
    } else {
        Write-Host ("{0}: ❌ UNBALANCED open={1} close={2} diff={3}" -f $f, $openDivs, $closeDivs, $diff)
    }
}
