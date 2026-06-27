## MLASTG-TEST-DATA-002: Data Sanitization Validation

### Control Reference
- MLASVS-DATA-004: Input Validation and Sanitization
- MLASVS-DATA-005: PII/PHI Detection
- MLASVS-DATA-010: Data Minimization
- MLASVS-DATA-011: Training Data Quality Checks
- MLASVS-DATA-013: Data Labeling Security
- MLASVS-DATA-014: Cross-Contamination Prevention
- MLASVS-DATA-015: Data De-identification
- MLASVS-DATA-016: Consent and Rights Management
- MLASVS-DATA-017: Data Distribution Analysis
- MLASVS-DATA-018: Data Corruption Detection
- MLASVS-DATA-024: Automated Data Poisoning Detection (L2)
- MLASVS-DATA-025: Adversarial Data Filtering (L2)
- MLASVS-DATA-029: Synthetic Data Validation (L2)

### Severity
**Medium** (L1) / **High** (L2)

### Overview
Training data quality directly determines model reliability. Poisoned, corrupted, or poorly labeled data can introduce backdoors, biases, and adversarial vulnerabilities. This test verifies that data sanitization controls detect and prevent anomalous training data from entering the ML pipeline.

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Tools | scikit-learn (`pip install scikit-learn`), numpy, scipy |
| Access | Training dataset (raw or processed), data ingestion pipeline documentation |
| Knowledge | Data preprocessing steps and expected data distributions |

### Step-by-Step Procedure

#### Step 1: Verify Input Validation
1. Review the data ingestion pipeline for schema validation
2. Submit records with: missing required fields, invalid data types, out-of-range values, NaN/Inf values
3. **Pass if:** All invalid records are correctly rejected and errors are logged.
4. **Fail if:** Invalid records are accepted into the training pipeline without rejection.

#### Step 2: Run Outlier Detection
1. Apply Isolation Forest to the training dataset:
   ```python
   from sklearn.ensemble import IsolationForest
   import numpy as np
   
   clf = IsolationForest(contamination=0.1, random_state=42)
   predictions = clf.fit_predict(training_data)
   outlier_rate = np.sum(predictions == -1) / len(predictions)
   ```
2. Apply Local Outlier Factor:
   ```python
   from sklearn.neighbors import LocalOutlierFactor
   
   lof = LocalOutlierFactor(contamination=0.1)
   lof_predictions = lof.fit_predict(training_data)
   ```
3. **Pass if:** Outlier rate is < 15% and both methods generally agree.
4. **Fail if:** Outlier rate is ≥ 15%, indicating potential data poisoning or severe data quality issues.

#### Step 3: Verify Data Distribution Analysis
1. Compute distribution statistics for each feature (mean, std, skewness, kurtosis)
2. Compare distributions across train/validation/test splits
3. **Pass if:** Distributions are statistically consistent across splits (e.g., KS test p > 0.05).
4. **Fail if:** Significant distribution differences exist, suggesting cross-contamination or splitting errors.

#### Step 4: Verify PII Detection (L1)
1. Scan training data for PII patterns: email addresses, phone numbers, SSNs, credit card numbers
2. Verify PII detection is integrated into the data pipeline
3. **Pass if:** PII is successfully detected and handled (redacted, masked, or excluded) per policy.
4. **Fail if:** PII goes undetected or is not appropriately handled by the pipeline.

#### Step 5: Verify Label Integrity (L1)
1. Check for label consistency across annotators (if applicable)
2. Verify label distribution matches expected class balance
3. **Pass if:** Label quality metrics meet defined thresholds and no suspicious anomalies are found.
4. **Fail if:** Significant label anomalies or inconsistencies exist across the dataset.

#### Step 6: Automated Poisoning Detection (L2)
1. Inject synthetic poisoned samples (1% of dataset, with distinct statistical signatures)
2. Verify the automated detection system flags injected samples
3. **Pass if:** Detection system successfully identifies ≥ 90% of the injected poisoned samples.
4. **Fail if:** Detection system identifies < 90% of poisoned samples, or automated detection is missing.

#### Step 7: Synthetic Data Validation (L2)
1. If synthetic data is used for training, verify it passes distribution comparison against real data
2. Verify synthetic data is labeled "synthetic" in the data catalog
3. **Pass if:** Synthetic data quality metrics meet defined thresholds and are properly labeled.
4. **Fail if:** Synthetic data significantly diverges from real distributions or lacks proper catalog labeling.

### Expected Result
| Level | Expected Outcome |
|-------|-----------------|
| L1 | Input validation rejects invalid records; outlier rate < 15%; PII detected; label integrity verified |
| L2 | All L1 controls met; automated poisoning detection active; synthetic data validated |

### Evidence Requirements
- [ ] Input validation test results (invalid records rejected)
- [ ] Outlier detection results (IsolationForest + LOF)
- [ ] Data distribution analysis results
- [ ] PII detection scan results
- [ ] Label integrity analysis
- [ ] (L2) Poisoning detection test results
- [ ] (L2) Synthetic data validation results

### Remediation Guidance
**If outlier rate is high:**
1. Investigate outliers to determine if they represent real data or poisoning
2. Remove confirmed poisoned samples
3. Implement automated outlier detection in the training pipeline

**If PII is detected:**
1. Remove or mask PII before training
2. Assess regulatory exposure (GDPR, HIPAA)
3. Implement automated PII detection as a pipeline gate

### References
- **MITRE ATLAS:**
  - AML.TA0005: Execution
  - AML.T0020: Poison Training Data
- **MLASWE:** MLASWE-0002 (Data Poisoning)
- **NIST AI RMF:** MAP 1.6 (Data provenance), MEASURE 2.5 (Data quality)
