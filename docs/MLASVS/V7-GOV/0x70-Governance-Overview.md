# V7: Governance & Compliance — MLASVS-GOV

## Overview

Governance and compliance controls ensure that ML systems are developed, deployed, and operated within a framework of accountability, transparency, and regulatory compliance. These controls address risk management, bias and fairness testing, audit readiness, and regulatory mapping (EU AI Act, NIST AI RMF, etc.).

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| Governance failure | — | — |
| Undetected model bias | — | — |
| Regulatory non-compliance | — | — |
| Inadequate audit trail | AML.TA0009 | — |
| Overreliance on AI decisions | AML.T0056 | — |

## Subcategories

### GOV-1: Risk Governance (Controls GOV-001 through GOV-006)
Organizational framework for ML risk management.

### GOV-2: Bias & Fairness (Controls GOV-007 through GOV-012)
Testing and monitoring for model bias and fairness.

### GOV-3: Audit & Compliance (Controls GOV-013 through GOV-020)
Audit readiness and regulatory compliance.

## Control Inventory

### L1 Controls (10)

| ID | Control | NIST AI RMF | Test Ref |
|----|---------|-------------|----------|
| GOV-001 | ML system inventory | Govern | TEST-GOV-001 |
| GOV-002 | ML risk assessment requirement | Govern | TEST-GOV-001 |
| GOV-003 | ML security policy | Govern | TEST-GOV-001 |
| GOV-004 | Data governance policy | Govern | TEST-GOV-001 |
| GOV-005 | Model documentation (model cards) | Map | TEST-GOV-001 |
| GOV-006 | Incident response plan | Manage | TEST-GOV-001 |
| GOV-007 | Bias evaluation requirement | Measure | TEST-GOV-001 |
| GOV-008 | Model performance monitoring | Measure | TEST-GOV-001 |
| GOV-009 | Audit logging for ML decisions | Measure | TEST-GOV-001 |
| GOV-010 | Third-party AI risk assessment | Map | TEST-GOV-001 |

### L2 Controls (10)

| ID | Control | NIST AI RMF | Test Ref |
|----|---------|-------------|----------|
| GOV-011 | AI ethics board | Govern | TEST-GOV-001 |
| GOV-012 | Human-in-the-loop critical decisions | Manage | TEST-GOV-001 |
| GOV-013 | Continuous compliance monitoring | Measure | TEST-GOV-001 |
| GOV-014 | External audit readiness | Govern | TEST-GOV-001 |
| GOV-015 | EU AI Act conformity assessment | Govern | TEST-GOV-001 |
| GOV-016 | Regular red team exercises | Measure | TEST-GOV-001 |
| GOV-017 | Bias continuous monitoring | Measure | TEST-GOV-001 |
| GOV-018 | Transparency reporting | Map | TEST-GOV-001 |
| GOV-019 | Regulatory filing automation | Govern | TEST-GOV-001 |
| GOV-020 | ML system impact assessment | Map | TEST-GOV-001 |

## Regulatory Mapping

### EU AI Act
| EU AI Act Requirement | MLASVS-GOV Controls |
|----------------------|---------------------|
| Risk classification | GOV-001, GOV-002 |
| Transparency obligations | GOV-005, GOV-018 |
| Human oversight | GOV-012 |
| Accuracy and robustness | GOV-008, GOV-016 |
| Record keeping | GOV-009, GOV-019 |

### NIST AI RMF
| RMF Function | MLASVS-GOV Controls |
|-------------|---------------------|
| Govern | GOV-001, GOV-002, GOV-003, GOV-004, GOV-011, GOV-014, GOV-015, GOV-019 |
| Map | GOV-005, GOV-010, GOV-018, GOV-020 |
| Measure | GOV-007, GOV-008, GOV-009, GOV-013, GOV-016, GOV-017 |
| Manage | GOV-006, GOV-012 |

## Related Links

- [MLASTG Test Cases: Governance](../../MLASTG/GOV-Tests/0x00-Gov-Tests-Overview.md)
