# === Stage 41: Add plain text import for a simple line-based format ===
# Project: VendorLedger
def parse_line_record(line):
    """Parse a simple comma-separated line into a dict of field values."""
    record = {}
    for field in line.split(","):
        key, _, value = field.partition("=")
        record[key.strip()] = value.strip()
    return record
