import os
import json
import logging
from flask import Flask, request, jsonify
from resources_store import ResourceStore
from translations import translate_to_spanish_simplified, extract_key_actions

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = Flask(__name__)

DATA_PATH = os.getenv("DATA_PATH", "/app/assets")
STORE_FILE = os.path.join(DATA_PATH, "resources_clean.json")
RIGHTS_FILE = os.path.join(DATA_PATH, "rights_snippets.json")

if not os.path.exists(STORE_FILE):
    try:
        import pipeline
        pipeline.run_csv_to_json(os.path.join(DATA_PATH, "sample_resources.csv"), STORE_FILE)
    except Exception as e:
        logging.error("Could not run pipeline: %s", e)

store = ResourceStore(STORE_FILE)

with open(RIGHTS_FILE, "r", encoding="utf-8") as f:
    RIGHTS = json.load(f)

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/resources")
def resources():
    zipcode = request.args.get("zipcode")
    category = request.args.get("category")
    limit = int(request.args.get("limit", 50))
    logging.info("Resource lookup zipcode=%s category=%s", zipcode, category)
    results = store.query(zipcode=zipcode, category=category, limit=limit)
    return jsonify({"count": len(results), "resources": results})

@app.route("/rights")
def rights():
    topic = request.args.get("topic")
    if topic:
        filtered = [r for r in RIGHTS if topic.lower() in r["topic"].lower()]
    else:
        filtered = RIGHTS
    return jsonify({"count": len(filtered), "rights": filtered})

@app.route("/translate", methods=["POST"])
def translate():
    body = request.get_json() or {}
    text = body.get("text", "")
    if not text:
        return jsonify({"error": "provide 'text' in request body"}), 400
    logging.info("Translate request length=%d", len(text))
    simplified_spanish = translate_to_spanish_simplified(text)
    actions = extract_key_actions(text)
    return jsonify({
        "original": text,
        "spanish": simplified_spanish,
        "actions": actions
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
