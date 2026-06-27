# MLASWE-0003: Model Extraction

## Description
Model extraction attacks, also known as model stealing, involve an adversary systematically querying a deployed machine learning model to extract its internal parameters, decision boundaries, or logic. By utilizing the resultant input-output pairs, the attacker trains a surrogate model that closely approximates the target's behavior. A successful extraction compromises intellectual property (IP), negates competitive advantage, and facilitates offline reconnaissance for subsequent attacks (e.g., adversarial evasion or membership inference).

## Risk
- **Severity:** High
- **Exploitability:** Medium (Requires sustained API access, sufficient query budget, and evasion of rate limits)
- **Prevalence:** Common (Public-facing inference APIs providing high-fidelity outputs are highly susceptible)

## Affected Components
- ML model inference APIs and public-facing endpoints
- Machine Learning as a Service (MLaaS) platforms (e.g., Cloud Vision APIs, NLP services)
- Proprietary algorithms deployed in zero-trust or hostile environments
- Models returning high-dimensional or high-precision confidence scores (which maximize information leakage)

## Sub-types
| Type | Description | Query Efficiency |
|------|-------------|-----------------|
| **Equation-Solving Extraction** | Analytically solving model parameters using exact input-output algebraic relations. | Low queries, exact replication |
| **Surrogate Model Extraction** | Training a secondary model to mimic the target API's input-output distribution. | High queries, approximate replication |
| **Confidence-Based Extraction** | Exploiting high-precision floating-point prediction vectors for accelerated convergence. | Medium queries |
| **Label-Only Extraction** | Approximating the model using only discrete, hard-label predictions. | Very high queries |

## Detection Methods
- **Query Pattern Analysis:** Implement telemetry to detect systematic, grid-like, or high-volume query distributions originating from single or distributed IP blocks.
- **Input Diversity Auditing:** Monitor the latent space coverage of API requests to identify actors attempting to map the entire decision boundary.
- **Shadow Model Comparison:** Continuously compare API behavior against known surrogate architectures to detect imitation.

## Preventive Controls (MLASVS)
- **MLASVS-MODEL-004:** Output confidence calibration
- **MLASVS-MODEL-005:** API rate limiting
- **MLASVS-MODEL-018:** Extraction resistance validation (L2)
- **MLASVS-MODEL-023:** Model watermarking (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.T0034:** Model Extraction (Primary)

## Remediation
1. **Output Precision Truncation:** APIs MUST truncate or obfuscate confidence scores (e.g., rounding to two decimal places, returning top-k labels instead of full vectors) to minimize gradient leakage.
2. **Adaptive Rate Limiting and Circuit Breakers:** Systems MUST enforce stringent, context-aware rate limiting (e.g., token bucket algorithms) per user and per API key, deploying circuit breakers to halt suspected extraction campaigns.
3. **Cryptographic Watermarking:** Models SHOULD embed robust cryptographic watermarks or unique fingerprint triggers in their outputs to ensure non-repudiation and enable forensic tracing of stolen surrogate models.
4. **Behavioral Query Monitoring:** The API gateway MUST implement behavioral analytics to detect and block extraction heuristics, such as out-of-distribution (OOD) query bursts or adaptive grid searches.
5. **Strong Authentication and Access Control:** Inference endpoints MUST require strong, mutual authentication (mTLS) or robust API key management to enforce identity-based access controls and audit logging.

## Real-World Examples
- **Cloud API Extraction:** Researchers successfully extracted a functional, high-fidelity surrogate of a commercial cloud vision API using a bounded query budget.
- **LLM Model Stealing:** Model extraction attacks against large language models (e.g., GPT-2/3) to instantiate localized, offline approximations for unregulated use.
- **Proprietary Fraud Detection:** Adversaries querying ad-fraud models to extract decision boundaries, subsequently bypassing fraud detection filters.

## References
- Tramèr et al., "Stealing Machine Learning Models via Prediction APIs" (USENIX Security 2016)
- Orekondy et al., "Knockoff Nets: Stealing Functionality of Black-Box Models" (CVPR 2019)
- MITRE ATLAS: AML.T0034
