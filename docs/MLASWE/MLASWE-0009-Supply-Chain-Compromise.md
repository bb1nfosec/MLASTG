# MLASWE-0009: Supply Chain Compromise

## Description
Supply chain compromise occurs when third-party ML components — pre-trained models, training datasets, ML libraries, or training infrastructure — contain security vulnerabilities, malicious code, or hidden backdoors that compromise the final ML system. This is especially dangerous in ML because compromised models can pass standard validation while containing hidden malicious behaviors.

## Risk
- **Severity:** Critical (stealthy, high-impact, difficult to detect)
- **Exploitability:** Hard (requires compromising upstream ML component)
- **Prevalence:** Uncommon but growing rapidly with ML adoption

## Affected Components
- Pre-trained models from public hubs (Hugging Face, PyTorch Hub, TF Hub)
- Third-party training datasets (Kaggle, academic datasets, web-scraped data)
- ML libraries and frameworks with vulnerabilities
- Cloud/third-party training infrastructure
- Transfer learning and fine-tuning pipelines

## Detection Methods
- **ML-SBOM Verification:** Inventory and scan all ML components
- **Model Scanning:** Detect unsafe code in model files (Pickle deserialization)
- **Dataset Integrity Verification:** Check cryptographic hashes and provenance
- **Dependency Scanning:** Identify known CVEs in ML libraries
- **Behavioral Analysis:** Test model behavior against expected ranges

## Preventive Controls (MLASVS)
- **MLASVS-SUPPLY-001 through 022:** Full supply chain controls
- **MLASVS-DATA-001, 002:** Data provenance and integrity
- **MLASVS-MODEL-021, 022:** Backdoor and trojan detection (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.TA0003:** Resource Development (supply chain compromise)

## Remediation
1. **ML-SBOM:** Generate and maintain complete Software Bill of Materials for all ML components
2. **Provenance Verification:** Use cryptographic signatures for models and datasets
3. **Model Scanning:** Scan model files for unsafe serialization code
4. **Dependency Scanning:** Use standard vulnerability scanners (Trivy, Snyk) for ML libraries
5. **Trusted Sources:** Restrict model/data sourcing to curated, vetted repositories
6. **Vendor Assessment:** Evaluate third-party AI vendors for security posture

## Real-World Examples
- **Hugging Face pickle exploits:** Malicious PyTorch models executing arbitrary code on load
- **Poisoned academic datasets:** Deliberately corrupted labels in public research datasets
- **PyPI typosquatting for ML packages:** Malicious packages with misspelled names of popular ML libraries

## References
- MITRE ATLAS: AML.TA0003
- OWASP LLM Top 10: LLM05
- Bagdasaryan et al., "How To Backdoor Federated Learning" (2020)
