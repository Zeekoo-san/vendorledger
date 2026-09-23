# === Stage 58: Add bulk update behavior for selected records ===
# Project: VendorLedger
class BulkUpdate:
    """Bulk update selected records in a VendorLedger."""
    def __init__(self, ledger, fields):
        self.ledger = ledger
        self.fields = fields

    def execute(self, records, values):
        for rec in records:
            for field, val in zip(self.fields, values):
                rec[field] = val
        return len(records)
