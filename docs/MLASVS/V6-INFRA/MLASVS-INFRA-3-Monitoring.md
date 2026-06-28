# MLASVS-INFRA-3: Monitoring & Incident Response

## Category
MLASVS-INFRA: Runtime & Infrastructure

## Overview
Monitoring and incident response for ML systems requires capabilities beyond traditional IT monitoring — including model behavior monitoring, drift detection, adversarial pattern recognition, and ML-specific playbooks.

## Controls

### INFRA-007: Inference Request Logging (L1)
**Description:** All inference requests and responses must be logged for audit and monitoring.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify that all inference API calls are logged with: user/API key, input metadata (not raw data), model version, timestamp, response status
2. Check that logs are stored in immutable, append-only storage
3. **Pass if:** All inference requests are logged with retention ≥ 90 days

**Remediation:** Enable structured logging on model serving platform. Store logs in immutable storage (e.g., S3 Object Lock). Apply PII scrubbing before persistence.

---

### INFRA-013: Adversarial Input Detection at Inference (L2)
**Description:** Real-time detection of adversarial inputs during inference to block evasion attacks.
**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify adversarial input detection is deployed inline in the inference path
2. Test with known adversarial patterns (FGSM, PGD samples)
3. **Pass if:** Detection identifies adversarial inputs with > 80% accuracy and < 5% false positive rate

**Remediation:** Deploy feature squeezing as a preprocessing filter. Use an ML-based detector (classifier) on input embeddings to flag anomalies.

---

### INFRA-014: Runtime Model Behavior Monitoring (L2)
**Description:** Continuous monitoring of model behavior metrics to detect compromise.
**MITRE ATLAS:** AML.T0018 (Manipulate AI Model)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify monitoring of: prediction distribution shifts, confidence score anomalies, latency changes, error rates
2. Check that statistically significant deviations trigger alerts
3. **Pass if:** Runtime monitoring detects anomalous behavior within 5 minutes

**Remediation:** Implement statistical process control (SPC) on model outputs. Use drift detection libraries (Evidently AI, NannyML, WhyLabs) with automated alerting.

---

### INFRA-019: ML-Specific SIEM Integration (L2)
**Description:** ML security events must feed into SIEM for correlation.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify ML security events (inference anomalies, access violations, drift alerts) are forwarded to SIEM
2. Check that correlation rules exist for ML-specific threat patterns
3. **Pass if:** ML events are integrated into SIEM with active alerts

**Remediation:** Configure structured logging in JSON format for all ML events. Forward to SIEM (Splunk, ELK, Sentinel) with ML-specific dashboards.

---

### INFRA-020: Dedicated ML Incident Response Playbook (L2)
**Description:** Specialized IR playbook for ML security incidents.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Review ML IR playbook document
2. Verify it covers: data poisoning, model extraction, adversarial attack, supply chain compromise, drift-based safety failures
3. Check that playbook is tested at least annually through tabletop exercises
4. **Pass if:** ML IR playbook exists, covers all ML-specific scenarios, and is tested

**Remediation:** Develop ML-specific incident response playbook modeled on NIST SP 800-61. Conduct quarterly tabletop exercises.

---

### MON-001: Alerting Thresholds (L1)
**Description:** Alert thresholds for model behavior anomalies must be defined and documented.
**MITRE ATLAS:** AML.T0018 (Manipulate AI Model)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify thresholds are defined for: accuracy degradation, latency increase, error rate rise, drift magnitude, query volume anomaly
2. Check that thresholds are reviewed quarterly
3. **Pass if:** Alert thresholds are defined, documented, and reviewed

**Remediation:** Define baseline metrics from historical data. Set thresholds at 3-sigma or 95th percentile. Review and adjust quarterly.

## Cross-References
- MITRE ATLAS: AML.TA0009, AML.T0010, AML.T0056
- NIST AI RMF: MEASURE-2, MANAGE-1
- NIST SP 800-61 (Incident Response)
