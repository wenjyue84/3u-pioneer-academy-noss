$ErrorActionPreference = "Stop"
$dir = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\07 3.4b Soalan Penilaian Pengetahuan\Core Abilities L1-L3 (format JPK)"
$files = Get-ChildItem -Path $dir -Filter "*.docx" | Sort-Object Name
foreach ($f in $files) {
    $pdfPath = [System.IO.Path]::ChangeExtension($f.FullName, "pdf")
    Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $pages = -1
    try {
        $doc = $word.Documents.Open($f.FullName)
        $doc.SaveAs([ref]$pdfPath, [ref]17)
        $pages = $doc.ComputeStatistics(2)
        $doc.Close([ref]$false)
    } catch {
        Write-Output "ERROR on $($f.Name): $_"
    } finally {
        try { $word.Quit() } catch {}
    }
    Write-Output "$($f.Name)|$pages"
    Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
}
