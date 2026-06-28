# MLASVS-SUPPLY-2: Base Model Vetting

## Category
MLASVS-SUPPLY: Supply Chain Security

## Overview
Base model vetting ensures that pre-trained models sourced from third parties are evaluated for security risks before being incorporated into production ML systems. This includes vulnerability scanning, provenance verification, and security testing.

## Controls

### SUPPLY-002: Pre-trained Model Origin Verification (L1)
**Description:** Origin and authenticity of all pre-trained models must be verified.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. For each pre-trained model, verify: source URL, publisher/organization, version, date downloaded
2. Check cryptographic signature or hash from trusted source
3. **Pass if:** Model origin is verified and documented

---

### SUPPLY-006: Model Hash Verification at Load (L1)
**Description:** Cryptographic hashes must be verified when loading pre-trained models.

**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Review model loading code for hash verification
2. Attempt to load a tampered model file
3. **Pass if:** Tampered models are detected and rejected at load time

---

### SUPPLY-007: Transfer Learning Source Validation (L1)
**Description:** Source models used for transfer learning must be validated for security.

**MITRE ATLAS:** AML.T0020 (Data Poisoning)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Verify that transfer learning source models underwent security evaluation
2. Check for known issues with the source model
3. **Pass if:** Source model has documented security evaluation

---

### SUPPLY-009: Base Model Vulnerability Scanning (L1)
**Description:** Pre-trained models must be scanned for known vulnerabilities.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Run vulnerability scanner on model files (ModelScan, etc.)
2. Check for unsafe deserialization, embedded code, or known vulnerabilities
3. **Pass if:** No critical vulnerabilities in base model

---

### SUPPLY-011: Secure Model Distribution Channels (L1)
**Description:** Models must be distributed through secure, authenticated channels.

**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Review model distribution mechanism (registry, artifact store, etc.)
2. Verify TLS and authentication are used for model downloads
3. **Pass if:** All model distribution uses secure channels

---

### SUPPLY-012: Third-Party Model Evaluation Report (L1)
**Description:** Comprehensive security evaluation reports must exist for third-party models.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Review security evaluation reports for each third-party model
2. Verify evaluation covers: origin, vulnerabilities, robustness, poisoning
3. **Pass if:** Evaluation reports exist and are current

---

### SUPPLY-015: Cryptographic Model Provenance (L2)
**Description:** Full cryptographic provenance using signed manifests for all models.

**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Verify signed manifests exist for each model version
2. Validate signature chain from development through deployment
3. **Pass if:** Complete signed provenance chain exists

---

### SUPPLY-016: Model Signing and Attestation (L2)
**Description:** Models must be cryptographically signed and attested before deployment.

**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Verify model signing implementation (sigstore, GPG, or equivalent)
2. Check that signing is automated in CI/CD pipeline
3. **Pass if:** Models are signed and verified before deployment

---

### SUPPLY-018: Adversarial Robustness of Base Model (L2)
**Description:** Base models must undergo adversarial robustness evaluation.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Review adversarial robustness test results for base model
2. Verify acceptable robustness thresholds are met
3. **Pass if:** Base model meets minimum robustness criteria

---

### SUPPLY-019: Backdoor Scanning of Pre-trained Models (L2)
**Description:** Pre-trained models must be scanned for potential backdoors.

**MITRE ATLAS:** AML.T0020 (Data Poisoning)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Run backdoor detection techniques (activation clustering, pruning, trigger inversion)
2. Verify no indicators of backdoor presence
3. **Pass if:** No backdoor indicators detected

---

### SUPPLY-020: Vendor Security Assessment Program (L2)
**Description:** Third-party ML model vendors must undergo security assessment.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Verify vendor security assessment program exists
2. Check that assessments cover: data handling, model security, incident response, compliance
3. **Pass if:** Vendor assessments are completed and current

---

### SUPPLY-022: Reproducible Build Verification (L2)
**Description:** Model builds must be reproducible from source to verify integrity.

**MITRE ATLAS:** AML.TA0006 (Persistence)
**Test Reference:** MLASTG-TEST-SUPPLY-002

**Verification:**
1. Verify training pipeline produces identical model given same code + data + seed
2. Compare cryptographic hashes of independent builds
3. **Pass if:** Builds are reproducible with matching hashes

## Cross-References
- MITRE ATLAS: AML.TA0003, AML.TA0006, AML.T0010, AML.T0020
- MLASWE: MLASWE-0007, MLASWE-0009
- NIST AI RMF: MAP-1, MAP-2, MEASURE-2
