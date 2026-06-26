# MLASTG-TEST-SUPPLY-002: Pre-Trained Model Provenance Verification

## Control Reference
**Controls Tested:** MLASVS-SUPPLY-002 (Pre-trained Model Origin Verification), MLASVS-SUPPLY-006 (Model Hash Verification at Load), MLASVS-SUPPLY-007 (Transfer Learning Source Validation), MLASVS-SUPPLY-009 (Base Model Vulnerability Scanning), MLASVS-SUPPLY-011 (Secure Model Distribution Channels), MLASVS-SUPPLY-012 (Third-Party Model Evaluation Report), MLASVS-SUPPLY-015 (Cryptographic Model Provenance — L2), MLASVS-SUPPLY-016 (Model Signing and Attestation — L2), MLASVS-SUPPLY-018 (Adversarial Robustness of Base Model — L2), MLASVS-SUPPLY-019 (Backdoor Scanning of Pre-Trained Models — L2), MLASVS-SUPPLY-020 (Vendor Security Assessment Program — L2), MLASVS-SUPPLY-022 (Reproducible Build Verification — L2)

## Severity
**High** (L1) / **Critical** (L2)

## Overview
Pre-trained models obtained from third-party sources (Hugging Face, model zoos, vendor APIs) represent a significant supply chain attack surface. Compromised or backdoored pre-trained models can introduce vulnerabilities that persist through fine-tuning. This test verifies that all pre-trained models have documented, verified origins and that their integrity is enforced at load time.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `sha256sum`, `openssl`, ModelScan (`pip install modelscan`) |
| Access | Model artifact storage (model files, model card, checksums) |
| Documentation | Source URLs and version documentation for all pre-trained models in use |

## Step-by-Step Procedure

### Step 1: Pre-Trained Model Inventory and Origin Verification
1. Enumerate all pre-trained models and checkpoints used in the target system
2. For each model, verify the following attributes are documented:
   - Source URL and repository (e.g., Hugging Face model card URL)
   - Model version or commit hash
   - Published cryptographic hash (SHA-256 minimum)
   - Model card or technical report documenting intended use, training data, and known limitations
3. **Pass if:** All pre-trained models have complete, documented, and verifiable origins
4. **Fail if:** Any model has an unknown or undocumented source, or lacks a published hash

### Step 2: Hash Verification at Load
1. Compute the SHA-256 hash of each model file currently in use:
   ```bash
   sha256sum model.safetensors
   sha256sum pytorch_model.bin
   ```
2. Compare the computed hash against the published/expected hash from the model source
3. **Pass if:** All computed hashes match the published expected values
4. **Fail if:** Any hash mismatch is detected — the model file has been tampered with

### Step 3: Verify Hash Verification is Enforced at Runtime
1. Review the model loading code to confirm hash verification is performed before the model is used:
   ```python
   import hashlib

   def load_verified_model(path: str, expected_sha256: str):
       """Load model only if SHA-256 hash matches the expected value."""
       sha256 = hashlib.sha256()
       with open(path, "rb") as f:
           for chunk in iter(lambda: f.read(65536), b""):
               sha256.update(chunk)
       actual = sha256.hexdigest()
       if actual != expected_sha256:
           raise ValueError(f"Model integrity check FAILED: expected {expected_sha256}, got {actual}")
       return load_model(path)
   ```
2. Modify the model file (add a null byte) and verify that loading raises an error
3. **Pass if:** Tampered model files are detected and loading is aborted

### Step 4: Scan Model Files for Unsafe Serialization (L2)
1. Run ModelScan against all model files to detect unsafe serialization patterns:
   ```bash
   modelscan --path model.pkl
   modelscan --path pytorch_model.bin
   modelscan --path model.h5
   ```
2. Review any flagged `__reduce__` calls or arbitrary code execution patterns in pickle serialization
3. **Pass if:** No unsafe serialization patterns are detected
4. **Fail if:** Any model file contains code that would execute on deserialization (pickle `__reduce__` exploit)

### Step 5: Verify Cryptographic Model Signing (L2)
1. Verify that model files are cryptographically signed using an organizational key pair
2. Verify the signature before deployment:
   ```bash
   openssl dgst -sha256 -verify model_signing_key.pub -signature model.sig model.bin
   ```
3. **Pass if:** All production models are signed and signature verification passes
4. **Fail if:** Models are unsigned or signature verification fails

### Step 6: Base Model Backdoor Scanning (L2)
1. For each pre-trained model used as a base for fine-tuning, run backdoor scanning analysis (see TEST-MODEL-004 for detailed procedure)
2. Reference the backdoor scanning results from MODEL-004 for any base model in scope
3. **Pass if:** No backdoor indicators detected in any base model

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | All pre-trained models have documented origins; hash verification passes; model loading code enforces hash check |
| L2 | No unsafe serialization detected; all models cryptographically signed; backdoor scanning completed |

## Evidence Requirements

- [ ] Pre-trained model inventory with source URLs and version documentation
- [ ] Hash verification results for each model file
- [ ] Model loading code review evidence (hash enforcement at load time)
- [ ] (L2) ModelScan output for all model files
- [ ] (L2) Model signing verification results
- [ ] (L2) Backdoor scanning results (cross-reference TEST-MODEL-004)

## Remediation Guidance

**If model origin is undocumented:**
1. Quarantine the model from production until provenance is established
2. Trace the model file's origin through system logs, git history, or artifact registries
3. Replace with a model from a verified, documented source if provenance cannot be established

**If hash verification fails:**
1. Do not use the model — treat the mismatch as a security incident
2. Investigate how the model file was modified (unauthorized access, storage corruption, supply chain tampering)
3. Restore from a known-good backup and enforce integrity monitoring

**If unsafe serialization is detected:**
1. Do not load or deploy the affected model file
2. Require all models to use safe serialization formats (SafeTensors preferred over Pickle)
3. Implement pre-load scanning with ModelScan as a CI/CD gate

## References
- **MITRE ATLAS:**
  - `AML.T0010` — Adversarial Examples (model tampering context)
  - `AML.T0018` — Backdoor ML Model
  - `AML.TA0003` — Supply Chain Compromise (tactic)
- **MLASWE:** MLASWE-0009 (Insufficient ML-SBOM / Supply Chain Hygiene), MLASWE-0007 (Backdoor / Trojan ML Model)
- **NIST AI RMF:** MAP 1.5 (Risk identification), GOVERN 1.6 (Supply chain risk)
- **Related Standard:** Sigstore (model signing), NTIA Minimum SBOM Elements
