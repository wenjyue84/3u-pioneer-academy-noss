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
| KOD DAN TAJUK UNIT KOMPETENSI | G452-010-3:2023-C02 BEV DIAGNOSTIC ACTIVITIES |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PREPARE DIAGNOSTIC TOOLS AND EQUIPMENT<br>2. CARRY OUT VEHICLE INSPECTION<br>3. PERFORM FAULT DIAGNOSIS<br>4. RECORD DIAGNOSTIC RESULTS |
| NO. KOD | G452-010-3:2023-C02/KP(2/12) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Bev Diagnostic Activities

**TUJUAN:** Upon completion of this Information Sheet, trainees will be able to:

<!-- /JPK_ENVELOPE_v1 -->
## Competency Unit: Perform Battery Management System (BMS) Rectification
## Work Activity 2: Carry Out BEV High Voltage Cable Replacement

---

## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees will be able to:
1. Explain BEV high voltage cable safety requirements and PPE specifications
2. Describe the fundamentals of BEV low voltage and high voltage electrical systems
3. Explain the HV circuit disconnection procedure (de-energisation)
4. Describe HV cable inspection procedures including insulation resistance testing
5. Explain the HV interlock system and its function

---

## 1. BEV High Voltage Cable Safety

### 1.1 Safety Precautions for HV Cable Work
HV cables in a BEV carry DC voltages between 200V and 800V. These cables are universally identified by their **orange colour** (per SAE J1654 and IEC 60445). Any orange cable, connector, or component must be treated as potentially energised until verified otherwise.

> **AMARAN / WARNING:** HV cables carry 200–800V DC. Do NOT touch any orange cable or connector without confirming zero-energy state. A single contact can cause cardiac arrest or fatal burns.

Key safety rules:
- **NEVER cut, splice, or repair HV cables** — always replace the complete cable assembly
- **NEVER attempt to measure HV circuits** without CAT III-1000V rated equipment
- The HV system must be fully de-energised and verified before any cable work
- Allow minimum 5-10 minutes after disconnection for capacitor discharge

### 1.2 HV Cable PPE
All BMS PPE requirements from KP(1/6) apply. For cable work specifically:
- Insulated gloves (Class 0) are mandatory for ALL cable handling, even after de-energisation
- Safety glasses must be arc-flash rated
- Leather over-gloves protect insulated gloves from cuts during cable routing work

---

## 2. BEV Low Voltage System (Sistem Voltan Rendah BEV)

### 2.1 Basic Principle of Ohm's Law
Ohm's Law is fundamental to understanding both LV and HV circuits:

**V = I x R**

Where:
- V = Voltage (Volts)
- I = Current (Amperes)
- R = Resistance (Ohms)

**Power:** P = V x I (Watts)

In BEV context: A 400V battery delivering 200A produces 80 kW of power (approximately 107 horsepower). This illustrates why HV is used — to deliver high power with manageable cable sizes.

### 2.2 BEV Low Voltage Circuit
The BEV low voltage (LV) system operates at 12V (some newer vehicles use 48V). The 12V system powers:
- Vehicle ECUs and control modules
- Lighting and indicators
- Dashboard and infotainment
- Door locks, windows, mirrors
- BMS communication circuits
- HV contactor coils (the 12V system controls the HV contactors)

**Critical insight:** The 12V system must be disconnected FIRST during de-energisation because it controls the HV contactors. Without 12V, the HV contactors cannot close, adding an additional safety layer.

### 2.3 Procedure to Disconnect 12V Battery
1. Turn vehicle to "OFF" mode
2. Remove the vehicle key; store in safety box
3. Wait 2 minutes for systems to power down
4. Locate the 12V auxiliary battery
5. Disconnect the NEGATIVE terminal first (to prevent chassis short circuit)
6. Disconnect the POSITIVE terminal
7. Insulate exposed terminals with tape or terminal covers
8. Secure the disconnected cables away from the battery posts

---

## 3. BEV High Voltage System (Sistem Voltan Tinggi BEV)

### 3.1 Fundamentals of HV Circuit
The BEV HV circuit is a closed-loop system connecting:
- HV traction battery pack (energy source)
- HV contactors (main positive and negative)
- Pre-charge relay and resistor
- Inverter/motor controller
- Traction motor(s)
- On-board charger (OBC)
- DC-DC converter (steps HV down to 12V)
- HV heating elements (PTC heater, heat pump)
- AC compressor (electric, for HVAC)

### 3.2 BEV Standard Electric Wire Colours

| Colour | Designation | Voltage Class |
|--------|-------------|---------------|
| Orange | HV DC circuits (>60V DC) | High Voltage |
| Orange with blue stripe | HV AC circuits (motor phases) | High Voltage |
| Red | 12V positive | Low Voltage |
| Black | 12V negative / ground | Low Voltage |
| Blue | Signal/communication | Low Voltage |

### 3.3 BEV Bus-Bar Connection
Bus-bars are solid copper or aluminium conductors used inside HV junction boxes and battery packs to distribute HV power. They are:
- Insulated with heat-shrink or insulation coating
- Secured with torqued bolts (specific torque values per manufacturer)
- Protected by insulation covers that must be replaced after any work

### 3.4 Specification of HV Wires

| Parameter | Typical Specification |
|-----------|----------------------|
| Conductor | Multi-strand copper, tinned |
| Insulation | Cross-linked polyethylene (XLPE) or silicone rubber |
| Voltage rating | 600V DC minimum (typically rated 1000V) |
| Temperature rating | -40 deg C to +150 deg C |
| Shielding | EMI shielding (braided or foil) |
| Colour | Orange (mandatory per SAE J1654) |

---

## 4. Procedure to Disconnect HV Circuit (Prosedur Pemutusan Litar HV)

This is the most critical safety procedure in BEV servicing. It MUST be followed precisely in sequence.

### 4.1 Step-by-Step HV Disconnection

**Step 1:** Turn vehicle key to "READY" OFF mode
- Ensure the vehicle is completely shut down
- The "READY" indicator on the dashboard must be OFF

**Step 2:** Store vehicle key in safety box
- Place the key fob in the safety box
- Lock the safety box
- This prevents accidental vehicle start-up during work

**Step 3:** Understand HV warning signage
- Identify all HV warning labels on the vehicle
- These indicate the location and voltage of HV components
- Common symbols: lightning bolt in triangle, "HIGH VOLTAGE" text

**Step 4:** Disconnect 12V battery negative terminal
- Using insulated tools, disconnect the 12V negative terminal
- This disables the HV contactor coil power supply
- The HV contactors will open, isolating the HV battery from the vehicle circuits

**Step 5:** Disconnect interlock/service plug
- Locate the interlock/service plug (typically orange, accessible from interior or under vehicle)
- Using insulated gloves, pull the interlock plug
- This physically breaks the HV circuit within the battery pack
- Store the interlock plug in the safety box with the vehicle key

**Step 6:** Wait for capacitor discharge
- Wait the manufacturer-specified time (typically 5-10 minutes)
- HV capacitors in the inverter and motor controller retain charge after disconnection
- NEVER skip this waiting period

**Step 7:** Verify zero-energy state
- Using a CAT III-1000V rated multimeter, measure voltage at the HV terminals
- Verify 0V DC (or below 5V DC) between positive and negative
- Verify 0V DC between each terminal and chassis ground
- Only proceed if ALL measurements confirm zero energy

---

## 5. High Voltage Cable Inspection

### 5.1 Cable Connector Condition
- Visual inspection of all HV connectors for: corrosion, moisture, damaged pins, broken locking mechanisms
- Check connector seals (O-rings) for damage or displacement
- Verify proper seating — connectors must click/lock fully

### 5.2 Cable Insulation Resistance Test
Using a Mega Ohm meter (CAT III, 1000V):
1. Set the meter to the appropriate test voltage (typically 500V DC test)
2. Connect one lead to the cable conductor, the other to the cable shield/chassis
3. Initiate the test and read the insulation resistance value
4. The value must exceed the manufacturer's minimum (typically >1 MOhm)
5. Record the reading for documentation

### 5.3 Bus-Bar Insulation Resistance Test
Similar procedure applied to bus-bars inside junction boxes:
1. Remove insulation covers (with HV confirmed de-energised)
2. Test between bus-bar and housing/chassis
3. Record readings

---

## 6. High Voltage Cable Interlock Connection

### 6.1 Introduction to Interlock Function
The HV interlock is a low-voltage safety circuit that runs through all HV connectors in series. If any HV connector is disconnected or not properly seated, the interlock circuit opens, and the BMS prevents HV contactor closure.

### 6.2 Continuity Inspection
Using a multimeter in continuity mode:
1. Disconnect the interlock circuit at the BMS connector
2. Measure continuity through the entire interlock loop
3. An open circuit indicates a disconnected or improperly seated HV connector
4. Identify the specific connector causing the open circuit

### 6.3 Interlock Connection Continuity Procedure
After any HV cable replacement:
1. Reconnect all HV connectors, ensuring positive lock engagement
2. Measure interlock continuity — must show closed circuit
3. Verify interlock signal at the BMS using diagnostic scan tool
4. Any interlock fault must be resolved before re-energising the HV system

---

## 7. Procedure for HV Cable Replacement

1. Complete full HV disconnection procedure (Section 4)
2. Identify the cable to be replaced using the wiring diagram
3. Disconnect the cable at both ends (connectors)
4. Note the cable routing path — take photos for reference
5. Remove cable clips and guides
6. Remove the old cable
7. Route the new cable following the exact original path
8. Secure with clips and guides at original positions
9. Connect both ends — verify connector lock engagement
10. Perform insulation resistance test on the new cable
11. Verify interlock continuity
12. Perform HV system re-energisation procedure

---

## 8. Procedure for HV System Functionality Test

After any HV cable work, before returning the vehicle to service:
1. Re-connect the interlock/service plug
2. Re-connect the 12V battery (positive first, then negative)
3. Retrieve the vehicle key from the safety box
4. Turn vehicle to "READY" mode
5. Check for any dashboard warning lights — there should be none
6. Connect diagnostic scan tool and verify: no fault codes, HV insulation resistance within specification, all HV component communication restored
7. If any faults are present, turn off vehicle, re-de-energise, and investigate

---

## 9. HV Cable and Connector Failure Modes

| Component | Failure Mode | Symptom | Diagnosis |
|-----------|-------------|---------|-----------|
| HV cable insulation | Breakdown / cracking | Insulation resistance < 1 MOhm, HV isolation fault code | Mega Ohm meter test |
| HV connector | Corrosion / moisture ingress | Intermittent HV fault, voltage drop | Visual + resistance check |
| HV connector | Locking mechanism failure | Cable comes loose, arcing risk | Physical pull test, interlock fault |
| Bus-bar | Loose torque / corrosion | Voltage drop, resistance heating | Torque check, thermal imaging |
| EMI shielding | Damaged braid | EMI interference on CAN/LIN signals | Oscilloscope on communication lines |

---

## Rujukan / References

1. SAE J1654 — High Voltage Primary Cable
2. IEC 60445 — Basic and Safety Principles for Man-Machine Interface
3. IEC 60900 — Live Working — Hand Tools
4. UN GTR No. 20 — Electric Vehicle Safety
5. Manufacturer's Service Manual
6. Hayes John G. (2018). *Electric Powertrain: Energy Systems, Power Electronics and Drives*