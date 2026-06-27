# MLASWE-0006: Prompt Injection

## Description
Prompt injection is a critical vulnerability wherein an adversary exploits Large Language Model (LLM) interfaces by supplying crafted inputs that override, subvert, or manipulate the model's foundational system instructions. This weakness allows attackers to hijack the LLM's execution flow, potentially forcing the system to exfiltrate sensitive data, execute unauthorized tool calls, bypass content filters, or generate malicious payloads. 

## Risk
- **Severity:** Critical (can lead to full system compromise depending on agentic capabilities)
- **Exploitability:** High (requires only text-based interaction; low barrier to entry)
- **Prevalence:** Widespread (systemically affects all foundational LLMs to varying degrees)

## Affected Components
- LLM-driven chat and completion API endpoints.
- Retrieval-Augmented Generation (RAG) pipelines processing untrusted external data.
- Autonomous LLM agents possessing tool, API, or execution environment access.
- Multi-turn conversational interfaces maintaining persistent context.

## Sub-types
| Type | Description | Difficulty |
|------|-------------|------------|
| **Direct Injection (Jailbreaking)** | User input directly contradicts or overrides system instructions. | Low |
| **Indirect Injection** | Malicious payloads are embedded in third-party data retrieved by RAG systems. | Medium |
| **Multi-turn Injection** | The attacker progressively manipulates model state across a prolonged session. | Medium |
| **Latent/Encoded Injection** | Payloads are obfuscated (e.g., Base64, token-smuggling) to evade basic filters. | High |

## Detection Methods
- **Input Pattern Analysis:** Security gateways MUST employ pattern matching to detect known injection signatures, control characters, and bypass techniques.
- **Semantic Intent Monitoring:** Organizations SHOULD deploy secondary LLM-based classifiers to evaluate the malicious intent of incoming prompts.
- **Embedding Anomaly Detection:** Systems SHOULD analyze input embeddings to detect adversarial or out-of-distribution structures.
- **Canary Tokens:** Developers MAY insert hidden tokens in the system prompt; if the LLM outputs the token, a prompt injection attack is highly probable.

## Preventive Controls (MLASVS)
- **MLASVS-LLM-001:** Prompt injection prevention
- **MLASVS-LLM-002:** Input/output boundary enforcement
- **MLASVS-LLM-004:** System prompt isolation
- **MLASVS-LLM-015:** Prompt firewall deployment (L2)
- **MLASVS-LLM-016:** Semantic prompt filtering (L2)
- **MLASVS-LLM-018:** RAG security controls (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0051:** LLM Prompt Injection (primary)
- **AML.T0052:** LLM Data Leakage
- **AML.T0053:** LLM Plugin Compromise

## Remediation
1. **Prompt Isolation:** Developers MUST logically separate system instructions from user inputs using robust delimiters (e.g., ChatML formats).
2. **AI Firewalls:** Organizations MUST deploy dedicated LLM firewalls (e.g., NeMo Guardrails) to perform semantic inspection of all inputs and outputs.
3. **Privilege Separation:** LLM agents MUST operate under the Principle of Least Privilege, explicitly lacking the authority to perform high-impact actions without human authorization.
4. **Data Sanitization:** All data retrieved by RAG pipelines MUST be sanitized and explicitly marked as untrusted prior to model ingestion.
5. **Instruction Defense:** System prompts SHOULD incorporate state-of-the-art defensive framing, explicitly instructing the model to disregard conflicting user directives.

## Real-World Examples
- **Corporate Data Exfiltration:** Employees inadvertently leaked proprietary source code and PII by bypassing ChatGPT's corporate data guardrails.
- **RAG Poisoning:** Attackers embedded invisible text in websites, hijacking web-crawling LLMs to return attacker-controlled summaries.
- **Plugin Exploitation:** Attackers utilized prompt injection to force LLM agents into executing unauthorized HTTP requests via connected plugins.

## References
- OWASP LLM Top 10: LLM01
- MITRE ATLAS: AML.T0051
- Greshake et al., "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection" (2023)
