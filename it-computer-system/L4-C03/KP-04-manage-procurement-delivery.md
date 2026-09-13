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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C03 COMPUTER SYSTEM & NETWORK PROCUREMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY PROCUREMENT REQUIREMENTS<br>2. PREPARE SPECIFICATIONS AND TENDER DOCUMENTS<br>3. EVALUATE QUOTATIONS AND VENDORS<br>4. MANAGE PROCUREMENT AND DELIVERY<br>5. DOCUMENT PROCUREMENT RECORDS |
| NO. KOD | IT-020-4:2013-C03/KP(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-manage-procurement-delivery

**TUJUAN:** Kertas rujukan untuk KP-04-manage-procurement-delivery.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Prepare and issue a Purchase Order (PO) following procurement award
2. Monitor delivery timelines and coordinate receipt inspection against specifications
3. Manage delivery discrepancies, damaged goods, and warranty registration
4. Apply handover and acceptance testing procedures for ICT hardware and network equipment

---

## 1.0 From Award to Purchase Order

Once the evaluation committee recommends a vendor and the award is approved by the authorised approver, a **Purchase Order (PO / Pesanan Tempatan)** is issued. The PO is a legally binding document committing the organisation to purchase from the vendor at the agreed price and terms.

### 1.1 Purchase Order Contents

| Field | Description |
|-------|-------------|
| PO number | Unique reference number for tracking |
| Date issued | Date of PO issuance |
| Vendor details | Name, address, registration number, contact |
| Item description | Full description matching the quotation/tender |
| Quantity | Number of units per line item |
| Unit price and total | As per accepted quotation |
| Delivery address | Exact site and receiving officer |
| Required delivery date | Contractual delivery deadline |
| Payment terms | e.g. 30 days from acceptance / invoice |
| Authorised signatory | Approver name and signature |

### 1.2 PO Tracking Register

Maintain a PO tracking register to monitor all active purchase orders:

| PO No. | Vendor | Description | Value (RM) | PO Date | Required Delivery | Actual Delivery | Status |
|--------|--------|-------------|-----------|---------|------------------|-----------------|--------|
| PO-2026-001 | XYZ Sdn Bhd | 20× Desktop PC | 90,000 | 01/06/2026 | 15/06/2026 | — | Pending |

---

## 2.0 Delivery Coordination

### 2.1 Pre-Delivery Preparation

Before the delivery date, the systems administrator should:
- Confirm the delivery date and time with the vendor
- Prepare the receiving area (adequate space, access, power for testing)
- Arrange for the Receiving Officer (Pegawai Penerima) to be present
- Print copies of the PO and technical specification for reference during inspection

### 2.2 Goods Received Note (GRN / Nota Barang Diterima)

Upon delivery, a Goods Received Note (GRN) is completed to acknowledge receipt:

| Field | Detail |
|-------|--------|
| GRN number | Sequential reference number |
| PO reference | Link to the original purchase order |
| Date received | Actual date of delivery |
| Vendor | Supplier name |
| Items received | Description and quantity |
| Condition | Physical condition upon receipt |
| Received by | Name and signature of receiving officer |
| Discrepancies noted | Any shortage, damage, or substitution |

---

## 3.0 Goods Inspection and Acceptance Testing

Physical receipt is not the same as acceptance. Acceptance requires verification that goods meet the specified requirements.

### 3.1 Physical Inspection Checklist

| Check | Action |
|-------|--------|
| Correct quantity delivered | Count items against PO line by line |
| Correct model/specification | Verify model number, processor, RAM, storage against spec |
| Packaging intact | Check for damaged boxes; photograph any damage before opening |
| Serial numbers recorded | Record serial number of every unit on the asset register |
| Accessories included | Verify cables, manuals, licence documents, COA are present |
| Energy Star / compliance labels | Confirm certification labels are present on unit |

### 3.2 Functional Acceptance Testing (FAT)

After physical inspection, conduct a Functional Acceptance Test on a sample (or all units for small quantities):

| Test | Pass Criteria |
|------|-------------|
| Power-on | Unit powers on without error; POST completes |
| OS boot | Windows boots to desktop; correct OS version and build |
| BIOS/UEFI check | Firmware version meets or exceeds specification; TPM 2.0 enabled |
| Hardware verification | Device Manager shows no unknown devices; all components detected |
| RAM test | Correct capacity and speed (Task Manager → Performance) |
| Storage test | Correct capacity; health status = Good (via CrystalDiskInfo or equivalent) |
| Network port | Gigabit link established; ping to gateway successful |
| Peripherals | Keyboard, mouse, monitor at correct resolution |
| Warranty registration | Serial number registered on vendor/manufacturer portal |

### 3.3 Acceptance Certificate (Sijil Penerimaan)

Upon successful FAT, the Receiving Officer signs an **Acceptance Certificate** confirming:
- Goods received match the PO specifications
- Functional testing passed
- Organisation's ownership of the goods is confirmed
- Warranty period begins from this date

The Acceptance Certificate triggers payment processing.

---

## 4.0 Managing Delivery Discrepancies

Discrepancies must be managed formally and documented:

| Discrepancy Type | Action |
|-----------------|--------|
| Short delivery (fewer units than ordered) | Issue a Discrepancy Note; vendor must deliver balance within agreed timeframe |
| Wrong model delivered | Reject non-compliant items; vendor to replace; do not process GRN for non-compliant items |
| Damaged goods | Photograph damage; issue rejection notice; vendor to replace at their cost |
| Substitute specification offered | Evaluate substitution against spec; accept only with written technical approval |
| Late delivery | Issue a Late Delivery Notice; liquidated damages (if contract includes LD clause) may apply |

### 4.1 Liquidated Damages (LD / Ganti Rugi Tertentu)

For contracts with an LD clause, late delivery incurs a financial penalty:

> **Typical formula:** LD = 0.5% of contract value per week of delay (or as stipulated in contract)

LD must be formally notified in writing to the vendor and deducted from payment. The LD rate and maximum cap must be stated in the original contract/PO.

---

## 5.0 Asset Registration and Tagging

Upon acceptance, all ICT assets must be registered in the ICT Asset Register (Daftar Aset ICT):

| Field | Detail |
|-------|--------|
| Asset tag number | Unique physical tag affixed to the unit |
| Description | Make, model, and specification summary |
| Serial number | Manufacturer serial number |
| Purchase date | Date on acceptance certificate |
| Purchase price | Unit price from PO |
| Location | Building, room, workstation reference |
| Assigned user | Name and staff ID |
| Warranty expiry | Calculated from acceptance date |
| Disposal method | To be completed at end of life |

For government agencies, ICT assets above a defined value threshold must be registered in the **Sistem Pengurusan Aset dan Stor (SPAS)** or equivalent government asset management system.

---

## 6.0 Common Errors in Procurement and Delivery Management

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Signing GRN without physical inspection | Accepting defective or incomplete goods | Never sign GRN until full physical count and condition check |
| Not recording serial numbers | Cannot track assets or process warranty claims | Record every serial number on GRN and asset register |
| Delaying acceptance testing | Payment released before quality verified | Complete FAT before signing acceptance certificate |
| Not issuing LD notice for late delivery | Organisation forfeits contractual remedy | Monitor delivery dates; issue formal LD notice immediately upon delay |
| Accepting substitute specification informally | Non-compliant goods absorbed into inventory | All substitutions require written technical approval before acceptance |

---

## Rujukan / References

- Arahan Perbendaharaan Malaysia — Bahagian Pengurusan Aset
- Pekeliling Perbendaharaan — Pengurusan Aset ICT Kerajaan
- MAMPU — Garis Panduan Pengurusan Aset ICT
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 3
- Sistem Pengurusan Aset dan Stor (SPAS) — Jabatan Akauntan Negara Malaysia