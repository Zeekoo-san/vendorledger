# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: VendorLedger
def colorize(text: str, code: str) -> str:
    """Append ANSI color codes to terminal text.

    Args:
        text: The text to colorize.
        code: ANSI escape code (e.g., '\033[31m' for red).

    Returns:
        The colorized text.
    """
    return f"{code}{text}\033[0m"
