# === Stage 37: Add recommendations for the next useful action ===
# Project: VendorLedger
class VendorPerformanceReport:
    def __init__(self, vendor_id: str, period_days: int = 90):
        self.vendor_id = vendor_id
        self.period_days = period_days
        self.orders = []
        self.payments = []
        self.contract = None
        self.performance_notes = []

    def add_order(self, order):
        self.orders.append(order)

    def add_payment(self, payment):
        self.payments.append(payment)

    def add_note(self, note):
        self.performance_notes.append(note)

    def set_contract(self, contract):
        self.contract = contract

    def get_order_metrics(self):
        total_orders = len(self.orders)
        total_value = sum(o.amount for o in self.orders)
        avg_value = total_value / total_orders if total_orders else 0
        return {
            'total_orders': total_orders,
            'total_value': total_value,
            'average_value': avg_value
        }

    def get_payment_metrics(self):
        total_payments = len(self.payments)
        total_amount = sum(p.amount for p in self.payments)
        on_time = sum(1 for p in self.payments if p.is_on_time)
        on_time_pct = (on_time / total_payments * 100) if total_payments else 0
        return {
            'total_payments': total_payments,
            'total_amount': total_amount,
            'on_time_payments': on_time,
            'on_time_percentage': on_time_pct
        }

    def get_overall_score(self):
        order_metrics = self.get_order_metrics()
        payment_metrics = self.get_payment_metrics()
        avg_value = order_metrics['average_value']
        on_time_pct = payment_metrics['on_time_percentage']
        score = min(100, max(0, (avg_value / 10000 * 20) + (on_time_pct * 0.5)))
        return score
