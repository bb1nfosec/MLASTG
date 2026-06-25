# MLASTG Companion Test Scripts

## Overview
This directory contains executable Python test scripts that implement the MLASTG test cases as automated test harnesses. Each script corresponds to one or more MLASTG-TEST-XXXX test cases.

## Setup

```bash
# Install base requirements
pip install adversarial-robustness-toolbox secml scikit-learn torch torchvision

# For LLM testing
pip install giskard rebuff

# For data privacy testing
pip install diffprivlib aif360

# Install test harness
pip install -r requirements.txt
```

## Script Organization

| Directory | Coverage | MLASTG Test Refs |
|-----------|----------|------------------|
| `data/` | Data provenance, sanitization, differential privacy | TEST-DATA-001 to 004 |
| `model/` | Adversarial robustness, extraction, membership inference | TEST-MODEL-001 to 004 |
| `llm/` | Prompt injection, output handling, jailbreak testing | TEST-LLM-001 to 003 |
| `supply/` | ML-SBOM audit, model provenance verification | TEST-SUPPLY-001 to 002 |
| `pipeline/` | CI/CD security scanning | TEST-PIPELINE-001 |
| `infra/` | Model serving, API security review | TEST-INFRA-001 to 002 |
| `gov/` | Governance assessment automation | TEST-GOV-001 |

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific category
python -m pytest tests/model/

# Run specific test with verbosity
python tests/model/test_adversarial_robustness.py -v

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
