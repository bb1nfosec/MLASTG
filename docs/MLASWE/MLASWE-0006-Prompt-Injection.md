# MLASWE-0006: Prompt Injection

## Description
Prompt injection is the exploitation of LLM applications through crafted inputs that override or manipulate the model's system instructions. Attackers can force the model to perform unauthorized actions, reveal sensitive information, bypass content restrictions, or execute harmful tool calls.

## Risk
- **Severity:** Critical
- **Exploitability:** Easy (requires only text input)
- **Prevalence:** Common (affects all LLM applications to varying degrees)

## Affected Components
- LLM chat/completion endpoints
- RAG applications (indirect injection through retrieved documents)
- LLM-powered agents with tool/plugin access
- Multi-turn conversational systems
- Systems with function calling capabilities

## Sub-types
| Type | Description | Difficulty |
|------|-------------|------------|
| **Direct injection** | User input directly overrides system prompt | Easy |
| **Indirect injection** | Malicious content in retrieved documents/context | Medium |
| **Multi-turn injection** | Gradual instruction bending across conversation turns | Medium |
| **Latent injection** | Injection hidden in embeddings or encoded form | Hard |

## Detection Methods
- **Input Pattern Analysis:** Detect known injection patterns and delimiters
- **LLM-based Detection:** Use a secondary LLM to classify prompt intent
- **Embedding Analysis:** Detect anomalous embedding patterns
- **Output Monitoring:** Flag responses that deviate from expected behavior
- **Canary Tokens:** Insert trap tokens that should never appear in output

## Preventive Controls (MLASVS)
- **MLASVS-LLM-001:** Prompt injection prevention
- **MLASVS-LLM-002:** Input/output boundary enforcement
- **MLASVS-LLM-004:** System prompt isolation
- **MLASVS-LLM-015:** Prompt firewall deployment (L2)
- **MLASVS-LLM-016:** Semantic prompt filtering (L2)
- **MLASVS-LLM-018:** RAG security controls (L2)
- **MLASVS-LLM-019:** Embedding-level anomaly detection (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0051:** LLM Prompt Injection (primary)
- **AML.T0052:** LLM Data Leakage
- **AML.T0053:** LLM Plugin Compromise

## Remediation
1. **Input Sanitization:** Filter known injection patterns
2. **Prompt Engineering:** Use robust system prompts with clear boundaries
3. **Prompt Firewall:** Deploy dedicated injection detection middleware
4. **Output Validation:** Filter responses for policy violations
5. **Least Privilege:** Grant LLMs minimal necessary permissions
6. **Human-in-the-Loop:** Require human approval for sensitive operations

## Real-World Examples
- **Samsung ChatGPT leak (2023):** Engineer pasted proprietary code into ChatGPT
- **Remote code execution via plugin:** Injection that exploited browser automation plugins
- **Indirect injection via web scraping:** RAG system compromised by malicious web content
- **Jailbreak prompt marketplaces:** Publicly traded jailbreak templates (DAN, etc.)

## References
- OWASP LLM Top 10: LLM01
- MITRE ATLAS: AML.T0051
- Greshake et al., "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (2023)
- Kang et al., "Exploiting Programmatic Behavior of LLMs: Dual-Use Through Prompt Injection" (2023)
