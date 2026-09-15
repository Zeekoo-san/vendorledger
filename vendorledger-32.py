# === Stage 32: Add pagination helpers for long console output ===
# Project: VendorLedger
def paginate(text: str, width: int = 80):
    """Wrap long text into fixed-width lines for console readability."""
    if not text:
        return []
    lines = []
    for raw in text.splitlines():
        for i in range(0, len(raw), width):
            lines.append(raw[i : i + width])
    return lines
