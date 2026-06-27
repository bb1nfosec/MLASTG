import importlib
import logging
import sys
import os
from typing import List, Dict, Any

# Ensure we can import the local tests/ directory
sys.path.insert(0, os.getcwd())
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

# Map categories to the modules they should execute
CATEGORY_MAP = {
    'model': [
        'tests.model.test_adversarial_robustness',
        'tests.model.test_extraction',
        'tests.model.test_backdoor'
    ],
    'llm': [
        'tests.llm.test_prompt_injection'
    ],
    'data': [
        'tests.data.test_data_sanitization'
    ],
    'supply': [
        'tests.supply.test_mlsbom'
    ],
    'infra': [
        'tests.infra.test_api_security',
        'tests.infra.test_tee_security'
    ],
    'pipeline': [
        'tests.pipeline.test_pipeline_security'
    ],
    'gov': [
        'tests.gov.test_governance'
    ]
}

def run_test_suite(target: str, category: str, demo: bool = False) -> List[Dict[str, Any]]:
    """
    Orchestrates the execution of MLASTG test scripts dynamically.
    """
    results = []
    
    categories_to_run = [category] if category != 'all' else list(CATEGORY_MAP.keys())
    
    for cat in categories_to_run:
        modules = CATEGORY_MAP.get(cat, [])
        for module_name in modules:
            try:
                mod = importlib.import_module(module_name)
                if hasattr(mod, 'run_test'):
                    # Execute the test module
                    test_results = mod.run_test(target, demo=demo)
                    if isinstance(test_results, list):
                        results.extend(test_results)
                    else:
                        results.append(test_results)
                else:
                    logger.warning(f"Module {module_name} missing run_test() function.")
            except Exception as e:
                logger.error(f"Failed to load or execute {module_name}: {e}")
                results.append({
                    "test_id": "UNKNOWN",
                    "control": "UNKNOWN",
                    "name": f"Module: {module_name}",
                    "status": "error",
                    "severity": "UNKNOWN",
                    "evidence": [f"Execution/Import error: {str(e)}"]
                })
                
    return results
