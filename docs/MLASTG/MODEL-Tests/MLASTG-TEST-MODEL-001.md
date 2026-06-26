# MLASTG-TEST-MODEL-001: Adversarial Robustness & Evasion Testing

## Control Reference
**Controls Tested:** MLASVS-MODEL-001 (Adversarial Robustness Testing), MLASVS-MODEL-002 (Input Perturbation Limits), MLASVS-MODEL-003 (Model Input Validation), MLASVS-MODEL-010 (Anomalous Input Detection), MLASVS-MODEL-012 (Resource Limits on Inference), MLASVS-MODEL-016 (Certified Adversarial Robustness - L2), MLASVS-MODEL-017 (Robustness Certification - L2), MLASVS-MODEL-024 (Adversarial Training Validation - L2), MLASVS-MODEL-025 (Feature Squeezing Validation - L2), MLASVS-MODEL-026 (Model Ensemble Diversity - L2), MLASVS-MODEL-027 (Certified Defense Mechanisms - L2), MLASVS-MODEL-028 (Red Team Exercise Completion - L2), MLASVS-MODEL-029 (Continuous Adversarial Retesting - L2)

## Severity
**High** (L1) / **Critical** (L2)

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | IBM ART (`pip install adversarial-robustness-toolbox`) |
| Model Access | White-box (architecture + weights) or black-box (API access) |
| Test Data | Minimum 1000 representative test samples |
| Compute | GPU recommended for iterative attacks (PGD, CW) |

## Step-by-Step Procedure

### Step 1: Establish Baseline Performance
1. Load the target model and test dataset
2. Evaluate clean (unperturbed) accuracy
3. Record baseline metrics:
   ```python
   import numpy as np
   from art.estimators.classification import PyTorchClassifier

   classifier = PyTorchClassifier(
       model=model, loss=criterion,
       input_shape=(3, 32, 32), nb_classes=10,
       clip_values=(0.0, 1.0)
   )

   # ART uses predict(); accuracy must be computed manually
   predictions = classifier.predict(x_test)
   clean_accuracy = np.sum(
       np.argmax(predictions, axis=1) == np.argmax(y_test, axis=1)
   ) / len(y_test)
   print(f"Clean accuracy: {clean_accuracy:.4f}")
   ```

### Step 2: Execute White-Box Evasion Attacks (L1)
1. Generate adversarial examples using Fast Gradient Sign Method (FGSM) at two perturbation budgets:
   ```python
   from art.attacks.evasion import FastGradientMethod

   # Moderate perturbation (L1 pass threshold)
   attack_fgsm_01 = FastGradientMethod(estimator=classifier, eps=0.1)
   x_test_adv_fgsm_01 = attack_fgsm_01.generate(x=x_test)
   preds_fgsm_01 = classifier.predict(x_test_adv_fgsm_01)
   accuracy_fgsm_01 = np.sum(
       np.argmax(preds_fgsm_01, axis=1) == np.argmax(y_test, axis=1)
   ) / len(y_test)

   # Strong perturbation (L2 stress test)
   attack_fgsm_03 = FastGradientMethod(estimator=classifier, eps=0.3)
   x_test_adv_fgsm_03 = attack_fgsm_03.generate(x=x_test)
   preds_fgsm_03 = classifier.predict(x_test_adv_fgsm_03)
   accuracy_fgsm_03 = np.sum(
       np.argmax(preds_fgsm_03, axis=1) == np.argmax(y_test, axis=1)
   ) / len(y_test)
   ```
2. Generate using Projected Gradient Descent (PGD):
   ```python
   from art.attacks.evasion import ProjectedGradientDescent

   attack_pgd = ProjectedGradientDescent(
       estimator=classifier, eps=0.3, eps_step=0.01,
       max_iter=40, targeted=False
   )
   x_test_adv_pgd = attack_pgd.generate(x=x_test)
   preds_pgd = classifier.predict(x_test_adv_pgd)
   accuracy_pgd = np.sum(
       np.argmax(preds_pgd, axis=1) == np.argmax(y_test, axis=1)
   ) / len(y_test)
   ```

### Step 3: Execute Black-Box Evasion Attacks (L1)
1. Generate using HopSkipJump attack (decision-based; no gradient access required):
   ```python
   from art.attacks.evasion import HopSkipJump

   attack_hsj = HopSkipJump(
       classifier=classifier, targeted=False,
       max_iter=50, max_eval=10000, init_eval=100
   )
   x_test_adv_hsj = attack_hsj.generate(x=x_test)
   preds_hsj = classifier.predict(x_test_adv_hsj)
   accuracy_hsj = np.sum(
       np.argmax(preds_hsj, axis=1) == np.argmax(y_test, axis=1)
   ) / len(y_test)
   ```
2. Document total query count and attack success rate per sample

### Step 4: Analyze Robustness Metrics
1. Summarize accuracy under each attack in a results table:
   ```
   Attack          | ε     | Clean Acc | Attacked Acc | Degradation | Result
   ----------------|-------|-----------|--------------|-------------|--------
   FGSM (moderate) | 0.1   | 94.2%     | 72.1%        | 22.1%       | ✅ Pass
   FGSM (strong)   | 0.3   | 94.2%     | 55.3%        | 38.9%       | ❌ Fail
   PGD (40 steps)  | 0.3   | 94.2%     | 48.7%        | 45.5%       | ❌ Fail
   HopSkipJump     | N/A   | 94.2%     | 78.4%        | 15.8%       | ✅ Pass
   ```
   *(values above are illustrative examples — replace with actual results)*
2. **L1 Pass Condition:** Accuracy drop ≤ 25% under FGSM at ε = 0.1 (moderate perturbation)
3. **L1 Fail Condition:** Accuracy drop > 25% under FGSM at ε = 0.1
4. **Note:** Strong-perturbation results (ε = 0.3) are informational for L1; they become pass/fail criteria only at L2

### Step 5: Test Input Validation (L1)
1. Send inputs outside expected range (very large/small values)
2. Send inputs with incorrect dimensions
3. Send inputs with NaN/Inf values
4. **Pass if:** Invalid inputs are rejected with appropriate errors (not processed)

### Step 6: Execute Certified Robustness Evaluation (L2)
1. Implement randomized smoothing certification:
   ```python
   # Generate smoothed classifier with Gaussian noise
   # Evaluate certified radius at 95% confidence
   # For at least 1000 test samples
   ```
2. Document certified accuracy at different radii
3. **L2 Pass Condition:** Certified accuracy ≥ 80% at radius r ≥ 0.1 (L2 norm)

### Step 7: Validate Adversarial Training (L2)
1. Verify training pipeline includes adversarial training (e.g., PGD-AT or TRADES)
2. Compare robust accuracy of the adversarially trained model against the standard trained baseline **under the same attack and budget (ε = 0.3, PGD-40)**
3. Test against attack types not used during adversarial training to assess generalization (e.g., train on PGD, test with CW or AutoAttack)
4. **Pass if:** Adversarially trained model achieves >15% higher robust accuracy than the standard trained model under the same attack budget

### Step 8: Test Input Detection Capabilities (L2)
1. Deploy feature squeezing defense:
   ```python
   from art.defences.preprocessor import FeatureSqueezing
   
   squeeze = FeatureSqueezing(bit_depth=5, clip_values=(0.0, 1.0))
   ```
2. Test detection rate of adversarial inputs
3. **Pass if:** Detection rate > 80% with false positive < 5%

### Step 9: Review Red Team Reports (L2)
1. Verify red team exercises were conducted within the last quarter
2. Review findings for evasion-related vulnerabilities
3. Confirm findings are tracked to remediation
4. **Pass if:** Red team exercises are conducted at least quarterly with tracked remediation

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Accuracy drop ≤ 25% under FGSM (ε=0.1) and PGD (ε=0.3, 40 steps); input validation enforces bounds |
| L2 | Certified robust accuracy ≥ 80% at r ≥ 0.1; adversarial training validated; quarterly red team exercises; continuous testing in CI/CD |

## Evidence Requirements

- [ ] Baseline clean accuracy
- [ ] Accuracy under FGSM, PGD, and one black-box attack
- [ ] Input validation test results
- [ ] (L2) Certified robustness evaluation results
- [ ] (L2) Adversarial training comparison
- [ ] (L2) Feature squeezing detection results
- [ ] (L2) Red team exercise reports
- [ ] (L2) CI/CD robustness test integration evidence

## Remediation Guidance

**If robustness is insufficient:**
1. Implement adversarial training with PGD-based examples
2. Apply feature squeezing preprocessing
3. Increase model capacity/resilience
4. Implement ensemble methods for diverse defenses
5. Consider certified defenses (randomized smoothing)

## References
- **MITRE ATLAS:**
  - `AML.T0010` — Adversarial Examples (Evasion)
  - `AML.T0037` — Craft Adversarial Data
  - `AML.T0007` — Discover Model Ontology
- **MLASWE:** MLASWE-0001 (Adversarial Perturbation)
- **NIST AI RMF:** MEASURE 1.1, MANAGE 2.2
- **NIST AI 100-2e2025:** Section 2.1 — Evasion Attacks
- **Academic:** Madry et al. (2018) "Towards Deep Learning Models Resistant to Adversarial Attacks"
