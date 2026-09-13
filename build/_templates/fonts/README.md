# Fonts used by `reference-textbook.docx`

The DOCX template specifies the following fonts. If the preferred face is not
installed on the reader's machine, Word silently substitutes the fallback.

| Role | Preferred | Fallback (Windows default) | Source |
|------|-----------|---------------------------|--------|
| Body serif | Source Serif 4 | Cambria | https://github.com/adobe-fonts/source-serif |
| Heading sans | Source Sans 3 | Calibri | https://github.com/adobe-fonts/source-sans |
| CJK (Chinese) | Source Han Serif SC | Microsoft YaHei | https://github.com/adobe-fonts/source-han-serif |
| Monospace (code) | JetBrains Mono | Consolas | https://www.jetbrains.com/lp/mono/ |

## Install (Windows)

Source Sans / Serif and Source Han Serif are free under the SIL Open Font
License. Download the OTFs from the Adobe Fonts GitHub releases, extract,
select all .otf files, right-click → **Install for all users**.

JetBrains Mono:
```powershell
winget install --id=JetBrains.JetBrainsMono
```

## Why these fonts

- **Source Serif 4** is a modern transitional serif designed for screen and
  print. Close cousin of Fedra Serif / Charter used by Cambridge/Pearson.
- **Source Sans 3** has a wide, open x-height ideal for chapter titles.
- **Source Han Serif SC** gives Chinese content genuine serif identity so
  that 推拿 / 穴位 / etc. do not render as sans-serif or bitmap.
- **JetBrains Mono** has ligatures and good Chinese fallback; more readable
  at 9.5 pt than Courier New.

## Licence

All four are free (OFL or Apache 2.0). The DOCX does not embed them; readers
either have them installed or see the fallback. No licence constraint ships
with the output file.
