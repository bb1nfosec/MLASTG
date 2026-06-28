# MLASVS-MODEL-1: Adversarial Robustness

## Category
MLASVS-MODEL: Model Security

## Overview
Adversarial robustness testing evaluates a model's resilience against inputs that have been intentionally perturbed to cause misclassification or incorrect outputs. This is a fundamental security property for any ML model exposed to untrusted inputs.

## Subcategories

### MODEL-1a: Adversarial Robustness Testing (Controls MODEL-001, MODEL-002, MODEL-003, MODEL-010, MODEL-016, MODEL-017, MODEL-024, MODEL-025, MODEL-026, MODEL-027, MODEL-028, MODEL-029)
Testing and hardening against evasion attacks using perturbation-based inputs.

### MODEL-1b: API & Resource Protection (Controls MODEL-005, MODEL-006, MODEL-012)
Protecting model endpoints from abuse during adversarial testing or attacks.

### MODEL-1c: Behavior Monitoring (Controls MODEL-009, MODEL-011, MODEL-013)
Detecting adversarial attacks through anomalous input/output patterns.

## Controls

### MODEL-001: Adversarial Robustness Testing (L1)
**Description:** Models must be tested against common adversarial attack methods (FGSM, PGD for white-box; HopSkipJump, Boundary Attack for black-box).

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Prerequisites:**
- IBM Adversarial Robustness Toolbox (ART) installed
- Access to model for querying
- Test dataset with at least 1000 samples

**Verification Steps:**
1. Select evasion attack appropriate to model type (classification, regression, etc.)
2. Generate adversarial examples using at minimum FGSM (ε = 0.1, 0.3) and PGD (ε = 0.3, steps = 40)
3. Measure accuracy under attack
4. Compare against baseline clean accuracy

**Acceptance Criteria:**
- L1: Accuracy drop under attack ≤ 25% for moderate perturbations (ε = 0.1)
- L2: Accuracy drop under attack ≤ 15% with certified robustness bounds

**Pass Condition:** Model shows robustness against at least one white-box and one black-box attack method.

---

### MODEL-002: Input Perturbation Limits (L1)
**Description:** Models must define and enforce maximum allowed input perturbation boundaries.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Identify maximum allowed L-infinity or L2 perturbation bound for input space
2. Verify that perturbations exceeding this bound are rejected
3. Test at boundary to confirm correct enforcement

**Remediation:** Implement input validation that checks for perturbation magnitude relative to expected input distribution.

---

### MODEL-003: Model Input Validation (L1)
**Description:** All inputs to the model must be validated against expected ranges, types, and formats before inference.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Review input validation logic in the serving infrastructure
2. Test with out-of-range values, wrong types, extreme values
3. Verify that invalid inputs are rejected with appropriate errors

**Remediation:** Implement comprehensive input schema validation using libraries like Pydantic or Cerberus.

---

### MODEL-016: Certified Adversarial Robustness (L2)
**Description:** For high-security models, certified (provable) robustness bounds must be established using methods like randomized smoothing or Lipschitz-based certification.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Implement certified robustness verification using randomized smoothing
2. Verify certified radius at 95% confidence for at least 1000 test samples
3. Measure certified accuracy at different radii
4. Document certified robustness guarantees

**Acceptance Criteria:** Certified accuracy ≥ 80% at radius r ≥ 0.1 for L2 norm perturbations.

---

### MODEL-024: Adversarial Training Validation (L2)
**Description:** Models trained for sensitive applications must incorporate adversarial training as a defense mechanism.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Verify that training pipeline includes adversarial training step
2. Confirm adversarial examples are generated during each training epoch
3. Compare robustness of adversarially trained vs. standard model
4. Verify robustness transfer to novel attack types not used during training

**Remediation:** Implement PGD-based adversarial training with periodic retraining against newly discovered attack methods.

---

### MODEL-028: Red Team Exercise Completion (L2)
**Description:** Regular adversarial red team exercises must be conducted against the model by independent security teams.

**MITRE ATLAS:** AML.TA0001 (Reconnaissance)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Review red team exercise reports
2. Verify that exercises include both white-box and black-box scenarios
3. Confirm that findings are tracked to remediation
4. Check that exercises are repeated at least quarterly

---

### MODEL-029: Continuous Adversarial Retesting (L2)
**Description:** Models must be continuously tested against new adversarial attack methods in a CI/CD pipeline.

**MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
**Test Reference:** MLASTG-TEST-MODEL-001

**Verification:**
1. Verify that adversarial robustness tests are incorporated into CI/CD
2. Check that new attack methods from the latest research are periodically added
3. Confirm that robustness regression triggers automated alerts

## Attack Methods Reference

| Attack | Type | Strength | Use Case |
|--------|------|----------|----------|
| **FGSM** | White-box (gradient) | Moderate | Quick robustness baseline |
| **PGD** | White-box (iterative) | Strong | Near-optimal worst-case evaluation |
| **DeepFool** | White-box (iterative) | Strong | Minimal perturbation search |
| **CW (Carlini-Wagner)** | White-box (optimization) | Very Strong | Targeted attacks, defense evaluation |
| **HopSkipJump** | Black-box (boundary) | Strong | No gradient access required |
| **Boundary Attack** | Black-box (decision) | Moderate | Only decision boundary access |
| **SimBA** | Black-box (query) | Moderate | Query-efficient attack |

## Defense Methods Reference

| Defense | Type | Best Against |
|---------|------|-------------|
| **Adversarial Training** | Reactive | Known attack types |
| **Feature Squeezing** | Proactive | High-frequency perturbations |
| **Randomized Smoothing** | Certified | L2 norm attacks (provable) |
| **Ensemble Defense** | Reactive | Transfer attacks |
| **Gradient Masking** | Obsolete | Not recommended (bypassable) |

## Cross-References

- **MITRE ATLAS:** AML.T0043 (Craft Adversarial Data)
- **NIST AI RMF:** MEASURE-1, MEASURE-2, MANAGE-1
- **NIST AI 100-2e2025:** Evasion category
- **OWASP AI Exchange:** Input Threats, AI Security Testing
- **OWASP ML Top 10:** ML01 (Input Manipulation)
