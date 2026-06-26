# MLASTG Testing Tools Reference

## Overview
This document catalogs the tools used in ML security testing, organized by testing domain. Each entry includes verified installation instructions, basic usage, and relevant MLASTG test references.

> **Note:** All `pip install` commands should be run inside a dedicated virtual environment (`python -m venv mlsec-env`). Tool availability on PyPI changes over time; verify the package name before installing.

## 1. Adversarial Robustness Testing

### IBM Adversarial Robustness Toolbox (ART)
**Purpose:** Comprehensive library for adversarial attacks and defenses
**URL:** https://github.com/Trusted-AI/adversarial-robustness-toolbox

```bash
pip install adversarial-robustness-toolbox
```

**Key Modules:**
- `art.attacks.evasion`: FGSM, PGD, DeepFool, Carlini-Wagner, Boundary Attack, HopSkipJump
- `art.attacks.poisoning`: Poisoning attacks for classification
- `art.attacks.extraction`: KnockoffNets, CopycatCNN
- `art.attacks.inference`: MembershipInference, ModelInversion
- `art.defences`: Adversarial training, feature squeezing, etc.
- `art.estimators`: Wrappers for TensorFlow, PyTorch, Keras, scikit-learn, XGBoost

**Relevant Tests:** TEST-MODEL-001, TEST-MODEL-002, TEST-MODEL-003, TEST-MODEL-004

```python
# Quick Start
from art.estimators.classification import PyTorchClassifier
from art.attacks.evasion import FastGradientMethod
import torch

# Wrap your model
classifier = PyTorchClassifier(
    model=model,
    loss=criterion,
    input_shape=(3, 32, 32),
    nb_classes=10,
    clip_values=(0.0, 1.0)
)

# Generate adversarial examples
attack = FastGradientMethod(estimator=classifier, eps=0.3)
x_test_adv = attack.generate(x=x_test)

# Evaluate
accuracy = classifier._model.evaluate(x_test_adv, y_test)[1]
```

---

### SecML
**Purpose:** ML security evaluation library with attack generation and defense assessment
**URL:** https://github.com/pralab/secml

```bash
pip install secml
```

**Key Features:**
- Adversarial attack generation (evasion, poisoning)
- Security evaluation metrics
- Model explanation and verification

---

### CleverHans (Research)
**Purpose:** Benchmarking adversarial example robustness (research-focused)
**URL:** https://github.com/cleverhans-lab/cleverhans

```bash
pip install cleverhans
```

---

## 2. LLM Security Testing

### Giskard
**Purpose:** Automated security testing for LLMs and Generative AI (GenAI) applications
**URL:** https://github.com/Giskard-AI/giskard

```bash
pip install giskard
```

**Testing Capabilities:**
- Prompt injection detection
- Jailbreak susceptibility
- Sensitive information disclosure
- Output hallucination
- Toxicity and bias

**Relevant Tests:** TEST-LLM-001, TEST-LLM-002, TEST-LLM-003

```python
# Quick Start
import giskard as gsk

# Wrap your model
def model_fn(df):
    return [llm.invoke(row["question"]) for row in df.to_dict("records")]

model = gsk.Model(model_fn, model_type="text_generation")
dataset = gsk.Dataset(pd.DataFrame({"question": ["What is..."]}))

# Run security scan
scan_results = gsk.scan(model, dataset)
scan_results.to_dataframe()
```

---

### Rebuff
**Purpose:** Prompt injection detection and mitigation
**URL:** https://github.com/protectai/rebuff

```bash
pip install rebuff
```

**Features:**
- Heuristic detection of injection patterns
- LLM-based injection classification
- Embedding similarity analysis
- Canary word detection

---

### PromptInject
**Purpose:** Framework for testing prompt injection attacks
**URL:** https://github.com/agencyenterprise/PromptInject

```bash
pip install promptinject
```

---

### TextAttack
**Purpose:** NLP adversarial attack library
**URL:** https://github.com/QData/TextAttack

```bash
pip install textattack
```

**Relevant for:** Adversarial testing of NLP models and LLM-based classifiers

---

### Guardrails AI
**Purpose:** Output validation and guardrailing framework for LLMs
**URL:** https://github.com/guardrails-ai/guardrails

```bash
pip install guardrails-ai
```

**Key Features:**
- Structured output validation with schema enforcement
- Sensitive data detection and redaction in LLM outputs
- Custom validators for domain-specific rules
- Rail spec language for declarative validation pipelines

**Relevant Tests:** TEST-LLM-002, TEST-LLM-003

---

### NVIDIA NeMo Guardrails
**Purpose:** Programmable guardrails for LLM-based conversational AI
**URL:** https://github.com/NVIDIA-NeMo/Guardrails

```bash
pip install nemoguardrails
```

**Key Features:**
- Topical, safety, and security guardrail configuration
- Dialog flow control to prevent out-of-scope conversations
- Integration with LangChain and custom LLM backends

**Relevant Tests:** TEST-LLM-001, TEST-LLM-003

---

## 3. Data Security & Privacy

### Diffprivlib (IBM)
**Purpose:** Differential privacy library
**URL:** https://github.com/IBM/differential-privacy-library

```bash
pip install diffprivlib
```

**Relevant Tests:** TEST-DATA-003

---

### OpenMined / PySyft
**Purpose:** Privacy-preserving ML (differential privacy, federated learning)
**URL:** https://github.com/OpenMined/PySyft

```bash
pip install syft
```

---

### Scikit-learn (Data Validation)
**Purpose:** Integrated data validation and anomaly detection
```bash
pip install scikit-learn
```

**Relevant Tests:** TEST-DATA-002

---

## 4. Model Extraction & Privacy

### PrivacyRaven (Trail of Bits)
**Purpose:** Privacy auditing for ML models
**URL:** https://github.com/trailofbits/PrivacyRaven

```bash
pip install privacyraven
```

**Capabilities:**
- Membership inference attacks
- Model extraction attacks
- Model inversion attacks

**Relevant Tests:** TEST-MODEL-002, TEST-MODEL-003

---

### MLPrivacyMetrics
**Purpose:** Measurement of privacy risks in ML models
```bash
pip install privacy-metrics
```

---

## 5. ML Supply Chain & SBOM

### ML-SBOM Tools
**Purpose:** Generation and verification of ML Software Bill of Materials

```bash
# CycloneDX ML-SBOM generation
pip install cyclonedx-bom

# Trivy for vulnerability scanning — Linux (Debian/Ubuntu)
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee /etc/apt/sources.list.d/trivy.list
sudo apt-get update && sudo apt-get install trivy

# Trivy — macOS
brew install trivy

# Trivy — Docker
docker pull aquasec/trivy
```

**Relevant Tests:** TEST-SUPPLY-001, TEST-SUPPLY-002

---

### ModelScan (Protect AI)
**Purpose:** Scanning ML model files for unsafe code
**URL:** https://github.com/protectai/modelscan

```bash
pip install modelscan
```

```python
from modelscan import ModelScan

scanner = ModelScan()
results = scanner.scan("path/to/model.pkl")  # scans for pickle deserialization vulnerabilities
```

---

## 6. Infrastructure & Pipeline

### MLflow Security
**Purpose:** Model registry and experiment tracking security
```bash
pip install mlflow
```

**Key Security Configurations:**
- Authentication enabled
- Artifact store access controls
- Model versioning with signatures
- Experiment permissions

---

### Kubernetes Security
**Purpose:** K8s security for model serving infrastructure
```bash
# kubectl + kube-bench for security scanning
kube-bench run --targets master,node
```

---

## 7. Governance & Bias Testing

### AIF360 (IBM)
**Purpose:** Bias detection and fairness metrics
**URL:** https://github.com/Trusted-AI/AIF360

```bash
pip install aif360
```

**Key Metrics:**
- Disparate Impact Ratio
- Statistical Parity Difference
- Equal Opportunity Difference
- Average Odds Difference

---

### What-If Tool (Google)
**Purpose:** Model exploration and fairness analysis
**URL:** https://github.com/pair-code/what-if-tool

```bash
pip install what-if-tool
```

---

## 8. General ML Security Utilities

### Counterfit (Microsoft) — Archived
**Purpose:** Automation layer for ML security testing
**URL:** https://github.com/Azure/counterfit

> **⚠️ Archived:** This repository has been archived by Microsoft and is no longer maintained. Listed here for reference only. For active ML security testing, prefer [IBM ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox) or the tools listed in the selection guide below.

### Adversarial ML Threat Matrix (MITRE)
**Purpose:** Threat matrix aligned with MITRE ATLAS
**URL:** https://github.com/mitre/advmlthreatmatrix

## Tool Selection Guide

| Testing Need | Recommended Tool | Alternatives |
|-------------|-----------------|--------------|
| Evasion (CV models) | ART | CleverHans, SecML |
| Evasion (NLP models) | TextAttack | ART (text), PromptInject |
| Prompt injection | Giskard | Rebuff, PromptInject |
| LLM output guardrailing | Guardrails AI | NeMo Guardrails, LlamaGuard |
| Jailbreak detection | Giskard | NeMo Guardrails, custom classifiers |
| Model extraction | ART (KnockoffNets) | PrivacyRaven |
| Membership inference | ART | PrivacyRaven |
| Data poisoning detection | ART (poisoning module) | Custom detection scripts |
| Differential privacy | diffprivlib | PySyft (Opacus), TF Privacy |
| Bias & fairness | AIF360 | What-If Tool, Fairlearn |
| ML-SBOM | CycloneDX + ModelScan | Trivy (model scanning) |
| Model security scanning | ModelScan | Guarddog |
| Pipeline secret scanning | TruffleHog | gitleaks, detect-secrets |
