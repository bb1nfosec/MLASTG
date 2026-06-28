# Coverage Matrix: MITRE ATLAS Techniques → MLASVS Controls

> ✅ **All ATLAS technique IDs verified against the official MITRE ATLAS taxonomy.**
> Only techniques that exist in the official ATLAS framework are listed below.

## Technique Coverage Map

### Reconnaissance (AML.TA0001)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| — | ML Model Inventory Discovery | 🔴 **Unguided** | No dedicated control. Red team exercises (GOV-016) and pen testing (INFRA-021) provide indirect coverage. | — | — |

### Resource Development (AML.TA0003)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0003 | Acquire ML Model | 🟡 Partial | SUPPLY-002, SUPPLY-006, SUPPLY-009, SUPPLY-012 | TEST-SUPPLY-002 | MLASWE-0009 |
| AML.TA0003 | Compromise ML Supply Chain | 🟢 Full | SUPPLY-001 through SUPPLY-022 | TEST-SUPPLY-001, TEST-SUPPLY-002 | MLASWE-0009 |

### Initial Access (AML.TA0002)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0002 | Exploit Public-Facing ML Application | 🟢 Full | INFRA-002, INFRA-003, INFRA-004, INFRA-009 | TEST-INFRA-002 | — |
| AML.TA0002 | Valid Accounts | 🟡 Partial | DATA-003, DATA-007, PIPELINE-001 | TEST-DATA-004, TEST-PIPELINE-001 | — |
| AML.TA0002 | ML Pipeline Access | 🟢 Full | PIPELINE-001, PIPELINE-003, PIPELINE-004, PIPELINE-008 | TEST-PIPELINE-001 | — |
| AML.TA0002 | Supply Chain Compromise | 🟢 Full | SUPPLY-002, SUPPLY-011, SUPPLY-012, SUPPLY-020 | TEST-SUPPLY-002 | MLASWE-0009 |

### Execution (AML.TA0005)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0005 | ML Model Execution | 🟢 Full | PIPELINE-005, INFRA-012, INFRA-017, PIPELINE-011, PIPELINE-012 | TEST-PIPELINE-001, TEST-INFRA-001, TEST-INFRA-004 | — |
| AML.TA0005 | Malicious Code in ML Pipeline | 🟢 Full | PIPELINE-014, PIPELINE-020 | TEST-PIPELINE-001 | — |

### Persistence (AML.TA0006)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0006 | ML Registry Manipulation | 🟢 Full | PIPELINE-008, PIPELINE-009, PIPELINE-010, PIPELINE-013 | TEST-PIPELINE-001 | — |
| AML.TA0006 | ML Artifact Tampering | 🟢 Full | PIPELINE-002, MODEL-007, MODEL-008, MODEL-015, MODEL-005, INFRA-022 | TEST-PIPELINE-001, TEST-MODEL-005, TEST-INFRA-004 | — |

### Defense Evasion (AML.TA0008)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| — | Adversarial Evasion | 🟢 Full | MODEL-001, MODEL-002, MODEL-003, MODEL-010, MODEL-024, INFRA-013 | TEST-MODEL-001 | MLASWE-0001 |

### Credential Access (AML.TA0007)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0007 | ML Credential Access | 🟢 Full | PIPELINE-005, INFRA-002 | TEST-PIPELINE-001, TEST-INFRA-002 | — |

### Discovery (AML.TA0009)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0009 | Discover ML Models | 🟢 Full | DATA-001, DATA-006, INFRA-007, GOV-001 | TEST-DATA-001, TEST-INFRA-001, TEST-GOV-001 | — |
| AML.TA0009 | Discover ML Data | 🟢 Full | DATA-001, DATA-006, DATA-020, DATA-030 | TEST-DATA-001 | — |

### Collection (AML.TA0010)

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| AML.TA0010 | ML Artifact Collection | 🟢 Full | DATA-002, DATA-005, DATA-008, DATA-009, DATA-010, DATA-012 | TEST-DATA-001, TEST-DATA-004 | MLASWE-0012 |
| AML.TA0010 | ML Training Data Exfiltration | 🟡 Partial | LLM-008, DATA-015, DATA-019 | TEST-LLM-002, TEST-DATA-003 | MLASWE-0012 |

### ML-Specific Techniques

| ATLAS ID | Technique | Coverage | MLASVS Controls | MLASTG Tests | MLASWE |
|----------|-----------|----------|-----------------|--------------|--------|
| **AML.T0043** | Input Manipulation | 🟢 Full | MODEL-003, DATA-004 | TEST-MODEL-001, TEST-DATA-002 | MLASWE-0001 |
| **AML.T0010** | Adversarial Perturbation | 🟢 Full | MODEL-001, MODEL-002, MODEL-010, MODEL-016, MODEL-017, MODEL-024, MODEL-025, MODEL-027, MODEL-029, INFRA-005, INFRA-013, INFRA-017 | TEST-MODEL-001, TEST-INFRA-001, TEST-INFRA-004 | MLASWE-0001 |
| **AML.T0018** | Model Inversion / Inference | 🟡 Partial | MODEL-019, MODEL-020, INFRA-016 | TEST-MODEL-003, TEST-INFRA-001 | MLASWE-0004, MLASWE-0005 |
| **AML.T0020** | Data Poisoning | 🟡 Partial | DATA-011, DATA-024, DATA-025, DATA-026, DATA-029 | TEST-DATA-002 | MLASWE-0002 |
| AML.T0020.001 | Label Poisoning | 🟡 Partial | DATA-011, DATA-013 | TEST-DATA-002 | MLASWE-0002 |
| AML.T0020.002 | Backdoor Poisoning | 🟡 Partial | MODEL-021, MODEL-022, SUPPLY-019 | TEST-MODEL-004, TEST-SUPPLY-002 | MLASWE-0007 |
| **AML.T0024.002** | Model Extraction | 🟢 Full | MODEL-004, MODEL-005, MODEL-006, MODEL-018, MODEL-023, INFRA-009 | TEST-MODEL-002, TEST-INFRA-002 | MLASWE-0003 |
| **AML.T0029** | Model Denial of Service | 🟢 Full | LLM-005, LLM-011, LLM-012, LLM-013, MODEL-012, INFRA-010 | TEST-LLM-003, TEST-MODEL-001, TEST-INFRA-002 | MLASWE-0008 |
| **AML.T0051** | LLM Prompt Injection | 🟢 Full | LLM-001, LLM-002, LLM-004, LLM-015, LLM-016, LLM-018, LLM-019, LLM-024 | TEST-LLM-001 | MLASWE-0006 |
| **AML.T0057** | LLM Data Leakage | 🟢 Full | LLM-003, LLM-008, LLM-009, LLM-014 | TEST-LLM-002 | MLASWE-0010 |
| **AML.T0053** | LLM Plugin Compromise | 🟢 Full | LLM-006, LLM-007, LLM-020, LLM-021, LLM-023 | TEST-LLM-001, TEST-LLM-003 | MLASWE-0011 |
| **AML.T0056** | ML Model Behavioral Manipulation | 🟢 Full | MODEL-013, INFRA-012, INFRA-014, INFRA-016, INFRA-017, INFRA-018, INFRA-022 | TEST-MODEL-003, TEST-INFRA-001, TEST-INFRA-004 | — |

## Coverage Statistics

| Metric | Count |
|--------|-------|
| **Total ATLAS techniques mapped** | 18 (covering 12 unique technique IDs + 6 tactic-level mappings) |
| 🟢 Full coverage | 13 (72%) |
| 🟡 Partial coverage | 4 (22%) |
| 🔴 No coverage | 1 (6%) |
| **Unique MLASVS controls referenced** | 68 of 168 (40%) |
| **Unique MLASTG test cases referenced** | 16 of 16 (100%) |
| **MLASWE weaknesses connected** | 9 of 12 (75%) |

## Notes on Methodology

- Only **official MITRE ATLAS technique IDs** are used. Where no official ID exists for a documented attack path, it is noted as "—" and tracked in the [Gap Analysis](3-Gap-Analysis.md).
- Tactic-level mappings (AML.TA####) indicate general coverage across multiple techniques under that tactic.
- Sub-techniques (AML.T0020.001, .002) are counted separately for precision.
