import time
from typing import List, Dict, Any

def run_test_suite(target: str, category: str, demo: bool = False) -> List[Dict[str, Any]]:
    """
    Orchestrates the execution of MLASTG test scripts.
    In demo mode, it returns simulated test results.
    """
    results = []
    
    categories_to_run = [category] if category != 'all' else ['data', 'model', 'llm', 'supply', 'infra', 'pipeline', 'gov']
    
    for cat in categories_to_run:
        # Simulate loading and running tests for the category
        time.sleep(1) # Fake delay for scanning
        
        if cat in ['model', 'all']:
            results.append({
                "test_id": "MLASTG-TEST-MODEL-001",
                "control": "MLASVS-MODEL-001",
                "name": "Adversarial Robustness Testing",
                "status": "pass" if demo else "error",
                "severity": "L1",
                "evidence": ["Evasion attack success rate < 10% on Fast Gradient Sign Method (FGSM)"]
            })
            results.append({
                "test_id": "MLASTG-TEST-MODEL-002",
                "control": "MLASVS-MODEL-004",
                "name": "Model Extraction Resistance",
                "status": "fail" if demo else "error",
                "severity": "L1",
                "evidence": ["API endpoint returned raw probabilities with 8 decimal precision, enabling high-fidelity surrogate training."]
            })
            
        if cat in ['llm', 'all']:
            results.append({
                "test_id": "MLASTG-TEST-LLM-001",
                "control": "MLASVS-LLM-001",
                "name": "Prompt Injection Testing",
                "status": "pass" if demo else "error",
                "severity": "L1",
                "evidence": ["LLM successfully deflected 24/25 generic DAN injection prompts.", "Guardrails active."]
            })

        if cat in ['supply', 'all']:
            results.append({
                "test_id": "MLASTG-TEST-SUPPLY-001",
                "control": "MLASVS-SUPPLY-001",
                "name": "ML-SBOM Audit",
                "status": "fail" if demo else "error",
                "severity": "L1",
                "evidence": ["No CycloneDX or SPDX ML-SBOM found in repository.", "Pickle file detected without ModelScan hash validation."]
            })
            
    return results
