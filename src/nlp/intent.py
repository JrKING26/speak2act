def detect_intent(text: str) -> str:
    if "remind" in text.lower():
        return "set_reminder"
    elif "play" in text.lower():
        return "play_music"
    elif "open" in text.lower():
        return "open_app"
    return "unknown"
