# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: VendorLedger
import random
from dataclasses import dataclass, field
from datetime import date, timedelta

@dataclass
class Vendor:
    name: str
    code: str
    active: bool = True

    def __post_init__(self):
        self.created = date.today() - timedelta(days=random.randint(1, 365))

@dataclass
class Contract:
    vendor_id: int
    vendor: Vendor
    start_date: date
    end_date: date
    annual_value: float
    currency: str = "USD"
    status: str = "active"

    def __post_init__(self):
        self.created = date.today() - timedelta(days=random.randint(1, 30))
        self.renewal_date = self.end_date + timedelta(days=90)

@dataclass
class Order:
    contract_id: int
    contract: Contract
    order_number: str
    line_items: list = field(default_factory=list)

    def __post_init__(self):
        self.order_number = f"ORD-{random.randint(1000, 9999)}"
        self.created = date.today() - timedelta(days=random.randint(1, 30))

@dataclass
class Payment:
    order_id: int
    order: Order
    amount: float
    currency: str = "USD"
    paid_date: date = field(default_factory=lambda: date.today() - timedelta(days=random.randint(1, 60)))
    status: str = "completed"

@dataclass
class PerformanceNote:
    vendor_id: int
    vendor: Vendor
    note_date: date
    category: str
    description: str
    score: float

    def __post_init__(self):
        self.note_date = date.today() - timedelta(days=random.randint(1, 60))
        self.score = round(random.uniform(1.0, 5.0), 1)
