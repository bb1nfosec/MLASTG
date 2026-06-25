# MLASWE-0005: Membership Inference

## Description
Membership inference attacks determine whether a specific data point was part of the model's training set. This privacy breach can reveal sensitive information about individuals whose data was used in training — for example, determining that a particular patient's records were used to train a medical diagnosis model, implying that individual has that medical condition.

## Risk
- **Severity:** Medium (privacy breach) to High (when used to infer sensitive attributes)
- **Exploitability:** Medium (requires model API access and some baseline data)
- **Prevalence:** Common (most overfitted models are vulnerable)

## Affected Components
- Classification models with confidence outputs
- Models with significant overfitting
- Medical, financial, and other sensitive-data models

## Sub-types
| Type | Description | Information Leakage |
|------|-------------|---------------------|
| **Confidence-based** | Attack uses output confidence scores to distinguish training vs. non-training data | High leakage |
| **Label-only** | Attack uses only hard labels without confidence scores | Lower leakage, more queries needed |
| **Black-box** | No access to model internals, only API | Medium |
| **White-box** | Full access to model parameters and gradients | Maximum leakage |

## Detection Methods
- **Shadow Model Training:** Train attack models to distinguish training vs. non-training data
- **Confidence Distribution Analysis:** Compare confidence scores on known vs. unknown data
- **Differential Privacy Auditing:** Measure empirical privacy leakage against DP guarantees

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-019:** Differential privacy in model (L2)
- **MLASVS-MODEL-020:** Membership inference prevention (L2)
- **MLASVS-DATA-019:** Differential privacy guarantees

## Attack Techniques (MITRE ATLAS)
- **AML.T0018:** Model Inversion (related technique)

## Remediation
1. **Differential Privacy:** Train with DP-SGD (provable membership inference resistance)
2. **Regularization:** Reduce overfitting through L1/L2 regularization, dropout
3. **Model Stacking:** Use ensemble methods that reduce overfitting
4. **Output Obfuscation:** Limit prediction vector precision, round or clip outputs

## Real-World Examples
- **Hospital readmission model:** Attackers determined which patients' records were used to train a readmission prediction model, inferring those patients had higher readmission risk
- **Genome-wide association studies:** Membership inference on genomic data models revealed individual participation in sensitive studies

## References
- Shokri et al., "Membership Inference Attacks Against Machine Learning Models" (IEEE S&P 2017)
- Carlini et al., "Membership Inference Attacks from First Principles" (2022)
- MITRE ATLAS: AML.T0018
