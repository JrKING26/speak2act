# src/nlp/intent.py

def detect_intent(text: str) -> str:
    """
    Placeholder intent detection.
    Later we'll integrate spaCy or HuggingFace here.
    """
    if "remind" in text.lower():
        return "set_reminder"
    elif "play" in text.lower():
        return "play_music"
    elif "open" in text.lower():
        return "open_app"
    else:
        return "unknown"
