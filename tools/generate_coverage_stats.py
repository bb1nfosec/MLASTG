#!/usr/bin/env python3
"""
Generate Coverage Statistics page from Navigator JSON data.

Reads docs/ATLAS-Mapping/2-atlas-navigator-layer.json and generates
docs/ATLAS-Mapping/5-Coverage-Statistics.md with accurate, up-to-date metrics.

Usage:
    python tools/generate_coverage_stats.py
    python tools/generate_coverage_stats.py --dry-run  # Print to stdout without writing
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
JSON_PATH = PROJECT_ROOT / "docs" / "ATLAS-Mapping" / "2-atlas-navigator-layer.json"
OUTPUT_PATH = PROJECT_ROOT / "docs" / "ATLAS-Mapping" / "5-Coverage-Statistics.md"

# ATLAS tactic ID → human-readable name
TACTIC_NAMES = {
    "TA0001": "Reconnaissance",
    "TA0002": "Initial Access",
    "TA0003": "Resource Development",
    "TA0005": "Execution",
    "TA0006": "Persistence",
    "TA0007": "Credential Access",
    "TA0008": "Evasion",
    "TA0009": "Discovery",
    "TA0010": "Collection",
    "TA0040": "Impact",
}

# Map technique number ranges to tactics (ATLAS ordering)
TECHNIQUE_TO_TACTIC = {
    "T0000": "TA0003",  # Resource Development
    "T0001": "TA0001",  # Reconnaissance
    "T0002": "TA0001",  # Reconnaissance
    "T0003": "TA0003",  # Resource Development
    "T0005": "TA0002",  # Initial Access
    "T0007": "TA0010",  # Collection
    "T0010": "TA0005",  # Execution
    "T0011": "TA0008",  # Evasion
    "T0012": "TA0006",  # Persistence
    "T0013": "TA0010",  # Collection
    "T0014": "TA0010",  # Collection
    "T0018": "TA0005",  # Execution
    "T0020": "TA0005",  # Execution
    "T0021": "TA0005",  # Execution
    "T0031": "TA0010",  # Collection
    "T0034": "TA0040",  # Impact (Denial of ML Service)
    "T0035": "TA0005",  # Execution
    "T0037": "TA0010",  # Collection
    "T0040": "TA0005",  # Execution (Establish Adversarial ML Infrastructure)
    "T0043": "TA0005",  # Execution
    "T0051": "TA0005",  # Execution (LLM)
    "T0052": "TA0005",  # Execution (LLM)
    "T0053": "TA0005",  # Execution (LLM)
    "T0054": "TA0005",  # Execution (LLM)
    "T0056": "TA0005",  # Execution (ML behavioral)
    "T0057": "TA0010",  # Collection (data exfil)
    "T0058": "TA0010",  # Collection (inversion)
    "T0059": "TA0006",  # Persistence (backdoor)
}

FULL_THRESHOLD = 80


def load_json() -> dict:
    with open(JSON_PATH) as f:
        return json.load(f)


def get_tactic(technique_id: str) -> str:
    """Derive tactic from technique ID."""
    parts = technique_id.split(".")
    base = parts[-1] if len(parts) > 1 else technique_id
    if base.startswith("AML."):
        base = base[4:]
    return TECHNIQUE_TO_TACTIC.get(base, "TA0005")


def classify(score: int) -> str:
    if score >= FULL_THRESHOLD:
        return "full"
    elif score > 0:
        return "partial"
    return "none"


def _parse_comment(comment: str) -> tuple:
    """Extract technique name, controls, and tests from comment field.
    
    Comment format: 'Technique Name - CONTROL-1, CONTROL-2 mapped'
    or 'Technique Name - CONTROL-1 partial'
    """
    if " - " in comment:
        name = comment.split(" - ")[0].strip()
        remainder = comment.split(" - ", 1)[1]
    else:
        name = comment
        remainder = ""
    
    # Extract control references (MLASVS-XXX or just XXX-NNN patterns)
    controls = []
    tests = []
    
    # Match patterns like SUPPLY-001, DATA-002, MODEL-003, LLM-004, INFRA-005, PIPELINE-006
    control_pattern = re.compile(r'\b(DATA|MODEL|LLM|INFRA|PIPELINE|SUPPLY|GOV)-\d{3}\b')
    for match in control_pattern.finditer(remainder):
        controls.append(match.group(0))
    
    # Match test references (TEST-XXX-NNN)
    test_pattern = re.compile(r'TEST-(DATA|MODEL|LLM|INFRA|PIPELINE|SUPPLY|GOV)-\d{3}\b')
    for match in test_pattern.finditer(remainder):
        tests.append(match.group(0))
    
    return name, controls, tests


def generate(data: dict) -> str:
    techniques = data["techniques"]
    now = datetime.utcnow().strftime("%Y-%m-%d")

    total = len(techniques)
    full = [t for t in techniques if classify(t["score"]) == "full"]
    partial = [t for t in techniques if classify(t["score"]) == "partial"]
    none = [t for t in techniques if classify(t["score"]) == "none"]
    avg_score = sum(t["score"] for t in techniques) / total if total else 0

    # Group by tactic
    tactic_groups = defaultdict(list)
    for t in techniques:
        tactic = get_tactic(t["techniqueID"])
        tactic_groups[tactic].append(t)

    # Build tactic table rows
    tactic_rows = []
    for tactic_id in sorted(tactic_groups.keys()):
        techs = tactic_groups[tactic_id]
        tactic_name = TACTIC_NAMES.get(tactic_id, tactic_id)
        f = sum(1 for t in techs if classify(t["score"]) == "full")
        p = sum(1 for t in techs if classify(t["score"]) == "partial")
        n = sum(1 for t in techs if classify(t["score"]) == "none")
        avg = sum(t["score"] for t in techs) / len(techs) if techs else 0
        tactic_rows.append(
            f"| {tactic_name} ({tactic_id}) | {len(techs)} | {f} | {p} | {n} | {avg:.0f}% |"
        )
    tactic_rows.append(
        f"| **Total** | **{total}** | **{len(full)}** | **{len(partial)}** | **{len(none)}** | **{avg_score:.1f}%** |"
    )

    # Build full coverage table
    full_rows = []
    for t in sorted(full, key=lambda x: x["techniqueID"]):
        name, controls, tests = _parse_comment(t["comment"])
        full_rows.append(
            f"| {t['techniqueID']} | {name} | {t['score']}% | {', '.join(controls) if controls else '—'} | {', '.join(tests) if tests else '—'} |"
        )

    # Build partial coverage table
    partial_rows = []
    for t in sorted(partial, key=lambda x: x["techniqueID"]):
        name, controls, _ = _parse_comment(t["comment"])
        partial_rows.append(
            f"| {t['techniqueID']} | {name} | {t['score']}% | {', '.join(controls) if controls else '—'} | Identified in [Gap Analysis](3-Gap-Analysis.md) |"
        )

    md = f"""# MLASTG ATLAS Coverage Statistics

> **Auto-generated** from `docs/ATLAS-Mapping/2-atlas-navigator-layer.json`.
> Generated: {now}
> ⚠️ Do not edit manually — run `python tools/generate_coverage_stats.py` to regenerate.

This page provides a quantitative summary of MLASTG's coverage of the MITRE ATLAS framework, derived automatically from the Navigator JSON data file.

---

## Aggregate Metrics

| Metric | Value |
|--------|-------|
| **Total ATLAS techniques mapped** | {total} |
| **Full coverage (score ≥ {FULL_THRESHOLD}%)** | {len(full)} ({len(full)*100//total}%) |
| **Partial coverage (0 < score < {FULL_THRESHOLD}%)** | {len(partial)} ({len(partial)*100//total}%) |
| **No coverage (score = 0)** | {len(none)} ({(len(none)*100/total if total else 0):.0f}%) |
| **Weighted coverage score** | {avg_score:.1f}% |

---

## Coverage by ATLAS Tactic

| Tactic | Techniques | Full | Partial | None | Avg Score |
|--------|-----------|------|---------|------|-----------|
{chr(10).join(tactic_rows)}

---

## Technique-Level Detail

### Full Coverage Techniques (Score ≥ {FULL_THRESHOLD}%)

| ATLAS ID | Technique | Score | MLASVS Controls | MLASTG Tests |
|----------|-----------|-------|-----------------|--------------|
{chr(10).join(full_rows)}

### Partial Coverage Techniques (Score < {FULL_THRESHOLD}%)

| ATLAS ID | Technique | Score | MLASVS Controls | Gap |
|----------|-----------|-------|-----------------|-----|
{chr(10).join(partial_rows)}

---

## Cross-Framework Alignment

| Framework | MLASTG Coverage | Notes |
|-----------|----------------|-------|
| MITRE ATLAS | {avg_score:.1f}% weighted | {len(full)}/{total} techniques full; {len(partial)} partial |
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
"""
    return md


def main():
    parser = argparse.ArgumentParser(
        description="Generate Coverage Statistics from Navigator JSON"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Print to stdout without writing"
    )
    args = parser.parse_args()

    if not JSON_PATH.exists():
        print(f"Error: {JSON_PATH} not found")
        sys.exit(1)

    data = load_json()
    md = generate(data)

    if args.dry_run:
        print(md)
    else:
        with open(OUTPUT_PATH, "w") as f:
            f.write(md)
        print(f"✅ Generated {OUTPUT_PATH}")
        print(f"   {len(data['techniques'])} techniques processed")


if __name__ == "__main__":
    main()
