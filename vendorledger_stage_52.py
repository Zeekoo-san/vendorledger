# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: VendorLedger
def _format_currency(value: float) -> str:
    """Return a currency string with two decimal places."""
    return f"{value:.2f}"
