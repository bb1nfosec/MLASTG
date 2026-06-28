---
title: "ATLAS Coverage Map — Interactive Matrix"
hide:
  - navigation
  - toc
---

# ATLAS Coverage Map

A periodic table of the ML/LLM attack techniques in the MLASTG threat model,
arranged by the **MLASVS control family** that covers them. Each tile is a
MITRE&nbsp;ATLAS technique; colour shows how completely MLASTG controls and
test cases address it. Select a tile to see its mapped controls.

<div class="atlas-stats">
  <div class="atlas-stat"><b>27</b><span>Techniques mapped</span></div>
  <div class="atlas-stat atlas-stat--full"><b>17</b><span>Full coverage</span></div>
  <div class="atlas-stat atlas-stat--partial"><b>10</b><span>Partial coverage</span></div>
  <div class="atlas-stat"><b>63%</b><span>Fully covered</span></div>
</div>

<div class="atlas-board">
  <div class="atlas-controls">
    <div id="atlas-toolbar" class="atlas-filters" role="group" aria-label="Filter techniques by coverage">
      <button type="button" data-filter="all" class="is-on">All</button>
      <button type="button" data-filter="full">Full</button>
      <button type="button" data-filter="partial">Partial</button>
    </div>
    <input id="atlas-search" class="atlas-search" type="search" placeholder="Search techniques…" aria-label="Search techniques">
  </div>

  <div class="atlas-layout">
    <div id="atlas-matrix" class="atlas-matrix" aria-label="ATLAS technique coverage matrix"></div>
    <aside id="atlas-detail" class="atlas-detail" aria-live="polite">
      <p class="atlas-detail__hint">Select a technique tile to inspect its mapped MLASVS controls.</p>
    </aside>
  </div>

  <div class="atlas-legend">
    <span><i class="atlas-dot atlas-dot--full"></i> Full coverage — controls and test cases exist</span>
    <span><i class="atlas-dot atlas-dot--partial"></i> Partial coverage — some controls, gaps remain</span>
  </div>
</div>

!!! tip "Open in the official MITRE ATLAS Navigator"
    Download the [Navigator layer JSON](2-atlas-navigator-layer.json), open the
    [MITRE ATLAS Navigator](https://mitre-atlas.github.io/atlas-navigator/),
    choose **Open Existing Layer → Upload from local**, and select the file to
    explore this coverage as a heat map over the full ATLAS matrix.

For the narrative breakdown and gaps, see the
[Coverage Matrix](1-Coverage-Matrix.md) and [Gap Analysis](3-Gap-Analysis.md).
