# ML-SBOM worked example

A complete, **validatable** Machine Learning Software Bill of Materials (ML-SBOM)
for an example model, `acme-fraud-detector` — a fraud classifier fine-tuned from
`distilbert-base-uncased` on two datasets. It demonstrates the supply-chain
controls **MLASVS-SUPPLY-001 … SUPPLY-008** and test **MLASTG-TEST-SUPPLY-001**.

## Files

| File | Format | Purpose |
|------|--------|---------|
| [`fraud-detector.mlsbom.json`](fraud-detector.mlsbom.json) | MLASTG-native | Validates directly against the MLASTG SBOM harness |
| [`fraud-detector.cyclonedx.json`](fraud-detector.cyclonedx.json) | CycloneDX 1.6 ML-BOM | Industry-standard form for SCA/GRC tooling |

Both describe the **same** system: the model, its base model, two training
datasets (each with source, hash, and license), framework dependencies (with
package URLs), the training environment, and signed build provenance.

## Validate it

```bash
# Passes — the example SBOM is complete
python tests/supply/test_mlsbom.py --sbom demos/ml-sbom/fraud-detector.mlsbom.json

# Fails (exit 1) — proves the check is real, not a rubber stamp
echo '{"model_name":"x"}' > /tmp/incomplete.json
python tests/supply/test_mlsbom.py --sbom /tmp/incomplete.json
```

The harness checks that every required field is present
(`model_name`, `model_version`, `base_model`, `training_dataset`,
`framework_dependencies`, `training_environment`) and that each dataset entry
carries `source`, `hash`, and `license`.

## What each part maps to

| SBOM content | MLASVS control |
|--------------|----------------|
| Model name, version, hash | SUPPLY-001 (ML-SBOM generation) |
| `base_model` source + hash + license | SUPPLY-002 (Base-model vetting) |
| `training_dataset[].provenance` | SUPPLY-003 (Training dataset provenance) |
| `framework_dependencies[].purl` | SUPPLY dependency-scanning controls |
| `provenance.signed` / attestation | SUPPLY-015 (Cryptographic model provenance) |

## CycloneDX mapping

The CycloneDX file expresses the model as a `machine-learning-model` component
with a `modelCard`, the datasets as `data` components, and the libraries as
`library` components, tied together by a `dependencies` graph — so the same
inventory is consumable by CycloneDX-aware supply-chain tooling.
