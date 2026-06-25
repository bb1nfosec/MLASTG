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
   from art.estimators.classification import PyTorchClassifier
   
   classifier = PyTorchClassifier(
       model=model, loss=criterion,
       input_shape=(3, 32, 32), nb_classes=10,
       clip_values=(0.0, 1.0)
   )
   clean_accuracy = classifier._model.evaluate(x_test, y_test)[1]
   print(f"Clean accuracy: {clean_accuracy:.4f}")
   ```

### Step 2: Execute White-Box Evasion Attacks (L1)
1. Generate adversarial examples using Fast Gradient Sign Method (FGSM):
   ```python
   from art.attacks.evasion import FastGradientMethod
   
   attack = FastGradientMethod(estimator=classifier, eps=0.3)
   x_test_adv_fgsm = attack.generate(x=x_test)
   accuracy_fgsm = classifier._model.evaluate(x_test_adv_fgsm, y_test)[1]
   ```
2. Generate using Projected Gradient Descent (PGD):
   ```python
   from art.attacks.evasion import ProjectedGradientDescent
   
   attack = ProjectedGradientDescent(
       estimator=classifier, eps=0.3, eps_step=0.01,
       max_iter=40, targeted=False
   )
   x_test_adv_pgd = attack.generate(x=x_test)
   accuracy_pgd = classifier._model.evaluate(x_test_adv_pgd, y_test)[1]
   ```

### Step 3: Execute Black-Box Evasion Attacks (L1)
1. Generate using HopSkipJump attack:
   ```python
   from art.attacks.evasion import HopSkipJump
   
   attack = HopSkipJump(
       classifier=classifier, targeted=False,
       max_iter=50, max_eval=10000, init_eval=100
   )
   x_test_adv_hsj = attack.generate(x=x_test)
   accuracy_hsj = classifier._model.evaluate(x_test_adv_hsj, y_test)[1]
   ```
2. Document query budget and success rate

### Step 4: Analyze Robustness Metrics
1. Calculate accuracy under each attack:
   ```
   Attack    | Clean Acc | Attacked Acc | Degradation
   ----------|-----------|--------------|------------
   FGSM      | 94.2%     | 72.1%        | 22.1%
   PGD       | 94.2%     | 55.3%        | 38.9%
   HopSkipJump | 94.2%   | 78.4%        | 15.8%
   ```
2. **L1 Pass Condition:** Accuracy drop ≤ 25% for moderate perturbations (ε = 0.1)
3. **L1 Fail Condition:** Accuracy drop > 25% for any attack

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
1. Verify training pipeline includes adversarial training
2. Compare robust accuracy of adversarially vs. standard trained model
3. Test against attack types not used during training (generalization)
4. **Pass if:** Adversarially trained model shows >15% improvement in robust accuracy

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
- **MITRE ATLAS:** AML.T0010, AML.T0037, AML.T0007
- **MLASWE:** MLASWE-0001 (Adversarial Perturbation)
- **NIST AI RMF:** MEASURE-1, MANAGE-1
- **NIST AI 100-2e2025:** Evasion attacks
