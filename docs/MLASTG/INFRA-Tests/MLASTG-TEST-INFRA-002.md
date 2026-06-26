# MLASTG-TEST-INFRA-002: Inference API Security Review

## Control Reference
**Controls Tested:** MLASVS-INFRA-002 (Inference Endpoint Authentication), MLASVS-INFRA-003 (Inference Endpoint Authorization), MLASVS-INFRA-004 (TLS for Model Endpoints), MLASVS-INFRA-009 (API Rate Limiting), MLASVS-INFRA-010 (Input Size Validation), MLASVS-INFRA-011 (API Versioning), MLASVS-INFRA-021 (Continuous Penetration Testing — L2)

## Severity
**High** (L1) / **Critical** (L2)

## Overview
ML inference APIs expose model predictions to consumers and attackers alike. Weak authentication, missing TLS, absent rate limiting, or inadequate input validation can enable model extraction attacks, denial-of-service, and privilege escalation. This test applies the OWASP API Security Top 10 to ML-specific inference endpoints.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `curl`, `openssl`, `nmap`, Postman or any HTTP testing tool |
| Access | Inference API endpoint URL; valid and invalid API credentials for testing |
| Documentation | API specification (OpenAPI/Swagger); documented rate limits and token limits |

## Step-by-Step Procedure

### Step 1: Authentication Testing
1. Attempt an inference request with no authentication token:
   ```bash
   curl -X POST https://api.example.com/v1/predict \
     -H 'Content-Type: application/json' \
     -d '{"input": [0.1, 0.2, 0.3]}'
   ```
2. Attempt with an invalid/malformed token:
   ```bash
   curl -X POST https://api.example.com/v1/predict \
     -H 'Authorization: Bearer invalid_token_here' \
     -H 'Content-Type: application/json' \
     -d '{"input": [0.1, 0.2, 0.3]}'
   ```
3. Attempt with an expired token (if you can obtain or construct one)
4. **Pass if:** All unauthenticated and invalid-token requests return HTTP 401 or 403 with a generic error message (no stack traces or internal details)
5. **Fail if:** Any unauthenticated request succeeds, or error responses expose internal information

### Step 2: Authorization Testing
1. If multiple roles exist (e.g., read-only vs. admin), attempt to access admin operations using a read-only token
2. Attempt to query models that the authenticated user is not authorized to access
3. **Pass if:** Authorization is enforced per resource; role boundaries cannot be crossed

### Step 3: TLS Configuration Verification
1. Verify all inference endpoints use HTTPS/TLS:
   ```bash
   openssl s_client -connect api.example.com:443 -tls1_2
   openssl s_client -connect api.example.com:443 -tls1_1  # Should fail
   ```
2. Verify TLS version: only TLS 1.2 and TLS 1.3 should be accepted; TLS 1.0 and 1.1 should be rejected
3. Check cipher suite strength (no RC4, DES, 3DES, or export-grade ciphers):
   ```bash
   nmap --script ssl-enum-ciphers -p 443 api.example.com
   ```
4. **Pass if:** All endpoints enforce TLS 1.2+; only strong cipher suites are accepted; no deprecated protocol versions accepted
5. **Fail if:** TLS 1.0/1.1 is accepted, or weak ciphers are supported

### Step 4: Rate Limiting Verification
1. Send a burst of inference requests (e.g., 200 requests in 10 seconds):
   ```bash
   for i in {1..200}; do
     curl -s -o /dev/null -w "%{http_code}\n" \
       -X POST https://api.example.com/v1/predict \
       -H "Authorization: Bearer $TOKEN" \
       -H 'Content-Type: application/json' \
       -d '{"input": [0.1, 0.2, 0.3]}'
   done | sort | uniq -c
   ```
2. Verify that requests above the rate limit threshold return HTTP 429 (Too Many Requests)
3. Verify the response includes a `Retry-After` header or equivalent guidance
4. **Pass if:** Rate limiting triggers with HTTP 429 after the documented threshold; threshold and response are documented
5. **Fail if:** No rate limiting is enforced, or the threshold is undocumented

### Step 5: Input Size and Format Validation
1. Send an input payload exceeding the documented maximum size by 10%:
   ```bash
   # Generate oversized input
   python3 -c "import json; print(json.dumps({'input': [0.1] * 100000}))" > oversized.json
   curl -X POST https://api.example.com/v1/predict \
     -H "Authorization: Bearer $TOKEN" \
     -H 'Content-Type: application/json' \
     -d @oversized.json
   ```
2. Send malformed inputs:
   - Incorrect data type (string where float expected)
   - Missing required fields
   - NaN and Infinity values
   - Deeply nested JSON structures
3. **Pass if:** All invalid inputs are rejected with HTTP 400 and a clear error message; no stack traces, file paths, or internal error details are exposed
4. **Fail if:** Oversized or malformed inputs are processed, or error responses expose internal details

### Step 6: API Versioning Verification
1. Verify that the API supports versioning (e.g., `/v1/predict`, `/v2/predict`)
2. Verify that deprecated API versions return appropriate responses (301 redirect or 410 Gone) with a sunset date
3. **Pass if:** API versioning is implemented and documented; deprecated versions have a defined sunset policy

### Step 7: Continuous Penetration Testing (L2)
1. Verify that scheduled or continuous API penetration testing is configured
2. Review the most recent pentest report for the inference API
3. Verify all HIGH/CRITICAL findings from the last pentest have been remediated
4. **Pass if:** Pentest was conducted within the last 6 months; all critical findings remediated

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Unauthenticated requests rejected; TLS 1.2+ enforced with strong ciphers; rate limiting active; invalid inputs rejected without internal error exposure |
| L2 | All L1 controls met; continuous penetration testing scheduled; last pentest report < 6 months old with critical findings remediated |

## Evidence Requirements

- [ ] Authentication rejection test results (401/403 on unauthenticated requests)
- [ ] TLS version and cipher suite scan results
- [ ] Rate limiting test results (429 response with documented threshold)
- [ ] Input validation test results (oversized + malformed inputs rejected)
- [ ] API versioning documentation
- [ ] (L2) Most recent penetration test report with finding remediation status

## Remediation Guidance

**If authentication is missing:**
1. Implement API key or OAuth 2.0 bearer token authentication at the API gateway
2. Enforce authentication as a middleware layer so no endpoint can be bypassed

**If TLS is weak:**
1. Disable TLS 1.0 and 1.1 at the load balancer / API gateway
2. Configure a strong cipher suite list (ECDHE + AES-GCM, ChaCha20-Poly1305)
3. Set up certificate monitoring to alert before certificate expiry

**If rate limiting is absent:**
1. Implement rate limiting at the API gateway layer (not just the application layer)
2. Define per-user, per-key, and per-IP limits
3. Log rate limit events to the SIEM for extraction attack detection

**If error responses expose internals:**
1. Implement a global error handler that returns generic error messages
2. Log full error details server-side only; never expose stack traces to clients

## References
- **MITRE ATLAS:**
  - `AML.T0034` — ML Inference API Access
  - `AML.T0040` — ML Service Disruption (DoS context)
- **OWASP API Security Top 10:** API1 (Broken Object Level Authorization), API2 (Broken Authentication), API4 (Unrestricted Resource Consumption), API8 (Security Misconfiguration)
- **MLASWE:** MLASWE-0012 (Insufficient Runtime Monitoring), MLASWE-0014 (Insecure ML API)
- **NIST AI RMF:** MANAGE 2.4, MEASURE 2.5
