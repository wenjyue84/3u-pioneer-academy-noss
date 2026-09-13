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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C05 COMPUTER NETWORK INSTALLATION MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION<br>2. PLAN COMPUTER NETWORK INSTALLATION<br>3. MANAGE COMPUTER NETWORK INSTALLATION WORK<br>4. PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C05/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-supervising-network-installation-work

**TUJUAN:** Kertas rujukan untuk KK-03-supervising-network-installation-work.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Act as the network installation site supervisor for a simulated installation exercise: conduct site inspections, identify workmanship deficiencies, manage a simulated change request, perform cable certification testing, and conduct network connectivity acceptance testing.

---

## Tempoh / Duration

6 hours (distributed across multiple lab sessions)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Simulated installation site (training lab configured with pre-installed cables and equipment) | 1 |
| 2 | Site Inspection Checklist template | 1 |
| 3 | Non-Conformance Report (NCR) template | 1 |
| 4 | Change Request (CR) form template | 1 |
| 5 | Cable certification tester (e.g., Fluke MicroScanner or equivalent) | 1 (shared) |
| 6 | Laptop with network management access | 1 |
| 7 | Cable schedule (from KK-02 planning exercise) | 1 |
| 8 | Progress tracking sheet | 1 |
| 9 | Camera or smartphone for photographic documentation | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Wear appropriate PPE for the site walk-through (safety shoes, hi-visibility vest if applicable)
- Do not connect live power to any equipment without instructor approval
- When using the cable tester, do not inject signal onto a live network port — verify the port is isolated first
- Report all safety observations to the instructor; do not attempt to correct electrical hazards yourself

---

## Prosedur / Procedures

### Bahagian A: Site Inspection / Pemeriksaan Tapak (2 hours)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| A1 | Receive the Site Inspection Checklist from the instructor. The training lab has been pre-configured with intentional deficiencies (at least 5) for you to identify. |
| A2 | Conduct a systematic inspection of the installed cabling using the checklist. For each item: observe the actual condition; record your observation; mark as COMPLIANT or NON-COMPLIANT. |
| A3 | Photograph each non-compliant item. Note the location (e.g., "IDF-1 Rack, patch panel Row 2, Port 14") and the specific deficiency (e.g., "excessive untwist length at punch-down, approximately 25 mm — exceeds 13 mm limit"). |
| A4 | For each non-compliant item, complete a Non-Conformance Report (NCR) using the template provided. The NCR must state: location, deficiency description, photograph reference, required corrective action, and deadline for re-inspection. |
| A5 | Verbally brief the "contractor" (a fellow trainee designated by the instructor) on the NCRs. Explain what must be corrected and by when. |

### Bahagian B: Change Request Management / Pengurusan Permohonan Perubahan (1 hour)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| B1 | The instructor will present a simulated change request from the client: "The client has requested 3 additional network points in the newly partitioned meeting room on Floor 2, not in the original specification." |
| B2 | Complete the Change Request (CR) form: describe the change, the reason, and assess the impact on scope, cost (estimate), and schedule (how many additional days). |
| B3 | Determine whether the change should be approved, rejected, or deferred. Write your recommendation with justification (minimum 3 sentences). |
| B4 | If approved, prepare a draft Variation Order (VO) authorising the additional work. State what the BoQ items that will be added are and the estimated cost. |

### Bahagian C: Cable Certification Testing / Ujian Pensijilan Kabel (2 hours)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| C1 | Receive the cable certification tester and the cable schedule. The instructor will assign a set of 10 cable runs for testing. |
| C2 | Set up the tester: configure for Cat6A Channel test, TIA-568 standard. Verify the tester's calibration date is current. |
| C3 | Test each assigned cable run. For each run: connect the tester at the patch panel end and the remote unit at the outlet end. Run the AUTOTEST. Record the result (PASS/FAIL) and the key measured values (length, worst-case NEXT, insertion loss) on the test record sheet. |
| C4 | For any FAIL result: identify the likely cause from the tester's diagnostic display (e.g., wire map error, excessive length, NEXT failure). Document the likely cause and the corrective action required. |
| C5 | Export the test results to the test record sheet. Calculate the pass rate (number PASS / total tested × 100%). |

### Bahagian D: Network Connectivity Acceptance Testing / Ujian Penerimaan Sambungan Rangkaian (1 hour)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| D1 | Connect a test laptop to the designated access port. Verify that an IP address is received via DHCP. Record: assigned IP, subnet mask, default gateway, DNS server. |
| D2 | Perform a ping test to: (a) the default gateway; (b) an IP address in a different VLAN (that should be blocked by the firewall). Record results. |
| D3 | Connect to the switch management interface (using instructor-provided credentials). Verify: the correct VLAN is assigned to the test port; the port is up at the expected speed (1000BASE-T or 10GBASE-T as applicable). |
| D4 | Test internet connectivity: open a browser and load a known website. Record whether access is successful. |
| D5 | Complete the Network Connectivity Test Record (Table A below) for all test items. |

---

## Table A: Network Connectivity Test Record / Rekod Ujian Sambungan Rangkaian

| No. | Test | Expected Result | Actual Result | Pass / Fail |
|-----|------|-----------------|--------------|-------------|
| 1 | DHCP IP assignment from access port | IP in correct subnet received | | |
| 2 | Ping to default gateway | Reply received; 0% loss | | |
| 3 | Ping to isolated VLAN | No reply (blocked by firewall) | | |
| 4 | Internet access (HTTP/HTTPS) | Pages load successfully | | |
| 5 | Switch port VLAN assignment verified | Correct VLAN tag confirmed | | |
| 6 | Switch port speed confirmed | 1000 Mbps or 10 Gbps as specified | | |

---

## Hasil Jangkaan / Expected Outcome

- Completed Site Inspection Checklist with all deficiencies identified and photographed
- Minimum 3 NCR forms completed and briefed to the contractor
- Completed Change Request form with recommendation and draft Variation Order
- Cable test records for 10 runs with pass/fail results and pass rate calculated
- Completed Network Connectivity Test Record

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Site inspection conducted systematically using checklist | [ ] Yes [ ] No |
| 2 | All deficiencies identified, photographed, and documented on NCR forms | [ ] Yes [ ] No |
| 3 | NCRs briefed to the contractor (fellow trainee) professionally | [ ] Yes [ ] No |
| 4 | Change Request form completed with cost and schedule impact assessed | [ ] Yes [ ] No |
| 5 | Draft Variation Order prepared if change approved | [ ] Yes [ ] No |
| 6 | Cable tester set up correctly (Cat6A, TIA-568, calibration verified) | [ ] Yes [ ] No |
| 7 | All 10 cable runs tested; results recorded with key values | [ ] Yes [ ] No |
| 8 | FAIL causes identified and corrective actions stated | [ ] Yes [ ] No |
| 9 | Network connectivity tests completed; Test Record table fully completed | [ ] Yes [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |