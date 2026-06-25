# MLASWE — MLSec Application Security Weakness Enumeration

## Overview

The **MLSec Application Security Weakness Enumeration (MLASWE)** is a comprehensive taxonomy of security weaknesses and vulnerabilities specific to machine learning systems. It serves as the classification layer for findings discovered during MLASTG assessments.

MLASWE follows the spirit of the **Common Weakness Enumeration (CWE)** and the **OWASP MASWE** but is tailored to the unique attack surface of ML/LLM systems.

## Purpose

- **Standardized Classification:** Provides consistent vulnerability identifiers for ML security findings
- **Cross-Reference Bridge:** Links MLASVS controls (defender requirements) to MITRE ATLAS techniques (attacker perspective)
- **Finding Taxonomy:** Enables security teams to classify, track, and trend ML-specific vulnerabilities
- **Knowledge Base:** Each MLASWE entry includes detection methods, remediation guidance, and real-world references

## MLASWE → MLASVS → MITRE ATLAS Mapping

```
MLASWE (Weakness)          ─── What went wrong
    │
    ├── Linked to ──► MLASVS controls that prevent this weakness
    └── Linked to ──► MITRE ATLAS techniques that exploit this weakness

Example:
    MLASWE-0001 (Adversarial Perturbation)
        ├── Prevented by: MLASVS-MODEL-001, MODEL-002, MODEL-016
        └── Exploited via: MITRE ATLAS AML.T0010
```

## Weakness Classification Structure

Each MLASWE entry follows this format:

```
## MLASWE-XXXX: [Weakness Title]

### Description
[What the weakness is and how it manifests in ML systems]

### Risk
- **Severity:** Critical / High / Medium / Low
- **Exploitability:** Easy / Medium / Difficult
- **Prevalence:** Common / Uncommon / Rare

### Affected Components
[Which ML system components are vulnerable]

### Detection Methods
[How to detect this weakness during testing]

### Preventive Controls (MLASVS)
[Links to relevant MLASVS controls]

### Attack Techniques (MITRE ATLAS)
[Links to relevant ATLAS techniques]

### Remediation
[How to fix or mitigate]

### Real-World Examples
[Known incidents or published research]

### References
[Papers, tools, CVE references]
```

## Complete MLASWE Catalog

| ID | Weakness | Severity | Related MLASVS | MITRE ATLAS |
|----|----------|----------|----------------|-------------|
| 0001 | Adversarial Perturbation | High | MODEL-001, MODEL-002, MODEL-016 | AML.T0010 |
| 0002 | Data Poisoning | Critical | DATA-011, DATA-024, DATA-025 | AML.T0020 |
| 0003 | Model Extraction | High | MODEL-005, MODEL-018, MODEL-023 | AML.T0034 |
| 0004 | Model Inversion | Medium | MODEL-019, MODEL-020 | AML.T0018 |
| 0005 | Membership Inference | Medium | MODEL-020, DATA-019 | AML.T0018 |
| 0006 | Prompt Injection | Critical | LLM-001, LLM-015, LLM-016 | AML.T0051 |
| 0007 | Backdoor/Trojan | Critical | MODEL-021, MODEL-022 | AML.T0020 |
| 0008 | Model Denial of Service | High | LLM-011, MODEL-012 | AML.T0037 |
| 0009 | Supply Chain Compromise | Critical | SUPPLY-001 through SUPPLY-022 | AML.TA0003 |
| 0010 | Insecure Output Handling | High | LLM-003, LLM-009, LLM-014 | AML.T0052 |
| 0011 | Excessive Agency | High | LLM-007, LLM-010, LLM-020 | AML.T0053 |
| 0012 | Training Data Leakage | High | DATA-005, DATA-010, DATA-015 | AML.TA0010 |

## Using MLASWE in Findings

When reporting a security finding during an ML assessment:

```yaml
Finding:
  title: "Prompt injection vulnerability in LLM chat application"
  mlaswe: "MLASWE-0006"
  mlasvs: "MLASVS-LLM-001 (Prompt Injection Prevention)"
  mitre_atlas: "AML.T0051"
  severity: "Critical"
  description: "..."
  evidence: "..."
  remediation: "..."
```

## Related Links

- [Complete MLASWE-0001: Adversarial Perturbation](MLASWE-0001-Adversarial-Perturbation.md)
- [Complete MLASWE-0002: Data Poisoning](MLASWE-0002-Data-Poisoning.md)
- [Complete MLASWE-0006: Prompt Injection](MLASWE-0006-Prompt-Injection.md)
- [MLASVS Categories](../MLASVS/0x02-MLASVS-Categories.md)
- [MITRE ATLAS](https://atlas.mitre.org/)
