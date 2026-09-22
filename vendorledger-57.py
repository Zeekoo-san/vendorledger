# === Stage 57: Add structured result objects for command handlers ===
# Project: VendorLedger
class Result:
    """Base class for structured command-handler results."""
    def __init__(self, success: bool, message: str, data=None, error: str = None):
        self.success = success
        self.message = message
        self.data = data
        self.error = error

    def __repr__(self):
        if self.success:
            return f"Result(success=True, message='{self.message}')"
        return f"Result(success=False, error='{self.error}')"


class ContractResult(Result):
    def __init__(self, vendor_id, contract_id, amount, duration_days, status, notes=None):
        super().__init__(success=True, message="Contract created", data={
            "vendor_id": vendor_id,
            "contract_id": contract_id,
            "amount": amount,
            "duration_days": duration_days,
            "status": status,
            "notes": notes,
        })


class OrderResult(Result):
    def __init__(self, order_id, vendor_id, product, quantity, price, total, delivery_date):
        super().__init__(success=True, message="Order created", data={
            "order_id": order_id,
            "vendor_id": vendor_id,
            "product": product,
            "quantity": quantity,
            "price": price,
            "total": total,
            "delivery_date": delivery_date,
        })


class PaymentResult(Result):
    def __init__(self, payment_id, order_id, amount, method, date, status):
        super().__init__(success=True, message="Payment recorded", data={
            "payment_id": payment_id,
            "order_id": order_id,
            "amount": amount,
            "method": method,
            "date": date,
            "status": status,
        })


class PerformanceResult(Result):
    def __init__(self, vendor_id, period, score, metrics, notes):
        super().__init__(success=True, message="Performance note added", data={
            "vendor_id": vendor_id,
            "period": period,
            "score": score,
            "metrics": metrics,
            "notes": notes,
        })
