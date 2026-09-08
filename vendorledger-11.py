# === Stage 11: Add JSON export for the current application state ===
# Project: VendorLedger
import json, datetime, os

def export_state(ledger_path="vendor_ledger.json"):
    if not os.path.exists(ledger_path):
        return {"error": "No ledger file found"}
    with open(ledger_path, "r") as f:
        state = json.load(f)
    state["_exported_at"] = datetime.datetime.utcnow().isoformat()
    with open(ledger_path, "w") as f:
        json.dump(state, f, indent=2)
    return state
