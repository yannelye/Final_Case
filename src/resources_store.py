import json

class ResourceStore:
    def __init__(self, json_path):
        self.json_path = json_path
        with open(self.json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def query(self, zipcode=None, category=None, limit=50):
        results = self.data
        if zipcode:
            results = [r for r in results if str(r.get("zipcode")) == str(zipcode)]
        if category:
            results = [r for r in results if r.get("category") == category]
        return results[:limit]
