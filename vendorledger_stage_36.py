# === Stage 36: Add templates for quickly creating common records ===
# Project: VendorLedger
# Templates for quickly creating common records

def create_contract_template():
    return {
        "contract_id": None,
        "contract_number": None,
        "vendor_id": None,
        "start_date": None,
        "end_date": None,
        "terms": "Standard terms",
        "status": "draft",
        "notes": "",
    }

def create_order_template():
    return {
        "order_id": None,
        "order_number": None,
        "vendor_id": None,
        "contract_id": None,
        "item": "",
        "quantity": 0,
        "unit_price": 0.0,
        "total": 0.0,
        "status": "pending",
        "delivery_date": None,
        "notes": "",
    }

def create_payment_template():
    return {
        "payment_id": None,
        "payment_number": None,
        "vendor_id": None,
        "order_id": None,
        "contract_id": None,
        "amount": 0.0,
        "currency": "USD",
        "payment_date": None,
        "method": "bank_transfer",
        "status": "pending",
        "notes": "",
    }

def create_performance_note_template():
    return {
        "note_id": None,
        "vendor_id": None,
        "date": None,
        "category": "general",
        "rating": None,
        "summary": "",
        "details": "",
        "status": "open",
        "resolved_date": None,
    }
