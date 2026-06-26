# MLASVS-MODEL-2: Extraction Prevention Controls

> **Subcategory:** V2: Model Security
> **Controls:** MODEL-004, MODEL-005, MODEL-006, MODEL-018, MODEL-023

## Overview

Model extraction prevention ensures that adversaries cannot steal a deployed ML model by systematically querying its API. This subcategory covers output precision limiting, API rate limiting, access control, extraction resistance validation, and model watermarking.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| MODEL-004 | Output confidence calibration | L1 | AML.T0018 | TEST-MODEL-002 | Limit precision of output confidence scores to reduce information leakage |
| MODEL-005 | API rate limiting | L1 | AML.T0034 | TEST-MODEL-002 | Enforce per-user query quotas to prevent bulk extraction |
| MODEL-006 | Access control on model endpoints | L1 | AML.TA0002 | TEST-MODEL-002 | Require authentication for all model inference endpoints |
| MODEL-018 | Extraction resistance validation | L2 | AML.T0034 | TEST-MODEL-002 | Verify that surrogate models cannot achieve high fidelity through API queries |
| MODEL-023 | Model watermarking | L2 | AML.T0034 | TEST-MODEL-002 | Embed unique fingerprints in model outputs for forensic tracing |

## Implementation Guidance

### Output Precision
- Truncate confidence scores to ≤ 3 decimal places at the API layer
- Consider returning only top-k predictions instead of full probability vectors
- Add calibrated noise to output vectors for differential privacy

### Rate Limiting
- Implement per-user and per-API-key rate limits at the API gateway
- Set cumulative query quotas (e.g., max 10,000 queries/day per user)
- Monitor for systematic query patterns indicating extraction attempts

### Model Watermarking
- Embed trigger-response pairs in model outputs
- Use fingerprinting techniques (e.g., backdoor watermarking)
- Maintain a registry of known watermarks for forensic comparison

## Related

- [MLASTG-TEST-MODEL-002: Extraction Resistance Testing](../../MLASTG/MODEL-Tests/MLASTG-TEST-MODEL-002.md)
- [MLASWE-0003: Model Extraction](../../MLASWE/MLASWE-0003-Model-Extraction.md)
- **MITRE ATLAS:** AML.T0034 (Model Extraction)
