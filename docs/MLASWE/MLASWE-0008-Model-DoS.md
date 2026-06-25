# MLASWE-0008: Model Denial of Service (DoS)

## Description
Model DoS attacks aim to exhaust the computational resources of an ML system through resource-intensive inputs, excessive query volume, or exploitation of algorithmic complexity. These attacks can render the model unavailable for legitimate users, cause financial damage (especially for pay-per-query APIs), or trigger cascading failures in dependent systems.

## Risk
- **Severity:** High (availability impact, potential financial losses)
- **Exploitability:** Easy (requires only API access, no specialized knowledge)
- **Prevalence:** Common (standard DoS techniques apply to ML endpoints)

## Affected Components
- ML model inference endpoints
- LLM chatbot and API services (high compute per query)
- AutoML and NAS (Neural Architecture Search) services
- Embedded ML systems (resource-constrained)

## Sub-types
| Type | Description | Target |
|------|-------------|--------|
| **Resource exhaustion** | Extremely long or complex inputs | LLM context window, compute |
| **Algorithmic complexity** | Inputs that trigger O(n²) or worse operations | Transformers (attention) |
| **Volume-based** | High request rate overwhelms serving infrastructure | API endpoints |
| **Adversarial trigger** | Specific inputs that crash or hang the model | Model edge cases |

## Detection Methods
- **Resource Monitoring:** Track CPU/GPU/memory usage per request
- **Input Complexity Analysis:** Detect abnormally long or complex inputs
- **Latency Monitoring:** Identify outlier request processing times
- **Rate Anomaly Detection:** Sudden volume spikes from specific sources

## Preventive Controls (MLASVS)
- **MLASVS-LLM-005:** Context window limits
- **MLASVS-LLM-011:** Rate limiting on LLM endpoints
- **MLASVS-LLM-012:** Token usage monitoring
- **MLASVS-LLM-013:** Input token limits
- **MLASVS-MODEL-012:** Resource limits on inference
- **MLASVS-INFRA-010:** Input size validation

## Attack Techniques (MITRE ATLAS)
- **AML.T0037:** Model Denial of Service (primary)

## Remediation
1. **Rate Limiting:** Enforce per-user/API-key query quotas
2. **Input Size Limits:** Reject excessively large or complex inputs
3. **Request Queuing:** Implement fair scheduling for inference requests
4. **Autoscaling:** Configure horizontal pod autoscaling for serving infrastructure
5. **Timeout Policies:** Set request timeouts to prevent long-running queries

## References
- MITRE ATLAS: AML.T0037
- OWASP LLM Top 10: LLM04 (Model Denial of Service)
