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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-security-control

**TUJUAN:** Kertas rujukan untuk PA-security-control.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. Ini adalah peperiksaan PRAKTIKAL. Anda akan dinilai berdasarkan keupayaan anda melaksanakan kawalan keselamatan sistem komputer secara menyeluruh.
2. Anda akan diberikan persekitaran makmal (Windows Server 2022 + Windows 11 workstation) dan satu set keperluan keselamatan. Anda mesti melaksanakan semua tugasan yang ditetapkan.
3. Anda akan dinilai berdasarkan: **Proses** (cara pelaksanaan), **Hasil** (output yang dihasilkan), **Sikap** (profesionalisme), **Keselamatan** (amalan kerja selamat), dan **Dokumentasi** (rekod konfigurasi dan laporan insiden).
4. Semua kerja mesti didokumentasikan dalam borang yang disediakan.
5. Masa dibenarkan: **5 jam**.

---

## Arahan kepada Penilai / Instructions to Assessor

- Sediakan persekitaran makmal: Windows Server 2022 (domain controller or standalone), Windows 11 workstation (domain-joined), dan Kali Linux VM (isolated lab network).
- Berikan kepada setiap pelatih: security requirements brief, blank configuration record, blank patch register, blank incident report, and incident scenario brief.
- Perhatikan setiap pelatih secara berterusan semasa penilaian.
- JANGAN membantu pelatih kecuali terdapat bahaya keselamatan.
- Tandakan setiap kriteria dalam rubrik penilaian semasa pelatih bekerja.
- Sahkan semua output akhir sebelum menandatangani borang penilaian.

---

## Tugasan / Task Description

**Scenario:** You are the systems administrator for Syarikat Niaga Bestari Sdn Bhd, a retail company with 60 staff. You have been instructed by the IT Manager to implement the following security controls on the company's Windows Server 2022 and verify compliance. After completing the implementation, you will be given an incident scenario to handle and document.

### Security Requirements Brief

| Requirement | Detail |
|-------------|--------|
| User roles | Finance User, HR Manager, IT Administrator, General Staff (4 roles) |
| Password policy | Minimum 12 characters, complexity enabled, max age 90 days, history 10 |
| Account lockout | 5 attempts, 30-minute duration, reset after 15 minutes |
| Firewall rules | Block Telnet (TCP 23); restrict RDP (TCP 3389) to admin IP only; allow HTTPS (TCP 443) |
| Patch status | All Critical and Important updates approved and installed |
| Audit logging | Logon, Account Management, Object Access, Policy Change — Success + Failure |
| Documentation | Security configuration baseline record + hardening checklist completed |

**Task sequence (complete in order):**

1. Security requirements analysis and RBAC design (30 minutes)
2. User accounts and access control configuration (60 minutes)
3. Firewall configuration and attack surface reduction (60 minutes)
4. Patch management verification and patch register (45 minutes)
5. Audit logging configuration and verification (30 minutes)
6. Security configuration baseline record and hardening checklist (30 minutes)
7. Incident response — handle and document the simulated incident (45 minutes)

**Total time allowed: 5 hours**

---

## Rubrik Penilaian / Assessment Rubric

### A. PROSES (Process) — 30 markah

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| A1 | Conducts security requirements analysis systematically before beginning implementation; identifies assets, threats, and required controls | 5 | |
| A2 | Designs and implements RBAC structure correctly: OUs, groups, users, and folder permissions aligned to role requirements | 6 | |
| A3 | Configures Windows Defender Firewall rules correctly with appropriate justification for each rule | 5 | |
| A4 | Verifies patch compliance using PowerShell and WSUS/Windows Update; documents findings in patch register | 5 | |
| A5 | Enables and verifies audit logging for all required categories; generates and locates test events in Event Viewer | 5 | |
| A6 | Follows a logical, systematic sequence throughout; does not skip steps or proceed without verifying previous step | 4 | |
| | **Subtotal Process** | **30** | |

### B. HASIL (Output) — 30 markah

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| B1 | User accounts and security groups created correctly; group memberships match role requirements | 5 | |
| B2 | NTFS folder permissions correctly configured; access control verified by login test | 5 | |
| B3 | Password policy and account lockout GPO applied and verifiable via `gpresult /r` | 5 | |
| B4 | Firewall rules correctly configured: RDP restricted to admin IP, Telnet blocked, HTTPS allowed | 5 | |
| B5 | All Critical/Important patches verified as installed; patch register complete with KB numbers, dates, and compliance status | 5 | |
| B6 | Security configuration baseline record and hardening checklist completed accurately for the assessed server | 5 | |
| | **Subtotal Output** | **30** | |

### C. SIKAP (Attitude) — 15 markah

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| C1 | Works independently without requesting assistance except when genuinely needed | 5 | |
| C2 | Demonstrates attention to detail: verifies each configuration step before proceeding | 5 | |
| C3 | Communicates clearly during incident response and report presentation; justifies decisions professionally | 5 | |
| | **Subtotal Attitude** | **15** | |

### D. KESELAMATAN KERJA (Work Safety) — 15 markah

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| D1 | Records pre-change state before making any configuration change; follows change management discipline | 5 | |
| D2 | Does not disable critical domain services; does not make changes outside the designated training OU/scope | 5 | |
| D3 | Logs off all sessions when not actively working; does not leave administrator credentials exposed | 5 | |
| | **Subtotal Work Safety** | **15** | |

### E. DOKUMENTASI (Documentation) — 10 markah

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| E1 | Incident report completed for all required sections; timeline cites specific Event IDs and timestamps | 5 | |
| E2 | All configuration records (baseline, hardening checklist, patch register, firewall rule register) submitted, complete, and signed | 5 | |
| | **Subtotal Documentation** | **10** | |

---

## Ringkasan Markah / Score Summary

| Bahagian / Section | Maksimum / Maximum | Markah / Score |
|--------------------|-------------------|---------------|
| A. Proses / Process | 30 | |
| B. Hasil / Output | 30 | |
| C. Sikap / Attitude | 15 | |
| D. Keselamatan Kerja / Work Safety | 15 | |
| E. Dokumentasi / Documentation | 10 | |
| **JUMLAH / TOTAL** | **100** | |

---

## Keputusan / Result

| | |
|---|---|
| **Kompeten / Competent** | [ ] |
| **Belum Kompeten / Not Yet Competent** | [ ] |

**Markah lulus minimum / Minimum passing score: 70/100**

*(Note: The minimum passing score for Performance Assessment is set at 70% to reflect the practical and safety-critical nature of security configuration work.)*

---

## Pengesahan / Verification

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|--------------|
| Pelatih / Trainee | | | |
| Penilai 1 / Assessor 1 | | | |
| Penilai 2 / Assessor 2 (jika berkenaan) | | | |
| Pengesah Dalaman / Internal Verifier | | | |

---

## Ulasan Penilai / Assessor Comments

*(Penilai hendaklah memberi maklum balas mengenai kekuatan, bidang penambahbaikan, dan sebarang ketidakpatuhan kritikal yang diperhatikan. / Assessor to provide feedback on strengths, areas for improvement, and any critical non-compliance observed.)*

| |
|---|
| |
| |
| |
| |
| |