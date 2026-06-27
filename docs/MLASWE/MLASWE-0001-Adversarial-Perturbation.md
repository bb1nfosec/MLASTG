# MLASWE-0001: Adversarial Perturbation

## Description
Adversarial perturbation involves the deliberate crafting of inputs with subtle, often imperceptible modifications designed to force a machine learning (ML) model to produce incorrect or targeted outputs. These perturbations exploit the highly non-linear decision boundaries of ML architectures. This vulnerability is fundamental to most contemporary deep learning models, representing a critical threat to system integrity.

## Risk
- **Severity:** High
- **Exploitability:** Medium (Requires moderate technical expertise and an understanding of the model's feature space)
- **Prevalence:** Pervasive (Virtually all continuous-input ML models are susceptible to some degree)

## Affected Components
- ML model inference endpoints (API and edge deployments)
- Image classification, object detection, and Natural Language Processing (NLP) models
- Any predictive model ingesting untrusted or externally-sourced inputs

## Detection Methods
- **Adversarial Robustness Testing:** Organizations MUST generate and evaluate adversarial examples using algorithms such as Fast Gradient Sign Method (FGSM), Projected Gradient Descent (PGD), DeepFool, and Carlini-Wagner (CW) (refer to MLASTG-TEST-MODEL-001).
- **Input Validation Review:** Implement continuous auditing of input bounds enforcement (refer to MLASVS-MODEL-003).
- **Anomaly Detection:** Monitor feature activations for inputs exhibiting statistically improbable distributions.

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-001:** Adversarial robustness testing
- **MLASVS-MODEL-002:** Input perturbation limits
- **MLASVS-MODEL-003:** Model input validation
- **MLASVS-MODEL-010:** Anomalous input detection
- **MLASVS-MODEL-016:** Certified adversarial robustness (L2)
- **MLASVS-MODEL-024:** Adversarial training validation (L2)
- **MLASVS-MODEL-025:** Feature squeezing validation (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0010:** Adversarial Perturbation (Primary)
- **AML.T0007:** Input Manipulation

## Remediation
1. **Adversarial Training:** The training pipeline MUST incorporate adversarial training by continuously augmenting the training corpus with adversarial examples (e.g., PGD, CW) to harden the model's decision boundaries.
2. **Input Preprocessing and Squeezing:** The inference architecture SHOULD apply strict input sanitization and feature squeezing (e.g., bit-depth reduction, spatial smoothing) to neutralize high-frequency perturbations prior to model ingestion.
3. **Certified Defenses:** High-assurance models MUST implement randomized smoothing or equivalent certified robustness techniques to provide mathematically provable guarantees against bounded perturbations (e.g., $L_2$ or $L_\infty$ norms).
4. **Input Validation Guardrails:** The system MUST enforce strict input bounding and employ state-of-the-art Out-of-Distribution (OOD) detection models as circuit breakers to drop anomalous or out-of-bounds samples before they reach the inference engine.
5. **Ensemble Architectures:** Deployments SHOULD utilize ensemble methods combining architecturally diverse models, significantly reducing the transferability of adversarial perturbations.

## Real-World Examples
- **Image Classifier Evasion:** Stop sign misclassification manipulated via strategically placed, low-visibility stickers.
- **NLP Toxicity Bypass:** Adversarial text structures containing homoglyphs or semantic perturbations that successfully evade content moderation filters.
- **Speech Recognition Anomalies:** Audio perturbations, imperceptible to the human ear, forcing forced mis-transcriptions or unauthorized command execution.

## References
- Goodfellow et al., "Explaining and Harnessing Adversarial Examples" (2014)
- Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks" (2017)
- Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks" (2017)
