# === Stage 63: Add relationships between records where useful ===
# Project: VendorLedger
def link_records(self):
    """Add relationships between records where useful."""
    self._link_orders_to_contract()
    self._link_payments_to_order()
    self._link_performance_to_vendor()

    def _link_orders_to_contract(self):
        for order in self._orders:
            order.contract_id = self._contracts[order.contract_id]

    def _link_payments_to_order(self):
        for payment in self._payments:
            payment.order_id = self._orders[payment.order_id]

    def _link_performance_to_vendor(self):
        for note in self._performance_notes:
            note.vendor_id = self._vendors[note.vendor_id]

    return self
