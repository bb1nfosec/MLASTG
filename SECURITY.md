# Security Policy

## Reporting a Vulnerability

The MLASTG project takes security seriously. We appreciate your efforts to responsibly disclose security issues and vulnerabilities in this framework.

### What to Report

This is a documentation/framework project. Reportable security issues include:

- **Incorrect security guidance** — Test procedures or controls that would lead security professionals to miss real vulnerabilities
- **Dangerous code samples** — Python test scripts that contain unsafe or exploitable code if run in production contexts
- **Supply chain issues** — Compromised dependencies in `requirements.txt` or CI/CD workflow files
- **Misinformation** — Incorrect MITRE ATLAS technique IDs, CVSS scores, or framework references that could mislead practitioners

### How to Report

**Do not open a public GitHub issue for security vulnerabilities.**

Please report security issues using one of these methods:

1. **GitHub Private Vulnerability Reporting** (preferred): Use the [Security tab](../../security/advisories/new) to submit a private advisory
2. **Email**: Send details to **vignesh4303@gmail.com**

### What to Include

When reporting, please provide:
- A description of the issue and its potential impact
- The specific file(s) and line number(s) affected
- A recommendation for the correct information or fix
- Your GitHub handle (for attribution in the fix, if desired)

### Response Timeline

| Severity | Response | Fix Target |
|----------|----------|------------|
| Critical (dangerous code/guidance) | 24 hours | 48 hours |
| High (significant misinformation) | 72 hours | 1 week |
| Medium (minor inaccuracies) | 1 week | Next release |

### Supported Versions

| Version | Status |
|---------|--------|
| 0.1 (Draft) | ✅ Actively maintained |

### Acknowledgements

We thank all security researchers who responsibly disclose issues. Contributors who report valid security issues will be acknowledged in the project's release notes (unless anonymity is requested).

### Out of Scope

- Issues in third-party tools referenced by MLASTG (report to respective projects)
- General requests for new test cases or controls (open a regular issue)
- Disagreements with security opinions or methodology choices (open a discussion)
