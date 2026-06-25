# MLASTG-TEST-MODEL-002: Extraction Resistance Testing

## Control Reference
MLASVS-MODEL-004 (Output Confidence Calibration), MODEL-005 (API Rate Limiting), MODEL-006 (Access Control), MODEL-018 (Extraction Resistance - L2), MODEL-023 (Model Watermarking - L2)

## Severity
High

## Prerequisites
- API access to model endpoint
- Ability to send at least 10,000 queries (for extraction simulation)
- Query budget tracking

## Procedure

### Step 1: Verify Output Precision
1. Query the model and examine output precision
2. Check that confidence scores have limited decimal places (≤ 3 recommended)
3. **Pass if:** Output precision is limited to reasonable granularity

### Step 2: Verify Rate Limiting
1. Send requests at increasing rates
2. Identify rate limit thresholds
3. **Pass if:** Rate limits are enforced per user/API key

### Step 3: Verify Authentication
1. Attempt unauthenticated inference requests
2. Verify token validation
3. **Pass if:** All inference endpoints require authentication

### Step 4: Surrogate Model Training (L2)
1. Collect 10,000+ query-response pairs
2. Train a surrogate model on collected data
3. Compare surrogate vs. target model accuracy on held-out test set
4. **Pass if:** Surrogate model achieves < 80% of target model accuracy

### Step 5: Verify Watermarking (L2)
1. Query with known watermark triggers
2. Verify watermark appears in outputs
3. **Pass if:** Model outputs contain detectable watermarks

## References
- MITRE ATLAS: AML.T0034
- MLASWE: MLASWE-0003
