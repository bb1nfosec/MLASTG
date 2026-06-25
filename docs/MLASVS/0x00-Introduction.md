# MLASVS — MLSec Application Security Verification Standard

**Version 0.1 (Draft)**

> The MLASVS defines **what** to verify in machine learning systems. It is the requirements layer of the MLASTG framework, analogous to the OWASP MASVS for mobile applications.

---

## 1. What Is the MLASVS?

The **MLSec Application Security Verification Standard (MLASVS)** is a comprehensive set of security requirements (controls) for machine learning systems. It covers:

- **Traditional ML models** — Classifiers, regressors, clustering models
- **Deep neural networks** — CNNs, RNNs, transformers, GANs
- **Large language models (LLMs)** — GPT-style models, chatbots, RAG systems
- **ML infrastructure** — Pipelines, feature stores, model registries, serving infrastructure

Each control is:
- **Testable** — Can be verified through defined procedures
- **Actionable** — Provides clear implementation guidance
- **Mappable** — Linked to MITRE ATLAS tactics, OWASP LLM Top 10, and NIST AI RMF
- **Scalable** — Offered at two security levels (L1 and L2)

---

## 2. Control Categories

| ID | Category | Focus Area | Control Count |
|----|----------|------------|---------------|
| [MLASVS-DATA](V1-DATA/0x10-Data-Security-Overview.md) | **Data Security & Privacy** | Data provenance, sanitization, differential privacy, access control | 18 L1 / 12 L2 |
| [MLASVS-MODEL](V2-MODEL/0x20-Model-Security-Overview.md) | **Model Security** | Adversarial robustness, extraction prevention, inversion, backdoors | 15 L1 / 15 L2 |
| [MLASVS-LLM](V3-LLM/0x30-LLM-Security-Overview.md) | **LLM Security** | Prompt injection, output handling, agency control, context isolation | 14 L1 / 10 L2 |
| [MLASVS-SUPPLY](V4-SUPPLY/0x40-Supply-Chain-Overview.md) | **Supply Chain Security** | ML-SBOM, base model vetting, dependency security | 12 L1 / 10 L2 |
| [MLASVS-PIPELINE](V5-PIPELINE/0x50-Pipeline-Overview.md) | **Pipeline & MLOps** | CI/CD, model registry, artifact integrity, feature stores | 10 L1 / 10 L2 |
| [MLASVS-INFRA](V6-INFRA/0x60-Runtime-Overview.md) | **Runtime & Infrastructure** | Model serving, API security, monitoring, incident response | 12 L1 / 10 L2 |
| [MLASVS-GOV](V7-GOV/0x70-Governance-Overview.md) | **Governance & Compliance** | Risk governance, bias/fairness, audit, regulatory compliance | 10 L1 / 10 L2 |

**Total:** 91 L1 controls + 77 L2 controls = **168 verifiable controls**

---

## 3. Security Levels

### L1 — Standard Security
Applies to all ML systems in production. Covers fundamental controls:
- Data access control and basic provenance
- Input validation and sanitization
- Basic adversarial robustness testing
- Standard supply chain verification
- Essential logging and monitoring
- Model registry and version control

### L2 — Defense-in-Depth
Applies to high-risk, enterprise, defense, and regulated environments. Adds:
- Full data provenance with cryptographic verification
- Differential privacy guarantees
- Rigorous adversarial robustness certification (certified adversarial defenses)
- Comprehensive ML-SBOM with continuous scanning
- Runtime model monitoring with automated incident response
- Full red teaming with adversarial attack simulation
- Regulatory compliance verification (EU AI Act, etc.)

---

## 4. Control Format

Each MLASVS control follows this template:

```
MLASVS-{CATEGORY}-{NUMBER}:
  Description:     One-line description of the control
  Category:        MLASVS-{CATEGORY}
  Level:           L1 | L2
  MITRE ATLAS:     AML.T#### — Technique name
  OWASP LLM:       LLM0X (if applicable)
  NIST AI RMF:     Map, Measure, Manage, or Govern
  Assessment:      [x] Pass / [ ] Fail / [ ] N/A
  Weakness Ref:    MLASWE-XXXX
  Test Reference:  MLASTG-TEST-XXXX
```

---

## 5. Relationship to Other Frameworks

```
MITRE ATLAS            ─── Tactics & Techniques (adversary perspective)
     │
     ▼
MLASVS                 ─── Security Controls (defender perspective)
     │
     ├── Mapped to ───► NIST AI RMF (Govern, Map, Measure, Manage)
     ├── Mapped to ───► OWASP AI Exchange (threat/control matrices)
     ├── Covers     ───► OWASP LLM Top 10 (all 10 risks)
     └── Covers     ───► OWASP ML Top 10 (all 10 vulnerabilities)
              │
              ▼
MLASTG                 ─── Test Cases (verification perspective)
              │
              ▼
MLASWE                 ─── Weaknesses (vulnerability classification)
```

---

## 6. Applying the MLASVS

### For Development Teams
1. Determine the target security level (L1 or L2) for your ML system
2. Review applicable controls from all 7 categories
3. Implement controls during model development and deployment
4. Use the [MLASTG Checklist](../checklist.md) to track compliance

### For Security Teams
1. Reference the MLASVS when defining security requirements for ML projects
2. Use the MLASTG test cases to verify each control
3. Classify findings using MLASWE identifiers
4. Report compliance status using the control framework

### For Auditors
1. Use MLASVS as the audit criteria for ML system reviews
2. Verify controls at the declared security level (L1 or L2)
3. Cross-reference findings to MLASWE weakness categories
4. Document residual risk for unaddressed controls

---

## 7. Control Inventory Summary

| Control ID | Title | Level | MITRE ATLAS Ref | Test Ref |
|-----------|-------|-------|-----------------|----------|
| **DATA-001** | Data provenance tracking | L1 | AML.TA0009 | TEST-DATA-001 |
| **DATA-002** | Cryptographic data integrity | L1 | AML.TA0010 | TEST-DATA-001 |
| **DATA-003** | Data access control enforcement | L1 | AML.TA0002 | TEST-DATA-004 |
| **DATA-004** | Input validation and sanitization | L1 | AML.TA0005 | TEST-DATA-002 |
| **DATA-005** | PII/PHI detection in training data | L1 | AML.TA0010 | TEST-DATA-002 |
| **DATA-006** | Data lineage documentation | L1 | AML.TA0009 | TEST-DATA-001 |
| ... | ... | ... | ... | ... |

*(Full control inventory in each category section)*

---

## 8. Versioning

| Version | Date | Notes |
|---------|------|-------|
| 0.1 (Draft) | 2025-Q2 | Initial framework structure and control definitions |
