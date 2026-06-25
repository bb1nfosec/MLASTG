# MLASWE-0001: Adversarial Perturbation

## Description
Adversarial perturbation involves crafting inputs with small, often imperceptible modifications that cause an ML model to produce incorrect outputs. These perturbations exploit the model's decision boundaries and are a fundamental weakness of most ML architectures.

## Risk
- **Severity:** High
- **Exploitability:** Medium (requires technical expertise)
- **Prevalence:** Common (almost all models are susceptible to some degree)

## Affected Components
- ML model inference endpoints
- Image classification, object detection, NLP models
- Any model receiving untrusted inputs

## Detection Methods
- **Adversarial Robustness Testing:** Generate adversarial examples using FGSM, PGD, DeepFool, CW attacks (see MLASTG-TEST-MODEL-001)
- **Input Validation Review:** Check for input bounds enforcement (see MOD-003)
- **Anomaly Detection:** Monitor for inputs with unusual feature distributions

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-001:** Adversarial robustness testing
- **MLASVS-MODEL-002:** Input perturbation limits
- **MLASVS-MODEL-003:** Model input validation
- **MLASVS-MODEL-010:** Anomalous input detection
- **MLASVS-MODEL-016:** Certified adversarial robustness (L2)
- **MLASVS-MODEL-024:** Adversarial training validation (L2)
- **MLASVS-MODEL-025:** Feature squeezing validation (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0010:** Adversarial Perturbation (primary)
- **AML.T0007:** Input Manipulation

## Remediation
1. **Adversarial Training:** Retrain with adversarial examples
2. **Input Preprocessing:** Apply feature squeezing, input sanitization
3. **Certified Defenses:** Implement randomized smoothing for provable robustness
4. **Input Validation:** Enforce input bounds and reject out-of-distribution samples
5. **Ensemble Methods:** Use diverse models to reduce transferability

## Real-World Examples
- **Image classifier evasion:** Stop sign misclassification via small sticker perturbations
- **NLP toxicity bypass:** Adversarial text that evades content filters
- **Speech recognition:** Audio perturbations imperceptible to humans that cause mis-transcription

## References
- Goodfellow et al., "Explaining and Harnessing Adversarial Examples" (2014)
- Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks" (2017)
- Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks" (2017)
