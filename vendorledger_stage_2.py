# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: VendorLedger
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Vendor:
    name: str
    tax_id: str
    address: str
    rating: float = 0.0
    notes: str = ""

@dataclass
class Contract:
    vendor: Vendor
    start_date: date
    end_date: date
    contract_value: float
    status: str = "active"

@dataclass
class Order:
    contract: Contract
    line_items: list = field(default_factory=list)
    order_date: date = None
    fulfillment_date: date = None
    total: float = 0.0

@dataclass
class Payment:
    order: Order
    amount: float
    payment_date: date
    method: str = ""
    status: str = "pending"

@dataclass
class PerformanceNote:
    vendor: Vendor
    date: date
    description: str
    score: float = 0.0
