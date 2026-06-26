# MLASTG-TEST-DATA-001: Data Provenance Verification

## Control Reference
**Controls Tested:** MLASVS-DATA-001 (Data Provenance Tracking), MLASVS-DATA-002 (Cryptographic Data Integrity), MLASVS-DATA-006 (Data Lineage Documentation), MLASVS-DATA-020 (Cryptographic Data Provenance - L2), MLASVS-DATA-026 (Real-time Data Integrity Monitoring - L2), MLASVS-DATA-030 (Data Trust Scoring - L2)

## Severity
**Medium** (L1) / **High** (L2)

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Access | Data catalog or dataset storage system |
| Tools | `sha256sum`, `openssl` or equivalent |
| Documentation | Data ingestion pipeline documentation |
| Additional (L2) | Access to CI/CD pipeline logs, data source manifests |

## Step-by-Step Procedure

### Step 1: Inventory Training Datasets
1. Identify all datasets used for model training, validation, and testing
2. Document dataset names, sources, collection dates, and responsible parties
3. Review data catalog entries for completeness

### Step 2: Verify Data Origin Documentation
1. Check that each dataset has documented:
   - Source system or data provider
   - Collection methodology
   - Collection date range
   - Responsible team or individual
   - Intended use case
2. **Pass if:** All training datasets have complete origin documentation

### Step 3: Verify Cryptographic Integrity
1. Locate stored SHA-256 (or stronger) hashes for each dataset
2. Recompute hashes:
   ```bash
   sha256sum training_dataset_v1.csv
   ```
3. Compare recomputed hashes against stored values
4. **Pass if:** All hashes match stored values

### Step 4: Review Data Lineage (L1)
1. Identify all data transformation steps applied
2. Verify transformations are documented in version-controlled pipeline code
3. Confirm raw data can be reproduced from transformations
4. **Pass if:** Complete transformation pipeline is documented and version-controlled

### Step 5: Verify Lineage Reproducibility (L1)
1. Execute the data pipeline from raw data to processed output
2. Compare final processed data hash against original training hash
3. **Pass if:** Reproduced data hash matches training data hash

### Step 6: Verify Signed Manifests (L2)
1. Locate signed data provenance manifests for each dataset
2. Verify signature chain:
   ```bash
   openssl verify -CAfile ca-cert.pem -untrusted intermediate.pem manifest.sig
   ```
3. Check that manifest covers full transformation history
4. **Pass if:** All manifests are valid and signed by authorized parties

### Step 7: Test Real-time Integrity Monitoring (L2)
1. For continuous learning systems, inject a corrupted data record
2. Verify that the monitoring system detects and alerts on integrity failure
3. Check that the corrupted record is quarantined or rejected
4. **Pass if:** Monitoring system detects integrity failures within defined SLAs

### Step 8: Evaluate Data Trust Scoring (L2)
1. Review data source trust scoring methodology
2. Verify that all data sources have assigned trust scores
3. Check that low-trust sources trigger additional verification
4. **Pass if:** Trust scoring is implemented and triggers appropriate verification

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | All datasets have documented provenance, verified hashes, and reproducible lineage |
| L2 | All datasets have signed provenance manifests, integrity monitoring, and trust scoring |

## Evidence Requirements

- [ ] Dataset inventory with provenance documentation
- [ ] Hash verification logs for each dataset
- [ ] Data lineage documentation
- [ ] (L2) Signed provenance manifests
- [ ] (L2) Integrity monitoring test results
- [ ] (L2) Trust scoring methodology and results

## Remediation Guidance

**If hashes don't match:**
1. Isolate affected datasets immediately
2. Determine if data was modified in transit or storage
3. Revert to known-good backup if available
4. Investigate root cause (unauthorized access, storage corruption)
5. Implement controls to prevent recurrence

**If provenance is incomplete:**
1. Implement automated data catalog with provenance capture
2. Add data ingestion metadata requirements
3. Train data engineers on provenance documentation

**If lineage is not reproducible:**
1. Version-control data pipeline code
2. Use deterministic preprocessing where possible
3. Record random seeds and parameters for stochastic transformations

## References
- **MITRE ATLAS:**
  - `AML.T0020` — Poison Training Data (provenance context)
  - `AML.T0059` — Backdoor ML Model (integrity monitoring context)
  - `AML.TA0009` — Collection (tactic; for lineage / data harvesting scenarios)
  - `AML.TA0010` — Exfiltration (tactic; for training data exfiltration scenarios)
- **MLASWE:** MLASWE-0002 (Training Data Poisoning), MLASWE-0009 (Insufficient ML-SBOM)
- **NIST AI RMF:** MAP 1.6 (Data provenance), MEASURE 2.5 (Data quality)
- **Related Standard:** ISO/IEC 5259 (Data quality for analytics and ML)
