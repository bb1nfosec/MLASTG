# MLSec Application Security Testing Guide (MLASTG)

**Enterprise & Defense-Grade Security Testing for Machine Learning Systems**

> **Status:** Active Development — Version 0.1 (Draft)
> 
> [![Version](https://img.shields.io/badge/version-0.1--draft-orange)](https://github.com/bb1nfosec/MLASTG)
> [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
> [![Documentation](https://img.shields.io/badge/docs-live-green)](https://helloworld-three-blush.vercel.app/)

---

[![English](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-zh-red.svg)](README.zh-CN.md)

🌐 We welcome international contributors! Translations in progress.

---

## Overview

The **MLSec Application Security Testing Guide (MLASTG)** is a comprehensive, open-source framework for security testing machine learning (ML) systems across the full threat landscape — from traditional ML classifiers to deep neural networks and large language models (LLMs).

Inspired by the **[OWASP Mobile Application Security Testing Guide (MASTG)](https://github.com/OWASP/MASTG)** and aligned with **[MITRE ATLAS](https://atlas.mitre.org/)**, **[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)**, and **[OWASP AI Exchange](https://owaspai.org/)**, the MLASTG provides:

- **A Verification Standard (MLASVS)** — What to verify, organized by control category with L1 (Standard) and L2 (Defense-in-Depth) levels
- **A Testing Guide (MLASTG)** — How to test, with detailed step-by-step test cases mapped to controls
- **A Weakness Enumeration (MLASWE)** — Common security weaknesses specific to ML/LLM systems
- **Executable Test Scripts** — Python-based test harnesses using industry-standard tools (ART, SecML, etc.)

---

## Why MLASTG?

| Problem | MLASTG Solution |
|---------|----------------|
| ML security lacks a standardized, testable verification framework | MLASVS provides clear, verifiable controls mapped to MITRE ATLAS tactics |
| Existing guides are fragmented across OWASP, NIST, and vendor documents | Unified reference integrating all major frameworks with cross-references |
| Testing procedures for adversarial ML are poorly documented | Detailed step-by-step test cases with companion Python scripts |
| Enterprise/defense environments require defense-in-depth | Two-tier verification (L1 Standard / L2 Defense-in-Depth) |
| No SBOM/SCA standard exists for ML supply chains | ML-SBOM requirements and supply chain verification controls |

---

## Architecture

```
MLASVS (The Standard)          ─── What to verify
    │
    ├── Maps to ───► MITRE ATLAS Tactics & Techniques
    ├── Aligns to ──► NIST AI RMF, OWASP AI Exchange
    └── Referenced by ──► MLASWE Weakness IDs
            │
            ▼
MLASTG (The Testing Guide)     ─── How to test
    │
    ├── Test Cases ──► MLASTG-TEST-XXXX (step-by-step procedures)
    ├── Techniques ──► MLASTG-TECH-XXXX (tools & methods)
    └── Companion Scripts ──► tests/*.py (executable test harnesses)
            │
            ▼
MLASWE (Weakness Enumeration)  ─── What can go wrong
    │
    └── MLASWE-XXXX identifiers for each weakness class
```

---

## Control Categories

| Category | ID | Coverage | Controls L1 | Controls L2 |
|----------|----|----------|-------------|--------------|
| Data Security & Privacy | **MLASVS-DATA** | Provenance, sanitization, differential privacy, access controls | 18 | 12 |
| Model Security | **MLASVS-MODEL** | Adversarial robustness, extraction/inversion prevention, backdoor detection | 15 | 15 |
| LLM-Specific Security | **MLASVS-LLM** | Prompt injection, output handling, agency, context isolation | 14 | 10 |
| Supply Chain Security | **MLASVS-SUPPLY** | ML-SBOM, base model vetting, dependency scanning | 12 | 10 |
| Pipeline & MLOps | **MLASVS-PIPELINE** | CI/CD, feature stores, model registries, artifact integrity | 10 | 10 |
| Runtime & Infrastructure | **MLASVS-INFRA** | Serving security, API security, monitoring, incident response | 12 | 10 |
| Governance & Compliance | **MLASVS-GOV** | Risk governance, bias/fairness, audit logging, regulatory | 10 | 10 |

**Total Controls:** 91 L1 + 77 L2 = **168 verifiable controls**

---

## Testing Levels

### L1 — Standard Security
Baseline controls for all ML applications in production. Covers:
- Fundamental data protection and access controls
- Basic adversarial robustness validation
- Standard supply chain hygiene
- Essential monitoring and logging

### L2 — Defense-in-Depth  
Enhanced controls for high-risk, enterprise/defense, and regulated environments. Adds:
- Rigorous adversarial robustness certification
- Differential privacy guarantees
- Comprehensive red teaming
- Full ML-SBOM with provenance verification
- Continuous runtime monitoring with automated response

---

## Quick Start

### For Security Testers
1. Review the **MLASVS** to identify applicable controls
2. Use the **MLASTG Testing Methodology** to plan your assessment
3. Execute test cases mapped to your target controls
4. Reference **MLASWE** for weakness classification in findings
5. Run companion **test scripts** for automated validation

### For Organizations
1. Adopt **MLASVS** as your internal ML security standard
2. Map existing controls to MLASVS categories
3. Conduct gap analysis using the **MLASTG Checklist**
4. Implement missing controls with L1 as minimum

---

## Mapping to Industry Frameworks

| Framework | MLASTG Alignment |
|-----------|-----------------|
| MITRE ATLAS | Each MLASVS control maps to relevant MITRE ATLAS tactics/techniques |
| NIST AI RMF 1.0 | MLASVS controls support all four RMF functions (Govern, Map, Measure, Manage) |
| OWASP AI Exchange | Cross-referenced to OWASP AI threat/control matrices |
| OWASP LLM Top 10 | Full coverage of all 10 LLM risks as MLASVS-LLM controls |
| OWASP ML Top 10 | Coverage of all 10 ML security vulnerabilities |
| NSA/CISA AI Security Guidance | Controls aligned with secure deployment guidance |
| EU AI Act | MLASVS-GOV controls mapped to regulatory requirements |

### ATLAS Navigator

Visualize MLASTG coverage in the [MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/):

1. Download the [Navigator Layer JSON](docs/ATLAS-Mapping/2-atlas-navigator-layer.json)
2. Open the [MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/)
3. Click **Open Existing Layer** → **Upload from local** and select the downloaded JSON file
4. Coverage will be visualized as a heat map: 🟢 Full, 🟡 Partial, 🔴 None

---

## Project Structure

```
MLASTG/
├── README.md                    ← This file
├── mkdocs.yml                   ← Documentation site config
├── docs/
│   ├── index.md                 ← Home / Overview
│   ├── MLASVS/                  ← Verification Standard
│   │   ├── 0x00-Introduction.md
│   │   ├── 0x01-Using-This-Standard.md
│   │   ├── V1-DATA/             ← Data Security controls
│   │   ├── V2-MODEL/            ← Model Security controls
│   │   ├── V3-LLM/              ← LLM Security controls
│   │   ├── V4-SUPPLY/           ← Supply Chain controls
│   │   ├── V5-PIPELINE/         ← Pipeline controls
│   │   ├── V6-INFRA/            ← Runtime & Infra controls
│   │   └── V7-GOV/              ← Governance controls
│   ├── MLASTG/                  ← Testing Guide
│   │   ├── 0x00-Testing-Methodology.md
│   │   ├── 0x01-Testing-Tools.md
│   │   ├── DATA-Tests/          ← Data security tests
│   │   ├── MODEL-Tests/         ← Model security tests
│   │   ├── LLM-Tests/           ← LLM security tests
│   │   ├── SUPPLY-Tests/        ← Supply chain tests
│   │   ├── PIPELINE-Tests/      ← Pipeline tests
│   │   ├── INFRA-Tests/         ← Infra tests
│   │   └── GOV-Tests/           ← Governance tests
│   ├── MLASWE/                  ← Weakness Enumeration
│   └── assets/                  ← Images, diagrams
├── tests/                       ← Python test scripts
│   ├── data/                    ← Data security test harnesses
│   ├── model/                   ← Model security test harnesses
│   ├── llm/                     ← LLM security test harnesses
│   ├── supply/                  ← Supply chain test harnesses
│   ├── pipeline/                ← Pipeline test harnesses
│   ├── infra/                   ← Runtime test harnesses
│   └── gov/                     ← Governance assessment tools
└── demos/                       ← Example vulnerable models & apps
```

---

## Contributing

This project is in active development. Contributions are welcome across:
- New test cases and step-by-step procedures
- Python test script implementations (see `tests/` directory)
- LLM-specific testing methodologies and datasets
- Case studies and real-world attack demonstrations
- Translations and internationalization (see `docs/zh/` for Chinese)
- Coverage for additional MLASVS control categories

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

This work is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**.

---

## Acknowledgements

- **OWASP MASTG** — The inspiration and structural model for this project
- **MITRE ATLAS** — Adversarial threat taxonomy foundation
- **NIST AI RMF** — Risk management framework alignment
- **OWASP AI Exchange** — Cross-referenced threat and control matrices
- **IBM ART** — Adversarial robustness testing tools
- All contributors to the AI/ML security community
