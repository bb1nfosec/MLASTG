# MLASTG → MITRE ATLAS Coverage Mapping

## Overview
This directory contains the complete mapping between the **MLASTG framework** (MLASVS controls + MLASTG test cases) and **MITRE ATLAS™** adversarial techniques. All technique IDs are verified against the official MITRE ATLAS taxonomy.

## Deliverables

| File | Format | Purpose |
|------|--------|---------|
| [Coverage Matrix](1-Coverage-Matrix.md) | Markdown table | Every ATLAS technique mapped to MLASVS controls with coverage rating |
| [Navigator Layer](2-atlas-navigator-layer.json) | JSON (Navigator format) | Import into MITRE ATLAS Navigator for visual heat map |
| [Gap Analysis](3-Gap-Analysis.md) | Markdown | Unprotected attack paths needing new controls |
| [Coverage Dashboard](4-Coverage-Dashboard.md) | Markdown | Summary statistics, coverage %, key findings |

## Coverage Rating System

| Rating | Meaning | Color | Criteria |
|--------|---------|-------|----------|
| **Full** | Fully covered | 🟢 Green | L1 + L2 controls exist with test cases |
| **Partial** | Partially covered | 🟡 Yellow | L1 controls exist, L2 or tests missing |
| **None** | No coverage | 🔴 Red | No MLASVS control for this attack path |

## Coverage Summary

| Metric | Value |
|--------|-------|
| **Total ATLAS techniques mapped** | 18 (12 technique IDs + 6 tactic-level) |
| 🟢 Full coverage | 13 (72%) |
| 🟡 Partial coverage | 4 (22%) |
| 🔴 No coverage | 1 (6%) |
| **Unique MLASVS controls** | 64 of 168 (38% coverage density) |
| **ATLAS Navigator techniques** | 10 technique IDs with scores |

## ATLAS Navigator Import

To visualize coverage in the MITRE ATLAS Navigator:
1. Download [`2-atlas-navigator-layer.json`](2-atlas-navigator-layer.json)
2. Open [MITRE ATLAS Navigator](https://mitre-attack.github.io/atlas-navigator/)
3. Click **Layer Controls** → **Import Layer** → select the JSON file
4. Coverage will appear as a heat map (green = full, yellow = partial, red = none)

## Notes
- Only **official MITRE ATLAS technique IDs** are included. Attack paths without official IDs use "—" and are tracked in the Gap Analysis.
- Tactic-level mappings (AML.TA####) indicate general coverage across techniques under that tactic.
- Sub-techniques (AML.T0020.001, .002) are counted separately.
