# MLASTG-TEST-MODEL-005: Model Integrity Verification

## Control Reference
- MLASVS-MODEL-007: Model Versioning
- MLASVS-MODEL-008: Model Signing
- MLASVS-MODEL-014: Secure Model Serialization
- MLASVS-MODEL-015: Model Rollback Capability
- MLASVS-MODEL-030: Model Provenance Attestation (L2)

## Severity
**Medium** (L1) / **High** (L2)

## Overview
Model integrity controls ensure that deployed ML models are authentic, untampered, properly versioned, and can be rapidly rolled back if compromised. A model that lacks integrity verification can be silently replaced with a backdoored or degraded version without detection. This test verifies versioning, signing, serialization safety, rollback capability, and provenance attestation.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `sha256sum`, `openssl`, ModelScan (`pip install modelscan`) |
| Access | Model registry, artifact store, deployment pipeline configuration |
| Documentation | Model versioning policy, signing key management, rollback procedures |

## Step-by-Step Procedure

### Step 1: Verify Model Versioning
1. Review the model registry for version history.
2. Verify that each model version has immutable version identifiers, timestamp of creation, training data hash, code commit hash, and author identity.
3. Verify that model artifacts are never overwritten (append-only).
4. **Pass condition:** Complete version history exists for all production models with required metadata.
5. **Fail condition:** Versions are missing, overwritten, or lack required metadata.

### Step 2: Verify Model Signing
1. Check that model files are cryptographically signed (e.g., using GPG or Sigstore/Cosign).
2. Attempt to deploy an unsigned model and verify it is rejected.
3. **Pass condition:** All production models are signed; unsigned models are rejected at deployment.
4. **Fail condition:** Models can be deployed without signing, or signature verification is not enforced.

### Step 3: Verify Hash Verification at Load
1. Review model loading code for hash verification implementation.
2. Tamper with a model file (e.g., add a null byte) and verify detection.
3. **Pass condition:** Hash verification is enforced at load time; tampered files are rejected.
4. **Fail condition:** Models can be loaded without integrity verification.

### Step 4: Verify Safe Serialization
1. Scan all model files for unsafe serialization patterns using tools like `modelscan`.
2. Check for Pickle `__reduce__` exploits or arbitrary code execution patterns.
3. Verify that SafeTensors format is preferred over Pickle for PyTorch models.
4. **Pass condition:** No unsafe serialization detected; SafeTensors used where possible.
5. **Fail condition:** Pickle files with `__reduce__` patterns are found, or SafeTensors is not used for new models.

### Step 5: Verify Rollback Capability
1. Identify the last three production model versions in the registry.
2. Execute a rollback to the previous version in a staging environment.
3. Measure rollback completion time against the documented Recovery Time Objective (RTO).
4. **Pass condition:** Rollback completes within the documented Recovery Time Objective (RTO).
5. **Fail condition:** Rollback fails, is not documented, or exceeds RTO.

### Step 6: Verify Model Provenance Attestation (L2)
1. Verify that each production model has a provenance attestation document including origin, training data provenance chain, environment, process, and cryptographic chain of custody.
2. **Pass condition:** Complete provenance attestation exists for all production models.
3. **Fail condition:** Any production model lacks provenance documentation.

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Model versioning complete; models signed; hash verification at load; safe serialization used; rollback tested. |
| L2 | All L1 controls met; model provenance attestation documented; complete chain of custody maintained. |

## Evidence Requirements
- [ ] Model registry version history screenshot or export
- [ ] Model signing verification results
- [ ] Hash verification code review evidence
- [ ] ModelScan output for all model files
- [ ] Rollback test results with completion time
- [ ] (L2) Model provenance attestation documents

## Remediation Guidance
**If model signing is absent:**
1. Integrate Sigstore or GPG signing into the CI/CD pipeline post-training.
2. Add signature verification as a pre-deployment check.
3. Reject unsigned model artifacts in the model registry.

**If hash verification is missing:**
1. Implement hash verification in the model loading code.
2. Store expected hashes in the model registry alongside the artifact.
3. Add hash verification as a CI/CD gate.

**If rollback is not possible:**
1. Maintain at least 3 previous production model versions in the registry.
2. Document and test rollback procedures quarterly.
3. Define and enforce Recovery Time Objective (RTO) for model rollback.

## References
- MITRE ATLAS: AML.TA0006 - Persistence (Model Registry Manipulation)
- MITRE ATLAS: AML.TA0002 - Initial Access (Supply Chain Compromise)
- MLASWE: MLASWE-0009 (Supply Chain Compromise)
