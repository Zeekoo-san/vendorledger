# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: VendorLedger
from datetime import datetime

def archive_records(records, cutoff_date=None, status_filter=None):
    if cutoff_date is None:
        cutoff_date = datetime.now().date()
    if status_filter is None:
        status_filter = ["completed", "inactive", "expired", "cancelled"]
    archived = []
    for r in records:
        if isinstance(r, dict) and r.get("status") in status_filter:
            end_date = r.get("end_date", r.get("expiry_date"))
            if end_date and datetime.fromisoformat(end_date.replace("Z", "+00:00")).date() <= cutoff_date:
                archived.append(r)
    return archived
