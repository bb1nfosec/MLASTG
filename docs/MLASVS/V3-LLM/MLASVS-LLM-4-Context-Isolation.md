# MLASVS-LLM-4: Context Isolation Controls

> **Subcategory:** V3: LLM Security
> **Controls:** LLM-004, LLM-018

## Overview

Context isolation maintains strict separation between system instructions, user input, and retrieved context (RAG). Without isolation, adversaries can manipulate the LLM's behavior through indirect injection via retrieved documents or context window manipulation.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| LLM-004 | System prompt isolation | L1 | AML.T0051 | TEST-LLM-001 | Protect system prompts from extraction or manipulation via user input |
| LLM-018 | RAG security controls | L2 | AML.T0051 | TEST-LLM-001 | Secure Retrieval-Augmented Generation pipelines against indirect injection |

## Implementation Guidance

### System Prompt Isolation
- Use structured prompt templates with clear delimiter boundaries
- Separate system instructions from user-accessible memory
- Implement prompt-level access controls (system prompts invisible to user queries)

### RAG Security
- Sanitize all retrieved documents before inclusion in context
- Detect injection patterns in document chunks
- Use content source attribution and trust scoring
- Implement chunk-level integrity verification

## Related

- [MLASTG-TEST-LLM-001: Prompt Injection Testing](../../MLASTG/LLM-Tests/MLASTG-TEST-LLM-001.md)
- [MLASWE-0006: Prompt Injection](../../MLASWE/MLASWE-0006-Prompt-Injection.md)
- **OWASP LLM Top 10:** LLM01 (Prompt Injection)
- **MITRE ATLAS:** AML.T0051 (LLM Prompt Injection)
