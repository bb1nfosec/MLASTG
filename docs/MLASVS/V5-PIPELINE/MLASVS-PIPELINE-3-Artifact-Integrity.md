# MLASVS-PIPELINE-3: Artifact Integrity

## Category
MLASVS-PIPELINE: Pipeline & MLOps

## Overview
ML artifact integrity ensures that model files, datasets, feature definitions, and pipeline outputs cannot be tampered with during storage, transit, or deployment.

## Controls

### PIPELINE-002: Pipeline Artifact Signing (L1)
**Description:** All ML artifacts produced by pipelines must be cryptographically signed.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that model artifacts, container images, and evaluation reports are signed in the CI/CD pipeline
2. Check that signatures are verified before artifacts are consumed downstream
3. **Pass if:** Artifacts are signed at build time and verified at consumption time

**Remediation:** Implement signing as the final step in CI/CD (using cosign or GPG). Configure verification at model registry ingestion and deployment.

---

### PIPELINE-007: Feature Store Access Control (L1)
**Description:** Feature stores must enforce access control.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify feature store requires authentication for read/write access
2. Check that RBAC limits access based on feature sensitivity level
3. **Pass if:** Feature store enforces access control

**Remediation:** Enable authentication and configure RBAC on the feature store (Feast, Tecton, etc.). Audit access quarterly.

---

### PIPELINE-018: Feature Store Data Integrity (L2)
**Description:** Feature data integrity must be ensured with schema validation and versioning.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify feature store implements schema validation on write
2. Check that feature definitions are version-controlled and changes are tracked
3. **Pass if:** Feature store provides integrity guarantees through validation and versioning

**Remediation:** Implement schema-on-write validation (Avro, Protobuf). Store feature definitions in git and track changes via CI/CD.

## Cross-References
- MITRE ATLAS: AML.TA0002, AML.TA0005, AML.TA0006
- NIST AI RMF: MEASURE-2
