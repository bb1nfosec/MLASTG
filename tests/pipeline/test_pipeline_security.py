#!/usr/bin/env python3
"""
MLASTG-TEST-PIPELINE-001: CI/CD Security Audit
================================================
Automated security checks for ML pipeline configurations.

Usage:
    python test_pipeline_security.py --repo-url https://github.com/org/repo
    python test_pipeline_security.py --repo-url https://github.com/org/repo --report pipeline_report.json
    python test_pipeline_security.py --demo
"""

import argparse
import json
import logging
import os
import subprocess
from pathlib import Path
from typing import Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


PIPELINE_CHECKS = [
    {"id": "PIPE-001", "name": "Secrets in Pipeline Config", "level": "L1"},
    {"id": "PIPE-002", "name": "Dependency Pinning", "level": "L1"},
    {"id": "PIPE-003", "name": "Container Image Scanning", "level": "L1"},
    {"id": "PIPE-004", "name": "Signed Artifacts", "level": "L2"},
    {"id": "PIPE-005", "name": "Model Registry Auth", "level": "L1"},
    {"id": "PIPE-006", "name": "Pipeline Isolation", "level": "L2"},
]


class PipelineSecurityTester:
    """Test CI/CD pipeline security configurations."""

    def __init__(self, repo_path: str = ".", level: str = "L1"):
        self.repo_path = Path(repo_path)
        self.level = level
        self.results = {}

    def check_secrets_exposure(self) -> Dict:
        """Check for hardcoded secrets in pipeline files."""
        logger.info("Checking for secrets in pipeline configurations...")
        pipeline_files = self._find_pipeline_files()
        secrets_found = []

        secret_patterns = [
            "password",
            "secret",
            "api_key",
            "apikey",
            "token",
            "aws_access_key",
            "aws_secret_key",
            "private_key",
        ]

        for file_path in pipeline_files:
            try:
                content = file_path.read_text()
                for pattern in secret_patterns:
                    if pattern.lower() in content.lower():
                        for line in content.split("\n"):
                            if pattern.lower() in line.lower() and "=" in line:
                                # Skip lines that look like env var references (e.g., ${{ secrets.X }})
                                stripped = line.strip()
                                if "${{" in stripped or "secrets." in stripped:
                                    continue
                                if stripped.startswith("#"):
                                    continue
                                secrets_found.append({
                                    "file": str(file_path),
                                    "pattern": pattern,
                                    "line": stripped[:100],
                                })
            except Exception as e:
                logger.warning(f"Could not read {file_path}: {e}")

        return {
            "control": "PIPE-001",
            "name": "Secrets in Pipeline Config",
            "files_scanned": len(pipeline_files),
            "secrets_found": len(secrets_found),
            "details": secrets_found[:10],  # Limit to 10
            "pass": len(secrets_found) == 0,
        }

    def check_dependency_pinning(self) -> Dict:
        """Check if dependencies are pinned to versions."""
        logger.info("Checking dependency pinning...")
        requirements_files = list(self.repo_path.rglob("requirements*.txt"))
        unpinned = []

        for req_file in requirements_files:
            try:
                lines = req_file.read_text().splitlines()
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith("#") and not line.startswith("-"):
                        if "==" not in line and ">=" not in line:
                            unpinned.append({
                                "file": str(req_file),
                                "package": line,
                            })
            except Exception as e:
                logger.warning(f"Could not read {req_file}: {e}")

        return {
            "control": "PIPE-002",
            "name": "Dependency Pinning",
            "files_scanned": len(requirements_files),
            "unpinned_dependencies": len(unpinned),
            "details": unpinned[:10],
            "pass": len(unpinned) == 0,
        }

    def check_container_security(self) -> Dict:
        """Check for Dockerfile security best practices."""
        logger.info("Checking container security...")
        dockerfiles = list(self.repo_path.rglob("Dockerfile*"))
        issues = []

        for dockerfile in dockerfiles:
            try:
                content = dockerfile.read_text()
                if "FROM" in content:
                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        if line.startswith("FROM") and ":latest" in line:
                            issues.append({
                                "file": str(dockerfile),
                                "issue": "Using :latest tag",
                                "line": i + 1,
                            })
                        if line.startswith("USER") and "root" in line.lower():
                            issues.append({
                                "file": str(dockerfile),
                                "issue": "Running as root",
                                "line": i + 1,
                            })
            except Exception as e:
                logger.warning(f"Could not read {dockerfile}: {e}")

        return {
            "control": "PIPE-003",
            "name": "Container Image Scanning",
            "files_scanned": len(dockerfiles),
            "issues_found": len(issues),
            "details": issues[:10],
            "pass": len(issues) == 0,
        }

    def _find_pipeline_files(self) -> List[Path]:
        """Find CI/CD pipeline configuration files."""
        patterns = [
            ".github/workflows/*.yml",
            ".github/workflows/*.yaml",
            ".gitlab-ci.yml",
            "Jenkinsfile",
            "azure-pipelines.yml",
            ".circleci/config.yml",
        ]
        files = []
        for pattern in patterns:
            files.extend(self.repo_path.glob(pattern))
        return files

    def run(self) -> Dict:
        """Run all pipeline security checks."""
        self.results["secrets"] = self.check_secrets_exposure()
        self.results["dependencies"] = self.check_dependency_pinning()
        self.results["containers"] = self.check_container_security()

        all_pass = all(
            r.get("pass", False)
            for r in self.results.values()
            if isinstance(r, dict) and "pass" in r
        )

        self.results["overall"] = {
            "status": "PASS" if all_pass else "FAIL",
            "test_id": "MLASTG-TEST-PIPELINE-001",
            "level": self.level,
        }

        return self.results

    def export_report(self, path: str):
        """Export results as JSON."""
        report = {
            "test_id": "MLASTG-TEST-PIPELINE-001",
            "control": "MLASVS-PIPELINE-001",
            "level": self.level,
            "results": self.results,
        }
        with open(path, "w") as f:
            json.dump(report, f, indent=2)
        logger.info(f"Report exported to {path}")


def demo():
    """Run demonstration with local repo."""
    logger.info("Pipeline Security Demo - scanning current directory")
    tester = PipelineSecurityTester(repo_path=".", level="L1")
    results = tester.run()

    for check, result in results.items():
        if isinstance(result, dict) and "control" in result:
            status = "✅" if result.get("pass") else "❌"
            logger.info(f"  {result['control']} - {result['name']}: {status}")

    logger.info(f"Overall: {results['overall']['status']}")


def run_test(target: str, demo: bool = False) -> list:
    """Orchestrate the test logic."""
    if demo:
        return [{"test_id": "MLASTG-TEST-PIPELINE-001", "control": "CI/CD Security Audit", "name": "Pipeline Security", "status": "pass", "severity": "L1", "evidence": ["Mock"]}]

    tester = PipelineSecurityTester(repo_path=target if target else ".", level="L1")
    results = tester.run()
    
    return [{
        "test_id": "MLASTG-TEST-PIPELINE-001",
        "control": "CI/CD Security Audit",
        "name": "Pipeline Security",
        "status": "pass" if results.get("overall", {}).get("status") == "PASS" else "fail",
        "severity": "L1",
        "evidence": [results]
    }]
