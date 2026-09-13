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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C02 COMPUTER SYSTEM ASSET MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM ASSET INVENTORY<br>2. DEFINE OPERATIONAL STATUS OF ASSETS<br>3. ESTIMATE COSTS AND SPACE REQUIREMENTS<br>4. DETERMINE ASSET MANAGEMENT SYSTEMS<br>5. MONITOR ASSET TAGGING AND LABELLING<br>6. EXECUTE ASSET DISPOSAL<br>7. PREPARE ASSET MANAGEMENT REPORTS |
| NO. KOD | IT-020-5:2013-C02/KP(3/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-estimate-costs-and-space-requirements

**TUJUAN:** Kertas rujukan untuk KP-03-estimate-costs-and-space-requirements.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the components of Total Cost of Ownership (TCO) for computer system assets
2. Calculate asset depreciation using straight-line and reducing balance methods
3. Estimate physical space requirements for IT equipment in office and data centre environments
4. Prepare a cost estimate for asset procurement, maintenance, and disposal
5. Justify asset investment decisions using cost-benefit analysis

---

## 1.0 Total Cost of Ownership (TCO)

The purchase price of an IT asset represents only a fraction of its true cost over its useful life. Total Cost of Ownership (TCO) captures all direct and indirect costs associated with an asset from acquisition to disposal.

### 1.1 TCO Components

| Cost Category | Items Included |
|--------------|---------------|
| **Acquisition Cost** | Purchase price, shipping and handling, import duties, taxes (SST) |
| **Deployment Cost** | Installation labour, configuration, cabling, software setup |
| **Operating Cost** | Electricity consumption, consumables (ink, toner, filters), software subscriptions |
| **Maintenance Cost** | Preventive maintenance contracts, spare parts, repair labour |
| **Support Cost** | Help desk support, warranty extensions, vendor support contracts |
| **Training Cost** | User training, administrator certification, e-learning subscriptions |
| **Upgrade Cost** | RAM upgrades, storage expansion, firmware updates |
| **Disposal Cost** | Data destruction, e-waste recycling fees, decommissioning labour |

### 1.2 TCO Formula

```
TCO = Acquisition Cost + Deployment Cost + (Annual Operating Cost × Useful Life)
    + (Annual Maintenance Cost × Useful Life) + Disposal Cost − Residual Value
```

**Example:** Desktop PC with 5-year useful life

| Component | Amount (RM) |
|-----------|------------|
| Purchase price | 3,200 |
| Setup and configuration | 150 |
| Annual electricity cost | 180 × 5 = 900 |
| Annual maintenance/support | 120 × 5 = 600 |
| Disposal (data destruction + recycling) | 80 |
| Residual value | −200 |
| **TCO** | **4,730** |

---

## 2.0 Asset Depreciation

Depreciation is the systematic allocation of an asset's cost over its useful life. Accurate depreciation is required for:
- Financial reporting (balance sheet, profit and loss statement)
- Budget planning (replacement cycle forecasting)
- Tax reporting (capital allowance claims)
- Disposal justification (written-down value)

### 2.1 Useful Life Standards for IT Assets

| Asset Type | Standard Useful Life | Residual Value |
|------------|---------------------|----------------|
| Desktop PC / Laptop | 4–5 years | 5–10% of cost |
| Server | 5–7 years | 5% of cost |
| Network switch / router | 5–7 years | 5% of cost |
| Printer (laser) | 5 years | 0–5% |
| UPS (Uninterruptible Power Supply) | 3–5 years | 0% |
| Monitor | 5–7 years | 5% |
| Mobile device (tablet, smartphone) | 2–3 years | 5% |

*Note: Public sector organisations in Malaysia follow Pekeliling Perbendaharaan for depreciation rates.*

### 2.2 Straight-Line Depreciation

The most common method for IT assets. Annual depreciation is constant throughout the useful life.

```
Annual Depreciation = (Cost − Residual Value) / Useful Life (years)
```

**Example:** Laptop purchased at RM 4,500; residual value RM 225; useful life 4 years

```
Annual Depreciation = (4,500 − 225) / 4 = RM 1,068.75 per year
```

| Year | Opening Book Value (RM) | Depreciation (RM) | Closing Book Value (RM) |
|------|------------------------|-------------------|------------------------|
| 1 | 4,500.00 | 1,068.75 | 3,431.25 |
| 2 | 3,431.25 | 1,068.75 | 2,362.50 |
| 3 | 2,362.50 | 1,068.75 | 1,293.75 |
| 4 | 1,293.75 | 1,068.75 | 225.00 |

### 2.3 Reducing Balance Depreciation

Applies a fixed percentage to the remaining book value each year. Produces higher depreciation in early years, lower in later years — suitable for assets that lose value rapidly (e.g. mobile devices).

```
Annual Depreciation = Book Value at Start of Year × Depreciation Rate (%)
```

**Example:** Smartphone at RM 2,000; depreciation rate 40% per annum

| Year | Opening Book Value (RM) | Depreciation (RM) | Closing Book Value (RM) |
|------|------------------------|-------------------|------------------------|
| 1 | 2,000.00 | 800.00 | 1,200.00 |
| 2 | 1,200.00 | 480.00 | 720.00 |
| 3 | 720.00 | 288.00 | 432.00 |

---

## 3.0 Estimating Space Requirements

Physical space planning ensures that IT assets are housed in environments that meet operational, safety, and regulatory requirements.

### 3.1 Office End-User Equipment

| Asset Type | Space Allowance per Unit | Notes |
|------------|------------------------|-------|
| Desktop PC (tower) | 0.04 m² (footprint) | Plus clearance for ventilation: 15 cm sides, 30 cm rear |
| Desktop PC (small form factor) | 0.01 m² | Can be VESA-mounted behind monitor |
| Monitor (24") | 0.06 m² (desk area) | Plus ergonomic depth allowance for user |
| Laptop + docking station | 0.05 m² | |
| Multifunction printer (office) | 0.3–0.5 m² | Plus paper tray access space |
| UPS (tower, 1–3 kVA) | 0.08–0.15 m² | Must not obstruct airflow or fire exits |

**Workspace rule of thumb (Malaysia OSHA 1994 and Akta Keselamatan dan Kesihatan Pekerjaan):** Minimum 4.6 m² (50 sq ft) of floor space per person in an office environment; IT equipment must not reduce this below minimum.

### 3.2 Server Room and Data Centre Space

Server room space is measured in rack units (U) for vertical capacity and square metres for floor area.

| Concept | Definition |
|---------|-----------|
| Rack Unit (U) | 44.45 mm (1.75 inches) of vertical space in a standard 19-inch server rack |
| Standard rack height | 42U (approximately 2 metres tall) |
| Floor tile (data centre) | 600 mm × 600 mm raised floor tile, each supporting up to 1,000 kg/m² |
| Hot aisle / Cold aisle | Alternating rows of racks facing front-to-front (cold aisle) and back-to-back (hot aisle) to manage airflow |

**Rack space planning:**

| Equipment | Rack Units Required |
|-----------|-------------------|
| 1U rack server | 1U |
| 2U rack server | 2U |
| Blade chassis (10-blade) | 7U |
| KVM switch | 1U |
| 24-port patch panel | 1U |
| 48-port network switch | 1U |
| 1U cable management panel | 1U |

**Example calculation:** A department requires 10 rack servers (2U each), 2 network switches (1U each), and 3 patch panels (1U each). Plus 20% spare capacity:

```
Used U = (10 × 2) + (2 × 1) + (3 × 1) = 25U
With 20% spare = 25 / 0.8 = 31.25U → Minimum 2 standard 42U racks
```

### 3.3 Power and Cooling Requirements

Space planning must account for power density and cooling load:

| Parameter | Calculation |
|-----------|-------------|
| Power density | Total wattage of equipment per rack / floor area (kW/m²) |
| Cooling capacity | Heat load = power consumption (kW) × 3,412 BTU/hr per kW |
| UPS sizing | Total load (VA) × 1.25 (25% headroom) |

---

## 4.0 Cost Estimation for Asset Procurement

A cost estimate for an asset acquisition project must cover all phases of the TCO.

### 4.1 Cost Estimate Template

| Line Item | Quantity | Unit Cost (RM) | Total (RM) |
|-----------|----------|---------------|-----------|
| Hardware purchase | — | — | — |
| Delivery and installation | — | — | — |
| Network cabling | — | — | — |
| Software licences (1 year) | — | — | — |
| Training (users) | — | — | — |
| Year 1 maintenance contract | — | — | — |
| Contingency (10%) | — | — | — |
| **Total Estimated Cost** | | | |

### 4.2 Cost-Benefit Analysis (CBA)

CBA compares the total cost of an investment against its quantifiable benefits to justify the expenditure.

| Element | Description |
|---------|-------------|
| Benefit 1: Productivity gain | Estimated hours saved per user per year × number of users × hourly labour cost |
| Benefit 2: Reduced downtime | Estimated downtime reduction (hours/year) × cost of downtime per hour |
| Benefit 3: Licence compliance | Estimated penalty avoidance if currently non-compliant |
| Benefit 4: Energy savings | Current power cost − projected power cost of new equipment |
| **Net Benefit** | Total Benefits − TCO |
| **Payback Period** | TCO / Annual Net Benefit (years) |
| **ROI** | (Net Benefit / TCO) × 100% |

---

## 5.0 Common Errors in Cost and Space Estimation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Using purchase price alone instead of TCO | Underestimation of true cost; budget shortfall | Always calculate full TCO including operating and disposal costs |
| Ignoring depreciation in budget planning | Replacement cost not budgeted; assets run beyond useful life | Include annual depreciation in the IT budget as a capital reserve |
| No space headroom in server room | Cannot expand without disruptive rearrangement | Plan for 20–30% spare rack capacity |
| Underestimating power load | Circuit breaker trips; equipment damage | Add 25% headroom to UPS and PDU sizing |
| CBA not documented | Investment decision cannot be justified to auditors | Prepare formal CBA document signed by IT manager and Finance |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- Malaysian Financial Reporting Standard (MFRS) 116 — Property, Plant and Equipment
- Pekeliling Perbendaharaan Malaysia — Pengurusan Aset Alih Kerajaan
- TIA-942 — Telecommunications Infrastructure Standard for Data Centres
- Akta Keselamatan dan Kesihatan Pekerjaan 1994 (OSHA) — Workplace space requirements
- ASHRAE TC 9.9 — Thermal Guidelines for Data Processing Environments