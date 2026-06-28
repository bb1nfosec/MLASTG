# MLASVS-INFRA-2: API Security

## Category
MLASVS-INFRA: Runtime & Infrastructure

## Overview
ML inference APIs are the primary interface to model functionality and must be secured against abuse, extraction, DoS attacks, and data leakage.

## Controls

### INFRA-002: Inference Endpoint Authentication (L1)
**Description:** All inference endpoints must require authentication before processing requests.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify API key, OAuth token, or IAM authentication is enforced
2. Test by sending an unauthenticated request — must receive 401 or 403
3. **Pass if:** All endpoints require authentication

**Remediation:** Implement API key authentication or OAuth 2.0. Use API gateways (Kong, AWS API Gateway, Envoy) for centralized auth.

---

### INFRA-003: Inference Endpoint Authorization (L1)
**Description:** Authorization must enforce per-user or per-role access limits.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify RBAC is configured for model endpoints
2. Check that users can only access models they are authorized for
3. **Pass if:** Authorization is enforced per user/role

**Remediation:** Implement fine-grained authorization (e.g., user → model mapping). Use ABAC/RBAC for access decisions.

---

### INFRA-004: TLS for Model Endpoints (L1)
**Description:** All inference traffic must be encrypted in transit.
**MITRE ATLAS:** AML.TA0010 (Collection)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify TLS 1.2+ is enforced for all model endpoints
2. Check cipher strength (AES-256-GCM or stronger) and certificate validity
3. **Pass if:** TLS is enforced with strong ciphers and valid certificates

**Remediation:** Enforce HTTPS-only access. Use TLS 1.3 where possible. Configure HSTS headers.

---

### INFRA-009: API Rate Limiting (L1)
**Description:** Rate limiting must be configured per user/API key to prevent extraction and DoS.
**MITRE ATLAS:** AML.T0024.002 (Extract AI Model)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify rate limits are configured (requests per second/minute per user)
2. Test that exceeding the limit triggers 429 Too Many Requests
3. **Pass if:** Rate limits are active and enforced

**Remediation:** Configure rate limiting at API gateway level. Set limits based on model serving capacity and acceptable query budgets.

---

### INFRA-010: Input Size Validation (L1)
**Description:** Input payload size must be validated to prevent resource exhaustion.
**MITRE ATLAS:** AML.T0029 (Denial of AI Service)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify maximum input size limits are defined and configured
2. Test with inputs exceeding the limit — must be rejected with 413
3. **Pass if:** Large inputs are rejected before reaching the model

**Remediation:** Set maximum request body size at the API gateway. Validate input dimensions against model input shape before inference.

---

### INFRA-011: API Versioning (L1)
**Description:** API versions must be maintained with a deprecation policy.
**MITRE ATLAS:** AML.TA0002 (Initial Access)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify API versioning strategy (URL path, header, or parameter based)
2. Check that deprecated versions have documented sunset dates
3. **Pass if:** API versions are managed with versioning and deprecation policy

**Remediation:** Implement URL-based versioning (`/v1/model`, `/v2/model`). Publish deprecation schedule with minimum 6-month notice for breaking changes.

---

### INFRA-021: Continuous Penetration Testing (L2)
**Description:** Model APIs must undergo regular penetration testing.
**MITRE ATLAS:** AML.TA0001 (Reconnaissance)
**Test Reference:** MLASTG-TEST-INFRA-002

**Verification:**
1. Verify penetration testing schedule (quarterly minimum)
2. Check that findings are tracked to remediation in a ticketing system
3. **Pass if:** Regular API penetration testing is conducted with tracked remediation

**Remediation:** Schedule quarterly API penetration tests. Include ML-specific test cases (extraction, adversarial, prompt injection) in the test scope.

## Cross-References
- OWASP API Security Top 10
- MITRE ATLAS: AML.TA0001, AML.TA0002, AML.T0010, AML.T0024.002, AML.T0029
