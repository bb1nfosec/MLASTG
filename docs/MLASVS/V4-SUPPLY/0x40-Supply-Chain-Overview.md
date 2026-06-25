# V4: Supply Chain Security — MLASVS-SUPPLY

## Overview

ML supply chain security addresses risks introduced by third-party models, pre-trained weights, training datasets, and ML libraries. Unlike traditional software supply chains, ML models can be compromised in ways that are difficult to detect — a poisoned model may perform correctly on standard benchmarks while containing hidden backdoors.

## Key Threats

| Threat | MITRE ATLAS | MLASWE Reference |
|--------|-------------|------------------|
| Compromised base model | AML.TA0003 | MLASWE-0009 |
| Poisoned pre-trained weights | AML.T0020 | MLASWE-0002 |
| Malicious dataset in supply chain | AML.T0020 | MLASWE-0009 |
| Vulnerable ML library | AML.TA0003 | MLASWE-0009 |
| Counterfeit model | AML.TA0003 | MLASWE-0009 |
| Tainted transfer learning source | AML.T0020 | MLASWE-0002 |

## Subcategories

### SUPPLY-1: ML-SBOM (Controls SUPPLY-001 through SUPPLY-008)
Machine Learning Software Bill of Materials — documenting all components in the ML supply chain.

### SUPPLY-2: Base Model Vetting (Controls SUPPLY-009 through SUPPLY-014)
Security evaluation of pre-trained models and foundation models.

### SUPPLY-3: Dependency Security (Controls SUPPLY-015 through SUPPLY-022)
Security of ML libraries, frameworks, and runtime dependencies.

## Control Inventory

### L1 Controls (12)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| SUPPLY-001 | ML-SBOM generation | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-002 | Pre-trained model origin verification | AML.TA0003 | TEST-SUPPLY-002 |
| SUPPLY-003 | Training dataset provenance | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-004 | ML library version tracking | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-005 | License compliance check | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-006 | Model hash verification at load | AML.TA0006 | TEST-SUPPLY-002 |
| SUPPLY-007 | Transfer learning source validation | AML.T0020 | TEST-SUPPLY-002 |
| SUPPLY-008 | Dataset license verification | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-009 | Base model vulnerability scanning | AML.TA0003 | TEST-SUPPLY-002 |
| SUPPLY-010 | ML dependency scanning | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-011 | Secure model distribution channels | AML.TA0002 | TEST-SUPPLY-002 |
| SUPPLY-012 | Third-party model evaluation report | AML.TA0003 | TEST-SUPPLY-002 |

### L2 Controls (10)

| ID | Control | MITRE ATLAS | Test Ref |
|----|---------|-------------|----------|
| SUPPLY-013 | Automated ML-SBOM generation in CI/CD | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-014 | Continuous dependency monitoring | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-015 | Cryptographic model provenance | AML.TA0006 | TEST-SUPPLY-002 |
| SUPPLY-016 | Model signing and attestation | AML.TA0006 | TEST-SUPPLY-002 |
| SUPPLY-017 | Fine-tuning data provenance chain | AML.T0020 | TEST-SUPPLY-001 |
| SUPPLY-018 | Adversarial robustness of base model | AML.T0010 | TEST-SUPPLY-002 |
| SUPPLY-019 | Backdoor scanning of pre-trained models | AML.T0020 | TEST-SUPPLY-002 |
| SUPPLY-020 | Vendor security assessment program | AML.TA0003 | TEST-SUPPLY-002 |
| SUPPLY-021 | ML supply chain incident response | AML.TA0003 | TEST-SUPPLY-001 |
| SUPPLY-022 | Reproducible build verification | AML.TA0006 | TEST-SUPPLY-002 |

## ML-SBOM Requirements

A complete ML-SBOM should include:

| Component | Description | Verification |
|-----------|-------------|-------------|
| **Model metadata** | Name, version, author, date | SUPPLY-001, SUPPLY-015 |
| **Base model** | Source, architecture, hash | SUPPLY-002, SUPPLY-006 |
| **Training dataset** | Origin, hash, license, curation | SUPPLY-003, SUPPLY-008 |
| **Fine-tuning data** | Provenance, transformations | SUPPLY-017 |
| **Framework dependencies** | Library name, version, CVE status | SUPPLY-004, SUPPLY-010 |
| **Training environment** | Compute specs, software versions | SUPPLY-013 |
| **Model signature** | Cryptographic signature | SUPPLY-016 |

## Related Links

- [MLASTG Test Cases: Supply Chain](../../MLASTG/SUPPLY-Tests/0x00-Supply-Tests-Overview.md)
- [MLASWE-0009: Supply Chain Compromise](../../MLASWE/MLASWE-0009-Supply-Chain-Compromise.md)
