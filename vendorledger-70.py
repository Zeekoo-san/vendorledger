# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: VendorLedger
CONFIRM = False


def confirm(prompt, value=True):
    global CONFIRM
    CONFIRM = value
    try:
        answer = input(prompt).strip().lower()
    except EOFError:
        answer = "n"
    CONFIRM = answer in ("y", "yes")


def clear_state(vendor_ledger):
    if not CONFIRM:
        print("Aborted: re-run with confirm=True to clear all data.")
        return vendor_ledger
    print("Clearing all contracts, orders, payments, and performance notes.")
    vendor_ledger.contracts = []
    vendor_ledger.orders = []
    vendor_ledger.payments = []
    vendor_ledger.performance_notes = []
    print("Ledger cleared.")
    return vendor_ledger
