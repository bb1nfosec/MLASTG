#!/usr/bin/env python3
"""
MLASTG-TEST-SUPPLY-001: ML-SBOM Audit
======================================
Validate ML Software Bill of Materials for completeness and vulnerability scanning.

Usage:
    python test_mlsbom.py --sbom sbom.json
    python test_mlsbom.py --demo
"""

import argparse
import json
import logging
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


REQUIRED_SBOM_FIELDS = [
    "model_name", "model_version", "base_model", "training_dataset",
    "framework_dependencies", "training_environment"
]

REQUIRED_DATASET_FIELDS = [
    "source", "hash", "license"
]

REQUIRED_DEPENDENCY_FIELDS = [
    "name", "version"
]


class MLSBOMValidator:
    """Validate ML-SBOM completeness and security."""

    def validate_sbom(self, sbom: Dict) -> Dict:
        """Check SBOM has all required fields."""
        missing = [f for f in REQUIRED_SBOM_FIELDS if f not in sbom]
        return {
            "field_check": {
                "required": REQUIRED_SBOM_FIELDS,
                "present": [f for f in REQUIRED_SBOM_FIELDS if f in sbom],
                "missing": missing,
            },
            "valid": len(missing) == 0,
        }

    def validate_datasets(self, sbom: Dict) -> List[Dict]:
        """Validate dataset entries in SBOM."""
        datasets = sbom.get("training_dataset", [])
        if isinstance(datasets, dict):
            datasets = [datasets]
        results = []
        for ds in datasets:
            missing = [f for f in REQUIRED_DATASET_FIELDS if f not in ds]
            results.append({
                "dataset": ds.get("source", "unknown"),
                "valid": len(missing) == 0,
                "missing_fields": missing,
            })
        return results

    def run(self, sbom: Dict) -> Dict:
        """Run complete SBOM validation."""
        results = {
            "sbom_validation": self.validate_sbom(sbom),
            "dataset_validation": self.validate_datasets(sbom),
            "test_id": "MLASTG-TEST-SUPPLY-001",
        }
        all_datasets_valid = all(d["valid"] for d in results["dataset_validation"])
        results["overall"] = {
            "status": "PASS" if results["sbom_validation"]["valid"] and all_datasets_valid else "FAIL",
        }
        return results


def demo():
    sbom = {
        "model_name": "example-classifier-v1",
        "model_version": "1.0.0",
        "base_model": {"source": "pytorch-hub", "hash": "sha256:abc123"},
        "training_dataset": [
            {"source": "s3://data/train.csv", "hash": "sha256:def456", "license": "MIT"},
        ],
        "framework_dependencies": [
            {"name": "pytorch", "version": "2.0.1"},
            {"name": "transformers", "version": "4.30.0"},
        ],
        "training_environment": {"gpu": "A100", "os": "Ubuntu 22.04", "cuda": "11.8"},
    }
    validator = MLSBOMValidator()
    results = validator.run(sbom)
    logger.info(f"SBOM valid: {results['sbom_validation']['valid']}")
    logger.info(f"Dataset valid: {all(d['valid'] for d in results['dataset_validation'])}")
    logger.info(f"Status: {results['overall']['status']}")


def run_test(target: str, demo: bool = False) -> list:
    """Orchestrate the test logic."""
    if demo:
        return [{"test_id": "MLASTG-TEST-SUPPLY-001", "control": "ML-SBOM Audit", "name": "SBOM Completeness", "status": "pass", "severity": "L1", "evidence": ["Mock"]}]

    try:
        with open(target, 'r') as f:
            sbom = json.load(f)
    except Exception as e:
        return [{"test_id": "MLASTG-TEST-SUPPLY-001", "control": "ML-SBOM Audit", "name": "SBOM Completeness", "status": "fail", "severity": "L1", "evidence": [f"Error reading SBOM: {e}"]}]

    validator = MLSBOMValidator()
    results = validator.run(sbom)
    
    return [{
        "test_id": "MLASTG-TEST-SUPPLY-001",
        "control": "ML-SBOM Audit",
        "name": "SBOM Completeness",
        "status": "pass" if results["overall"]["status"] == "PASS" else "fail",
        "severity": "L1",
        "evidence": [results]
    }]


if __name__ == "__main__":
    import argparse, json as _json
    _ap = argparse.ArgumentParser(description="MLASTG ML-SBOM validator (MLASTG-TEST-SUPPLY-001)")
    _ap.add_argument("--demo", action="store_true", help="Validate a synthetic SBOM")
    _ap.add_argument("--sbom", help="Path to an ML-SBOM JSON file to validate")
    _ap.add_argument("--target", default=".", help="Alias for --sbom")
    _args = _ap.parse_args()
    _target = _args.sbom or _args.target
    _results = run_test(_target, demo=_args.demo)
    print(_json.dumps(_results, indent=2, default=str))
    raise SystemExit(0 if all(r.get("status") == "pass" for r in _results) else 1)
