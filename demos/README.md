# MLASTG Demos

## Overview
This directory contains example vulnerable ML models and applications for educational security testing. Each demo includes a security weakness, instructions for exploitation, and guidance for remediation.

## Planned Demos

| Demo | Weakness | Tool | Status |
|------|----------|------|--------|
| Backdoored image classifier | MLASWE-0007 | ART + PyTorch | Planned |
| RAG chatbot with injection | MLASWE-0006 | LangChain + Giskard | Planned |
| Overconfident credit model | MLASWE-0005 | sklearn + ART | Planned |
| Unprotected model API | MLASWE-0003 | Flask + ART | Planned |

## Contributing Demos
To contribute a demo:
1. Create a new directory under `demos/`
2. Include a README with setup, exploitation, and remediation
3. Include runnable code (Python scripts or Jupyter notebooks)
4. Ensure all dependencies are documented in `requirements.txt`
