## MLASTG-TEST-DATA-004: Data Access Control Review

### Control Reference
- MLASVS-DATA-003: Data Access Control Enforcement
- MLASVS-DATA-007: Secure Data Storage
- MLASVS-DATA-008: Data Encryption at Rest
- MLASVS-DATA-009: Data Encryption in Transit
- MLASVS-DATA-012: Data Retention Policy
- MLASVS-DATA-021: Federated Data Governance (L2)
- MLASVS-DATA-027: Data Usage Auditing (L2)
- MLASVS-DATA-028: Cross-Border Data Compliance (L2)

### Severity
**Medium** (L1) / **High** (L2)

### Overview
Data access control ensures that ML training data, validation data, and associated metadata are protected throughout their lifecycle. Weak access controls can enable unauthorized data access, training data exfiltration, and regulatory non-compliance. This test audits access control enforcement, encryption, retention, and auditing for all ML data stores.

### Prerequisites
| Requirement | Details |
|-------------|---------|
| Access | Data catalog, storage infrastructure documentation, IAM configuration |
| Tools | `openssl`, cloud provider security console, audit log viewer |
| Documentation | Data classification policy, retention policy, access control matrix |

### Step-by-Step Procedure

#### Step 1: Verify Access Control Enforcement
1. Review the access control matrix for all ML data stores (training data, feature stores, data lakes)
2. Verify that role-based access control (RBAC) is configured:
   - Data scientists: read access to training data; no write/delete
   - ML engineers: read/write access to processed data; no raw data deletion
   - Admins: full access; restricted to small group with MFA
3. Attempt access with unauthorized credentials
4. **Pass if:** All data stores enforce authentication and authorization; unauthorized access is rejected.
5. **Fail if:** Any data store allows unauthenticated access or assigned roles are overly permissive.

#### Step 2: Verify Data Encryption at Rest
1. Identify all storage locations for ML data (S3, GCS, Azure Blob, local disks)
2. Verify encryption configuration:
   ```bash
   # For AWS S3
   aws s3api get-bucket-encryption --bucket <bucket-name>
   
   # For local files
   lsblk -o NAME,FSTYPE,MOUNTPOINT  # Check for LUKS or encrypted volumes
   ```
3. **Pass if:** All ML data stores use AES-256 or equivalent encryption at rest.
4. **Fail if:** Any ML data store stores data unencrypted.

#### Step 3: Verify Data Encryption in Transit
1. Verify TLS is enforced for all data transfer channels:
   - Data ingestion pipelines
   - Feature store connections
   - Model training data feeds
2. **Pass if:** All data in transit uses TLS 1.2+ with strong cipher suites.
3. **Fail if:** Any data transfer channel allows unencrypted HTTP or uses outdated TLS versions.

#### Step 4: Verify Data Retention Policy
1. Review the data retention policy documentation
2. Verify that retention periods are defined for each data category
3. Check that automated disposal is configured for expired data
4. **Pass if:** Retention policy is documented, enforced, and data disposal is automated.
5. **Fail if:** Retention policy is missing, poorly defined, or data disposal requires manual intervention.

#### Step 5: Verify Audit Logging
1. Verify that all data access events are logged with:
   - User identity (anonymized or hashed)
   - Timestamp (UTC)
   - Action (read, write, delete)
   - Data resource accessed
2. Verify logs are shipped to centralized SIEM
3. **Pass if:** A complete and centralized audit trail exists for all data access events.
4. **Fail if:** Audit logging is incomplete, missing critical fields, or not centralized.

#### Step 6: Verify Federated Data Governance (L2)
1. If multiple data sources or organizations contribute data, verify governance controls
2. Verify that data use agreements are documented and enforced
3. **Pass if:** The federated governance framework is clearly documented and enforced across contributors.
4. **Fail if:** Data is contributed without formalized governance or data use agreements.

#### Step 7: Verify Cross-Border Data Compliance (L2)
1. Identify all data sources and their geographic locations
2. Verify compliance with applicable regulations (GDPR, CCPA, etc.)
3. Verify that data transfer mechanisms (SCCs, BCRs) are documented
4. **Pass if:** Cross-border data handling is fully documented and legally compliant.
5. **Fail if:** Data crosses borders without appropriate transfer mechanisms or regulatory compliance.

### Expected Result
| Level | Expected Outcome |
|-------|-----------------|
| L1 | RBAC enforced on all data stores; encryption at rest and in transit; retention policy documented; audit logging active |
| L2 | All L1 controls met; federated governance documented; cross-border compliance verified |

### Evidence Requirements
- [ ] Data access control matrix documentation
- [ ] Encryption configuration evidence (at rest and in transit)
- [ ] Data retention policy document
- [ ] Audit log sample showing required fields
- [ ] (L2) Federated governance framework documentation
- [ ] (L2) Cross-border compliance documentation

### Remediation Guidance
**If access controls are insufficient:**
1. Implement RBAC with least-privilege for all data stores
2. Enable MFA for administrative access
3. Review and restrict overly permissive roles

**If encryption is missing:**
1. Enable encryption at rest on all storage (S3 SSE-KMS, GCS CMEK, Azure SSE)
2. Enforce TLS 1.2+ on all data transfer channels
3. Rotate encryption keys on a defined schedule

**If audit logging is incomplete:**
1. Add structured logging middleware to data access layers
2. Ship logs to centralized SIEM
3. Define log retention per policy

### References
- **MITRE ATLAS:**
  - AML.TA0002: Initial Access
  - AML.TA0010: Collection
- **MLASWE:** MLASWE-0012 (Training Data Leakage)
- **NIST AI RMF:** MAP 1.5 (Risk identification), GOVERN 1.2 (Policies)
- **Related Standard:** ISO/IEC 27001 (Information Security Management)
