# MLASTG-TEST-MODEL-002: Model Extraction Resistance Testing

## Control Reference
**Controls Tested:** MLASVS-MODEL-004 (Output Confidence Calibration), MLASVS-MODEL-005 (API Rate Limiting), MLASVS-MODEL-006 (Access Control on Model Endpoints), MLASVS-MODEL-018 (Extraction Resistance Validation — L2), MLASVS-MODEL-023 (Model Watermarking — L2)

## Severity
**High** (L1) / **Critical** (L2)

## Overview
Model extraction attacks allow an adversary to reconstruct a functional copy of a proprietary model by querying the model's API and using the query-response pairs to train a surrogate model. This test verifies that the system applies rate limiting, output truncation, authentication, and optional watermarking to resist such attacks.

## Prerequisites

| Requirement | Details |
|-------------|---------|
| Tools | IBM ART (`pip install adversarial-robustness-toolbox`), PrivacyRaven (`pip install privacyraven`) |
| Access | API access to the model inference endpoint |
| Query Budget | Ability to send at least 10,000 queries for surrogate model training |
| Data | Held-out test dataset with ground truth labels |

## Step-by-Step Procedure

### Step 1: Verify Output Precision
1. Query the model and inspect confidence/probability output values
2. Check the number of decimal places returned in confidence scores
3. **Pass if:** Confidence scores are limited to ≤ 3 decimal places or returned as top-k classes only (not full probability vector)
4. **Fail if:** Full-precision probability vectors (6+ decimal places) are returned — this enables high-fidelity extraction

### Step 2: Verify API Authentication
1. Send inference requests without an authentication token
2. Send requests with an invalid token
3. Send requests with an expired token
4. **Pass if:** All unauthenticated or invalid requests are rejected with HTTP 401 or 403

### Step 3: Verify Rate Limiting
1. Send requests at an escalating rate (10 req/s, 50 req/s, 100 req/s)
2. Document the rate limit threshold and the response returned when it is exceeded
3. **Pass if:** Rate limits are enforced per user or API key with a documented threshold and 429 response

### Step 4: Surrogate Model Training Attack (L2)
1. Collect at least 10,000 query-response pairs from the target model API
2. Train a surrogate model on the collected query-response pairs using the same architecture family as the target (if known) or a generic architecture:
   ```python
   from art.attacks.extraction import KnockoffNets
   from art.estimators.classification import PyTorchClassifier
   import numpy as np

   # Wrap target model (black-box: only API access)
   target_classifier = PyTorchClassifier(
       model=target_api_wrapper,
       loss=criterion,
       input_shape=input_shape,
       nb_classes=num_classes
   )

   # Run KnockoffNets extraction attack
   attack = KnockoffNets(
       classifier=target_classifier,
       batch_size_fit=32,
       batch_size_query=32,
       nb_epochs=10,
       nb_stolen=10000,
       sampling_strategy="random"
   )
   surrogate_classifier = attack.extract(x_steal, thieved_classifier=surrogate_model)

   # Evaluate fidelity: compare surrogate vs target on held-out test set
   target_preds   = np.argmax(target_classifier.predict(x_test), axis=1)
   surrogate_preds = np.argmax(surrogate_classifier.predict(x_test), axis=1)
   fidelity = np.mean(target_preds == surrogate_preds)
   print(f"Surrogate fidelity: {fidelity:.4f}")
   ```
3. **Pass if:** Surrogate model fidelity < 0.80 (achieves less than 80% agreement with the target model on the held-out test set)
4. **Fail if:** Fidelity ≥ 0.80 — the model can be reproduced to high accuracy through API queries alone

### Step 5: Verify Model Watermarking (L2)
1. Obtain the set of known watermark trigger inputs from the model owner
2. Query the model with each trigger and record the outputs
3. Verify that the watermark signature is detectable and unique
4. **Pass if:** Model outputs contain a detectable watermark on trigger inputs that would allow attribution of extracted models

## Expected Result

| Level | Expected Outcome |
|-------|-----------------|
| L1 | Unauthenticated requests rejected; confidence output precision limited; rate limiting enforced with documented threshold |
| L2 | Surrogate model fidelity < 80% after 10,000 queries; model watermarking detectable and attributable |

## Evidence Requirements

- [ ] Output precision test results (number of decimal places in confidence scores)
- [ ] Authentication rejection test results (401/403 on unauthenticated requests)
- [ ] Rate limit threshold documentation and response example
- [ ] (L2) Surrogate model training results with fidelity score
- [ ] (L2) Watermark detection results and trigger-response log

## Remediation Guidance

**If output precision is too high:**
1. Truncate confidence scores to 3 decimal places at the API output layer
2. Return only top-k predictions rather than full probability vectors
3. Add calibrated noise to confidence scores (prediction API randomization)

**If rate limiting is absent or insufficient:**
1. Implement per-user and per-API-key rate limits at the API gateway level
2. Monitor cumulative query patterns and trigger alerts on high query volumes
3. Implement CAPTCHA or proof-of-work challenges for high-volume access

**If surrogate fidelity is high:**
1. Reduce output precision further
2. Add prediction perturbation (differential privacy in output layer)
3. Implement per-request query logging with anomaly detection
4. Apply adaptive rate limiting based on query diversity

## References
- **MITRE ATLAS:**
  - `AML.T0024.002` — ML Model Inference API Access (extraction context)
  - `AML.T0005` — Create Proxy ML Model
- **MLASWE:** MLASWE-0003 (Model Extraction / Intellectual Property Theft)
- **NIST AI RMF:** MANAGE 2.4, MEASURE 2.6
- **Academic:** Tramèr et al. (2016) "Stealing Machine Learning Models via Prediction APIs"
