# V2: Model Security — MLASVS-MODEL

## Overview

Model security addresses attacks that target the trained model itself. These include adversarial evasion (manipulating inputs to cause misclassification), extraction (stealing model parameters or behavior), inversion (reconstructing training data), and backdoor/trojan attacks (hidden malicious behaviors).

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| Adversarial evasion | AML.T0010 | MLASWE-0001 |
| Model extraction | AML.T0024.002 | MLASWE-0003 |
| Model inversion | AML.T0018 | MLASWE-0004 |
| Membership inference | AML.T0018 | MLASWE-0005 |
| Backdoor/trojan attack | AML.T0020 | MLASWE-0007 |
| Model denial of service | AML.T0029 | MLASWE-0008 |

## Subcategories

### MODEL-1: Adversarial Robustness (Controls MODEL-001, MODEL-002, MODEL-003, MODEL-010, MODEL-012, MODEL-016, MODEL-017, MODEL-024, MODEL-025, MODEL-026, MODEL-027, MODEL-028, MODEL-029)
Testing and hardening against evasion attacks using perturbation-based inputs.

### MODEL-2: Extraction Prevention (Controls MODEL-004, MODEL-005, MODEL-006, MODEL-018, MODEL-023)
Preventing adversaries from stealing model behavior or parameters.

### MODEL-3: Inversion & Privacy (Controls MODEL-009, MODEL-011, MODEL-013, MODEL-019, MODEL-020)
Preventing adversaries from inferring training data from model outputs.

### MODEL-4: Backdoor Detection (Controls MODEL-021, MODEL-022)
Detecting hidden malicious behaviors injected during training.

### MODEL-5: Model Integrity (Controls MODEL-007, MODEL-008, MODEL-014, MODEL-015, MODEL-030)
Ensuring models are authentic, untampered, and properly versioned.

## Control Inventory

### L1 Controls (15)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| MODEL-001 | Adversarial robustness testing | AML.T0015 | TEST-MODEL-001 |
| MODEL-002 | Input perturbation limits | AML.T0015 | TEST-MODEL-001 |
| MODEL-003 | Model input validation | AML.T0043 | TEST-MODEL-001 |
| MODEL-004 | Output confidence calibration | AML.T0024.001 | TEST-MODEL-002 |
| MODEL-005 | API rate limiting | AML.T0024.002 | TEST-MODEL-002 |
| MODEL-006 | Access control on model endpoints | AML.TA0002 | TEST-MODEL-002 |
| MODEL-007 | Model versioning | AML.TA0006 | TEST-MODEL-005 |
| MODEL-008 | Model signing | AML.TA0006 | TEST-MODEL-005 |
| MODEL-009 | Inference logging | AML.TA0009 | TEST-MODEL-003 |
| MODEL-010 | Anomalous input detection | AML.T0015 | TEST-MODEL-001 |
| MODEL-011 | Output sanitization | AML.T0024.001 | TEST-MODEL-003 |
| MODEL-012 | Resource limits on inference | AML.T0029 | TEST-MODEL-001 |
| MODEL-013 | Model behavior monitoring | AML.T0018 | TEST-MODEL-003 |
| MODEL-014 | Secure model serialization | AML.TA0002 | TEST-MODEL-005 |
| MODEL-015 | Model rollback capability | AML.TA0006 | TEST-MODEL-005 |

### L2 Controls (15)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| MODEL-016 | Certified adversarial robustness | AML.T0015 | TEST-MODEL-001 |
| MODEL-017 | Robustness certification (provable bounds) | AML.T0015 | TEST-MODEL-001 |
| MODEL-018 | Extraction resistance validation | AML.T0024.002 | TEST-MODEL-002 |
| MODEL-019 | Differential privacy in model | AML.T0024.000 | TEST-MODEL-003 |
| MODEL-020 | Membership inference prevention | AML.T0024.000 | TEST-MODEL-003 |
| MODEL-021 | Backdoor detection validation | AML.T0020 | TEST-MODEL-004 |
| MODEL-022 | Trojan detection | AML.T0020 | TEST-MODEL-004 |
| MODEL-023 | Model watermarking | AML.T0024.002 | TEST-MODEL-002 |
| MODEL-024 | Adversarial training validation | AML.T0015 | TEST-MODEL-001 |
| MODEL-025 | Feature squeezing validation | AML.T0015 | TEST-MODEL-001 |
| MODEL-026 | Model ensemble diversity | AML.T0015 | TEST-MODEL-001 |
| MODEL-027 | Certified defense mechanisms | AML.T0015 | TEST-MODEL-001 |
| MODEL-028 | Red team exercise completion | AML.TA0001 | TEST-MODEL-001 |
| MODEL-029 | Continuous adversarial retesting | AML.T0015 | TEST-MODEL-001 |
| MODEL-030 | Model provenance attestation | AML.TA0006 | TEST-MODEL-005 |

## Related EW Links

- [MLASTG Test Cases: Model Security](../../MLASTG/MODEL-Tests/0x00-Model-Tests-Overview.md)
- [MLASWE-0001: Adversarial Perturbation](../../MLASWE/MLASWE-0001-Adversarial-Perturbation.md)
- [MLASWE-0003: Model Extraction](../../MLASWE/MLASWE-0003-Model-Extraction.md)
- [MLASWE-0004: Model Inversion](../../MLASWE/MLASWE-0004-Model-Inversion.md)
- [MLASWE-0005: Membership Inference](../../MLASWE/MLASWE-0005-Membership-Inference.md)
- [MLASWE-0007: Backdoor/Trojan](../../MLASWE/MLASWE-0007-Backdoor-Trojan.md)
