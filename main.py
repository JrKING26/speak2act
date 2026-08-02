from src.audio.asr import AudioASR
from src.nlp.intent import detect_intent
from src.executor.executor import execute_action

def run_agent():
    asr = AudioASR()
    text = asr.transcribe()   # Google first, Whisper fallback
    print("You said:", text)

    # Step 2: NLP intent detection
    intent = detect_intent(text)
    print("Detected intent:", intent)

    # Step 3: Execute action
    result = execute_action(intent, text)
    print("Agent:", result)

if __name__ == "__main__":
    run_agent()
