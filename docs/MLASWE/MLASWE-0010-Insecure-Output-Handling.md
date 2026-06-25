# MLASWE-0010: Insecure Output Handling

## Description
Insecure output handling occurs when LLM-generated content is accepted without validation and processed in a way that can cause harm — rendered as HTML (leading to XSS), executed as code (leading to RCE), used in SQL queries (leading to injection), or trusted for critical decisions without verification. This is the second most critical LLM risk (OWASP LLM02).

## Risk
- **Severity:** High (can enable XSS, RCE, SQL injection, or data corruption)
- **Exploitability:** Medium (depends on downstream processing context)
- **Prevalence:** Common (many LLM applications pass output directly to browsers/executors)

## Affected Components
- LLM-generated content rendered as HTML or markdown in browsers
- LLM code generation output executed without sandboxing
- LLM output used in SQL queries, shell commands, or API calls
- RAG systems that inject retrieved content into executing environments

## Sub-types
| Type | Description | Downstream Risk |
|------|-------------|-----------------|
| **XSS via LLM output** | LLM generates JavaScript that renders unsanitized in browser | XSS, session theft |
| **RCE via code generation** | LLM-generated code executed without sandbox | Full system compromise |
| **SQL injection via LLM** | LLM output incorporated directly into SQL queries | Database compromise |
| **Decision automation** | LLM output trusted for critical decisions without human review | Operational failure |

## Detection Methods
- **Output Injection Testing:** Craft inputs that cause harmful outputs and verify handling
- **Context-Aware Output Scanning:** Validate output against downstream processing context
- **Fuzzing:** Send adversarial prompts and analyze response safety

## Preventive Controls (MLASVS)
- **MLASVS-LLM-003:** Output validation and filtering
- **MLASVS-LLM-009:** Content filtering pipeline
- **MLASVS-LLM-014:** Output length limits

## Attack Techniques (MITRE ATLAS)
- **AML.T0052:** LLM Data Leakage (related to output handling failures)

## Remediation
1. **Output Encoding:** Apply context-appropriate encoding (HTML entity, URL, SQL escaping)
2. **Content Security Policy:** Implement CSP headers to prevent XSS from rendered output
3. **Sandboxed Execution:** Execute generated code in isolated environments (containers, VMs)
4. **Parameterized Queries:** Never use LLM output directly in SQL — use parameterized statements
5. **Human-in-the-Loop:** Require review before executing critical LLM-generated commands
6. **Output Schema Validation:** Validate structured LLM output against expected schema

## Real-World Examples
- **ChatGPT plugin XSS:** LLM-generated markdown rendered as HTML in a browser, enabling cross-site scripting via malicious outputs
- **AutoGPT file deletion:** Autonomous agent deleted system files based on LLM-generated shell commands
- **GitHub Copilot code injection:** Generated code containing vulnerable patterns that were deployed without review

## References
- OWASP LLM Top 10: LLM02 (Insecure Output Handling)
- MITRE ATLAS: AML.T0052, AML.T0051
