# Changelog

All notable changes to MLASTG are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Conformance self-assessment** — an interactive, client-side page to mark each
  of the 168 controls Pass/Fail/N-A, see live L1/L2 and per-category conformance
  scores, and export an evidence JSON (`mlastg-conformance.json`).
- **ML-SBOM worked example** (`demos/ml-sbom/`) — a validatable ML-SBOM in both
  MLASTG-native and CycloneDX 1.6 ML-BOM formats, checked in CI (must pass; an
  incomplete SBOM must fail). Added real `__main__` entrypoints to four harnesses
  whose CI `--demo` steps were previously silent no-ops.
- **Green CI on the working branch** — fixed `test-scripts.yml` (was `main`-only,
  so it never ran on `master`) and `mlastg-scan.yml` (was `pip install mlastg`
  from PyPI, plus a broken compliance-score parser). All 10 harness demos,
  pytest, and the full demo scan now pass in CI on every push.
- **Control → ATLAS → test → weakness traceability** — the control register now
  maps each control to the MLASWE weaknesses it mitigates (48 controls), and the
  register UI gained a Weakness column.
- **Machine-readable control register** — `tools/generate_controls_register.py`
  extracts all 168 controls (from both block- and table-format pages) into
  [`docs/MLASVS/controls.json`](docs/MLASVS/controls.json), surfaced through a
  filterable, searchable interactive Control Register page with control →
  level → ATLAS → test traceability.
- Interactive **ATLAS Coverage Map** — a periodic-table view of ML/LLM attack
  techniques grouped by MLASVS control family, with per-technique control
  mappings, coverage filtering, and search.
- Redesigned documentation landing page and dark-first theme.
- Expanded, enterprise-oriented `README.md` with CLI usage, CI/CD, reporting,
  and licensing detail.

### Changed
- **Reconciled MITRE ATLAS mappings against the official ATLAS taxonomy**
  (mitre-atlas/atlas-data). Corrected wrong technique IDs/names across the
  coverage map, Navigator layer, all MLASVS control pages, MLASTG test pages,
  ATLAS-Mapping narrative pages, and `controls.json`. The Navigator layer now
  exports valid IDs (26 techniques, 18 full / 8 partial).
- Corrected the live documentation URL across `README.md` and `README.zh-CN.md`.
- Removed placeholder author contact from `pyproject.toml`.

## [0.1.0] — 2026-06-27

### Added
- MLASVS verification standard: 168 controls across 7 categories (L1 / L2).
- MLASTG testing guide with step-by-step test cases per category.
- MLASWE weakness enumeration (13 weakness classes).
- `mlastg` automation CLI (`scan`, `report`) with JSON/Markdown reporting.
- Python test harnesses for all 7 categories, integrated with the orchestrator.
- MITRE ATLAS Navigator coverage layer and mapping pages.
- CI workflows: security scan, test scripts, docs publish, Vercel deploy,
  Navigator validation.

[Unreleased]: https://github.com/bb1nfosec/MLASTG/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/bb1nfosec/MLASTG/releases/tag/v0.1.0
