<#
.SYNOPSIS  Print Word page count for every .docx in a folder (one Word process per file). Also patches "[TBD: jumlah muka surat]" in the header table with the real total when -PatchTotal is given.
#>
param([Parameter(Mandatory)][string]$Folder, [switch]$PatchTotal)
$tmpd = "C:\tmp_juno_pdf"; New-Item -ItemType Directory -Force $tmpd | Out-Null
$i = 0
foreach ($f in Get-ChildItem -LiteralPath $Folder -Filter *.docx -File) {
    $i++; $tmp = "$tmpd\c$i.docx"; Copy-Item -LiteralPath $f.FullName $tmp -Force
    $w = $null
    try {
        $w = New-Object -ComObject Word.Application; $w.Visible = $false; $w.DisplayAlerts = 0
        $doc = $w.Documents.Open($tmp)
        $pages = $doc.ComputeStatistics(2)
        if ($PatchTotal) {
            $rng = $doc.Content; $fnd = $rng.Find
            $null = $fnd.Execute("[TBD: jumlah muka surat]", $false, $false, $false, $false, $false, $true, 1, $false, "$pages", 2)
            $pages = $doc.ComputeStatistics(2); $doc.Save()
        }
        $doc.Close($false)
        Write-Output ("{0}`t{1}" -f $pages, $f.Name)
    } catch { Write-Output ("ERR`t{0}`t{1}" -f $f.Name, $_.Exception.Message) }
    finally { if ($w) { try { $w.Quit() } catch {} } }
    if ($PatchTotal -and (Test-Path $tmp)) { Copy-Item $tmp -Destination $f.FullName -Force }
}
