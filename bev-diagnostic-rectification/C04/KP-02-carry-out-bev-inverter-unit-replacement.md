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

## KERTAS PENERANGAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | G452-010-3:2023 DIAGNOSTIK DAN PEMBAIKAN KENDERAAN ELEKTRIK BATERI |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | G452-010-3:2023-C04 BEV MOTOR AND DRIVE SYSTEM RECTIFICATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. INSPECT MOTOR AND DRIVE SYSTEM<br>2. DIAGNOSE MOTOR AND DRIVE FAULTS<br>3. CARRY OUT MOTOR AND DRIVE RECTIFICATION<br>4. VERIFY MOTOR AND DRIVE PERFORMANCE |
| NO. KOD | G452-010-3:2023-C04/KP(2/10) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Bev Motor And Drive System Rectification

**TUJUAN:** > **AMARAN / WARNING:** The inverter unit contains DC bus capacitors that store lethal charge even after HV isolation. Wait minimum 10 minutes (or per Manufacturer's Service Manual specification) after disconnecting the HV service plug before touching HV connectors. Verify residual voltage is below 60V DC using a CAT-III multimeter before proceeding.

<!-- /JPK_ENVELOPE_v1 -->
## Work Activity 2: Carry Out BEV Inverter Unit Replacement

## Objektif Pembelajaran
1. Explain inverter unit function, components, and safety requirements
2. Describe inverter diagnostic procedures and fault code interpretation
3. Explain BEV LV and HV circuit fundamentals relevant to inverter work
4. Describe the inverter replacement procedure including coolant management

---

> **AMARAN / WARNING:** The inverter unit contains DC bus capacitors that store lethal charge even after HV isolation. Wait minimum 10 minutes (or per Manufacturer's Service Manual specification) after disconnecting the HV service plug before touching HV connectors. Verify residual voltage is below 60V DC using a CAT-III multimeter before proceeding.

## 1. BEV Inverter Unit

### 1.1 Function
The inverter (also called motor controller or power electronics unit) converts HV DC power from the battery to three-phase AC power to drive the traction motor. During regenerative braking, it converts AC back to DC to charge the battery.

### 1.2 Components
| Component | Function |
|-----------|----------|
| IGBT/SiC power modules | High-speed switching devices that create AC waveform from DC |
| Gate driver circuits | Control the switching of power modules |
| DC bus capacitors | Smooth DC input; store energy during switching |
| Current sensors | Measure motor phase currents for control |
| Temperature sensors | Monitor power module and coolant temperatures |
| Control PCB | Processes motor control algorithms (Field Oriented Control / FOC) |
| HV connectors | DC input from battery, AC output to motor |
| Coolant channels | Liquid cooling for power modules |

### 1.3 Safety Requirements
- Inverter contains DC bus capacitors that retain lethal charge after power-off
- MUST wait for capacitor discharge (5-10 minutes after de-energisation)
- Never open the inverter housing — internal components are not field-serviceable
- The inverter is replaced as a complete unit

### 1.4 Field Oriented Control (FOC) — Kawalan Berorientasi Medan
The inverter's Control PCB implements **Field Oriented Control (FOC)**, also called Vector Control:
- FOC independently controls the torque-producing and flux-producing components of motor current
- Enables smooth torque at any speed, including near-zero RPM
- Uses resolver/encoder feedback for real-time rotor position — loss of position signal disables drive
- Switching frequency: typically 8–20 kHz (SiC modules allow higher frequency with lower losses)

### 1.5 Inverter Specifications (Typical)
| Parameter | Specification |
|-----------|--------------|
| DC input voltage | 200–800V DC (platform dependent) |
| Peak output power | 50–300 kW |
| Switching frequency | 8–20 kHz |
| Switching technology | IGBT (older) or SiC MOSFET (newer, higher efficiency) |
| Efficiency | >97% at rated power |
| Cooling | Liquid-cooled (shared powertrain loop) |

---

## 2. Inverter Diagnostic Procedures

### 2.1 Inspection
1. Connect diagnostic scan tool
2. Read inverter-specific fault codes
3. Check inverter temperature readings (should be within operating range)
4. Verify motor phase current balance
5. Check for communication between inverter and VCU/BMS

### 2.2 Common Fault Codes
| Category | Description |
|----------|-------------|
| Over-temperature | Inverter exceeds temperature limit — cooling fault or high load |
| Over-current | Phase current exceeds limit — motor fault or inverter failure |
| Under-voltage / over-voltage | DC bus voltage out of range — battery or contactor issue |
| Communication | Lost communication with VCU or BMS |
| IGBT fault | Internal power module failure — replacement required |
| Insulation fault | Insulation resistance below threshold |

---

## 3. BEV LV and HV Systems
Same fundamentals as C02/KP(2/6) Sections 2-4. The HV disconnection procedure is identical.

---

## 4. Inverter Coolant Management

The inverter is liquid-cooled, sharing the powertrain cooling circuit with the motor and potentially the DC-DC converter.

- **Draining:** Drain coolant from the inverter circuit before disconnecting coolant hoses
- **Waste management:** SW305 scheduled waste
- **Refill:** Manufacturer-specified coolant type and volume; bleed air; run pump

---

## 5. Inverter Replacement Procedure

1. Complete HV de-energisation and zero-energy verification
2. Drain coolant from inverter circuit
3. Disconnect HV DC input cables from inverter
4. Disconnect motor phase cables (3-phase AC output)
5. Disconnect LV control/communication connectors
6. Disconnect coolant hoses
7. Remove inverter mounting bolts
8. Remove inverter unit (typically 10-25 kg)
9. Install new inverter in reverse order
10. Reconnect coolant hoses, HV cables, LV connectors
11. Refill coolant, bleed air
12. Re-energise HV system
13. Perform functionality test via diagnostic scan tool
14. Road test to verify motor operation under load

---

## 6. Inverter Functionality Test
1. No fault codes after re-energisation
2. Motor phase current balance verified
3. Inverter temperature within specification
4. Vehicle enters "READY" mode and drives normally
5. Regenerative braking functional

---

## Rujukan
1. Manufacturer's Service Manual
2. Hayes John G. (2018). *Electric Powertrain*
3. Gottlieb I. (1994). *Electric Motors and Control Techniques*