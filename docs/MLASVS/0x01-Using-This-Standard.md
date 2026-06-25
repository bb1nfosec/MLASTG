# Using the MLASVS

## How to Select the Right Security Level

### L1 — Standard Security
**Mandatory for:** All ML systems exposed to external users, processing sensitive data, or integrated into business-critical workflows.

**Suitable for:**
- Customer-facing ML applications
- Internal ML tools processing business data
- ML models consuming external input
- Any system where compromise would cause measurable business impact

### L2 — Defense-in-Depth
**Mandatory for:** Systems where compromise would cause severe harm to individuals, organizations, or national security.

**Suitable for:**
- Defense and intelligence applications
- Healthcare ML systems (diagnosis, treatment planning)
- Financial services (fraud detection, credit scoring, trading)
- Critical infrastructure (energy, transportation, water)
- Systems processing sensitive personal data (biometric, genetic)
- Autonomous systems (vehicles, drones, industrial control)

## How to Apply the Controls

1. **Scope the assessment** — Identify all ML components in your system
2. **Select the level** — Use L1 as minimum baseline, L2 where indicated
3. **Review all 7 categories** — Each category addresses a distinct attack surface
4. **Trace controls** — Each control maps to test cases in MLASTG
5. **Document evidence** — Record test results for each applicable control
6. **Track weaknesses** — Use MLASWE identifiers for findings

## Control Notation

| Notation | Meaning |
|----------|---------|
| ✅ Tested and passed | Control has been verified and meets requirements |
| ❌ Tested and failed | Control has been verified but does not meet requirements |
| ⚠️ Partially tested | Control partially implemented or partially verified |
| 🔲 Not tested | Control has not been verified |
| N/A | Control is not applicable to this system |

## Partial Compliance

For L2 systems, L1 controls are mandatory. Organizations may:
- Implement all L2 controls for complete compliance
- Implement L1 controls with documented risk acceptance for L2 gaps
- Use phased approach with remediation timelines

## Customizing the Standard

Organizations may extend the MLASVS with:
- Industry-specific controls (e.g., HIPAA for healthcare, PCI DSS for payments)
- Organization-specific controls derived from internal threat models
- Stricter thresholds for adversarial robustness metrics
- Additional data privacy controls for jurisdictional requirements

## Mapping to Existing Frameworks

If your organization already uses:
- **NIST AI RMF** → Use MLASVS controls as technical verification for RMF categories
- **OWASP AI Exchange** → MLASVS provides the testable verification layer
- **ISO/IEC 42001** → MLASVS-DATA and MLASVS-GOV support AI management system controls
- **EU AI Act** → MLASVS controls support conformity assessment requirements
