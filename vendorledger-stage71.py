# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: VendorLedger
def seed_demo_data(store):
    store["vendors"] = [
        {"id": "V001", "name": "Acme Widgets", "category": "hardware", "status": "active"},
        {"id": "V002", "name": "Globex Supplies", "category": "office", "status": "active"},
        {"id": "V003", "name": "Initech Paper", "category": "paper", "status": "paused"},
    ]
    store["contracts"] = [
        {"id": "C001", "vendor_id": "V001", "start": "2024-01-01", "end": "2024-12-31", "value": 120000.0},
        {"id": "C002", "vendor_id": "V002", "start": "2024-02-01", "end": "2024-11-30", "value": 45000.0},
    ]
    store["orders"] = [
        {"id": "O001", "contract_id": "C001", "vendor_id": "V001", "quantity": 100, "unit_price": 150.0, "status": "delivered"},
        {"id": "O002", "contract_id": "C002", "vendor_id": "V002", "quantity": 500, "unit_price": 20.0, "status": "in_progress"},
    ]
    store["payments"] = [
        {"id": "P001", "order_id": "O001", "amount": 15000.0, "date": "2024-03-15", "status": "paid"},
        {"id": "P002", "order_id": "O002", "amount": 5000.0, "date": "2024-06-01", "status": "pending"},
    ]
    store["performance_notes"] = [
        {"id": "N001", "vendor_id": "V001", "date": "2024-04-01", "rating": 4.8, "comment": "Reliable and on-time deliveries."},
        {"id": "N002", "vendor_id": "V002", "date": "2024-05-10", "rating": 3.5, "comment": "Occasional delays noted."},
    ]
