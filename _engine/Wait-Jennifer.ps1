<#
.SYNOPSIS
  Block until Jennifer sends something, then exit so the agent is re-invoked.

.DESCRIPTION
  Polls the Periskope feed every $IntervalSec for an inbound message newer than
  the watermark `_engine/.jennifer-watermark`. Exits 0 the moment one appears,
  and exits 3 if $MaxMinutes passes with nothing — so a silent hour is
  distinguishable from a reply.

  Run detached (`run_in_background: true`). The point is to wait without the
  agent burning turns polling: it is woken by the process exiting, not by a timer.

  Deliberately does *not* transcribe or interpret anything. It only detects that
  something arrived; `Watch-Jennifer.ps1` does the reading, including Whisper
  transcription of voice notes.
#>
[CmdletBinding()]
param(
    [int]$IntervalSec = 60,
    [int]$MaxMinutes  = 50
)

$ErrorActionPreference = 'Stop'
$ChatId    = '60126111677@c.us'
$Watermark = Join-Path $PSScriptRoot '.jennifer-watermark'

. C:\Users\Jyue\Scripts\Periskope-Direct.ps1

$since = if (Test-Path $Watermark) {
    [datetime](Get-Content $Watermark -Raw).Trim()
} else {
    (Get-Date).AddMinutes(-5)
}

$deadline = (Get-Date).AddMinutes($MaxMinutes)
$polls = 0

# A heartbeat, so a silent watcher can be told apart from a dead one. On
# 2026-08-25 a run's window elapsed with no output and no exit notification, and
# there was no way to tell whether it was still polling or had died — which for a
# watcher is the difference between "no reply yet" and "not watching".
Write-Output ("watching $ChatId since $($since.ToString('MM-dd HH:mm')); " +
              "deadline $($deadline.ToString('HH:mm')), every ${IntervalSec}s")

while ((Get-Date) -lt $deadline) {
    $polls++
    if ($polls % 15 -eq 0) {
        Write-Output "still watching — $polls polls, nothing since $($since.ToString('HH:mm'))"
    }
    try {
        $r = Get-PeriskopeMessages -ChatIds $ChatId -Limit 2000
        $new = @($r.Messages[$ChatId]) |
               Where-Object { $_ -and -not $_.from_me -and ([datetime]$_.timestamp) -gt $since }
        if ($new) {
            $first = ($new | Sort-Object timestamp | Select-Object -First 1)
            Write-Output ("NEW MESSAGE from Jennifer at " +
                          "$(([datetime]$first.timestamp).ToString('HH:mm')) " +
                          "($(@($new).Count) total, after $polls polls)")
            Write-Output "Run: _engine\Watch-Jennifer.ps1"
            exit 0
        }
    } catch {
        # A transient API failure must not end the wait — it would look like silence.
        Write-Output "poll $polls failed: $($_.Exception.Message)"
    }
    Start-Sleep -Seconds $IntervalSec
}

Write-Output "NO REPLY after $MaxMinutes minutes ($polls polls). Watermark unchanged."
exit 3
