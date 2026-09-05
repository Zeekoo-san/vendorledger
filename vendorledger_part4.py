# === Stage 4: Implement create operations for the primary records ===
# Project: VendorLedger
def create_vendor(self, name, tax_id, address, email, phone, notes):
    return Vendor(name, tax_id, address, email, phone, notes)

def create_contract(self, vendor, title, terms, start_date, end_date, value, currency, notes):
    return Contract(vendor, title, terms, start_date, end_date, value, currency, notes)

def create_order(self, contract, title, items, order_date, delivery_date, notes):
    return Order(contract, title, items, order_date, delivery_date, notes)

def create_payment(self, order, amount, currency, paid_date, notes):
    return Payment(order, amount, currency, paid_date, notes)

def create_performance_note(self, vendor, contract, description, rating, date, notes):
    return PerformanceNote(vendor, contract, description, rating, date, notes)
