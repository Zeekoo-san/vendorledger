# === Stage 67: Add a function that returns key project metrics ===
# Project: VendorLedger
def project_metrics(vendor_ledger):
    total_orders = sum(len(v['orders']) for v in vendor_ledger['vendors'].values())
    total_payments = sum(v['payments'] for v in vendor_ledger['vendors'].values())
    total_contracts = len(vendor_ledger['contracts'])
    total_notes = sum(len(v['notes']) for v in vendor_ledger['vendors'].values())
    active_vendors = sum(1 for v in vendor_ledger['vendors'].values() if v['active'])
    metrics = {
        'total_vendors': len(vendor_ledger['vendors']),
        'active_vendors': active_vendors,
        'total_orders': total_orders,
        'total_payments': total_payments,
        'total_contracts': total_contracts,
        'total_notes': total_notes,
    }
    return metrics
