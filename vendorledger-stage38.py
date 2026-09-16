# === Stage 38: Add data integrity checks for broken references ===
# Project: VendorLedger
def check_reference_integrity(ledger):
    """Validate all cross-references in the ledger are intact."""
    errors = []
    for c in ledger.contracts:
        for o in c.orders:
            if o.vendor_id not in c.vendor_id:
                errors.append(f"Order {o.id} vendor_id {o.vendor_id} not in contract {c.id}")
            if o.contract_id != c.id:
                errors.append(f"Order {o.id} contract_id {o.contract_id} != contract {c.id}")
    for p in ledger.payments:
        if p.order_id not in (o.id for o in ledger.orders):
            errors.append(f"Payment {p.id} order_id {p.order_id} not found")
    for n in ledger.performance_notes:
        if n.contract_id not in (c.id for c in ledger.contracts):
            errors.append(f"Note {n.id} contract_id {n.contract_id} not found")
    return errors
