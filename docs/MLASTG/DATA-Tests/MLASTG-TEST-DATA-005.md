# MLASTG-TEST-DATA-005: Federated Learning Poisoning Detection

## Control Reference
**Controls Tested:** MLASVS-DATA-001 (Data Provenance Tracking), MLASVS-DATA-002 (Data Sanitization), MLASVS-DATA-004 (Training Data Integrity Verification), MLASVS-DATA-006 (Data Quality Monitoring), MLASVS-DATA-010 (Data Source Validation), MLASVS-DATA-019 (Differential Privacy for Distributed Training — L2), MLASVS-DATA-023 (Secure Aggregation Verification — L2)

## Severity
**High** (L1) / **Critical** (L2)

## Overview
Federated learning (FL) distributes training across multiple participants who never share raw data. This distributed architecture introduces unique poisoning attack surfaces: malicious participants can submit poisoned local model updates (model poisoning), manipulate local training data (data poisoning), or collude to skew the aggregated model. Byzantine-resilient aggregation, contribution auditing, and anomaly detection on updates are essential defenses. This test evaluates the resilience of federated learning pipelines against these attacks.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | `flower` (`pip install flwr`), `numpy`, `scikit-learn`, ART (`pip install adversarial-robustness-toolbox`) |
| Access | Federated learning pipeline (development/staging) |
| Documentation | FL architecture diagram, aggregation strategy, participant roster, update protocol |

## Step-by-Step Procedure

### Step 1: Map Federated Learning Architecture
1. Document the FL system components:
   - Aggregation server (central coordinator)
   - Participant nodes (edge devices, hospitals, organizations)
   - Communication protocol (gRPC, HTTP, MQTT)
   - Aggregation strategy (FedAvg, FedProx, Secure Aggregation)
   - Model update format (gradients, weights, deltas)
2. Identify trust boundaries between participants and the server
3. **Pass if:** Complete FL architecture documentation exists with trust boundaries
4. **Fail if:** Architecture is undocumented or trust boundaries are undefined

### Step 2: Test Byzantine-Resilient Aggregation
1. Simulate Byzantine participants submitting poisoned model updates:
   - **Label flipping:** Submit updates trained on inverted labels
   - **Scaling attack:** Multiply gradients by a large factor (e.g., 100x)
   - **Noise injection:** Submit random Gaussian noise as model updates
   - **Zero update:** Submit a zero vector (free-riding)
2. Inject these poisoned updates into the aggregation round alongside honest updates
3. Measure the impact on global model accuracy:
   ```python
   import numpy as np
   
   def label_flip_update(honest_update, flip_ratio=0.3):
       """Simulate a label-flipping attack on local gradients."""
       poisoned = honest_update.copy()
       n_params = len(poisoned)
       flip_indices = np.random.choice(n_params, int(n_params * flip_ratio), replace=False)
       poisoned[flip_indices] *= -1
       return poisoned
   
   def scaling_attack(honest_update, scale_factor=100):
       """Simulate a gradient scaling attack."""
       return honest_update * scale_factor
   ```
4. **Pass if:** Global model accuracy degrades by < 10% with up to 30% Byzantine participants
5. **Fail if:** A single malicious participant can degrade accuracy by > 20%

### Step 3: Test Gradient Inversion Attack
1. Attempt to reconstruct training data from shared gradients/updates:
   - Submit a known input to the FL protocol
   - Capture the resulting gradient update
   - Attempt reconstruction using gradient inversion techniques (DLG, Deep Leakage)
2. Measure reconstruction fidelity (cosine similarity, MSE between original and reconstructed)
3. **Pass if:** Gradient inversion does not recover meaningful training data
4. **Fail if:** Original training samples can be reconstructed with high fidelity

### Step 4: Test Contribution Auditing (L2)
1. Verify that each participant's contribution is logged with:
   - Participant ID (anonymized or pseudonymous)
   - Round number
   - Update magnitude and direction
   - Model performance contribution (if tracked)
2. Test whether a participant can submit updates under a different identity
3. **Pass if:** All contributions are attributed and identity spoofing is prevented
4. **Fail if:** Participants can submit anonymous updates or forge identity

### Step 5: Test Secure Aggregation (L2)
1. Verify that the aggregation protocol prevents the server from inspecting individual updates:
   - Homomorphic encryption (e.g., CKKS scheme)
   - Secure multi-party computation (SMPC)
   - Differential privacy noise addition
2. Attempt to extract individual participant updates from the aggregated model
3. **Pass if:** Individual updates cannot be reconstructed from the aggregation
4. **Fail if:** The server can inspect individual participant gradients

### Step 6: Test Differential Privacy in FL (L2)
1. Verify that differential privacy (DP) is applied to local updates before sharing:
   ```python
   # Gradient clipping + Gaussian noise
   def apply_dp_to_update(update, max_norm=1.0, noise_multiplier=0.1):
       clipped = np.clip(update, -max_norm, max_norm)
       noise = np.random.normal(0, noise_multiplier * max_norm, clipped.shape)
       return clipped + noise
   ```
2. Verify that the privacy budget (epsilon, delta) is tracked across rounds
3. **Pass if:** DP is enforced on shared updates with documented (epsilon, delta) budget

### Step 7: Test Model Update Validation
1. Verify that the aggregation server validates incoming updates:
   - Update shape consistency with global model
   - Update norm bounds (reject abnormally large gradients)
   - Update freshness (reject stale or replayed updates)
2. Submit malformed updates and verify rejection:
   - Wrong tensor dimensions
   - Updates exceeding norm thresholds
   - Replayed updates from previous rounds
3. **Pass if:** Malformed updates are rejected; only valid updates are aggregated

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | FL architecture documented; Byzantine-resilient aggregation verified; gradient inversion blocked; update validation enforced |
| L2 | All L1 controls met; secure aggregation prevents individual inspection; DP applied to shared updates; contribution auditing complete |

## Evidence Requirements

- [ ] FL architecture diagram with trust boundaries
- [ ] Byzantine resilience test results (accuracy with poisoned participants)
- [ ] Gradient inversion attack results
- [ ] (L2) Secure aggregation verification evidence
- [ ] (L2) DP configuration with privacy budget documentation
- [ ] Update validation test results

## Remediation Guidance

**If Byzantine resilience is insufficient:**
1. Implement robust aggregation (Krum, Trimmed Mean, Median Aggregation) instead of FedAvg
2. Add anomaly detection on incoming updates (norm-based, direction-based)
3. Limit the maximum number of participants per round

**If gradient inversion succeeds:**
1. Add differential privacy noise to local gradients before sharing
2. Increase gradient clipping to reduce information leakage
3. Consider secure aggregation (homomorphic encryption or SMPC)

**If update validation is absent:**
1. Implement server-side validation for update shape, norm, and freshness
2. Reject updates exceeding a norm threshold (e.g., > 2x median norm)
3. Track and reject replayed updates using round-number binding

## References
- **MITRE ATLAS:** AML.T0020 (Poison Training Data), AML.T0059 (Backdoor ML Model)
- **MLASWE:** MLASWE-0002 (Data Poisoning), MLASWE-0009 (Supply Chain Compromise)
- **Academic:** Bagdasaryan et al., "How to Backdoor Federated Learning" (2020)
- **Academic:** Zhu et al., "Deep Leakage from Gradients" (2019)
- **NIST AI RMF:** MAP 1.5 (Risk identification for distributed systems)
- **Framework:** FedML, PySyft, Flower FL security documentation
