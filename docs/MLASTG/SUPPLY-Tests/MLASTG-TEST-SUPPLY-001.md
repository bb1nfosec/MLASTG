# MLASTG-TEST-SUPPLY-001: ML-SBOM Audit

## Control Reference
MLASVS-SUPPLY-001 (ML-SBOM Generation), SUPPLY-003 (Dataset Provenance), SUPPLY-004 (Library Tracking), SUPPLY-005 (License Compliance), SUPPLY-008 (Dataset License), SUPPLY-010 (Dependency Scanning), SUPPLY-013 (Automated SBOM in CI/CD - L2), SUPPLY-014 (Continuous Monitoring - L2), SUPPLY-017 (Fine-tuning Provenance - L2), SUPPLY-021 (Supply Chain IR - L2)

## Severity
High

## Procedure

### Step 1: Verify ML-SBOM Exists
1. Locate ML-SBOM document (CycloneDX format recommended)
2. Verify it covers: model metadata, base model, training datasets, framework dependencies, training environment
3. **Pass if:** ML-SBOM exists and covers all required components

### Step 2: Verify Dependency Scanning
1. Run vulnerability scanner on ML dependencies listed in SBOM
2. Identify CVEs with severity ≥ High
3. **Pass if:** No critical/high vulnerabilities without documented mitigations

### Step 3: Verify Automated Generation (L2)
1. Check CI/CD pipeline for automated ML-SBOM generation
2. Verify SBOM is updated on each model version
3. **Pass if:** SBOM is automatically generated and versioned

## References
- MITRE ATLAS: AML.TA0003
- MLASWE: MLASWE-0009
