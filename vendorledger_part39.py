# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: VendorLedger
def repair_integrity(records):
    """Simple data integrity repair: remove duplicates, fill missing dates,
    and log any anomalies found while scanning the ledger records."""
    anomalies = []
    seen_ids = set()
    for entry in records:
        rec_id = entry.get("rec_id")
        if rec_id is None:
            entry["rec_id"] = str(id(entry))
            anomalies.append(f"Assigned anonymous rec_id to record: {entry}")
        if rec_id in seen_ids:
            anomalies.append(f"Duplicate record_id {rec_id} removed")
            records.remove(entry)
        else:
            seen_ids.add(rec_id)
    for entry in records:
        if "order_date" not in entry or not entry["order_date"]:
            entry["order_date"] = "TBD"
            anomalies.append(f"Filled missing order_date for rec_id {entry['rec_id']}")
    return records, anomalies
