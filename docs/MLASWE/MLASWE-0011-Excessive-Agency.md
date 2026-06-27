# MLASWE-0011: Excessive Agency

## Description
Excessive Agency is a critical architectural vulnerability occurring when an AI agent or LLM is granted disproportionate autonomy, privileges, or tool access relative to its intended function. When an attacker successfully compromises the model (e.g., via prompt injection), they can leverage this excessive agency to force the system to perform unauthorized, destructive, or highly privileged actions across the enterprise environment.

## Risk
- **Severity:** Critical (leads directly to unauthorized data modification, financial loss, or lateral movement)
- **Exploitability:** Medium (requires successful model manipulation coupled with over-provisioned access)
- **Prevalence:** Rapidly growing as organizations deploy autonomous AI agents, LangChain tools, and Copilots.

## Affected Components
- LLM agents equipped with tools, plugins, or API integrations.
- Robotic Process Automation (RPA) systems utilizing ML for decision-making.
- AI-driven CI/CD deployment pipelines.
- Autonomous customer service bots with backend database write access.

## Detection Methods
- **Authorization Auditing:** Security teams MUST conduct regular audits of IAM roles and API scopes assigned to AI agents.
- **Execution Tracing:** Systems MUST implement comprehensive logging to trace the provenance of every tool invocation back to the originating prompt.
- **Anomaly Detection:** Operations SHOULD monitor agent behavioral patterns to detect deviations from expected, baseline tool utilization.

## Preventive Controls (MLASVS)
- **MLASVS-LLM-007:** Tool call authorization
- **MLASVS-LLM-010:** Human-in-the-loop for critical actions
- **MLASVS-LLM-020:** Agentic workflow authorization (L2)
- **MLASVS-LLM-021:** Tool/plugin isolation sandbox (L2)
- **MLASVS-LLM-023:** Human override mechanisms (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0053:** LLM Plugin Compromise (primary)

## Remediation
1. **Principle of Least Privilege:** AI agents MUST be provisioned with the absolute minimum permissions required to perform their specific tasks. Read-only access SHOULD be preferred.
2. **Human-in-the-Loop (HITL):** Systems MUST require explicit, out-of-band human authorization before an agent can execute any destructive, financial, or high-impact action.
3. **Granular Tool Scoping:** Developers MUST narrowly scope the functionality of plugins. For instance, an email plugin SHOULD only allow reading specific folders, rather than granting full mailbox delegation.
4. **Session and State Limits:** Agents MUST operate within strict time bounds and computational limits to prevent runaway autonomous execution loops.
5. **API Hardening:** Backend APIs consumed by the agent MUST enforce their own robust authentication and authorization checks, irrespective of the agent's internal logic.

## Real-World Examples
- **Unauthorized Email Exfiltration:** An autonomous email assistant, over-provisioned with full mailbox access, was manipulated via an incoming malicious email to forward sensitive corporate communications to an external attacker.
- **Rogue Trading Agents:** Algorithmic financial agents executing trades without human oversight resulted in catastrophic market anomalies and rapid financial loss.

## References
- OWASP LLM Top 10: LLM08 (Excessive Agency)
- MITRE ATLAS: AML.T0053
