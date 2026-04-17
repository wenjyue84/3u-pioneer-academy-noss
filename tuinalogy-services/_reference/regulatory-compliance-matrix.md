# Regulatory Compliance Matrix — Tuinalogy WIM
## Malaysian Regulatory Frameworks Applicable to T&CM Practice

**Document Code:** TUINA/_reference/regulatory-compliance-matrix
**Version:** 1.0 | **Date:** 2026-04-17
**Purpose:** Cross-reference Tuinalogy WIM content against Malaysian regulatory requirements.
**Usage:** Parsed by `tools/audit-regulatory-compliance.py` to generate compliance gap reports.

---

## FORMAT NOTE (for audit tool parser)
Each regulation block begins with `### REG:` followed by the regulation name.
Each section within a regulation begins with `#### SEC:` followed by the section name.
Keywords are listed under `**Keywords:**` as comma-separated values.
Required coverage is under `**Required Coverage:**`.
Verification points (linked WIM docs) are under `**Verification Points:**`.

---

## 1. T&CM Act 2013 (Traditional and Complementary Medicine Act 2013)

### REG: T&CM Act 2013

#### SEC: Registration and Scope of Practice (Part III)
**Keywords:** registered practitioner, registration, scope of practice, T&CM Act, TCM registration, practitioner licence, authorised practice, traditional medicine registration
**Required Coverage:** All CU lesson plans and information sheets must state that tuina services must be performed only by registered T&CM practitioners. Reference T&CM Act 2013 Part III.
**Verification Points:** PM-teori.md (all CUs), KP-01 (C01), KA.md

#### SEC: Prohibited Acts and Restrictions (Section 28)
**Keywords:** prohibited, restricted practice, Section 28, contraindication, forbidden, not permitted, unauthorised
**Required Coverage:** KP documents covering assessment and treatment must list prohibited acts. Contraindication documentation must cite relevant restrictions.
**Verification Points:** KP-*.md, KK-*.md, PA.md

#### SEC: Patient Consent and Informed Consent
**Keywords:** consent, informed consent, patient agreement, persetujuan pesakit, borang persetujuan, signed consent
**Required Coverage:** Every CU involving client contact must address obtaining informed consent before treatment. C01 and E01 are primary CUs.
**Verification Points:** KP-01 (C01), KK-01 (C01), PA.md (all CUs)

#### SEC: Adverse Event Reporting
**Keywords:** adverse event, adverse reaction, adverse effect, adverse report, kesan buruk, komplikasi, complication reporting
**Required Coverage:** KP and KK documents must include steps for recognising and reporting adverse reactions during/after tuina treatment.
**Verification Points:** KP-*.md (C01, E01), KK-*.md (C01)

---

## 2. OSHA 1994 (Occupational Safety and Health Act 1994)

### REG: OSHA 1994

#### SEC: Workplace Safety Obligations (Section 15)
**Keywords:** workplace safety, occupational safety, OSHA, safe work, hazard, risk assessment, penilaian risiko, keselamatan tempat kerja
**Required Coverage:** Practical lesson plans (PM-amali) and work sheets (KK) must incorporate OSHA workplace safety requirements. Risk assessment steps required.
**Verification Points:** PM-amali.md (all CUs), KK-*.md

#### SEC: Ergonomics and Manual Handling
**Keywords:** ergonomic, ergonomics, posture, body mechanics, manual handling, lifting, pemodalitian badan, postur, ergonomik
**Required Coverage:** KP and KK documents covering tuina techniques must address practitioner ergonomics and correct body mechanics to prevent work-related injury.
**Verification Points:** KP-*.md (C02, C03, C04), KK-*.md (C02, C03)

#### SEC: Infection Control and Hygiene
**Keywords:** infection control, sterilisation, sterilization, disinfection, hygiene, sanitation, hand washing, PPE, personal protective equipment, kawalan jangkitan, kebersihan
**Required Coverage:** All CUs involving client contact must address infection control protocols per OSHA 1994 and MOH guidelines. Sterilisation of equipment is mandatory coverage.
**Verification Points:** KP-*.md (C01, E01, E02), KK-*.md (C01, E01), PM-amali.md

#### SEC: First Aid and Emergency Procedures
**Keywords:** first aid, emergency, emergency procedure, pertolongan cemas, kecemasan, CPR, resuscitation
**Required Coverage:** At least one KP per practical module must address first aid procedures for adverse reactions and medical emergencies.
**Verification Points:** KP-*.md (C01, E01), KA.md, PA.md

---

## 3. PDPA 2010 (Personal Data Protection Act 2010)

### REG: PDPA 2010

#### SEC: Collection and Processing of Personal Data (Section 5)
**Keywords:** personal data, data collection, patient data, data processing, PDPA, perlindungan data, data peribadi, rekod pesakit, patient record
**Required Coverage:** KP documents covering client assessment and record-keeping must include PDPA requirements for collecting and processing personal health data.
**Verification Points:** KP-01 (C01), KP-*.md (assessment CUs), KA.md

#### SEC: Confidentiality and Data Security
**Keywords:** confidential, confidentiality, privacy, data security, kerahsiaan, sulit, privasi, non-disclosure
**Required Coverage:** All assessment and record-keeping procedures must address patient confidentiality obligations under PDPA 2010.
**Verification Points:** KP-*.md (C01, C02), KA.md, PA.md

#### SEC: Patient Rights and Data Access
**Keywords:** patient rights, data access, right to access, hak pesakit, informed, data correction, consent withdrawal
**Required Coverage:** KP documents must inform practitioners of patient rights to access their own health records and withdraw consent.
**Verification Points:** KP-01 (C01), KA.md

---

## 4. MOH Code of Ethics 2007 (Ministry of Health Code of Ethics for T&CM Practitioners)

### REG: MOH Code of Ethics 2007

#### SEC: Professional Conduct and Integrity
**Keywords:** ethics, ethical, code of ethics, professional conduct, integrity, professionalism, etika, kod etika, integriti
**Required Coverage:** All CU theory lesson plans must incorporate ethical principles of T&CM practice. KP documents should reference professional conduct obligations.
**Verification Points:** PM-teori.md (all CUs), KP-01 (C01), KA.md

#### SEC: Patient Welfare and Non-Maleficence
**Keywords:** patient welfare, do no harm, non-maleficence, primum non nocere, patient safety, keselamatan pesakit, kebajikan pesakit
**Required Coverage:** Safety protocols in all KK and PA documents must be framed within the non-maleficence principle. Contraindications must be explicitly addressed.
**Verification Points:** KK-*.md, PA.md (all CUs), KP-*.md

#### SEC: Referral and Scope Boundary
**Keywords:** referral, refer, rujukan, specialist, beyond scope, limitation, had skop, overreach
**Required Coverage:** KP and KK documents must specify when a condition is beyond tuina scope and requires medical referral. C01 basic assessment CU is primary.
**Verification Points:** KP-*.md (C01, C02), KK-*.md, PA.md

#### SEC: Advertising and Representation
**Keywords:** advertising, advertisement, false claim, misleading, iklan, representasi palsu, exaggeration
**Required Coverage:** At least one reference per module to ethical advertising and representation restrictions for T&CM practitioners.
**Verification Points:** KP-01 (C01), KA.md

---

*Matrix generated for: tuinalogy-services/ (C01–C05, E01–E02)*
*Audit tool: `tools/audit-regulatory-compliance.py`*
*Last updated: 2026-04-17*
