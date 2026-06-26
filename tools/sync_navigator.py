#!/usr/bin/env python3
"""
Sync ATLAS Navigator HTML from JSON data file.

Generates docs/assets/atlas-navigator.html from docs/ATLAS-Mapping/2-atlas-navigator-layer.json
to eliminate the maintenance burden of keeping two data sources in sync.

Usage:
    python tools/sync_navigator.py
    python tools/sync_navigator.py --check  # Dry-run: verify files are in sync
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
JSON_PATH = PROJECT_ROOT / "docs" / "ATLAS-Mapping" / "2-atlas-navigator-layer.json"
HTML_PATH = PROJECT_ROOT / "docs" / "assets" / "atlas-navigator.html"


def load_navigator_json() -> dict:
    """Load and return the Navigator JSON data."""
    with open(JSON_PATH, "r") as f:
        return json.load(f)


def load_navigator_html() -> str:
    """Load the current Navigator HTML."""
    with open(HTML_PATH, "r") as f:
        return f.read()


def extract_techniques_from_html(html: str) -> list:
    """Extract the hardcoded techniques array from the HTML file."""
    # Find the techniques array in the JavaScript
    match = re.search(
        r'const techniques = \[(.*?)\];', html, re.DOTALL
    )
    if not match:
        return []
    
    # Parse the JavaScript array as JSON-like structure
    raw = match.group(1)
    # Extract individual technique objects
    techs = []
    for tech_match in re.finditer(
        r'\{[^}]*id:\s*"([^"]*)"[^}]*name:\s*"([^"]*)"[^}]*score:\s*(\d+)[^}]*\}',
        raw
    ):
        techs.append({
            "id": tech_match.group(1),
            "name": tech_match.group(2),
            "score": int(tech_match.group(3)),
        })
    return techs


def techniques_in_sync(json_data: dict, html: str) -> bool:
    """Check if JSON and HTML have the same techniques with the same scores."""
    json_techs = {t["techniqueID"]: t for t in json_data["techniques"]}
    html_techs = {t["id"]: t for t in extract_techniques_from_html(html)}
    
    if set(json_techs.keys()) != set(html_techs.keys()):
        missing = set(json_techs.keys()) - set(html_techs.keys())
        extra = set(html_techs.keys()) - set(json_techs.keys())
        if missing:
            print(f"Techniques in JSON but not HTML: {missing}")
        if extra:
            print(f"Techniques in HTML but not JSON: {extra}")
        return False
    
    for tid in json_techs:
        json_score = json_techs[tid]["score"]
        html_score = html_techs[tid]["score"]
        if json_score != html_score:
            print(f"Score mismatch for {tid}: JSON={json_score}, HTML={html_score}")
            return False
    
    return True


def generate_techniques_js(json_data: dict) -> str:
    """Generate the JavaScript techniques array from JSON data."""
    lines = []
    for tech in json_data["techniques"]:
        tid = tech["techniqueID"]
        # Determine tactic from comment or default
        comment = tech.get("comment", "")
        controls = tech.get("controls", [])
        tests = []
        
        # Extract tactic from technique ID patterns
        tactic_map = {
            "T0000": "resource", "T0001": "recon", "T0002": "recon",
            "T0003": "initial", "T0005": "initial", "T0007": "collection",
            "T0010": "exec", "T0011": "evasion", "T0012": "persist",
            "T0013": "collection", "T0014": "collection", "T0018": "exec",
            "T0020": "exec", "T0021": "exec", "T0031": "collection",
            "T0034": "exec", "T0035": "exec", "T0037": "collection",
            "T0040": "resource", "T0043": "exec", "T0051": "exec",
            "T0052": "exec", "T0053": "exec", "T0054": "exec",
            "T0056": "exec", "T0057": "collection", "T0058": "collection",
            "T0059": "persist",
        }
        base_id = tid.split(".")[-1] if "." in tid else tid
        tactic = tactic_map.get(base_id, "exec")
        
        # Extract controls and tests from comment
        controls_str = json.dumps(tech.get("controls", [])) if tech.get("controls") else "[]"
        tests_str = "[]"  # Tests not in JSON, keep empty
        
        line = (
            f'            {{ id: "{tid}", name: "{comment.split(" - ")[0] if " - " in comment else tid}", '
            f'tactic: "{tactic}", score: {tech["score"]}, '
            f'controls: {controls_str}, tests: {tests_str} }},'
        )
        lines.append(line)
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Sync ATLAS Navigator HTML from JSON")
    parser.add_argument("--check", action="store_true", help="Verify files are in sync (dry-run)")
    parser.add_argument("--update", action="store_true", help="Update HTML to match JSON")
    args = parser.parse_args()
    
    if not JSON_PATH.exists():
        print(f"Error: {JSON_PATH} not found")
        sys.exit(1)
    
    if not HTML_PATH.exists():
        print(f"Error: {HTML_PATH} not found")
        sys.exit(1)
    
    json_data = load_navigator_json()
    html = load_navigator_html()
    
    if techniques_in_sync(json_data, html):
        print("✅ Navigator JSON and HTML are in sync")
        sys.exit(0)
    
    if args.check:
        print("❌ Navigator JSON and HTML are out of sync")
        print("   Run: python tools/sync_navigator.py --update")
        sys.exit(1)
    
    if args.update:
        # Regenerate the techniques array from JSON
        new_techniques = generate_techniques_js(json_data)
        
        # Replace the old techniques array in HTML
        new_html = re.sub(
            r'const techniques = \[.*?\];',
            f'const techniques = [\n{new_techniques}\n        ];',
            html,
            flags=re.DOTALL
        )
        
        with open(HTML_PATH, "w") as f:
            f.write(new_html)
        
        print(f"✅ Updated {HTML_PATH}")
        print(f"   {len(json_data['techniques'])} techniques synced from JSON")
        sys.exit(0)
    
    # Default: show what's different and exit
    print("❌ Navigator files are out of sync")
    print("   Use --update to sync HTML from JSON")
    print("   Use --check to verify sync status")
    sys.exit(1)


if __name__ == "__main__":
    main()
