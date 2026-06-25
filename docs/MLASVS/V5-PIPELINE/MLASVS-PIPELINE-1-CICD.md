# MLASVS-PIPELINE-1: CI/CD Pipeline Security

## Category
MLASVS-PIPELINE: Pipeline & MLOps

## Overview
CI/CD pipeline security for ML systems ensures that training, evaluation, and deployment pipelines are protected from unauthorized access, tampering, and misconfiguration.

## Controls

### PIPELINE-001: ML Pipeline Access Control (L1)
**Description:** Access to ML pipelines must be authenticated and authorized.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify pipeline platform (GitHub Actions, GitLab CI, Jenkins) has authentication enforced
2. Check RBAC is configured per pipeline/resource
3. **Pass if:** Pipelines require authentication with role-based access

**Remediation:** Enable mandatory authentication on the CI/CD platform. Configure RBAC to restrict pipeline modification to authorized teams.

---

### PIPELINE-002: Pipeline Artifact Signing (L1)
**Description:** All ML artifacts produced by pipelines must be signed.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that model artifacts, container images, and reports are signed
2. Check that signatures are verified before downstream use
3. **Pass if:** Artifacts are signed and verified

**Remediation:** Implement artifact signing in CI/CD using cosign, GPG, or sigstore. Automate signature verification at each consumption point.

---

### PIPELINE-003: Experiment Tracking Access Control (L1)
**Description:** Experiment tracking systems must enforce access control.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify experiment tracking platform has authentication enabled
2. Check that RBAC is configured for experiments
3. **Pass if:** Experiment access is controlled

**Remediation:** Enable authentication on experiment tracking (MLflow, W&B, etc.). Configure team-based access policies.

---

### PIPELINE-004: Training Environment Isolation (L1)
**Description:** Training environments must be isolated from other systems.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify training runs in isolated compute (separate namespace, VPC, or cluster)
2. Check that training environments cannot access production data without explicit authorization
3. **Pass if:** Training environments are isolated

**Remediation:** Use dedicated Kubernetes namespaces, VPCs, or compute clusters for training workloads. Apply network policies to restrict egress.

---

### PIPELINE-005: Pipeline Secret Management (L1)
**Description:** Secrets used in ML pipelines must be managed securely.
**MITRE ATLAS:** AML.TA0002 (Credential Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify secrets are stored in dedicated secret management (Vault, AWS Secrets Manager, GitHub Secrets)
2. Check that secrets are not hardcoded in pipeline YAML or code
3. **Pass if:** Secrets are managed through dedicated secret store

**Remediation:** Migrate all secrets to a dedicated secrets manager. Enforce secret scanning in pre-commit hooks.

---

### PIPELINE-006: Run History Audit Logging (L1)
**Description:** All pipeline runs must be logged with immutable audit trails.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify pipeline run history is retained
2. Check that logs include: who ran, what changed, when, approval status
3. **Pass if:** Complete audit trail exists for all pipeline runs

**Remediation:** Configure pipeline platform to retain run history indefinitely. Export logs to SIEM for centralized auditing.

---

### PIPELINE-007: Feature Store Access Control (L1)
**Description:** Feature stores must enforce access control.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify feature store authentication
2. Check that RBAC limits access based on data sensitivity
3. **Pass if:** Feature store enforces access control

**Remediation:** Enable authentication and authorization on the feature store platform (Feast, Tecton, etc.). Configure least-privilege access policies.

---

### PIPELINE-008: Model Registry Authentication (L1)
**Description:** Model registry must require authentication.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify registry requires authentication for all operations
2. Check that API tokens or IAM roles are used
3. **Pass if:** Registry enforces authentication

**Remediation:** Enable authentication on model registry. Use API tokens with limited scope for CI/CD integration.

---

### PIPELINE-009: Deployment Approval Workflow (L1)
**Description:** Model deployments must require approval.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify deployment workflow requires approver
2. Check that promotions between environments require separate approval
3. **Pass if:** Deployment approvals are enforced

**Remediation:** Configure manual approval gates between staging and production. Require separate approvers for each environment promotion.

---

### PIPELINE-010: Model Deployment Rollback (L1)
**Description:** Registry must support rollback to previous model versions.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify rollback capability exists
2. Test rollback procedure
3. **Pass if:** Rollback completes successfully within defined RTO

**Remediation:** Implement automated rollback with canary deployment. Document rollback procedure and test quarterly.

---

### PIPELINE-011: Pipeline Integrity Monitoring (L2)
**Description:** Pipeline configurations must be monitored for unauthorized changes.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify monitoring for pipeline YAML/config changes
2. Check alerting for unauthorized changes
3. **Pass if:** Pipeline integrity monitoring is active

**Remediation:** Enable change monitoring on pipeline configuration files. Use branch protection and signed commits.

---

### PIPELINE-012: Automated Pipeline Security Scanning (L2)
**Description:** Pipelines must include automated security scanning steps.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify SAST/SCA scanning is integrated into pipeline
2. Check that model scanning is included
3. **Pass if:** Security scanning is automated in pipeline

**Remediation:** Integrate Trivy/Snyk for dependency scanning, ModelScan for model file scanning, and bandit for Python code scanning.

---

### PIPELINE-013: Immutable Model Registry (L2)
**Description:** Model registry entries should be immutable once published.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that model versions cannot be overwritten or deleted
2. Check that changes create new versions
3. **Pass if:** Registry enforces immutability

**Remediation:** Configure model registry to prevent overwrites. Implement version pinning for all production deployments.

---

### PIPELINE-014: Reproducible Training Verification (L2)
**Description:** Pipeline must support reproducible training with deterministic results.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify pipeline tracks: random seeds, data versions, code commits, hyperparameters
2. Test reproducibility by running training twice
3. **Pass if:** Training produces identical results given same inputs

**Remediation:** Use deterministic algorithms, lock random seeds, version-control data, and containerize training environments.

---

### PIPELINE-015: Data Leakage Prevention in Pipeline (L2)
**Description:** Pipelines must prevent data leakage between stages and environments.
**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Review data flow between pipeline stages
2. Check that training data is properly isolated from test/eval data
3. **Pass if:** No data leakage paths exist in pipeline

**Remediation:** Implement data isolation at the storage layer. Use separate buckets/directories for train, test, and eval splits.

---

### PIPELINE-016: Cross-tenant Isolation in ML Platforms (L2)
**Description:** Multi-tenant ML platforms must enforce tenant isolation.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify tenant isolation for model registries
2. Check that one tenant cannot access another's models
3. **Pass if:** Tenant isolation is verified

**Remediation:** Use namespace isolation, RBAC, and network policies to enforce tenant boundaries.

---

### PIPELINE-017: Pipeline Compliance Attestation (L2)
**Description:** Pipelines must produce compliance attestation artifacts.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify pipeline generates compliance reports (SBOM, provenance, audit log)
2. Check that attestations are stored with model artifacts
3. **Pass if:** Compliance attestation artifacts are generated

**Remediation:** Add pipeline steps to generate SBOM, provenance, and compliance reports. Store alongside model artifacts in registry.

---

### PIPELINE-018: Feature Store Data Integrity (L2)
**Description:** Feature stores must ensure data integrity and provenance.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify feature store has data validation on write
2. Check that feature transformations are version-controlled
3. **Pass if:** Feature store ensures data integrity

**Remediation:** Implement schema validation on feature writes. Version-control feature definitions (e.g., using Feast's `feature_store.yaml` in git).

---

### PIPELINE-019: Canary Deployment for Models (L2)
**Description:** New model versions should support canary/shadow deployment.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify canary deployment infrastructure exists
2. Check that traffic splitting is configured
3. **Pass if:** Canary deployment is available

**Remediation:** Implement canary deployment using service mesh (Istio) or load balancer traffic splitting.

---

### PIPELINE-020: Automated Testing Gate in CI/CD (L2)
**Description:** Security tests must gate deployments in CI/CD.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-PIPELINE-001

**Verification:**
1. Verify that adversarial robustness tests are required for deployment
2. Check that failed security tests block deployment
3. **Pass if:** Security tests act as gating criteria

**Remediation:** Integrate MLASTG test scripts into CI/CD pipeline. Configure pipeline to block deployment if any security test fails.

## Cross-References
- MITRE ATLAS: AML.TA0002, AML.TA0005, AML.TA0006, AML.TA0009, AML.TA0010
- NIST AI RMF: MAP-2, MEASURE-2, MANAGE-1
- MLSecOps best practices
