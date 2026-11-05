# === Stage 66: Add export of a short status dashboard ===
# Project: VendorLedger
def export_status_dashboard(vendors, orders, payments):
    summary = {
        "total_vendors": len(vendors),
        "total_orders": len(orders),
        "total_payments": sum(p.get("amount", 0) for p in payments),
        "pending_orders": sum(1 for o in orders if o.get("status") != "completed"),
        "completed_orders": sum(1 for o in orders if o.get("status") == "completed"),
        "total_revenue": sum(o.get("amount", 0) for o in orders if o.get("status") == "completed"),
    }
    lines = ["VENDOR LEDGER STATUS DASHBOARD"]
    lines.append("=" * 32)
    lines.append(f"Total Vendors      : {summary['total_vendors']}")
    lines.append(f"Total Orders       : {summary['total_orders']}")
    lines.append(f"  Completed        : {summary['completed_orders']}")
    lines.append(f"  Pending          : {summary['pending_orders']}")
    lines.append(f"Total Payments     : {summary['total_payments']:.2f}")
    lines.append(f"Total Revenue      : {summary['total_revenue']:.2f}")
    return "\n".join(lines)
