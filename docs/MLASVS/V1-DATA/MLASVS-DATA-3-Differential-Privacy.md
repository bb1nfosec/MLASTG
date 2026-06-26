# MLASVS-DATA-3: Differential Privacy Controls

> **Subcategory:** V1: Data Security & Privacy
> **Controls:** DATA-019, DATA-022, DATA-023

## Overview

Differential privacy controls ensure that ML training algorithms incorporate formal privacy guarantees, preventing adversaries from extracting information about individual training data records. This subcategory covers epsilon-guaranteed differential privacy, secure multi-party computation, and homomorphic encryption.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| DATA-019 | Differential privacy (ε-guarantee) | L2 | AML.TA0010 | TEST-DATA-003 | Implement differential privacy with documented epsilon budget |
| DATA-022 | Secure multi-party computation | L2 | AML.TA0010 | TEST-DATA-003 | Enable collaborative ML training without exposing raw data |
| DATA-023 | Homomorphic encryption support | L2 | AML.TA0010 | TEST-DATA-003 | Support computation on encrypted data for privacy-preserving inference |

## Implementation Guidance

### Differential Privacy
- Use DP-SGD (Differentially Private Stochastic Gradient Descent) during training
- Document and track the privacy budget (ε, δ) across all training runs
- Recommended ε values: ≤ 10 for standard data, ≤ 2 for sensitive data (healthcare, finance)
- Use libraries: Opacus (PyTorch), TF Privacy (TensorFlow), diffprivlib (scikit-learn)

### Secure Multi-Party Computation
- Enable federated learning for cross-organizational model training
- Use secure aggregation protocols to prevent server-side data access
- Validate that no single party can reconstruct another party's data

### Homomorphic Encryption
- Support encrypted inference for highly sensitive deployment contexts
- Evaluate computational overhead vs. privacy requirements
- Use libraries: TenSEAL, SEAL (Microsoft)

## Privacy Budget Guidance

| Data Sensitivity | Recommended ε | Justification Required |
|-----------------|---------------|----------------------|
| Public/Non-sensitive | ≤ 10 | Standard documentation |
| Internal/Business | ≤ 5 | Risk assessment |
| Sensitive (PII) | ≤ 2 | Detailed justification |
| Highly sensitive (PHI, biometric) | ≤ 1 | CISO approval |

## Related

- [MLASTG-TEST-DATA-003: Differential Privacy Audit](../../MLASTG/DATA-Tests/MLASTG-TEST-DATA-003.md)
- [MLASWE-0005: Membership Inference](../../MLASWE/MLASWE-0005-Membership-Inference.md)
- **MITRE ATLAS:** AML.TA0010 (Collection)
- **NIST AI RMF:** MEASURE 2.5 (Data quality)
