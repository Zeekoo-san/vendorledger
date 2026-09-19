# === Stage 46: Add a schema version field and migration helper ===
# Project: VendorLedger
import json, os, glob
from pathlib import Path

SCHEMA_VERSION = 3
MIGRATION_LOG = "schema_migrations.json"

def ensure_schema_migrations():
    if not os.path.exists(MIGRATION_LOG):
        with open(MIGRATION_LOG, "w") as f:
            json.dump({"applied": [], "pending": []}, f, indent=2)

def get_current_applied():
    ensure_schema_migrations()
    with open(MIGRATION_LOG) as f:
        return json.load(f)["applied"]

def apply_migration(migration_fn, name, description):
    applied = get_current_applied()
    if name in applied:
        print(f"Migration '{name}' already applied, skipping.")
        return
    print(f"Applying migration: {name} - {description}")
    migration_fn()
    with open(MIGRATION_LOG, "w") as f:
        json.dump({"applied": applied + [name], "pending": []}, f, indent=2)
    print(f"Migration '{name}' applied successfully.")

def migrate_add_schema_version():
    base = Path(__file__).parent
    for f in base.rglob("*.py"):
        if "VendorLedger" not in f.read_text():
            continue
        content = f.read_text()
        if "SCHEMA_VERSION" in content:
            continue
        f.write_text(content + "\n\nSCHEMA_VERSION = 3\n")
