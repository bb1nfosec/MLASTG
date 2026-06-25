# MLASVS-DATA-1: Data Provenance

## Category
MLASVS-DATA: Data Security & Privacy

## Overview
Data provenance ensures that every dataset used in ML training, evaluation, and inference has a verifiable origin, transformation history, and integrity chain. Without provenance, poisoned or compromised data can enter the ML pipeline undetected.

## Controls

### DATA-001: Data Provenance Tracking (L1)
**Description:** All datasets used for ML training must have documented provenance including source, collection method, date, and responsible party.

**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Review dataset documentation for provenance information
2. Verify that all training datasets include source tracking
3. Confirm that labeled data sources are identified

**Remediation:** Implement a data catalog system that automatically captures dataset metadata during ingestion.

---

### DATA-002: Cryptographic Data Integrity (L1)
**Description:** All training datasets must have cryptographic hashes (SHA-256 or stronger) recorded at time of acquisition and verifiable at time of use.

**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Verify that SHA-256 hashes were computed and stored for each dataset
2. Recompute hashes and compare against stored values
3. Check that hash verification is performed before training begins

**Remediation:** Automate hash computation in the data ingestion pipeline with integrity checks before each training run.

---

### DATA-006: Data Lineage Documentation (L1)
**Description:** All data transformations, preprocessing steps, and augmentations applied to training data must be documented and reproducible.

**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Review pipeline code for data transformation steps
2. Verify that preprocessing pipelines are version-controlled
3. Confirm that data transformations are reproducible from raw data

**Remediation:** Use ML pipeline tools (Kubeflow, MLflow, TFX) that automatically capture data lineage.

---

### DATA-020: Cryptographic Data Provenance (L2)
**Description:** Full cryptographic provenance chain using signed manifests or transparency logs for all training datasets.

**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Verify that signed manifests exist for each dataset version
2. Check that provenance chain covers source → transformation → training
3. Validate signature chain integrity

**Remediation:** Implement sigstore-style signing for datasets or use a transparency log (e.g., Rekor).

---

### DATA-026: Real-time Data Integrity Monitoring (L2)
**Description:** For continuous learning systems, data integrity must be monitored in real-time during the data ingestion pipeline.

**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Verify that streaming data pipelines include integrity checks
2. Confirm that integrity failures trigger alerts
3. Check that drift detection is applied to incoming data distributions

**Remediation:** Implement real-time data validation using tools like Apache Beam validation transforms or custom streaming checks.

---

### DATA-030: Data Trust Scoring (L2)
**Description:** Each data source must be assigned a trust score based on provenance completeness, historical integrity, and source reputation.

**MITRE ATLAS:** AML.TA0009 (Discovery)
**Test Reference:** MLASTG-TEST-DATA-001

**Verification:**
1. Review data source trust scoring methodology
2. Verify that low-trust sources are flagged for human review
3. Confirm that trust scores are factored into automated data selection

**Remediation:** Implement a data quality/trust framework with quantitative scoring criteria.

## Cross-References

- **MITRE ATLAS:** AML.TA0009, AML.TA0010
- **OWASP ML Top 10:** ML04 (Supply Chain), ML08 (Transfer Learning)
- **NIST AI RMF:** MAP-1, MAP-2, MEASURE-2
- **OWASP AI Exchange:** Data Limitation, Development-time Threats
