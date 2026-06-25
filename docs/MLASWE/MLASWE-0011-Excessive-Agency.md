# MLASWE-0011: Excessive Agency

## Description
Excessive agency occurs when an LLM or AI agent is granted more autonomy than is necessary or safe. This can lead to unauthorized tool use, data access, financial transactions, or system modifications that should require human approval. Combined with prompt injection, excessive agency is one of the most dangerous LLM vulnerabilities (OWASP LLM08).

## Risk
- **Severity:** High (can lead to unauthorized actions, data breaches, financial loss)
- **Exploitability:** Medium (requires prompt injection + tool access)
- **Prevalence:** Common in LLM agentic architectures (AutoGPT, ChatGPT plugins, etc.)

## Affected Components
- LLM-based agents with plugin/tool access
- AutoGPT-style autonomous systems
- LLMs connected to databases, APIs, or execution environments
- RPA (Robotic Process Automation) with AI decision-making

## Detection Methods
- **Permission Boundary Testing:** Attempt actions beyond expected authorization
- **Tool Invocation Auditing:** Review logs for unauthorized tool/plugin usage
- **Authorization Chain Verification:** Trace decision chains to verify approvals

## Preventive Controls (MLASVS)
- **MLASVS-LLM-007:** Tool call authorization
- **MLASVS-LLM-010:** Human-in-the-loop for critical actions
- **MLASVS-LLM-020:** Agentic workflow authorization (L2)
- **MLASVS-LLM-021:** Tool/plugin isolation sandbox (L2)
- **MLASVS-LLM-023:** Human override mechanisms (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0053:** LLM Plugin Compromise (primary)

## Remediation
1. **Least Privilege:** Grant LLMs/agents minimum necessary permissions
2. **Tool Scoping:** Define precise capabilities for each tool/plugin
3. **Human Approval Gate:** Require explicit user approval for destructive/irreversible actions
4. **Isolation Sandbox:** Run agentic workflows in isolated environments
5. **Audit Logging:** Log all automated decisions and tool invocations
6. **Time-bound Sessions:** Limit agent autonomy to specific time windows

## References
- OWASP LLM Top 10: LLM08 (Excessive Agency), LLM07 (Insecure Plugin Design)
- MITRE ATLAS: AML.T0053
