#!/usr/bin/env python3
"""
MLASTG-TEST-DATA-002: Data Sanitization Validation
==================================================
Detect anomalous training data using statistical methods.
Helps identify potential data poisoning attempts.

Usage:
    python test_data_sanitization.py --dataset train_data.csv
    python test_data_sanitization.py --dataset train_data.csv --report sanitization_report.json
"""

import argparse
import json
import logging
from typing import Dict

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class DataSanitizationTester:
    """Detect anomalous data points that may indicate poisoning attempts."""

    def __init__(self, contamination: float = 0.1):
        self.contamination = contamination
        self.results = {}

    def detect_outliers_iforest(self, data: np.ndarray) -> Dict:
        """Use Isolation Forest to detect outliers."""
        logger.info("Running Isolation Forest outlier detection...")
        model = IsolationForest(contamination=self.contamination, random_state=42)
        predictions = model.fit_predict(data)
        outliers = np.sum(predictions == -1)
        return {
            "method": "IsolationForest",
            "total_samples": len(data),
            "outliers_detected": int(outliers),
            "outlier_rate": round(float(outliers / len(data)), 4),
        }

    def detect_outliers_lof(self, data: np.ndarray) -> Dict:
        """Use Local Outlier Factor for density-based detection."""
        logger.info("Running LOF outlier detection...")
        model = LocalOutlierFactor(contamination=self.contamination)
        predictions = model.fit_predict(data)
        outliers = np.sum(predictions == -1)
        return {
            "method": "LOF",
            "total_samples": len(data),
            "outliers_detected": int(outliers),
            "outlier_rate": round(float(outliers / len(data)), 4),
        }

    def run_all_checks(self, data: np.ndarray) -> Dict:
        """Run all sanitization checks."""
        self.results["iforest"] = self.detect_outliers_iforest(data)
        self.results["lof"] = self.detect_outliers_lof(data)
        
        max_outlier_rate = max(
            self.results["iforest"]["outlier_rate"],
            self.results["lof"]["outlier_rate"],
        )
        threshold = 0.15  # > 15% outliers indicates potential poisoning
        self.results["overall"] = {
            "status": "PASS" if max_outlier_rate <= threshold else "WARN",
            "max_outlier_rate": max_outlier_rate,
            "threshold": threshold,
            "test_id": "MLASTG-TEST-DATA-002",
        }
        return self.results

    def export_report(self, path: str):
        with open(path, "w") as f:
            json.dump(self.results, f, indent=2)
        logger.info(f"Report exported to {path}")


def demo():
    """Run demonstration with synthetic data."""
    np.random.seed(42)
    clean = np.random.randn(190, 10)
    poison = np.random.randn(10, 10) * 5  # Anomalous data
    data = np.vstack([clean, poison])
    
    tester = DataSanitizationTester(contamination=0.1)
    results = tester.run_all_checks(data)
    logger.info(f"IsolationForest outliers: {results['iforest']['outliers_detected']}")
    logger.info(f"LOF outliers: {results['lof']['outliers_detected']}")
    logger.info(f"Status: {results['overall']['status']}")
    return results


def main():
    parser = argparse.ArgumentParser(description="Data Sanitization Testing")
    parser.add_argument("--dataset", help="Path to training data (.npy or .csv)")
    parser.add_argument("--report", default="sanitization_report.json")
    parser.add_argument("--demo", action="store_true", help="Run with synthetic data")
    args = parser.parse_args()

    if args.demo:
        demo()
    else:
        logger.info("Provide --dataset to analyze, or --demo for demonstration.")


if __name__ == "__main__":
    main()
