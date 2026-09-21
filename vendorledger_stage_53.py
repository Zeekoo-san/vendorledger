# === Stage 53: Add command help text and usage examples ===
# Project: VendorLedger
def print_help():
    """Print command help text and usage examples for VendorLedger."""
    print("VendorLedger - Vendor Management Ledger")
    print("=" * 40)
    print("\nUsage Examples:")
    print("  python vendor_ledger.py --contract V-001")
    print("  python vendor_ledger.py --order O-100")
    print("  python vendor_ledger.py --payment P-001")
    print("  python vendor_ledger.py --performance V-001")
    print("\nCommands:")
    print("  --contract <id>     View contract details")
    print("  --order <id>        View order details")
    print("  --payment <id>      View payment details")
    print("  --performance <id>  View performance notes")
    print("  --help              Show this help message")
