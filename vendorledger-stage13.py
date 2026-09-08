# === Stage 13: Add file save support using a configurable path ===
# Project: VendorLedger
import os

class FileStorage:
    def __init__(self, base_path="vendor_ledger_data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

    def save(self, record, filename):
        filepath = os.path.join(self.base_path, filename)
        with open(filepath, "w") as f:
            import json
            json.dump(record, f, indent=2)
        return filepath

    def load(self, filename):
        filepath = os.path.join(self.base_path, filename)
        with open(filepath, "r") as f:
            import json
            return json.load(f)
