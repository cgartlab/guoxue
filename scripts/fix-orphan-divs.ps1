$base = "C:\Users\Chenzhigang\.qclaw\workspace-54nuktoh8cd83kjj\guoxue"

$files = @(
    "lessons\01-lunyu\index.html",
    "lessons\01-lunyu-mixed\index.html",
    "lessons\02-sanzijing\index.html",
    "lessons\02-xueer\index.html",
    "lessons\03-xueer-xiaoti\index.html",
    "lessons\04-zengzi-sansheng\index.html",
    "lessons\05-dao-qiancheng-guo\index.html",
    "lessons\06-dizi-ruze-xiao\index.html",
    "lessons\07-xianxian-yise\index.html",
    "lessons\08-junzi-bu-zhong\index.html",
    "_template.html"
)

$fixed = 0
foreach ($f in $files) {
    $path = [System.IO.Path]::Combine($base, $f)
    if (-not (Test-Path $path)) {
        Write-Host ("{0}: NOT FOUND" -f $f)
        continue
    }
    
    $text = Get-Content $path -Raw
    # Remove orphan </div> that appears right after </footer>
    $newText = $text -replace '(</footer>)\s*\n\s*</div>', '$1'
    
    if ($newText -ne $text) {
        # Write with UTF8 without BOM
        [System.IO.File]::WriteAllText($path, $newText, [System.Text.UTF8Encoding]::new($false))
        Write-Host ("{0}: fixed" -f $f)
        $fixed++
    } else {
        Write-Host ("{0}: no orphan found" -f $f)
    }
}

Write-Host ("Done. Fixed {0} files." -f $fixed)
