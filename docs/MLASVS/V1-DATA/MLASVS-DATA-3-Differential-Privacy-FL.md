# MLASVS-DATA-3: Differential Privacy (Extended — Federated & Distributed)

## Additional Controls for Federated Learning

This document extends the base MLASVS-DATA-3 controls with federated learning-specific differential privacy requirements referenced by TEST-DATA-005.

---

### DATA-019: Differential Privacy for Distributed Training (L2)
**Description:** In federated or distributed training settings, differential privacy (DP) must be applied to model updates before sharing. The privacy budget (epsilon, delta) must be tracked across all training rounds and participants.

**MITRE ATLAS:** AML.T0020 (Poison Training Data)
**Test Reference:** MLASTG-TEST-DATA-005

**Verification:**
1. Verify that DP-SGD or DP-FedAvg is applied to local model updates before sharing
2. Confirm that gradient clipping is enforced (max norm bound documented)
3. Verify that calibrated Gaussian noise is added to clipped gradients
4. Check that the privacy budget (epsilon, delta) is tracked across rounds and participants
5. Verify that the total privacy budget does not exceed organizational limits

**Acceptance Criteria:**
- Total epsilon ≤ 10 for training with meaningful privacy guarantees
- Delta < 1/n² where n is the number of training samples
- Privacy budget is enforced and training stops when budget is exhausted

**Remediation:**
1. Implement DP-SGD (Abadi et al., 2016) with per-sample gradient clipping
2. Use privacy accounting (Rényi DP or moment accounting) to track cumulative epsilon
3. Add budget enforcement to the training loop

---

### DATA-023: Secure Aggregation Verification (L2)
**Description:** In federated learning, the aggregation protocol must prevent the central server from inspecting individual participant model updates. Use homomorphic encryption, secure multi-party computation (SMPC), or trusted execution environments (TEEs).

**MITRE ATLAS:** AML.T0013 (Extract ML Model)
**Test Reference:** MLASTG-TEST-DATA-005

**Verification:**
1. Identify the aggregation protocol (FedAvg, Secure Aggregation, etc.)
2. Verify that individual updates cannot be reconstructed from the aggregated result
3. If using homomorphic encryption, verify the encryption scheme (CKKS, BFV)
4. If using SMPC, verify the number of parties and threshold
5. If using TEEs, verify attestation and isolation

**Acceptance Criteria:**
- Individual participant gradients cannot be reconstructed by the server
- Aggregation protocol is documented and reviewed by a security team
- TEE attestation (if applicable) passes remote verification

**Remediation:**
1. Implement Google's Secure Aggregation protocol for federated learning
2. Use PySyft's SMPC-based aggregation
3. Deploy aggregation in a TEE (Intel SGX, AWS Nitro Enclaves)

---

## Cross-References

- **MITRE ATLAS:** AML.T0020, AML.T0013
- **Academic:** Abadi et al., "Deep Learning with Differential Privacy" (2016)
- **Academic:** Bonawitz et al., "Practical Secure Aggregation for Privacy-Preserving Machine Learning" (2017)
- **Framework:** PySyft, TensorFlow Privacy, Opacus
