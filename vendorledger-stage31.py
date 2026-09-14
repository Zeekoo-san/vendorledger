# === Stage 31: Add compact table rendering for long lists ===
# Project: VendorLedger
class CompactTable:
    """Renders long lists as a scrollable compact table with fixed column widths."""

    def __init__(self, columns, width=80, max_rows=20):
        self.columns = columns
        self.width = width
        self.max_rows = max_rows

    def render(self, data, row_key=None):
        if not data:
            return "No data."
        max_len = max((len(str(row.get(col, ''))) for row in data for col in self.columns), default=0)
        col_widths = [min(max_len, max(self.width // len(self.columns), 3)) for _ in self.columns]
        row_key = row_key or 0
        return "\n".join(
            "\t".join(f"{row.get(col, '')[:w]:>{w}}" for col, w in zip(self.columns, col_widths))
            for row in data[:self.max_rows]
        )
