# MLASVS-GOV-2: Bias & Fairness

## Category
MLASVS-GOV: Governance & Compliance

## Overview
Bias and fairness testing ensures ML models do not produce discriminatory outcomes across protected attributes (race, gender, age, etc.) and that fairness metrics are monitored throughout the model lifecycle.

## Controls

### GOV-007: Bias Evaluation Requirement (L1)
**Description:** All ML models must undergo bias evaluation before deployment.
**NIST AI RMF:** Measure (Measure-2)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify bias evaluation is conducted for each model before production deployment
2. Check that evaluation covers relevant protected attributes for the use case
3. **Pass if:** Bias evaluation report exists and documents fairness metrics

**Remediation:** Implement bias evaluation pipeline using AIF360 or Fairlearn. Define protected attributes based on use case and applicable regulations.

---

### GOV-008: Model Performance Monitoring (L1)
**Description:** Model performance must be monitored with fairness metrics tracked alongside accuracy.
**NIST AI RMF:** Measure (Measure-2)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify fairness metrics are tracked alongside accuracy, precision, recall
2. Check that performance is monitored across demographic groups
3. **Pass if:** Performance monitoring includes fairness dimensions per demographic group

**Remediation:** Add fairness metrics (Disparate Impact Ratio, Statistical Parity Difference) to model monitoring dashboards.

---

### GOV-017: Bias Continuous Monitoring (L2)
**Description:** Real-time bias detection with automated alerting on fairness drift.
**NIST AI RMF:** Measure (Measure-2)
**Test Reference:** MLASTG-TEST-GOV-001

**Verification:**
1. Verify real-time bias detection system is deployed
2. Check that significant fairness metric drift triggers automated alerts
3. **Pass if:** Continuous bias monitoring is active with alert thresholds

**Remediation:** Implement real-time bias monitoring using Evidently AI or custom monitoring. Set alert thresholds based on regulatory guidance (e.g., Disparate Impact Ratio < 0.8).

## Fairness Metrics Reference
| Metric | Formula | Fair Threshold | Detection |
|--------|---------|----------------|-----------|
| **Disparate Impact Ratio** | P(positive | unprivileged) / P(positive | privileged) | ≥ 0.8 | Pre-deployment |
| **Statistical Parity Difference** | P(positive | unprivileged) - P(positive | privileged) | ±0.1 | Pre-deployment |
| **Equal Opportunity Difference** | TPR(unprivileged) - TPR(privileged) | ±0.05 | Pre-deployment + monitoring |
| **Average Odds Difference** | avg(FPR diff + TPR diff) | ±0.05 | Monitoring |

## Cross-References
- NIST AI RMF: Measure (MEASURE-2)
- EU AI Act: Transparency obligations (Article 13)
- AI Fairness 360 (AIF360) toolkit
