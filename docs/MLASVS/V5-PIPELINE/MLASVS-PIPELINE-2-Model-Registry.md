# MLASVS-PIPELINE-2: Model Registry Security

## Category
MLASVS-PIPELINE: Pipeline & MLOps

## Overview
Model registry security ensures that stored model artifacts are protected from tampering, unauthorized access, and version confusion attacks. The model registry (MLflow, Seldon, Hugging Face Hub, etc.) is the authoritative source for deployment-ready models.

## Controls

### PIPELINE-008: Model Registry Authentication (L1)
**Description:** Model registry must require authentication for all operations.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify registry requires authentication for read and write operations
2. Check that API tokens or IAM roles are used for programmatic access
3. **Pass if:** Registry enforces authentication for all access

**Remediation:** Enable mandatory authentication. Use service accounts with minimal required permissions for CI/CD.

---

### PIPELINE-009: Deployment Approval Workflow (L1)
**Description:** Model deployments must require approval from authorized personnel.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify deployment workflow requires an approver
2. Check that promotions between environments (dev → staging → prod) require separate approval
3. **Pass if:** Deployment approvals are enforced per environment

**Remediation:** Configure mandatory approval gates at each deployment stage. Require at least one approval from a security or ML engineering lead.

---

### PIPELINE-010: Model Deployment Rollback (L1)
**Description:** Model registry must support rollback to previous model versions.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify rollback capability exists in the registry or deployment platform
2. Test rollback procedure from current to previous version
3. **Pass if:** Rollback completes successfully within defined RTO (target: < 15 minutes)

**Remediation:** Implement automated rollback with monitoring triggers. Maintain at least 3 previous versions for rapid rollback.

---

### PIPELINE-013: Immutable Model Registry (L2)
**Description:** Model registry entries should be immutable once published.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that published model versions cannot be overwritten or deleted
2. Check that modifications create new versions rather than updating existing ones
3. **Pass if:** Registry enforces immutability for published artifacts

**Remediation:** Configure registry to disallow overwrites and deletes of published models. Use version pinning for all production deployments.

---

### PIPELINE-016: Cross-tenant Isolation in ML Platforms (L2)
**Description:** Multi-tenant ML platforms must enforce tenant isolation.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that one tenant cannot access, modify, or view another tenant's model registry
2. Check that RBAC policies are scoped per tenant
3. **Pass if:** Tenant isolation is verified through penetration testing

**Remediation:** Implement namespace-based isolation, tenant-scoped RBAC, and regular isolation testing.

---

### PIPELINE-018: Feature Store Data Integrity (L2)
**Description:** Feature stores must ensure data integrity and provenance.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify feature store includes data validation on write operations
2. Check that feature definitions and transformations are version-controlled
3. **Pass if:** Feature store enforces schema validation and change tracking

**Remediation:** Implement schema-on-write validation. Store feature definitions in version control (e.g., Feast feature views in git).

---

### PIPELINE-019: Canary Deployment for Models (L2)
**Description:** New model versions should support canary/shadow deployment.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify canary deployment infrastructure exists in the serving platform
2. Check that traffic splitting (e.g., 5% → 25% → 100%) is configured
3. **Pass if:** Canary deployment is available and has been used in the last 90 days

**Remediation:** Implement canary deployment using service mesh (Istio), load balancer rules, or ML serving platform features (Seldon, KServe).

## Cross-References
- MITRE ATLAS: AML.TA0002, AML.TA0005, AML.TA0006
- NIST AI RMF: MEASURE-2, MANAGE-1
