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
| NO. KOD | G452-010-3:2023-C04/KP(3/10) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Bev Motor And Drive System Rectification

**TUJUAN:** > **AMARAN / WARNING:** Traction motor terminals carry HV AC voltage during operation (200–800V, 3-phase). After HV de-energisation, wait for inverter capacitor discharge (minimum 10 minutes) before disconnecting motor phase cables. Phase cables carry residual back-EMF if the rotor is moved — secure the vehicle on a lift before servicing. Refer to Manufacturer's Service Manual for motor-specific isolation procedure.

<!-- /JPK_ENVELOPE_v1 -->
## Work Activity 3: Carry Out BEV Traction Motor Replacement

## Objektif Pembelajaran
1. Explain traction motor types, function, and components
2. Describe traction motor diagnostic procedures and fault code interpretation
3. Explain the motor replacement procedure including coolant management

---

> **AMARAN / WARNING:** Traction motor terminals carry HV AC voltage during operation (200–800V, 3-phase). After HV de-energisation, wait for inverter capacitor discharge (minimum 10 minutes) before disconnecting motor phase cables. Phase cables carry residual back-EMF if the rotor is moved — secure the vehicle on a lift before servicing. Refer to Manufacturer's Service Manual for motor-specific isolation procedure.

## 1. BEV Traction Motor

### 1.1 Motor Types

| Type | Full Name | Characteristics | Common Usage |
|------|-----------|----------------|--------------|
| PSM | Permanent Magnet Synchronous Motor | High efficiency, high power density, uses rare-earth magnets | Most common in modern BEVs (Tesla Model 3 rear, BYD, Hyundai) |
| ASM/IM | Asynchronous Motor / Induction Motor | Robust, no permanent magnets, lower cost | Tesla Model S/3 front, some others |
| SRM | Switched Reluctance Motor | Simple construction, no magnets, high torque ripple | Emerging technology, limited current use |

### 1.2 Motor Components
| Component | Function |
|-----------|----------|
| Stator | Stationary part with three-phase windings — creates rotating magnetic field |
| Rotor | Rotating part — PSM has permanent magnets; ASM has conductive bars |
| Bearings | Support rotor shaft rotation |
| Resolver/encoder | Measures rotor position for precise control |
| Temperature sensors | Monitor winding and bearing temperatures |
| Cooling jacket | Liquid cooling channels in stator housing |
| HV connectors | Three-phase power connections from inverter |

### 1.3 Motor Specifications (Typical)
| Parameter | Range |
|-----------|-------|
| Power | 50-300 kW |
| Torque | 100-500 Nm |
| Speed | Up to 20,000 RPM |
| Voltage | 200-800V AC (3-phase) |
| Weight | 30-80 kg |
| Cooling | Liquid (most common) |

---

## 2. Traction Motor Diagnostic Procedures

### 2.1 Inspection
1. Diagnostic scan: read motor-specific fault codes
2. Check motor temperature readings
3. Verify resolver/encoder signals (rotor position accuracy)
4. Listen for abnormal noise (bearing wear, rotor contact)
5. Check motor mount condition

### 2.2 Common Fault Codes
- Over-temperature: winding or bearing temperature exceeded
- Resolver fault: position sensor failure — vehicle may not drive
- Insulation fault: winding insulation degradation
- Phase imbalance: unequal current in motor phases
- Vibration: bearing wear or rotor imbalance

---

## 3. Motor Replacement Procedure

1. Complete HV de-energisation
2. Drain coolant from motor cooling circuit
3. Disconnect 3-phase HV cables from motor
4. Disconnect resolver/encoder connector
5. Disconnect temperature sensor connectors
6. Disconnect coolant hoses from motor jacket
7. Support motor weight with hydraulic crane or transmission jack
8. Remove motor mounting bolts
9. Remove motor from vehicle/transaxle assembly
10. Install new motor in reverse order
11. Refill coolant, bleed air
12. Re-energise and verify with diagnostic tool
13. Road test — verify smooth acceleration, no vibration, regenerative braking

---

## 4. Motor Coolant Management
Same procedure as inverter coolant management. Motor shares the powertrain cooling loop. Use manufacturer-specified coolant. Bleed air after refill.

---

## 5. Regenerative Braking Theory — Motor as Generator (Teori Brek Regeneratif)

During deceleration, the inverter transitions the traction motor into **generator mode**:
1. The rotor continues spinning (driven by vehicle momentum)
2. FOC reverses the torque command — motor produces negative torque (braking force)
3. The motor generates AC current; the inverter converts it to DC and feeds it back to the HV battery
4. Energy recovery: typically 15–30% of kinetic energy is recovered per braking event

**Limitations of regenerative braking:**
- Battery SOC near 100%: no storage capacity → regenerative braking disabled, friction braking only
- Very cold battery: reduced charge acceptance → regenerative braking limited
- Low speed (< ~5 km/h): regenerative torque insufficient → friction braking takes over

The inverter and brake control system coordinate to blend regenerative and friction braking transparently to the driver. Refer to Manufacturer's Service Manual for regenerative braking calibration parameters.

## 6. Motor Failure Modes (Mod Kegagalan Motor)

| Component | Failure Mode | Symptom | Diagnosis |
|-----------|-------------|---------|-----------|
| Stator winding | Inter-turn short | Reduced power; over-temperature fault | Phase resistance test; insulation resistance test |
| Rotor magnets (PSM) | Demagnetisation | Reduced torque at high speed | Scan tool — compare torque output vs. command |
| Resolver/encoder | Signal error | Vehicle does not drive; resolver fault code | Check signal waveform; inspect connector |
| Motor bearings | Wear / contamination | Grinding or whining noise | Listen during active test; vibration analysis |
| Cooling jacket | Blockage | Motor over-temperature fault | Coolant flow rate check; temperature sensor reading |
| HV phase connector | Oxidation / loose | Phase imbalance fault; intermittent power loss | Torque connector; inspect terminal condition |

---

## Rujukan
1. Manufacturer's Service Manual
2. Gottlieb I. (1994). *Electric Motors and Control Techniques*
3. Hayes John G. (2018). *Electric Powertrain*