# -*- coding: utf-8 -*-
"""Build 3.3a Rangka Nota Pembelajaran docx files (5, one per core CU) for IT-072-3:2012."""
import copy
import docx
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

TEMPLATE = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\raw\adi-mpc-template-2026-09\4-pelaksanaan-kompilasi\3.3a Template Rangka Nota Pembelajaran (BM).docx"
OUTDIR = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\04 3.3a Rangka Nota Pembelajaran"
import os
os.makedirs(OUTDIR, exist_ok=True)

NOSS_TITLE = "IT-072-3:2012 VIDEO / FILM (EDITING) TAHAP 3"
JAWATAN = "Editor"

# (code, cu_title, [ (wa_code_title, [ (topic, [subtopics]) ]) ])
CUS = [
    ("C01", "Visual Editing Project Analysis", [
        ("WA1 — Analyse visual editing project script (IT-072-3:2012-C01-W01)", [
            ("Types of script", []),
            ("Project concept (Storyline, Message, Theme, Genre)", []),
            ("Type of audio (Dialogue, Voice Over, Music, Ambience)", []),
            ("Type of language version (Single/Bi/Multi language)", []),
            ("Project media output (Web, Tape, Film, Hardisk, DVD/Blu-ray, 3D Stereoscopic)", []),
            ("Project duration (Script requirement, Man hour requirement, Machine availability)", []),
            ("Editing technique in theory (Continuity cut, Jump cut, Parallel cut, Cross cut, Slow cut, Fast cut, Elliptical cut, Montage, Overlapping editing, Transition, Rhythmic editing, Graphical editing, Temporal editing, Spatial editing)", []),
        ]),
        ("WA2 — Analyse visual editing project concept (IT-072-3:2012-C01-W02)", [
            ("Category of genre (Action, Adventure, Comedy, Crime, Documentary, Fantasy, Historical, Horror, Mystery, dll.)", []),
            ("Types of genre — sub-genre penuh ikut kategori (Comedy, Action, Adventure, Crime, Documentary, Fantasy, Historical, Horror, Mystery, Paranoid, Philosophical, Political, Romance, Saga, Satire, Science fiction, Slice of life, Speculative, Thriller, Urban)", []),
            ("Category of theme (Life, Society, Human nature)", []),
            ("Visual effect (VFX) elements (concept design, creation, digital art assets, animation)", []),
            ("Sound effect (Hard sound, Background sound, Foley sound, Sound design)", []),
            ("Background music (Antecedents, Incidental, Furniture, Elevator, Ambient, Foreground)", []),
            ("Visualise editing technique (sama senarai teknik seperti WA1, digunakan dalam konteks konsep kreatif)", []),
        ]),
        ("WA3 — Classify visual editing format and sources (IT-072-3:2012-C01-W03)", [
            ("Project material (Tape, High Definition, Film, Stills/graphic, Tapeless Format, Archive)", []),
            ("Frame rate (24fps, 25fps, 50i, 29.97, 30fps, 23.976, 60i, HD Universal Timecode)", []),
            ("Scanning lines (Interlaced, Progressive)", []),
            ("Aspect ratio (4:3, 14:9, 16:9, Cinemascope, Anamorphic, Flat screen, Letter box, Pillar box, Wide screen)", []),
            ("Frame Dimension (1920x1080, 1440x1080, 1270x720, 720x576, 720x480)", []),
        ]),
        ("WA4 — Preview footage (IT-072-3:2012-C01-W04)", [
            ("Computer software and hardware (Application, Codec, Device)", []),
            ("Type of material (Tape, Data SD/HD, Film)", []),
            ("Required shot (Good takes, KIV takes)", []),
            ("Footage format conversion (Up conversion, Down conversion, Frame Rate Conversion)", []),
            ("Continuity sheet", []),
        ]),
        ("WA5 — Produce project workflow (IT-072-3:2012-C01-W05)", [
            ("Offline editing process", []),
            ("Online editing process", []),
            ("Project duration", []),
            ("Working schedule", []),
        ]),
    ]),
    ("C02", "Visual Editing Preparation", [
        ("WA1: Review cue sheet / continuity sheet / shooting board", [
            ("Bab 1 — Script", ["Peranan skrip dalam menentukan shot yang diperlukan", "Cara membaca skrip untuk tujuan penyuntingan"]),
            ("Bab 2 — Continuity Sheet", ["Fungsi continuity sheet dalam menjaga kesinambungan visual", "Cara membaca dan mentafsir continuity sheet"]),
            ("Bab 3 — Shooting Board", ["Fungsi shooting board berbanding storyboard", "Perkaitan shooting board dengan susunan shot sebenar"]),
            ("Bab 4 — DIT (Digital Imaging Technician) Sheet", ["Fungsi DIT sheet dalam merekod metadata footage", "Maklumat kritikal dalam DIT sheet untuk proses review"]),
        ]),
        ("WA2: Convert recorded materials / footage", [
            ("Bab 1 — Type of Editing Format (4K, 2K, HD, SD)", ["Ciri setiap format dan kesesuaian penggunaan", "Kesan pemilihan format terhadap proses editing"]),
            ("Bab 2 — Software and Hardware Specification", ["Keperluan minimum software/hardware bagi setiap format", "Padanan spesifikasi dengan projek"]),
            ("Bab 3 — Type of Compression Footages (Low resolution, High resolution, Uncompressed)", ["Kelebihan dan kekurangan setiap jenis mampatan", "Kesan mampatan terhadap kualiti dan storan"]),
        ]),
        ("WA3: Perform digitising / capturing recorded materials", [
            ("Bab 1 — Film Scanning", ["Konsep dan proses imbasan filem ke format digital"]),
            ("Bab 2 — Transfer Process (Telecine, broadcast equipment, data transfer/AV file types)", ["Soft vs hard telecine", "Peralatan broadcast (Digital Beta, DV Cam, HD Cam)", "Jenis fail AV: MOV, AVI, MXF, MP4"]),
            ("Bab 3 — Computer Software and Hardware", ["Keperluan sistem untuk capture/digitising"]),
            ("Bab 4 — Type of Format Material (Tape vs Tapeless)", ["Tape: HD CAM, Beta, DV CAM", "Tapeless: SDHC Card, P2 Card, SxS Card"]),
            ("Bab 5 — Type of Conversion Format", ["Down conversion 4K→HD, 4K→SD"]),
            ("Bab 6 — Type of Aspect Ratio Format", ["4:3, 16:9, Cinemascope, Anamorphic, Flat screen, Letter box, Wide screen"]),
        ]),
        ("WA4: Arrange scenes to respected bins", [
            ("Bab 1 — Editing Software", ["Fungsi bin dalam NLE (Non-Linear Editing) software"]),
            ("Bab 2 — Scene Coordination", ["Kaedah menyelaraskan scene mengikut turutan skrip/projek"]),
            ("Bab 3 — Bins Labelling", ["Konvensyen penamaan dan pelabelan bin"]),
        ]),
    ]),
    ("C03", "Offline Visual Editing", [
        ("WA1: Perform shot selection (IT-072-3:2012-C03-W01)", [
            ("Bab 1 Editing software", ["Kategori software (NLE): Final Cut Pro, Avid, Premiere Pro, Edius", "Fungsi asas berkaitan bin & pemilihan shot"]),
            ("Bab 2 Bins arrangement", ["Konsep bin dalam NLE", "Struktur bin ikut scene/hari rakaman"]),
            ("Bab 3 Good shots", ["Kriteria shot yang baik (fokus, pendedahan, komposisi, prestasi lakonan)", "Perbezaan good take vs no-good (NG)"]),
            ("Bab 4 Footages material (Tape & Tapeless)", ["Jenis media: HD CAM, Betacam, DV CAM (tape); SDHC, P2, SxS (tapeless)"]),
            ("Bab 5 Script", ["Peranan skrip dalam mengenal pasti shot yang diperlukan"]),
            ("Bab 6 Continuity sheet", ["Fungsi continuity sheet semasa pemilihan shot"]),
            ("Bab 7 Shooting board", ["Rujukan shooting board untuk susunan visual"]),
            ("Bab 8 DIT (Digital Imaging Technician) sheet", ["Fungsi DIT sheet dalam menjejak metadata footage"]),
        ]),
        ("WA2: Perform sequence timeline editing (IT-072-3:2012-C03-W02)", [
            ("Bab 1 Technique of editing", ["Continuity, Parallel, Overlapping, Temporal, Elliptical, Montage, Spatial, Rhythmic editing"]),
            ("Bab 2 Good shots", ["Semakan semula kriteria shot baik dalam konteks penyusunan sequence"]),
            ("Bab 3 Script", ["Rujukan skrip untuk turutan scene"]),
            ("Bab 4 Shooting board", ["Penjajaran sequence dengan shooting board"]),
            ("Bab 5 Editing software", ["FCP, Avid Media Composer/Symphony, Sony Vegas, Adobe Premiere Pro, Canopus Edius, AutoDesk Smoke"]),
        ]),
        ("WA3: Perform sequence timeline repairing (IT-072-3:2012-C03-W03)", [
            ("Bab 1 Technique of editing (sama senarai WA2)", []),
            ("Bab 2 Good shots", []),
            ("Bab 3 Script", []),
            ("Bab 4 Shooting board", []),
            ("Bab 5 Editing software (sama senarai WA2)", []),
            ("Bab 6 Timeline trimming", ["Cutting point, Shot trimming, Duration, Audio trimming"]),
        ]),
        ("WA4: Apply Audio Visual (AV) elements (IT-072-3:2012-C03-W04)", [
            ("Bab 1 Audio Visual (AV) elements", ["Visual effect, Audio effect/foley, Music background, Subtitle/language, Supers/title"]),
            ("Bab 2 Audio Visual (AV) specification", ["Broadcast spec; Digital Cinema Audio (DCA)"]),
        ]),
        ("WA5: Produce final offline (IT-072-3:2012-C03-W05)", [
            ("Bab 1 Offline timeline project", ["Semakan akhir sebelum online"]),
            ("Bab 2 Edit-Decision-List (EDL)", ["Fungsi dan format EDL"]),
            ("Bab 3 XML / AAF Import/Export Process", ["Proses eksport/import antara sistem editing"]),
            ("Bab 4 Editing software", ["Keserasian eksport EDL/XML/AAF antara NLE"]),
        ]),
    ]),
    ("C04", "Audio Sweetening", [
        ("WA1: Organise clean sound (IT-072-3:2012-C04-W01)", [
            ("Bab 1: Clean sound i.e.: Ambience, Dialogue", ["Definisi clean sound dan kepentingannya dalam sequence timeline", "Ambience vs Dialogue — ciri dan perbezaan"]),
            ("Bab 2: Audio signal i.e.: Frequency range, Waveform, Parameters", ["Frequency range bunyi manusia dan alat editing", "Membaca waveform dalam software editing"]),
            ("Bab 3: Audio editing techniques in editing software", ["Teknik asas pembersihan dan penyusunan trek audio"]),
        ]),
        ("WA2: Verify foley effect (IT-072-3:2012-C04-W02)", [
            ("Bab 1: Category foley effect i.e.: Feet, Prop, Cloth, etc", ["Kategori-kategori foley dan kegunaan masing-masing"]),
            ("Bab 2: Foley effect i.e.: Footstep, Hand props, Knock, Bang, etc", ["Contoh spesifik foley effect dan aplikasinya dalam sequence"]),
        ]),
        ("WA3: Carry out audio levelling (IT-072-3:2012-C04-W03)", [
            ("Bab 1: Types of audio i.e.: Voice Over, Dialogue", []),
            ("Bab 2: Audio level i.e.: Balancing, Mixing", []),
            ("Bab 3: Audio specification i.e.: Broadcast, Digital Cinema Audio (DCA)", []),
            ("Bab 4: Editing software i.e.: AVID Pro Tools, Adobe Audition, Adobe Soundbooth, Apple Sound Track Pro, etc", []),
        ]),
        ("WA4: Carry out music levelling (IT-072-3:2012-C04-W04)", [
            ("Bab 1: Music level i.e.: Balancing, Mixing", []),
            ("Bab 2: Music i.e.: Background, Composition", []),
            ("Bab 3: Standard audio specification i.e.: Broadcast, Digital Cinema Audio (DCA), etc", []),
            ("Bab 4: Editing software i.e.: AVID Pro Tools, Adobe Audition, Adobe Soundbooth, Apple Sound Track Pro, etc", []),
        ]),
        ("WA5: Carry out sound effect levelling (IT-072-3:2012-C04-W05)", [
            ("Bab 1: Sound effect level i.e.: Balancing, Mixing", []),
            ("Bab 2: Standard audio specification i.e.: Broadcast, Digital Cinema Audio (DCA)", []),
            ("Bab 3: Editing software i.e.: AVID Pro Tools, Adobe Audition, Adobe Soundbooth, Apple Sound Track Pro, etc", []),
        ]),
        ("WA6: Confirm audio balancing (IT-072-3:2012-C04-W06)", [
            ("Bab 1: Foley effect i.e.: Footstep, Hand props, Knock, Bang, etc", []),
            ("Bab 2: Clean sound i.e.: Ambience, Dialogue", []),
            ("Bab 3: Music i.e.: Background, Composition", []),
            ("Bab 4: Sound effects", []),
            ("Bab 5: Audio specification i.e.: Broadcast, Digital Cinema Audio (DCA)", []),
            ("Bab 6: Editing software i.e.: AVID Pro Tools, Adobe Audition, Adobe Soundbooth, Apple Sound Track Pro", []),
        ]),
    ]),
    ("C05", "Online Visual Editing", [
        ("WA1: Import Edit-Decision-List (EDL)", [
            ("Bab 1: Visual resolution i.e.: Negative cutting for online, Digitising HD tape for online, Reconnect AV clips (Tapeless)", ["Negative cutting untuk online", "Digitising HD tape untuk online", "Reconnect AV clips (tapeless workflow)"]),
            ("Bab 2: Sequence timeline / time code", ["Format timecode (SMPTE)", "Menyemak timeline sequence semasa import EDL"]),
            ("Bab 3: Sequence duration", ["Mengesahkan tempoh akhir sequence", "Punca percanggahan tempoh offline vs online"]),
        ]),
        ("WA2: Apply visual elements to editing sequences", [
            ("Bab 1: Visual elements i.e.: Motion graphic, Montage, Visual effects, Transition, Supers / title, Sub-title", ["Motion graphic", "Montage", "Visual effects", "Transition", "Supers / title dan sub-title"]),
        ]),
        ("WA3: Apply titling to editing sequences", [
            ("Bab 1: Editing sequence", ["Menyemak sequence sebelum titling", "Menentukan lokasi masuk/keluar title dalam sequence"]),
            ("Bab 2: Titling position i.e.: Safe area, Credit title, Opening sequence, Sub-title, Lower third", ["Safe area (title-safe / action-safe)", "Credit title dan opening sequence", "Sub-title", "Lower third"]),
        ]),
        ("WA4: Perform colour correction", [
            ("Bab 1: Understanding vectorscope and waveform", ["Fungsi waveform monitor", "Fungsi vectorscope"]),
            ("Bab 2: Visual colour enhancement i.e.: White balance, Brightness and contrast, Chroma colour, Temperature", ["White balance", "Brightness and contrast", "Chroma colour", "Colour temperature"]),
            ("Bab 3: Colour theme / concept", ["Mood dan tema warna projek", "Pematuhan spesifikasi broadcast/cinema"]),
        ]),
        ("WA5: Apply balanced audio to editing sequence", [
            ("Bab 1: Type of audio i.e.: Music, Sound effect, Foley effect, Voice Over, Dialogue", ["Music", "Sound effect dan Foley effect", "Voice Over dan Dialogue"]),
            ("Bab 2: Audio format i.e.: Uncompressed (AIFF, WAV, PCM); Lossless compression (Flec, ATRAC, MPEG 4, WMA Lossless); Lossy compression (MPEG 3, AAC, WMA Lossy)", ["Uncompressed audio", "Lossless compression", "Lossy compression"]),
        ]),
        ("WA6: Perform final online submission", [
            ("Bab 1: \"Double head\"", []),
            ("Bab 2: Broadcast equipment i.e.: Digital Beta, HD Cam", []),
            ("Bab 3: Film projector", []),
            ("Bab 4: Media player", []),
            ("Bab 5: Blu-ray", []),
            ("Bab 6: Type of final material i.e.: Tape, Data (SD / HD), Film", []),
            ("Bab 7: Type of supporting material i.e.: Script, Storyboard, Log book", []),
            ("Bab 8: Editing suite log book", []),
        ]),
    ]),
]


def set_cell_text(cell, lines):
    """Replace a cell's paragraphs with the given (text, bold) list, reusing the cell's first paragraph style/font."""
    p0 = cell.paragraphs[0]
    base_style = p0.style
    # clear existing paragraphs
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)
    p0.text = ""
    first = True
    for text, bold in lines:
        if first:
            p = p0
            first = False
        else:
            p = cell.add_paragraph()
        p.style = base_style
        run = p.add_run(text)
        run.bold = bold
        run.font.size = Pt(10.5)


def add_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = tblPr.find(qn('w:tblBorders'))
    if borders is None:
        borders = tbl.makeelement(qn('w:tblBorders'), {})
        tblPr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = borders.makeelement(qn(f'w:{edge}'), {
            qn('w:val'): 'single', qn('w:sz'): '4', qn('w:space'): '0', qn('w:color'): '000000'
        })
        borders.append(el)


def build_cu_doc(cu_code, cu_title, was, out_path):
    d = docx.Document(TEMPLATE)

    # 1. Restyle the title paragraph (index 0, style 'Title')
    title_p = d.paragraphs[0]
    assert title_p.style.name == "Title", title_p.style.name
    for r in list(title_p.runs):
        r.text = ""
    new_title = f"3.3a Rangka Nota Pembelajaran — IT-072-3:2012-{cu_code} {cu_title}"
    if title_p.runs:
        title_p.runs[0].text = new_title
    else:
        title_p.add_run(new_title)

    # 2. Remove all guideline body paragraphs (everything except the title paragraph)
    body = d.element.body
    keep = title_p._p
    to_remove = []
    for child in list(body):
        if child.tag == qn('w:p') and child is not keep:
            to_remove.append(child)
        elif child.tag == qn('w:tbl'):
            to_remove.append(child)
    for el in to_remove:
        body.remove(el)

    # 3. Header info table (5 cols: Kod Program, Tahap, Kod/Nama CU, Bil. WA, Tarikh)
    header_tbl = d.add_table(rows=2, cols=5)
    try:
        header_tbl.style = "Table Grid"
    except KeyError:
        add_table_borders(header_tbl)
    hdr_cells = header_tbl.rows[0].cells
    for c, txt in zip(hdr_cells, ["Kod Program", "Tahap", "Kod/Nama CU", "Bil. WA", "Tarikh"]):
        c.text = ""
        run = c.paragraphs[0].add_run(txt)
        run.bold = True
    val_cells = header_tbl.rows[1].cells
    values = ["IT-072-3:2012", "3", f"{cu_code} — {cu_title}", str(len(was)), ""]
    for c, txt in zip(val_cells, values):
        c.text = ""
        c.paragraphs[0].add_run(txt)

    d.add_paragraph("")

    # 4. Grab the template PROMPT-box table's format (1 row x 1 col) to clone per WA.
    #    We re-open the original template separately to steal a pristine copy of that table's XML.
    tsrc = docx.Document(TEMPLATE)
    prompt_tbl_xml = tsrc.tables[0]._tbl  # 1x1 prompt table

    for wa_title, topics in was:
        # heading
        h = d.add_paragraph()
        h.style = d.styles["Heading 2"]
        h.add_run(wa_title)

        # clone the prompt table
        new_tbl_xml = copy.deepcopy(prompt_tbl_xml)
        body.append(new_tbl_xml)
        new_table = d.tables[-1]
        cell = new_table.rows[0].cells[0]

        lines = [("PROMPT CHATGPT/AI", True)]
        lines.append((f"Syarikat saya [TBD: nama syarikat].", False))
        lines.append((f"Syarikat akan menawarkan program {NOSS_TITLE} kepada pekerja kami yang berkerja sebagai {JAWATAN}.", False))
        lines.append((f"Module: {cu_code} {cu_title}", False))
        lines.append((f"Work Activity: {wa_title}", False))
        lines.append(("Senarai topik nota yang berkenaan dengan work activity:", False))
        n = 1
        for topic, subs in topics:
            lines.append((f"{n} {topic}", False))
            for s in subs:
                lines.append((f"- {s}", False))
            n += 1

        set_cell_text(cell, lines)
        d.add_paragraph("")

    d.save(out_path)
    return out_path


if __name__ == "__main__":
    names = {
        "C01": "VISUAL EDITING PROJECT ANALYSIS",
        "C02": "VISUAL EDITING PREPARATION",
        "C03": "OFFLINE VISUAL EDITING",
        "C04": "AUDIO SWEETENING",
        "C05": "ONLINE VISUAL EDITING",
    }
    seq = {"C01": "01", "C02": "02", "C03": "03", "C04": "04", "C05": "05"}
    results = []
    for cu_code, cu_title, was in CUS:
        fname = f"3.3a-{seq[cu_code]} Rangka Nota Pembelajaran {cu_code} {names[cu_code]} (IT-072).docx"
        out_path = os.path.join(OUTDIR, fname)
        build_cu_doc(cu_code, cu_title, was, out_path)
        results.append((out_path, len(was)))

    print("=== BUILD RESULTS ===")
    for path, n in results:
        print(n, path)
