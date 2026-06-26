# MLASTG-TEST-GOV-002: AI Ethics Board & Human-in-the-Loop Assessment

## Control Reference
**Controls Tested:** MLASVS-GOV-011 (AI Ethics Board — L2), MLASVS-GOV-012 (Human-in-the-Loop for Critical Decisions — L2), MLASVS-GOV-013 (Bias Continuous Monitoring — L2), MLASVS-GOV-014 (Model Performance Drift Monitoring — L2), MLASVS-GOV-015 (EU AI Act Conformity Assessment — L2), MLASVS-GOV-016 (Regular Red Team Exercises — L2), MLASVS-GOV-017 (Bias Continuous Monitoring — L2), MLASVS-GOV-018 (Adversarial Robustness Monitoring — L2), MLASVS-GOV-019 (Model Retirement Policy — L2), MLASVS-GOV-020 (ML System Impact Assessment — L2)

## Severity
**High** (L2)

## Overview
This test assesses the maturity of an organization's AI governance beyond baseline L1 controls. It evaluates whether an AI Ethics Board is established and functional, whether human-in-the-loop mechanisms are enforced for high-stakes decisions, and whether continuous monitoring for bias, drift, and adversarial robustness is operational. This is a L2-only test — L1 assessments do not require these controls.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Access | AI Ethics Board charter (if exists), HITL configuration, monitoring dashboards |
| Stakeholders | AI/ML governance lead, ethics board chair (if available), compliance officer |
| Tools | Manual review and interview-based assessment |

## Step-by-Step Procedure

### Step 1: AI Ethics Board Assessment
1. Verify that an AI Ethics Board exists with:
   - Formal charter or mandate document
   - Defined membership (technical, legal, ethicist, domain expert, affected-party representative)
   - Meeting schedule (at least quarterly)
   - Decision authority (binding vs. advisory)
2. Review the last 6 months of meeting minutes for:
   - Topics discussed (bias incidents, new model deployments, policy changes)
   - Decisions made and implementation status
   - Dissenting opinions and how they were addressed
3. **Pass if:** Ethics Board is established, meets regularly, and has documented decision authority
4. **Fail if:** No Ethics Board exists, or it exists but has no authority or meeting history

### Step 2: Human-in-the-Loop Mechanism Assessment
1. Identify all high-stakes ML decision points:
   - Credit lending decisions
   - Hiring/recruitment screening
   - Healthcare diagnostics or triage
   - Content moderation at scale
   - Law enforcement risk scoring
2. For each high-stakes decision point, verify:
   - Human review is required before the decision is finalized
   - The human reviewer has sufficient context (input features, model confidence, explanation)
   - The human can override the model's recommendation
   - Override decisions are logged
3. **Pass if:** All high-stakes decision points have enforced HITL with override capability
4. **Fail if:** Any high-stakes decision can be executed autonomously without human review

### Step 3: Continuous Bias Monitoring Assessment
1. Verify that bias monitoring is configured for each production model:
   - Protected attributes are defined (gender, race, age, disability, etc.)
   - Fairness metrics are computed (demographic parity, equalized odds, disparate impact)
   - Alert thresholds are set for metric violations
   - Monitoring cadence is defined (real-time, daily, weekly)
2. Review the last 6 months of bias monitoring reports for:
   - Metric trends over time
   - Alerts triggered and how they were addressed
   - Any bias incidents that occurred between monitoring periods
3. **Pass if:** Continuous bias monitoring is active with defined thresholds and incident response

### Step 4: Model Drift and Performance Monitoring
1. Verify that model performance monitoring includes:
   - Input data drift detection (statistical tests on feature distributions)
   - Output prediction drift detection (prediction distribution monitoring)
   - Ground truth monitoring (accuracy/F1 tracking when labels become available)
   - Alert thresholds for performance degradation
2. **Pass if:** Drift monitoring is active with defined alert thresholds and response procedures

### Step 5: Adversarial Robustness Monitoring (L2)
1. Verify that adversarial robustness is periodically retested:
   - Red team exercises conducted within the last 6 months
   - Automated adversarial robustness tests in CI/CD
   - Findings tracked to remediation
2. **Pass if:** Adversarial robustness is retested at least quarterly

### Step 6: Model Retirement Policy
1. Verify that a model retirement policy exists:
   - Criteria for retirement (performance below threshold, bias threshold exceeded, regulatory change)
   - Process for decommissioning a model (rollback to previous version, notification to stakeholders)
   - Archive requirements for retired models
2. **Pass if:** Model retirement policy is documented and at least one model has been retired per the process

### Step 7: ML System Impact Assessment
1. Verify that each production ML system has an impact assessment:
   - Potential harms to individuals and groups
   - Risk severity and likelihood classification
   - Mitigation measures implemented
   - Review cycle (at least annually)
2. **Pass if:** Impact assessments exist for all high-risk ML systems

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L2 | Ethics Board established and functional; HITL enforced for all high-stakes decisions; continuous bias monitoring active; drift monitoring active; adversarial robustness retested quarterly; model retirement policy documented; impact assessments complete |

## Evidence Requirements

- [ ] AI Ethics Board charter and last 6 months of meeting minutes
- [ ] HITL configuration for each high-stakes decision point
- [ ] Continuous bias monitoring configuration and last 6 months of reports
- [ ] Drift monitoring configuration and alert history
- [ ] Red team exercise report (within last 6 months)
- [ ] Model retirement policy and any retirement records
- [ ] ML System Impact Assessment documents

## Remediation Guidance

**If Ethics Board does not exist:**
1. Establish a cross-functional AI Ethics Board with technical, legal, and ethics expertise
2. Define a charter with meeting schedule and decision authority
3. Ensure at least one affected-party representative is on the board

**If HITL is not enforced:**
1. Identify all high-stakes ML decision points in the system
2. Implement a review gate that requires human approval before execution
3. Ensure reviewers have sufficient context (explanations, confidence scores)

**If continuous bias monitoring is absent:**
1. Deploy automated fairness monitoring using AIF360 or Fairlearn
2. Define alert thresholds for each protected attribute
3. Integrate monitoring into the ML pipeline with automated alerts

## References
- **NIST AI RMF:** GOVERN 1.1, GOVERN 1.2, MEASURE 2.9
- **EU AI Act:** Articles 14 (Human Oversight), 26 (Obligations of deployers)
- **ISO/IEC 42001:** AI Management System Standard
- **MLASWE:** MLASWE-0015 (Governance and Accountability Gap)
