# MLASTG → ATLAS Gap Analysis

## Overview
This document identifies MITRE ATLAS techniques that have **no or insufficient coverage** by MLASVS controls. These are priority areas for developing new controls and test cases.

## 🔴 Critical Gaps: No Coverage

| ATLAS ID | Technique | Risk | Recommended New Control |
|----------|-----------|------|------------------------|
| — | ML Model Inventory Discovery | Medium | GOV-016a: Model inventory obfuscation; restrict API discovery endpoints |

**Impact:** An adversary can discover what ML models an organization uses without any defensive detection. No official ATLAS ID exists for this attack path — tracked as MLASTG-internal gap.

🟡 **4 techniques with Partial coverage need L2 controls and/or dedicated test cases:**

| ATLAS ID | Technique | Current Gap | Recommended |
|----------|-----------|-------------|-------------|
| AML.TA0001 | Reconnaissance | Only red team exercises (GOV-016) and pen testing (INFRA-021) — no technical detection controls | MLASVS-GOV: Reconnaissance detection monitoring |
| AML.TA0002 | Valid Accounts | DATA-003 and GOV-001 cover inventory but not usage monitoring | MLASVS-INFRA: ML-specific account monitoring |
| AML.TA0003.001 | Acquire ML Model | SUPPLY-002, 006, 009 cover vetting but not ongoing monitoring | MLASVS-SUPPLY: Continuous base model monitoring |
| AML.TA0006 | Backdoor ML Model | MODEL-021/022 (L2) have detection but no automated prevention | MLASVS-MODEL: Automated backdoor prevention at training |
| AML.T0018 | Model Inversion | MODEL-019/020 (L2) and INFRA-016 exist but no L1 baseline | MLASVS-MODEL: L1 inversion prevention (output clipping) |
| AML.T0020 | Data Poisoning | DATA-024/025 (L2) exist but no L1 automated detection | MLASVS-DATA: L1 poisoning detection (statistical checks) |

## Coverage Improvement Roadmap

| Priority | Tactic | Technique | Action | Effort |
|----------|--------|-----------|--------|--------|
| P0 | Reconnaissance (TA0001) | Model Discovery | Add MLASVS-GOV control for discovery monitoring | Medium |
| P1 | Impact | Data Poisoning | Add L1 statistical poisoning detection | Medium |
| P2 | Collection | Model Inversion | Add L1 output clipping control | Low |
| P3 | Persistence | Backdoor | Add automated training-time prevention | High |

## Complete Unmapped ATLAS Techniques

The following ATLAS techniques/sub-techniques fall outside current MLASTG scope but should be evaluated for future coverage:

| ATLAS ID | Technique | Consideration |
|----------|-----------|--------------|
| AML.T0040 | ML Supply Chain (AI Bill of Materials) | Partially covered by ML-SBOM; dedicated control needed |
| AML.T0041 | ML Supply Chain (External ML Services) | Covered by SUPPLY-020; enhancement needed |
| AML.T0042 | ML Attack Staging | Future: control for staging environment security |
| AML.T0043 | ML Output Handling | Future: beyond LLM output handling |

## How to Close Gaps

1. **For "None" techniques**: Create new MLASVS controls following the existing template format
2. **For "Partial" techniques**: Add missing L2 controls or test cases
3. Update this gap analysis after each major framework update
