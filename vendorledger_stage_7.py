# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: VendorLedger
def format_contract(contract: Contract) -> str:
    lines = [f"Contract #{contract.id} - {contract.vendor_name}"]
    lines.append(f"  Status: {contract.status.value} | Amount: ${contract.amount:,.2f}")
    lines.append(f"  Start: {contract.start_date.strftime('%Y-%m-%d')} | End: {contract.end_date.strftime('%Y-%m-%d')}")
    lines.append(f"  Terms: {contract.payment_terms_months} months")
    if contract.notes:
        lines.append(f"  Notes: {contract.notes}")
    return "\n".join(lines)


def format_order(order: Order) -> str:
    lines = [f"Order #{order.id} - {order.vendor_name}"]
    lines.append(f"  Date: {order.order_date.strftime('%Y-%m-%d')} | Amount: ${order.amount:,.2f}")
    lines.append(f"  Status: {order.status.value}")
    return "\n".join(lines)


def format_payment(payment: Payment) -> str:
    lines = [f"Payment #{payment.id} - ${payment.amount:,.2f}"]
    lines.append(f"  Date: {payment.payment_date.strftime('%Y-%m-%d')} | Method: {payment.payment_method}")
    if payment.notes:
        lines.append(f"  Notes: {payment.notes}")
    return "\n".join(lines)


def format_performance(performance: Performance) -> str:
    lines = [f"Performance - {performance.vendor_name}"]
    lines.append(f"  Date: {performance.date.strftime('%Y-%m-%d')} | Score: {performance.score}/10")
    if performance.notes:
        lines.append(f"  Notes: {performance.notes}")
    return "\n".join(lines)
