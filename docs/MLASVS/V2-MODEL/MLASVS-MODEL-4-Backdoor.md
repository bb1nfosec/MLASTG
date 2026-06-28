# MLASVS-MODEL-4: Backdoor Detection Controls

> **Subcategory:** V2: Model Security
> **Controls:** MODEL-021, MODEL-022

## Overview

Backdoor detection ensures that deployed models do not contain hidden malicious behaviors that produce attacker-controlled outputs when triggered. This subcategory covers activation-based detection and trojan identification.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| MODEL-021 | Backdoor detection validation | L2 | AML.T0020 | TEST-MODEL-004 | Validate that models pass backdoor detection analysis |
| MODEL-022 | Trojan detection | L2 | AML.T0020 | TEST-MODEL-004 | Detect trojan triggers using activation clustering and trigger inversion |

## Implementation Guidance

### Activation Clustering
- Extract penultimate layer activations for the full validation dataset
- Cluster activations per class using k-means (k=2 per class)
- Investigate large, clearly separated clusters as potential backdoor indicators

### Trigger Pattern Inversion (Neural Cleanse)
- For each output class, optimize to find the minimal trigger perturbation
- Flag classes requiring unusually small triggers (anomaly index > 2)

### STRIP Analysis
- Superimpose random clean images on test inputs
- Monitor prediction entropy under perturbation
- Backdoored inputs maintain low entropy despite noise

## Prevention Controls

- Audit training data for anomalous patterns before training
- Use activation clustering as a training-time defense
- Source pre-trained models only from verified, signed sources
- Implement backdoor scanning as a mandatory CI/CD gate

## Related

- [MLASTG-TEST-MODEL-004: Backdoor & Trojan Detection Testing](../../MLASTG/MODEL-Tests/MLASTG-TEST-MODEL-004.md)
- [MLASWE-0007: Backdoor/Trojan](../../MLASWE/MLASWE-0007-Backdoor-Trojan.md)
- **MITRE ATLAS:** AML.T0020 (Data Poisoning), AML.T0018.000 (Poison AI Model)
