#!/usr/bin/env python3
"""
MLASTG-TEST-MODEL-004: Backdoor Detection Testing
==================================================
Detect potential backdoors/trojans in ML models using
activation clustering analysis.

Usage:
    python test_backdoor.py --demo
"""

import argparse
import logging
from typing import Dict

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.neural_network import MLPClassifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


class BackdoorDetector:
    """Detect potential backdoors using activation analysis."""

    def __init__(self):
        self.results = {}

    def extract_activations(self, model, X: np.ndarray) -> np.ndarray:
        """Extract hidden layer activations from MLP."""
        # Compute activations through the network manually
        activations = X.copy()
        for i in range(len(model.coefs_) - 1):  # Skip output layer
            # MLP stores intercepts in intercepts_ list, not intercept_
            bias = model.intercepts_[i] if hasattr(model, 'intercepts_') else 0
            activations = np.maximum(0, activations @ model.coefs_[i] + bias)
        return activations

    def cluster_analysis(self, activations: np.ndarray) -> Dict:
        """Cluster activations to detect anomalous patterns."""
        kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
        labels = kmeans.fit_predict(activations)
        
        # Measure cluster separation
        if len(np.unique(labels)) > 1:
            sil_score = silhouette_score(activations, labels)
        else:
            sil_score = 0.0
        
        # Check cluster balance
        cluster_sizes = np.bincount(labels)
        balance_ratio = min(cluster_sizes) / max(cluster_sizes)
        
        return {
            "silhouette_score": round(float(sil_score), 4),
            "cluster_balance_ratio": round(float(balance_ratio), 4),
            "backdoor_indicator": sil_score > 0.5 and balance_ratio < 0.3,
        }

    def run(self, X_train: np.ndarray, y_train: np.ndarray,
            X_test: np.ndarray, y_test: np.ndarray) -> Dict:
        """Run backdoor detection analysis."""
        model = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42)
        model.fit(X_train, y_train)
        
        clean_acc = model.score(X_test, y_test)
        self.results["clean_accuracy"] = round(float(clean_acc), 4)
        
        activations = self.extract_activations(model, X_test)
        cluster_results = self.cluster_analysis(activations)
        self.results["cluster_analysis"] = cluster_results
        
        self.results["overall"] = {
            "status": "PASS" if not cluster_results["backdoor_indicator"] else "WARN",
            "test_id": "MLASTG-TEST-MODEL-004",
        }
        return self.results


def demo():
    np.random.seed(42)
    X = np.random.randn(300, 10)
    y = np.random.randint(0, 2, 300)
    split = 200
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]
    
    detector = BackdoorDetector()
    results = detector.run(X_train, y_train, X_test, y_test)
    logger.info(f"Clean accuracy: {results['clean_accuracy']}")
    logger.info(f"Cluster silhouette: {results['cluster_analysis']['silhouette_score']}")
    logger.info(f"Backdoor indicator: {results['cluster_analysis']['backdoor_indicator']}")
    logger.info(f"Status: {results['overall']['status']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backdoor Detection Testing")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    if args.demo:
        demo()
