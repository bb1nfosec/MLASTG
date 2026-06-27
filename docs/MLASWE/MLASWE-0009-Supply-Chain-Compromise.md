# MLASWE-0009: Supply Chain Compromise

## Description
Supply chain compromise in machine learning occurs when an adversary infiltrates an organization's ML pipeline via compromised third-party dependencies, including pre-trained models, datasets, ML frameworks, or infrastructure. Because ML models are opaque binary blobs (e.g., Pickle files, PyTorch weights) and datasets are massive, they serve as ideal vectors for embedding malicious code or backdoors. This represents a critical systemic risk to enterprise ML integrity.

## Risk
- **Severity:** Critical (can lead to RCE, data theft, or systemic model backdoors)
- **Exploitability:** Medium (requires compromise of a popular upstream repository or typosquatting)
- **Prevalence:** Rapidly increasing alongside the reliance on public model hubs (e.g., Hugging Face, GitHub).

## Affected Components
- Public model repositories and pre-trained foundation models.
- Third-party open-source datasets and web-scraped corpora.
- Core ML frameworks (PyTorch, TensorFlow) and Python dependencies.
- Cloud-based training environments and MLOps orchestration pipelines.

## Detection Methods
- **Cryptographic Provenance:** Systems MUST verify digital signatures and cryptographic hashes of all incoming models and datasets.
- **Static Artifact Analysis:** Security tools MUST scan model artifacts for unsafe serialization formats (e.g., identifying arbitrary code execution in Pickle files).
- **Software Composition Analysis (SCA):** Pipelines MUST scan all Python dependencies and ML frameworks for known CVEs.
- **Behavioral Sandboxing:** Models SHOULD be instantiated and tested within strict, network-isolated sandboxes to detect anomalous system calls.

## Preventive Controls (MLASVS)
- **MLASVS-SUPPLY-001 through 022:** Full supply chain controls
- **MLASVS-DATA-001:** Data provenance documentation
- **MLASVS-DATA-002:** Data integrity verification
- **MLASVS-MODEL-021:** Backdoor detection validation (L2)

## Attack Techniques (MITRE ATLAS)
- **AML.TA0003:** Resource Development (Supply Chain)
- **AML.T0010:** ML Supply Chain Compromise

## Remediation
1. **Machine Learning SBOM (ML-SBOM):** Organizations MUST maintain an exhaustive Machine Learning Bill of Materials detailing the provenance of all data, weights, and software dependencies.
2. **Safe Serialization:** Teams MUST strictly prohibit the use of insecure serialization formats (e.g., Python `pickle`). Models MUST be saved in secure formats (e.g., `safetensors`, ONNX).
3. **Artifact Scanning:** CI/CD pipelines MUST integrate specialized scanners (e.g., ModelScan, ProtectAI) to evaluate model weights for embedded malicious payloads prior to deployment.
4. **Network Isolation:** Training and inference environments MUST operate in strictly isolated networks with no egress internet access to prevent payload staging or data exfiltration.
5. **Private Registries:** Enterprises SHOULD utilize internal, curated, and hardened registries for approved ML models and datasets, prohibiting direct developer downloads from public hubs.

## Real-World Examples
- **Hugging Face Malicious Models:** Security analysts routinely discover models on public hubs utilizing PyTorch's `pickle` format to execute reverse shells upon instantiation.
- **PyPI Typosquatting:** Attackers deployed malicious Python packages mimicking popular ML libraries, resulting in credential theft from developer environments.
- **Poisoned Datasets:** Adversaries have compromised public academic datasets by altering labels, subsequently poisoning downstream corporate models.

## References
- OWASP LLM Top 10: LLM05 (Supply Chain Vulnerabilities)
- MITRE ATLAS: AML.T0010
- Bagdasaryan et al., "How To Backdoor Federated Learning" (2020)
