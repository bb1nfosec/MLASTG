# MLSec Application Security Testing Guide (MLASTG)

**Enterprise & Defense-Grade Security Testing for Machine Learning Systems**

> **Status:** Active Development — Version 0.1 (Draft)
>
> [![Version](https://img.shields.io/badge/version-0.1--draft-orange)](https://github.com/bb1nfosec/MLASTG)
> [![Docs License: CC BY-SA 4.0](https://img.shields.io/badge/docs-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
> [![Code License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](#license)
> [![Documentation](https://img.shields.io/badge/docs-live-green)](https://mlastg.vercel.app/)
> [![Docs Build](https://github.com/bb1nfosec/MLASTG/actions/workflows/mkdocs-publish.yml/badge.svg)](https://github.com/bb1nfosec/MLASTG/actions/workflows/mkdocs-publish.yml)
> [![Test Scripts](https://github.com/bb1nfosec/MLASTG/actions/workflows/test-scripts.yml/badge.svg)](https://github.com/bb1nfosec/MLASTG/actions/workflows/test-scripts.yml)

---

[![English](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![中文](https://img.shields.io/badge/lang-zh-red.svg)](README.zh-CN.md)

🌐 We welcome international contributors! Translations in progress.

**📖 Live documentation: [mlastg.vercel.app](https://mlastg.vercel.app/) — including the interactive [ATLAS Coverage Map](https://mlastg.vercel.app/ATLAS-Mapping/2-Coverage-Map/).**

---

## Contents

- [Overview](#overview)
- [Why MLASTG?](#why-mlastg)
- [Architecture](#architecture)
- [Control Categories](#control-categories)
- [Assurance Levels](#assurance-levels)
- [Threat Coverage — MITRE ATLAS](#threat-coverage--mitre-atlas)
- [Automated Testing — the `mlastg` CLI](#automated-testing--the-mlastg-cli)
- [Continuous Assurance (CI/CD)](#continuous-assurance-cicd)
- [Reporting & Compliance](#reporting--compliance)
- [Quick Start](#quick-start)
- [Framework Alignment](#framework-alignment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **MLSec Application Security Testing Guide (MLASTG)** is a comprehensive, open-source framework for security testing machine learning (ML) systems across the full threat landscape — from traditional ML classifiers to deep neural networks and large language models (LLMs).

Inspired by the **[OWASP Mobile Application Security Testing Guide (MASTG)](https://github.com/OWASP/MASTG)** and aligned with **[MITRE ATLAS](https://atlas.mitre.org/)**, **[NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)**, and **[OWASP AI Exchange](https://owaspai.org/)**, MLASTG provides four tightly-coupled layers:

- **A Verification Standard (MLASVS)** — *What to verify*, organized by control category with L1 (Standard) and L2 (Defense-in-Depth) assurance levels.
- **A Testing Guide (MLASTG)** — *How to test*, with detailed step-by-step test cases mapped to controls.
- **A Weakness Enumeration (MLASWE)** — *What can go wrong*, a common taxonomy of ML/LLM weaknesses for classifying findings.
- **Executable Test Scripts + CLI** — *Automated validation*, Python harnesses orchestrated by the `mlastg` command-line scanner.

Designed for **enterprise and defense-grade** environments: every control is testable, mapped to recognized frameworks, and assignable to an assurance tier so security programs can demonstrate measurable, audit-ready coverage of the ML attack surface.

---

## Why MLASTG?

| Problem | MLASTG Solution |
|---------|----------------|
| ML security lacks a standardized, testable verification framework | MLASVS provides clear, verifiable controls mapped to MITRE ATLAS tactics |
| Existing guidance is fragmented across OWASP, NIST, and vendor documents | A unified reference integrating all major frameworks with cross-references |
| Testing procedures for adversarial ML are poorly documented | Detailed step-by-step test cases with companion Python scripts |
| Enterprise/defense environments require defense-in-depth | Two-tier verification (L1 Standard / L2 Defense-in-Depth) |
| No SBOM/SCA standard exists for ML supply chains | ML-SBOM requirements and supply-chain verification controls |
| Coverage is hard to prove to auditors and leadership | A MITRE ATLAS coverage map and exportable JSON/Markdown assessment reports |

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
    └── Companion Scripts ──► tests/*.py (executable harnesses)
            │
            ▼
mlastg CLI (Automation)        ─── Run, score, and report
    │
    └── mlastg scan ──► orchestrates harnesses ──► JSON + Markdown reports
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

## Assurance Levels

### L1 — Standard Security
Baseline controls for all ML applications in production:
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

## Threat Coverage — MITRE ATLAS

Every MLASVS control is mapped to the **[MITRE ATLAS](https://atlas.mitre.org/)** adversarial-threat taxonomy. The mapping is published two ways:

- **Interactive [ATLAS Coverage Map](https://mlastg.vercel.app/ATLAS-Mapping/2-Coverage-Map/)** — a periodic-table view of ML/LLM attack techniques, arranged by the MLASVS control family that covers them, with per-technique control mappings.
- **Importable Navigator layer** — load [`2-atlas-navigator-layer.json`](docs/ATLAS-Mapping/2-atlas-navigator-layer.json) into the [MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/) (**Open Existing Layer → Upload from local**) to view coverage as a heat map.

| Coverage | Techniques | Meaning |
|----------|:---------:|---------|
| 🟢 Full | 18 | MLASVS controls **and** MLASTG test cases exist |
| 🟡 Partial | 8 | Some controls mapped; gaps remain |
| **Total mapped** | **26** | **≈69% fully covered** |

> Technique IDs and names are reconciled against the official
> [MITRE ATLAS data](https://github.com/mitre-atlas/atlas-data).

See the [Coverage Matrix](docs/ATLAS-Mapping/1-Coverage-Matrix.md) and [Gap Analysis](docs/ATLAS-Mapping/3-Gap-Analysis.md) for the narrative breakdown.

### Control Register (traceability)

All 168 controls are also published as a machine-readable register —
[`controls.json`](docs/MLASVS/controls.json) — with an interactive
[Control Register](https://mlastg.vercel.app/MLASVS/Control-Register/) that maps
each control to its assurance level, MITRE ATLAS reference, and companion test
case. It is regenerated from the documentation by
[`tools/generate_controls_register.py`](tools/generate_controls_register.py),
so the catalog never drifts from the standard.

---

## Automated Testing — the `mlastg` CLI

`mlastg` is a [Click](https://click.palletsprojects.com/)-based command-line scanner (with [Rich](https://rich.readthedocs.io/) output) that orchestrates the category test harnesses and produces assessment reports.

### Install

```bash
# Core CLI
pip install -e .

# Optional: testing harness dependencies (ART, scikit-learn, torch, giskard, …)
pip install -e ".[tests]"
```

### Run a scan

```bash
# Scan a live LLM endpoint for LLM-category weaknesses
mlastg scan --target https://api.example.com/v1/chat --category llm

# Scan a local model artifact for model-category weaknesses
mlastg scan --target ./models/classifier.pkl --category model

# Dry-run everything with local stubs (no external calls)
mlastg scan --target demo --category all --demo
```

| Option | Values | Default | Purpose |
|--------|--------|---------|---------|
| `--target` | URL · API endpoint · local path | *(required)* | System under test |
| `--category` | `model` · `llm` · `data` · `supply` · `infra` · `pipeline` · `gov` · `all` | `all` | Test category to execute |
| `--demo` | flag | off | Use local stubs instead of real calls |
| `--output` | path | `mlastg_report.json` | Raw JSON results |
| `--format` | `json` · `markdown` · `both` | `both` | Report format(s) |

### Generate a report from existing results

```bash
mlastg report --input mlastg_report.json --output mlastg_report.md
```

> **Safe by default:** `--demo` runs against local stubs so you can validate the pipeline without touching production systems. Only scan targets you are authorized to test.

---

## Continuous Assurance (CI/CD)

MLASTG ships GitHub Actions workflows so assurance runs on every change:

| Workflow | Purpose |
|----------|---------|
| `mlastg-scan.yml` | Runs the `mlastg` scanner (demo mode) as a CI gate |
| `test-scripts.yml` | Executes the Python test harnesses |
| `mkdocs-publish.yml` | Builds and publishes the documentation site |
| `deploy-vercel.yml` | Deploys the docs to Vercel |
| `deploy-navigator.yml` | Validates and publishes the ATLAS Navigator layer |

---

## Reporting & Compliance

The CLI emits both machine- and human-readable artifacts:

- **`mlastg_report.json`** — structured results for pipelines, dashboards, and ticketing.
- **`mlastg_report.md`** — a Markdown compliance report suitable for audit evidence.

Findings reference **MLASWE** weakness IDs and the **MLASVS** controls they violate, so results map cleanly back to MITRE ATLAS, NIST AI RMF, the OWASP AI/LLM/ML Top 10s, and the EU AI Act for governance reporting.

---

## Quick Start

### For Security Testers
1. Review the **MLASVS** to identify applicable controls.
2. Use the **MLASTG Testing Methodology** to plan your assessment.
3. Execute test cases mapped to your target controls (manually or via `mlastg scan`).
4. Reference **MLASWE** for weakness classification in findings.
5. Export JSON/Markdown reports for evidence.

### For Organizations
1. Adopt **MLASVS** as your internal ML security standard.
2. Map existing controls to MLASVS categories.
3. Conduct gap analysis using the **MLASTG Checklist** and the **ATLAS Coverage Map**.
4. Implement missing controls with L1 as a minimum and L2 for high-risk systems.
5. Wire `mlastg scan` into CI to keep coverage from regressing.

---

## Framework Alignment

| Framework | MLASTG Alignment |
|-----------|-----------------|
| MITRE ATLAS | Each MLASVS control maps to relevant ATLAS tactics/techniques |
| NIST AI RMF 1.0 | Controls support all four RMF functions (Govern, Map, Measure, Manage) |
| OWASP AI Exchange | Cross-referenced to OWASP AI threat/control matrices |
| OWASP LLM Top 10 | Full coverage of all 10 LLM risks as MLASVS-LLM controls |
| OWASP ML Top 10 | Coverage of all 10 ML security vulnerabilities |
| NSA/CISA AI Security Guidance | Controls aligned with secure deployment guidance |
| EU AI Act | MLASVS-GOV controls mapped to regulatory requirements |

---

## Project Structure

```
MLASTG/
├── README.md                    ← This file
├── mkdocs.yml                   ← Documentation site config
├── pyproject.toml               ← mlastg CLI package definition
├── mlastg_cli/                  ← Automated testing CLI
│   ├── main.py                  ← Click entrypoint (scan, report)
│   ├── orchestrator.py          ← Runs the category test suites
│   └── reporter.py              ← JSON / Markdown report generation
├── docs/
│   ├── index.md                 ← Home / landing page
│   ├── MLASVS/                  ← Verification Standard (V1–V7)
│   ├── MLASTG/                  ← Testing Guide (per-category tests)
│   ├── MLASWE/                  ← Weakness Enumeration
│   ├── ATLAS-Mapping/           ← Coverage map, matrix, gap analysis, Navigator layer
│   ├── stylesheets/ javascripts/← Custom theme + interactive UI
│   └── assets/                  ← Images, diagrams
├── tests/                       ← Python test harnesses (data, model, llm, supply, pipeline, infra, gov)
├── demos/                       ← Example vulnerable models & apps
└── .github/workflows/           ← CI: scan, tests, docs, deploy, navigator
```

---

## Maturity & Roadmap

MLASTG is at **v0.1** and honest about what that means. The framework skeleton,
control catalog, test procedures, automation CLI, and ATLAS coverage map are
implemented and usable today; the items below are tracked for production
hardening. See [CHANGELOG.md](CHANGELOG.md) for release history.

| Area | Status | Notes |
|------|:------:|-------|
| MLASVS standard (168 controls, 7 categories) | ✅ Implemented | Documented with L1/L2 levels |
| MLASTG test procedures | ✅ Implemented | Step-by-step, pass/fail criteria |
| `mlastg` CLI + Python harnesses | ✅ Implemented | Real ART-based harnesses; `--demo` stubs for safe CI |
| MITRE ATLAS coverage map | ✅ Reconciled | 26 techniques; IDs/names verified against official ATLAS data across the coverage map, Navigator layer, control docs, and register. zh translations pending |
| Expanded ATLAS coverage (beyond 26 techniques) | 🟡 In progress | Mapping additional ATLAS techniques to controls |
| Machine-readable control register (JSON) | ✅ Implemented | [`controls.json`](docs/MLASVS/controls.json) + interactive [register](https://mlastg.vercel.app/MLASVS/Control-Register/); generated from the docs |
| End-to-end reference run (sample model + fixtures) | ⬜ Planned | A reproducible green-path example |
| Independent review / release tags | ⬜ Planned | Versioned releases and external review |

> **Adoption guidance:** today MLASTG is best used as a **reference standard,
> checklist, and automation accelerator** to structure an ML security program.
> Treat the ATLAS technique IDs as v0.1 mappings pending reconciliation, and
> validate controls against your own threat model before certification.

---

## Contributing

This project is in active development. Contributions are welcome across:
- New test cases and step-by-step procedures
- Python test-script implementations (see `tests/`) and CLI orchestrator coverage
- LLM-specific testing methodologies and datasets
- Case studies and real-world attack demonstrations
- Translations and internationalization (see `docs/zh/` for Chinese)
- Additional MLASVS control categories and ATLAS mappings

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) for guidelines, and [SECURITY.md](SECURITY.md) for responsible disclosure.

---

## License

MLASTG is **dual-licensed** so it fits cleanly into both documentation and engineering pipelines:

- **Documentation, standard, and guidance content** — [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE).
- **Code** (the `mlastg` CLI, test harnesses, and tooling) — **MIT License**.

---

## Acknowledgements

- **OWASP MASTG** — The inspiration and structural model for this project
- **MITRE ATLAS** — Adversarial threat taxonomy foundation
- **NIST AI RMF** — Risk management framework alignment
- **OWASP AI Exchange** — Cross-referenced threat and control matrices
- **IBM ART** — Adversarial robustness testing tools
- All contributors to the AI/ML security community
