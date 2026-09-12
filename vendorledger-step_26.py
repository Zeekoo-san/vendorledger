# === Stage 26: Add weekly summary calculations ===
# Project: VendorLedger
def weekly_summary(vendor_list, date):
    """Return a dict of weekly stats per vendor for the given date."""
    weekly = {}
    for v in vendor_list:
        if v.contract and v.contract.active:
            orders = [o for o in v.orders if o.delivery_date <= date]
            paid = [o for o in orders if o.paid]
            weekly[v.vendor_id] = {
                "orders": len(orders),
                "completed": len([o for o in orders if o.completed]),
                "paid": len(paid),
                "total_value": sum(o.value for o in orders),
                "paid_value": sum(o.value for o in paid),
                "avg_lead_days": (
                    sum((o.delivery_date - o.order_date).days for o in orders if o.order_date)
                    / max(len(orders), 1)
                ),
                "performance": sum(1 for note in v.performance_notes if note.rating >= 4),
                "notes_count": len(v.performance_notes),
            }
    return weekly
