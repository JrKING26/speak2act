def execute_action(intent: str, text: str) -> str:
    if intent == "set_reminder":
        return f"Reminder set: {text}"
    elif intent == "play_music":
        return "Playing music..."
    elif intent == "open_app":
        return "Opening application..."
    return "No action available for this intent."
