# MLASVS-DATA-4: Data Access Control Controls

> **Subcategory:** V1: Data Security & Privacy
> **Controls:** DATA-003, DATA-007, DATA-008, DATA-009, DATA-012, DATA-021, DATA-027, DATA-028

## Overview

Data access control ensures that ML data is properly protected throughout its lifecycle — from storage and transit to usage and disposal. This subcategory covers access enforcement, encryption, retention policies, and compliance requirements.

## Controls

| ID | Control | Level | MITRE ATLAS | Test Reference | Description |
|----|---------|-------|-------------|----------------|-------------|
| DATA-003 | Data access control enforcement | L1 | AML.TA0002 | TEST-DATA-004 | Enforce role-based access control on all ML data stores |
| DATA-007 | Secure data storage | L1 | AML.TA0002 | TEST-DATA-004 | Store ML data in secure, access-controlled environments |
| DATA-008 | Data encryption at rest | L1 | AML.TA0010 | TEST-DATA-004 | Encrypt all ML data at rest using AES-256 or equivalent |
| DATA-009 | Data encryption in transit | L1 | AML.TA0010 | TEST-DATA-004 | Encrypt all ML data in transit using TLS 1.2+ |
| DATA-012 | Data retention policy | L1 | AML.TA0010 | TEST-DATA-004 | Define and enforce data retention and disposal schedules |
| DATA-021 | Federated data governance | L2 | AML.TA0002 | TEST-DATA-004 | Enable cross-organization data governance for federated ML |
| DATA-027 | Data usage auditing | L2 | AML.TA0009 | TEST-DATA-004 | Audit all data access and usage for compliance |
| DATA-028 | Cross-border data compliance | L2 | AML.TA0010 | TEST-DATA-004 | Ensure data handling complies with cross-border regulations |

## Implementation Guidance

### Access Control
- Implement RBAC with least-privilege principles for all data stores
- Require MFA for administrative access to training data
- Log all data access events with user identity, timestamp, and action

### Encryption
- Use AES-256 for data at rest
- Enforce TLS 1.2+ for all data in transit
- Rotate encryption keys on a defined schedule (minimum annually)

### Retention and Disposal
- Define retention periods based on regulatory requirements and business needs
- Implement automated data disposal for expired records
- Maintain disposal logs for audit purposes

## Related

- [MLASTG-TEST-DATA-001: Data Provenance Verification](../../MLASTG/DATA-Tests/MLASTG-TEST-DATA-001.md)
- [MLASWE-0012: Training Data Leakage](../../MLASWE/MLASWE-0012-Training-Data-Leakage.md)
- **MITRE ATLAS:** AML.TA0002 (Initial Access), AML.TA0010 (Collection)
