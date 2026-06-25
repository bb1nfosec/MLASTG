# V6: Runtime & Infrastructure Security — MLASVS-INFRA

## Overview

Runtime and infrastructure security covers the production deployment of ML models — model serving infrastructure, API endpoints, monitoring systems, and incident response capabilities. Even a secure model can be compromised through infrastructure vulnerabilities.

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| Model serving infrastructure compromise | AML.TA0002 | — |
| API abuse / excessive queries | AML.T0034 | MLASWE-0003 |
| Denial of service against model endpoint | AML.T0037 | MLASWE-0008 |
| Inference data interception | AML.TA0010 | MLASWE-0012 |
| Side-channel attacks | AML.T0018 | — |
| Model cache poisoning | AML.TA0005 | — |

## Subcategories

### INFRA-1: Model Serving (Controls INFRA-001 through INFRA-008)
Security of model serving infrastructure (Kubernetes, TorchServe, TF Serving, Triton, etc.).

### INFRA-2: API Security (Controls INFRA-009 through INFRA-015)
Security of model inference APIs and endpoints.

### INFRA-3: Monitoring & Response (Controls INFRA-016 through INFRA-022)
Runtime monitoring, anomaly detection, and incident response for ML systems.

## Control Inventory

### L1 Controls (12)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| INFRA-001 | Model serving network segmentation | AML.TA0002 | TEST-INFRA-001 |
| INFRA-002 | Inference endpoint authentication | AML.TA0002 | TEST-INFRA-002 |
| INFRA-003 | Inference endpoint authorization | AML.TA0002 | TEST-INFRA-002 |
| INFRA-004 | TLS for model endpoints | AML.TA0010 | TEST-INFRA-002 |
| INFRA-005 | GPU/compute isolation | AML.TA0002 | TEST-INFRA-001 |
| INFRA-006 | Model cache security | AML.TA0005 | TEST-INFRA-001 |
| INFRA-007 | Inference request logging | AML.TA0009 | TEST-INFRA-001 |
| INFRA-008 | Batch inference security | AML.TA0002 | TEST-INFRA-001 |
| INFRA-009 | API rate limiting | AML.T0034 | TEST-INFRA-002 |
| INFRA-010 | Input size validation | AML.T0037 | TEST-INFRA-002 |
| INFRA-011 | API versioning | AML.TA0002 | TEST-INFRA-002 |
| INFRA-012 | Model health monitoring | AML.TA0005 | TEST-INFRA-001 |

### L2 Controls (10)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| INFRA-013 | Adversarial input detection at inference | AML.T0010 | TEST-INFRA-001 |
| INFRA-014 | Runtime model behavior monitoring | AML.T0056 | TEST-INFRA-001 |
| INFRA-015 | Automated model rollback on anomaly | AML.T0006 | TEST-INFRA-001 |
| INFRA-016 | Side-channel attack prevention | AML.T0018 | TEST-INFRA-001 |
| INFRA-017 | Confidential computing for inference | AML.TA0010 | TEST-INFRA-001 |
| INFRA-018 | Real-time drift monitoring | AML.T0056 | TEST-INFRA-001 |
| INFRA-019 | ML-specific SIEM integration | AML.TA0009 | TEST-INFRA-001 |
| INFRA-020 | Dedicated ML incident response playbook | AML.TA0009 | TEST-INFRA-001 |
| INFRA-021 | Continuous penetration testing | AML.TA0001 | TEST-INFRA-002 |
| INFRA-022 | Hardware-rooted model attestation | AML.TA0006 | TEST-INFRA-001 |

## Common ML Serving Security Checklist

- [ ] Model endpoint is not exposed to the public internet without WAF/auth
- [ ] Inference API enforces authentication and authorization
- [ ] All inference traffic is encrypted (TLS 1.2+)
- [ ] Rate limiting is configured per API key/user
- [ ] Input size is validated to prevent DoS
- [ ] Model caching does not leak data between users
- [ ] GPU memory is isolated between model replicas
- [ ] Inference logs do not capture raw PII/proprietary data
- [ ] Model health checks are implemented
- [ ] Canary deployment is supported

## Related Links

- [MLASTG Test Cases: Infrastructure](../../MLASTG/INFRA-Tests/0x00-Infra-Tests-Overview.md)
