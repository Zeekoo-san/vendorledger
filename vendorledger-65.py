# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: VendorLedger
import ast
import re
from collections import Counter


def merge_imports(existing, new):
    """Merge two lists of import statements, dropping obvious duplicates.

    Two imports are considered duplicates when their normalized forms match.
    Normalization strips whitespace, quotes, and collapses module paths to
    their dotted form so that equivalent imports collapse to one entry.
    """
    if not existing:
        return list(new)
    if not new:
        return list(existing)

    existing_norm = [normalize_import(item) for item in existing]
    new_norm = [normalize_import(item) for item in new]

    kept = []
    for norm in new_norm:
        if norm not in existing_norm:
            kept.append(norm)

    merged = list(existing) + kept
    return dedupe_similar(merged)


def normalize_import(statement):
    """Reduce an import statement to a comparable dotted module path.

    Handles both 'import a.b.c' and 'from a.b.c import x' forms by returning
    the module portion only. This makes semantically identical imports match
    regardless of minor formatting differences.
    """
    statement = statement.strip()
    if not statement:
        return statement

    statement = re.sub(r'#[^\n]*', '', statement).strip()
    statement = re.sub(r'"', '', statement)
    statement = re.sub(r"'", '', statement)

    if statement.startswith('from '):
        parts = statement.split()
        return parts[1] if len(parts) > 1 else ''

    if statement.startswith('import '):
        body = statement[len('import '):]
        return parse_import_body(body)

    return statement


def parse_import_body(body):
    """Extract the module path from an 'import' statement body.

    Splits on commas and semicolons, then takes the first token's module.
    Aliases and submodules are ignored for deduplication purposes.
    """
    body = re.sub(r';', ',', body)
    tokens = [t.strip() for t in body.split(',')]
    for token in tokens:
        module = re.match(r'^[\w\.]+', token)
        if module:
            return module.group(0)
    return ''


def dedupe_similar(imports):
    """Remove near-duplicate imports that differ only by trailing details.

    Imports like 'import a.b.c' and 'import a.b.c.d' are collapsed to the
    shortest form when they share a common prefix, avoiding redundant entries
    while preserving the more specific import.
    """
    if len(imports) <= 1:
        return imports

    result = []
    for imp in imports:
        base = imp.split('.')[0]
        if any(result[i].split('.')[0] == base for i in range(len(result))):
            result.append(imp.split('.')[-1])
        else:
            result.append(imp)

    return result
