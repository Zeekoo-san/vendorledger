# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: VendorLedger
def vendor_priority(vendor: dict) -> tuple:
    """Return (score, label) for a vendor based on historical performance."""
    avg_perf = vendor.get("avg_performance", 0.0)
    on_time = vendor.get("on_time_delivery", 0.0)
    score = avg_perf * 0.6 + on_time * 0.4
    if score >= 0.85:
        label = "preferred"
    elif score >= 0.65:
        label = "acceptable"
    else:
        label = "at_risk"
    return score, label
