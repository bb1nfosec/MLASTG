---
title: "MLASVS Conformance Self-Assessment"
hide:
  - navigation
  - toc
---

# Conformance Self-Assessment

Assess your system against the **168 MLASVS controls** and get a live
conformance score per assurance level. Mark each control **Pass**, **Fail**, or
**N/A** — your selections are saved in this browser and never leave it. When
you're done, **export the results JSON** as audit evidence.

Scoring excludes controls marked N/A from the denominator. A level is
**conformant** when every applicable control passes with none left unassessed.

<div id="cf-app" data-src="../controls.json" class="cf-app">
  <p class="cr-loading">Loading controls…</p>
</div>

!!! note "Privacy & evidence"
    This is a fully client-side tool — nothing is uploaded. The exported
    `mlastg-conformance.json` records each control's status plus L1/L2 scores,
    suitable for attaching to an assessment report. Pair it with the
    [Control Register](Control-Register.md) and `mlastg scan` output for a
    complete evidence package.
