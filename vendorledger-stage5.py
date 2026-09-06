# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: VendorLedger
def update_vendor(self, vendor_id, updates):
    """Update an existing vendor record. Returns None if not found."""
    if vendor_id not in self._vendors:
        print(f"Vendor {vendor_id} not found – no update applied.")
        return None
    for key, value in updates.items():
        if key not in self._vendors[vendor_id]:
            print(f"Unknown field '{key}' for vendor {vendor_id} – ignored.")
            continue
        self._vendors[vendor_id][key] = value
    print(f"Vendor {vendor_id} updated: {updates}")
    return self._vendors[vendor_id]


def update_order(self, order_id, updates):
    """Update an existing order. Returns None if not found."""
    if order_id not in self._orders:
        print(f"Order {order_id} not found – no update applied.")
        return None
    for key, value in updates.items():
        if key not in self._orders[order_id]:
            print(f"Unknown field '{key}' for order {order_id} – ignored.")
            continue
        self._orders[order_id][key] = value
    print(f"Order {order_id} updated: {updates}")
    return self._orders[order_id]


def update_payment(self, payment_id, updates):
    """Update an existing payment. Returns None if not found."""
    if payment_id not in self._payments:
        print(f"Payment {payment_id} not found – no update applied.")
        return None
    for key, value in updates.items():
        if key not in self._payments[payment_id]:
            print(f"Unknown field '{key}' for payment {payment_id} – ignored.")
            continue
        self._payments[payment_id][key] = value
    print(f"Payment {payment_id} updated: {updates}")
    return self._payments[payment_id]


def update_performance_note(self, note_id, updates):
    """Update an existing performance note. Returns None if not found."""
    if note_id not in self._performance_notes:
        print(f"Performance note {note_id} not found – no update applied.")
        return None
    for key, value in updates.items():
        if key not in self._performance_notes[note_id]:
            print(f"Unknown field '{key}' for note {note_id} – ignored.")
            continue
        self._performance_notes[note_id][key] = value
    print(f"Note {note_id} updated: {updates}")
    return self._performance_notes[note_id]
