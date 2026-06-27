# MLASWE-0005: Membership Inference

## Description
Membership inference attacks occur when an adversary can ascertain whether a specific data record was included in a model's training dataset. In enterprise environments processing PII, PHI, or proprietary intellectual property, this vulnerability constitutes a critical privacy breach. An attacker MAY exploit the model's confidence scores or decision boundaries to infer the presence of sensitive records, thereby violating confidentiality guarantees and regulatory requirements (e.g., GDPR, HIPAA).

## Risk
- **Severity:** Medium (general privacy breach) to Critical (when inferring highly sensitive or regulated attributes)
- **Exploitability:** Medium (requires API access, target baseline data, and statistical analysis capabilities)
- **Prevalence:** Common (frequently observed in overfitted models or models trained on sparse datasets)

## Affected Components
- Classification models exposing high-precision confidence scores or logits.
- Models exhibiting significant overfitting to training data.
- Generative models capable of emitting exact memorized training artifacts.
- ML pipelines processing medical, financial, or other highly regulated data.

## Sub-types
| Type | Description | Information Leakage |
|------|-------------|---------------------|
| **Confidence-based** | The attacker utilizes output confidence scores to differentiate training vs. non-training data. | High |
| **Label-only** | The attacker infers membership solely from hard classification labels (requires a higher volume of queries). | Medium |
| **Black-box** | The attacker possesses only API access to the model, without knowledge of its internal parameters. | Medium |
| **White-box** | The attacker possesses full access to the model architecture, parameters, and gradients. | Critical |

## Detection Methods
- **Shadow Model Training:** Organizations SHOULD train shadow models mimicking the target to evaluate empirical membership inference vulnerability.
- **Confidence Distribution Analysis:** Security teams MUST monitor and compare confidence score distributions on known vs. unknown data.
- **Privacy Leakage Auditing:** Auditors MUST empirically measure privacy leakage against theoretical Differential Privacy (DP) bounds.

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-019:** Differential privacy in model (L2)
- **MLASVS-MODEL-020:** Membership inference prevention (L2)
- **MLASVS-DATA-019:** Differential privacy guarantees

## Attack Techniques (MITRE ATLAS)
- **AML.T0018:** Model Inversion (related technique)

## Remediation
1. **Differential Privacy:** Organizations MUST implement Differential Privacy (e.g., DP-SGD) during training to provide mathematical bounds on membership leakage.
2. **Regularization:** Engineers SHOULD employ robust regularization techniques (e.g., L1/L2 penalties, dropout, early stopping) to strictly mitigate overfitting.
3. **Output Obfuscation:** The system MUST restrict output granularity by clipping, rounding, or masking high-precision confidence vectors exposed to end users.
4. **Ensemble Methods:** Architecture SHOULD utilize model stacking or ensemble learning to reduce individual model memorization capacity.
5. **Data Minimization:** Teams MUST rigorously apply data minimization principles, ensuring only essential data is utilized for model training.

## Real-World Examples
- **Healthcare Data Leakage:** Attackers inferred patient participation in sensitive medical cohorts by analyzing the predictive confidence of clinical diagnostic models.
- **Genomic Privacy Breaches:** Membership inference attacks successfully identified individuals within genome-wide association study (GWAS) datasets.

## References
- Shokri et al., "Membership Inference Attacks Against Machine Learning Models" (IEEE S&P 2017)
- Carlini et al., "Membership Inference Attacks from First Principles" (2022)
- MITRE ATLAS: AML.T0018
