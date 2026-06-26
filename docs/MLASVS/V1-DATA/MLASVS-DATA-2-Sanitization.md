# MLASVS-DATA-2: Data Sanitization Controls

> **Subcategory:** V1: Data Security & Privacy
> **Controls:** DATA-004, DATA-005, DATA-010, DATA-011, DATA-013, DATA-014, DATA-015, DATA-016, DATA-017, DATA-018, DATA-024, DATA-025, DATA-029

## Overview

Data sanitization ensures that training and inference data is clean, validated, and free from poison, contamination, or adversarial manipulation. This subcategory covers input validation, quality checks, labeling security, and automated poisoning detection.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| DATA-004 | Input validation and sanitization | L1 | AML.TA0005 | TEST-DATA-002 | Validate all data inputs against defined schemas and ranges |
| DATA-005 | PII/PHI detection in training data | L1 | AML.TA0010 | TEST-DATA-002 | Detect and handle personally identifiable information in training data |
| DATA-010 | Data minimization | L1 | AML.TA0010 | TEST-DATA-002 | Collect only data necessary for the intended ML purpose |
| DATA-011 | Training data quality checks | L1 | AML.TA0005 | TEST-DATA-002 | Automated quality validation of training data before use |
| DATA-013 | Data labeling security | L1 | AML.TA0005 | TEST-DATA-002 | Secure data labeling workflows to prevent label manipulation |
| DATA-014 | Cross-contamination prevention | L1 | AML.TA0005 | TEST-DATA-002 | Prevent data leakage between training, validation, and test sets |
| DATA-015 | Data de-identification | L1 | AML.TA0010 | TEST-DATA-002 | Remove or mask sensitive identifiers from training data |
| DATA-016 | Consent and rights management | L1 | AML.TA0010 | TEST-DATA-002 | Ensure data usage complies with consent and data rights |
| DATA-017 | Data distribution analysis | L1 | AML.TA0005 | TEST-DATA-002 | Analyze data distributions to detect anomalies and drift |
| DATA-018 | Data corruption detection | L1 | AML.TA0005 | TEST-DATA-002 | Detect corrupted, malformed, or incomplete data records |
| DATA-024 | Automated data poisoning detection | L2 | AML.TA0005 | TEST-DATA-002 | Automated detection of poisoned training data samples |
| DATA-025 | Adversarial data filtering | L2 | AML.TA0005 | TEST-DATA-002 | Filter adversarial or manipulated samples from training data |
| DATA-029 | Synthetic data validation | L2 | AML.TA0005 | TEST-DATA-002 | Validate quality and representativeness of synthetic training data |

## Implementation Guidance

### Input Validation
- Define strict schemas for all data inputs
- Reject records with missing required fields, invalid types, or out-of-range values
- Log all rejected records for audit purposes

### Quality Checks
- Automate statistical validation (distribution, range, completeness)
- Flag records that deviate significantly from expected distributions
- Implement human review for flagged anomalies

### Labeling Security
- Use multiple annotators with inter-annotator agreement metrics
- Audit labeling consistency across demographic groups
- Version-control labeled datasets with annotator attribution

## Related

- [MLASTG-TEST-DATA-002: Data Sanitization Validation](../../MLASTG/DATA-Tests/MLASTG-TEST-DATA-002.md)
- [MLASWE-0002: Data Poisoning](../../MLASWE/MLASWE-0002-Data-Poisoning.md)
- **MITRE ATLAS:** AML.TA0005 (Execution), AML.TA0010 (Collection)
