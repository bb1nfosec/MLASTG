#!/usr/bin/env python3
"""
MLASTG-TEST-INFRA-002: API Security Review
==========================================
Test model inference API for common security vulnerabilities.

Usage:
    python test_api_security.py --endpoint https://api.example.com/v1/model
    python test_api_security.py --endpoint http://localhost:8000/predict --demo
"""

import argparse
import logging
import time
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class APISecurityTester:
    """Test ML inference API endpoints for security issues."""

    def __init__(self, endpoint: str, api_key: Optional[str] = None):
        self.endpoint = endpoint
        self.api_key = api_key
        self.results = {}

    def test_authentication(self) -> Dict:
        """Test that endpoint requires authentication."""
        import requests
        try:
            response = requests.get(self.endpoint, timeout=10)
            status = response.status_code
            return {
                "test": "Authentication Required",
                "unauthenticated_status": status,
                "pass": status in (401, 403),
            }
        except Exception as e:
            return {"test": "Authentication Required", "error": str(e), "pass": False}

    def test_tls(self) -> Dict:
        """Verify TLS is used (when applicable)."""
        if self.endpoint.startswith("http://"):
            return {"test": "TLS Enforcement", "pass": False, "reason": "HTTP (not HTTPS)"}
        return {"test": "TLS Enforcement", "pass": True, "reason": "HTTPS"}

    def test_rate_limiting(self) -> Dict:
        """Quick rate limit check."""
        import requests
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        statuses = []
        for _ in range(10):
            try:
                r = requests.get(self.endpoint, headers=headers, timeout=5)
                statuses.append(r.status_code)
            except:
                statuses.append(0)
            time.sleep(0.05)
        
        rate_limited = any(s == 429 for s in statuses)
        return {
            "test": "Rate Limiting",
            "status_codes": statuses,
            "rate_limited_detected": rate_limited,
            "pass": rate_limited,  # Rate limiting should trigger eventually
        }

    def run(self) -> Dict:
        """Run all API security checks."""
        self.results["authentication"] = self.test_authentication()
        self.results["tls"] = self.test_tls()
        self.results["rate_limiting"] = self.test_rate_limiting()
        
        all_pass = all(r.get("pass", False) for r in self.results.values() if isinstance(r, dict))
        self.results["overall"] = {
            "status": "PASS" if all_pass else "REVIEW",
            "test_id": "MLASTG-TEST-INFRA-002",
        }
        return self.results


def run_test(target: str, demo: bool = False) -> list:
    """Run API security tests and return results as a list of dicts."""
    if demo:
        return [
            {
                "test_id": "MLASTG-TEST-INFRA-002",
                "control": "INFRA-002",
                "name": "Authentication Required",
                "status": "pass",
                "severity": "L1",
                "evidence": ["Mock demo result"]
            }
        ]

    tester = APISecurityTester(endpoint=target)
    results_dict = tester.run()
    
    test_results = []
    for key, val in results_dict.items():
        if key == "overall":
            continue
        test_results.append({
            "test_id": "MLASTG-TEST-INFRA-002",
            "control": "INFRA-002",
            "name": val.get("test", key),
            "status": "pass" if val.get("pass") else "fail",
            "severity": "L1",
            "evidence": [str(val)]
        })
    return test_results


if __name__ == "__main__":
    import argparse, json as _json
    _ap = argparse.ArgumentParser(description="MLASTG test harness")
    _ap.add_argument("--demo", action="store_true", help="Run with synthetic data (no live target)")
    _ap.add_argument("--target", default=".", help="Target endpoint or path to assess")
    _args = _ap.parse_args()
    _results = run_test(_args.target, demo=_args.demo)
    print(_json.dumps(_results, indent=2, default=str))
    raise SystemExit(0 if all(r.get("status") == "pass" for r in _results) else 1)
