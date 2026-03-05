import re

BANNED_KEYWORDS = [
    "sex", "drugs", "weapon", "bomb", "politics"
]

def validate_input(text):
    for word in BANNED_KEYWORDS:
        if word in text.lower():
            return False
    return True

def validate_output(text):
    if re.search(r"\bmg\b|\bdosage\b|\bprescribe\b", text.lower()):
        return False
    return True