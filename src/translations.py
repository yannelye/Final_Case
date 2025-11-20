import re

PHRASEBOOK = {
    "evacuate": "evacuar",
    "shelter": "refugio",
    "evacuation": "evacuación",
    "police": "la policía",
    "do not": "no",
    "don't": "no",
    "call 911": "llame al 911",
    "medical attention": "atención médica",
    "immigration": "inmigración",
    "legal assistance": "asistencia legal",
    "food bank": "banco de alimentos",
    "appointment": "cita",
    "free": "gratuito"
}

def translate_to_spanish_simplified(text):
    text = text.strip()
    low = text.lower()
    for en, es in PHRASEBOOK.items():
        low = re.sub(r"\\b" + re.escape(en) + r"\\b", es, low)
    sentences = re.split(r"[.!?]+", low)
    simple = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        s = s.capitalize()
        simple.append(s)
    joined = ". ".join(simple)
    if joined and not joined.endswith("."):
        joined += "."
    return "Mensaje en español (versión accesible): " + joined

def extract_key_actions(text):
    sentences = re.split(r"[.!?]+", text)
    actions = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if re.search(r"\\b(call|go to|evacuate|go|stay|gather|leave|seek|ask for|apply|bring)\\b", s.lower()):
            actions.append(s.strip())
        if re.match(r"^[A-Z][a-z]+\\s", s) and s.split()[0].lower() in ("leave", "stay", "call", "go"):
            actions.append(s.strip())
    seen = []
    for a in actions:
        if a not in seen:
            seen.append(a)
    return seen[:6]
