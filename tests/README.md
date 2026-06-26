# MLASTG Companion Test Scripts

## Overview
This directory contains executable Python test scripts that implement the MLASTG test cases as automated test harnesses. Each script corresponds to one or more MLASTG-TEST-XXXX test cases.

## Setup

```bash
# Install base requirements
pip install adversarial-robustness-toolbox scikit-learn torch torchvision requests

# For LLM testing
pip install giskard

# For data privacy testing
pip install diffprivlib aif360

# Install test harness
pip install -r requirements.txt
```

## Script Organization

| Directory | Coverage | MLASTG Test Refs | Script |
|-----------|----------|------------------|--------|
| `data/` | Data provenance, sanitization, differential privacy, federated learning poisoning | TEST-DATA-001 to 005 | `test_data_sanitization.py` |
| `model/` | Adversarial robustness, extraction, membership inference, backdoor, RL reward hacking | TEST-MODEL-001 to 006 | `test_adversarial_robustness.py`, `test_extraction.py`, `test_backdoor.py` |
| `llm/` | Prompt injection, output handling, jailbreak testing | TEST-LLM-001 to 004 | `test_prompt_injection.py` |
| `supply/` | ML-SBOM audit, model provenance verification | TEST-SUPPLY-001 to 002 | `test_mlsbom.py` |
| `pipeline/` | CI/CD security scanning, artifact integrity | TEST-PIPELINE-001 | `test_pipeline_security.py` |
| `infra/` | Model serving, API security, agentic workflow, confidential computing/TEE | TEST-INFRA-001 to 004 | `test_api_security.py`, `test_tee_security.py` |
| `gov/` | Governance assessment automation | TEST-GOV-001 | `test_governance.py` |

## Running Tests

```bash
# Run all demos
python tests/model/test_adversarial_robustness.py --demo
python tests/data/test_data_sanitization.py --demo
python tests/pipeline/test_pipeline_security.py --demo

# Run specific category with pytest
python -m pytest tests/model/ -v
python -m pytest tests/data/ -v

# Generate report
python tests/model/test_adversarial_robustness.py --report output.json
```

## Output Format

Each script outputs structured JSON with:
```json
{
  "test_id": "MLASTG-TEST-MODEL-001",
  "control": "MLASVS-MODEL-001",
  "timestamp": "2025-06-25T12:00:00Z",
  "results": {
    "status": "pass|fail|error",
    "metrics": {},
    "evidence": []
  }
}
```
