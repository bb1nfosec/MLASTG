# MLSec Application Security Testing Guide

**Enterprise & Defense-Grade Security Testing for Machine Learning Systems**

Welcome to the **MLASTG** — the definitive open-source framework for security testing machine learning systems across traditional ML, deep learning, and large language models (LLMs).

## The Challenge

Machine learning systems introduce a fundamentally new attack surface that traditional application security testing cannot address:

| Attack Vector | Traditional Software | ML Systems |
|--------------|---------------------|------------|
| Input manipulation | SQL injection, XSS | Adversarial perturbations, prompt injection |
| Data corruption | Configuration tampering | Training data poisoning, backdoor injection |
| Intellectual property theft | Source code exfiltration | Model extraction, inversion attacks |
| Supply chain risk | Library vulnerabilities | Compromised base models, poisoned datasets |
| Logic exploitation | Business logic flaws | Model bias exploitation, adversarial triggers |

## The MLASTG Solution

The MLASTG provides a structured, three-layer approach to ML security testing:

### 🔷 MLASVS — The Verification Standard
What security controls must be verified, organized into 7 categories with two assurance levels.

### 🔶 MLASTG — The Testing Guide  
How to verify each control with detailed step-by-step test cases, techniques, and procedures.

### 🔷 MLASWE — The Weakness Enumeration
A common taxonomy of ML/LLM security weaknesses for consistent vulnerability classification.

## Who Is This For?

| Role | What MLASTG Provides |
|------|---------------------|
| **Security Engineers** | Testable controls, step-by-step test procedures, Python test harnesses |
| **ML Engineers** | Security requirements for model development and deployment |
| **Penetration Testers** | Complete testing methodology with tools and techniques |
| **CISO / Security Leaders** | Governance framework, compliance mapping, risk assessment criteria |
| **Auditors / Regulators** | Verifiable controls mapped to regulatory frameworks |
| **Red Teams** | Attack simulation procedures aligned with MITRE ATLAS |

## Quick Navigation

| Section | Description |
|---------|-------------|
| [Testing Methodology](MLASTG/0x00-Testing-Methodology.md) | How to conduct a structured ML security assessment |
| [Testing Tools](MLASTG/0x01-Testing-Tools.md) | Tooling reference (ART, Giskard, Guardrails AI, etc.) |
| [Assessment Checklist](../checklist.md) | Track assessment progress against all 168 controls |

> **Version 0.1 (Draft):** The MLASVS Standard, MLASWE Weakness Enumeration, and executable test scripts are in active development. See the [GitHub repository](https://github.com/bb1nfosec/MLASTG) for the latest status.

## Framework Alignment

The MLASTG is cross-referenced with:

- **[MITRE ATLAS](https://atlas.mitre.org/)** — Adversarial tactics and techniques
- **[NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework)** — Risk management framework
- **[OWASP AI Exchange](https://owaspai.org/)** — AI security best practices
- **[OWASP LLM Top 10](https://genai.owasp.org/llm-top-10/)** — LLM vulnerability catalog
- **[OWASP ML Top 10](https://owasp.org/www-project-machine-learning-security-top-10/)** — ML vulnerability catalog
- **[NSA/CISA AI Security](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3741371/nsa-publishes-guidance-for-strengthening-ai-system-security/)** — Defense-grade guidance

## License

This work is licensed under **CC BY-SA 4.0**.
