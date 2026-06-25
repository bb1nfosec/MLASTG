# MLASWE-0012: Training Data Leakage

## Description
Training data leakage occurs when a model inadvertently reveals its training data through outputs, embeddings, or extracted artifacts. LLMs are particularly susceptible as they can memorize and reproduce training data verbatim, exposing PII, proprietary code, confidential documents, or copyrighted content used during training.

## Risk
- **Severity:** High (privacy breach, IP theft, regulatory violation)
- **Exploitability:** Medium (requires crafting extraction prompts)
- **Prevalence:** Common in LLMs (demonstrated memorization in models of all sizes)

## Affected Components
- LLMs and generative AI models
- Models trained on web-scraped data containing PII
- Models fine-tuned on proprietary or sensitive documents
- Code completion models trained on private codebases

## Detection Methods
- **Extraction Attack Simulation:** Attempt to extract training data via prompt engineering
- **Output Monitoring:** Scan model outputs for verbatim training data reproduction
- **Deduplication Analysis:** Check for near-duplicate outputs to training data
- **Membership Inference:** Test if specific known data points were in training set

## Preventive Controls (MLASVS)
- **MLASVS-DATA-005:** PII/PHI detection in training data
- **MLASVS-DATA-010:** Data minimization
- **MLASVS-DATA-015:** Data de-identification
- **MLASVS-LLM-008:** Sensitive data exfiltration prevention
- **MLASVS-MODEL-019:** Differential privacy in model (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.TA0010:** Collection (training data exfiltration)

## Remediation
1. **Training Data Sanitization:** Remove PII and sensitive data from training sets
2. **Differential Privacy:** Train with DP-SGD to bound memorization
3. **Output Filtering:** Deploy detection for verbatim training data reproduction
4. **Deduplication:** Remove near-duplicate examples from training to reduce memorization
5. **Data Minimization:** Only include necessary data in training sets
6. **Memorization Testing:** Systematically test model for memorization of sensitive data

## Real-World Examples
- **GPT-2 extraction (Carlini 2021):** Extracted personal information (phone numbers, emails) from GPT-2
- **GitHub Copilot leaked API keys:** Generated code that included hardcoded credentials from training
- **Samsung ChatGPT leak (2023):** Engineers pasted proprietary code into ChatGPT

## References
- Carlini et al., "Extracting Training Data from Large Language Models" (USENIX Security 2021)
- Carlini et al., "Quantifying Memorization Across Neural Language Models" (2022)
- MITRE ATLAS: AML.TA0010
- OWASP LLM Top 10: LLM06
