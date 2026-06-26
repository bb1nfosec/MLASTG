# MLASVS-LLM-2: Output Handling Controls

> **Subcategory:** V3: LLM Security
> **Controls:** LLM-003, LLM-008, LLM-009, LLM-014

## Overview

LLM output handling ensures that model outputs are properly validated, filtered, and safely processed by downstream systems. Insecure output handling can lead to XSS, code injection, sensitive data leakage, and system compromise.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| LLM-003 | Output validation and filtering | L1 | AML.T0052 | TEST-LLM-002 | Validate and filter LLM outputs before rendering or execution |
| LLM-008 | Sensitive data exfiltration prevention | L1 | AML.T0052 | TEST-LLM-002 | Prevent LLM from outputting API keys, credentials, or PII |
| LLM-009 | Content filtering pipeline | L1 | AML.T0052 | TEST-LLM-002 | Deploy content moderation to block policy-violating outputs |
| LLM-014 | Output length limits | L1 | AML.T0052 | TEST-LLM-002 | Enforce maximum output length to prevent resource exhaustion |

## Implementation Guidance

### Output Encoding
- Never render raw LLM output as HTML without sanitization
- Use DOMPurify or equivalent for HTML contexts
- Implement Content Security Policy (CSP) headers

### Sensitive Data Filtering
- Deploy regex-based post-processing for API keys, credentials, SSNs, emails
- Implement context isolation — LLM context should not contain production credentials
- Use PII detection tools (AWS Macie, Azure Purview) for output scanning

### Content Filtering
- Enable content moderation APIs (Azure Content Safety, AWS Comprehend Moderator)
- Implement multi-layer filtering with configurable thresholds
- Log all filtered content for review and tuning

## Related

- [MLASTG-TEST-LLM-002: Output Validation & Data Exfiltration Testing](../../MLASTG/LLM-Tests/MLASTG-TEST-LLM-002.md)
- [MLASWE-0010: Insecure Output Handling](../../MLASWE/MLASWE-0010-Insecure-Output-Handling.md)
- **OWASP LLM Top 10:** LLM02 (Insecure Output Handling), LLM06 (Sensitive Information Disclosure)
- **MITRE ATLAS:** AML.T0052 (LLM Data Leakage)
