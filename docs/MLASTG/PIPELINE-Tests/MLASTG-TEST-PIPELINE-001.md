# MLASTG-TEST-PIPELINE-001: ML Pipeline & CI/CD Security Audit

## Control Reference
**Controls Tested:** MLASVS-PIPELINE-001 (ML Pipeline Access Control), MLASVS-PIPELINE-002 (Pipeline Artifact Signing), MLASVS-PIPELINE-003 (Experiment Tracking Access Control), MLASVS-PIPELINE-004 (Training Environment Isolation), MLASVS-PIPELINE-005 (Pipeline Secret Management), MLASVS-PIPELINE-006 (Run History Audit Logging), MLASVS-PIPELINE-007 (Feature Store Access Control), MLASVS-PIPELINE-008 (Model Registry Authentication), MLASVS-PIPELINE-009 (Deployment Approval Workflow), MLASVS-PIPELINE-010 (Model Deployment Rollback — L1), MLASVS-PIPELINE-011 (Pipeline Integrity Monitoring — L2), MLASVS-PIPELINE-012 (Automated Pipeline Security Scanning — L2), MLASVS-PIPELINE-013 (Immutable Model Registry — L2), MLASVS-PIPELINE-014 (Reproducible Training Verification — L2), MLASVS-PIPELINE-019 (Canary Deployment for Models — L2), MLASVS-PIPELINE-020 (Automated Testing Gate in CI/CD — L2)

## Severity
**Medium** (L1) / **High** (L2)

## Overview
ML pipelines introduce a complex attack surface spanning training code, data preprocessing, experiment tracking, model registries, and deployment automation. A compromise at any stage can result in a backdoored model reaching production. This test audits the security posture of the full ML pipeline from data ingestion to model deployment.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | MLflow, Kubeflow, or equivalent MLOps platform access; git history access |
| Access | CI/CD pipeline configuration (GitHub Actions, GitLab CI, Jenkins, etc.); MLOps platform admin or auditor role |
| Documentation | Pipeline architecture diagram; deployment approval workflow documentation |

## Step-by-Step Procedure

### Step 1: Access Control Review
1. Verify that the MLOps platform (MLflow, Kubeflow, SageMaker, etc.) requires authentication for all user and API access
2. Verify that role-based access control (RBAC) is configured:
   - Data scientists: can submit training runs; cannot promote models to production
   - ML engineers: can manage pipelines; cannot modify production model serving
   - Admins: full access; restricted to a small group with MFA enforced
3. Review access logs for any unauthorized access attempts in the last 30 days
4. **Pass if:** All pipeline components enforce authentication; RBAC is configured with least-privilege roles
5. **Fail if:** Any pipeline component allows unauthenticated access, or roles are overly permissive

### Step 2: Pipeline Artifact Integrity
1. Verify that model artifacts are cryptographically signed as part of the CI/CD pipeline
2. Verify that signatures are verified at each deployment gate (staging → production)
3. Attempt to deploy an unsigned model artifact and verify it is rejected
4. **Pass if:** Models are signed at build time and signature verification is enforced at every deployment gate
5. **Fail if:** Models can be deployed without signing, or signatures are not verified

### Step 3: Secret Management Review
1. Audit all pipeline configuration files, environment variable definitions, and pipeline code for hardcoded secrets:
   ```bash
   # Scan for common secret patterns in the repository
   git log --all -p | grep -E '(api_key|password|token|secret)\s*=' | head -50
   # Or use a dedicated tool:
   trufflehog git file://./  --only-verified
   ```
2. Verify that all secrets (API keys, database passwords, cloud credentials) are stored in a dedicated secrets manager (HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager)
3. **Pass if:** No secrets are hardcoded in code or configuration files; all secrets retrieved from secrets manager at runtime
4. **Fail if:** Any API key, password, or token is found hardcoded in pipeline code or configuration

### Step 4: Deployment Approval Workflow
1. Review the model deployment process for human-in-the-loop controls
2. Verify that promotion from staging to production requires explicit human approval (not just automated test pass)
3. Verify that production deployments require a different approver than the submitter (four-eyes principle)
4. Check that the approval process is logged with timestamp, approver identity, and model version
5. **Pass if:** Production deployments require documented human approval with logged evidence
6. **Fail if:** Any automated pathway exists from staging to production without human approval

### Step 5: Run History and Audit Logging
1. Review the experiment tracking system for audit log completeness
2. Verify logs capture: who ran each experiment, what parameters were used, what data was used, what model was produced, and when
3. **Pass if:** Full audit trail exists for all training runs traceable to a human initiator

### Step 6: Model Rollback Capability
1. Identify the last three production model versions in the model registry
2. Execute a rollback to the previous model version in a staging environment
3. Measure rollback completion time
4. **Pass if:** Rollback completes successfully within the documented Recovery Time Objective (RTO)
5. **Fail if:** Rollback fails, or no rollback procedure exists

### Step 7: Automated Security Testing Gate in CI/CD (L2)
1. Review the CI/CD pipeline configuration for automated ML security testing steps
2. Verify that the pipeline includes:
   - Model file scanning (ModelScan or equivalent)
   - Dependency vulnerability scanning (Trivy or equivalent)
   - SBOM generation
   - Adversarial robustness test execution
3. Verify that pipeline fails if any security gate fails
4. **Pass if:** Automated security tests are configured as blocking gates in the CI/CD pipeline

### Step 8: Canary Deployment Verification (L2)
1. Verify that model updates are deployed using a canary or blue/green strategy
2. Verify that the canary traffic split is configurable and monitored
3. Verify that automatic rollback is triggered if model performance degrades during canary phase
4. **Pass if:** Canary deployment is configured with automatic rollback on performance regression

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | All pipeline components enforce authentication and RBAC; no hardcoded secrets; artifacts signed; human approval for production deployments; rollback tested |
| L2 | Automated security testing gates in CI/CD; immutable model registry; canary deployment with automatic rollback; pipeline integrity monitoring active |

## Evidence Requirements

- [ ] MLOps platform RBAC configuration screenshots or export
- [ ] Artifact signing and verification evidence (pipeline config + test of unsigned rejection)
- [ ] Secret management audit results (no hardcoded secrets found)
- [ ] Deployment approval workflow documentation and example approval log
- [ ] Experiment tracking audit log sample
- [ ] Rollback test results with completion time
- [ ] (L2) CI/CD security gate configuration evidence
- [ ] (L2) Canary deployment configuration and rollback trigger evidence

## Remediation Guidance

**If hardcoded secrets are found:**
1. Rotate all exposed credentials immediately
2. Remove hardcoded secrets from code and git history (`git filter-branch` or BFG Repo Cleaner)
3. Integrate a secrets manager and update all secret references
4. Add a pre-commit hook to scan for secret patterns before commits

**If no deployment approval workflow exists:**
1. Implement branch protection rules requiring review before production merge
2. Add a manual approval gate in the CI/CD pipeline before production deployment jobs
3. Document the approval workflow in the ML security policy

**If artifact signing is absent:**
1. Integrate Sigstore or GPG signing into the CI/CD pipeline post-training step
2. Add signature verification as a pre-deployment check

## References
- **MITRE ATLAS:**
  - `AML.T0010` — ML Pipeline Compromise (supply chain context)
  - `AML.TA0004` — Persistence (compromised pipeline context)
- **MLASWE:** MLASWE-0008 (Insecure MLOps Pipeline), MLASWE-0009 (Insufficient ML-SBOM)
- **NIST AI RMF:** GOVERN 1.2 (Policies and processes), MAP 1.5 (Risk identification)
- **Related Standard:** SLSA (Supply chain Levels for Software Artifacts)
