import hashlib
import json
from pathlib import Path

LEDGER_PATH = Path("audit/ledger.json")

def commit_state(state: dict):
    """
    Grava estado em ledger auditável (Merkle-ready).
    """
    LEDGER_PATH.parent.mkdir(exist_ok=True)
    
    ledger = []
    if LEDGER_PATH.exists():
        ledger = json.loads(LEDGER_PATH.read_text())

    entry_hash = hashlib.sha256(json.dumps(state, sort_keys=True).encode()).hexdigest()

    ledger.append({
        "state": state,
        "hash": entry_hash
    })

    LEDGER_PATH.write_text(json.dumps(ledger, indent=2))
    return entry_hash
