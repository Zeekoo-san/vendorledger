# === Stage 25: Add daily summary calculations ===
# Project: VendorLedger
def daily_summary(transactions, date_filter=None):
    """Compute a compact daily summary of transactions."""
    filtered = [t for t in transactions if date_filter is None or t.get("date") == date_filter]
    summary = {}
    for t in filtered:
        day = t.get("date", "Unknown")
        if day not in summary:
            summary[day] = {"total": 0, "count": 0, "by_vendor": {}}
        summary[day]["total"] += t.get("amount", 0)
        summary[day]["count"] += 1
        vendor = t.get("vendor")
        if vendor:
            if vendor not in summary[day]["by_vendor"]:
                summary[day]["by_vendor"][vendor] = 0
            summary[day]["by_vendor"][vendor] += t.get("amount", 0)
    return summary
