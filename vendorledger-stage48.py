# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: VendorLedger
import unittest
from datetime import date

class TestVendorLedger(unittest.TestCase):

    def test_create_contract(self):
        contract = VendorLedger.create_contract(
            vendor_id="V001",
            name="Acme Corp",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 12, 31),
            terms="Net 30"
        )
        self.assertEqual(contract.vendor_id, "V001")
        self.assertEqual(contract.name, "Acme Corp")
        self.assertEqual(contract.terms, "Net 30")

    def test_create_order(self):
        order = VendorLedger.create_order(
            contract_id="C001",
            items=[{"sku": "WIDGET", "qty": 10, "unit_price": 5.0}],
            delivery_date=date(2024, 3, 15)
        )
        self.assertEqual(order.contract_id, "C001")
        self.assertEqual(len(order.items), 1)
        self.assertEqual(order.items[0].qty, 10)
        self.assertEqual(order.total_amount, 50.0)

    def test_create_payment(self):
        payment = VendorLedger.create_payment(
            order_id="O001",
            amount=50.0,
            method="bank_transfer",
            date=date(2024, 3, 20)
        )
        self.assertEqual(payment.amount, 50.0)
        self.assertEqual(payment.status, "pending")

    def test_validate_contract_dates(self):
        with self.assertRaises(ValueError):
            VendorLedger.create_contract(
                vendor_id="V002",
                name="Bad Corp",
                start_date=date(2025, 1, 1),
                end_date=date(2024, 6, 30),
                terms="Net 30"
            )

    def test_validate_payment_amount(self):
        with self.assertRaises(ValueError):
            VendorLedger.create_payment(
                order_id="O002",
                amount=-100.0,
                method="bank_transfer",
                date=date(2024, 4, 1)
            )

    def test_validate_payment_date(self):
        with self.assertRaises(ValueError):
            VendorLedger.create_payment(
                order_id="O003",
                amount=100.0,
                method="bank_transfer",
                date=date(2020, 1, 1)
            )

if __name__ == "__main__":
    unittest.main()
