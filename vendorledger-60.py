# === Stage 60: Add saved views for frequently used filters ===
# Project: VendorLedger
class SavedView:
    def __init__(self, name, query, filters):
        self.name = name
        self.query = query
        self.filters = filters

    def to_dict(self):
        return {"name": self.name, "query": self.query, "filters": self.filters}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["query"], data["filters"])

    def display(self):
        return f"Saved View: {self.name}\nFilters: {self.filters}\nQuery: {self.query}"


class SavedViewManager:
    def __init__(self):
        self.views = []

    def add_view(self, view):
        self.views.append(view)
        print(f"Saved view '{view.name}' added.")

    def get_view(self, name):
        for view in self.views:
            if view.name == name:
                return view
        return None

    def delete_view(self, name):
        self.views = [v for v in self.views if v.name != name]
        print(f"Saved view '{name}' deleted.")

    def list_views(self):
        return [v.display() for v in self.views]


if __name__ == "__main__":
    manager = SavedViewManager()
    manager.add_view(SavedView("Active Contracts", "SELECT * FROM contracts WHERE status='active'", {"status": "active"}))
    manager.add_view(SavedView("Pending Payments", "SELECT * FROM payments WHERE status='pending'", {"status": "pending"}))
    print("\nSaved Views:\n")
    for view in manager.list_views():
        print(view)
