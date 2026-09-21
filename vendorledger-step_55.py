# === Stage 55: Add a setting to disable colorized output ===
# Project: VendorLedger
import os

os.environ.setdefault('VENDORLEDGER_DISABLE_COLOR', '0')

class ColorConfig:
    def __init__(self):
        self._disabled = os.environ.get('VENDORLEDGER_DISABLE_COLOR', '0') == '1'

    def is_color_enabled(self):
        return not self._disabled

    def enable_color(self):
        self._disabled = False

    def disable_color(self):
        self._disabled = True

    def __repr__(self):
        return f'<ColorConfig disabled={self._disabled}>'
