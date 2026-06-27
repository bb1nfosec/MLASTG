# MLASTG-TEST-INFRA-004: Confidential Computing & TEE-Based Model Inference Security

## Control Reference
**Controls Tested:** MLASVS-INFRA-017 (Confidential Computing for Inference — L2), MLASVS-INFRA-022 (Hardware-Rooted Model Attestation — L2), MLASVS-INFRA-016 (Side-Channel Attack Prevention — L2), MLASVS-INFRA-005 (GPU/Compute Isolation), MLASVS-PIPELINE-003 (Artifact Integrity Verification), MLASVS-MODEL-005 (Model Integrity Verification)

## Severity (L1/L2)
**High** (L1) / **Critical** (L2)

## Overview
Confidential computing uses hardware-based Trusted Execution Environments (TEEs) to protect model weights, training data, and inference inputs/outputs from unauthorized access — including access by cloud providers, co-tenants, or privileged system administrators. Technologies include Intel SGX/TDX, AMD SEV-SNP, and ARM CCA. This test verifies that TEE-based inference deployments correctly isolate workloads, validate attestation, protect against side-channel leakage, and maintain model integrity throughout the inference lifecycle.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `dcap-quoting-provider`, `sgx_tool`, `az-dcap-client`, or vendor-specific attestation CLI; `perf` / `cachegrind` for side-channel analysis; Python 3 with `statistics` (stdlib); cloud provider TEE console |
| Access | TEE-enabled compute instances (Intel SGX/TDX, AMD SEV-SNP); attestation service configuration; model serving deployment configuration |
| Documentation | TEE deployment architecture; attestation verification policy; threat model for confidentiality requirements |
| Hardware | Confidential computing instances (e.g., AWS Nitro Enclaves, Azure Confidential Computing, GCP Confidential VMs, Equinix Metal with SGX) |

## Step-by-Step Procedure

### Step 1: TEE Environment Verification
1. Verify that the model serving infrastructure is deployed on TEE-capable hardware:
   ```bash
   # Intel SGX
   sgx_tool enclave_info
   
   # AMD SEV-SNP
   dmesg | grep -i "SEV\|SEV-SNP"
   
   # Check cloud provider metadata
   curl -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/attributes/confidential-computing 2>/dev/null
   ```
2. Verify that the TEE is enabled and active (not just available):
   ```bash
   # Intel TDX
   dmesg | grep -i "TDX\|Trust Domain"
   
   # AMD SEV-SNP
   cat /sys/kernel/debug/sev/snp_enabled
   ```
3. **Pass if:** Model serving runs on TEE-capable hardware with TEE enabled
4. **Fail if:** TEE is available but not enabled, or model serving runs on standard (non-confidential) hardware

### Step 2: Attestation Verification
1. Verify that remote attestation is configured and validated before model loading:
   - The attestation report should include: TEE type, security version, measurement of the enclave/VM code, and platform configuration
   - Attestation should be verified against a trusted attestation service (Intel DCAP, Azure Attestation, AMD KDS)
2. Test attestation bypass scenarios:
   ```bash
   # Attempt to load a model without attestation verification
   # (This should fail in a properly configured system)
   curl -X POST https://model-server/v1/load-model \
     -H "Content-Type: application/json" \
     -d '{"model_path": "s3://models/production.pt", "skip_attestation": true}'
   ```
3. Verify that attestation measurements match expected values (the code measurement should correspond to the known-good model serving binary):
   ```bash
   # Verify attestation report measurement
   sgx_tool verify --report attestation_report.bin \
     --expected_mrenclave <known_good_hash> \
     --expected_mrsigner <known_signer_hash>
   ```
4. **Pass if:** Attestation is mandatory before model loading; bypass attempts are rejected; measurements match expected values
5. **Fail if:** Attestation can be skipped, is not enforced, or measurements are not verified

### Step 3: Model Weight Confidentiality Verification
1. Verify that model weights are encrypted at rest within the TEE memory:
   - Confirm that decryption keys are sealed to the TEE (not accessible outside the enclave)
   - Verify that model weights cannot be read from the host OS or hypervisor
2. Test memory access from outside the TEE:
   ```bash
   # Attempt to read TEE memory from host (should fail or return garbage)
   sudo dd if=/dev/mem bs=1 count=1024 skip=<tee_memory_offset> 2>/dev/null | xxd | head -5
   ```
3. Verify that model weights are not written to disk in plaintext during checkpointing or caching:
   ```bash
   # Check for plaintext model artifacts on disk
   find /tmp -name "*.pt" -o -name "*.pth" -o -name "*.onnx" 2>/dev/null | \
     xargs -I{} sh -c 'echo "=== {} ===" && file {} && strings {} | head -3'
   ```
4. **Pass if:** Model weights are encrypted in TEE memory; host cannot access plaintext weights; no plaintext artifacts on disk
5. **Fail if:** Model weights are accessible from outside the TEE, or plaintext artifacts exist on disk

### Step 4: Input/Output Isolation Verification
1. Verify that inference inputs are encrypted in transit to the TEE:
   ```bash
   # Verify TLS termination happens inside the TEE (not at a proxy)
   openssl s_client -connect model-server:443 -brief 2>&1 | grep -i "TLS\|protocol"
   ```
2. Verify that inference outputs are encrypted before leaving the TEE boundary
3. Test cross-tenant data isolation within the TEE:
   - Submit concurrent requests from different "tenants" (simulated with different API keys)
   - Verify that one tenant's data cannot leak to another tenant's inference context
4. **Pass if:** Inputs and outputs are encrypted at TEE boundaries; cross-tenant isolation is maintained
5. **Fail if:** Inputs/outputs are transmitted in plaintext, or cross-tenant data leakage is possible

### Step 5: Side-Channel Resistance Assessment (L2)
1. Analyze the TEE deployment for known side-channel attack vectors:
   - **Cache-timing attacks:** Monitor cache access patterns during inference to detect potential cache-based information leakage
   - **Power analysis:** If physical access is available, monitor power consumption during inference
   - **Branch prediction:** Verify that branch prediction patterns do not leak model structure information
   - **Memory access patterns:** Verify that memory access patterns are constant-time or obfuscated
2. Perform a cache-timing measurement:```python
import time
import statistics

def measure_cache_timing(fn, iterations=10000):
    """Measure timing variance that could indicate cache side-channel leakage."""
    times = []
    for _ in range(iterations):
        start = time.perf_counter_ns()
        fn()
        end = time.perf_counter_ns()
        times.append(end - start)
    mean_t = statistics.mean(times)
    stdev_t = statistics.stdev(times) if len(times) > 1 else 0
    coefficient_of_variation = stdev_t / mean_t if mean_t > 0 else 0
    return {
        "mean_ns": mean_t,
        "std_ns": stdev_t,
        "cv": coefficient_of_variation,
        "suspicious": coefficient_of_variation > 0.15  # High variance may indicate cache effects
    }

result = measure_cache_timing(lambda: model_server.predict(test_input))
print(f"Timing CV: {result['cv']:.4f} — {'⚠️ Investigate' if result['suspicious'] else '✅ Acceptable'}")
```
3. **Pass if:** Cache-timing coefficient of variation is below 0.15; no obvious side-channel leakage vectors identified
4. **Fail if:** High timing variance suggests cache-based leakage, or known side-channel mitigations are absent

### Step 6: Attestation Logging and Audit Trail
1. Verify that all attestation events are logged with:
   - Timestamp (UTC)
   - Attestation report hash
   - Verification result (pass/fail)
   - TEE type and security version
   - Model hash loaded (post-attestation)
2. Verify that attestation logs are sent to a centralized, tamper-evident log store (SIEM, immutable audit log)
3. Verify that failed attestation attempts trigger alerts:
   ```bash
   # Simulate a failed attestation and verify alert
   # (This requires coordination with the security team)
   # Check SIEM for recent attestation failure alerts
   ```
4. **Pass if:** Attestation events are logged, sent to SIEM, and failed attempts trigger alerts
5. **Fail if:** Attestation is not logged, logs are stored locally only, or failed attempts are silent

### Step 7: TEE Lifecycle and Update Security (L2)
1. Verify that TEE firmware and microcode are updated to address known vulnerabilities:
   ```bash
   # Intel SGX
   dmesg | grep -i "microcode\|ucode"
   cat /proc/cpuinfo | grep "microcode"
   
   # AMD SEV
   dmesg | grep -i "SEV firmware"
   ```
2. Verify that the attestation policy includes minimum TEE security version requirements (reject old/vulnerable TEE versions)
3. Verify that model updates within the TEE are validated:
   - New model versions must pass attestation before deployment
   - Model rollback to a known-vulnerable version should be prevented
4. **Pass if:** TEE firmware is current; attestation policy enforces minimum versions; model updates are validated
5. **Fail if:** TEE firmware is outdated, or model updates bypass attestation

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Model serving on TEE-capable hardware; attestation enforced before model loading; model weights encrypted in TEE memory; input/output isolation verified |
| L2 | All L1 controls met; side-channel resistance assessed; attestation audit trail with SIEM integration; TEE firmware current; model update validation enforced |

## Evidence Requirements

- [ ] TEE hardware verification output (SGX/SEV/TDX enabled)
- [ ] Attestation verification logs (bypass attempt results, measurement verification)
- [ ] Model weight confidentiality test results (memory access, disk scan)
- [ ] Input/output encryption verification (TLS termination analysis)
- [ ] (L2) Side-channel timing analysis results
- [ ] (L2) Attestation audit trail sample from SIEM
- [ ] (L2) TEE firmware version and microcode verification
- [ ] (L2) Model update validation test results

## Remediation Guidance

**If TEE is not enabled:**
1. Migrate model serving to confidential computing instances (AWS Nitro Enclaves, Azure Confidential Computing, or GCP Confidential VMs)
2. Enable TEE in the compute instance configuration
3. Re-deploy the model serving stack within the TEE boundary

**If attestation is not enforced:**
1. Integrate remote attestation into the model loading pipeline (Intel DCAP or vendor-specific SDK)
2. Configure attestation service with known-good measurement values
3. Reject model loading if attestation verification fails

**If side-channel leakage is detected:**
1. Implement constant-time inference operations where possible
2. Add controlled noise to timing responses
3. Isolate TEE workloads from shared cache hierarchies (use cache partitioning)
4. Consider hardware-level mitigations (Intel CAT, cache line flushing)

**If attestation logging is absent:**
1. Instrument the attestation flow with structured logging
2. Forward attestation events to SIEM with dedicated dashboards
3. Create alerts for attestation failures with severity based on context

## References
- **MITRE ATLAS:**
  - `AML.T0056` — ML Model Behavioral Manipulation (integrity verification context)
  - `AML.T0012` — Backdoor ML Model (TEE-based integrity enforcement)
- **MLASWE:** MLASWE-0003 (Model Extraction — TEE as mitigation), MLASWE-0013 (Insufficient Runtime Monitoring)
- **NIST AI RMF:** MANAGE 1.3 (Infrastructure security), MEASURE 2.6 (Runtime monitoring)
- **Standards:** Intel SGX Developer Guide, AMD SEV-SNP Firmware Interface, NIST SP 800-193 (Platform Firmware Resiliency)
- **Reference:** Confidential Computing Consortium — Security Primitives (2024)
