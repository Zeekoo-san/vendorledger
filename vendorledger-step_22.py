# === Stage 22: Add favorite records and quick favorite listing ===
# Project: VendorLedger
class Favorite:
    def __init__(self, record, note=""):
        self.record = record
        self.note = note

    def __repr__(self):
        return f"Favorite({self.record}, note={self.note!r})"


class FavoriteRegistry:
    def __init__(self):
        self._favorites = []

    def add(self, record, note=""):
        self._favorites.append(Favorite(record, note))
        return self

    def get_favorites(self):
        return list(self._favorites)

    def clear(self):
        self._favorites.clear()

    def __len__(self):
        return len(self._favorites)


# Example usage:
# reg = FavoriteRegistry()
# reg.add(Contract("C1"), "Priority vendor").add(Contract("C2"), "Bulk orders")
# for fav in reg.get_favorites():
#     print(fav)
