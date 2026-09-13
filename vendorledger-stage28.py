# === Stage 28: Add overdue item detection based on due dates ===
# Project: VendorLedger
def find_overdue_items(items, today=None):
    """Return list of items past their due date, sorted by how far overdue."""
    if today is None:
        today = datetime.date.today()
    overdue = []
    for item in items:
        due = item.get("due_date")
        if due and isinstance(due, str):
            due = datetime.date.fromisoformat(due)
        if due and due < today:
            overdue.append({"item": item, "days_overdue": (today - due).days})
    overdue.sort(key=lambda x: x["days_overdue"])
    return overdue

def mark_items_overdue(items, today=None):
    """Add an 'overdue' key to items whose due date has passed."""
    if today is None:
        today = datetime.date.today()
    result = []
    for item in items:
        due = item.get("due_date")
        if due and isinstance(due, str):
            due = datetime.date.fromisoformat(due)
        if due and due < today:
            item["overdue"] = (today - due).days
        result.append(item)
    return result
