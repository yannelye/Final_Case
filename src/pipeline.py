import csv
import json
import os

def run_csv_to_json(csv_path, json_out):
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            r["zipcode"] = r.get("zipcode", "").strip()
            r["category"] = r.get("category", "").strip()
            rows.append(r)
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(rows)} resources to {json_out}")

if __name__ == "__main__":
    BASE = os.getenv("DATA_PATH", "/app/assets")
    csv_path = os.path.join(BASE, "sample_resources.csv")
    out = os.path.join(BASE, "resources_clean.json")
    run_csv_to_json(csv_path, out)
