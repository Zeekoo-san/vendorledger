# === Stage 51: Add unit tests for search and filter behavior ===
# Project: VendorLedger
import pytest
from vendor_ledger.models.contract import Contract
from vendor_ledger.models.order import Order
from vendor_ledger.models.payment import Payment
from vendor_ledger.models.performance_note import PerformanceNote
from vendor_ledger.services import ledger

@pytest.fixture
def sample_data():
    c1 = Contract("C001", "Acme Corp", 10000.0, "2024-01-01", "2024-12-31", "good")
    c2 = Contract("C002", "Beta Inc", 5000.0, "2024-03-01", "2025-02-28", "needs_review")
    o1 = Order("O001", c1, 2500.0, "2024-02-15")
    o2 = Order("O002", c2, 1500.0, "2024-04-10")
    p1 = Payment("P001", o1, 2000.0, "2024-03-01", "approved")
    p2 = Payment("P002", o2, 1500.0, "2024-05-15", "pending")
    n1 = PerformanceNote("N001", c1, "on_time_delivery", "2024-06-01", 4.5)
    n2 = PerformanceNote("N002", c2, "late_shipment", "2024-07-10", 3.0)
    ledger.load_all([c1, c2, o1, o2, p1, p2, n1, n2])
    return {"c1": c1, "c2": c2, "o1": o1, "o2": o2, "p1": p1, "p2": p2, "n1": n1, "n2": n2}

class TestSearchAndFilter:
    def test_search_by_vendor(self, sample_data):
        results = ledger.search(vendor="Acme Corp")
        assert len(results) == 1
        assert results[0]["vendor"] == "Acme Corp"

    def test_search_by_contract_id(self, sample_data):
        results = ledger.search(contract_id="C001")
        assert len(results) == 1
        assert results[0]["contract_id"] == "C001"

    def test_filter_by_status(self, sample_data):
        results = ledger.filter(status="good")
        assert len(results) == 1
        assert results[0]["contract_id"] == "C001"

    def test_filter_by_performance(self, sample_data):
        results = ledger.filter(performance_rating=4.5)
        assert len(results) == 1
        assert results[0]["note_id"] == "N001"

    def test_search_combined(self, sample_data):
        results = ledger.search(vendor="Beta Inc", status="needs_review")
        assert len(results) == 1
        assert results[0]["contract_id"] == "C002"
