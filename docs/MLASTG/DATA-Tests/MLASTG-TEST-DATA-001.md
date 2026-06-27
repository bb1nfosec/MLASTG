## MLASTG-TEST-DATA-001: Data Provenance Verification

### Control Reference
- MLASVS-DATA-001: Data Provenance Tracking
- MLASVS-DATA-002: Cryptographic Data Integrity
- MLASVS-DATA-006: Data Lineage Documentation
- MLASVS-DATA-020: Cryptographic Data Provenance (L2)
- MLASVS-DATA-026: Real-time Data Integrity Monitoring (L2)
- MLASVS-DATA-030: Data Trust Scoring (L2)

### Severity
**Medium** (L1) / **High** (L2)

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Access | Data catalog or dataset storage system |
| Tools | `sha256sum`, `openssl` or equivalent |
| Documentation | Data ingestion pipeline documentation |
| Additional (L2) | Access to CI/CD pipeline logs, data source manifests |

### Step-by-Step Procedure

#### Step 1: Inventory Training Datasets
1. Identify all datasets used for model training, validation, and testing
2. Document dataset names, sources, collection dates, and responsible parties
3. Review data catalog entries for completeness
4. **Pass if:** All datasets used for training, validation, and testing are successfully identified and documented.
5. **Fail if:** Any dataset used in the ML lifecycle is undocumented or missing from the inventory.

#### Step 2: Verify Data Origin Documentation
1. Check that each dataset has documented:
   - Source system or data provider
   - Collection methodology
   - Collection date range
   - Responsible team or individual
   - Intended use case
2. **Pass if:** All training datasets have complete origin documentation.
3. **Fail if:** Any training dataset lacks origin documentation or the documentation is incomplete.

#### Step 3: Verify Cryptographic Integrity
1. Locate stored SHA-256 (or stronger) hashes for each dataset
2. Recompute hashes:
   ```bash
   sha256sum training_dataset_v1.csv
   ```
3. Compare recomputed hashes against stored values
4. **Pass if:** All recomputed hashes match the stored values exactly.
5. **Fail if:** Any hash fails to match, indicating potential data corruption or unauthorized tampering.

#### Step 4: Review Data Lineage (L1)
1. Identify all data transformation steps applied
2. Verify transformations are documented in version-controlled pipeline code
3. Confirm raw data can be reproduced from transformations
4. **Pass if:** The complete transformation pipeline is documented and version-controlled.
5. **Fail if:** Data transformations are undocumented, manual, or not version-controlled.

#### Step 5: Verify Lineage Reproducibility (L1)
1. Execute the data pipeline from raw data to processed output
2. Compare final processed data hash against original training hash
3. **Pass if:** Reproduced data hash matches the training data hash exactly.
4. **Fail if:** The reproduced hash differs from the original training hash, indicating non-deterministic processing or undocumented changes.

#### Step 6: Verify Signed Manifests (L2)
1. Locate signed data provenance manifests for each dataset
2. Verify signature chain:
   ```bash
   openssl verify -CAfile ca-cert.pem -untrusted intermediate.pem manifest.sig
   ```
3. Check that manifest covers full transformation history
4. **Pass if:** All manifests are valid, cover the full transformation history, and are signed by authorized parties.
5. **Fail if:** Manifests are invalid, unsigned, missing, or do not cover the full history.

#### Step 7: Test Real-time Integrity Monitoring (L2)
1. For continuous learning systems, inject a corrupted data record
2. Verify that the monitoring system detects and alerts on integrity failure
3. Check that the corrupted record is quarantined or rejected
4. **Pass if:** The monitoring system detects the integrity failure within defined SLAs and appropriately quarantines the record.
5. **Fail if:** The system fails to detect the corrupted record or allows it to proceed into the training pipeline.

#### Step 8: Evaluate Data Trust Scoring (L2)
1. Review data source trust scoring methodology
2. Verify that all data sources have assigned trust scores
3. Check that low-trust sources trigger additional verification
4. **Pass if:** Trust scoring is implemented for all sources and appropriately triggers verification for low-trust data.
5. **Fail if:** Trust scoring is absent, incomplete, or ignored in the pipeline.

### Expected Result
| Level | Expected Outcome |
|-------|-----------------|
| L1 | All datasets have documented provenance, verified hashes, and reproducible lineage |
| L2 | All datasets have signed provenance manifests, integrity monitoring, and trust scoring |

### Evidence Requirements
- [ ] Dataset inventory with provenance documentation
- [ ] Hash verification logs for each dataset
- [ ] Data lineage documentation
- [ ] (L2) Signed provenance manifests
- [ ] (L2) Integrity monitoring test results
- [ ] (L2) Trust scoring methodology and results

### Remediation Guidance
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

### References
- **MITRE ATLAS:**
  - AML.T0020: Poison Training Data
  - AML.T0059: Backdoor ML Model
  - AML.TA0009: Collection
  - AML.TA0010: Exfiltration
- **MLASWE:** MLASWE-0002 (Training Data Poisoning), MLASWE-0009 (Insufficient ML-SBOM)
- **NIST AI RMF:** MAP 1.6 (Data provenance), MEASURE 2.5 (Data quality)
- **Related Standard:** ISO/IEC 5259 (Data quality for analytics and ML)
