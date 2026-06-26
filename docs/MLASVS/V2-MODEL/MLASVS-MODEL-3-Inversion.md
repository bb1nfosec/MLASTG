# MLASVS-MODEL-3: Inversion & Privacy Controls

> **Subcategory:** V2: Model Security
> **Controls:** MODEL-009, MODEL-011, MODEL-013, MODEL-019, MODEL-020

## Overview

Model inversion and privacy controls prevent adversaries from reconstructing training data or inferring membership information from model outputs. This subcategory covers inference logging, output sanitization, behavior monitoring, differential privacy in models, and membership inference prevention.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| MODEL-009 | Inference logging | L1 | AML.TA0009 | TEST-MODEL-003 | Log inference requests with anonymized identifiers for audit |
| MODEL-011 | Output sanitization | L1 | AML.T0018 | TEST-MODEL-003 | Sanitize model outputs to prevent training data reconstruction |
| MODEL-013 | Model behavior monitoring | L1 | AML.T0056 | TEST-MODEL-003 | Monitor model behavior for anomalous patterns indicating attacks |
| MODEL-019 | Differential privacy in model | L2 | AML.T0018 | TEST-MODEL-003 | Implement differential privacy guarantees in model training |
| MODEL-020 | Membership inference prevention | L2 | AML.T0018 | TEST-MODEL-003 | Prevent adversaries from determining if specific records were in training data |

## Implementation Guidance

### Inference Logging
- Log: timestamp, request ID, model version, input shape (not raw data), output label (not full probabilities)
- Retain logs per data retention policy
- Ship logs to centralized SIEM

### Output Sanitization
- Limit confidence score precision (≤ 3 decimal places)
- Return label-only predictions where possible
- Apply prediction perturbation for sensitive deployments

### Differential Privacy in Models
- Use DP-SGD during training with documented epsilon budget
- Apply per-sample gradient clipping
- Validate privacy budget consumption across training iterations

## Related

- [MLASTG-TEST-MODEL-003: Membership Inference Testing](../../MLASTG/MODEL-Tests/MLASTG-TEST-MODEL-003.md)
- [MLASWE-0004: Model Inversion](../../MLASWE/MLASWE-0004-Model-Inversion.md)
- [MLASWE-0005: Membership Inference](../../MLASWE/MLASWE-0005-Membership-Inference.md)
- **MITRE ATLAS:** AML.T0018 (Model Inversion)
