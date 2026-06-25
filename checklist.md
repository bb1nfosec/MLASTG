# MLASTG Assessment Checklist

> Use this checklist to track progress during an ML security assessment.
> Mark each control as ✅ Pass, ❌ Fail, ⚠️ Partial, 🔲 Not Tested, or N/A.

## Project Information

| Field | Value |
|-------|-------|
| **System Name** | |
| **Assessment Date** | |
| **Assessor** | |
| **Target Level** | L1 / L2 |
| **ML System Type** | |
| **Model Architecture** | |

---

## V1: Data Security & Privacy (MLASVS-DATA)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| DATA-001 | Data provenance tracking | 🔲 | |
| DATA-002 | Cryptographic data integrity | 🔲 | |
| DATA-003 | Data access control enforcement | 🔲 | |
| DATA-004 | Input validation and sanitization | 🔲 | |
| DATA-005 | PII/PHI detection in training data | 🔲 | |
| DATA-006 | Data lineage documentation | 🔲 | |
| DATA-007 | Secure data storage | 🔲 | |
| DATA-008 | Data encryption at rest | 🔲 | |
| DATA-009 | Data encryption in transit | 🔲 | |
| DATA-010 | Data minimization | 🔲 | |
| DATA-011 | Training data quality checks | 🔲 | |
| DATA-012 | Data retention policy | 🔲 | |
| DATA-013 | Data labeling security | 🔲 | |
| DATA-014 | Cross-contamination prevention | 🔲 | |
| DATA-015 | Data de-identification | 🔲 | |
| DATA-016 | Consent and rights management | 🔲 | |
| DATA-017 | Data distribution analysis | 🔲 | |
| DATA-018 | Data corruption detection | 🔲 | |

**L1 Pass Rate:** _____ / 18 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| DATA-019 | Differential privacy (ε-guarantee) | 🔲 | |
| DATA-020 | Cryptographic data provenance | 🔲 | |
| DATA-021 | Federated data governance | 🔲 | |
| DATA-022 | Secure multi-party computation | 🔲 | |
| DATA-023 | Homomorphic encryption support | 🔲 | |
| DATA-024 | Automated data poisoning detection | 🔲 | |
| DATA-025 | Adversarial data filtering | 🔲 | |
| DATA-026 | Real-time data integrity monitoring | 🔲 | |
| DATA-027 | Data usage auditing | 🔲 | |
| DATA-028 | Cross-border data compliance | 🔲 | |
| DATA-029 | Synthetic data validation | 🔲 | |
| DATA-030 | Data trust scoring | 🔲 | |

**L2 Pass Rate:** _____ / 12 (_____%)

---

## V2: Model Security (MLASVS-MODEL)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| MODEL-001 | Adversarial robustness testing | 🔲 | |
| MODEL-002 | Input perturbation limits | 🔲 | |
| MODEL-003 | Model input validation | 🔲 | |
| MODEL-004 | Output confidence calibration | 🔲 | |
| MODEL-005 | API rate limiting | 🔲 | |
| MODEL-006 | Access control on model endpoints | 🔲 | |
| MODEL-007 | Model versioning | 🔲 | |
| MODEL-008 | Model signing | 🔲 | |
| MODEL-009 | Inference logging | 🔲 | |
| MODEL-010 | Anomalous input detection | 🔲 | |
| MODEL-011 | Output sanitization | 🔲 | |
| MODEL-012 | Resource limits on inference | 🔲 | |
| MODEL-013 | Model behavior monitoring | 🔲 | |
| MODEL-014 | Secure model serialization | 🔲 | |
| MODEL-015 | Model rollback capability | 🔲 | |

**L1 Pass Rate:** _____ / 15 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| MODEL-016 | Certified adversarial robustness | 🔲 | |
| MODEL-017 | Robustness certification (provable bounds) | 🔲 | |
| MODEL-018 | Extraction resistance validation | 🔲 | |
| MODEL-019 | Differential privacy in model | 🔲 | |
| MODEL-020 | Membership inference prevention | 🔲 | |
| MODEL-021 | Backdoor detection validation | 🔲 | |
| MODEL-022 | Trojan detection | 🔲 | |
| MODEL-023 | Model watermarking | 🔲 | |
| MODEL-024 | Adversarial training validation | 🔲 | |
| MODEL-025 | Feature squeezing validation | 🔲 | |
| MODEL-026 | Model ensemble diversity | 🔲 | |
| MODEL-027 | Certified defense mechanisms | 🔲 | |
| MODEL-028 | Red team exercise completion | 🔲 | |
| MODEL-029 | Continuous adversarial retesting | 🔲 | |
| MODEL-030 | Model provenance attestation | 🔲 | |

**L2 Pass Rate:** _____ / 15 (_____%)

---

## V3: LLM Security (MLASVS-LLM)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| LLM-001 | Prompt injection prevention | 🔲 | |
| LLM-002 | Input/output boundary enforcement | 🔲 | |
| LLM-003 | Output validation and filtering | 🔲 | |
| LLM-004 | System prompt isolation | 🔲 | |
| LLM-005 | Context window limits | 🔲 | |
| LLM-006 | Plugin permission scoping | 🔲 | |
| LLM-007 | Tool call authorization | 🔲 | |
| LLM-008 | Sensitive data exfiltration prevention | 🔲 | |
| LLM-009 | Content filtering pipeline | 🔲 | |
| LLM-010 | Human-in-the-loop for critical actions | 🔲 | |
| LLM-011 | Rate limiting on LLM endpoints | 🔲 | |
| LLM-012 | Token usage monitoring | 🔲 | |
| LLM-013 | Input token limits | 🔲 | |
| LLM-014 | Output length limits | 🔲 | |

**L1 Pass Rate:** _____ / 14 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| LLM-015 | Prompt firewall deployment | 🔲 | |
| LLM-016 | Semantic prompt filtering | 🔲 | |
| LLM-017 | Jailbreak detection system | 🔲 | |
| LLM-018 | RAG security controls | 🔲 | |
| LLM-019 | Embedding-level anomaly detection | 🔲 | |
| LLM-020 | Agentic workflow authorization | 🔲 | |
| LLM-021 | Tool/plugin isolation sandbox | 🔲 | |
| LLM-022 | Continuous red teaming pipeline | 🔲 | |
| LLM-023 | Human override mechanisms | 🔲 | |
| LLM-024 | Multi-turn attack detection | 🔲 | |

**L2 Pass Rate:** _____ / 10 (_____%)

---

## V4: Supply Chain Security (MLASVS-SUPPLY)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| SUPPLY-001 | ML-SBOM generation | 🔲 | |
| SUPPLY-002 | Pre-trained model origin verification | 🔲 | |
| SUPPLY-003 | Training dataset provenance | 🔲 | |
| SUPPLY-004 | ML library version tracking | 🔲 | |
| SUPPLY-005 | License compliance check | 🔲 | |
| SUPPLY-006 | Model hash verification at load | 🔲 | |
| SUPPLY-007 | Transfer learning source validation | 🔲 | |
| SUPPLY-008 | Dataset license verification | 🔲 | |
| SUPPLY-009 | Base model vulnerability scanning | 🔲 | |
| SUPPLY-010 | ML dependency scanning | 🔲 | |
| SUPPLY-011 | Secure model distribution channels | 🔲 | |
| SUPPLY-012 | Third-party model evaluation report | 🔲 | |

**L1 Pass Rate:** _____ / 12 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| SUPPLY-013 | Automated ML-SBOM generation in CI/CD | 🔲 | |
| SUPPLY-014 | Continuous dependency monitoring | 🔲 | |
| SUPPLY-015 | Cryptographic model provenance | 🔲 | |
| SUPPLY-016 | Model signing and attestation | 🔲 | |
| SUPPLY-017 | Fine-tuning data provenance chain | 🔲 | |
| SUPPLY-018 | Adversarial robustness of base model | 🔲 | |
| SUPPLY-019 | Backdoor scanning of pre-trained models | 🔲 | |
| SUPPLY-020 | Vendor security assessment program | 🔲 | |
| SUPPLY-021 | ML supply chain incident response | 🔲 | |
| SUPPLY-022 | Reproducible build verification | 🔲 | |

**L2 Pass Rate:** _____ / 10 (_____%)

---

## V5: Pipeline & MLOps (MLASVS-PIPELINE)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| PIPELINE-001 | ML pipeline access control | 🔲 | |
| PIPELINE-002 | Pipeline artifact signing | 🔲 | |
| PIPELINE-003 | Experiment tracking access control | 🔲 | |
| PIPELINE-004 | Training environment isolation | 🔲 | |
| PIPELINE-005 | Pipeline secret management | 🔲 | |
| PIPELINE-006 | Run history audit logging | 🔲 | |
| PIPELINE-007 | Feature store access control | 🔲 | |
| PIPELINE-008 | Model registry authentication | 🔲 | |
| PIPELINE-009 | Deployment approval workflow | 🔲 | |
| PIPELINE-010 | Model deployment rollback | 🔲 | |

**L1 Pass Rate:** _____ / 10 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| PIPELINE-011 | Pipeline integrity monitoring | 🔲 | |
| PIPELINE-012 | Automated pipeline security scanning | 🔲 | |
| PIPELINE-013 | Immutable model registry | 🔲 | |
| PIPELINE-014 | Reproducible training verification | 🔲 | |
| PIPELINE-015 | Data leakage prevention in pipeline | 🔲 | |
| PIPELINE-016 | Cross-tenant isolation in ML platforms | 🔲 | |
| PIPELINE-017 | Pipeline compliance attestation | 🔲 | |
| PIPELINE-018 | Feature store data integrity | 🔲 | |
| PIPELINE-019 | Canary deployment for models | 🔲 | |
| PIPELINE-020 | Automated testing gate in CI/CD | 🔲 | |

**L2 Pass Rate:** _____ / 10 (_____%)

---

## V6: Runtime & Infrastructure (MLASVS-INFRA)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| INFRA-001 | Model serving network segmentation | 🔲 | |
| INFRA-002 | Inference endpoint authentication | 🔲 | |
| INFRA-003 | Inference endpoint authorization | 🔲 | |
| INFRA-004 | TLS for model endpoints | 🔲 | |
| INFRA-005 | GPU/compute isolation | 🔲 | |
| INFRA-006 | Model cache security | 🔲 | |
| INFRA-007 | Inference request logging | 🔲 | |
| INFRA-008 | Batch inference security | 🔲 | |
| INFRA-009 | API rate limiting | 🔲 | |
| INFRA-010 | Input size validation | 🔲 | |
| INFRA-011 | API versioning | 🔲 | |
| INFRA-012 | Model health monitoring | 🔲 | |

**L1 Pass Rate:** _____ / 12 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| INFRA-013 | Adversarial input detection at inference | 🔲 | |
| INFRA-014 | Runtime model behavior monitoring | 🔲 | |
| INFRA-015 | Automated model rollback on anomaly | 🔲 | |
| INFRA-016 | Side-channel attack prevention | 🔲 | |
| INFRA-017 | Confidential computing for inference | 🔲 | |
| INFRA-018 | Real-time drift monitoring | 🔲 | |
| INFRA-019 | ML-specific SIEM integration | 🔲 | |
| INFRA-020 | Dedicated ML incident response playbook | 🔲 | |
| INFRA-021 | Continuous penetration testing | 🔲 | |
| INFRA-022 | Hardware-rooted model attestation | 🔲 | |

**L2 Pass Rate:** _____ / 10 (_____%)

---

## V7: Governance & Compliance (MLASVS-GOV)

### L1 Controls

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| GOV-001 | ML system inventory | 🔲 | |
| GOV-002 | ML risk assessment requirement | 🔲 | |
| GOV-003 | ML security policy | 🔲 | |
| GOV-004 | Data governance policy | 🔲 | |
| GOV-005 | Model documentation (model cards) | 🔲 | |
| GOV-006 | Incident response plan | 🔲 | |
| GOV-007 | Bias evaluation requirement | 🔲 | |
| GOV-008 | Model performance monitoring | 🔲 | |
| GOV-009 | Audit logging for ML decisions | 🔲 | |
| GOV-010 | Third-party AI risk assessment | 🔲 | |

**L1 Pass Rate:** _____ / 10 (_____%)

### L2 Controls (Additional)

| ID | Control | Status | Notes |
|----|---------|--------|-------|
| GOV-011 | AI ethics board | 🔲 | |
| GOV-012 | Human-in-the-loop critical decisions | 🔲 | |
| GOV-013 | Continuous compliance monitoring | 🔲 | |
| GOV-014 | External audit readiness | 🔲 | |
| GOV-015 | EU AI Act conformity assessment | 🔲 | |
| GOV-016 | Regular red team exercises | 🔲 | |
| GOV-017 | Bias continuous monitoring | 🔲 | |
| GOV-018 | Transparency reporting | 🔲 | |
| GOV-019 | Regulatory filing automation | 🔲 | |
| GOV-020 | ML system impact assessment | 🔲 | |

**L2 Pass Rate:** _____ / 10 (_____%)

---

## Summary

| Category | L1 Controls | L1 Pass Rate | L2 Controls | L2 Pass Rate |
|----------|-------------|-------------|-------------|-------------|
| DATA | 18 | _____% | 12 | _____% |
| MODEL | 15 | _____% | 15 | _____% |
| LLM | 14 | _____% | 10 | _____% |
| SUPPLY | 12 | _____% | 10 | _____% |
| PIPELINE | 10 | _____% | 10 | _____% |
| INFRA | 12 | _____% | 10 | _____% |
| GOV | 10 | _____% | 10 | _____% |
| **Total** | **91** | **_____%** | **77** | **_____%** |
| **Grand Total** | **168 controls** | **_____%** | | |

**Overall Assessment:**
- ✅ L1 Compliant (if all L1 controls pass)
- ✅ L2 Compliant (if all L1 + L2 controls pass)
- ❌ Non-compliant — remediate failed controls per severity

## Key Findings

| Finding | Severity | MLASWE Ref | Status |
|---------|----------|------------|--------|
| | | | |
| | | | |
