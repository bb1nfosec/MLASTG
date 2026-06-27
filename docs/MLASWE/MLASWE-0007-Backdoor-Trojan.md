# MLASWE-0007: Backdoor/Trojan

## Description
A backdoor or trojan attack embeds a hidden trigger pattern into a model during training such that the model behaves normally on benign inputs but produces attacker-controlled outputs when the trigger is present. These attacks are extremely difficult to detect because the model passes standard validation and testing — the backdoor only activates on inputs containing the specific trigger.

## Risk
- **Severity:** Critical (stealthy, persistent, attacker-controlled behavior)
- **Exploitability:** Hard (requires poisoning the training process or supply chain)
- **Prevalence:** Rare but extremely dangerous

## Affected Components
- Models from third-party or pre-trained sources
- Transfer learning pipelines (fine-tuning compromised base models)
- Systems using public model zoos (Hugging Face, TorchHub, TF Hub)

## Sub-types
| Type | Description | Trigger |
|------|-------------|---------|
| **Patch-based backdoor** | Small visual patch triggers misclassification | Spatial (e.g., corner sticker) |
| **Blended backdoor** | Trigger blended into training images at low opacity | Visual blending |
| **Weight poisoning** | Direct manipulation of model weights post-training | None (always present) |
| **Input-independent backdoor** | Any input with a particular feature triggers misclassification | Semantic (e.g., specific color) |

## Detection Methods
- **Activation Clustering:** Analyze neuron activations for poisoned clusters
- **Trigger Inversion:** Reverse-engineer potential trigger patterns
- **Pruning-based Detection:** Remove or disable neurons that activate only on triggers
- **Spectral Signatures:** Analyze covariance of feature representations
- **Fine-tuning Analysis:** Check if fine-tuning removes backdoor behavior

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-021:** Backdoor detection validation (L2)
- **MLASVS-MODEL-022:** Trojan detection (L2)
- **MLASVS-DATA-024:** Automated data poisoning detection (L2)
- **MLASVS-SUPPLY-019:** Backdoor scanning of pre-trained models (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0020.002:** Data Poisoning - Backdoor

## Remediation
1. **Model Sanitization:** Apply pruning-based defenses to remove potential backdoor neurons
2. **Fine-tuning:** Fine-tune models on clean data to overwrite backdoor behavior
3. **Input Preprocessing:** Detect and neutralize trigger patterns in inputs
4. **Provenance:** Only use models from trusted, verifiable sources
5. **Robust Training:** Use training methods resistant to poisoning

## Real-World Examples
- **BadNets (2017):** First systematic demonstration of backdoor attacks on neural networks
- **Hugging Face poisoned models:** Researchers found backdoored models on public model hubs
- **Supply chain backdoor via pre-trained weight:** Trojan inserted into pre-trained ImageNet model

## References
- Gu et al., "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain" (2017)
- Chen et al., "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning" (2017)
- MITRE ATLAS: AML.T0020 (Data Poisoning), AML.T0020.000 (Backdoor Poisoning sub-technique)
