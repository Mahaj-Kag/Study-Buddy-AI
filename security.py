import re

def is_injection(text: str) -> bool:
    patterns = [
        "ignore previous instructions",
        "bypass",
        "system prompt",
        "jailbreak",
        "reveal hidden",
    ]
    return any(p in text.lower() for p in patterns)


def redact_pii(text: str) -> str:
    text = re.sub(r"\b[\w\.-]+@[\w\.-]+\.\w+\b", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b\d{12,19}\b", "[REDACTED_CARD]", text)
    return text