# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: VendorLedger
def tags_add(self, tag: str) -> None:
    if tag not in self.tags:
        self.tags.append(tag)

def tags_remove(self, tag: str) -> None:
    if tag in self.tags:
        self.tags.remove(tag)

def tag_summary(self, tag: str) -> dict:
    if tag not in self.tags:
        return {}
    return {
        "tag": tag,
        "count": self.tags.count(tag),
        "total": sum(self.tags),
        "avg": sum(self.tags) / len(self.tags) if self.tags else 0,
        "min": min(self.tags) if self.tags else 0,
        "max": max(self.tags) if self.tags else 0,
    }
