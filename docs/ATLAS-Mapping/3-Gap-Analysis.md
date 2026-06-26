# MLASTG → ATLAS Gap Analysis

## Overview
This document identifies MITRE ATLAS techniques that have **no or insufficient coverage** by MLASVS controls. These are priority areas for developing new controls and test cases. This analysis is updated for v0.1 (Draft) and reflects the current state of MLASVS controls and MLASTG test cases.

## 🔴 Critical Gaps: No Coverage

| ATLAS ID | Technique | Risk | Recommended New Control | Remediation |
|----------|-----------|------|------------------------|-------------|
| — | ML Model Inventory Discovery | Medium | GOV-016a: Model inventory obfuscation; restrict API discovery endpoints | Implement API endpoint obfuscation; require authentication for model metadata queries; monitor for enumeration patterns |

**Impact:** An adversary can discover what ML models an organization uses without any defensive detection. No official ATLAS ID exists for this attack path — tracked as MLASTG-internal gap.

**Remediation Steps:**
1. Document all production ML model endpoints in an internal inventory
2. Remove or restrict public-facing model metadata endpoints (e.g., `/models`, `/health`)
3. Implement authentication for model discovery queries
4. Monitor for systematic model enumeration patterns in API access logs
5. Consider model endpoint obfuscation (randomized URLs, service mesh routing)

## 🟡 Partial Coverage: Techniques Needing Enhancement

### Reconnaissance (AML.TA0001)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| Only red team exercises (GOV-016) and pen testing (INFRA-021) provide indirect coverage | No technical detection controls for ML-specific reconnaissance | Add MLASVS-GOV control for reconnaissance detection monitoring |

**Remediation Steps:**
1. Implement monitoring for ML-specific reconnaissance patterns:
   - Systematic API probing across model versions
   - Unusual access patterns to model documentation or metadata
   - Queries that map model capabilities or architecture
2. Add detection rules to SIEM for ML endpoint enumeration
3. Include ML reconnaissance scenarios in red team exercises

### Initial Access — Valid Accounts (AML.TA0002)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| DATA-003 and GOV-001 cover inventory but not usage monitoring | No ML-specific account usage monitoring | Add MLASVS-INFRA control for ML-specific account monitoring |

**Remediation Steps:**
1. Implement per-user ML API usage dashboards
2. Alert on access from new IP addresses or unusual geographic locations
3. Monitor for privilege escalation attempts on ML platform accounts
4. Implement session timeout for ML platform access

### Resource Development — Acquire ML Model (AML.TA0003.001)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| SUPPLY-002, 006, 009 cover vetting but not ongoing monitoring | No continuous monitoring of base model sources | Add MLASVS-SUPPLY control for continuous base model monitoring |

**Remediation Steps:**
1. Subscribe to security advisories for ML model repositories (Hugging Face, PyTorch Hub)
2. Implement automated re-scanning of base models when new vulnerabilities are disclosed
3. Monitor model repository for updates, deprecations, or security incidents
4. Establish a process for rapid model replacement when base models are compromised

### Persistence — Backdoor ML Model (AML.TA0006)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| MODEL-021/022 (L2) have detection but no automated prevention | No automated backdoor prevention at training time | Add MLASVS-MODEL control for automated training-time prevention |

**Remediation Steps:**
1. Implement activation clustering as a training-time defense
2. Add data sanitization checks before training begins
3. Use certified robustness methods where applicable
4. Implement continuous monitoring for backdoor behavior in production

### Collection — Model Inversion (AML.T0018)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| MODEL-019/020 (L2) and INFRA-016 exist but no L1 baseline | No L1 inversion prevention controls | Add MLASVS-MODEL L1 control for output clipping |

**Remediation Steps:**
1. Implement L1 output clipping: limit confidence score precision to ≤ 3 decimal places
2. Return label-only predictions where full probability vectors are not required
3. Apply prediction perturbation for sensitive deployments
4. Monitor for systematic querying patterns indicative of inversion attacks

### Impact — Data Poisoning (AML.T0020)

| Current State | Gap | Remediation |
|--------------|-----|-------------|
| DATA-024/025 (L2) exist but no L1 automated detection | No L1 statistical poisoning detection | Add MLASVS-DATA L1 control for statistical checks |

**Remediation Steps:**
1. Implement statistical outlier detection in the training pipeline (Isolation Forest, LOF)
2. Add label consistency checks before training
3. Monitor data distribution shifts between training runs
4. Implement data versioning with tamper-evident logging

## Coverage Improvement Roadmap

### P0 — Immediate (v0.2)

| Priority | Tactic | Technique | Action | Effort | Impact |
|----------|--------|-----------|--------|--------|--------|
| P0 | Reconnaissance (TA0001) | Model Discovery | Add MLASVS-GOV control for discovery monitoring | Medium | Eliminates the only zero-coverage area |
| P0 | Impact (TA0020) | Data Poisoning | Add L1 statistical poisoning detection | Medium | Upgrades poisoning to Full coverage |

### P1 — Short-term (v0.3)

| Priority | Tactic | Technique | Action | Effort | Impact |
|----------|--------|-----------|--------|--------|--------|
| P1 | Collection (TA0010) | Model Inversion | Add L1 output clipping control | Low | Upgrades inversion to Full coverage |
| P1 | Persistence (TA0006) | Backdoor | Add automated training-time prevention | High | Strengthens backdoor detection |

### P2 — Medium-term (v0.4+)

| Priority | Tactic | Technique | Action | Effort | Impact |
|----------|--------|-----------|--------|--------|--------|
| P2 | Reconnaissance (TA0001) | Model Fingerprinting | Add model fingerprint detection controls | Medium | Covers architecture discovery attacks |
| P2 | Collection (TA0010) | Training Data Exfiltration | Add L1 exfiltration detection | Medium | Upgrades data exfiltration to Full |
| P2 | Resource Development (TA0003) | Acquire ML Model | Add continuous base model monitoring | Medium | Strengthens supply chain controls |

### P3 — Long-term (v0.5+)

| Priority | Tactic | Technique | Action | Effort | Impact |
|----------|--------|-----------|--------|--------|--------|
| P3 | All | Multimodal ML | Extend controls to vision-language models | High | New attack surface coverage |
| P3 | All | Reinforcement Learning | Add RL-specific controls (reward poisoning) | High | New ML paradigm coverage |
| P3 | All | Federated Learning | Add federated learning security controls | High | Cross-organizational ML |

## Complete Unmapped ATLAS Techniques

The following ATLAS techniques/sub-techniques fall outside current MLASTG scope but should be evaluated for future coverage:

| ATLAS ID | Technique | Current Status | Recommended Action | Priority |
|----------|-----------|---------------|-------------------|----------|
| AML.T0040 | ML Supply Chain (AI Bill of Materials) | Partially covered by ML-SBOM (SUPPLY-001) | Dedicated NTIA-compliant SBOM control | P1 |
| AML.T0041 | ML Supply Chain (External ML Services) | Covered by SUPPLY-020 (vendor assessment) | Enhance with API-specific controls | P2 |
| AML.T0042 | ML Attack Staging | Not covered | Add staging environment security controls | P2 |
| AML.T0043 | ML Output Handling | Covered by LLM-003/008/009 (LLM-specific) | Extend to non-LLM ML output handling | P2 |
| AML.T0057 | LLM Data Disclosure | Covered by LLM-008/009 | Verify comprehensive coverage | P1 |
| AML.T0058 | LLM DoS / Resource Exhaustion | Covered by LLM-005/011/012/013 | Verify comprehensive coverage | P1 |

## Coverage Statistics (v0.1)

| Metric | Value | Trend |
|--------|-------|-------|
| Total ATLAS techniques mapped | 18 | — |
| 🟢 Full coverage | 13 (72%) | Target: 85% by v0.3 |
| 🟡 Partial coverage | 4 (22%) | Target: 10% by v0.3 |
| 🔴 No coverage | 1 (6%) | Target: 0% by v0.2 |
| MLASVS controls mapped | 64 of 168 (38%) | Target: 50% by v0.3 |
| MLASTG test cases mapped | 14 of 14 (100%) | ✅ Complete |
| MLASWE weaknesses connected | 9 of 12 (75%) | Target: 100% by v0.2 |

## How to Close Gaps

1. **For "None" techniques:** Create new MLASVS controls following the existing template format in `docs/MLASVS/`
2. **For "Partial" techniques:** Add missing L2 controls or dedicated test cases
3. **For unmapped techniques:** Evaluate relevance and add to roadmap
4. **Update cadence:** Re-run this analysis after each major framework update (minimum quarterly)
5. **Validation:** After adding new controls, update the Coverage Matrix and Navigator JSON

## Cross-Framework Gap Alignment

| Framework | Gap Area | MLASTG Coverage | Action Needed |
|-----------|----------|----------------|---------------|
| MITRE ATLAS | Reconnaissance detection | 🔴 None | Add GOV control |
| OWASP LLM Top 10 | LLM09 (Overreliance) | 🟡 Partial (GOV controls) | Add dedicated LLM control |
| OWASP ML Top 10 | ML10 (Model Theft) | 🟢 Full (MODEL-004/005/006) | Verify test coverage |
| NIST AI RMF | MAP 1.6 (Data provenance) | 🟢 Full (DATA-001/006) | Verify test coverage |
| EU AI Act | Art. 14 (Human oversight) | 🟡 Partial (GOV-012) | Strengthen L1 baseline |
