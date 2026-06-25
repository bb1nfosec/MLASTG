# MLASTG Testing Methodology

## 1. Overview

This document defines the methodology for conducting a structured security assessment of machine learning systems using the MLASVS (standard) and MLASWE (weakness taxonomy).

The methodology follows a phased approach adapted from standard penetration testing methodologies (PTES, OWASP) and extended for the unique characteristics of ML systems.

## 2. The ML Security Assessment Lifecycle

```
Phase 1: Planning & Scoping
    │
    ▼
Phase 2: Intelligence Gathering & Threat Modeling
    │
    ▼
Phase 3: Control Verification (MLASTG Test Cases)
    ├── Data Security Tests
    ├── Model Security Tests
    ├── LLM Security Tests
    ├── Supply Chain Tests
    ├── Pipeline Tests
    ├── Infrastructure Tests
    └── Governance Tests
    │
    ▼
Phase 4: Exploitation & Validation
    │
    ▼
Phase 5: Reporting & Remediation
```

## 3. Phase 1: Planning & Scoping

### 3.1 Define Scope

- **Identify ML components:** Models, training pipelines, inference endpoints, feature stores, model registries
- **Determine ML system type:** Classification, regression, NLP, computer vision, LLM/GenAI, recommendation
- **Map data flows:** Training data sources → preprocessing → training → evaluation → deployment → inference
- **Identify dependencies:** Pre-trained models, third-party APIs, external datasets, ML libraries

### 3.2 Select Security Level

| Level | Criteria |
|-------|----------|
| **L1 (Standard)** | Internal ML systems, non-critical customer-facing applications |
| **L2 (Defense-in-Depth)** | Regulated industries, defense, healthcare, financial, critical infrastructure |

### 3.3 Establish Rules of Engagement

- Define testing window and notification requirements
- Determine if adversarial testing (evasion, extraction) is in scope
- Establish model availability requirements (avoid DoS to production models)
- Define data handling for any training data or model artifacts accessed during testing

## 4. Phase 2: Intelligence Gathering & Threat Modeling

### 4.1 Architecture Discovery

- Document ML system architecture (diagrams, data flows, component interactions)
- Identify all ML artifacts (datasets, models, pipelines, serving infrastructure)
- Map trust boundaries between components

### 4.2 Threat Modeling Using MITRE ATLAS

Map the system architecture to MITRE ATLAS tactics:

| ATLAS Tactic | ML System Focus |
|-------------|-----------------|
| Reconnaissance | ML-SBOM, public model info, API documentation |
| Initial Access | Inference endpoint exposure, pipeline credentials |
| Execution | Training code execution, model loading |
| Persistence | Backdoor models, compromised feature stores |
| Privilege Escalation | ML platform admin access |
| Defense Evasion | Adversarial perturbations, model obfuscation |
| Credential Access | API keys, training data access tokens |
| Discovery | Model architecture fingerprinting, dataset enumeration |
| Collection | Inference data harvesting, training data exfiltration |
| Exfiltration | Model extraction, training data leakage |
| Impact | Model poisoning, denial of service, misclassification |

### 4.3 Tool Setup

| Tool | Purpose | Installation |
|------|---------|-------------|
| IBM ART | Adversarial robustness testing | `pip install adversarial-robustness-toolbox` |
| SecML | ML security evaluation | `pip install secml` |
| Giskard | LLM security testing | `pip install giskard` |
| Counterfit | AI security automation | `pip install counterfit` |
| PromptInject | Prompt injection testing | `pip install promptinject` |
| TextAttack | NLP adversarial testing | `pip install textattack` |

## 5. Phase 3: Control Verification

### 5.1 Test Execution Flow

For each applicable MLASVS control:

1. **Identify** the control from the applicable category
2. **Reference** the corresponding MLASTG-TEST-XXXX test case
3. **Execute** the test procedure
4. **Document** results with evidence
5. **Classify** any findings using MLASWE identifiers

### 5.2 Test Categories

| Category | Test Cases | Focus |
|----------|-----------|-------|
| **DATA** | MLASTG-TEST-DATA-001 to 004 | Data provenance, sanitization, differential privacy, access controls |
| **MODEL** | MLASTG-TEST-MODEL-001 to 005 | Adversarial robustness, extraction, inversion, backdoors, integrity |
| **LLM** | MLASTG-TEST-LLM-001 to 003 | Prompt injection, output handling, jailbreak testing |
| **SUPPLY** | MLASTG-TEST-SUPPLY-001 to 002 | ML-SBOM audit, model provenance |
| **PIPELINE** | MLASTG-TEST-PIPELINE-001 | CI/CD security audit |
| **INFRA** | MLASTG-TEST-INFRA-001 to 002 | Model serving, API security |
| **GOV** | MLASTG-TEST-GOV-001 | Governance assessment |

### 5.3 Test Procedure Template

Each test case follows this structure:

```
## MLASTG-TEST-XXXX: [Test Title]

### Control Reference
MLASVS-{CATEGORY}-{NUMBER}: {Control Description}

### Severity
Critical / High / Medium / Low / Informational

### Prerequisites
- Access requirements
- Tools required
- Model/data access needed

### Step-by-Step Procedure
1. [Step 1]
2. [Step 2]
3. [Step 3]
   ...

### Expected Result
[What should happen if the control is properly implemented]

### Evidence Requirements
- [What to capture as proof of testing]

### Remediation Guidance
[How to fix if the test fails]

### References
- MITRE ATLAS: AML.TXXXX
- MLASWE: MLASWE-XXXX
```

## 6. Phase 4: Exploitation & Validation

### 6.1 Adversarial Testing

For L2 assessments, adversarial exploitation is in scope:

| Attack Type | Tool | Technique |
|------------|------|-----------|
| Evasion (white-box) | ART, CleverHans | FGSM, PGD, DeepFool |
| Evasion (black-box) | ART | HopSkipJump, Boundary Attack |
| Data poisoning | ART, SecML | Gradient matching, backdoor injection |
| Model extraction | ART | KnockoffNets, CopycatCNN |
| Membership inference | ART | Shadow model, confident-based |
| Prompt injection | Giskard, PromptInject | Direct, indirect, multi-turn |
| Jailbreak | Custom frameworks | DAN, role-playing, encoding bypass |

### 6.2 Validation Criteria

| Attack Success Rate | Risk Level |
|--------------------|------------|
| < 5% success | Low risk |
| 5-15% success | Medium risk |
| 15-30% success | High risk |
| > 30% success | Critical risk |

## 7. Phase 5: Reporting

### 7.1 Report Structure

```
Executive Summary
├── Assessment scope and methodology
├── Risk overview by category
├── Key findings and critical risks
└── Overall security posture

Technical Findings
├── By MLASVS Category
│   ├── Control Reference
│   ├── MLASWE Reference
│   ├── Test Procedure Executed
│   ├── Evidence
│   ├── Risk Rating
│   └── Remediation Recommendation
└── Adversarial Testing Results
    ├── Attack type
    ├── Success rate
    ├── Affected controls
    └── Mitigation effectiveness

Compliance Mapping
├── MLASVS Coverage (%)
├── Controls by level (L1/L2)
├── Industry framework alignment
└── Gap analysis

Appendices
├── Test execution logs
├── Tool outputs and screenshots
├── Model architecture diagrams
└── ML-SBOM analysis
```

### 7.2 Risk Ratings

| Rating | Definition | ML Impact |
|--------|------------|-----------|
| **Critical** | Immediate exploitation with severe impact | Model can be reliably poisoned, extracted with >50% fidelity, or made unavailable |
| **High** | Exploitation possible with moderate effort | Model evasion >30% success rate, training data leakage confirmed |
| **Medium** | Exploitation requires significant resources | Model injection requires >100K queries, membership inference marginally above baseline |
| **Low** | Limited exploitation potential | Control deficiency with compensating controls in place |

### 7.3 Remediation Timing

| Risk Level | Remediation Timeline |
|------------|---------------------|
| Critical | 24-48 hours |
| High | 1-2 weeks |
| Medium | 1-3 months |
| Low | 3-6 months |
