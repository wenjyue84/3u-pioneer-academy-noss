<!-- JPK_ENVELOPE_v1 -->
<table border="0" cellspacing="0" cellpadding="8" width="100%">
<tr>
<td width="130" valign="top"><img src="../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>
<td valign="middle">
<b>JABATAN PEMBANGUNAN KEMAHIRAN (JPK)</b><br>
TINGKAT 7-8, BLOK D4, KOMPLEKS D,<br>
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,<br>
62530 PUTRAJAYA
</td>
</tr>
</table>

## KERTAS PENILAIAN PRESTASI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-server-installation

**TUJUAN:** Kertas rujukan untuk PA-server-installation.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This is a PRACTICAL examination. You will be assessed on your ability to perform a complete server installation.
2. You will be given a job order, server hardware, rack equipment, installation media, and tools. You must complete the full installation cycle.
3. You will be assessed on: **Process** (how you do it), **Output** (the result), **Attitude** (professionalism), **Safety** (ESD, electrical, and rack safety), and **Environmental** compliance.
4. You must wear an anti-static wrist strap throughout all hardware handling phases.
5. All work must be documented on the provided server installation set-up report form.
6. Total time allowed: **4 hours**.

---

## Arahan kepada Penilai / Instructions to Assessor

- Provide each trainee with a designated rack unit, server chassis, hardware components, tools, and a simulated job order.
- Observe each trainee continuously during the assessment.
- Do NOT assist the trainee unless there is a safety hazard.
- Mark each criterion on the assessment rubric as the trainee works.
- Verify the final output (operational server, completed set-up report) at the end of the session.

---

## Tugasan / Task Description

**Scenario:** You are a Level 3 Computer System Technician assigned to the IT infrastructure team. You receive the following server installation job order:

| Field | Details |
|-------|---------|
| Job order number | PA-C04-2026-001 |
| Requested by | IT Infrastructure Manager |
| Priority | High |
| Description | Install a new rack-mount server for departmental file sharing |
| Form factor | 1U or 2U rack-mount (as available in lab) |
| CPU | 1 x server-grade CPU (as provided) |
| RAM | ECC RAM modules (as provided) |
| Storage | RAID 1 using 2 drives (as provided) |
| NIC | 1 x built-in or add-in NIC |
| OS | Windows Server 2022 or Linux (as directed by assessor) |
| Role | File server |
| Rack position | As assigned by assessor |
| Network | Static IP as provided by assessor |
| Deadline | Within assessment session |

**You must complete the following tasks in sequence:**

1. Analyse the job order and perform pre-installation checks (20 minutes)
2. Mount server rails and rack the server chassis (20 minutes)
3. Install CPUs, RAM, and storage drives; configure RAID (60 minutes)
4. Install OS and configure server roles and network settings (60 minutes)
5. Conduct server functionality tests (30 minutes)
6. Prepare the server installation set-up report and present to assessor (30 minutes)

**Total time allowed: 4 hours**

---

## Rubrik Penilaian / Assessment Rubric

### WA1 — ANALISIS JOB ORDER / ANALYSE JOB ORDER (10 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| W1.1 | Reviews and interprets all fields of the job order before commencing work | 3 | |
| W1.2 | Identifies hardware requirements and performs compatibility checks (CPU socket, RAM type, RAID configuration) | 4 | |
| W1.3 | Verifies rack space availability and documents pre-installation checklist | 3 | |
| | **Subtotal WA1** | **10** | |

### WA2 — PEMASANGAN PERKAKASAN / EXECUTE HARDWARE INSTALLATION (30 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| W2.1 | Installs rack rails correctly; server slides in and locks without force | 5 | |
| W2.2 | Installs CPU(s) correctly — correct orientation, no bent pins, retention lever fully engaged | 5 | |
| W2.3 | Applies thermal interface material correctly; heatsink mounted securely | 5 | |
| W2.4 | Installs RAM in correct slots; modules fully seated | 5 | |
| W2.5 | Installs storage drives and configures RAID via RAID controller BIOS or HBA utility | 5 | |
| W2.6 | Connects all internal cables (power, data, front panel) neatly; manages cable routing | 5 | |
| | **Subtotal WA2** | **30** | |

### WA3 — PEMASANGAN PERISIAN / CARRY OUT SOFTWARE INSTALLATION (25 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| W3.1 | Configures BIOS/UEFI correctly — boot order, virtualisation, RAID mode, time/date | 5 | |
| W3.2 | Installs OS successfully; server boots to login screen without errors | 8 | |
| W3.3 | Installs all required drivers (chipset, NIC, RAID/storage controller) in correct order | 7 | |
| W3.4 | Configures server role (file sharing) and assigns static IP address as per job order | 5 | |
| | **Subtotal WA3** | **25** | |

### WA4 — UJIAN FUNGSI PELAYAN / PERFORM SERVER FUNCTIONALITY TEST (15 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| W4.1 | Verifies all hardware is detected correctly (no unknown devices in Device Manager / `lspci`) | 5 | |
| W4.2 | Tests network connectivity — pings gateway and a remote host successfully | 5 | |
| W4.3 | Tests server role — demonstrates file share is accessible from a client machine or confirms service is running | 5 | |
| | **Subtotal WA4** | **15** | |

### WA5 — LAPORAN PEMASANGAN / PREPARE SET-UP REPORT (10 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| W5.1 | Report includes all required sections: hardware inventory, RAID configuration, OS version, IP settings, test results, sign-off | 5 | |
| W5.2 | Report is accurate, legible, and presented to assessor with verbal explanation | 5 | |
| | **Subtotal WA5** | **10** | |

---

## Ringkasan Markah / Score Summary

| Bahagian / Section | Markah Maksimum / Maximum | Markah Diperoleh / Score |
|--------------------|--------------------------|--------------------------|
| WA1 — Analyse Job Order | 10 | |
| WA2 — Hardware Installation | 30 | |
| WA3 — Software Installation | 25 | |
| WA4 — Server Functionality Test | 15 | |
| WA5 — Set-Up Report | 10 | |
| **Jumlah / TOTAL** | **90** | |

> **Nota:** Markah tambahan 10 markah diperuntukkan untuk Keselamatan & Sikap (Safety & Attitude) — lihat bahagian berikut.

### KESELAMATAN & SIKAP / SAFETY & ATTITUDE (10 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| S1 | Wears anti-static wrist strap during all hardware handling; power disconnected before opening chassis | 4 | |
| S2 | Handles components by edges; correct torque applied to rack screws; no dropped components | 3 | |
| S3 | Workspace clean and organised throughout; tools and packaging properly managed | 3 | |
| | **Subtotal Safety & Attitude** | **10** | |

---

## Markah Keseluruhan / Grand Total

| | Markah / Marks |
|---|---|
| WA1–WA5 Subtotal | / 90 |
| Safety & Attitude | / 10 |
| **JUMLAH KESELURUHAN / GRAND TOTAL** | **/ 100** |

---

## Keputusan / Result

| | |
|---|---|
| **Kompeten / Competent (C)** — 60 marks and above | [ ] |
| **Belum Kompeten / Not Yet Competent (NYC)** — below 60 marks | [ ] |

---

## Pengesahan / Verification

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| Pelatih / Trainee | | | |
| Penilai 1 / Assessor 1 | | | |
| Penilai 2 / Assessor 2 (jika berkaitan) | | | |
| Pengesah Dalaman / Internal Verifier | | | |

---

## Ulasan / Comments

*(Penilai hendaklah memberikan maklum balas mengenai kekuatan, bidang penambahbaikan, dan sebarang ketidakpatuhan kritikal yang diperhatikan.)*

|  |
|---|
|  |
|  |
|  |