# MLASTG Compliance Report

**Generated:** 2026-06-27 12:53:40
**Compliance Score:** 50.0%

## Summary
- **Passed:** 2
- **Failed:** 2
- **Errors:** 0

## Detailed Findings

### ❌ Failed Controls
#### MLASTG-TEST-MODEL-002: Model Extraction Resistance (Severity: L1)
- **Control:** MLASVS-MODEL-004
- **Evidence:** API endpoint returned raw probabilities with 8 decimal precision, enabling high-fidelity surrogate training.

#### MLASTG-TEST-SUPPLY-001: ML-SBOM Audit (Severity: L1)
- **Control:** MLASVS-SUPPLY-001
- **Evidence:** No CycloneDX or SPDX ML-SBOM found in repository.

### ✅ Passed Controls
- **MLASTG-TEST-MODEL-001**: Adversarial Robustness Testing (MLASVS-MODEL-001)
- **MLASTG-TEST-LLM-001**: Prompt Injection Testing (MLASVS-LLM-001)
