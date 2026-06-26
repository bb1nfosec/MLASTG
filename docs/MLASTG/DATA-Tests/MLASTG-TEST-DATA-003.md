# MLASTG-TEST-DATA-003: Differential Privacy Audit

## Control Reference
**Controls Tested:** MLASVS-DATA-019 (Differential Privacy ε-Guarantee — L2), MLASVS-DATA-022 (Secure Multi-Party Computation — L2), MLASVS-DATA-023 (Homomorphic Encryption Support — L2)

## Severity
**High** (L2 Only)

## Overview
Differential privacy provides formal mathematical guarantees that a model's training process does not leak information about individual records. This test verifies that differential privacy mechanisms are correctly implemented, that the privacy budget is tracked, and that the epsilon value meets the documented requirements.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | diffprivlib (`pip install diffprivlib`), Opacus, or TF Privacy |
| Access | Model training configuration, privacy budget documentation |
| Knowledge | Training pipeline implementation, data sensitivity classification |

## Step-by-Step Procedure

### Step 1: Verify DP Training Mechanism
1. Verify that a differential privacy training mechanism is in use:
   - DP-SGD (Differentially Private Stochastic Gradient Descent)
   - Privacy accountant from Opacus (PyTorch) or TF Privacy (TensorFlow)
   - diffprivlib for scikit-learn models
2. **Pass if:** A recognized DP training mechanism is documented and active
3. **Fail if:** No differential privacy mechanism is implemented

### Step 2: Verify Privacy Budget (ε)
1. Request the documented epsilon (ε) value from the model development team
2. Verify that ε is tracked and has not been exceeded across training runs
3. Apply the following thresholds based on data sensitivity:

   | Data Sensitivity | ε Threshold | Justification Required |
   |-----------------|-------------|----------------------|
   | Public/Non-sensitive | ≤ 10 | Standard |
   | Internal/Business | ≤ 5 | Risk assessment |
   | Sensitive (PII) | ≤ 2 | Detailed justification |
   | Highly sensitive (PHI, biometric) | ≤ 1 | CISO approval |

4. **Pass if:** ε ≤ threshold for the data sensitivity classification
5. **Fail if:** ε exceeds the threshold without documented justification

### Step 3: Verify Delta (δ) Parameter
1. Verify that δ is set to a value smaller than 1/n (where n is the training dataset size)
2. **Pass if:** δ < 1/n and is documented
3. **Fail if:** δ is missing or exceeds 1/n

### Step 4: Verify Per-Sample Gradient Clipping
1. Review the training code for gradient clipping implementation
2. Verify that gradient clipping norm is defined and enforced
3. **Pass if:** Gradient clipping is implemented with a documented clipping norm

### Step 5: Test Privacy Leakage (L2)
1. Compare model performance on a known member vs. non-member dataset
2. If membership inference attack accuracy < 60%, privacy is likely preserved
3. **Pass if:** Membership inference attack accuracy < 60%
4. **Fail if:** Attack accuracy ≥ 60%, suggesting insufficient privacy protection

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L2 | DP training mechanism active; ε ≤ threshold for data sensitivity; δ < 1/n; gradient clipping enforced; membership inference accuracy < 60% |

## Evidence Requirements

- [ ] DP training mechanism documentation
- [ ] Privacy budget (ε, δ) documentation
- [ ] Gradient clipping configuration
- [ ] Membership inference test results
- [ ] Data sensitivity classification

## Remediation Guidance

**If no DP mechanism is implemented:**
1. Integrate Opacus (PyTorch) or TF Privacy into the training pipeline
2. Define privacy budget policies based on data sensitivity
3. Add privacy accountant to the training loop

**If ε exceeds threshold:**
1. Reduce noise multiplier or increase training epochs with privacy accountant
2. Document justification if business requirements require a higher ε
3. Consider using a smaller, more sensitive dataset for high-privacy scenarios

## References
- **MITRE ATLAS:** AML.T0018 (Model Inversion), AML.TA0010 (Collection)
- **MLASWE:** MLASWE-0005 (Membership Inference)
- **NIST AI RMF:** MEASURE 2.5 (Data quality), MANAGE 2.4
- **Academic:** Dwork et al., "The Algorithmic Foundations of Differential Privacy" (2014)
