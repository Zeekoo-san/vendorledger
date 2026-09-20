# === Stage 50: Add unit tests for import and export behavior ===
# Project: VendorLedger
import json, os
from pathlib import Path
from vendor_ledger import VendorLedger, Vendor, Contract, Order, Payment, PerformanceNote

def test_import_export(tmp_path):
    ledger = VendorLedger()
    v = Vendor(name="Acme Corp", tier="gold")
    c = Contract(vendor=v, amount=10000, duration=12)
    o = Order(contract=c, qty=10, unit_price=100)
    p = Payment(order=o, amount=500)
    n = PerformanceNote(order=o, rating=4, comment="Good quality")
    ledger.add(vendor=v)
    ledger.add(contract=c)
    ledger.add(order=o)
    ledger.add(payment=p)
    ledger.add(note=n)

    data = ledger.export()
    assert isinstance(data, dict)
    assert "vendors" in data
    assert "contracts" in data
    assert "orders" in data
    assert "payments" in data
    assert "notes" in data
    assert data["vendors"][0]["name"] == "Acme Corp"

    out_path = tmp_path / "ledger.json"
    out_path.write_text(json.dumps(data, indent=2))
    loaded = json.loads(out_path.read_text())
    assert loaded["vendors"][0]["name"] == "Acme Corp"
    assert len(loaded["contracts"]) == 1
    assert len(loaded["orders"]) == 1
    assert len(loaded["payments"]) == 1
    assert len(loaded["notes"]) == 1
    assert loaded["payments"][0]["amount"] == 500
    assert loaded["notes"][0]["rating"] == 4
