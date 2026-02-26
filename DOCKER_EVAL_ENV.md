# Nexorian 3rd-Party Evaluation Environment (Dockerized)
## Version: 1.0.0-PROVEN

This environment is designed for independent auditors to reproduce the Nexorian Governance Proofs in a sterile, host-isolated container.

### 1. Requirements
- Docker Desktop or Linux Docker Engine
- Git
- RSA-4096 Public Key (for Genesis handshake verification)

### 2. Sandbox Initialization
To pull the official evaluation image and initiate a 3rd party audit:

```bash
# 1. Clone the verifiable source
git clone https://github.com/timeismoneyinc2019-crypto/Nexorian.git
cd Nexorian

# 2. Build the sterile audit container
docker build -t nexorian-audit:latest -f Dockerfile.audit .

# 3. Execute the Stress Load & Governance Check
docker run --rm nexorian-audit:latest
```

### 3. Verification Commands
Within the target environment, auditors can run the following to validate the published `audit_proof_final.jsonl`:

```bash
# Verify log chain integrity
python scripts/verify_chain.py --log audit_proof_final.jsonl --seed 80b2...edc6

# Verify Admissibility Gate (Role Violation Trap)
python scripts/test_gate.py --role OPERATOR --command RECURSIVE_DELETE
```

### 4. Notarized Finality
Successful execution of the above commands on any 3rd-party infrastructure confirms the **Deterministic Governance Rating of 1.0**.

---
*MANDATORY FOR CORPORATE & REGULATORY EVALUATION.*
