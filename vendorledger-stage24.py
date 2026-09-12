# === Stage 24: Add grouped summaries by category or status ===
# Project: VendorLedger
def grouped_summaries(items, group_by):
    groups = {}
    for item in items:
        key = item[group_by]
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups
