# speak2act 🎤⚡

An open-source Speech-to-Intent Agent that listens to voice commands, detects intent, and executes actions.

## 🚀 Features
- Speech recognition (ASR) using Whisper/SpeechBrain
- Intent & entity detection (spaCy / HuggingFace)
- Action executor for system tasks
- Modular repo structure for easy extension

## 📂 Repo Structure
- `src/audio/` → audio preprocessing + ASR
- `src/nlp/` → intent/entity detection
- `src/executor/` → action mapping
- `config/` → intents and settings
- `tests/` → unit tests

## 🛠️ Setup
```bash
git clone https://github.com/<your-username>/speak2act.git
cd speak2act
pip install -r requirements.txt

