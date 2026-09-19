# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: VendorLedger
def run_demo():
    ledger = VendorLedger()
    vendor = Vendor(name="Acme Corp", tier="gold")
    contract = Contract(
        vendor=vendor,
        start="2026-01-01",
        end="2026-12-31",
        annual_amount=120000,
        currency="USD",
    )
    ledger.add_contract(contract)

    order = Order(
        contract=contract,
        quantity=50,
        unit_price=100,
        status="pending",
    )
    ledger.add_order(order)

    payment = Payment(
        order=order,
        amount=5000,
        method="bank_transfer",
        status="completed",
    )
    ledger.add_payment(payment)

    note = PerformanceNote(
        vendor=vendor,
        score=8.5,
        comment="On-time delivery, good quality",
    )
    ledger.add_note(note)

    print("Demo scenario executed:")
    print(f"  Vendor: {vendor.name} ({vendor.tier})")
    print(f"  Contract: {contract.annual_amount} {contract.currency}")
    print(f"  Order: {order.quantity} units @ {order.unit_price}")
    print(f"  Payment: {payment.amount} {payment.method}")
    print(f"  Note: {note.comment} (score {note.score})")


run_demo()
