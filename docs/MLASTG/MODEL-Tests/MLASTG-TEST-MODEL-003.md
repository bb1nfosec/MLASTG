# MLASTG-TEST-MODEL-003: Membership Inference Testing

## Control Reference
MLASVS-MODEL-009 (Inference Logging), MODEL-011 (Output Sanitization), MODEL-013 (Model Behavior Monitoring), MODEL-019 (Differential Privacy - L2), MODEL-020 (Membership Inference Prevention - L2)

## Severity
Medium

## Prerequisites
- Model API with confidence scores
- Known training data samples (50+) and non-training data samples (50+)

## Procedure

### Step 1: Membership Inference Attack
1. Shadow model training approach:
   - Train shadow models on data resembling training set
   - Build attack classifier on shadow model outputs
   - Apply attack to target model
2. Measure attack accuracy above random guessing (50%)

### Step 2: Verify Differential Privacy (L2)
1. Request DP audit from model development team
2. Verify ε (privacy budget) is documented
3. **Pass if:** ε ≤ 8 for L1, ε ≤ 2 for L2, or documented alternative

### Step 3: Verify Inference Logging
1. Review inference logs for completeness
2. Verify logs don't contain raw PII
3. **Pass if:** Inferences are logged with anonymized identifiers

## References
- MITRE ATLAS: AML.T0018
- MLASWE: MLASWE-0004, MLASWE-0005
