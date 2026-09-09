# === Stage 16: Add argparse support for the most common commands ===
# Project: VendorLedger
import argparse

def main():
    parser = argparse.ArgumentParser(description="VendorLedger CLI")
    subparsers = parser.add_subparsers(dest="command")

    # contract
    c = subparsers.add_parser("contract", help="manage contracts")
    c.add_argument("action", choices=["add", "list", "show", "status"])
    c.add_argument("--vendor", required=True, help="vendor name")
    c.add_argument("--amount", type=float, help="contract amount")
    c.add_argument("--term", default="12", help="months")

    # order
    o = subparsers.add_parser("order", help="manage orders")
    o.add_argument("action", choices=["add", "list", "status"])
    o.add_argument("--contract", required=True, help="contract id")
    o.add_argument("--quantity", type=int, help="quantity ordered")

    # payment
    p = subparsers.add_parser("payment", help="record payments")
    p.add_argument("action", choices=["add", "list", "status"])
    p.add_argument("--order", required=True, help="order id")
    p.add_argument("--amount", type=float, required=True)
    p.add_argument("--date", default=None, help="YYYY-MM-DD")

    # note
    n = subparsers.add_parser("note", help="add performance notes")
    n.add_argument("action", choices=["add", "list"])
    n.add_argument("--order", required=True, help="order id")
    n.add_argument("--text", required=True)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    print(f"[VendorLedger] command: {args.command} action: {getattr(args, 'action', None)}")

if __name__ == "__main__":
    main()
