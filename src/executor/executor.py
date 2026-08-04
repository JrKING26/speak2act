def execute_action(intent: str, text: str) -> str:
    if intent == "set_reminder":
        return f"Reminder set: {text}"
    elif intent == "get_weather":
        return "Today's weather is sunny ☀️"
    elif intent == "exit":
        return "Goodbye 👋"
    else:
        return "Sorry, I didn’t understand."
