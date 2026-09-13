# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: VendorLedger
def parse_date(date_str, fmt=None):
    """Parse a date string with clear error messages."""
    if fmt is None:
        for f in ("%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%m-%d-%Y", "%d-%m-%Y"):
            try:
                return datetime.strptime(date_str, f)
            except ValueError:
                continue
        raise ValueError(f"Unable to parse date '{date_str}'")
    return datetime.strptime(date_str, fmt)
