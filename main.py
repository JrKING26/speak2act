import argparse

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


def verify_whisper(audio_file=None):
    asr = AudioASR()
    success = asr.verify_whisper(test_audio_file=audio_file)
    if success:
        print("Whisper verification succeeded.")
    else:
        print("Whisper verification failed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Speak2Act agent or verify Whisper.")
    parser.add_argument("--verify-whisper", nargs="?", const="", help="Verify Whisper; optionally provide an audio file path.")
    args = parser.parse_args()

    if args.verify_whisper is not None:
        audio_file = args.verify_whisper or None
        verify_whisper(audio_file=audio_file)
    else:
        run_agent()

