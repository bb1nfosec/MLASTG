# Changelog

All notable changes to MLASTG are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project aims to follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- Interactive **ATLAS Coverage Map** — a periodic-table view of ML/LLM attack
  techniques grouped by MLASVS control family, with per-technique control
  mappings, coverage filtering, and search.
- Redesigned documentation landing page and dark-first theme.
- Expanded, enterprise-oriented `README.md` with CLI usage, CI/CD, reporting,
  and licensing detail.

### Changed
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
