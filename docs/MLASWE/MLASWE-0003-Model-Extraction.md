# MLASWE-0003: Model Extraction

## Description
Model extraction attacks aim to steal a deployed ML model by systematically querying it and using the input-output pairs to train a surrogate model that approximates the target's behavior. Successful extraction can compromise competitive advantage, enable offline analysis for further attacks (e.g., evasion), and violate model IP protections.

## Risk
- **Severity:** High
- **Exploitability:** Medium (requires API access and query budget)
- **Prevalence:** Common (most public API models are extractable to some degree)

## Affected Components
- ML model inference APIs
- SaaS ML platforms (e.g., cloud vision APIs, NLP-as-a-service)
- Proprietary models deployed behind APIs
- Models with high-dimensional outputs (more information leakage)

## Sub-types
| Type | Description | Query Efficiency |
|------|-------------|-----------------|
| **Equation-solving extraction** | Solve model parameters using input-output equations | Low queries, exact |
| **Surrogate model extraction** | Train a local model to mimic API behavior | High queries, approximate |
| **Confidence-based extraction** | Exploit full prediction vectors for faster convergence | Medium |
| **Label-only extraction** | Learn from hard label predictions only | Very high queries |

## Detection Methods
- **Query Pattern Analysis:** Monitor for systematic, high-volume queries from single sources
- **Input Diversity Analysis:** Detect coverage of large portions of input space
- **Model Watermarking:** Embed hidden triggers in model outputs for forensic tracing
- **API Rate Monitoring:** Track per-user query volumes and velocities
- **Shadow Model Comparison:** Compare API behavior against known surrogate models

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-004:** Output confidence calibration (limit precision of output vectors)
- **MLASVS-MODEL-005:** API rate limiting
- **MLASVS-MODEL-018:** Extraction resistance validation (L2)
- **MLASVS-MODEL-023:** Model watermarking (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0034:** Model Extraction (primary)

## Remediation
1. **Output Perturbation:** Add noise to API outputs, reduce prediction vector precision
2. **Rate Limiting:** Enforce per-user/API-key query quotas
3. **Access Control:** Require authentication for all inference endpoints
4. **Watermarking:** Embed unique fingerprints in model outputs
5. **Query Monitoring:** Detect and block extraction patterns (e.g., grid search)
6. **Model Obfuscation:** Limit output dimensions when possible

## Real-World Examples
- **Amazon AWS Rekognition extraction:** Researchers extracted a functional copy of AWS Rekognition via API queries
- **GPT model stealing:** Model extraction attacks on GPT-2/3 to create local approximations
- **Stealing production ad models:** Fraudsters extract ad-serving ML models to create adversarial content

## References
- Tramèr et al., "Stealing Machine Learning Models via Prediction APIs" (USENIX Security 2016)
- Orekondy et al., "Knockoff Nets: Stealing Functionality of Black-Box Models" (CVPR 2019)
- MITRE ATLAS: AML.T0034
