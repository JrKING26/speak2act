# src/executor/executor.py

def execute_action(intent: str, text: str) -> str:
    """
    Placeholder executor function.
    Later we'll integrate system calls or APIs here.
    """
    if intent == "set_reminder":
        return f"Reminder set: {text}"
    elif intent == "play_music":
        return "Playing music..."
    elif intent == "open_app":
        return "Opening application..."
    else:
        return "No action available for this intent."
