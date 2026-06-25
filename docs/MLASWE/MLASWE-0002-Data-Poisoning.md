# MLASWE-0002: Data Poisoning

## Description
Data poisoning occurs when an adversary intentionally corrupts the training data to manipulate model behavior. This can be through direct injection of malicious samples, label manipulation, or subtle perturbation of existing training data. Poisoned models may perform well on validation sets while containing hidden backdoors or biases.

## Risk
- **Severity:** Critical
- **Exploitability:** Medium (requires access to data pipeline)
- **Prevalence:** Uncommon but growing

## Affected Components
- Training data ingestion pipelines
- Public dataset usage
- Crowdsourced or third-party labeled data
- Continuous/online learning systems

## Sub-types
| Type | Description | Detection Difficulty |
|------|-------------|---------------------|
| **Label poisoning** | Flipping or corrupting training labels | Low |
| **Data injection** | Adding malicious samples to training set | Medium |
| **Backdoor poisoning** | Inserting trigger patterns that cause targeted misclassification | High |
| **Clean-label poisoning** | Poisoning correctly labeled samples to be misclassified | Very High |

## Detection Methods
- **Statistical Outlier Detection:** Identify anomalous training samples via clustering
- **Activation Clustering:** Analyze neuron activations to find poisoned clusters
- **Data Sanitization:** Automated cleaning of training data before use
- **Robust Training:** Use training methods resistant to poisoning
- **Provenance Verification:** Check data origin and integrity

## Preventive Controls (MLASVS)
- **MLASVS-DATA-011:** Training data quality checks
- **MLASVS-DATA-002:** Cryptographic data integrity
- **MLASVS-DATA-024:** Automated data poisoning detection (L2)
- **MLASVS-DATA-025:** Adversarial data filtering (L2)
- **MLASVS-DATA-030:** Data trust scoring (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0020:** Data Poisoning (primary)
- **AML.T0020.001:** Label Poisoning
- **AML.T0020.002:** Backdoor Poisoning

## Remediation
1. **Data Provenance:** Verify data source integrity and maintain cryptographic hashes
2. **Data Sanitization:** Remove outliers, validate labels, filter suspicious samples
3. **Robust Training:** Use techniques like differential privacy that limit per-sample influence
4. **Data Lineage:** Track all data transformations and maintain version control
5. **Limited Data Sources:** Restrict training data to trusted, vetted sources

## Real-World Examples
- **Microsoft Tay chatbot** (2016): Poisoned via malicious tweets in training pipeline
- **Backdoor attack on face recognition:** Trigger-specific misclassification
- **Clean-label poisoning on ImageNet:** Poisoned samples indistinguishable from clean data

## References
- Gu et al., "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain" (2017)
- Shafahi et al., "Poison Frogs! Targeted Clean-Label Poisoning Attacks on Neural Networks" (2018)
- MITRE ATLAS: AML.T0020
