# MLASVS-SUPPLY-3: Dependency Security

## Category
MLASVS-SUPPLY: Supply Chain Security

## Overview
ML dependency security addresses vulnerabilities in the software libraries, frameworks, and runtime environments used throughout the ML lifecycle. ML projects often have complex dependency trees that can introduce supply chain risks.

## Controls

### SUPPLY-004: ML Library Version Tracking (L1)
**Description:** All ML libraries and frameworks used in training and inference must be tracked with specific versions in the ML-SBOM.

*Already defined in SUPPLY-1 (ML-SBOM). Cross-reference for completeness.*

### SUPPLY-010: ML Dependency Scanning (L1)
**Description:** ML libraries and dependencies must be scanned for known vulnerabilities using standard security scanners.

*Already defined in SUPPLY-1 (ML-SBOM). Cross-reference for completeness.*

## Additional Dependencies Security Measures

### DEP-001: Dependency Pinning (L1)
**Description:** All ML dependencies must be pinned to specific versions (not version ranges) in requirements files.

**Verification:**
1. Review `requirements.txt`, `pyproject.toml`, `environment.yml` for unpinned dependencies
2. Check for version ranges (e.g., `torch>=1.0` without upper bound)
3. **Pass if:** All dependencies are pinned to specific versions

**Remediation:** Pin all dependencies using `pip freeze > requirements.txt` or use lock files (`Pipfile.lock`, `poetry.lock`).

---

### DEP-002: Private Package Repositories (L2)
**Description:** For enterprise deployments, ML dependencies should be sourced from private, vetted package repositories rather than public PyPI.

**Verification:**
1. Verify enterprise package proxy is configured (e.g., JFrog Artifactory, AWS CodeArtifact)
2. Check that public PyPI access is restricted or proxied
3. **Pass if:** Dependencies are served through controlled, private repository

---

### DEP-003: SBOM Scanning for ML Libraries (L1)
**Description:** ML library SBOMs must be generated and scanned for vulnerabilities.

**Verification:**
1. Generate SBOM for ML project dependencies using `cyclonedx-py`
2. Run vulnerability scanner against SBOM
3. **Pass if:** SBOM scan shows no critical unmitigated vulnerabilities

---

### DEP-004: Runtime Environment Hardening (L2)
**Description:** ML runtime environments (containers, virtual environments) must be hardened.

**Verification:**
1. Review Dockerfile or environment configuration for security best practices
2. Check that base images are minimal and updated
3. **Pass if:** Runtime environments follow hardening guidelines

## Cross-References
- MITRE ATLAS: AML.TA0003
- MLASWE: MLASWE-0009
- OWASP ML Top 10: ML05 (Supply Chain)
