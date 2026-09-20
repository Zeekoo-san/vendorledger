# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: VendorLedger
import unittest
from vendor_ledger.models.contract import Contract

class TestContractEdgeCases(unittest.TestCase):
    def test_update_missing_contract(self):
        contract = Contract(id="nonexistent", vendor_id="V001", total_amount=0)
        with self.assertRaises(KeyError):
            contract.update(Contract(id="nonexistent", vendor_id="V001", total_amount=100))
    def test_delete_missing_contract(self):
        contract = Contract(id="nonexistent", vendor_id="V001", total_amount=0)
        with self.assertRaises(KeyError):
            contract.delete()
    def test_update_preserves_id(self):
        contract = Contract(id="C001", vendor_id="V001", total_amount=1000)
        updated = contract.update(Contract(id="C001", vendor_id="V001", total_amount=1500))
        self.assertEqual(updated.id, "C001")
        self.assertEqual(updated.total_amount, 1500)
    def test_delete_returns_original(self):
        contract = Contract(id="C002", vendor_id="V002", total_amount=500)
        deleted = contract.delete()
        self.assertEqual(deleted.id, "C002")
        self.assertEqual(deleted.total_amount, 500)

if __name__ == "__main__":
    unittest.main()
