import hashlib
import json
import os

files = [
    "AUDIT_ATTESTATION.md",
    "DOCKER_EVAL_ENV.md",
    "index.html",
    "docs/WHITE_PAPER_ENTERPRISE.md",
    "docs/THESIS_DETERMINISTIC_GOVERNANCE.md",
    "audit_proof_final.jsonl",
    "stress_test_results.jsonl",
    "REPRODUCIBILITY_GUIDE.md",
    "ANNOUNCEMENT_v1.md"
]

manifest = {}

for f in files:
    if os.path.exists(f):
        sha256_hash = hashlib.sha256()
        with open(f, "rb") as rb:
            for byte_block in iter(lambda: rb.read(4096), b""):
                sha256_hash.update(byte_block)
        manifest[f] = sha256_hash.hexdigest().lower()
    else:
        print(f"Warning: {f} not found.")

with open("manifest.json", "w", encoding="utf-8") as wf:
    json.dump(manifest, wf, indent=4)

print("Manifest generated successfully.")
