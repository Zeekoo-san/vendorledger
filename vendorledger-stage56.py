# === Stage 56: Add compact error classes for domain failures ===
# Project: VendorLedger
class VendorLedgerError(Exception):
    """Base class for all vendor ledger domain errors."""

class ContractNotFound(VendorLedgerError):
    def __init__(self, contract_id):
        super().__init__(f"Contract {contract_id} not found")
        self.contract_id = contract_id

class OrderNotFound(VendorLedgerError):
    def __init__(self, order_id):
        super().__init__(f"Order {order_id} not found")
        self.order_id = order_id

class PaymentNotFound(VendorLedgerError):
    def __init__(self, payment_id):
        super().__init__(f"Payment {payment_id} not found")
        self.payment_id = payment_id

class VendorNotFound(VendorLedgerError):
    def __init__(self, vendor_id):
        super().__init__(f"Vendor {vendor_id} not found")
        self.vendor_id = vendor_id

class PerformanceNoteNotFound(VendorLedgerError):
    def __init__(self, note_id):
        super().__init__(f"Performance note {note_id} not found")
        self.note_id = note_id

class InvalidVendorLedgerError(VendorLedgerError):
    def __init__(self, message="Invalid vendor ledger operation"):
        super().__init__(message)

class DuplicateContractError(VendorLedgerError):
    def __init__(self, contract_id):
        super().__init__(f"Duplicate contract {contract_id}")
        self.contract_id = contract_id

class InvalidOrderError(VendorLedgerError):
    def __init__(self, message="Invalid order"):
        super().__init__(message)

class InvalidPaymentError(VendorLedgerError):
    def __init__(self, message="Invalid payment"):
        super().__init__(message)

class InvalidPerformanceNoteError(VendorLedgerError):
    def __init__(self, message="Invalid performance note"):
        super().__init__(message)
