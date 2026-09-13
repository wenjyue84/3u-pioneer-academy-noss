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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KK(2/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-planning-server-roles-and-services

**TUJUAN:** Kertas rujukan untuk KK-02-planning-server-roles-and-services.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Design a server role architecture for a given organisation scenario, produce a capacity-planned Server Role Plan document, and present the design rationale to the instructor.

---

## Tempoh / Duration

6 hours (practical session)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Verified Requirements Summary from KK-01 (or instructor-provided) | 1 |
| 2 | Server role planning worksheet template | 1 |
| 3 | Capacity planning worksheet (CPU, RAM, storage sizing tables) | 1 |
| 4 | Network topology diagram template (Visio, draw.io, or paper) | 1 |
| 5 | Computer with word processor, spreadsheet, and diagramming software | 1 |
| 6 | Reference: KP-02 (Server Roles and Services Planning) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Validate all capacity calculations before committing to a hardware specification — undersized servers cause production failures
- Document all assumptions clearly; a design based on an incorrect assumption is a design risk
- Save all work files with versioned filenames; do not overwrite previous versions

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Review the Requirements Summary (from KK-01 or as provided). List all server roles required by the organisation based on the stated requirements. For each role, note: the service it provides, the OS platform (Windows/Linux), and whether it will be a physical server or a VM. |
| 2 | Decide on the architecture model: dedicated physical servers, consolidated virtualisation cluster, or hybrid. Justify your decision based on the scenario's user count, budget indication, and availability requirements. Reference the decision guide in KP-02 Section 3.3. |
| 3 | For each server (physical host or major VM), complete the capacity planning calculation: (a) CPU: estimate required vCPUs or physical cores at ≤70–80% utilisation; (b) RAM: apply the RAM planning rules from KP-02 Section 4.2; (c) Storage: calculate usable capacity = current data volume × (1 + annual growth rate)³, then add 20–30% free buffer. Show all calculations explicitly. |
| 4 | Design the network topology. Assign IP addresses and VLANs. At minimum, define: Production VLAN (user and server traffic), Management VLAN (iDRAC/iLO and admin access). Draw the topology diagram showing servers, switches, VLANs, and firewall zones. |
| 5 | Design the availability architecture. For each critical role (Domain Controller, core application), identify the redundancy mechanism: second DC, failover cluster, VM HA, or load balancer. Document what happens to each service if the primary server fails. |
| 6 | Compile the OS and licensing plan. For each server, state the OS edition, the licensing model (retail, OEM, volume/KMS, subscription), and the estimated licence cost. Confirm that the licensing model supports the intended deployment (e.g. Windows Server Standard supports 2 VMs per licence). |
| 7 | Produce the Server Role Plan document containing: role inventory table, server allocation table, capacity planning calculations, network topology diagram, availability design summary, OS and licensing table, and a proposed project timeline (procurement → installation → commissioning). |
| 8 | Prepare a 5-minute verbal presentation of your design for the instructor. Cover: (a) the architecture model chosen and why, (b) one key design decision (e.g. RAID level for database server) and its justification, (c) the biggest risk in the plan and how you have mitigated it. |
| 9 | Present to the instructor and answer clarification questions. |
| 10 | Revise the Server Role Plan based on instructor feedback; submit the final version. Complete the assessment checklist. |

---

## Hasil Dijangka / Expected Outcome

- A complete Server Role Plan document with all required sections
- Explicit, verifiable capacity calculations for CPU, RAM, and storage
- A network topology diagram showing VLANs, IP addressing, and server placement
- A verbal design presentation demonstrating understanding of rationale, not just outputs

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | All required server roles identified and justified | [ ] Yes  [ ] No |
| 2 | Architecture model (physical / virtual / hybrid) chosen with justification | [ ] Yes  [ ] No |
| 3 | CPU capacity calculated with utilisation target stated | [ ] Yes  [ ] No |
| 4 | RAM sizing applied using workload-appropriate rule | [ ] Yes  [ ] No |
| 5 | Storage calculation shows raw, RAID overhead, usable, and 3-year growth | [ ] Yes  [ ] No |
| 6 | Network topology diagram drawn with VLANs and IP addresses | [ ] Yes  [ ] No |
| 7 | Redundancy mechanism identified for each critical role | [ ] Yes  [ ] No |
| 8 | OS and licensing plan complete | [ ] Yes  [ ] No |
| 9 | Verbal presentation delivered; design rationale clearly explained | [ ] Yes  [ ] No |
| 10 | Server Role Plan revised and submitted after feedback | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |