# MLASTG-TEST-SUPPLY-002: Model Provenance Verification

## Control Reference
MLASVS-SUPPLY-002 (Origin Verification), SUPPLY-006 (Hash Verification), SUPPLY-007 (Transfer Learning Validation), SUPPLY-009 (Vulnerability Scanning), SUPPLY-011 (Secure Distribution), SUPPLY-012 (Third-Party Evaluation), SUPPLY-015 (Cryptographic Provenance - L2), SUPPLY-016 (Model Signing - L2), SUPPLY-018 (Base Model Robustness - L2), SUPPLY-019 (Backdoor Scanning - L2), SUPPLY-020 (Vendor Assessment - L2), SUPPLY-022 (Reproducible Build - L2)

## Severity
High

## Procedure

### Step 1: Pre-Trained Model Verification
1. For each pre-trained model used, verify:
   - Source URL and version
   - Cryptographic hash (SHA-256)
   - Model card or documentation
2. **Pass if:** All pre-trained models have documented, verified origins

### Step 2: Hash Verification at Load
1. Check that model loading code includes hash verification
2. Modify model file and verify detection
3. **Pass if:** Tampered model files are detected and rejected

### Step 3: Base Model Scanning (L2)
1. Run model security scanner (e.g., ModelScan) on model files
2. Check for unsafe serialization (e.g., pickle `__reduce__`)
3. **Pass if:** No unsafe code patterns detected

## References
- MITRE ATLAS: AML.TA0003
- MLASWE: MLASWE-0009
