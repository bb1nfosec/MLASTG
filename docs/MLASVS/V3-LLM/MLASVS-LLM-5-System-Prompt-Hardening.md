# MLASVS-LLM-5: System Prompt Hardening Controls

> **Subcategory:** V3: LLM Security
> **Controls:** LLM-004, LLM-015, LLM-016

## Overview

System prompt hardening designs robust system prompts that resist extraction, manipulation, and bypass attempts. This subcategory covers prompt isolation, firewall deployment, and semantic filtering — all designed to make the LLM's instructions resistant to adversarial input.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| LLM-004 | System prompt isolation | L1 | AML.T0051 | TEST-LLM-001 | Protect system prompts from extraction or manipulation via user input |
| LLM-015 | Prompt firewall deployment | L2 | AML.T0051 | TEST-LLM-001 | Deploy dedicated middleware to detect and block prompt injection |
| LLM-016 | Semantic prompt filtering | L2 | AML.T0051 | TEST-LLM-001 | Use NLP classifiers to detect injection intent beyond keyword matching |

## Implementation Guidance

### Prompt Design
- Include explicit refusal instructions for known attack categories
- Use structured delimiters (XML tags, special tokens) to separate instruction zones
- Avoid embedding sensitive information in system prompts

### Prompt Firewall
- Deploy Rebuff, Guardrails AI, or similar as a pre-processing layer
- Test against known injection pattern databases
- Target < 1% false positive rate on legitimate user queries

### Semantic Filtering
- Train or fine-tune a classifier to detect injection intent
- Test against paraphrased and obfuscated injection variants
- Maintain a feedback loop to improve detection over time

## Related

- [MLASTG-TEST-LLM-001: Prompt Injection Testing](../../MLASTG/LLM-Tests/MLASTG-TEST-LLM-001.md)
- [MLASWE-0006: Prompt Injection](../../MLASWE/MLASWE-0006-Prompt-Injection.md)
- **OWASP LLM Top 10:** LLM01 (Prompt Injection)
- **MITRE ATLAS:** AML.T0051 (LLM Prompt Injection)
