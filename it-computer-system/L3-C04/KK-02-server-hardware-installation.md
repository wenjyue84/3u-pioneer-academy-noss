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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KK(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-server-hardware-installation

**TUJUAN:** Kertas rujukan untuk KK-02-server-hardware-installation.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Upon completing this activity, the trainee will be able to:
- Mount a rack-mount server into a standard 19-inch server rack safely and correctly
- Install and seat server hardware components including CPU, RAM, storage drives, and expansion cards
- Connect power and data cables according to the server chassis layout and job order specifications
- Verify the hardware installation visually before powering on the server

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Rack-mount server (1U or 2U) | 1 |
| 2 | 19-inch server rack (or rack simulator frame) | 1 |
| 3 | Rail kit (compatible with server and rack) | 1 set |
| 4 | Server-grade CPU (e.g., Intel Xeon or AMD EPYC) | As per job order |
| 5 | ECC RAM modules | As per job order |
| 6 | Server hard disk drives (HDD) or SSDs | As per job order |
| 7 | Network interface card (NIC), if required | As per job order |
| 8 | Redundant power supply unit (PSU), if required | As per job order |
| 9 | Server motherboard manual | 1 |
| 10 | Screwdriver set (Phillips, flathead) | 1 set |
| 11 | Anti-static wrist strap | 1 |
| 12 | Anti-static mat | 1 |
| 13 | Torque screwdriver (optional) | 1 |
| 14 | Cable management arms and ties | As needed |

---

## Langkah Keselamatan / Safety Precautions

- **MANDATORY:** Wear an anti-static wrist strap connected to the chassis ground at all times when handling server components
- Ensure the server is completely powered off and the power cord is disconnected before opening the chassis
- Server chassis covers and rails may have sharp edges — wear cut-resistant gloves when handling sheet metal
- Rack-mount servers can be heavy (15–30 kg); use a two-person lift or a server lift tool when mounting into the rack
- Do not lean the server vertically when the rack is open — the centre of gravity may cause it to topple
- Keep the aisle clear of tools and packaging material while working at the rack

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | **Verify the job order.** Confirm the approved pre-installation checklist (from KK-01) is on hand. Cross-check all components against the bill of materials before opening any packaging. |
| 2 | **Prepare the rack space.** Identify the assigned rack unit (U) position from the job order. Ensure the designated space is empty and that adjacent equipment will not be obstructed. |
| 3 | **Install the rail kit.** Attach the inner rails to the server chassis and the outer rails to the rack posts according to the rail kit instructions. Verify the rails are level and locked in position. |
| 4 | **Open the server chassis.** Remove the top cover by releasing the retention latch or unscrewing the cover screws. Place the cover on the anti-static mat. |
| 5 | **Install the CPU(s).** Locate the CPU socket(s) on the server motherboard. Release the socket lever. Align the CPU using the alignment notch or triangle marker. Lower gently — do not apply force. Close the socket lever. Apply the manufacturer-specified amount of thermal compound to each CPU. Attach the heatsink and secure according to the motherboard manual. |
| 6 | **Install ECC RAM modules.** Refer to the motherboard manual for supported memory population rules (e.g., channel A before channel B). Open retention clips, align the notch, and press each module firmly until both clips snap. Verify all modules are fully and evenly seated. |
| 7 | **Install storage drives.** For hot-swap bays: slide each drive carrier into the correct bay until it clicks. For fixed bays: mount the drive with screws, connect the SATA/SAS data cable and power cable. Verify drive numbering matches the job order slot assignment. |
| 8 | **Install expansion cards (NIC, HBA, etc.).** Remove the appropriate PCIe slot cover. Align the card with the slot and press firmly until fully seated. Secure the card bracket with a screw. Connect any required power or data cables. |
| 9 | **Install or verify redundant PSU.** If a second PSU is required, slide it into the empty PSU bay until it latches. Connect the IEC power cable. Verify the PSU status LED shows standby. |
| 10 | **Perform cable management.** Route all power and data cables through the cable management arm or tie-points. Ensure cables do not obstruct airflow, fans, or hot-swap bays. Label each cable according to the job order. |
| 11 | **Replace the chassis cover.** Slide the cover back onto the chassis and secure the retention latch or screws. |
| 12 | **Mount the server into the rack.** With assistance, slide the server onto the outer rails until it is fully seated. Install the rack screws or cage nuts to secure the server to the rack posts. Do not over-tighten. |
| 13 | **Connect the power cord(s).** Plug the IEC power cord(s) into the server PSU(s) and connect to the PDU (power distribution unit) or UPS outlet as specified in the job order. Do not power on yet. |
| 14 | **Final hardware inspection.** Open the chassis one more time (or inspect through the front bezel) to verify no loose screws, tools, or packaging remain inside. Confirm all components are seated. Close the chassis and submit to the instructor for verification before proceeding to KK-03. |

---

## Hasil Dijangka / Expected Outcome

A fully assembled rack-mount server with:
- Server correctly mounted and secured in the designated rack unit position
- All CPUs installed with thermal compound and heatsinks secured
- ECC RAM installed in the correct population order per motherboard manual
- Storage drives installed in the correct bays per job order
- Expansion cards fully seated and secured
- All cables routed, managed, and labelled
- Chassis cover closed with no loose items inside
- Power cord connected but server not yet powered on

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Anti-static precautions followed throughout installation | [ ] Yes  [ ] No |
| 2 | Rail kit installed correctly and server slides smoothly | [ ] Yes  [ ] No |
| 3 | CPU(s) installed with thermal compound and heatsinks secured | [ ] Yes  [ ] No |
| 4 | ECC RAM installed in correct slots per motherboard manual | [ ] Yes  [ ] No |
| 5 | Storage drives installed in correct bays per job order | [ ] Yes  [ ] No |
| 6 | Expansion cards fully seated and secured with bracket screw | [ ] Yes  [ ] No |
| 7 | Redundant PSU installed and latched (if applicable) | [ ] Yes  [ ] No |
| 8 | All cables routed, managed, and labelled | [ ] Yes  [ ] No |
| 9 | Server secured to rack posts with rack screws | [ ] Yes  [ ] No |
| 10 | No loose tools, screws, or packaging inside chassis | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |