#!/usr/bin/env python3
"""
Generate a machine-readable MLASVS control register from the documentation.

Extracts every control that is fully defined in docs/MLASVS as a
`### <ID>: <Title> (<Level>)` block, captures its metadata (description,
MITRE ATLAS technique, OWASP reference, test reference, source page), and
records the full universe of referenced control IDs so documentation
completeness can be reported honestly.

Outputs:
  docs/MLASVS/controls.json   — structured register + summary

Run:  python3 tools/generate_controls_register.py
"""
from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MLASVS = ROOT / "docs" / "MLASVS"
OUT = MLASVS / "controls.json"

CATEGORIES = {
    "DATA": "Data Security & Privacy",
    "MODEL": "Model Security",
    "LLM": "LLM-Specific Security",
    "SUPPLY": "Supply Chain Security",
    "PIPELINE": "Pipeline & MLOps",
    "INFRA": "Runtime & Infrastructure",
    "GOV": "Governance & Compliance",
}
CAT_RE = "|".join(CATEGORIES)

HEADING_RE = re.compile(
    r"^###\s+(?P<id>(?:%s)-\d{3}):\s*(?P<title>.+?)\s*\((?P<level>L[12])\)\s*$" % CAT_RE
)
REF_RE = re.compile(r"\b(?:%s)-\d{3}\b" % CAT_RE)


def field(block: str, label: str) -> str | None:
    m = re.search(r"\*\*%s:?\*\*\s*(.+)" % re.escape(label), block)
    return m.group(1).strip() if m else None


def first_atlas(text: str | None) -> str | None:
    """Match either a technique (AML.T0051) or a tactic (AML.TA0005)."""
    if not text:
        return None
    m = re.search(r"AML\.TA?\d{4}(?:\.\d{3})?", text)
    return m.group(0) if m else None


def _make(cid, title, level, desc, atlas_raw, owasp, test, rel, fmt):
    return {
        "id": cid,
        "category": cid.split("-")[0],
        "category_name": CATEGORIES[cid.split("-")[0]],
        "title": (title or "").strip() or None,
        "level": level,
        "description": (desc or "").strip() or None,
        "atlas": first_atlas(atlas_raw),
        "atlas_raw": (atlas_raw or "").strip() or None,
        "owasp": owasp,
        "test": (test or "").strip() or None,
        "mlaswe": [],
        "source": rel,
        "format": fmt,
    }


def parse_blocks(lines: list[str], rel: str) -> list[dict]:
    out: list[dict] = []
    i = 0
    while i < len(lines):
        m = HEADING_RE.match(lines[i])
        if not m:
            i += 1
            continue
        j = i + 1
        body: list[str] = []
        while j < len(lines) and not re.match(r"^#{2,3}\s", lines[j]):
            body.append(lines[j])
            j += 1
        block = "\n".join(body)
        out.append(
            _make(
                m.group("id"),
                m.group("title"),
                m.group("level"),
                field(block, "Description"),
                field(block, "MITRE ATLAS"),
                field(block, "OWASP LLM Top 10") or field(block, "OWASP ML Top 10"),
                field(block, "Test Reference"),
                rel,
                "block",
            )
        )
        i = j
    return out


def parse_tables(lines: list[str], rel: str) -> list[dict]:
    """Parse markdown control tables; map columns by their header names."""
    out: list[dict] = []
    i = 0
    while i < len(lines):
        row = lines[i].strip()
        if row.startswith("|") and re.search(r"\|\s*ID\s*\|", row, re.I) and "level" in row.lower():
            headers = [h.strip().lower() for h in row.strip("|").split("|")]
            col = {h: k for k, h in enumerate(headers)}
            i += 2  # skip header + separator
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                i += 1
                if len(cells) < len(headers):
                    continue

                def g(*names):
                    for n in names:
                        for h, k in col.items():
                            if n in h and k < len(cells):
                                return cells[k]
                    return None

                cid = g("id")
                if not cid or not re.fullmatch(r"(?:%s)-\d{3}" % CAT_RE, cid or ""):
                    continue
                lvl = (g("level") or "").upper()
                lvl = "L2" if "L2" in lvl else "L1"
                out.append(
                    _make(
                        cid,
                        g("control", "name", "title"),
                        lvl,
                        g("description", "requirement"),
                        g("atlas", "mitre"),
                        g("owasp"),
                        g("test"),
                        rel,
                        "table",
                    )
                )
            continue
        i += 1
    return out


def parse_file(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    rel = path.relative_to(ROOT).as_posix()
    return parse_blocks(lines, rel) + parse_tables(lines, rel)


def build_weakness_map() -> dict[str, list[str]]:
    """control_id -> sorted list of MLASWE weakness IDs that the control mitigates.

    Read from each MLASWE page's "Preventive Controls (MLASVS)" section."""
    mlaswe_dir = ROOT / "docs" / "MLASWE"
    ctrl_to_weak: dict[str, set[str]] = {}
    wid_re = re.compile(r"MLASWE-\d{4}")
    ctrl_ref_re = re.compile(r"MLASVS-((?:%s)-\d{3})" % CAT_RE)
    for path in sorted(mlaswe_dir.glob("MLASWE-*.md")):
        text = path.read_text(encoding="utf-8")
        m = wid_re.search(text)
        if not m:
            continue
        wid = m.group(0)
        # Limit to the Preventive Controls section if present
        sec = re.search(
            r"##\s*Preventive Controls.*?(?=\n##\s|\Z)", text, re.S | re.I
        )
        scope = sec.group(0) if sec else text
        for cm in ctrl_ref_re.finditer(scope):
            ctrl_to_weak.setdefault(cm.group(1), set()).add(wid)
    return {k: sorted(v) for k, v in ctrl_to_weak.items()}


def main() -> None:
    files = sorted(MLASVS.rglob("MLASVS-*.md")) + sorted(MLASVS.rglob("0x*.md"))
    seen: dict[str, dict] = {}
    referenced: set[str] = set()

    for path in files:
        referenced.update(REF_RE.findall(path.read_text(encoding="utf-8")))
        for c in parse_file(path):
            # First full definition wins; keep deterministic order
            seen.setdefault(c["id"], c)

    # Also sweep the whole docs tree for referenced IDs (tests, ATLAS pages)
    for path in (ROOT / "docs").rglob("*.md"):
        if "/zh/" in path.as_posix():
            continue
        referenced.update(REF_RE.findall(path.read_text(encoding="utf-8")))

    weak_map = build_weakness_map()
    for c in seen.values():
        c["mlaswe"] = weak_map.get(c["id"], [])

    controls = sorted(
        seen.values(), key=lambda c: (c["category"], int(c["id"].split("-")[1]))
    )

    summary = {"by_category": {}, "totals": {}}
    for cat, name in CATEGORIES.items():
        defined = [c for c in controls if c["category"] == cat]
        ref_ids = {r for r in referenced if r.startswith(cat + "-")}
        summary["by_category"][cat] = {
            "name": name,
            "defined": len(defined),
            "referenced": len(ref_ids),
            "l1": sum(1 for c in defined if c["level"] == "L1"),
            "l2": sum(1 for c in defined if c["level"] == "L2"),
            "undocumented": sorted(ref_ids - {c["id"] for c in defined}),
        }
    summary["totals"] = {
        "defined": len(controls),
        "referenced": len(referenced),
        "l1": sum(1 for c in controls if c["level"] == "L1"),
        "l2": sum(1 for c in controls if c["level"] == "L2"),
        "with_atlas": sum(1 for c in controls if c["atlas"]),
        "with_test": sum(1 for c in controls if c["test"]),
        "with_weakness": sum(1 for c in controls if c["mlaswe"]),
        "format_block": sum(1 for c in controls if c["format"] == "block"),
        "format_table": sum(1 for c in controls if c["format"] == "table"),
        "missing_atlas": sorted(c["id"] for c in controls if not c["atlas"]),
    }

    OUT.write_text(
        json.dumps(
            {
                "name": "MLASVS Control Register",
                "version": "0.1",
                "generated": date.today().isoformat(),
                "source": "https://github.com/bb1nfosec/MLASTG",
                "summary": summary,
                "controls": controls,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    t = summary["totals"]
    print(f"Wrote {OUT.relative_to(ROOT)}")
    print(f"  defined controls : {t['defined']}")
    print(f"  referenced IDs   : {t['referenced']}")
    print(f"  with ATLAS map   : {t['with_atlas']}")
    print(f"  with test ref    : {t['with_test']}")
    for cat, s in summary["by_category"].items():
        gap = f" (undocumented: {len(s['undocumented'])})" if s["undocumented"] else ""
        print(f"  {cat:9s} defined {s['defined']:2d} / referenced {s['referenced']:2d}{gap}")


if __name__ == "__main__":
    main()
