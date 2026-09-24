# === Stage 61: Add performance timing for core list and search operations ===
# Project: VendorLedger
import time
from vendor_ledger import Ledger

ledger = Ledger()
ledger.add_contract("C1", "Acme", 10000, 2025, "Software")
ledger.add_order("C1", "O1", 3000, "2025-06-01", "License")
ledger.add_payment("O1", 2500, "2025-06-15")
ledger.add_performance_note("O1", 0.95, "Good communication")

times = {}

t0 = time.perf_counter()
_ = ledger.list_contracts()
times["list_contracts"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.list_orders()
times["list_orders"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.list_payments()
times["list_payments"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.list_performance_notes()
times["list_performance_notes"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.search_contracts("Acme")
times["search_contracts"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.search_orders("License")
times["search_orders"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.search_payments("2025-06")
times["search_payments"] = time.perf_counter() - t0

t0 = time.perf_counter()
_ = ledger.search_performance_notes("communication")
times["search_performance_notes"] = time.perf_counter() - t0

for name, elapsed in times.items():
    print(f"{name}: {elapsed*1000:.2f} ms")
