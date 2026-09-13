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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-server-configuration

**TUJUAN:** Kertas rujukan untuk PA-server-configuration.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This is a PRACTICAL examination. You will be assessed on your ability to perform a complete server configuration cycle from requirements analysis through to formal handover documentation.
2. You will be given a scenario brief, a physical or virtualised server, and all required resources. You must complete all six work activities.
3. You will be assessed on: **Process** (methodology and sequence), **Output** (quality and completeness of deliverables), **Attitude** (professionalism and independent decision-making), **Safety** (hardware safety and security practices), and **Environmental** compliance (workspace and documentation management).
4. No assistance is permitted from the instructor unless there is a safety hazard.
5. All commands executed and their outputs must be recorded as evidence.

---

## Arahan kepada Penilai / Instructions to Assessor

- Provide each trainee with the scenario brief, a server (physical or VM lab), all required hardware and software access, and the documentation templates.
- Observe each trainee continuously and mark criteria as work is performed — do not assess retrospectively from the final output alone.
- Do NOT provide technical guidance. Redirect safety hazards only.
- Verify all deliverables (configuration records, command outputs, handover document) at the end.
- Mark the assessment rubric sections in order: complete WA1–WA2 assessment before the trainee begins hardware work; complete WA3–WA5 assessment during practical configuration; complete WA6 at handover.

---

## Senario Penilaian / Assessment Scenario

**Scenario:** You are a Level 4 IT Administrator at Pioneer Academy, a private educational institution. You have been assigned to deploy a new server (SRV-ASSESS01) as a domain controller and DHCP server for a branch campus with 150 users.

| Field | Details |
|-------|---------|
| Server | Dell PowerEdge R450 (or equivalent lab server / VM) |
| Required roles | Active Directory Domain Services, DNS, DHCP |
| Domain | assess.pioneer.edu.my |
| Production IP | 10.0.2.10 / 24, Gateway 10.0.2.1 |
| iDRAC / Management IP | 10.0.20.10 / 24 |
| OS | Windows Server 2022 Standard |
| User count | 150 users (students and staff) |
| Data residency | Malaysia only (PDPA 2010 applies) |
| Time allowed | 6 hours total |

**Deliverables required:**
1. Requirements Summary (minimum 8 requirements categorised and prioritised)
2. Server Role Plan (role allocation, capacity calculations, network topology diagram)
3. RAID Configuration Worksheet (completed from hardware configuration)
4. Completed Server Configuration Record (all 7 sections)
5. As-Built Document (with deviations and acceptance test results)
6. Signed Handover Checklist

---

## Rubrik Penilaian / Assessment Rubric

### WA1 — Analyse Server Configuration Requirements (15 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 1.1 | Reads the scenario brief completely before beginning any work | 2 | |
| 1.2 | Identifies a minimum of 3 stakeholder groups and lists relevant questions for each | 3 | |
| 1.3 | Extracts minimum 8 requirements; all correctly categorised as Business, Technical, or Compliance | 4 | |
| 1.4 | Applies MoSCoW prioritisation with justification to all requirements | 3 | |
| 1.5 | Identifies at least 2 gaps or ambiguities requiring clarification before planning | 3 | |
| | **Subtotal WA1** | **15** | |

### WA2 — Plan Server Roles and Services (15 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 2.1 | All required server roles identified and justified | 3 | |
| 2.2 | Capacity calculations shown: CPU (with utilisation %), RAM (correct rule applied), Storage (RAID overhead + 3-year growth + buffer) | 6 | |
| 2.3 | Network topology diagram drawn with IP addresses, VLANs, and server placement | 3 | |
| 2.4 | Redundancy mechanism identified for the Domain Controller role | 3 | |
| | **Subtotal WA2** | **15** | |

### WA3 — Configure Server Hardware and Storage (20 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 3.1 | iDRAC/iLO default credentials changed; static management IP assigned | 3 | |
| 3.2 | Hardware health verified via iDRAC — no critical errors in System Event Log | 2 | |
| 3.3 | BIOS/UEFI: UEFI mode, Secure Boot, VT-x, and C-States configured correctly per checklist | 5 | |
| 3.4 | OS logical drive (RAID 1) created and shows Optimal status | 4 | |
| 3.5 | DATA logical drive created with correct RAID level per plan | 4 | |
| 3.6 | Hot spare configured; BBWC/FBWC status verified | 2 | |
| | **Subtotal WA3** | **20** | |

### WA4 — Configure Server OS and Roles (20 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 4.1 | OS installed on correct volume; complex Administrator password set | 2 | |
| 4.2 | Post-installation steps completed in correct order: IP, rename, timezone, NTP, RDP, WinRM, updates | 5 | |
| 4.3 | AD DS role installed; server promoted to DC for assess.pioneer.edu.my | 4 | |
| 4.4 | `dcdiag /v` run — ALL tests PASSED (or failing tests identified and resolved) | 3 | |
| 4.5 | DNS forward and reverse zones present; forwarders configured; name resolution verified | 3 | |
| 4.6 | DHCP installed, authorised in AD, scope configured, and lease verified from client | 3 | |
| | **Subtotal WA4** | **20** | |

### WA5 — Implement Server Security Settings (15 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 5.1 | Windows Firewall default-deny inbound applied; role-specific rules created | 3 | |
| 5.2 | Password policy GPO applied: minimum 14 characters, complexity, 90-day max age | 3 | |
| 5.3 | Account lockout policy: 5 attempts, 30-minute duration | 2 | |
| 5.4 | Advanced audit policy enabled for required categories; Event IDs 4624/4625 verified in Security log | 4 | |
| 5.5 | Built-in Administrator renamed; Guest account disabled | 2 | |
| 5.6 | NTLMv2-only authentication enforced via GPO | 1 | |
| | **Subtotal WA5** | **15** | |

### WA6 — Document Server Configuration (15 marks)

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| 6.1 | Server Configuration Record complete — all 7 sections filled with actual values; no blank fields | 5 | |
| 6.2 | As-Built Document includes: deviations from plan (if any), acceptance test results, known issues | 4 | |
| 6.3 | Document version v1.0 with correct header; stored in team-accessible location (or designated share) | 2 | |
| 6.4 | Handover walkthrough conducted — all five required topics covered; instructor questions answered satisfactorily | 4 | |
| | **Subtotal WA6** | **15** | |

---

## Ringkasan Markah / Score Summary

| Work Activity | Maximum | Score |
|--------------|---------|-------|
| WA1 — Analyse Requirements | 15 | |
| WA2 — Plan Roles and Services | 15 | |
| WA3 — Configure Hardware and Storage | 20 | |
| WA4 — Configure OS and Roles | 20 | |
| WA5 — Implement Security Settings | 15 | |
| WA6 — Document Configuration | 15 | |
| **TOTAL** | **100** | |

---

## Keputusan / Result

**Pass mark: 60 / 100. All WA subtotals must achieve minimum 40% of the WA maximum marks (i.e. no WA may score zero — all work activities must be attempted and produce at least a partial outcome).**

| | |
|---|---|
| **Kompeten / Competent** | [ ] |
| **Belum Kompeten / Not Yet Competent (NYC)** | [ ] |

---

## Pengesahan / Verification

| | Name | Qualification | Signature | Date |
|---|------|--------------|-----------|------|
| Trainee | | | | |
| Assessor 1 | | | | |
| Assessor 2 (if applicable) | | | | |
| Internal Verifier | | | | |

---

## Ulasan / Comments

*(Assessor: record specific strengths, areas for improvement, and any critical non-compliance. NYC candidates must be told which WAs require re-assessment and given a re-assessment date.)*

| Strength areas: |
|---|
| |
| |

| Areas for improvement: |
|---|
| |
| |

| Critical non-compliance (if any): |
|---|
| |

| Re-assessment date (NYC only): |
|---|
| |