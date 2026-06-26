# MLASVS-MODEL-5: Model Integrity Controls

> **Subcategory:** V2: Model Security
> **Controls:** MODEL-007, MODEL-008, MODEL-014, MODEL-015, MODEL-030

## Overview

Model integrity controls ensure that ML models are authentic, untampered, properly versioned, and can be rolled back if compromised. This subcategory covers versioning, signing, secure serialization, rollback capability, and provenance attestation.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| MODEL-007 | Model versioning | L1 | AML.TA0006 | TEST-MODEL-005 | Maintain versioned model registry with immutable history |
| MODEL-008 | Model signing | L1 | AML.TA0006 | TEST-MODEL-005 | Cryptographically sign model artifacts to detect tampering |
| MODEL-014 | Secure model serialization | L1 | AML.TA0002 | TEST-MODEL-005 | Use safe serialization formats (SafeTensors preferred over Pickle) |
| MODEL-015 | Model rollback capability | L1 | AML.TA0006 | TEST-MODEL-005 | Enable rapid rollback to previous model versions |
| MODEL-030 | Model provenance attestation | L2 | AML.TA0006 | TEST-MODEL-005 | Attest model origin, training process, and chain of custody |

## Implementation Guidance

### Versioning
- Maintain a model registry with immutable version history
- Tag each version with: timestamp, training data hash, code commit, author
- Never overwrite model artifacts — use append-only registries

### Signing
- Sign model files using GPG or Sigstore
- Verify signatures at every deployment gate (staging → production)
- Reject unsigned or tampered model files

### Secure Serialization
- Prefer SafeTensors format over Pickle for PyTorch models
- Scan model files with ModelScan before loading
- Implement hash verification at load time

### Rollback
- Maintain at least 3 previous production model versions
- Test rollback procedures quarterly
- Document Recovery Time Objective (RTO) for model rollback

## Related

- [MLASTG-TEST-SUPPLY-002: Pre-Trained Model Provenance Verification](../../MLASTG/SUPPLY-Tests/MLASTG-TEST-SUPPLY-002.md)
- [MLASWE-0009: Supply Chain Compromise](../../MLASWE/MLASWE-0009-Supply-Chain-Compromise.md)
- **MITRE ATLAS:** AML.TA0006 (Persistence), AML.TA0002 (Initial Access)
