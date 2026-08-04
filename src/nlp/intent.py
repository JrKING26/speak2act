def detect_intent(text: str) -> str:
    text = text.lower()
    if "remind" in text:
        return "set_reminder"
    elif "weather" in text:
        return "get_weather"
    elif "quit" in text:
        return "exit"
    else:
        return "unknown"
