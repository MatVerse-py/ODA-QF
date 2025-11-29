import json
import hashlib
from pathlib import Path

LEDGER_PATH = Path("audit/ledger.json")

def verify_ledger():
    if not LEDGER_PATH.exists():
        return False

    data = json.loads(LEDGER_PATH.read_text())
    for entry in data:
        computed = hashlib.sha256(json.dumps(entry["state"], sort_keys=True).encode()).hexdigest()
        if computed != entry["hash"]:
            return False
    return True
