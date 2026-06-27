# MLASVS Categories Overview

## Complete Control Inventory

### V1: Data Security & Privacy — 30 Controls (18 L1 + 12 L2)

> **Note (DATA-3 numbering):** Two files cover DATA-3 differential privacy — `MLASVS-DATA-3-Differential-Privacy.md` (standard ε-DP) and `MLASVS-DATA-3-Differential-Privacy-FL.md` (federated learning variant, referred to as DATA-3a). Both are counted under the existing 30-control total. See DATA-019 (standard DP) and DATA-021 (federated data governance) in the table below.

| ID | Control | Level | MITRE ATLAS | Test Reference |
|----|---------|-------|-------------|----------------|
| DATA-001 | Data provenance tracking | L1 | AML.TA0009 | TEST-DATA-001 |
| DATA-002 | Cryptographic data integrity | L1 | AML.TA0010 | TEST-DATA-001 |
| DATA-003 | Data access control enforcement | L1 | AML.TA0002 | TEST-DATA-004 |
| DATA-004 | Input validation and sanitization | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-005 | PII/PHI detection in training data | L1 | AML.TA0010 | TEST-DATA-002 |
| DATA-006 | Data lineage documentation | L1 | AML.TA0009 | TEST-DATA-001 |
| DATA-007 | Secure data storage | L1 | AML.TA0002 | TEST-DATA-004 |
| DATA-008 | Data encryption at rest | L1 | AML.TA0010 | TEST-DATA-004 |
| DATA-009 | Data encryption in transit | L1 | AML.TA0010 | TEST-DATA-004 |
| DATA-010 | Data minimization | L1 | AML.TA0010 | TEST-DATA-002 |
| DATA-011 | Training data quality checks | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-012 | Data retention policy | L1 | AML.TA0010 | TEST-DATA-004 |
| DATA-013 | Data labeling security | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-014 | Cross-contamination prevention | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-015 | Data de-identification | L1 | AML.TA0010 | TEST-DATA-002 |
| DATA-016 | Consent and rights management | L1 | AML.TA0010 | TEST-DATA-002 |
| DATA-017 | Data distribution analysis | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-018 | Data corruption detection | L1 | AML.TA0005 | TEST-DATA-002 |
| DATA-019 | Differential privacy (ε-guarantee) | L2 | AML.TA0010 | TEST-DATA-003 |
| DATA-020 | Cryptographic data provenance | L2 | AML.TA0009 | TEST-DATA-001 |
| DATA-021 | Federated data governance | L2 | AML.TA0002 | TEST-DATA-004 |
| DATA-022 | Secure multi-party computation | L2 | AML.TA0010 | TEST-DATA-003 |
| DATA-023 | Homomorphic encryption support | L2 | AML.TA0010 | TEST-DATA-003 |
| DATA-024 | Automated data poisoning detection | L2 | AML.TA0005 | TEST-DATA-002 |
| DATA-025 | Adversarial data filtering | L2 | AML.TA0005 | TEST-DATA-002 |
| DATA-026 | Real-time data integrity monitoring | L2 | AML.TA0010 | TEST-DATA-001 |
| DATA-027 | Data usage auditing | L2 | AML.TA0009 | TEST-DATA-004 |
| DATA-028 | Cross-border data compliance | L2 | AML.TA0010 | TEST-DATA-004 |
| DATA-029 | Synthetic data validation | L2 | AML.TA0005 | TEST-DATA-002 |
| DATA-030 | Data trust scoring | L2 | AML.TA0009 | TEST-DATA-001 |

### V2: Model Security — 30 Controls (15 L1 + 15 L2)

| ID | Control | Level | MITRE ATLAS | Test Reference |
|----|---------|-------|-------------|----------------|
| MODEL-001 | Adversarial robustness testing | L1 | AML.T0010 | TEST-MODEL-001 |
| MODEL-002 | Input perturbation limits | L1 | AML.T0010 | TEST-MODEL-001 |
| MODEL-003 | Model input validation | L1 | AML.T0007 | TEST-MODEL-001 |
| MODEL-004 | Output confidence calibration | L1 | AML.T0018 | TEST-MODEL-002 |
| MODEL-005 | API rate limiting | L1 | AML.T0034 | TEST-MODEL-002 |
| MODEL-006 | Access control on model endpoints | L1 | AML.TA0002 | TEST-MODEL-002 |
| MODEL-007 | Model versioning | L1 | AML.TA0006 | TEST-MODEL-005 |
| MODEL-008 | Model signing | L1 | AML.TA0006 | TEST-MODEL-005 |
| MODEL-009 | Inference logging | L1 | AML.TA0009 | TEST-MODEL-003 |
| MODEL-010 | Anomalous input detection | L1 | AML.T0010 | TEST-MODEL-001 |
| MODEL-011 | Output sanitization | L1 | AML.T0018 | TEST-MODEL-003 |
| MODEL-012 | Resource limits on inference | L1 | AML.T0037 | TEST-MODEL-001 |
| MODEL-013 | Model behavior monitoring | L1 | AML.T0056 | TEST-MODEL-003 |
| MODEL-014 | Secure model serialization | L1 | AML.TA0002 | TEST-MODEL-005 |
| MODEL-015 | Model rollback capability | L1 | AML.TA0006 | TEST-MODEL-005 |
| MODEL-016 | Certified adversarial robustness | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-017 | Robustness certification (provable bounds) | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-018 | Extraction resistance validation | L2 | AML.T0034 | TEST-MODEL-002 |
| MODEL-019 | Differential privacy in model | L2 | AML.T0018 | TEST-MODEL-003 |
| MODEL-020 | Membership inference prevention | L2 | AML.T0018 | TEST-MODEL-003 |
| MODEL-021 | Backdoor detection validation | L2 | AML.T0020 | TEST-MODEL-004 |
| MODEL-022 | Trojan detection | L2 | AML.T0020 | TEST-MODEL-004 |
| MODEL-023 | Model watermarking | L2 | AML.T0034 | TEST-MODEL-002 |
| MODEL-024 | Adversarial training validation | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-025 | Feature squeezing validation | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-026 | Model ensemble diversity | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-027 | Certified defense mechanisms | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-028 | Red team exercise completion | L2 | AML.TA0001 | TEST-MODEL-001 |
| MODEL-029 | Continuous adversarial retesting | L2 | AML.T0010 | TEST-MODEL-001 |
| MODEL-030 | Model provenance attestation | L2 | AML.TA0006 | TEST-MODEL-005 |

### V3: LLM Security — 24 Controls (14 L1 + 10 L2)

| ID | Control | Level | MITRE ATLAS | Test Reference |
|----|---------|-------|-------------|----------------|
| LLM-001 | Prompt injection prevention | L1 | AML.T0051 | TEST-LLM-001 |
| LLM-002 | Input/output boundary enforcement | L1 | AML.T0051 | TEST-LLM-001 |
| LLM-003 | Output validation and filtering | L1 | AML.T0052 | TEST-LLM-002 |
| LLM-004 | System prompt isolation | L1 | AML.T0051 | TEST-LLM-001 |
| LLM-005 | Context window limits | L1 | AML.T0037 | TEST-LLM-003 |
| LLM-006 | Plugin permission scoping | L1 | AML.T0053 | TEST-LLM-001 |
| LLM-007 | Tool call authorization | L1 | AML.T0053 | TEST-LLM-001 |
| LLM-008 | Sensitive data exfiltration prevention | L1 | AML.T0052 | TEST-LLM-002 |
| LLM-009 | Content filtering pipeline | L1 | AML.T0052 | TEST-LLM-002 |
| LLM-010 | Human-in-the-loop for critical actions | L1 | AML.T0053 | TEST-LLM-003 |
| LLM-011 | Rate limiting on LLM endpoints | L1 | AML.T0037 | TEST-LLM-003 |
| LLM-012 | Token usage monitoring | L1 | AML.T0037 | TEST-LLM-003 |
| LLM-013 | Input token limits | L1 | AML.T0037 | TEST-LLM-003 |
| LLM-014 | Output length limits | L1 | AML.T0052 | TEST-LLM-002 |
| LLM-015 | Prompt firewall deployment | L2 | AML.T0051 | TEST-LLM-001 |
| LLM-016 | Semantic prompt filtering | L2 | AML.T0051 | TEST-LLM-001 |
| LLM-017 | Jailbreak detection system | L2 | AML.T0051 | TEST-LLM-003 |
| LLM-018 | RAG security controls | L2 | AML.T0051 | TEST-LLM-001 |
| LLM-019 | Embedding-level anomaly detection | L2 | AML.T0051 | TEST-LLM-001 |
| LLM-020 | Agentic workflow authorization | L2 | AML.T0053 | TEST-LLM-003 |
| LLM-021 | Tool/plugin isolation sandbox | L2 | AML.T0053 | TEST-LLM-001 |
| LLM-022 | Continuous red teaming pipeline | L2 | AML.T0051 | TEST-LLM-003 |
| LLM-023 | Human override mechanisms | L2 | AML.T0053 | TEST-LLM-003 |
| LLM-024 | Multi-turn attack detection | L2 | AML.T0051 | TEST-LLM-003 |

### V4-V7: Refer to category-specific documents

- [V4: Supply Chain Security](V4-SUPPLY/0x40-Supply-Chain-Overview.md) — 22 controls
- [V5: Pipeline & MLOps](V5-PIPELINE/0x50-Pipeline-Overview.md) — 20 controls
- [V6: Runtime & Infrastructure](V6-INFRA/0x60-Runtime-Overview.md) — 22 controls
- [V7: Governance & Compliance](V7-GOV/0x70-Governance-Overview.md) — 20 controls
