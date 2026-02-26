# NEXORIAN: INDEPENDENT REPRODUCIBILITY GUIDE
## Institutional Audit Protocol v1.0.0

This guide provides a standardized protocol for third-party auditors to verify the deterministic governance claims of the Nexorian Enterprise Platform.

### 1. Verification of Published Artifacts
Every project document, log, and specification is signed with a SHA-256 hash.

**Protocol**:
1. Clone the Audit Evidence repository:
   ```bash
   git clone https://github.com/timeismoneyinc2019-crypto/Nexorian-Audit.git
   ```
2. Open `manifest.json`.
3. Verify the hash for `docs/WHITE_PAPER_ENTERPRISE.md`:
   ```bash
   # Windows
   Get-FileHash -Path docs/WHITE_PAPER_ENTERPRISE.md -Algorithm SHA256
   ```
4. Confirm coincidence with the manifest value.

### 2. Execution Reproducibility (Dockerized)
The Nexorian platform provides a sterile environment for reproducing stress tests.

**Protocol**:
1. Navigate to the `docker/` directory (or see `DOCKER_EVAL_ENV.md`).
2. Build the audit image:
   ```bash
   docker build -t nexorian-audit .
   ```
3. Run the reproduction suite:
   ```bash
   docker run nexorian-audit --scenario CT-09
   ```
4. Observe the hard-rejection of instructions when energy limits are breached.
5. Compare the resulting `reproduction_log.jsonl` with the published `stress_test_results.jsonl`.

### 3. SDK Admissibility Verification
Verify that the SDK client rejects unauthorized commands without network egress.

**Protocol**:
1. Install the SDK: `pip install nexorian-sdk`
2. Run `python examples/sandbox_demo.py`.
3. Verify that Scenario 2 triggers a `PermissionError` (GOVERNANCE_VETO).

### 4. AUDITOR CHECKLIST
- [ ] SHA-256 Manifest matches all file contents.
- [ ] Stress Test Results are reproducible in the evaluation environment.
- [ ] Audit Ledger exhibits 100% cryptographic continuity (SHA3-256).
- [ ] SDK prevents invalid state transitions in Sandbox mode.

---
**CERTIFICATION**:
This environment is certified for offline, sterile verification by the Nexorian Core Team. For notarized support, contact `compliance@nexorian.org`.
