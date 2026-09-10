# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: VendorLedger
import os
import sys

def dry_run_mode():
    """Sets the DRY_RUN environment variable to enable dry-run behavior for commands that mutate state."""
    os.environ['DRY_RUN'] = 'true'
    print("Dry-run mode enabled. No actual state changes will be made.")

def dry_run_mode_off():
    """Disables dry-run mode by clearing the DRY_RUN environment variable."""
    os.environ.pop('DRY_RUN', None)
    print("Dry-run mode disabled. Commands will now make actual state changes.")

def is_dry_run():
    """Checks if dry-run mode is currently enabled by looking at the DRY_RUN environment variable."""
    return os.environ.get('DRY_RUN', '').lower() == 'true'

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == '--on':
            dry_run_mode()
        elif sys.argv[1] == '--off':
            dry_run_mode_off()
        else:
            print(f"Usage: python script.py [--on|--off]")
    else:
        print("Dry-run mode is currently:", "enabled" if is_dry_run() else "disabled")
