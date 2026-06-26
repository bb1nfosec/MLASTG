# MLASTG-TEST-SUPPLY-001: ML Software Bill of Materials (ML-SBOM) Audit

## Control Reference
**Controls Tested:** MLASVS-SUPPLY-001 (ML-SBOM Generation), MLASVS-SUPPLY-003 (Training Dataset Provenance), MLASVS-SUPPLY-004 (ML Library Version Tracking), MLASVS-SUPPLY-005 (License Compliance Check), MLASVS-SUPPLY-008 (Dataset License Verification), MLASVS-SUPPLY-010 (ML Dependency Scanning), MLASVS-SUPPLY-013 (Automated ML-SBOM Generation in CI/CD — L2), MLASVS-SUPPLY-014 (Continuous Dependency Monitoring — L2), MLASVS-SUPPLY-017 (Fine-tuning Data Provenance Chain — L2), MLASVS-SUPPLY-021 (ML Supply Chain Incident Response — L2)

## Severity
**High** (L1) / **Critical** (L2)

## Overview
An ML Software Bill of Materials (ML-SBOM) is the foundation of ML supply chain security. Without it, organizations cannot know what models, datasets, and libraries compose their ML system — making vulnerability management, license compliance, and incident response impossible. This test verifies that a complete and current ML-SBOM exists and is actively maintained.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | CycloneDX (`pip install cyclonedx-bom`), Trivy (see installation below), ModelScan (`pip install modelscan`) |
| Access | Model registry, artifact store, CI/CD pipeline configuration |
| Documentation | Existing dependency manifests (`requirements.txt`, `pyproject.toml`, `conda.yml`) |

**Tool Installation:**
```bash
# CycloneDX for SBOM generation
pip install cyclonedx-bom

# Trivy for vulnerability scanning (Linux)
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo deb https://aquasecurity.github.io/trivy-repo/deb generic main | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt-get update && sudo apt-get install trivy

# macOS
brew install trivy
```

## Step-by-Step Procedure

### Step 1: Verify ML-SBOM Exists
1. Locate the ML-SBOM document for the target system
2. Verify the SBOM uses a machine-readable format (CycloneDX JSON/XML recommended; SPDX acceptable)
3. Verify the SBOM covers all required components:
   - Base or pre-trained model (name, version, source URL, hash)
   - Training and fine-tuning datasets (name, version, source, license)
   - ML framework and library dependencies (name, version, CVE status)
   - Training and inference environment (OS, CUDA version, hardware)
4. **Pass if:** An ML-SBOM exists in a machine-readable format covering all required components
5. **Fail if:** No SBOM exists, or it is incomplete / undated

### Step 2: Verify Dependency Vulnerability Scanning
1. Run a vulnerability scanner against the ML dependency manifest:
   ```bash
   # Scan Python environment
   trivy fs --scanners vuln requirements.txt

   # Or scan the full project directory
   trivy fs --scanners vuln .
   ```
2. Identify all CVEs with severity ≥ HIGH
3. For each high/critical CVE, check whether a documented mitigation or upgrade path exists
4. **Pass if:** No unmitigated HIGH or CRITICAL CVEs exist in the dependency list
5. **Fail if:** One or more HIGH/CRITICAL CVEs have no documented mitigation

### Step 3: Verify License Compliance
1. Review the SBOM for all dataset and model licenses
2. Flag any licenses that are incompatible with the organization's use case (e.g., non-commercial-only datasets used in a commercial product)
3. **Pass if:** All datasets and base models are licensed for the intended use case
4. **Fail if:** Any dataset or model is used in violation of its license terms

### Step 4: Verify Automated SBOM Generation in CI/CD (L2)
1. Review the CI/CD pipeline configuration for automated SBOM generation steps
2. Verify the SBOM is regenerated and versioned on every model training or deployment event:
   ```bash
   # Example: CycloneDX automated generation
   cyclonedx-py environment -o sbom-$(git rev-parse --short HEAD).json
   ```
3. Verify the generated SBOM is stored in a version-controlled artifact store
4. **Pass if:** SBOM is automatically generated and version-stamped on each model version

### Step 5: Verify Continuous Monitoring (L2)
1. Verify that new CVEs are automatically checked against the SBOM on a regular schedule (at minimum, daily)
2. Verify that alerts are generated when new HIGH/CRITICAL CVEs affect components in the SBOM
3. **Pass if:** Automated CVE monitoring is configured and alert routing is tested

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | ML-SBOM exists in machine-readable format covering all components; no unmitigated HIGH/CRITICAL CVEs; all licenses compliant |
| L2 | Automated SBOM generation in CI/CD; continuous CVE monitoring with alerting; fine-tuning data provenance chain documented |

## Evidence Requirements

- [ ] ML-SBOM document (CycloneDX or SPDX format)
- [ ] Vulnerability scan results with CVE list and mitigation status
- [ ] License compliance review results
- [ ] (L2) CI/CD pipeline configuration showing automated SBOM generation
- [ ] (L2) Continuous monitoring configuration and alert routing documentation
- [ ] (L2) Supply chain incident response playbook

## Remediation Guidance

**If no SBOM exists:**
1. Generate an initial SBOM using CycloneDX: `cyclonedx-py environment -o ml-sbom.json`
2. Augment the auto-generated SBOM with ML-specific metadata (base model, datasets) manually
3. Establish a process to regenerate and version the SBOM on every model change

**If HIGH/CRITICAL CVEs are present:**
1. Prioritize upgrading affected libraries in the next sprint
2. Document an interim mitigation plan if upgrading immediately is not feasible
3. Set a hard remediation deadline: critical CVEs ≤ 48 hours; high CVEs ≤ 2 weeks

**If license violations are found:**
1. Immediately quarantine the affected model or dataset from production
2. Engage legal counsel to assess exposure
3. Replace with a license-compatible alternative dataset or model

## References
- **MITRE ATLAS:**
  - `AML.T0010` — Adversarial Examples (dependency tampering context)
  - `AML.TA0003` — Supply Chain Compromise (tactic)
- **MLASWE:** MLASWE-0009 (Insufficient ML-SBOM / Supply Chain Hygiene)
- **NIST AI RMF:** MAP 1.5 (Risk identification), GOVERN 1.6 (Supply chain risk)
- **Related Standard:** NTIA Minimum Elements for an SBOM; CycloneDX ML Bill of Materials Specification
