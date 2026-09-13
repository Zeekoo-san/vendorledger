# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: VendorLedger
import datetime

def upcoming_items(items, days_ahead=30, reference=None):
    """Return items whose scheduled date falls within the next `days_ahead` days.
    
    Args:
        items: Iterable of objects with a `date` attribute (datetime.date or datetime.datetime).
        days_ahead: Number of days to look ahead.
        reference: Optional datetime.date or datetime.datetime to use as the reference date.
                   Defaults to today.
    
    Returns:
        List of items sorted by date (earliest first).
    
    Raises:
        TypeError: If any item in `items` is not a dict or has no `date` key.
    """
    if reference is None:
        reference = datetime.date.today()
    else:
        if isinstance(reference, datetime.datetime):
            reference = reference.date()
    
    try:
        ref_date = reference.date()
    except AttributeError:
        raise TypeError("Reference date must be a datetime.date or datetime.datetime instance.")

    if not isinstance(items, (list, tuple, set)):
        items = list(items)

    result = []
    for item in items:
        if isinstance(item, dict):
            date_val = item.get("date")
            if date_val is None:
                continue
            try:
                dt = datetime.date.fromisoformat(date_val) if isinstance(date_val, str) else date_val.date()
            except (ValueError, AttributeError):
                continue
        elif hasattr(item, "date"):
            dt = item.date()
        else:
            continue

        if isinstance(dt, datetime.datetime):
            dt = dt.date()

        if isinstance(dt, datetime.date):
            if dt > ref_date and dt <= ref_date + datetime.timedelta(days=days_ahead):
                result.append(item)
        elif isinstance(dt, datetime.datetime):
            if dt > ref_date and dt <= ref_date + datetime.timedelta(days=days_ahead):
                result.append(item)

    result.sort(key=lambda x: x["date"] if isinstance(x, dict) else x.date())
    return result
