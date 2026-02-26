# Nexorian Audit & Evidence Repository (Public)
## Procedural Verification Manifest

### 1. Artifact Retrieval
Download target artifacts directly from this repository or clone the manifest:
`git clone https://github.com/timeismoneyinc2019-crypto/Nexorian-Audit.git`

### 2. Local Hash Computation
Compute SHA-256 hashes for any downloaded artifact using standard tools:
- Windows (PowerShell): `Get-FileHash <filename> -Algorithm SHA256`
- Linux/macOS: `sha256sum <filename>`

### 3. Hash Comparison Procedure
1. Locate the corresponding `.sha256` file for the artifact (e.g., `audit_proof_final.jsonl.sha256`).
2. Compare the locally computed hash with the contents of the `.sha256` file.
3. Affirm integrity if hashes match exactly.

### 4. Log Event Verification
1. Open `manifest.json` to identify the expected state-hash of the audit ledger.
2. For any entry $N$ in the `.jsonl` log:
   `SHA3-256(Entry_{N-1}.hash + Entry_N.data) == Entry_N.hash`
3. If the chain is broken, the audit is considered falsified.

### 5. Tamper & Drift Detection
- **Tamper**: Any mismatch between the artifact and its `.sha256` file.
- **Drift**: Any deviation between the `manifest.json` hash and the actual repository state.
- **Procedure**: Periodically pulse `python scripts/verify_manifest.py` against the repository.

---
*EVIDENCE-ONLY. NO OPERATIONAL CODE.*
