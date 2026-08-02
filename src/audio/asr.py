import speech_recognition as sr
import whisper


class AudioASR:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
        self.recognizer.energy_threshold = 300
        self.microphone = sr.Microphone()
        self.whisper_model = whisper.load_model("base")

    def _listen(self, timeout=5, phrase_time_limit=10):
        with self.microphone as source:
            print("🎙️ Listening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            return self.recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit,
            )

    def transcribe_google(self, timeout=5, phrase_time_limit=10):
        try:
            audio = self._listen(timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = self.recognizer.recognize_google(audio, language="en-US")
            return text.strip()
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout window.")
            return None
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
            return None
        except sr.RequestError as exc:
            print(f"Could not request results from Google Speech Recognition: {exc}")
            return None
        except Exception as exc:
            print(f"Google transcription failed: {exc}")
            return None

    def transcribe_whisper(self, filename="fallback.wav", timeout=5, phrase_time_limit=10):
        try:
            audio = self._listen(timeout=timeout, phrase_time_limit=phrase_time_limit)
            with open(filename, "wb") as f:
                f.write(audio.get_wav_data())
            result = self.whisper_model.transcribe(filename)
            return result.get("text", "").strip()
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout window.")
            return None
        except Exception as exc:
            print(f"Whisper transcription failed: {exc}")
            return None

    def transcribe(self):
        text = self.transcribe_google()
        if text:
            return text

        text = self.transcribe_whisper()
        if text:
            return text

        return ""
