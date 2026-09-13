# 3U Pioneer Academy – NOSS-Compliant Online Learning Platform

## **System Requirements Specification (SRS) - NOSS Alignment**

**Version 2.0 · Updated 28 Jul 2025**  
**NOSS Compliance: IT-010-45-2013, IT-020-4-2013, IT-120-45-2011, IT-121-45-2011, IT-122-45-2011**

---

### 1 Introduction

#### 1.1 Purpose

This document defines the requirements for a NOSS-compliant online learning platform ("the System") serving *3U Pioneer Academy*. The platform will support competency-based training aligned with **National Occupational Skills Standards (NOSS)** framework, covering multi-disciplinary programmes including:

- **ICT Application Development** (IT-010 series)
- **Computer System Management** (IT-020 series) 
- **Multimedia Programming** (IT-120 series)
- **Database Programming** (IT-121 series)
- **Server Application Development** (IT-122 series)
- **Traditional Chinese Medicine**
- **Beauty & Wellness**
- **Accounting & Finance**

The System provides a digital hub for NOSS-aligned teaching, learning, competency assessment, and skills development tracking.

#### 1.2 Scope

* **User Roles:** System Administrator, NOSS Assessor, Lecturer/Trainer, Student/Trainee, Industry Partner
* **Functional Scope:** NOSS competency mapping, CoCU (Curriculum of Competency Units) management, competency-based assessment, skills tracking, evidence collection, certification workflow, industry collaboration, **NOSS compliance reporting**
* **Delivery Scope:** Responsive Web Application (Phase 1) with NOSS API integration & Malaysian Skills Certification Agency (MSCA) connectivity (Phase 2)

#### 1.3 Definitions & Acronyms

| Abbreviation | Definition |
| ------------ | ---------- |
| SRS | System Requirements Specification |
| NOSS | National Occupational Skills Standards |
| CoCU | Curriculum of Competency Units |
| DSD | Department of Skills Development |
| MSCA | Malaysian Skills Certification Agency |
| NSDB | National Skills Development Board |
| PDPA | Personal Data Protection Act 2010 |
| SP | Standard Practice |
| SC | Standard Content |

---

### 2 Overall Description

#### 2.1 User View

* **System Administrator** – Configures NOSS programmes, manages assessors/trainers, views competency analytics, generates NOSS compliance reports, interfaces with MSCA
* **NOSS Assessor** – Conducts competency assessments, evaluates practical demonstrations, verifies workplace evidence, issues competency certificates
* **Lecturer/Trainer** – Delivers CoCU content, tracks competency progression, provides formative assessment, maintains evidence portfolios
* **Student/Trainee** – Accesses competency units, completes practical tasks, submits evidence, tracks competency achievement, views certification progress
* **Industry Partner** – Provides workplace assessment opportunities, validates competency standards, contributes to curriculum development

#### 2.2 NOSS-Aligned Product Features

| Module / Service | Key Capabilities |
| ---------------- | ---------------- |
| **NOSS Programme Management** | CoCU mapping; competency level tracking; SP/SC alignment; certification pathway management |
| **Competency Assessment** | Practical demonstration tracking; workplace evidence collection; rubric-based evaluation; competency validation |
| **Skills Development Tracking** | Competency progression monitoring; training hours logging; applied skills verification; attitude/safety assessment |
| **Evidence Portfolio** | Digital evidence storage; competency mapping; assessment criteria alignment; audit trail maintenance |
| **Certification Workflow** | MSCA integration; certificate generation; competency validation; NOSS compliance reporting |
| **Industry Collaboration** | Workplace assessment coordination; industry validation; curriculum alignment; employment pathway tracking |
| **Analytics & Reporting** | Competency achievement rates; training effectiveness; industry alignment; NOSS compliance metrics |
| **Multi-language Support** | Bahasa Malaysia, English, Chinese; NOSS terminology consistency; cultural competency integration |

---

### 3 Functional Requirements

#### 3.1 NOSS Programme Management

* **FR-01** The System shall support NOSS programme structure with five competency levels (Level 1-5) and corresponding certificate types
* **FR-02** Lecturers shall create CoCU-aligned courses with competency descriptors, work activities, knowledge requirements, and applied skills
* **FR-03** System shall map each course to specific NOSS competency units and track progression through competency levels
* **FR-04** Administrators shall configure NOSS programme taxonomy: *Academy › NOSS Sector › Competency Level › CoCU*

#### 3.2 Competency-Based Assessment

* **FR-05** NOSS Assessors shall conduct competency assessments with practical demonstration requirements and workplace evidence collection
* **FR-06** System shall support continuous assessment throughout training with formative and summative evaluation capabilities
* **FR-07** Assessment criteria shall align with NOSS competency standards including knowledge, skills, and attitude requirements
* **FR-08** System shall generate unique assessment IDs and maintain audit trails for all competency evaluations

#### 3.3 Skills Development & Tracking

* **FR-09** System shall log training hours for each CoCU with delivery mode tracking (practical, theoretical, workplace)
* **FR-10** Lecturers shall track applied skills development with evidence collection for each competency unit
* **FR-11** System shall monitor attitude/safety/environmental considerations as specified in NOSS standards
* **FR-12** Students shall maintain digital evidence portfolios demonstrating competency achievement

#### 3.4 Certification & Compliance

* **FR-13** System shall integrate with MSCA for certificate generation and competency validation
* **FR-14** Administrators shall generate NOSS compliance reports for DSD submission
* **FR-15** System shall track certification pathways from individual competency units to full diploma/advanced diploma
* **FR-16** All competency assessments shall comply with Malaysian Skills Certification requirements

#### 3.5 Industry Collaboration

* **FR-17** Industry partners shall validate competency standards and provide workplace assessment opportunities
* **FR-18** System shall facilitate industry feedback integration and curriculum alignment
* **FR-19** Employment pathway tracking shall align with NOSS career progression frameworks

#### 3.6 Multi-language & Cultural Support

* **FR-20** Interface shall support Bahasa Malaysia, English, and Chinese with NOSS terminology consistency
* **FR-21** Cultural competency integration shall align with Malaysian workplace standards
* **FR-22** System shall accommodate traditional Chinese medicine and beauty industry specific requirements

---

### 4 Non-Functional Requirements

| Category | ID | Requirement |
| -------- | -- | ----------- |
| **NOSS Compliance** | NFR-NOSS-01 | Full alignment with NOSS framework standards and DSD requirements |
| **Performance** | NFR-P-01 | Support ≥300 concurrent users; initial page load ≤3s on 50 Mbps link |
| **Scalability** | NFR-S-01 | Micro-service architecture; competency data stored in horizontally scalable storage |
| **Reliability** | NFR-R-01 | ≥99.5% annual uptime; nightly competency data snapshots; 24×7 monitoring |
| **Security** | NFR-SEC-01 | Hardened against OWASP Top-10; all traffic via TLS 1.3; competency data encrypted at rest |
| **Malaysian Compliance** | NFR-MY-01 | Comply with PDPA 2010, Malaysian copyright law, NOSS data retention requirements |
| **Usability** | NFR-U-01 | Interface supports Bahasa Malaysia, English, Chinese; mobile UI follows WCAG AA standards |
| **Audit Trail** | NFR-AUDIT-01 | Complete audit trail for all competency assessments; data retention ≥5 years per NOSS requirements |

---

### 5 System Architecture Overview

```
Client (Browser / PWA)
        │
 NOSS API Gateway (GraphQL/REST) ── Auth Service (JWT + RBAC)
        │
┌────────────┬────────────┬────────────┬──────────────┐
│NOSS Mgmt   │Competency  │Assessment  │Certification │
│Service     │Tracking    │Service     │Service       │
│PostgreSQL  │TimescaleDB │ObjectStore │MSCA API     │
└────────────┴────────────┴────────────┴──────────────┘
        │
Event Bus (RabbitMQ/Kafka) → NOSS Compliance Reporting & Analytics
        │
DSD Integration → Malaysian Skills Development Framework
```

---

### 6 NOSS Role-Permission Matrix

| Function | System Admin | NOSS Assessor | Lecturer | Student | Industry Partner |
| -------- | ------------ | ------------- | -------- | ------- | ---------------- |
| Configure NOSS programmes | ✔ | ✖ | ✖ | ✖ | ✖ |
| Conduct competency assessment | ✖ | ✔ | ✖ | ✖ | ✖ |
| Deliver CoCU content | ✖ | ✖ | ✔ | ✖ | ✖ |
| Submit competency evidence | ✖ | ✖ | ✖ | ✔ | ✖ |
| Validate industry standards | ✖ | ✖ | ✖ | ✖ | ✔ |
| Generate NOSS reports | ✔ | ✔ | ✖ | ✖ | ✖ |
| Issue certificates | ✖ | ✔ | ✖ | ✖ | ✖ |
| Track training hours | ✖ | ✖ | ✔ | ✔ | ✖ |

---

### 7 NOSS Data Model

* **NOSSProgramme** (id, programme_code, sector, competency_level, certificate_type, dsd_approval_date)
* **CompetencyUnit** (id, cocu_code, descriptor, work_activities, knowledge_requirements, applied_skills, training_hours)
* **CompetencyAssessment** (id, student_id, assessor_id, competency_unit_id, assessment_type, evidence_collected, result, assessment_date)
* **TrainingHours** (id, student_id, cocu_id, hours_logged, delivery_mode, practical_theoretical_split, logged_date)
* **EvidencePortfolio** (id, student_id, competency_unit_id, evidence_type, file_reference, validation_status, submission_date)
* **CertificationPathway** (id, student_id, programme_id, current_level, completed_units, certification_status)

---

### 8 External Interfaces

#### 8.1 Malaysian Government Integration
* **MSCA API** - Certificate generation and validation
* **DSD Data Portal** - NOSS compliance reporting
* **NSDB Integration** - Skills development framework alignment

#### 8.2 Industry Partner APIs
* **Workplace Assessment Coordination**
* **Industry Validation Services**
* **Employment Pathway Tracking**

#### 8.3 International Standards
* **ASEAN Skills Recognition Framework**
* **ILO Standards Compliance**
* **International Certification Bodies**

---

### 9 NOSS Compliance Requirements

#### 9.1 Competency Standards Alignment
- All courses must map to specific NOSS competency units
- Assessment criteria must align with NOSS competency descriptors
- Training hours must meet NOSS minimum requirements
- Evidence collection must demonstrate applied skills

#### 9.2 Certification Process
- Competency-based assessment throughout training
- Practical demonstration of skills
- Workplace evidence collection
- Continuous assessment with formative feedback
- MSCA integration for certificate issuance

#### 9.3 Quality Assurance
- Regular NOSS compliance audits
- Industry feedback integration
- Continuous improvement processes
- International benchmarking
- DSD monitoring and evaluation

#### 9.4 Data Management
- PDPA 2010 compliance for personal data
- NOSS data retention requirements (≥5 years)
- Audit trail maintenance for all competency assessments
- Secure storage of evidence portfolios
- Malaysian copyright law compliance

---

### 10 Implementation Phases

#### Phase 1: Core NOSS Platform (Months 1-6)
- Basic NOSS programme management
- Competency tracking and assessment
- Multi-language interface (BM, English, Chinese)
- Evidence portfolio management
- Basic reporting capabilities

#### Phase 2: Advanced Features (Months 7-12)
- MSCA integration for certification
- Advanced analytics and compliance reporting
- Industry partner collaboration tools
- Mobile application development
- Advanced assessment tools

#### Phase 3: Enterprise Features (Months 13-18)
- Full DSD integration
- International standards compliance
- Advanced workplace assessment coordination
- AI-powered competency evaluation
- Comprehensive industry alignment

---

### 11 Risk Management

#### 11.1 NOSS Compliance Risks
- **Risk**: Non-compliance with NOSS standards
- **Mitigation**: Regular DSD consultation, expert panel review, continuous monitoring

#### 11.2 Technical Risks
- **Risk**: System performance under high load
- **Mitigation**: Scalable architecture, load testing, performance monitoring

#### 11.3 Regulatory Risks
- **Risk**: PDPA compliance violations
- **Mitigation**: Data protection audits, legal consultation, secure data handling

---

### 12 Success Metrics

#### 12.1 NOSS Compliance Metrics
- 100% alignment with NOSS competency standards
- 95%+ competency achievement rates
- 100% MSCA certification success rate
- Zero NOSS compliance violations

#### 12.2 Technical Performance Metrics
- 99.5%+ system uptime
- <3 second page load times
- 100% data security compliance
- Zero data breaches

#### 12.3 User Satisfaction Metrics
- 90%+ user satisfaction scores
- 95%+ competency assessment accuracy
- 100% multi-language support effectiveness
- High industry partner engagement rates

---

### 13 Appendix

#### 13.1 NOSS Programme Codes
- **IT-010-45-2013**: Systems Module Development & Systems Implementation Integration
- **IT-020-4-2013**: Computer System Administration
- **IT-120-45-2011**: Multimedia Programming
- **IT-121-45-2011**: Database Programming
- **IT-122-45-2011**: Server Application Development and Management

#### 13.2 Deployment Environments
- **Development**: Docker Compose with NOSS test data
- **Staging**: Kubernetes with MSCA test integration
- **Production**: High-availability Kubernetes with full DSD integration

#### 13.3 Quality Assurance
- Automated NOSS compliance testing
- Regular security audits
- Performance monitoring and optimization
- Continuous integration with NOSS standards updates

---

**Document Control**
- **Version**: 2.0
- **Date**: 28 Jul 2025
- **NOSS Compliance**: Verified
- **DSD Approval**: Pending
- **Next Review**: 6 months

---

*This SRS document aligns with National Occupational Skills Standards (NOSS) framework and Malaysian government requirements. For official NOSS information, refer to the Department of Skills Development (DSD) website: www.dsd.gov.my* 