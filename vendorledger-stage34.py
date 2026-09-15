# === Stage 34: Add support for multiple local user profiles ===
# Project: VendorLedger
class UserProfiles:
    def __init__(self):
        self.profiles = {}

    def add(self, name: str, vendor_id: str, email: str):
        self.profiles[name] = {"vendor_id": vendor_id, "email": email}

    def lookup(self, name: str) -> dict:
        return self.profiles.get(name, None)

    def list(self) -> list:
        return list(self.profiles.values())
