---
title: "MLASVS Control Register"
hide:
  - navigation
  - toc
---

# MLASVS Control Register

A machine-readable register of all **168 MLASVS controls**, generated directly
from the standard's documentation. Each row links a control to its assurance
level, MITRE&nbsp;ATLAS technique, companion test case, the MLASWE weaknesses it
mitigates, and its framework alignment (NIST AI RMF, OWASP) — the full
control → ATLAS → test → weakness → framework traceability chain GRC tooling and
auditors need. Hover a framework tag for the specific reference. Filter by category or level, search, or
download the raw [`controls.json`](controls.json).

<div class="cr-summary">
  <div class="cr-stat"><b>168</b><span>Controls</span></div>
  <div class="cr-stat"><b>89</b><span>L1 — Standard</span></div>
  <div class="cr-stat"><b>79</b><span>L2 — Defense-in-Depth</span></div>
  <div class="cr-stat"><b>148</b><span>ATLAS-mapped</span></div>
</div>

<div id="cr-app" data-src="../controls.json" class="cr-app">
  <p class="cr-loading">Loading control register…</p>
</div>

!!! note "How this is generated"
    The register is produced by
    [`tools/generate_controls_register.py`](https://github.com/bb1nfosec/MLASTG/blob/master/tools/generate_controls_register.py),
    which extracts controls from the MLASVS pages (both block- and table-format
    definitions) into [`controls.json`](controls.json). Governance (GOV)
    controls are process/oversight controls and intentionally carry no ATLAS
    technique mapping. Levels reflect the source documentation.
