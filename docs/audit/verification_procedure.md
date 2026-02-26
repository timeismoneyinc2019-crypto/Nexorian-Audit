# Nexorian Third-Party Verification Pathway (Procedure)

### 1. Reproduction of Results
To reproduce Nexorian governance outcomes, follow the step-by-step procedure below:
1. Clone the public repository: `https://github.com/timeismoneyinc2019-crypto/Nexorian.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Execute the stress-test harness: `python core/simulation/step5_stress_test.py`
4. Compare output `stress_test_results.jsonl` with the published audit manifest.

### 2. Independent Log Validation
Audit logs can be validated without the Nexorian runtime:
1. Load the target `.jsonl` audit file.
2. For each entry $N$, verify: `SHA3-256(Entry_{N-1}.hash + Entry_N.data) == Entry_N.hash`.
3. Verify that `Entry_0.hash` matches the published **Genesis Anchor**.

### 3. Falsifiability of Claims
A Nexorian governance claim is considered **falsified** if:
- A command marked as `REJECTED` results in a state change in the execution environment.
- Any entry in the audit log fails the SHA3-256 chain verification.
- A command exceeding the defined `epoch_limit` is marked as `APPROVED`.

### 4. Evaluator Environment
The `scripts/` directory contains all tools required to simulate, verify, and audit the system in a sterile environment.

---
*Procedural Finality v1.0*
