# MLASVS-SUPPLY-1: ML Software Bill of Materials (ML-SBOM)

## Category
MLASVS-SUPPLY: Supply Chain Security

## Overview
The ML Software Bill of Materials (ML-SBOM) documents every component in an ML system's supply chain — including pre-trained models, training datasets, ML libraries, frameworks, and training infrastructure. A complete ML-SBOM enables vulnerability tracking, incident response, and compliance verification.

## Controls

### SUPPLY-001: ML-SBOM Generation (L1)
**Description:** A complete ML-SBOM must be generated for each model, covering model metadata, base models, training datasets, framework dependencies, and training environment.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Request the ML-SBOM for each production model
2. Verify SBOM includes: model name/version/author, base model source + hash, training dataset origin + hash, framework/library versions, training environment specs
3. Check SBOM format (CycloneDX or SPDX recommended)
4. **Pass if:** Complete ML-SBOM exists for all production models

**Remediation:** Implement automated SBOM generation in the model registration pipeline. Use CycloneDX ML-CDX extension when available.

---

### SUPPLY-003: Training Dataset Provenance (L1)
**Description:** Each training dataset must have documented provenance including source URL, collection date, license, and responsible party.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. For each training dataset, verify: source URL or origin, collection date/methodology, license terms, responsible team
2. Check that provenance is recorded in the ML-SBOM
3. **Pass if:** All training datasets have complete provenance records

---

### SUPPLY-004: ML Library Version Tracking (L1)
**Description:** All ML libraries and frameworks used in training and inference must be tracked with specific versions in the ML-SBOM.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Verify that all ML dependencies (PyTorch, TensorFlow, scikit-learn, transformers, etc.) are listed with specific versions
2. Check that the SBOM includes training and inference dependencies
3. **Pass if:** Complete dependency inventory exists

---

### SUPPLY-005: License Compliance Check (L1)
**Description:** All ML components must be checked for license compliance before use.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Review license terms for all third-party models and datasets
2. Check for incompatible or restricted licenses
3. **Pass if:** License compliance review is documented for all components

---

### SUPPLY-008: Dataset License Verification (L1)
**Description:** Dataset licenses must be verified and documented to ensure compliance with usage terms.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. For each dataset, identify the license (MIT, CC, custom, etc.)
2. Verify intended use is compatible with license terms
3. **Pass if:** Licenses are compatible with intended use case

---

### SUPPLY-010: ML Dependency Scanning (L1)
**Description:** ML libraries and dependencies must be scanned for known vulnerabilities using standard security scanners.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Run dependency scanner (Trivy, Snyk, Dependabot) on ML project dependencies
2. Review findings for critical and high-severity CVEs
3. **Pass if:** No critical CVEs without documented mitigation plan

---

### SUPPLY-013: Automated ML-SBOM Generation in CI/CD (L2)
**Description:** ML-SBOM must be automatically generated as part of the CI/CD pipeline and updated on each model version.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Verify CI/CD pipeline includes automated SBOM generation step
2. Check that SBOM is versioned alongside the model artifact
3. **Pass if:** SBOM is automatically generated per model version

---

### SUPPLY-014: Continuous Dependency Monitoring (L2)
**Description:** ML dependencies must be continuously monitored for newly discovered vulnerabilities.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Verify continuous monitoring tool is configured (Dependabot, Renovate, Snyk)
2. Check alerting is configured for newly discovered CVEs
3. **Pass if:** Continuous monitoring is active with alerts configured

---

### SUPPLY-017: Fine-tuning Data Provenance Chain (L2)
**Description:** For fine-tuned models, the provenance chain must extend from base model through all fine-tuning datasets.

**MITRE ATLAS:** AML.T0020 (Data Poisoning)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. For fine-tuned models, verify: base model source + hash, fine-tuning dataset(s) provenance, adapter weights provenance
2. **Pass if:** Complete provenance chain exists for fine-tuned models

---

### SUPPLY-021: ML Supply Chain Incident Response (L2)
**Description:** An incident response plan specifically addressing ML supply chain compromises must exist and be tested.

**MITRE ATLAS:** AML.TA0003 (Resource Development)
**Test Reference:** MLASTG-TEST-SUPPLY-001

**Verification:**
1. Review ML supply chain incident response plan
2. Verify plan covers: compromised base model, poisoned dataset, vulnerable dependency, malicious package
3. **Pass if:** IR plan covers ML-specific supply chain scenarios

## Cross-References
- MITRE ATLAS: AML.TA0003, AML.T0020
- MLASWE: MLASWE-0009
- NIST AI RMF: MAP-1, MAP-2
