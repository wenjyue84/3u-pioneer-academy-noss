import os, shutil

OUTDIR = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\07 3.4b Soalan Penilaian Pengetahuan\Core Abilities L1-L3 (format JPK)"
TMPDIR = r"C:\tmp_juno_ca_soalan"

items = [
    ("01", "1", "CA01", "BASIC WORKING COMMUNICATION"),
    ("02", "1", "CA02", "PERSONAL BEHAVIOUR SKILL"),
    ("03", "1", "CA03", "WORK PLACE ETHICS AWARENESS"),
    ("04", "1", "CA04", "SAFETY HEALTH AND ENVIRONMENT AWARENESS"),
    ("05", "2", "CA01", "COMMUNICATION APPLICATION"),
    ("06", "2", "CA02", "INTERPERSONAL BEHAVIOUR"),
    ("07", "2", "CA03", "WORK PLACE CULTURE BEHAVIOUR"),
    ("08", "2", "CA04", "HEALTH SAFETY AND ENVIRONMENTAL ADAPTATION"),
    ("09", "3", "CA01", "EFFECTIVE COMMUNICATION"),
    ("10", "3", "CA02", "INFORMATION TECHNOLOGY AWARENESS"),
    ("11", "3", "CA03", "LEADERSHIP SKILL"),
    ("12", "3", "CA04", "WORK PLACE ETHICS"),
    ("13", "3", "CA05", "ADMINISTRATIVE SKILL"),
    ("14", "3", "CA06", "HSE CONSCIOUSNESS"),
]

os.makedirs(OUTDIR, exist_ok=True)
mapping = []
for seq, level, ca, title in items:
    src = os.path.join(TMPDIR, f"CA-{seq}.docx")
    fname = f"SOALAN-CA-{seq} Z-009-{level}-2015 {ca} SOALAN PENILAIAN {title} (IT-072).docx"
    dst = os.path.join(OUTDIR, fname)
    shutil.copy2(src, dst)
    mapping.append((seq, dst))
    print(dst)
