# MLASWE-0008: Model Denial of Service (DoS)

## Description
Model Denial of Service (DoS) attacks exploit the inherently resource-intensive nature of machine learning inference to exhaust system compute, memory, or financial resources. Attackers craft inputs that maximize algorithmic complexity (e.g., exploiting transformer attention mechanisms), consume massive context windows, or simply overwhelm the API with high-volume requests. This results in service degradation, total outage, or catastrophic financial impact (Economic DoS).

## Risk
- **Severity:** High (critical impact on availability and business continuity)
- **Exploitability:** Low barrier to entry (requires standard API access; easily automated)
- **Prevalence:** Widespread (most ML APIs are vulnerable without strict throttling)

## Affected Components
- ML inference endpoints and serving infrastructure.
- LLM conversational APIs (highly susceptible due to variable context lengths).
- Automated ML (AutoML) or pipeline orchestration services.
- Edge or embedded ML deployments with strict resource constraints.

## Sub-types
| Type | Description | Target Resource |
|------|-------------|-----------------|
| **Algorithmic Complexity** | Inputs specifically crafted to trigger worst-case computational paths (e.g., O(n²) operations). | CPU / GPU Compute |
| **Resource Exhaustion** | Voluminous inputs designed to exceed memory constraints or context windows. | VRAM / Memory |
| **Volume-based (Volumetric)** | A flood of concurrent requests overwhelming the serving cluster. | Network / Infrastructure |
| **Sponge Examples** | Adversarial inputs optimized to maximize energy consumption and latency. | Hardware / Energy |

## Detection Methods
- **Resource Telemetry:** Operations MUST monitor granular CPU, GPU, and VRAM utilization per inference request.
- **Latency Profiling:** Systems MUST establish baseline inference latency and alert on severe statistical outliers.
- **Token Analytics:** LLM gateways MUST track token generation rates and flag anomalous usage spikes per tenant.
- **Payload Inspection:** Security perimeters SHOULD inspect payload structures to prevent algorithmic complexity exploits.

## Preventive Controls (MLASVS)
- **MLASVS-LLM-005:** Context window limits
- **MLASVS-LLM-011:** Rate limiting on LLM endpoints
- **MLASVS-LLM-012:** Token usage monitoring
- **MLASVS-LLM-013:** Input token limits
- **MLASVS-MODEL-012:** Resource limits on inference
- **MLASVS-INFRA-010:** Input size validation

## Attack Techniques (MITRE ATLAS)
- **AML.T0029:** Model Denial of Service

## Remediation
1. **Strict Rate Limiting:** API gateways MUST enforce rigorous, multi-tiered rate limiting (per IP, per user, per API key) on all inference endpoints.
2. **Hard Constraints:** Systems MUST enforce hard caps on input lengths, context windows, and maximum output token generation.
3. **Execution Timeouts:** Inference engines MUST implement strict processing timeouts to terminate hanging or overly complex queries.
4. **Dynamic Autoscaling:** Infrastructure SHOULD utilize horizontal pod autoscaling based on custom metrics (e.g., GPU utilization, queue depth) to absorb traffic spikes.
5. **Circuit Breakers:** Microservice architectures MUST implement circuit breaker patterns to prevent cascading failures across the enterprise.

## Real-World Examples
- **Sponge Attacks:** Researchers demonstrated that specifically crafted text inputs could increase LLM inference latency by up to 30x, effectively causing DoS.
- **Economic Exhaustion:** Attackers exploited public LLM chatbots to run massive automated data extraction routines, resulting in astronomical API billing for the victim organization.

## References
- Shumailov et al., "Sponge Examples: Energy-Latency Attacks on Neural Networks" (2021)
- OWASP LLM Top 10: LLM04
- MITRE ATLAS: AML.T0029
