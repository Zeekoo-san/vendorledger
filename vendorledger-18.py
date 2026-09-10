# === Stage 18: Add an activity log with timestamps and action names ===
# Project: VendorLedger
class ActivityLog:
    def __init__(self, ledger):
        self.ledger = ledger
        self.log = []

    def log(self, action, user=None):
        entry = {"timestamp": datetime.now(), "action": action, "user": user or "system"}
        self.log.append(entry)

    def get_log(self):
        return self.log
