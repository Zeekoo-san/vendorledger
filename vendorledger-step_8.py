# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: VendorLedger
def filter_records(records, **kwargs):
    """Filter records by any combination of status, category, owner, tag.
    
    Args:
        records: List of record dicts.
        **kwargs: Keyword arguments for filtering, e.g., status='active', category='tech'.
    
    Returns:
        Filtered list of records.
    
    Example:
        >>> filter_records(records, status='completed')
        [record1, record2]
    """
    if not kwargs:
        return records
    
    result = []
    for record in records:
        match = True
        for field, value in kwargs.items():
            if field in record:
                if record[field] != value:
                    match = False
                    break
            else:
                match = False
                break
        if match:
            result.append(record)
    return result
