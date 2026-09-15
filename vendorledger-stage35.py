# === Stage 35: Add active user switching and user-specific records ===
# Project: VendorLedger
class UserLedgerEntry:
    def __init__(self, user_id, entry):
        self.user_id = user_id
        self.entry = entry

    def is_active(self):
        return self.entry.get("active", False)

    def to_dict(self):
        return {"user_id": self.user_id, "entry": self.entry}


class UserLedger:
    def __init__(self):
        self.entries = {}

    def add_entry(self, user_id, entry):
        self.entries[user_id] = UserLedgerEntry(user_id, entry)

    def get_active_entries(self):
        return {uid: e for uid, e in self.entries.items() if e.is_active()}

    def get_user_entries(self, user_id):
        return [e for e in self.entries.values() if e.user_id == user_id]

    def deactivate_entry(self, user_id):
        if user_id in self.entries:
            self.entries[user_id].entry["active"] = False

    def switch_user(self, user_id):
        if user_id in self.entries:
            self.entries[user_id].entry["active"] = True
            for uid in list(self.entries.keys()):
                if uid != user_id:
                    self.entries[uid].entry["active"] = False
