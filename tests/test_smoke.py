import requests

BASE = "http://localhost:8080"

def test_health():
    r = requests.get(f"{BASE}/health", timeout=3)
    assert r.status_code == 200
    assert r.json().get("status") == "ok"
