# MLASTG ATLAS Coverage Statistics

> **Auto-generated** from `docs/ATLAS-Mapping/2-atlas-navigator-layer.json`.
> Generated: 2026-06-26
> ⚠️ Do not edit manually — run `python tools/generate_coverage_stats.py` to regenerate.

This page provides a quantitative summary of MLASTG's coverage of the MITRE ATLAS framework, derived automatically from the Navigator JSON data file.

---

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| **Total ATLAS techniques mapped** | 28 |
| **Full coverage (score ≥ 80%)** | 19 (67%) |
| **Partial coverage (0 < score < 80%)** | 9 (32%) |
| **No coverage (score = 0)** | 0 (0%) |
| **Weighted coverage score** | 83.9% |

---

## Coverage by ATLAS Tactic

| Tactic | Techniques | Full | Partial | None | Avg Score |
|--------|-----------|------|---------|------|-----------|
| Reconnaissance (TA0001) | 2 | 1 | 1 | 0 | 75% |
| Initial Access (TA0002) | 1 | 0 | 1 | 0 | 50% |
| Resource Development (TA0003) | 2 | 2 | 0 | 0 | 100% |
| Execution (TA0005) | 12 | 8 | 4 | 0 | 83% |
| Persistence (TA0006) | 2 | 2 | 0 | 0 | 100% |
| Evasion (TA0008) | 1 | 1 | 0 | 0 | 100% |
| Collection (TA0010) | 7 | 5 | 2 | 0 | 86% |
| Impact (TA0040) | 1 | 0 | 1 | 0 | 50% |
| **Total** | **28** | **19** | **9** | **0** | **83.9%** |

---

## Technique-Level Detail

### Full Coverage Techniques (Score ≥ 80%)

| ATLAS ID | Technique | Score | MLASVS Controls | MLASTG Tests |
|----------|-----------|-------|-----------------|--------------|
| AML.T0000 | ML Attack Staging | 100% | PIPELINE-001 | — |
| AML.T0001 | Search for Tainted ML Data | 100% | DATA-001 | — |
| AML.T0003 | Compromise ML Supply Chain | 100% | SUPPLY-001, SUPPLY-002 | — |
| AML.T0043 | ML Model Inversion Attack | 100% | MODEL-003 | — |
| AML.T0010 | Exploit ML Model | 100% | MODEL-001, MODEL-002 | — |
| AML.T0015 | Evade ML Model | 100% | MODEL-001, MODEL-002 | — |
| AML.T0012 | Backdoor ML Model | 100% | MODEL-004, MODEL-005 | — |
| AML.T0024.002 | Extract ML Model | 100% | MODEL-002, MODEL-003 | — |
| AML.T0014 | Invert ML Model | 100% | MODEL-003 | — |
| AML.T0020 | Poison Training Data | 100% | DATA-001, DATA-002 | — |
| AML.T0035 | Erode ML Model Integrity | 100% | MODEL-004, MODEL-005 | — |
| AML.T0029 | ML Model Extraction | 100% | MODEL-002 | — |
| AML.T0043 | Exploit Adversarial ML Vulnerability | 100% | MODEL-001 | — |
| AML.T0051 | LLM Prompt Injection | 100% | LLM-001, LLM-004 | — |
| AML.T0057 | LLM Output Handling | 100% | LLM-002 | — |
| AML.T0054 | LLM Jailbreak | 100% | LLM-005 | — |
| AML.T0056 | ML Model Behavioral Manipulation | 100% | MODEL-004, INFRA-012, INFRA-018 | — |
| AML.T0058 | ML Model Inversion Attack | 100% | MODEL-003 | — |
| AML.T0059 | Backdoor ML Model | 100% | MODEL-004, DATA-001 | — |

### Partial Coverage Techniques (Score < 80%)

| ATLAS ID | Technique | Score | MLASVS Controls | Gap |
|----------|-----------|-------|-----------------|-----|
| AML.T0002 | Obtain ML Model from Public Source | 50% | SUPPLY-002 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0005 | Exploit ML Model for Initial Access | 50% | MODEL-001 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0018 | Poison Training Data | 50% | DATA-001, DATA-002 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0021 | Clean Training Data | 50% | DATA-002 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0031 | Exfiltration via ML Inference | 50% | LLM-002 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0024.002 | Denial of ML Service | 50% | LLM-010 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0040 | Establish Adversarial ML Infrastructure | 50% | INFRA-001 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0053 | LLM Plugin Compromise | 50% | LLM-006, LLM-007 | Identified in [Gap Analysis](3-Gap-Analysis.md) |
| AML.T0057 | ML Model Data Exfiltration | 50% | MODEL-003 | Identified in [Gap Analysis](3-Gap-Analysis.md) |

---

## Cross-Framework Alignment

| Framework | MLASTG Coverage | Notes |
|-----------|----------------|-------|
| MITRE ATLAS | 83.9% weighted | 19/28 techniques full; 9 partial |
| OWASP LLM Top 10 | 10/10 | Complete coverage |
| OWASP ML Top 10 | 10/10 | Complete coverage |
| NIST AI RMF | All 4 functions | Govern, Map, Measure, Manage |
| EU AI Act | GOV controls mapped | High-risk categories addressed |
| ISO/IEC 42001 | Partial | AI Management System alignment |

---

## Regenerating This Page

```bash
# Auto-generate from Navigator JSON
python tools/generate_coverage_stats.py

# Dry-run (print to stdout)
python tools/generate_coverage_stats.py --dry-run

# Build site
mkdocs build
```

---

## References

- [MITRE ATLAS](https://atlas.mitre.org/) — Adversarial Threat Landscape for AI Systems
- [Coverage Matrix](1-Coverage-Matrix.md) — Full technique-to-control mapping
- [Gap Analysis](3-Gap-Analysis.md) — Detailed remediation roadmap
- [Interactive Navigator](../assets/atlas-navigator.html) — Searchable technique explorer
