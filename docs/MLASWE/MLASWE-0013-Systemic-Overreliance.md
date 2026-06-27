# MLASWE-0013: Systemic Overreliance

## Description
Systemic Overreliance (or Automation Bias) occurs when an organization, system, or user implicitly trusts the outputs of an AI model without adequate verification, oversight, or fallback mechanisms. Models are prone to "hallucinations," factual inaccuracies, and logic errors. When these outputs are accepted as absolute truth and utilized in critical decision-making processes—such as medical diagnosis, legal analysis, or code deployment—the consequences can be catastrophic.

## Risk
- **Severity:** High (can lead to critical operational failures, legal liability, and safety risks)
- **Exploitability:** N/A (this is a systemic architectural and human-factors vulnerability)
- **Prevalence:** Ubiquitous across enterprises rapidly adopting generative AI solutions.

## Affected Components
- AI-assisted software development and code generation pipelines.
- Legal, financial, or medical document summarization systems.
- Automated security analysis and threat intelligence triage.
- Any workflow where AI output bypasses human verification.

## Detection Methods
- **A/B Testing with Baselines:** Organizations SHOULD periodically benchmark human performance against AI-assisted performance to identify degradation due to automation bias.
- **Audit Trails:** Systems MUST maintain immutable logs detailing which decisions were AI-generated versus human-verified.
- **User Behavior Monitoring:** Security teams SHOULD monitor systems for users instantly approving AI suggestions without review time (e.g., sub-second code PR approvals).

## Preventive Controls (MLASVS)
- **MLASVS-LLM-010:** Human-in-the-loop for critical actions
- **MLASVS-APP-008:** AI output confidence signaling
- **MLASVS-APP-009:** Fail-safe defaults and fallback mechanisms

## Attack Techniques (MITRE ATLAS)
- N/A (Primarily an operational and architectural vulnerability)

## Remediation
1. **Mandatory Human-in-the-Loop (HITL):** Enterprise architectures MUST mandate explicit human review and authorization for all AI-generated outputs that influence critical infrastructure, legal standing, or safety.
2. **Confidence Signalling:** AI interfaces SHOULD clearly articulate uncertainty, explicitly displaying confidence scores, citations, or data lineage to end users.
3. **UX Friction:** User interfaces MUST intentionally introduce "constructive friction" (e.g., mandatory review checklists) to prevent blind acceptance of AI recommendations.
4. **Cross-Validation Architectures:** Critical systems SHOULD employ multi-model consensus or deterministic heuristic checks to validate the plausibility of an primary AI's output.
5. **Fallback Mechanisms:** All AI-dependent systems MUST possess robust, deterministic fallback procedures to maintain operations during model degradation or failure.

## Real-World Examples
- **Legal Hallucinations:** Attorneys submitted AI-generated legal briefs containing entirely fictitious case citations, resulting in severe judicial sanctions, because they failed to verify the AI's output.
- **Vulnerable Code Deployment:** Software engineers blindly accepted AI-generated code snippets containing fundamental security flaws (e.g., SQL injection vulnerabilities), directly pushing them to production.

## References
- OWASP LLM Top 10: LLM09 (Overreliance)
- NIST AI Risk Management Framework (AI RMF)
