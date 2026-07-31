# src/cli.py

from src.service.audio_service import transcribe_audio
from src.service.intent_detection import detect_intent
from src.service.executor import execute_action

def run_cli():
    """
    Simple CLI loop for testing the pipeline.
    """
    print("Welcome to Speak2Act CLI!")
    while True:
        text = input("You: ")
        if text.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Pipeline: text -> intent -> action
        intent = detect_intent(text)
        result = execute_action(intent, text)
        print(f"Bot: {result}")

if __name__ == "__main__":
    run_cli()
