# MLASTG-TEST-GOV-001: ML Governance & Compliance Audit

## Control Reference
**Controls Tested:** MLASVS-GOV-001 (ML System Inventory), MLASVS-GOV-002 (ML Risk Assessment Requirement), MLASVS-GOV-003 (ML Security Policy), MLASVS-GOV-004 (Data Governance Policy), MLASVS-GOV-005 (Model Documentation / Model Cards), MLASVS-GOV-006 (Incident Response Plan), MLASVS-GOV-007 (Bias Evaluation Requirement), MLASVS-GOV-008 (Model Performance Monitoring), MLASVS-GOV-009 (Audit Logging for ML Decisions), MLASVS-GOV-010 (Third-Party AI Risk Assessment), MLASVS-GOV-011 (AI Ethics Board — L2), MLASVS-GOV-012 (Human-in-the-Loop for Critical Decisions — L2), MLASVS-GOV-015 (EU AI Act Conformity Assessment — L2), MLASVS-GOV-016 (Regular Red Team Exercises — L2), MLASVS-GOV-017 (Bias Continuous Monitoring — L2), MLASVS-GOV-020 (ML System Impact Assessment — L2)

## Severity
**Medium** (L1) / **High** (L2)

## Overview
ML governance encompasses the policies, processes, documentation, and accountability structures that ensure ML systems are developed and operated responsibly. Poor governance creates risk through undocumented systems, unchecked bias, regulatory non-compliance, and absent incident response capabilities. This test audits the governance posture of the organization's ML program.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | AIF360 (`pip install aif360`), Fairlearn (`pip install fairlearn`) for bias assessment |
| Access | ML system inventory documentation; model cards; incident response plans; governance policies |
| Stakeholders | CISO or AI/ML governance lead should be available for interview |

## Step-by-Step Procedure

### Step 1: ML System Inventory Verification
1. Locate the organization's ML system inventory or AI asset register
2. Verify the inventory includes for each system:
   - System name and description
   - Business owner and technical owner
   - Risk classification (high-risk, limited-risk, minimal-risk)
   - Deployment environment (production / staging / experimental)
   - Regulatory applicability (GDPR, HIPAA, EU AI Act risk category, etc.)
3. **Pass if:** A complete, current inventory exists with all required fields for every production ML system
4. **Fail if:** No inventory exists, or production systems are missing from the inventory

### Step 2: Model Card Verification
1. For each production ML model, verify a model card exists
2. Verify the model card contains:
   - Intended use and out-of-scope use cases
   - Training data description (sources, size, preprocessing)
   - Evaluation results (accuracy, fairness metrics) across demographic groups
   - Known limitations and failure modes
   - Bias assessment results
   - Contact information for model owners
3. **Pass if:** Model cards exist for all production models and contain all required fields
4. **Fail if:** Model cards are absent, incomplete, or out of date (> 12 months since last update)

### Step 3: ML Security Policy Review
1. Verify that a formal ML security policy exists and is approved by the CISO or equivalent
2. Verify the policy covers:
   - Acceptable use of ML systems
   - Data governance requirements
   - Security testing requirements before production deployment
   - Third-party AI risk requirements
3. **Pass if:** ML security policy is in force, approved, and reviewed within the last 12 months

### Step 4: Incident Response Plan Review
1. Locate the ML-specific incident response plan (or verify ML is addressed in the general IR plan)
2. Verify coverage of ML-specific scenarios:
   - Data poisoning attack detected
   - Model extraction attack in progress
   - Adversarial attack campaign
   - Bias incident (discriminatory decision at scale)
   - Supply chain compromise (backdoored model discovered)
3. Verify escalation paths, containment steps, and communication templates are defined
4. **Pass if:** ML IR plan covers all required scenarios; a tabletop exercise has been conducted within the last 12 months

### Step 5: Bias Assessment Verification
1. Request the most recent bias/fairness evaluation report for each production model
2. Verify the evaluation measures relevant fairness metrics for the application domain:
   ```python
   from aif360.metrics import BinaryLabelDatasetMetric
   # Compute disparate impact ratio and statistical parity difference
   # for each protected attribute (gender, race, age group, etc.)
   ```
3. Verify that demographic subgroup performance is reported (not just aggregate accuracy)
4. **Pass if:** Bias evaluation is documented for all production models; results are reviewed by a responsible party; a mitigation plan exists if disparate impact ratio < 0.8
5. **Fail if:** No bias evaluation has been conducted, or results were not reviewed for operational impact

### Step 6: Audit Logging for ML Decisions
1. Verify that high-stakes ML decisions (credit decisions, hiring, healthcare triage, content moderation) are logged with sufficient detail for review:
   - Input features (or sufficient anonymized summary)
   - Model version
   - Decision output
   - Timestamp
   - Confidence score
2. Verify that audit logs are immutable and retained for the required period
3. **Pass if:** Audit logs capture required decision context and are retained per policy

### Step 7: EU AI Act Conformity Assessment (L2)
1. Determine if any ML systems are classified as high-risk under the EU AI Act (Annex III categories: biometric, critical infrastructure, education, employment, essential services, law enforcement, border control, justice)
2. For high-risk systems, verify compliance documentation:
   - Technical documentation per Article 11
   - Data governance documentation per Article 10
   - Human oversight measures per Article 14
   - Transparency and user notification per Article 13
3. **Pass if:** High-risk systems have complete EU AI Act conformity documentation, or systems are correctly classified as non-high-risk

### Step 8: Red Team Exercise Verification (L2)
1. Verify that red team exercises targeting ML systems have been conducted within the last 6 months
2. Review red team findings for coverage of: evasion, extraction, poisoning, prompt injection (if LLM), supply chain attacks
3. Verify all critical findings are tracked to remediation
4. **Pass if:** Red team exercises conducted within 6 months; critical findings have documented remediation plans

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | ML system inventory current; model cards complete; ML security policy in force; IR plan covers ML scenarios; bias assessment conducted for production models |
| L2 | EU AI Act conformity documented for applicable systems; red team exercises within 6 months; AI ethics board established; continuous bias monitoring active |

## Evidence Requirements

- [ ] ML system inventory document (current, with risk classifications)
- [ ] Model cards for each production model
- [ ] ML security policy (approved, dated within 12 months)
- [ ] ML incident response plan with tabletop exercise record
- [ ] Bias/fairness evaluation reports for production models
- [ ] Audit log sample for high-stakes ML decisions
- [ ] (L2) EU AI Act conformity assessment documentation (or non-applicability justification)
- [ ] (L2) Red team exercise report (within last 6 months)
- [ ] (L2) AI ethics board charter and meeting minutes
- [ ] (L2) Continuous bias monitoring configuration

## Remediation Guidance

**If model cards are absent:**
1. Create model cards using the Google Model Card Toolkit or Hugging Face model card template
2. Establish a policy requiring a model card as a prerequisite for production deployment
3. Schedule a review of existing production models to produce retroactive model cards within 90 days

**If bias assessment is not conducted:**
1. Conduct an immediate bias evaluation using AIF360 or Fairlearn
2. Define a fairness testing requirement in the ML security policy
3. Add bias testing as a mandatory gate in the ML deployment pipeline

**If IR plan does not cover ML scenarios:**
1. Extend the existing IR plan with ML-specific playbooks for each scenario listed above
2. Conduct a tabletop exercise specifically targeting an ML incident scenario within 60 days

## References
- **NIST AI RMF:** GOVERN 1.1 (Policies), GOVERN 1.2 (Accountability), MAP 1.6 (Risk context), MEASURE 2.9 (Fairness)
- **EU AI Act:** Articles 10, 11, 13, 14 (high-risk AI system requirements)
- **OWASP ML Top 10:** ML02 (Data Poisoning Attack), ML05 (Model Inversion Attack)
- **MLASWE:** MLASWE-0015 (Governance and Accountability Gap), MLASWE-0016 (Unmitigated Bias)
- **Reference:** ISO/IEC 42001 (AI Management System Standard)
