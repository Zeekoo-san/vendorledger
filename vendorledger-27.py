# === Stage 27: Add monthly summary calculations ===
# Project: VendorLedger
def monthly_summary(vendors, orders, payments, contracts):
    from collections import defaultdict
    monthly = defaultdict(lambda: {
        'orders': [], 'payments': [], 'contracts': [],
        'total_amount': 0.0, 'total_paid': 0.0, 'count': 0
    })
    for order in orders:
        month = order['order_date'][:7] if 'order_date' in order else 'Unknown'
        monthly[month]['orders'].append(order)
        monthly[month]['total_amount'] += order.get('amount', 0.0)
        monthly[month]['count'] += 1
    for payment in payments:
        month = payment['payment_date'][:7] if 'payment_date' in payment else 'Unknown'
        monthly[month]['payments'].append(payment)
        monthly[month]['total_paid'] += payment.get('amount', 0.0)
    for contract in contracts:
        start = contract['start_date'][:7] if 'start_date' in contract else 'Unknown'
        end = contract['end_date'][:7] if 'end_date' in contract else start
        for m in (start, end):
            monthly[m]['contracts'].append(contract)
    return dict(monthly)
