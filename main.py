# main.py

from src.service.audio_service import transcribe_audio
from src.service.intent_detection import detect_intent
from src.service.executor import execute_action

def main():
    """
    End-to-end pipeline:
    speech -> text -> intent -> action
    """
    print("=== Speak2Act Demo ===")

    # For now, simulate audio input with a file path
    file_path = "sample.wav"

    # Step 1: Speech to text
    text = transcribe_audio(file_path)
    print(f"[ASR] Transcribed: {text}")

    # Step 2: Text to intent
    intent = detect_intent(text)
    print(f"[NLP] Detected intent: {intent}")

    # Step 3: Intent to action
    result = execute_action(intent, text)
    print(f"[Executor] Result: {result}")

if __name__ == "__main__":
    main()
