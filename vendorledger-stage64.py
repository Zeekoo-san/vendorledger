# === Stage 64: Add validation for relationship references ===
# Project: VendorLedger
def validate_relationships(ledger):
    valid_vendor_ids = {c['id'] for c in ledger['contracts']}
    valid_order_ids = {o['id'] for o in ledger['orders']}
    valid_payment_ids = {p['id'] for p in ledger['payments']}

    def check(contract):
        if not isinstance(contract, dict):
            return "Contract is not a dictionary"
        for field in ('vendor_id', 'lead_order_id'):
            if field not in contract:
                return f"Contract missing field '{field}'"
            ref = contract[field]
            if not isinstance(ref, str) or not ref:
                return f"Contract '{contract.get('id')}' has invalid reference for '{field}'"
            if ref not in valid_order_ids and ref not in valid_payment_ids:
                return f"Contract '{contract.get('id')}' references unknown id '{ref}'"
        return None

    def check_order(order):
        if not isinstance(order, dict):
            return "Order is not a dictionary"
        for field in ('vendor_id',):
            if field not in order:
                return f"Order missing field '{field}'"
            ref = order[field]
            if not isinstance(ref, str) or not ref:
                return f"Order '{order.get('id')}' has invalid reference for '{field}'"
            if ref not in valid_vendor_ids:
                return f"Order '{order.get('id')}' references unknown vendor '{ref}'"
        return None

    def check_payment(payment):
        if not isinstance(payment, dict):
            return "Payment is not a dictionary"
        for field in ('vendor_id', 'order_id'):
            if field not in payment:
                return f"Payment missing field '{field}'"
            ref = payment[field]
            if not isinstance(ref, str) or not ref:
                return f"Payment '{payment.get('id')}' has invalid reference for '{field}'"
            if ref not in valid_vendor_ids:
                return f"Payment '{payment.get('id')}' references unknown vendor '{ref}'"
            if field == 'order_id' and ref not in valid_order_ids:
                return f"Payment '{payment.get('id')}' references unknown order '{ref}'"
        return None

    errors = []
    for contract in ledger.get('contracts', []):
        err = check(contract)
        if err:
            errors.append(err)
    for order in ledger.get('orders', []):
        err = check_order(order)
        if err:
            errors.append(err)
    for payment in ledger.get('payments', []):
        err = check_payment(payment)
        if err:
            errors.append(err)
    return errors
