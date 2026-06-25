# MLASTG-TEST-INFRA-001: Model Serving Security Review

## Control Reference
MLASVS-INFRA-001 (Network Segmentation), INFRA-005 (GPU Isolation), INFRA-006 (Model Cache), INFRA-007 (Inference Logging), INFRA-008 (Batch Security), INFRA-012 (Health Monitoring), INFRA-013 (Adversarial Input Detection - L2), INFRA-014 (Runtime Monitoring - L2), INFRA-015 (Automated Rollback - L2), INFRA-016 (Side-Channel Prevention - L2), INFRA-017 (Confidential Computing - L2), INFRA-018 (Drift Monitoring - L2), INFRA-019 (SIEM Integration - L2), INFRA-020 (Incident Response - L2), INFRA-022 (Hardware Attestation - L2)

## Severity
High

## Procedure

### Step 1: Network Segmentation
1. Verify model serving is on isolated network segment
2. Check that only necessary ports are exposed
3. **Pass if:** Model servers are network-isolated from general infrastructure

### Step 2: Compute Isolation
1. Verify GPU/compute resources are isolated between model replicas
2. Check for multi-tenancy risks in model serving
3. **Pass if:** Tenant isolation prevents cross-tenant data access

### Step 3: Monitoring Review (L2)
1. Verify runtime behavior monitoring is deployed
2. Check drift detection is configured for model inputs/outputs
3. **Pass if:** Monitoring detects anomalous model behavior within defined thresholds

### Step 4: Incident Response (L2)
1. Review ML-specific incident response playbook
2. Verify escalation paths are defined
3. **Pass if:** Dedicated ML IR playbook exists and is tested

## References
- NSA/CISA AI Security Deployment Guidance
