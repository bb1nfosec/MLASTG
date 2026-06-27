# MLASWE-0002: Data Poisoning

## Description
Data poisoning occurs when an adversary intentionally corrupts or manipulates the training data to alter the subsequent behavior of a machine learning model. This vector includes the direct injection of malicious samples, strategic label manipulation, or the subtle perturbation of existing training artifacts. Compromised models may exhibit high accuracy on standard validation sets while harboring latent backdoors, vulnerabilities, or targeted biases that manifest only under attacker-specified conditions.

## Risk
- **Severity:** Critical
- **Exploitability:** Medium (Requires access to the data ingestion pipeline, crowdsourced inputs, or continuous learning feedback loops)
- **Prevalence:** Uncommon but rapidly escalating in federated and online learning environments

## Affected Components
- Training data ingestion and preprocessing pipelines
- Models reliant on public or open-source datasets
- Crowdsourced or third-party labeled data platforms
- Continuous, online, and federated learning systems

## Sub-types
| Type | Description | Detection Difficulty |
|------|-------------|---------------------|
| **Label Poisoning** | Deliberately flipping or corrupting training labels to degrade model accuracy. | Low |
| **Data Injection** | Injecting novel, malicious samples into the training corpus. | Medium |
| **Backdoor Poisoning** | Inserting hidden trigger patterns that force targeted misclassification during inference. | High |
| **Clean-Label Poisoning** | Poisoning mathematically correct labels with imperceptible feature space perturbations. | Very High |

## Detection Methods
- **Statistical Outlier Detection:** Implement robust anomaly detection algorithms (e.g., Isolation Forests) to identify statistically anomalous training samples.
- **Activation Clustering:** Analyze deep neural network hidden layer activations to detect and isolate poisoned data clusters.
- **Automated Data Sanitization:** Employ automated data cleansing pipelines that enforce strict schema and distribution adherence prior to ingestion.
- **Cryptographic Provenance:** Validate the cryptographic hash and origin signature of all external datasets.

## Preventive Controls (MLASVS)
- **MLASVS-DATA-011:** Training data quality checks
- **MLASVS-DATA-002:** Cryptographic data integrity
- **MLASVS-DATA-024:** Automated data poisoning detection (L2)
- **MLASVS-DATA-025:** Adversarial data filtering (L2)
- **MLASVS-DATA-030:** Data trust scoring (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0020:** Data Poisoning (Primary)
- **AML.T0020.001:** Label Poisoning
- **AML.T0020.002:** Backdoor Poisoning

## Remediation
1. **Cryptographic Data Provenance:** Organizations MUST enforce strict data provenance by validating cryptographic hashes (e.g., SHA-256) and digital signatures for all training data prior to ingestion.
2. **Data Sanitization Pipelines:** Data pipelines MUST implement rigorous sanitization, actively rejecting statistical outliers, validating label integrity, and applying adversarial filters to drop suspicious samples.
3. **Robust Training and Differential Privacy:** Training procedures SHOULD leverage robust optimization techniques, such as Differentially Private Stochastic Gradient Descent (DP-SGD), to mathematically bound the influence of any single training sample, thereby neutralizing clean-label poisoning.
4. **Immutable Data Lineage:** The architecture MUST maintain an immutable data lineage ledger, tracking all data transformations and maintaining strict version control to facilitate forensic rollback.
5. **Zero-Trust Data Sourcing:** Models MUST only ingest training data from explicitly trusted, continuously vetted sources, applying zero-trust principles to any third-party or crowdsourced data.

## Real-World Examples
- **Microsoft Tay Chatbot (2016):** An online learning pipeline poisoned via coordinated malicious inputs, rapidly degrading the model's output alignment.
- **Facial Recognition Backdoors:** Insertion of specific trigger artifacts (e.g., specialized glasses) resulting in deterministic misclassification of targeted individuals.
- **Clean-Label Poisoning on ImageNet:** The introduction of mathematically poisoned samples that appear benign to human reviewers but corrupt the model's feature extraction logic.

## References
- Gu et al., "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain" (2017)
- Shafahi et al., "Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks" (2018)
- MITRE ATLAS: AML.T0020
