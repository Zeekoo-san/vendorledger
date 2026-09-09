# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: VendorLedger
def dispatch(text):
    """Parse a simple text command and return a response string."""
    parts = text.strip().split(None, 1)
    cmd = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""

    if cmd == "help":
        return "Available commands: help, add_vendor, view_vendors, add_order, view_orders, add_payment, view_payments, add_note, view_notes, status"
    elif cmd == "add_vendor":
        if not arg:
            return "Usage: add_vendor <name> <type>"
        name, vtype = arg.split(None, 1)
        return f"Vendor '{name}' added as {vtype}"
    elif cmd == "view_vendors":
        return "Vendor list: (none registered yet)"
    elif cmd == "add_order":
        if not arg:
            return "Usage: add_order <vendor_name> <amount>"
        return f"Order for {arg.split(None, 1)[0]}: {arg.split(None, 1)[1]} recorded"
    elif cmd == "view_orders":
        return "Order list: (none yet)"
    elif cmd == "add_payment":
        if not arg:
            return "Usage: add_payment <vendor_name> <amount>"
        return f"Payment of {arg.split(None, 1)[1]} to {arg.split(None, 1)[0]} logged"
    elif cmd == "view_payments":
        return "Payment list: (none yet)"
    elif cmd == "add_note":
        if not arg:
            return "Usage: add_note <vendor_name> <note>"
        return f"Note added for {arg.split(None, 1)[0]}"
    elif cmd == "view_notes":
        return "Notes: (none yet)"
    elif cmd == "status":
        return "System status: VendorLedger running. No persistent storage in this demo."
    else:
        return f"Unknown command: {cmd}. Type 'help' for a list."
