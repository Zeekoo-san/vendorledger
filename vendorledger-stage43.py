# === Stage 43: Add CSV import for the primary record type ===
# Project: VendorLedger
def import_contracts_from_csv(csv_path: str) -> list[Contract]:
    """Read contracts from a CSV file.

    Expected columns: vendor_id, vendor_name, contract_type, value, start_date, end_date.
    Returns a list of Contract objects.
    """
    import csv
    from datetime import date

    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        contracts = []
        for row in reader:
            vendor_id = int(row["vendor_id"])
            vendor_name = row["vendor_name"]
            contract_type = row["contract_type"]
            value = int(row["value"])
            start_date = date.fromisoformat(row["start_date"])
            end_date = date.fromisoformat(row["end_date"])
            contract = Contract(
                vendor_id=vendor_id,
                vendor_name=vendor_name,
                contract_type=contract_type,
                value=value,
                start_date=start_date,
                end_date=end_date,
            )
            contracts.append(contract)
    return contracts
