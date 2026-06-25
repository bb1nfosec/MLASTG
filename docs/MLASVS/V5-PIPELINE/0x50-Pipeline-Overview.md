# V5: Pipeline & MLOps Security — MLASVS-PIPELINE

## Overview

ML pipelines — including CI/CD, feature stores, model registries, and experiment tracking — are critical infrastructure that must be secured. Compromise at any point in the pipeline can lead to poisoned models, data leakage, or deployment of unverified artifacts.

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| CI/CD pipeline compromise | AML.TA0002 | — |
| Model registry tampering | AML.TA0006 | MLASWE-0007 |
| Feature store poisoning | AML.T0020 | MLASWE-0002 |
| Experiment tracking data leakage | AML.TA0010 | MLASWE-0012 |
| Artifact integrity failure | AML.TA0006 | — |

## Subcategories

### PIPELINE-1: CI/CD Security (Controls PIPELINE-001 through PIPELINE-007)
Security of the ML CI/CD pipeline.

### PIPELINE-2: Model Registry (Controls PIPELINE-008 through PIPELINE-013)
Security of model storage, versioning, and deployment registry.

### PIPELINE-3: Artifact Integrity (Controls PIPELINE-014 through PIPELINE-020)
Ensuring ML artifacts are untampered from build to deployment.

## Control Inventory

### L1 Controls (10)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| PIPELINE-001 | ML pipeline access control | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-002 | Pipeline artifact signing | AML.TA0006 | TEST-PIPELINE-001 |
| PIPELINE-003 | Experiment tracking access control | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-004 | Training environment isolation | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-005 | Pipeline secret management | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-006 | Run history audit logging | AML.TA0009 | TEST-PIPELINE-001 |
| PIPELINE-007 | Feature store access control | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-008 | Model registry authentication | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-009 | Deployment approval workflow | AML.TA0006 | TEST-PIPELINE-001 |
| PIPELINE-010 | Model deployment rollback | AML.TA0006 | TEST-PIPELINE-001 |

### L2 Controls (10)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| PIPELINE-011 | Pipeline integrity monitoring | AML.TA0005 | TEST-PIPELINE-001 |
| PIPELINE-012 | Automated pipeline security scanning | AML.TA0005 | TEST-PIPELINE-001 |
| PIPELINE-013 | Immutable model registry | AML.TA0006 | TEST-PIPELINE-001 |
| PIPELINE-014 | Reproducible training verification | AML.TA0005 | TEST-PIPELINE-001 |
| PIPELINE-015 | Data leakage prevention in pipeline | AML.TA0010 | TEST-PIPELINE-001 |
| PIPELINE-016 | Cross-tenant isolation in ML platforms | AML.TA0002 | TEST-PIPELINE-001 |
| PIPELINE-017 | Pipeline compliance attestation | AML.TA0009 | TEST-PIPELINE-001 |
| PIPELINE-018 | Feature store data integrity | AML.TA0005 | TEST-PIPELINE-001 |
| PIPELINE-019 | Canary deployment for models | AML.TA0006 | TEST-PIPELINE-001 |
| PIPELINE-020 | Automated testing gate in CI/CD | AML.TA0005 | TEST-PIPELINE-001 |

## Related Links

- [MLASTG Test Cases: Pipeline](../../MLASTG/PIPELINE-Tests/0x00-Pipeline-Tests-Overview.md)
