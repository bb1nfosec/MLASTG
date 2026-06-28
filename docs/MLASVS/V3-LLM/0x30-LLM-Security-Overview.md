# V3: LLM Security — MLASVS-LLM

## Overview

Large Language Models (LLMs) present a unique security challenge. Unlike traditional ML models where the attack surface is primarily input → prediction, LLMs introduce prompt injection, insecure output handling, excessive agency, and complex multi-turn attack vectors. This category addresses the OWASP LLM Top 10 and MITRE ATLAS LLM-specific techniques.

## Key Threats

| Threat | MITRE ATLAS | OWASP LLM | MLASWE Reference |
|--------|-------------|-----------|------------------|
| Prompt injection | AML.T0051 | LLM01 | MLASWE-0006 |
| Insecure output handling | AML.T0057 | LLM02 | MLASWE-0010 |
| Training data poisoning | AML.T0020 | LLM03 | MLASWE-0002 |
| Model denial of service | AML.T0029 | LLM04 | MLASWE-0008 |
| Supply chain vulnerabilities | AML.TA0003 | LLM05 | MLASWE-0009 |
| Sensitive information disclosure | AML.T0057 | LLM06 | MLASWE-0012 |
| Insecure plugin design | AML.T0053 | LLM07 | MLASWE-0011 |
| Excessive agency | AML.T0053 | LLM08 | MLASWE-0011 |
| Overreliance | AML.T0056 | LLM09 | — |
| Model theft | AML.T0024.002 | LLM10 | MLASWE-0003 |

## Subcategories

### LLM-1: Prompt Injection Prevention (Controls LLM-001, LLM-002, LLM-004, LLM-006, LLM-007, LLM-015, LLM-016, LLM-018, LLM-019, LLM-021)
Protecting LLMs from prompt manipulation attacks including direct, indirect, and multi-turn injection.

### LLM-2: Output Handling (Controls LLM-003, LLM-008, LLM-009, LLM-014)
Ensuring LLM outputs are properly validated, filtered, and safely handled.

### LLM-3: Agency Control (Controls LLM-005, LLM-010, LLM-011, LLM-012, LLM-013, LLM-017, LLM-020, LLM-022, LLM-023, LLM-024)
Controlling LLM autonomy, resource usage, and decision-making authority.

### LLM-4: Context Isolation (Control LLM-004, LLM-018)
Maintaining separation between system instructions, user input, and retrieved context.

### LLM-5: System Prompt Hardening (Controlled via LLM-004, LLM-015, LLM-016)
Designing robust system prompts resistant to extraction and manipulation.

## Control Inventory

### L1 Controls (14)

| ID | Control | MITRE ATLAS | OWASP LLM | Test Ref |
|----|---------|-------------|-----------|----------|
| LLM-001 | Prompt injection prevention | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-002 | Input/output boundary enforcement | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-003 | Output validation and filtering | AML.T0057 | LLM02 | TEST-LLM-002 |
| LLM-004 | System prompt isolation | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-005 | Context window limits | AML.T0029 | LLM04 | TEST-LLM-003 |
| LLM-006 | Plugin permission scoping | AML.T0053 | LLM07 | TEST-LLM-001 |
| LLM-007 | Tool call authorization | AML.T0053 | LLM08 | TEST-LLM-001 |
| LLM-008 | Sensitive data exfiltration prevention | AML.T0057 | LLM06 | TEST-LLM-002 |
| LLM-009 | Content filtering pipeline | AML.T0057 | LLM02 | TEST-LLM-002 |
| LLM-010 | Human-in-the-loop for critical actions | AML.T0053 | LLM08 | TEST-LLM-003 |
| LLM-011 | Rate limiting on LLM endpoints | AML.T0029 | LLM04 | TEST-LLM-003 |
| LLM-012 | Token usage monitoring | AML.T0029 | LLM04 | TEST-LLM-003 |
| LLM-013 | Input token limits | AML.T0029 | LLM04 | TEST-LLM-003 |
| LLM-014 | Output length limits | AML.T0057 | LLM02 | TEST-LLM-002 |

### L2 Controls (10)

| ID | Control | MITRE ATLAS | OWASP LLM | Test Ref |
|----|---------|-------------|-----------|----------|
| LLM-015 | Prompt firewall deployment | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-016 | Semantic prompt filtering | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-017 | Jailbreak detection system | AML.T0051 | LLM01 | TEST-LLM-003 |
| LLM-018 | RAG security controls | AML.T0051 | LLM06 | TEST-LLM-001 |
| LLM-019 | Embedding-level anomaly detection | AML.T0051 | LLM01 | TEST-LLM-001 |
| LLM-020 | Agentic workflow authorization | AML.T0053 | LLM08 | TEST-LLM-003 |
| LLM-021 | Tool/plugin isolation sandbox | AML.T0053 | LLM07 | TEST-LLM-001 |
| LLM-022 | Continuous red teaming pipeline | AML.T0051 | LLM01 | TEST-LLM-003 |
| LLM-023 | Human override mechanisms | AML.T0053 | LLM08 | TEST-LLM-003 |
| LLM-024 | Multi-turn attack detection | AML.T0051 | LLM01 | TEST-LLM-003 |

## OWASP LLM Top 10 Coverage Map

| OWASP LLM Risk | MLASTG Controls |
|---------------|-----------------|
| LLM01: Prompt Injection | LLM-001, LLM-002, LLM-004, LLM-015, LLM-016, LLM-017, LLM-019, LLM-024 |
| LLM02: Insecure Output Handling | LLM-003, LLM-009, LLM-014 |
| LLM03: Training Data Poisoning | (Covered in MLASVS-DATA) |
| LLM04: Model Denial of Service | LLM-005, LLM-011, LLM-012, LLM-013 |
| LLM05: Supply Chain | (Covered in MLASVS-SUPPLY) |
| LLM06: Sensitive Information Disclosure | LLM-008, LLM-018 |
| LLM07: Insecure Plugin Design | LLM-006, LLM-021 |
| LLM08: Excessive Agency | LLM-007, LLM-010, LLM-020, LLM-023 |
| LLM09: Overreliance | (Covered in MLASVS-GOV) |
| LLM10: Model Theft | (Covered in MLASVS-MODEL) |

## Related Links

- [MLASTG Test Cases: LLM Security](../../MLASTG/LLM-Tests/0x00-LLM-Tests-Overview.md)
- [MLASWE-0006: Prompt Injection](../../MLASWE/MLASWE-0006-Prompt-Injection.md)
- [MLASWE-0010: Insecure Output Handling](../../MLASWE/MLASWE-0010-Insecure-Output-Handling.md)
- [MLASWE-0011: Excessive Agency](../../MLASWE/MLASWE-0011-Excessive-Agency.md)
