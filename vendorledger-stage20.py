# === Stage 20: Add duplicate detection for newly created records ===
# Project: VendorLedger
def find_duplicates(records):
    if not records:
        return []
    seen = {}
    duplicates = []
    for record in records:
        key = record.get('vendor', record.get('contract_id', record.get('order_id', record.get('payment_id', ''))))
        if key in seen:
            duplicates.append(key)
        else:
            seen[key] = record
    return duplicates
