# MLASWE-0007: Backdoor/Trojan

## Description
A machine learning backdoor (or trojan) is a stealthy vulnerability where a model is intentionally compromised during training or fine-tuning to exhibit malicious behavior only when presented with a specific, attacker-defined trigger. In the absence of the trigger, the model MUST perform nominally, allowing it to evade standard quality assurance and validation testing. This constitutes a severe supply chain and integrity risk.

## Risk
- **Severity:** Critical (enables persistent, targeted, and attacker-controlled outcomes)
- **Exploitability:** High (if the adversary has supply chain access); Low (post-deployment)
- **Prevalence:** Rare in the wild, but represents a catastrophic systemic risk for enterprise ML.

## Affected Components
- Pre-trained foundational models sourced from public repositories (e.g., Hugging Face, TorchHub).
- Transfer learning and fine-tuning pipelines utilizing third-party weights.
- Federated learning environments lacking robust aggregation defenses.
- Outsourced Model-as-a-Service (MaaS) training environments.

## Sub-types
| Type | Description | Trigger Nature |
|------|-------------|----------------|
| **Patch-based** | A localized visual anomaly (e.g., a specific pixel pattern or sticker) forces misclassification. | Spatial / Visual |
| **Blended** | The trigger is subtly blended into inputs globally (e.g., specific image noise). | Latent |
| **Semantic** | The model triggers upon a specific contextual concept (e.g., a specific word or phrase in NLP). | Contextual |
| **Weight Poisoning** | Direct surgical modification of model weights post-training to embed the backdoor. | Structural |

## Detection Methods
- **Activation Clustering:** Security teams SHOULD analyze neural activation patterns to identify anomalous clusters indicating trojaned neurons.
- **Trigger Inversion:** Analysts MUST attempt to mathematically reverse-engineer potential triggers using optimization techniques (e.g., Neural Cleanse).
- **Spectral Signatures:** Data pipelines SHOULD evaluate the covariance of latent feature representations to detect poisoned training samples.
- **Robustness Auditing:** QA teams MUST test models against out-of-distribution and adversarial inputs prior to production deployment.

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-021:** Backdoor detection validation (L2)
- **MLASVS-MODEL-022:** Trojan detection (L2)
- **MLASVS-DATA-024:** Automated data poisoning detection (L2)
- **MLASVS-SUPPLY-019:** Backdoor scanning of pre-trained models (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0020.002:** Data Poisoning - Backdoor

## Remediation
1. **Provenance Verification:** Organizations MUST strictly source models and datasets from trusted, cryptographically verifiable vendors.
2. **Model Sanitization:** Engineering teams SHOULD employ model pruning to surgically excise dormant neurons that may harbor backdoor logic.
3. **Robust Aggregation:** Federated learning systems MUST utilize robust aggregation protocols (e.g., Krum, Trimmed Mean) to neutralize malicious updates.
4. **Adversarial Fine-Tuning:** Teams SHOULD subject third-party models to rigorous fine-tuning on highly curated, clean datasets to overwrite potential trojan behaviors.
5. **Input Anomaly Detection:** Systems MUST deploy runtime input sanitization to detect and strip potential physical or digital triggers.

## Real-World Examples
- **BadNets (2017):** Demonstrated the feasibility of backdooring deep neural networks by poisoning a small fraction of training data, causing targeted misclassification.
- **Public Model Hubs:** Security researchers have routinely identified backdoored or maliciously modified models hosted on public platforms, waiting for enterprise integration.

## References
- Gu et al., "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain" (2017)
- Wang et al., "Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks" (2019)
- MITRE ATLAS: AML.T0020.002
