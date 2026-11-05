# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: VendorLedger
def reset_demo_data(db):
    if db is None:
        print("No database connection provided.")
        return
    for table in ["performance_notes", "payments", "orders", "contracts", "vendors"]:
        try:
            db.execute(f"DELETE FROM {table};")
        except Exception as exc:
            print(f"Could not reset {table}: {exc}")
    db.commit()
    print("Demo data reset complete.")
