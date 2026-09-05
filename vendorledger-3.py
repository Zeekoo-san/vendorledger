# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: VendorLedger
def validate_id(value):
    if value is None or not isinstance(value, str) or len(value.strip()) == 0:
        raise ValueError("Identifier must be a non-empty string")
    return value.strip()

def validate_short_text(value, max_len=200):
    if value is None or not isinstance(value, str):
        raise ValueError("Short text must be a string")
    if len(value) > max_len:
        raise ValueError(f"Short text exceeds {max_len} characters")
    return value

def validate_amount(value):
    if value is None or not isinstance(value, (int, float)):
        raise ValueError("Amount must be a number")
    if value < 0:
        raise ValueError("Amount cannot be negative")
    return value
