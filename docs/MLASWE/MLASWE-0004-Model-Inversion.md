# MLASWE-0004: Model Inversion

## Description
Model inversion attacks attempt to reconstruct the original training data from model outputs. By exploiting the model's confidence scores and gradients, attackers can generate class-representative samples that reveal sensitive training data. For example, a facial recognition model can be inverted to generate images that resemble individuals in the training set.

## Risk
- **Severity:** Medium (surface general features) to High (reconstruct specific records)
- **Exploitability:** Medium (requires white-box access or high-confidence API)
- **Prevalence:** Uncommon (more computationally intensive than other attacks)

## Affected Components
- Generative and discriminative models with high-dimensional outputs
- Facial recognition, medical diagnosis, and biometric models
- Any model trained on sensitive personal data

## Sub-types
| Type | Description | Data Leakage |
|------|-------------|--------------|
| **Class-based inversion** | Generate representative sample for a class label | Class features |
| **Registration-based inversion** | Reconstruct specific training record | Individual data |
| **Gradient-based inversion** | Recover data from model gradients (federated learning) | Precise records |

## Detection Methods
- **Reconstruction Attack Simulation:** Attempt inversion and measure similarity to training data
- **Differential Privacy Auditing:** Verify that DP guarantees bound inversion risk
- **Overfitting Analysis:** Check for memorization indicators

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-019:** Differential privacy in model (L2)
- **MLASVS-MODEL-020:** Membership inference prevention (L2)
- **MLASVS-DATA-019:** Differential privacy guarantees

## Attack Techniques (MITRE ATLAS)
- **AML.T0018:** Model Inversion (primary)

## Remediation
1. **Differential Privacy:** Train with DP-SGD to limit per-sample influence
2. **Confidence Limiting:** Reduce output precision, apply temperature scaling
3. **Regularization:** Apply strong regularization to prevent overfitting
4. **Output Filtering:** Suppress high-confidence predictions that enable inversion

## References
- Fredrikson et al., "Model Inversion Attacks that Exploit Confidence Information" (2015)
- Fredrikson et al., "Privacy in Pharmacogenetics: A Case Study" (2014)
- MITRE ATLAS: AML.T0018
