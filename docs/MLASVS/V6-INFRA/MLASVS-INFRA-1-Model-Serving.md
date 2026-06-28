# MLASVS-INFRA-1: Model Serving Security

## Category
MLASVS-INFRA: Runtime & Infrastructure

## Overview
Model serving security addresses the infrastructure that hosts ML models for inference — including Kubernetes clusters, TorchServe, TF Serving, Triton Inference Server, and custom serving solutions. Compromise of serving infrastructure can lead to model theft, data leakage, or denial of service.

## Controls

### INFRA-001: Model Serving Network Segmentation (L1)
**Description:** Model serving infrastructure must be on a separate network segment from general infrastructure.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify network ACLs restrict access to model servers to authorized clients only
2. Check that only necessary ports (model API port, health check endpoint) are exposed
3. **Pass if:** Model servers are network-isolated from general corporate infrastructure

**Remediation:** Deploy model serving in a dedicated VPC/subnet with strict ingress/egress rules. Use a WAF or API gateway as the sole entry point.

---

### INFRA-005: GPU/Compute Isolation (L1)
**Description:** GPU and compute resources must be isolated between model replicas and tenants.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify GPU memory isolation (e.g., MPS, CUDA MPS, MIG on A100)
2. Check that one model replica cannot access another replica's memory space
3. **Pass if:** Compute resources are hardware-isolated between tenants

**Remediation:** Use Multi-Instance GPU (MIG) for A100/H100, or dedicated GPU allocation per model replica. Avoid GPU time-sharing across untrusted tenants.

---

### INFRA-006: Model Cache Security (L1)
**Description:** Model inference caches must not leak data between users.
**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Review caching strategy for inference responses
2. Verify cache keys include user or session context where data isolation is required
3. **Pass if:** Cache does not serve one user's results to another user

**Remediation:** Implement tenant-aware caching with user/session context in cache keys. Disable caching for responses containing sensitive data.

---

### INFRA-007: Inference Request Logging (L1)
**Description:** All inference requests must be logged for audit and monitoring purposes.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify inference logs are collected for all API requests
2. Check that logs do not contain raw PII or sensitive data
3. **Pass if:** Inference requests are logged with anonymized identifiers

**Remediation:** Enable access logging on model serving platform. Apply log scrubbing to remove PII before persistence.

---

### INFRA-008: Batch Inference Security (L1)
**Description:** Batch inference jobs must be secured with access controls.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify batch inference jobs require authentication
2. Check that batch results are stored securely
3. **Pass if:** Batch inference is authenticated and results are access-controlled

**Remediation:** Use service accounts for batch job execution. Store batch results in access-controlled storage (S3 with IAM, etc.).

---

### INFRA-012: Model Health Monitoring (L1)
**Description:** Basic health monitoring must be implemented for model endpoints.
**MITRE ATLAS:** AML.TA0005 (Execution)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify health check endpoints exist and are active
2. Check that health checks validate actual model inference capability, not just HTTP response
3. **Pass if:** Health checks provide meaningful model availability status

**Remediation:** Implement deep health checks (e.g., test inference with known input). Configure liveness and readiness probes in Kubernetes.

---

### INFRA-013: Adversarial Input Detection at Inference (L2)
**Description:** Real-time detection of adversarial inputs during inference.
**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify adversarial input detection is deployed inline before model inference
2. Test with known adversarial patterns (FGSM, PGD samples)
3. **Pass if:** Detection identifies adversarial inputs with > 80% accuracy and < 5% false positive rate

**Remediation:** Deploy a classifier-based or statistical detection model in the inference path. Use feature squeezing as a lightweight preprocessing filter.

---

### INFRA-014: Runtime Model Behavior Monitoring (L2)
**Description:** Runtime monitoring must detect anomalous model behavior.
**MITRE ATLAS:** AML.T0018 (Manipulate AI Model)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify monitoring of: prediction distribution shifts, confidence score anomalies, latency changes
2. Check alerting for statistically significant behavioral deviations
3. **Pass if:** Runtime monitoring detects anomalous behavior within 5 minutes

**Remediation:** Implement statistical process control (SPC) on model outputs. Use drift detection libraries (Evidently AI, NannyML, WhyLabs).

---

### INFRA-015: Automated Model Rollback on Anomaly (L2)
**Description:** Automated rollback to previous model version when anomalies are detected.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify rollback automation is configured in the serving platform
2. Test rollback trigger by simulating anomaly detection
3. **Pass if:** Automatic rollback completes within defined RTO (target: < 5 minutes)

**Remediation:** Configure automated rollback triggers based on behavior monitoring alerts. Maintain the previous N model versions for rapid rollback.

---

### INFRA-016: Side-Channel Attack Prevention (L2)
**Description:** Mitigations for side-channel attacks on model inference.
**MITRE ATLAS:** AML.T0024.001 (Invert AI Model)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Review side-channel attack surface (timing, power consumption, cache behavior)
2. Verify mitigations (constant-time inference, response noise injection, cache flushing)
3. **Pass if:** Side-channel mitigations are implemented for high-security models

**Remediation:** Add controlled noise to response timing and output precision. Flush caches between requests from different tenants.

---

### INFRA-017: Confidential Computing for Inference (L2)
**Description:** Sensitive inference workloads should use confidential computing.
**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify TEE (Trusted Execution Environment) support for inference (Intel SGX/TDX, AMD SEV)
2. Check that model weights and input data are encrypted in memory during inference
3. **Pass if:** Confidential computing is available for sensitive inference workloads

**Remediation:** Deploy sensitive models on confidential computing hardware. Use attestation to verify TEE integrity before loading models.

---

### INFRA-018: Real-time Drift Monitoring (L2)
**Description:** Model drift (data distribution and concept drift) must be monitored in real-time.
**MITRE ATLAS:** AML.T0018 (Manipulate AI Model)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify drift detection is configured for model inputs (data drift) and prediction distributions (concept drift)
2. Check that significant drift triggers alerts with defined thresholds
3. **Pass if:** Drift monitoring is active with appropriate thresholds

**Remediation:** Implement drift detection using Evidently AI, NannyML, or similar. Set alert thresholds based on historical baseline variance.

---

### INFRA-019: ML-Specific SIEM Integration (L2)
**Description:** ML security events must feed into SIEM for correlation and analysis.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify ML security events (inference anomalies, access violations, drift alerts) are forwarded to SIEM
2. Check that correlation rules exist for ML-specific threat patterns
3. **Pass if:** ML events are integrated into SIEM with active correlation rules

**Remediation:** Configure structured logging for all ML events. Forward to SIEM (Splunk, ELK, Sentinel) with ML-specific dashboards and correlation rules.

---

### INFRA-020: Dedicated ML Incident Response Playbook (L2)
**Description:** Specialized incident response playbook for ML security incidents.
**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Review ML IR playbook document
2. Verify it covers: data poisoning discovered, model extracted, adversarial attack underway, supply chain compromise, model drift causing safety incidents
3. Check that the playbook is tested at least annually through tabletop exercises
4. **Pass if:** ML IR playbook exists, covers all ML-specific scenarios, and is tested

**Remediation:** Develop ML-specific incident response playbook. Conduct tabletop exercises quarterly. Integrate with existing organizational IR framework.

---

### INFRA-022: Hardware-Rooted Model Attestation (L2)
**Description:** Hardware-based attestation that verified models are running in trusted environments.
**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-INFRA-001

**Verification:**
1. Verify hardware attestation (TPM, SGX, SEV) is configured for model serving nodes
2. Check that attestation measurements are recorded and auditable
3. **Pass if:** Hardware attestation is active and measurements are verifiable

**Remediation:** Enable TPM-based attestation on serving nodes. Integrate attestation verification into the model deployment pipeline.

## Cross-References
- MITRE ATLAS: AML.TA0002, AML.TA0005, AML.TA0006, AML.TA0009, AML.TA0010, AML.T0010, AML.T0018, AML.T0056
- NSA/CISA Deploying AI Systems Securely
- NIST AI RMF: MEASURE-2, MANAGE-1
