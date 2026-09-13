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
| KOD DAN TAJUK UNIT KOMPETENSI | G452-010-3:2023-C02 BEV DIAGNOSTIC ACTIVITIES |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PREPARE DIAGNOSTIC TOOLS AND EQUIPMENT<br>2. CARRY OUT VEHICLE INSPECTION<br>3. PERFORM FAULT DIAGNOSIS<br>4. RECORD DIAGNOSTIC RESULTS |
| NO. KOD | G452-010-3:2023-C02/KT(4/12) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** Bev Diagnostic Activities

**TUJUAN:** a) Explain the purpose of the pre-charge system in a BEV. What would happen if the main positive contactor closed without pre-charge? b) List the FIVE (5) main components of the pre-charge control system.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Work Activity 4: Carry Out BEV Pre-Charge Control System Servicing
**Reference:** G452-010-3:2023-C02/KP(4/6)

---

## Soalan / Questions

### Soalan 1 — Short Answer
a) Explain the purpose of the pre-charge system in a BEV. What would happen if the main positive contactor closed without pre-charge?
b) List the FIVE (5) main components of the pre-charge control system.

### Soalan 2 — Sequencing
Arrange the pre-charge sequence steps in the correct order by writing 1–7 in the brackets:

- ( ) BMS closes the main POSITIVE contactor
- ( ) BMS opens the pre-charge relay
- ( ) BMS closes the PRE-CHARGE relay
- ( ) BMS receives "READY" request from VCU
- ( ) BMS monitors voltage difference across main positive contactor
- ( ) BMS closes the main NEGATIVE contactor
- ( ) Inverter capacitors charge gradually

### Soalan 3 — Multiple Choice
What is the typical resistance value of a pre-charge resistor?
A. 0.1-1 ohm
B. 50-200 ohm
C. 1000-5000 ohm
D. 1 MOhm

### Soalan 4 — True/False
a) The pre-charge system operates continuously while the vehicle is in "READY" mode.
b) Pre-charge timeout is a common fault code related to this system.
c) Pre-charge resistors remain cool during operation and can be touched immediately.

### Soalan 5 — Short Answer
Describe the diagnostic procedure for a pre-charge system fault. Include what measurements to take and what to compare them against.

---

## Skema Jawapan / Answer Scheme

### S1
a) The pre-charge system limits inrush current into the large capacitors inside the inverter during initial power-up. Without pre-charge, closing the main positive contactor directly would cause: welding/fusing of contactor contacts (due to high peak inrush current pulse, potentially thousands of amperes), damage to inverter capacitors, arc flash at the contactor, and BMS fault code resulting in system shutdown.

b) Five main components of the pre-charge control system:
1. Pre-charge relay (small relay rated for transient current)
2. Pre-charge resistor (typically 50–200 ohm, limits inrush current)
3. Main positive contactor (heavy-duty HV contactor)
4. Main negative contactor (heavy-duty HV contactor)
5. BMS control circuit (sequences contactor operation and monitors voltage differential)

### S2
Correct sequence (write 1–7):
1. BMS receives "READY" request from VCU → bracket = **4**
2. BMS closes the main NEGATIVE contactor → bracket = **6**
3. BMS closes the PRE-CHARGE relay → bracket = **3**
4. Inverter capacitors charge gradually (through pre-charge resistor) → bracket = **7**
5. BMS monitors voltage difference across main positive contactor (until ΔV < threshold) → bracket = **5**
6. BMS closes the main POSITIVE contactor → bracket = **1**
7. BMS opens the pre-charge relay → bracket = **2**

### S3
**Answer: B** — The pre-charge resistor typically has a resistance of 50–200 ohm. This value is chosen to limit inrush current to a safe level while still allowing the inverter capacitors to charge within an acceptable time frame (typically <500 ms).

### S4
a) **FALSE** — The pre-charge system only operates during the initial energisation sequence. Once the main positive contactor closes and the inverter capacitors are fully charged, the pre-charge relay opens and does not operate again until the next READY cycle.

b) **TRUE** — "Pre-charge timeout" is a common BMS fault code that indicates the inverter capacitors did not reach the expected voltage within the allowed time. Typical causes: failed pre-charge relay, failed pre-charge resistor (open circuit), high-resistance fault in the pre-charge circuit, or a shorted capacitor in the inverter.

c) **FALSE** — Pre-charge resistors dissipate significant energy during each charge cycle (energy = ½CV² where C = capacitor bank capacitance). After recent operation, the resistor body can be hot enough to cause burns. Allow 5 minutes of cool-down before touching, even after HV de-energisation.

### S5
Complete pre-charge diagnostic procedure:
1. Connect diagnostic scan tool; record all active pre-charge fault codes
2. Note any pre-charge timeout fault — indicates the circuit failed to charge capacitors in time
3. Perform HV disconnection and verify zero-energy state with CAT III multimeter
4. Measure pre-charge resistor resistance: compare to manufacturer specification (typically 50–200 ohm). An open circuit reading (OL) indicates a burned-out resistor
5. Measure pre-charge relay coil resistance: compare to specification (typically 40–120 ohm). Infinite resistance = open coil = relay failure
6. Check wiring continuity from BMS control output to pre-charge relay coil
7. Inspect connector condition at pre-charge relay and resistor: look for corrosion, heat damage, or loose terminals
8. If relay and resistor check OK, suspect inverter capacitor fault — refer to inverter diagnosis procedure