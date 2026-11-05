# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: VendorLedger
def build_changelog(activity_log):
    """Generate a compact changelog from the activity log.

    Groups entries by date and summarizes each change with its author.
    """
    entries = activity_log.get("entries", [])

    grouped = {}
    for entry in entries:
        date = entry.get("date", "Unknown")
        grouped.setdefault(date, []).append(entry)

    lines = ["CHANGELOG", "=" * 40]
    for date in sorted(grouped.keys(), reverse=True):
        lines.append(f"\n[{date}]")
        for entry in grouped[date]:
            action = entry.get("action", "note")
            author = entry.get("author", "unknown")
            detail = entry.get("detail", "")
            prefix = {
                "contract": "+",
                "order": "+",
                "payment": "$",
                "note": "!",
            }.get(action, "*")
            lines.append(f"  {prefix} {action} by {author}: {detail}")

    return "\n".join(lines)
