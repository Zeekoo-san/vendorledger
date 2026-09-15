# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: VendorLedger
# vendor_settings.py — settings dictionary and update helpers

_DEFAULT_SETTINGS = {
    "currency": "USD",
    "date_format": "%Y-%m-%d",
    "max_retries": 3,
    "log_level": "INFO",
    "notification_email": "",
    "tax_rate": 0.0,
    "payment_terms_days": 30,
    "allowed_vendors": [],
    "max_contracts_per_vendor": 0,  # 0 means unlimited
    "audit_enabled": True,
}


def get_settings():
    """Return a copy of the current settings dictionary."""
    return _SETTINGS.copy()


def set_settings(key, value):
    """Update a single setting by key. Returns True on success."""
    if key not in _DEFAULT_SETTINGS:
        raise KeyError(f"Unknown setting: {key}")
    _SETTINGS[key] = value
    return True


def reset_settings():
    """Reset all settings to their defaults."""
    global _SETTINGS
    _SETTINGS = _DEFAULT_SETTINGS.copy()
    return True
