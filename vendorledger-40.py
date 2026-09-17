# === Stage 40: Add plain text report export ===
# Project: VendorLedger
def export_to_text(self):
    lines = []
    lines.append(f"VendorLedger Report - {self.name}")
    lines.append("=" * 40)
    for v in self.vendors:
        lines.append(f"Vendor: {v.name}")
        lines.append(f"  Status: {v.status}")
        if v.contract:
            lines.append(f"  Contract: {v.contract.name} (end: {v.contract.end_date})")
        for o in v.orders:
            lines.append(f"  Order: #{o.id} - {o.item} - {o.qty}x${o.unit_price:.2f} = ${o.total:.2f}")
        for p in v.payments:
            lines.append(f"  Payment: ${p.amount:.2f} on {p.date}")
        for note in v.notes:
            lines.append(f"  Note: {note.text}")
        lines.append("-" * 40)
    return "\n".join(lines)
