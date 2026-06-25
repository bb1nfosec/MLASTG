# MLASVS-GOV-3: Audit & Compliance

## Category
MLASVS-GOV: Governance & Compliance

## Overview
Audit and compliance controls ensure ML systems meet regulatory requirements, maintain audit trails, and are ready for external review.

## Controls

### GOV-009: Audit Logging for ML Decisions (L1)
**Description:** All ML-driven decisions must be logged with sufficient context for audit.
**NIST AI RMF:** Measure (Measure-3)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify ML decision logs include: input context, model output, confidence score, model version deployed, timestamp, requestor identity
2. Check that logs are immutable and retention meets regulatory requirements (minimum 1 year)
3. **Pass if:** All ML decisions are logged with auditable context in immutable storage

**Remediation:** Implement structured logging for all inference decisions. Store in append-only log system. Set retention based on regulatory requirements.

---

### GOV-010: Third-Party AI Risk Assessment (L1)
**Description:** Third-party AI/ML services must undergo security assessment before use.
**NIST AI RMF:** Map (Map-3)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify third-party risk assessment process exists for AI/ML vendors
2. Check that assessments cover: data handling practices, model security, compliance certifications, incident response capability
3. **Pass if:** Third-party assessments are completed and current for all AI/ML vendors

**Remediation:** Establish vendor risk assessment program covering AI-specific risks. Review assessments annually or upon material changes.

---

### GOV-013: Continuous Compliance Monitoring (L2)
**Description:** Compliance must be monitored continuously through automated controls.
**NIST AI RMF:** Measure (Measure-4)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify compliance monitoring dashboard/tooling is deployed
2. Check that compliance drift (controls failing after previously passing) triggers alerts
3. **Pass if:** Continuous compliance monitoring is active with automated alerts

**Remediation:** Implement automated compliance monitoring using policy-as-code tools. Integrate MLASVS controls into monitoring framework.

---

### GOV-014: External Audit Readiness (L2)
**Description:** ML systems must be ready for external audit at all times.
**NIST AI RMF:** Govern (Govern-6)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify audit documentation is maintained and current
2. Check that evidence artifacts (model cards, assessment reports, logs) are preserved
3. **Pass if:** Complete audit-ready documentation is maintained for all production ML systems

**Remediation:** Maintain an audit preparation checklist. Run quarterly self-assessments against MLASVS controls.

---

### GOV-015: EU AI Act Conformity Assessment (L2)
**Description:** High-risk ML systems must meet EU AI Act conformity requirements.
**EU AI Act:** Title III (High-Risk AI Systems)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify EU AI Act risk classification for each ML system
2. Check conformity assessment documentation: technical documentation, risk management system, data governance, transparency, human oversight, accuracy/robustness
3. **Pass if:** Documentation addresses all applicable EU AI Act requirements

**Remediation:** Map MLASVS controls to EU AI Act requirements. Engage legal counsel for conformity assessment.

---

### GOV-019: Regulatory Filing Automation (L2)
**Description:** Automated generation of regulatory filings for ML systems.
**NIST AI RMF:** Govern (Govern-7)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify regulatory filing automation exists or is planned
2. Check that automation covers applicable regulations (EU AI Act, local AI regulations)
3. **Pass if:** Regulatory filings can be generated with automated tooling

**Remediation:** Implement template-based regulatory report generation. Pull data from ML system catalog and model cards.

## Cross-References
- NIST AI RMF: Govern, Map, Measure
- EU AI Act: Title III (High-Risk), Title IV (Transparency)
- ISO/IEC 42001: AI Management System
