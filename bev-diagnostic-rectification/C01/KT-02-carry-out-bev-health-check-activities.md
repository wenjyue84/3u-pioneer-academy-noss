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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | G452-010-3:2023 DIAGNOSTIK DAN PEMBAIKAN KENDERAAN ELEKTRIK BATERI |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | G452-010-3:2023-C01 BEV HIGH VOLTAGE SAFETY |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY HIGH VOLTAGE HAZARDS<br>2. APPLY HIGH VOLTAGE SAFETY PROCEDURES<br>3. USE HIGH VOLTAGE PPE<br>4. CARRY OUT HIGH VOLTAGE ISOLATION |
| NO. KOD | G452-010-3:2023-C01/KT(2/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** Bev High Voltage Safety

**TUJUAN:** What is the function of the Insulation Monitoring Device (IMD) in a BEV?

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Competency Unit: Perform BEV Scheduled Maintenance
## Work Activity 2: Carry Out BEV Health Check Activities

**Reference:** G452-010-3:2023-C01/KP(2/3)

---

## Soalan / Questions

### Soalan 1 — Multiple Choice

What is the function of the Insulation Monitoring Device (IMD) in a BEV?

A. Monitors the engine oil temperature
B. Monitors the insulation resistance between HV circuits and the vehicle chassis
C. Monitors the cabin air filter condition
D. Monitors the tyre pressure

### Soalan 2 — Multiple Choice

Which CAT rating is the minimum required for a digital multimeter used to measure HV circuits in a BEV?

A. CAT I — 600V
B. CAT II — 600V
C. CAT III — 1000V
D. CAT IV — 600V

### Soalan 3 — True/False

State whether each statement is TRUE or FALSE. Provide justification for FALSE answers.

a) OBD-II port in a BEV uses a standard 16-pin DLC connector.

b) Fault codes beginning with "P1xxx" are generic/global codes applicable to all vehicle manufacturers.

c) A BEV health check report must be signed by the performing technician.

d) Freeze frame data records the vehicle conditions at the time a fault code was stored.

e) Cell voltage balance in a BEV battery pack typically allows a deviation of +/- 5.0V.

### Soalan 4 — Short Answer

a) List FIVE (5) Electronic Control Units (ECUs) found in a typical BEV and state their functions.

b) Explain the three-tier condition rating system used during BEV component assessment. Provide an example for each tier.

c) Describe the FIVE (5) steps involved in interpreting a diagnostic fault code.

### Soalan 5 — Multiple Choice

Which of the following is NOT a step in the BEV health check testing procedure?

A. Connect diagnostic scan tool to OBD-II port
B. Turn vehicle to "READY" mode
C. Disassemble the HV battery pack for visual inspection
D. Read all system fault codes

### Soalan 6 — Short Answer

What is the minimum acceptable HV insulation resistance value, and why is this measurement important during a BEV health check?

### Soalan 7 — Matching

Match each diagnostic protocol in Column A with its description in Column B.

| Column A (Protocol) | Column B (Description) |
|--------------------|----------------------|
| 1. ISO 15765-4 | a. Standardised diagnostic commands for ECU communication |
| 2. ISO 14229 (UDS) | b. Primary CAN-based protocol for BEV diagnostics |
| 3. SAE J1979 | c. Additional manufacturer-proprietary access parameters |
| 4. Manufacturer-specific | d. OBD-II diagnostic test modes |

---

## Skema Jawapan / Answer Scheme

### Soalan 1
**Answer: B** — The IMD monitors the insulation resistance between HV circuits and the vehicle chassis. A fault indication means potential HV leakage to the chassis.

### Soalan 2
**Answer: C** — CAT III — 1000V is the minimum rating required for HV measurement in BEVs.

### Soalan 3
a) **TRUE** — The OBD-II port uses a standard 16-pin DLC connector, typically located under the dashboard.

b) **FALSE** — P1xxx codes are manufacturer-specific. Generic/global codes are P0xxx and P2xxx.

c) **TRUE** — The report must be signed by the performing technician and reviewed by the supervisor.

d) **TRUE** — Freeze frame data captures parameters such as SOC, temperature, and vehicle speed at the time the fault occurred.

e) **FALSE** — Cell voltage balance typically allows +/- 0.05V deviation (not 5.0V). A 5.0V deviation would indicate a severely failed cell.

### Soalan 4
a) Five ECUs:
1. BMS ECU — Battery state of charge (SOC), state of health (SOH), cell voltages, temperatures
2. Motor Control Unit (MCU) — Motor performance, inverter status, regenerative braking
3. Vehicle Control Unit (VCU) — Overall vehicle systems coordination
4. Thermal Management ECU — Cooling system status, pump operation, valve positions
5. Charging ECU — On-board charger status, charging protocols

b) Three-tier condition rating:
- GOOD (Baik): Component within specification, no issues. Example: Brake pad thickness at 8mm (specification minimum is 3mm).
- ADVISORY (Nasihat): Approaching limit or minor concern. Example: Brake pad at 4mm — still serviceable but schedule for next service.
- DEFECTIVE (Rosak): Outside specification or failed. Example: HV insulation resistance below minimum threshold — immediate attention required.

c) Five steps for interpreting fault codes:
1. Record the full code (e.g., P0A1F)
2. Check whether the code is current (active) or historical (stored)
3. Cross-reference with manufacturer technical service bulletins (TSBs)
4. Verify with freeze frame data (conditions when fault occurred)
5. Clear codes only after root cause analysis; document before clearing

### Soalan 5
**Answer: C** — Disassembling the HV battery pack is NOT part of a health check. Health checks are non-invasive; battery pack disassembly is a separate rectification activity.

### Soalan 6
The minimum acceptable HV insulation resistance is typically >500 ohm/V (per manufacturer specification). This measurement is critical because low insulation resistance indicates that HV current may be leaking to the vehicle chassis, creating an electrocution risk for occupants and technicians. The IMD continuously monitors this value during vehicle operation.

### Soalan 7
1-b, 2-a, 3-d, 4-c