# === Stage 45: Add restore from backup with validation ===
# Project: VendorLedger
def restore_ledger(path: str) -> dict:
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception as e:
        return {"status": "error", "message": f"Failed to read backup: {e}"}
    if not isinstance(data, dict) or "ledger" not in data:
        return {"status": "error", "message": "Invalid backup structure"}
    for section in ("contracts", "orders", "payments", "performance_notes"):
        if section not in data["ledger"]:
            return {"status": "error", "message": f"Missing section: {section}"}
    try:
        data["ledger"].setdefault("contracts", [])
        data["ledger"].setdefault("orders", [])
        data["ledger"].setdefault("payments", [])
        data["ledger"].setdefault("performance_notes", [])
    except Exception as e:
        return {"status": "error", "message": f"Failed to restore: {e}"}
    return {"status": "ok", "message": f"Restored {len(data['ledger'].get('contracts', []))} contracts, "
                                       f"{len(data['ledger'].get('orders', []))} orders, "
                                       f"{len(data['ledger'].get('payments', []))} payments, "
                                       f"{len(data['ledger'].get('performance_notes', []))} notes"}
