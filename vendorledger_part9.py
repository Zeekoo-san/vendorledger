# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: VendorLedger
def sort_vendors(sort_key='last_update'):
    """Return a sorted list of Vendor objects."""
    keys = {
        'title': lambda v: v.title.lower(),
        'date': lambda v: v.contract_date,
        'priority': lambda v: v.priority,
        'last_update': lambda v: v.last_update,
    }
    if sort_key not in keys:
        raise ValueError(f'Unknown sort key: {sort_key}')
    return sorted(vendors, key=keys[sort_key])
