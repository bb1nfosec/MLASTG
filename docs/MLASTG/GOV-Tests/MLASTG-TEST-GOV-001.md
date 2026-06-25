# MLASTG-TEST-GOV-001: Governance & Compliance Audit

## Control Reference
MLASVS-GOV-001 through 020 (all governance controls)

## Severity
Medium

## Procedure

### Step 1: ML System Inventory
1. Verify comprehensive inventory of all ML systems exists
2. Check that each system has risk classification
3. **Pass if:** Complete inventory with risk classification

### Step 2: Model Documentation
1. Verify model cards exist for each production model
2. Check that model cards include: intended use, limitations, training data, performance metrics, bias assessment
3. **Pass if:** Model cards exist and are complete

### Step 3: Incident Response Plan
1. Verify ML-specific incident response plan exists
2. Check that plan covers: data poisoning, model theft, adversarial attack, supply chain compromise
3. **Pass if:** IR plan covers ML-specific scenarios

### Step 4: Bias Assessment (L2)
1. Verify bias evaluation has been conducted
2. Check for disparate impact across demographic groups
3. **Pass if:** Bias evaluation is documented with mitigation plan if needed

### Step 5: Regulatory Compliance (L2)
1. Map ML system to applicable regulations (EU AI Act, HIPAA, etc.)
2. Verify compliance documentation
3. **Pass if:** Regulatory mapping is documented with compliance status

## References
- NIST AI RMF: Govern, Map, Measure, Manage
- EU AI Act conformity requirements
