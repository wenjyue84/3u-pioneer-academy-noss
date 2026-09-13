<#
.SYNOPSIS
  Report any message from Jennifer that has arrived since the last check.

.DESCRIPTION
  Polls the Periskope account feed for chat 60126111677@c.us and prints only
  inbound messages newer than the watermark in `_engine/.jennifer-watermark`.
  Voice notes are downloaded and transcribed with the local Whisper model,
  because on 2026-08-24 one of her requirements — that a vehicle-sales scenario
  cannot be used, since vehicle sales has its own NOSS — existed **only** in a
  voice note and appeared nowhere in the text messages. Reading only the text
  would have missed it again.

  Prints `NO NEW MESSAGES` and exits 0 when there is nothing, so a polling loop
  can tell "quiet" from "failed".

.PARAMETER Mark
  Advance the watermark to the newest message without printing. Use after the
  new messages have been read and acted on.
#>
[CmdletBinding()]
param(
    [switch]$Mark,
    [int]$Limit = 2000
)

$ErrorActionPreference = 'Stop'

$ChatId    = '60126111677@c.us'
$Root      = Split-Path $PSScriptRoot -Parent
$Watermark = Join-Path $PSScriptRoot '.jennifer-watermark'
$MediaDir  = Join-Path $Root 'raw\jennifer-wa-inbound'
$Whisper   = 'C:\Users\Jyue\Documents\1-projects\voice-to-text-transription-local-system'

. C:\Users\Jyue\Scripts\Periskope-Direct.ps1

$since = if (Test-Path $Watermark) {
    [datetime](Get-Content $Watermark -Raw).Trim()
} else {
    (Get-Date).AddHours(-2)
}

$result = Get-PeriskopeMessages -ChatIds $ChatId -Limit $Limit
if ($result.Coverage[$ChatId] -eq 'FetchFailed') {
    Write-Output "FETCH FAILED — Periskope returned nothing; window validity unknown."
    exit 2
}

$all = @($result.Messages[$ChatId])
if (-not $all) { Write-Output "NO NEW MESSAGES (chat quiet in window)"; exit 0 }

$newest = ($all | Sort-Object timestamp | Select-Object -Last 1).timestamp

if ($Mark) {
    ([datetime]$newest).ToString('o') | Set-Content $Watermark -NoNewline
    Write-Output "watermark -> $newest"
    exit 0
}

# Inbound only. Our own sends are not feedback.
$new = $all |
    Where-Object { -not $_.from_me -and ([datetime]$_.timestamp) -gt $since } |
    Sort-Object timestamp

if (-not $new) {
    Write-Output "NO NEW MESSAGES (since $($since.ToString('MM-dd HH:mm')))"
    exit 0
}

Write-Output "=== $(@($new).Count) NEW FROM JENNIFER (since $($since.ToString('MM-dd HH:mm'))) ==="

$voice = @()
foreach ($m in $new) {
    $t = ([datetime]$m.timestamp).ToString('MM-dd HH:mm')
    if ($m.body) {
        Write-Output "[$t] $($m.body)"
    } elseif ($m.media) {
        New-Item -ItemType Directory -Force -Path $MediaDir | Out-Null
        $ext  = switch -Regex ($m.media.mimetype) { 'ogg|opus|mpeg' {'mp3'} 'jpeg' {'jpg'} 'png' {'png'} 'pdf' {'pdf'} default {'bin'} }
        $file = Join-Path $MediaDir ("{0}_{1}.{2}" -f ([datetime]$m.timestamp).ToString('yyyyMMdd-HHmmss'), $m.message_type, $ext)
        if (-not (Test-Path $file)) {
            try { Invoke-WebRequest -Uri $m.media.path -OutFile $file -ErrorAction Stop } catch {}
        }
        Write-Output "[$t] <$($m.message_type)> $file"
        if ($m.message_type -in @('ptt','audio')) { $voice += $file }
    } else {
        Write-Output "[$t] <$($m.message_type)>"
    }
}

if ($voice) {
    Write-Output ""
    Write-Output "=== TRANSCRIPTS ==="
    $inbox = Join-Path $Whisper 'inbox'
    New-Item -ItemType Directory -Force -Path $inbox | Out-Null
    foreach ($v in $voice) {
        $dst = Join-Path $inbox ("watch_" + [IO.Path]::GetFileNameWithoutExtension($v) + ".mp3")
        Copy-Item $v $dst -Force
        $py = @"
import sys
sys.path.insert(0, r'$Whisper')
from transcriber import transcribe_audio
print(transcribe_audio(audio_path=r'$dst', model_name='large-v3-turbo',
                       device='cuda', compute_type='int8_float16', output_format='txt'))
"@
        $tmp = [IO.Path]::GetTempFileName() + '.py'
        $py | Out-File -FilePath $tmp -Encoding utf8
        $out = & "$Whisper\.venv\Scripts\python.exe" $tmp 2>&1 | Select-String -Pattern '\.txt$'
        Remove-Item $tmp -Force -ErrorAction SilentlyContinue
        if ($out -match '([A-Za-z]:\\[^\r\n]+\.txt)') {
            $text = (Get-Content $Matches[1] -Raw) -replace '\s+', ' '
            Write-Output "$([IO.Path]::GetFileName($v)) :: $text"
        } else {
            Write-Output "$([IO.Path]::GetFileName($v)) :: TRANSCRIPTION FAILED"
        }
    }
}

Write-Output ""
Write-Output "Run with -Mark once these have been handled."
