# MLASVS-LLM-3: Agency Control Controls

> **Subcategory:** V3: LLM Security
> **Controls:** LLM-005, LLM-010, LLM-011, LLM-012, LLM-013, LLM-017, LLM-020, LLM-022, LLM-023, LLM-024

## Overview

Agency control limits the autonomy and resource consumption of LLM-based systems. Excessive agency allows unauthorized actions; insufficient resource controls enable denial-of-service. This subcategory covers context limits, human-in-the-loop, rate limiting, token monitoring, jailbreak detection, agentic authorization, and multi-turn attack detection.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| LLM-005 | Context window limits | L1 | AML.T0029 | TEST-LLM-003 | Enforce maximum context window size |
| LLM-010 | Human-in-the-loop for critical actions | L1 | AML.T0053 | TEST-LLM-003 | Require human approval for destructive or irreversible LLM actions |
| LLM-011 | Rate limiting on LLM endpoints | L1 | AML.T0029 | TEST-LLM-003 | Enforce per-user request rate limits on LLM APIs |
| LLM-012 | Token usage monitoring | L1 | AML.T0029 | TEST-LLM-003 | Monitor and alert on abnormal token consumption patterns |
| LLM-013 | Input token limits | L1 | AML.T0029 | TEST-LLM-003 | Enforce maximum input token count per request |
| LLM-017 | Jailbreak detection system | L2 | AML.T0051 | TEST-LLM-003 | Deploy automated detection of jailbreak attempts |
| LLM-020 | Agentic workflow authorization | L2 | AML.T0053 | TEST-LLM-003 | Gate all tool/API invocations behind explicit authorization checks |
| LLM-022 | Continuous red teaming pipeline | L2 | AML.T0051 | TEST-LLM-003 | Maintain automated red team testing for LLM vulnerabilities |
| LLM-023 | Human override mechanisms | L2 | AML.T0053 | TEST-LLM-003 | Enable human operators to override or halt LLM actions at any time |
| LLM-024 | Multi-turn attack detection | L2 | AML.T0051 | TEST-LLM-003 | Detect gradual instruction drift across multi-turn conversations |

## Implementation Guidance

### Resource Limits
- Set per-user, per-minute, and per-day token quotas
- Implement exponential backoff for repeat offenders
- Alert on consumption exceeding 2x baseline per user

### Human-in-the-Loop
- Classify actions by risk level (read-only, reversible, destructive)
- Require explicit approval for all destructive/irreversible actions
- Log all human approvals with timestamps and operator identity

### Jailbreak Detection
- Deploy classifier-based detection as a pre-processing layer
- Maintain a database of known jailbreak patterns
- Use semantic similarity to detect novel variants

## Related

- [MLASTG-TEST-LLM-003: Jailbreak & Denial-of-Service Testing](../../MLASTG/LLM-Tests/MLASTG-TEST-LLM-003.md)
- [MLASWE-0011: Excessive Agency](../../MLASWE/MLASWE-0011-Excessive-Agency.md)
- [MLASWE-0008: Model DoS](../../MLASWE/MLASWE-0008-Model-DoS.md)
- **OWASP LLM Top 10:** LLM04 (Model DoS), LLM08 (Excessive Agency)
- **MITRE ATLAS:** AML.T0029 (Denial of AI Service), AML.T0053 (LLM Plugin Compromise)
