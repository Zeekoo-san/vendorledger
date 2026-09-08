# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: VendorLedger
import json

def load_ledger(path: str) -> dict:
    """Load the JSON ledger file, returning an empty dict on any error."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Top-level JSON must be an object")
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        print(f"[LEDGER] Malformed JSON at {path}: {exc}")
        return {}
    except Exception as exc:
        print(f"[LEDGER] Unexpected error reading {path}: {exc}")
        return {}
