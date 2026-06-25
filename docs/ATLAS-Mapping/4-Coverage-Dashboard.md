# MLASTG → ATLAS Coverage Dashboard

> **Generated:** v0.1 (Draft) — Data from corrected matrix with verified ATLAS IDs

## Overall Coverage

```
                              ⬤⬤⬤⬤⬤⬤⬤⬤⬤⬤⬤⬤⬤ 72% Full
                              ⬤⬤⬤⬤ 22% Partial  
                              ⬤ 6% None
```

| Metric | Value |
|--------|-------|
| **Total ATLAS techniques** | 18 |
| **Full coverage** | 13 (72.2%) |
| **Partial coverage** | 4 (22.2%) |
| **No coverage** | 1 (5.6%) |
| **MLASVS controls mapped** | 64 unique controls |
| **MLASTG test cases mapped** | 12 test cases |
| **MLASWE weaknesses connected** | 9 weaknesses |

## Coverage by Tactic

| Tactic | Techniques | Full | Partial | None |
|--------|-----------|------|---------|------|
| Reconnaissance (TA0001) | 1 | 0 | 0 | 1 |
| Resource Development (TA0003) | 2 | 1 | 1 | 0 |
| Initial Access (TA0002) | 4 | 3 | 1 | 0 |
| Execution (TA0005) | 2 | 2 | 0 | 0 |
| Persistence (TA0006) | 2 | 2 | 0 | 0 |
| Credential Access (TA0007) | 1 | 1 | 0 | 0 |
| Discovery (TA0009) | 2 | 2 | 0 | 0 |
| Collection (TA0010) | 2 | 1 | 1 | 0 |
| **ML-specific techniques** | **10** | **8** | **2** | **0** |
| — ML Attack/Evasion | 1 | 1 | 0 | 0 |
| — Adversarial Perturbation | 1 | 1 | 0 | 0 |
| — Model Inversion | 1 | 0 | 1 | 0 |
| — Data Poisoning (+ sub) | 3 | 0 | 3 | 0 |
| — Model Extraction | 1 | 1 | 0 | 0 |
| — Model DoS | 1 | 1 | 0 | 0 |
| — LLM Prompt Injection | 1 | 1 | 0 | 0 |
| — LLM Data Leakage | 1 | 1 | 0 | 0 |
| — LLM Plugin Compromise | 1 | 1 | 0 | 0 |
| — ML Behavioral Manipulation | 1 | 1 | 0 | 0 |

## Control Density Heat Map

| ATLAS ID | Technique | Controls | Density |
|----------|-----------|----------|---------|
| AML.T0010 | Adversarial Perturbation | 10 controls | 🔥 High |
| AML.T0037 | Model DoS | 6 controls | 🔥 High |
| AML.T0051 | LLM Prompt Injection | 8 controls | 🔥 High |
| AML.T0034 | Model Extraction | 6 controls | 🔥 High |
| AML.T0053 | LLM Plugin Compromise | 5 controls | 🔥 Medium |
| AML.T0020 | Data Poisoning | 5 controls | 🔥 Medium |
| AML.T0052 | LLM Data Leakage | 4 controls | 🔥 Medium |
| AML.T0018 | Model Inversion | 3 controls | ⚡ Low |
| AML.T0007 | Input Manipulation | 2 controls | ⚡ Low |
| AML.T0056 | ML Behavioral Manipulation | 4 controls | 🔥 Medium |
| — | ML Model Discovery (TA0001) | 0 controls | ❌ None |

## Cross-Framework Alignment

| Framework | MLASTG Coverage | Status |
|-----------|----------------|--------|
| MITRE ATLAS | 72% Full, 22% Partial, 6% None | 🟢 Strong |
| OWASP LLM Top 10 | 10/10 fully covered | 🟢 Complete |
| OWASP ML Top 10 | 10/10 fully covered | 🟢 Complete |
| NIST AI RMF | All 4 functions covered | 🟢 Complete |
| EU AI Act | GOV controls mapped | 🟡 In progress |

## Recommendations

### Next release (v0.2)
1. Add **Reconnaissance detection** control — currently the only zero-coverage area
2. Upgrade **Data Poisoning** to Full coverage with L1 automated detection tests

### Medium-term
1. Add L1 controls for **Model Inversion** (e.g., output confidence rounding)
2. Extend coverage to multimodal ML attacks (vision-language models)
3. Add **Reinforcement Learning** controls (reward poisoning scenarios)
