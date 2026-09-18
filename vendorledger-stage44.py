# === Stage 44: Add backup creation for the data file ===
# Project: VendorLedger
import os
import shutil
from datetime import datetime

def create_backup(source_path, backup_dir=None):
    """Create a timestamped backup of the data file."""
    if backup_dir is None:
        backup_dir = os.path.join(os.path.dirname(source_path), "backups")
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, os.path.basename(source_path) + f".backup_{timestamp}")
    shutil.copy2(source_path, backup_path)
    return backup_path
