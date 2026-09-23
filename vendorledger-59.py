# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: VendorLedger
# VendorLedger – bulk delete with confirmation guard
# Appends to existing ledger module.

class BulkDeleteGuard:
    """Prevents accidental bulk removal unless explicitly confirmed."""

    def __init__(self, ledger: Ledger):
        self.ledger = ledger

    def _count(self, kind: str) -> int:
        return getattr(self.ledger, f"count_{kind}")()

    def confirm(self, kind: str) -> bool:
        """Ask user; return True only when confirmed and count > 0."""
        n = self._count(kind)
        if n == 0:
            print(f"[BulkDelete] Nothing to remove for {kind}.")
            return False
        response = input(f"[BulkDelete] Delete all {n} {kind}? (y/n) ")
        return response.strip().lower() == "y"

    def execute(self, kind: str) -> int:
        if not self.confirm(kind):
            return 0
        method = getattr(self.ledger, f"delete_{kind}")
        removed = method()
        print(f"[BulkDelete] Removed {removed} {kind}.")
        return removed
