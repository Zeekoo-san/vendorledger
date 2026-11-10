# === Stage 72: Add Markdown report export ===
# Project: VendorLedger
def export_markdown_report(vendors, currency="USD"):
    lines = ["# VendorLedger Report", "", f"Generated: {datetime.now().isoformat()}",
             f"Total Vendors: {len(vendors)}", "", "## Summary",
             f"Total Active Contracts: {sum(1 for v in vendors if any(c.status == 'active' for c in v.contracts))}",
             f"Total Orders: {sum(len(v.orders) for v in vendors)}",
             f"Total Payments: {sum(len(v.payments) for v in vendors)}"]
    for vendor in vendors:
        total_paid = sum(p.amount for p in vendor.payments)
        lines.append("")
        lines.append(f"## {vendor.name}")
        lines.append(f"Status: {vendor.status} | Balance: {currency}{vendor.balance:.2f}")
        lines.append(f"Contracts: {len(vendor.contracts)} | Orders: {len(vendor.orders)} | Payments: {len(vendor.payments)}")
        lines.append("")
        lines.append("### Contracts")
        for c in vendor.contracts:
            lines.append(f"- {c.title} ({c.status}, {currency}{c.value:.2f})")
        lines.append("")
        lines.append("### Payments")
        for p in vendor.payments:
            lines.append(f"- {p.date} for order {p.order_id} ({currency}{p.amount:.2f})")
        perf = [note for note in vendor.performance_notes if note.rating is not None]
        if perf:
            avg_rating = sum(n.rating for n in perf) / len(perf)
            lines.append(f"Average Performance Rating: {avg_rating:.2f}")
        else:
            lines.append("Performance Rating: None")
    return "\n".join(lines)
