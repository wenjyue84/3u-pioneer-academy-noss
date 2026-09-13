"""Generate the CU-selection worksheet a course owner fills in before generation.

Jennifer, 2026-08-24 23:19: *"我觉得我们应该要告诉 AI 我们要选择什么 CU，因为要配合到
我们提倡的课程内容。不能直接丢给它然后没有 instruction。"*

She is right, and the fix is not a better prompt — it is asking the question at the
right moment. This produces one filled-in-by-hand sheet per NOSS listing every
competency unit with the size of its assessment surface, so the choice is made by
the person who knows the syllabus, before a single question is written.

The completed sheet is transcribed into `_engine/profiles/<noss>.json` and from
then on the choice is a contract the validator enforces.

    uv run python -m _engine.ppa.cli worksheet --all
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from .schema import NossGraph, Profile

# A practical station is realistically 40–55 minutes. Three of them plus a
# 30-minute oral session and 10 minutes of handover is what fits in three hours —
# which is why the recommendation below is three practical units, not five.
MINUTES_PER_PRACTICAL_CU = 48
ORAL_SESSION_MINUTES = 30
HANDOVER_MINUTES = 10


def suggest_practical_capacity(duration_max_minutes: int) -> int:
    usable = duration_max_minutes - ORAL_SESSION_MINUTES - HANDOVER_MINUTES
    return max(1, usable // MINUTES_PER_PRACTICAL_CU)


def render_worksheet(graph: NossGraph, existing: Profile | None = None) -> str:
    cap = suggest_practical_capacity(existing.duration_max_minutes if existing else 180)
    lines: list[str] = []
    add = lines.append

    add(f"# Borang Pemilihan Unit Kompetensi — {graph.noss_code}")
    add("")
    add(f"**{graph.noss_title}** · Tahap {graph.level}")
    add(f"**Sumber NOSS:** `{graph.source_file}`")
    add(f"**Dijana:** {date.today().isoformat()}")
    add("")
    add("Sila tandakan **satu** mod bagi setiap unit kompetensi, kemudian hantar semula "
        "borang ini. Pilihan ini menentukan kertas soalan sepenuhnya — tiada unit yang "
        "dipilih secara automatik.")
    add("")
    add("| Mod | Maksud |")
    add("|---|---|")
    add("| `amali` | Dinilai melalui tugasan praktikal dalam kertas SOALAN |")
    add("| `lisan` | Dinilai melalui sesi soal jawab sahaja |")
    add("| `tiada` | Tidak dinilai langsung — tidak muncul di mana-mana dalam kertas |")
    add("")
    add("---")
    add("")
    add("## Unit kompetensi dalam NOSS ini")
    add("")
    add("| Kod | Jenis | Unit Kompetensi | Aktiviti Kerja | Kriteria Prestasi | Mod (isi di sini) |")
    add("|---|---|---|---|---|---|")
    for cu in graph.competency_units:
        jenis = "Teras" if cu.type == "core" else "Elektif"
        current = ""
        if existing:
            current = {"practical": "amali", "oral": "lisan",
                       "excluded": "tiada"}.get(existing.cu_modes.get(cu.code, ""), "")
        add(f"| **{cu.code}** | {jenis} | {cu.title_en} | {len(cu.work_activities)} | "
            f"{cu.pc_count} | {current or '⟪ ⟫'} |")
    add("")

    core = [c for c in graph.competency_units if c.type == "core"]
    elective = [c for c in graph.competency_units if c.type == "elective"]

    add("## Panduan memilih")
    add("")
    add(f"- Peperiksaan amali tiga jam memuatkan lebih kurang **{cap} unit secara amali**. "
        f"Setiap stesen amali mengambil ~{MINUTES_PER_PRACTICAL_CU} minit, ditambah "
        f"{ORAL_SESSION_MINUTES} minit sesi lisan dan {HANDOVER_MINUTES} minit penyerahan.")
    add("- Unit dengan **kriteria prestasi paling banyak** memakan masa paling lama. "
        "Dalam NOSS ini yang terbesar ialah "
        + ", ".join(f"{c.code} ({c.pc_count} kriteria)"
                    for c in sorted(graph.competency_units,
                                    key=lambda c: -c.pc_count)[:2]) + ".")
    add("- Unit yang ditanda `lisan` masih dinilai dan masih dikira dalam markah — "
        "ia bukan unit yang digugurkan.")
    if elective:
        add(f"- NOSS ini mempunyai {len(elective)} unit elektif "
            f"({', '.join(c.code for c in elective)}). Unit elektif yang disenaraikan "
            "pada muka hadapan **mesti** mempunyai soalan dan markah. Jika tiada, "
            "tandakan `tiada` — jangan biarkan ia tersenarai tanpa dinilai.")
    else:
        add("- NOSS ini **tiada unit elektif**. Semua unit adalah teras.")
    add(f"- Terdapat {len(core)} unit teras. Semua unit teras perlu dinilai dalam "
        "sekurang-kurangnya satu mod (`amali` atau `lisan`) melainkan ada sebab "
        "yang dipersetujui dengan PPL.")
    add("")

    if graph.source_notes:
        add("## Nota tentang dokumen NOSS ini")
        add("")
        add("Perkara berikut ditemui semasa menyalin NOSS ini. Ia disalin sebagaimana "
            "tercetak dan tidak dibetulkan sendiri:")
        add("")
        for n in graph.source_notes:
            add(f"- {n}")
        add("")

    add("## Maklumat lain yang diperlukan")
    add("")
    add("| Perkara | Nilai |")
    add("|---|---|")
    add("| Tempoh peperiksaan amali | ⟪ ⟫ jam |")
    add("| Bilangan soalan lisan | ⟪ ⟫ |")
    add("| Wajaran amali : lisan | ⟪ ⟫% : ⟪ ⟫% |")
    add("| Industri / senario SET A | ⟪ ⟫ |")
    add("| Industri / senario SET B | ⟪ ⟫ |")
    add("| Nama pusat bertauliah pada muka hadapan | ⟪ ⟫ |")
    add("")
    add("> **Senario:** elakkan industri yang mempunyai NOSS tersendiri. Contohnya "
        "jualan kenderaan tidak sesuai dijadikan senario bagi NOSS jualan am, kerana "
        "terdapat NOSS khusus bagi bidang tersebut.")
    add("")
    return "\n".join(lines) + "\n"


def write_all(graph_dir: Path, profile_dir: Path, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for gf in sorted(graph_dir.glob("*.json")):
        graph = NossGraph.load(gf)
        pf = profile_dir / gf.name
        existing = Profile.load(pf) if pf.exists() else None
        dest = out_dir / f"borang-pemilihan-cu-{gf.stem}.md"
        dest.write_text(render_worksheet(graph, existing), encoding="utf-8")
        written.append(dest)
    return written
