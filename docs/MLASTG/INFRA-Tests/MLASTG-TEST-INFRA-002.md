# MLASTG-TEST-INFRA-002: API Security Review

## Control Reference
MLASVS-INFRA-002 (Endpoint Auth), INFRA-003 (Endpoint Authorization), INFRA-004 (TLS), INFRA-009 (Rate Limiting), INFRA-010 (Input Size Validation), INFRA-011 (API Versioning), INFRA-021 (Continuous PenTesting - L2)

## Severity
High

## Procedure

### Step 1: Authentication Test
1. Attempt inference API calls without authentication token
2. Test with invalid/expired tokens
3. **Pass if:** API rejects unauthenticated requests with 401/403

### Step 2: TLS Verification
1. Verify all model endpoints use TLS 1.2+
2. Check for weak cipher support
3. **Pass if:** All endpoints enforce TLS 1.2+ with strong ciphers

### Step 3: Rate Limiting Test
1. Send rapid inference requests
2. Verify rate limits are enforced
3. **Pass if:** Rate limiting triggers after threshold with documented message

### Step 4: Input Validation
1. Send oversized inputs (max limit + 1)
2. Send malformed input data
3. **Pass if:** Invalid inputs are rejected with clear error messages (no stack traces)

## References
- OWASP API Security Top 10
