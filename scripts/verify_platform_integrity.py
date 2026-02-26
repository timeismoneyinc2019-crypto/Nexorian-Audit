import hashlib
import json
import os
import datetime

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest().lower()

def run_verification():
    print(f"--- NEXORIAN CONTINUOUS VERIFICATION [{datetime.datetime.now()}] ---")
    manifest_path = "manifest.json"
    
    if not os.path.exists(manifest_path):
        print("ERROR: Manifest not found.")
        return

    with open(manifest_path, "r") as f:
        manifest = json.load(f)

    all_passed = True
    log_entries = []

    for file_path, expected_hash in manifest.items():
        if not os.path.exists(file_path):
            print(f"[-] MISSING: {file_path}")
            all_passed = False
            continue
        
        actual_hash = get_sha256(file_path)
        if actual_hash == expected_hash:
            print(f"[+] VERIFIED: {file_path}")
        else:
            print(f"[!] FAILED: {file_path}")
            print(f"    Expected: {expected_hash}")
            print(f"    Actual:   {actual_hash}")
            all_passed = False

    # Log the verification event
    status = "SUCCESS" if all_passed else "FAILURE"
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "status": status,
        "checked_files": len(manifest)
    }
    
    with open("verification_audit.log", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

    print(f"\nFINAL STATUS: {status}")

if __name__ == "__main__":
    run_verification()
