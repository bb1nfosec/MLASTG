# MLASTG-TEST-PIPELINE-001: CI/CD & Pipeline Security Audit

## Control Reference
MLASVS-PIPELINE-001 through 020 (all pipeline controls)

## Severity
Medium

## Procedure

### Step 1: Access Control Review
1. Verify MLOps platform (MLflow, Kubeflow, etc.) has authentication enabled
2. Verify role-based access control (RBAC) is configured
3. **Pass if:** All ML pipeline components enforce authentication and authorization

### Step 2: Artifact Integrity
1. Verify model artifacts are signed in CI/CD pipeline
2. Check that signatures are verified before deployment
3. **Pass if:** Models are signed and verified at each deployment gate

### Step 3: Secret Management
1. Review how API keys, credentials, and tokens are stored
2. Verify secrets are not hardcoded in pipeline code
3. **Pass if:** Secrets use dedicated secret management (Vault, secrets manager)

### Step 4: Deployment Workflow
1. Verify deployment requires approval (human-in-the-loop)
2. Check that production deploys require separate approval from staging
3. **Pass if:** Deployments have documented approval workflows

### Step 5: Rollback Capability (L2)
1. Verify model rollback is tested and documented
2. Test rollback to previous model version
3. **Pass if:** Rollback completes successfully within defined RTO

## References
- NIST AI RMF: MAP, MEASURE
