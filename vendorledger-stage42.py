# === Stage 42: Add CSV export without external dependencies ===
# Project: VendorLedger
def export_csv(self, filename='vendor_ledger.csv'):
    import csv
    rows = []
    for entry in self.entries:
        row = [
            entry.get('date', ''),
            entry.get('type', ''),
            entry.get('vendor', ''),
            entry.get('amount', ''),
            entry.get('notes', ''),
        ]
        rows.append(row)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'type', 'vendor', 'amount', 'notes'])
        writer.writerows(rows)
    return filename
