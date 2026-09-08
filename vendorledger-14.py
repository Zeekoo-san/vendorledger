# === Stage 14: Add file load support with fallback demo data ===
# Project: VendorLedger
def load_vendors(source: str = "demo") -> list[Vendor]:
    """Return vendor records from a file or fall back to built-in demo data."""
    try:
        path = os.path.join(DATA_DIR, f"{source}.json")
        with open(path, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
        return [Vendor(**r) for r in raw]
    except Exception:
        return DEMO_VENDORS
