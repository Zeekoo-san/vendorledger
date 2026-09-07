# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: VendorLedger
def search_vendors(self, query: str):
    """Case-insensitive search across key fields."""
    query = query.strip().lower()
    if not query:
        return list(self._vendors.values())

    results = []
    for vid, v in self._vendors.items():
        searchable = [
            v['name'], v['email'], v['phone'], v['address'],
            v['category'], v['status'], v['notes'],
        ]
        if any(query in s for s in searchable):
            results.append(v)
    return results
