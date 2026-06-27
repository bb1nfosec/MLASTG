# MLASWE-0012: Training Data Leakage

## Description
Training Data Leakage (or Model Memorization) occurs when a machine learning model inadvertently embeds and subsequently exposes the exact data upon which it was trained. For Large Language Models, this vulnerability is acute, as they can perfectly regurgitate proprietary source code, Personally Identifiable Information (PII), or confidential corporate documents. This constitutes a severe violation of data privacy regulations (e.g., GDPR, CCPA) and intellectual property rights.

## Risk
- **Severity:** High to Critical (results in direct exposure of PII, PHI, or enterprise intellectual property)
- **Exploitability:** Medium (often requires sophisticated prompt engineering or extraction attacks)
- **Prevalence:** Highly common in models trained on vast, uncurated corpuses (e.g., standard LLMs).

## Affected Components
- Foundational and fine-tuned Large Language Models.
- Code generation assistants (e.g., Copilot equivalents) trained on private repositories.
- Image generation models prone to replicating copyrighted or private imagery.
- Any model trained on unredacted, sensitive corporate data lakes.

## Detection Methods
- **Extraction Simulation:** Red teams MUST perform active extraction attacks utilizing prefix-matching and prompt-looping techniques to force data regurgitation.
- **Deduplication Analysis:** Data pipelines MUST analyze the training corpus for highly duplicated strings, which exponentially increases the likelihood of memorization.
- **Output Content Filtering:** Security monitoring SHOULD employ Data Loss Prevention (DLP) scanners on model outputs to detect and block PII or proprietary markers.

## Preventive Controls (MLASVS)
- **MLASVS-DATA-005:** PII/PHI detection in training data
- **MLASVS-DATA-010:** Data minimization
- **MLASVS-DATA-015:** Data de-identification
- **MLASVS-LLM-008:** Sensitive data exfiltration prevention
- **MLASVS-MODEL-019:** Differential privacy in model (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.TA0010:** Collection (training data exfiltration)
- **AML.T0024:** Exfiltration via ML Inference

## Remediation
1. **Aggressive Data Sanitization:** Organizations MUST implement robust data scrubbing pipelines to rigorously identify and remove PII, credentials, and sensitive IP prior to model training.
2. **Data Deduplication:** Data engineering teams SHOULD enforce aggressive exact and near-exact deduplication on training corpuses to minimize model memorization capacity.
3. **Differential Privacy:** Where feasible, training processes SHOULD utilize Differential Privacy (DP-SGD) to mathematically bound the risk of memorizing any single training record.
4. **Data Minimization:** Teams MUST adhere strictly to data minimization principles, ensuring models are not unnecessarily exposed to sensitive fields.
5. **Egress DLP Scanning:** System architectures MUST route all model outputs through enterprise Data Loss Prevention (DLP) engines to detect and redact sensitive information before reaching the end user.

## Real-World Examples
- **GPT-2 Memorization:** Security researchers successfully extracted verbatim PII, including names, phone numbers, and email addresses, directly from the public GPT-2 model.
- **Source Code Regurgitation:** Proprietary API keys and sensitive internal algorithms were perfectly replicated by code generation models trained on public and leaked repositories.

## References
- Carlini et al., "Extracting Training Data from Large Language Models" (USENIX Security 2021)
- OWASP LLM Top 10: LLM06 (Sensitive Information Disclosure)
- MITRE ATLAS: AML.TA0010
