# V1: Data Security & Privacy — MLASVS-DATA

## Overview

Data is the foundation of any ML system. Compromised training data leads to compromised models. This category covers security controls for the entire data lifecycle: collection, storage, processing, labeling, training, and disposal.

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| Data poisoning (training) | AML.T0020 | MLASWE-0002 |
| Data poisoning (label manipulation) | AML.T0020 | MLASWE-0002 |
| Data exfiltration | AML.TA0010 | MLASWE-0012 |
| Supply chain via compromised datasets | AML.T0020 | MLASWE-0009 |
| Privacy leakage from training data | AML.T0018 | MLASWE-0012 |
| Data integrity compromise | AML.TA0005 | MLASWE-0002 |

## Subcategories

### DATA-1: Data Provenance (Controls DATA-001, DATA-002, DATA-006, DATA-020, DATA-026, DATA-030)
Ensuring data origin, transformation history, and integrity are verifiable.

### DATA-2: Data Sanitization (Controls DATA-004, DATA-005, DATA-010, DATA-011, DATA-013, DATA-014, DATA-015, DATA-016, DATA-017, DATA-018, DATA-024, DATA-025, DATA-029)
Ensuring training and inference data is clean, validated, and free from poison/contamination.

### DATA-3: Differential Privacy (Controls DATA-019, DATA-022, DATA-023)
Ensuring training algorithms incorporate privacy guarantees.

### DATA-4: Access Control (Controls DATA-003, DATA-007, DATA-008, DATA-009, DATA-012, DATA-021, DATA-027, DATA-028)
Ensuring data is properly protected and access is controlled.

## Control Inventory

### L1 Controls (18)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| DATA-001 | Data provenance tracking | AML.TA0009 | TEST-DATA-001 |
| DATA-002 | Cryptographic data integrity | AML.TA0010 | TEST-DATA-001 |
| DATA-003 | Data access control enforcement | AML.TA0002 | TEST-DATA-004 |
| DATA-004 | Input validation and sanitization | AML.TA0005 | TEST-DATA-002 |
| DATA-005 | PII/PHI detection in training data | AML.TA0010 | TEST-DATA-002 |
| DATA-006 | Data lineage documentation | AML.TA0009 | TEST-DATA-001 |
| DATA-007 | Secure data storage | AML.TA0002 | TEST-DATA-004 |
| DATA-008 | Data encryption at rest | AML.TA0010 | TEST-DATA-004 |
| DATA-009 | Data encryption in transit | AML.TA0010 | TEST-DATA-004 |
| DATA-010 | Data minimization | AML.TA0010 | TEST-DATA-002 |
| DATA-011 | Training data quality checks | AML.TA0005 | TEST-DATA-002 |
| DATA-012 | Data retention policy | AML.TA0010 | TEST-DATA-004 |
| DATA-013 | Data labeling security | AML.TA0005 | TEST-DATA-002 |
| DATA-014 | Cross-contamination prevention | AML.TA0005 | TEST-DATA-002 |
| DATA-015 | Data de-identification | AML.TA0010 | TEST-DATA-002 |
| DATA-016 | Consent and rights management | AML.TA0010 | TEST-DATA-002 |
| DATA-017 | Data distribution analysis | AML.TA0005 | TEST-DATA-002 |
| DATA-018 | Data corruption detection | AML.TA0005 | TEST-DATA-002 |

### L2 Controls (12)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| DATA-019 | Differential privacy (ε-guarantee) | AML.TA0010 | TEST-DATA-003 |
| DATA-020 | Cryptographic data provenance | AML.TA0009 | TEST-DATA-001 |
| DATA-021 | Federated data governance | AML.TA0002 | TEST-DATA-004 |
| DATA-022 | Secure multi-party computation | AML.TA0010 | TEST-DATA-003 |
| DATA-023 | Homomorphic encryption support | AML.TA0010 | TEST-DATA-003 |
| DATA-024 | Automated data poisoning detection | AML.TA0005 | TEST-DATA-002 |
| DATA-025 | Adversarial data filtering | AML.TA0005 | TEST-DATA-002 |
| DATA-026 | Real-time data integrity monitoring | AML.TA0010 | TEST-DATA-001 |
| DATA-027 | Data usage auditing | AML.TA0009 | TEST-DATA-004 |
| DATA-028 | Cross-border data compliance | AML.TA0010 | TEST-DATA-004 |
| DATA-029 | Synthetic data validation | AML.TA0005 | TEST-DATA-002 |
| DATA-030 | Data trust scoring | AML.TA0009 | TEST-DATA-001 |

## Related EW Links

- [MLASTG Test Cases: Data Security](../../MLASTG/DATA-Tests/0x00-Data-Tests-Overview.md)
- [MLASWE-0002: Data Poisoning](../../MLASWE/MLASWE-0002-Data-Poisoning.md)
- [MLASWE-0012: Training Data Leakage](../../MLASWE/MLASWE-0012-Training-Data-Leakage.md)
