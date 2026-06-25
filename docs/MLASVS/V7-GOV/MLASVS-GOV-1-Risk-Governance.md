# MLASVS-GOV-1: Risk Governance

## Category
MLASVS-GOV: Governance & Compliance

## Overview
Risk governance provides the organizational framework for managing ML security risk, including policies, roles, responsibilities, and oversight mechanisms. These controls ensure that ML risks are identified, assessed, and managed at the organizational level.

## Controls

### GOV-001: ML System Inventory (L1)
**Description:** Complete inventory of all ML systems in the organization must be maintained.
**NIST AI RMF:** Govern (Govern-1)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify inventory exists covering: model name, purpose, type, data sources, deployment status, risk classification
2. Check that inventory is reviewed and updated at least quarterly
3. **Pass if:** Complete, current ML system inventory exists with risk classification

**Remediation:** Implement an ML system catalog (e.g., using MLflow, data catalog tools, or a CMDB). Automate discovery where possible.

---

### GOV-002: ML Risk Assessment Requirement (L1)
**Description:** All ML systems must undergo security risk assessment before production deployment.
**NIST AI RMF:** Govern (Govern-2)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify risk assessment process is documented
2. Check that completed assessments exist for each production ML system
3. **Pass if:** Risk assessments are completed and approved before deployment

**Remediation:** Integrate risk assessment into the ML model release process. Use MLASVS as the assessment criteria.

---

### GOV-003: ML Security Policy (L1)
**Description:** Organization must have an ML-specific security policy approved by management.
**NIST AI RMF:** Govern (Govern-3)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Review ML security policy document
2. Verify it covers: data handling, model security, supply chain, incident response, governance structure, acceptable use
3. **Pass if:** ML security policy exists, is current, and has management approval

**Remediation:** Draft and approve an ML security policy. Reference MLASVS control categories as technical requirements.

---

### GOV-004: Data Governance Policy (L1)
**Description:** Data governance policy must cover ML-specific data considerations.
**NIST AI RMF:** Govern (Govern-4)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Review data governance policy
2. Verify it covers: training data provenance, data quality standards, labeling quality controls, privacy requirements for training data
3. **Pass if:** Data governance policy addresses ML data requirements

**Remediation:** Extend existing data governance policy to cover ML data lifecycle and quality standards.

---

### GOV-005: Model Documentation (Model Cards) (L1)
**Description:** Each ML model must have a model card documenting its purpose, limitations, and performance.
**NIST AI RMF:** Map (Map-1)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify model cards exist for each production model
2. Check model card includes: intended use, limitations, training data description, performance metrics, bias evaluation results, deployment considerations
3. **Pass if:** Complete model cards exist for all production models

**Remediation:** Implement model card generation in the model registration pipeline. Use the standard model card template from Mitchell et al. (2019).

---

### GOV-006: Incident Response Plan (L1)
**Description:** Incident response plan must cover ML-specific compromise scenarios.
**NIST AI RMF:** Manage (Manage-1)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Review IR plan for ML-specific content
2. Verify coverage of: data poisoning discovered, model theft detected, adversarial attack in progress, supply chain compromise identified, model drift causing safety incidents
3. **Pass if:** IR plan includes ML-specific scenarios with defined response procedures

**Remediation:** Extend existing IR plan with ML scenario playbooks. Conduct tabletop exercises for each scenario.

---

### GOV-011: AI Ethics Board (L2)
**Description:** Organization must have an AI ethics board or equivalent oversight body.
**NIST AI RMF:** Govern (Govern-5)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify AI ethics board exists with defined charter, membership, and meeting cadence
2. Check board reviews high-risk ML applications before deployment
3. **Pass if:** AI ethics oversight body is active and has reviewed high-risk applications

**Remediation:** Establish an AI ethics board with cross-functional membership (legal, security, engineering, product).

---

### GOV-012: Human-in-the-Loop for Critical Decisions (L2)
**Description:** Critical decisions driven by ML must require human review and approval.
**NIST AI RMF:** Manage (Manage-3)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Identify ML-driven decision points that could cause significant harm if incorrect
2. Verify human review gates exist for each critical decision point
3. **Pass if:** Humans are in the loop for all critical ML-driven decisions

**Remediation:** Define critical decision criteria. Implement human review workflows for decisions meeting those criteria.

---

### GOV-016: Regular Red Team Exercises (L2)
**Description:** ML systems must undergo regular adversarial red team testing.
**NIST AI RMF:** Measure (Measure-1)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify red team exercise schedule (minimum quarterly)
2. Check that exercises include: adversarial evasion, prompt injection, model extraction, data poisoning scenarios
3. **Pass if:** Red team exercises are conducted quarterly with documented findings and remediation

**Remediation:** Establish recurring red team engagements with ML-specific testing scope. Use MITRE ATLAS as the attack framework reference.

---

### GOV-018: Transparency Reporting (L2)
**Description:** ML system transparency reports must be published for external stakeholders.
**NIST AI RMF:** Map (Map-4)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify transparency reports exist for public-facing or high-risk ML systems
2. Check reports cover: system purpose, data usage, performance, limitations, fairness assessment
3. **Pass if:** Transparency reports are published and current

**Remediation:** Publish regular transparency reports (annually minimum). Follow model card and system card formats.

---

### GOV-020: ML System Impact Assessment (L2)
**Description:** Impact assessments must be conducted for high-risk ML systems covering societal, privacy, fairness, and safety impacts.
**NIST AI RMF:** Map (Map-2)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify impact assessments exist for systems classified as high-risk
2. Check they cover: societal impact, privacy impact, fairness across demographic groups, safety considerations
3. **Pass if:** Impact assessments are completed, documented, and reviewed by governance body

**Remediation:** Implement ML impact assessment process modeled on NIST AI RMF and EU AI Act requirements.

## Cross-References
- NIST AI RMF: Govern, Map, Measure, Manage
- EU AI Act: Risk classification and conformity requirements
- ISO/IEC 42001: AI Management System
