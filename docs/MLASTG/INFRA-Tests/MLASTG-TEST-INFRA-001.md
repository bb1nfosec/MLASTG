# MLASTG-TEST-INFRA-001: Model Serving Infrastructure Security Review

## Control Reference
**Controls Tested:** MLASVS-INFRA-001 (Model Serving Network Segmentation), MLASVS-INFRA-005 (GPU/Compute Isolation), MLASVS-INFRA-006 (Model Cache Security), MLASVS-INFRA-007 (Inference Request Logging), MLASVS-INFRA-008 (Batch Inference Security), MLASVS-INFRA-012 (Model Health Monitoring), MLASVS-INFRA-013 (Adversarial Input Detection at Inference — L2), MLASVS-INFRA-014 (Runtime Model Behavior Monitoring — L2), MLASVS-INFRA-015 (Automated Model Rollback on Anomaly — L2), MLASVS-INFRA-016 (Side-Channel Attack Prevention — L2), MLASVS-INFRA-017 (Confidential Computing for Inference — L2), MLASVS-INFRA-018 (Real-time Drift Monitoring — L2), MLASVS-INFRA-019 (ML-Specific SIEM Integration — L2), MLASVS-INFRA-020 (Dedicated ML Incident Response Playbook — L2), MLASVS-INFRA-022 (Hardware-Rooted Model Attestation — L2)

## Severity (L1/L2)
**High** (L1) / **Critical** (L2)

## Overview
Model serving infrastructure is the external-facing component most exposed to adversarial interactions. Weaknesses in network isolation, compute tenancy, logging, and runtime monitoring can enable model extraction, adversarial evasion at scale, and denial-of-service attacks. This test reviews the security architecture and operational controls of the model serving layer.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `nmap`, `kubectl`, cloud provider security console, SIEM access |
| Access | Infrastructure architecture diagrams; serving platform configuration (Kubernetes, TorchServe, Triton, BentoML, etc.) |
| Documentation | Network architecture diagram; incident response playbook |

## Step-by-Step Procedure

### Step 1: Network Segmentation Verification
1. Obtain the network architecture diagram for the model serving environment
2. Verify that model serving nodes are on an isolated network segment (VPC, subnet, or namespace) separate from general application infrastructure
3. Verify that only the required ports are exposed (typically: inference API port, health check port)
4. Scan for unexpected open ports:
   ```bash
   nmap -sV -p- <model-serving-host>
   ```
5. **Pass if:** Model servers are network-isolated; only required ports are open; unexpected ports are not exposed
6. **Fail if:** Model servers share a flat network with general infrastructure, or unnecessary ports are open

### Step 2: Compute and GPU Isolation
1. Verify GPU/compute resources are isolated between model replicas and, if applicable, between tenants
2. Review Kubernetes namespace isolation, resource quotas, and Pod Security Standards
3. Verify that no multi-tenant model serving configuration allows cross-tenant data access via shared GPU memory
4. **Pass if:** Tenant isolation is enforced at the compute level; shared GPU memory access across tenants is prevented
5. **Fail if:** Multiple tenants share GPU resources without isolation controls

### Step 3: Inference Request Logging
1. Verify that inference requests are logged with the following minimum fields:
   - Timestamp (UTC)
   - Request identifier
   - API key or user identifier (anonymized or hashed)
   - Model name and version
   - Input shape (not raw input data unless required and privacy-reviewed)
   - Output label or class (not full probability vector)
   - Response latency
2. Verify that logs are shipped to a centralized log store and retained per the data retention policy
3. **Pass if:** All required log fields are captured and retained
4. **Fail if:** Logging is absent, incomplete, or logs are stored only locally on the serving node

### Step 4: Model Health Monitoring
1. Verify that active health monitoring is deployed for all production model endpoints
2. Verify that the following metrics are monitored with defined alert thresholds:
   - Request latency (p50, p95, p99)
   - Error rate (4xx, 5xx responses)
   - Model prediction distribution (output class distribution monitoring)
   - GPU/CPU utilization
3. **Pass if:** All required metrics are monitored with documented alert thresholds

### Step 5: Adversarial Input Detection at Inference (L2)
1. Verify that an adversarial input detector is deployed in the serving pipeline
2. Deploy a test input known to be adversarial (e.g., from TEST-MODEL-001 results):
   ```python
   # Send adversarial example to serving endpoint and verify detection
   response = requests.post(
       f"{serving_url}/predict",
       json={"input": adversarial_sample.tolist()},
       headers={"Authorization": f"Bearer {api_key}"}
   )
   assert response.json().get("flagged") == True, "Adversarial input not detected!"
   ```
3. **Pass if:** Known adversarial inputs are flagged by the runtime detector with > 80% detection rate and < 5% false positive rate

### Step 6: Real-Time Drift Monitoring (L2)
1. Verify that data drift monitoring is configured for model inputs
2. Verify that concept drift monitoring is configured for model output distributions
3. Inject synthetic drift (shift input distribution by 2+ standard deviations) and verify detection:
   - Detection should trigger an alert within the documented SLA (recommend: < 15 minutes)
4. **Pass if:** Drift monitoring detects significant distribution shifts within the documented SLA

### Step 7: ML Incident Response Playbook Review (L2)
1. Locate the ML-specific incident response playbook
2. Verify the playbook covers the following ML-specific scenarios:
   - Training data poisoning detected post-deployment
   - Model extraction attack in progress (anomalous query volume)
   - Adversarial attack campaign (model evasion at scale)
   - Supply chain compromise (compromised base model discovered)
3. Verify the playbook includes escalation paths, containment actions, and rollback procedures
4. **Pass if:** A dedicated ML IR playbook exists, covers all required scenarios, and has been tested in the last 6 months

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Model servers are network-isolated; compute isolation verified; inference logging complete; health monitoring active |
| L2 | Adversarial input detection > 80%; drift monitoring with alert SLA; ML IR playbook tested within 6 months; SIEM integration active |

## Evidence Requirements

- [ ] Network architecture diagram showing model serving isolation
- [ ] Port scan results (no unexpected open ports)
- [ ] Compute isolation configuration (Kubernetes PSS, resource quotas)
- [ ] Inference log sample showing required fields
- [ ] Health monitoring configuration and alert threshold documentation
- [ ] (L2) Adversarial input detection test results
- [ ] (L2) Drift monitoring configuration and synthetic drift test results
- [ ] (L2) ML incident response playbook with last test date
- [ ] (L2) SIEM integration evidence

## Remediation Guidance

**If network isolation is insufficient:**
1. Move model serving to a dedicated subnet or Kubernetes namespace with network policies
2. Implement egress filtering to prevent model servers from making unauthorized outbound connections
3. Use a service mesh (Istio, Linkerd) for mTLS between internal services

**If logging is incomplete:**
1. Add structured logging middleware to the serving framework
2. Define a logging schema and enforce it via schema validation at log ingestion
3. Set up log forwarding to a centralized SIEM

**If no IR playbook exists:**
1. Develop an ML-specific IR playbook based on the scenarios listed above
2. Conduct a tabletop exercise within 30 days of playbook creation
3. Review and update the playbook after any actual ML security incident

## References
- **MITRE ATLAS:**
  - `AML.T0024.002` — ML Inference API Access (serving attack surface)
  - `AML.T0040` — ML Service Disruption
- **MLASWE:** MLASWE-0012 (Insufficient Runtime Monitoring), MLASWE-0013 (Missing ML Incident Response)
- **NIST AI RMF:** MANAGE 1.3 (Incident response), MEASURE 2.6 (Runtime monitoring)
- **Reference:** NSA/CISA AI Security Deployment Guidance (2024)
