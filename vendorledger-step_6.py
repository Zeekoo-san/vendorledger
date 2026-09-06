# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: VendorLedger
def delete(self, record_id: str, confirm: bool = False) -> bool:
        """Delete a record by ID.
        When confirm is False, the deletion is only simulated (returns False).
        When confirm is True, the record is actually removed from the ledger.
        """
        if not confirm:
            print(f"[DRY RUN] Would delete record {record_id}. Set confirm=True to execute.")
            return False
        if record_id not in self._records:
            print(f"Record {record_id} not found.")
            return False
        del self._records[record_id]
        print(f"Record {record_id} deleted successfully.")
        return True
