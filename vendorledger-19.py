# === Stage 19: Add undo support for the last simple mutation ===
# Project: VendorLedger
class SimpleUndo:
    def __init__(self):
        self.history = []

    def record(self, action):
        self.history.append(action)

    def undo(self):
        if not self.history:
            return None
        return self.history.pop()
