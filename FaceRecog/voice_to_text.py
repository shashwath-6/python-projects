import sys
import json
import requests
import pyttsx3
import speech_recognition as sr

from PyQt5.QtCore import Qt, QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit,
    QLineEdit, QPushButton, QHBoxLayout
)

# Thread for voice input
class VoiceRecognitionThread(QThread):
    recognized = pyqtSignal(str)
    error = pyqtSignal(str)

    def run(self):
        recognizer = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = recognizer.recognize_google(audio)
                self.recognized.emit(text)
        except sr.UnknownValueError:
            self.error.emit("❌ Could not understand the audio.")
        except sr.RequestError:
            self.error.emit("❌ Could not connect to Google Speech API.")
        except Exception as e:
            self.error.emit(f"❌ Mic error: {e}")


# TTS in a thread-safe way
class TTSWorker(QThread):
    def __init__(self, text, voice_id):
        super().__init__()
        self.text = text
        self.voice_id = voice_id

    def run(self):
        engine = pyttsx3.init()
        engine.setProperty('rate', 160)
        engine.setProperty('voice', self.voice_id)
        engine.say(self.text)
        engine.runAndWait()


class MiniVoiceChatBot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Voice ChatBot")
        self.setGeometry(100, 100, 500, 600)

        # Set up engine once to get voice ID
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        self.voice_id = voices[1].id if len(voices) > 1 else voices[0].id  # Use 2nd or fallback to 1st
        del engine  # We'll re-init engine in each TTSWorker thread

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        layout.addWidget(self.chat_area)

        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type here or use mic...")
        self.input_field.returnPressed.connect(self.handle_send)

        self.mic_button = QPushButton("🎤")
        self.mic_button.clicked.connect(self.handle_voice_input)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.mic_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def handle_send(self):
        prompt = self.input_field.text().strip()
        if not prompt:
            return
        self.chat_area.append(f"<b>You:</b> {prompt}")
        self.input_field.clear()
        self.chat_with_ollama(prompt)

    def handle_voice_input(self):
        self.chat_area.append("🎙️ <i>Listening...</i>")
        self.voice_thread = VoiceRecognitionThread()
        self.voice_thread.recognized.connect(self.process_voice_input)
        self.voice_thread.error.connect(self.process_voice_error)
        self.voice_thread.start()

    def process_voice_input(self, prompt):
        self.chat_area.append(f"<b>You (Mic):</b> {prompt}")
        self.chat_with_ollama(prompt)

    def process_voice_error(self, message):
        self.chat_area.append(message)

    def chat_with_ollama(self, prompt):
        reply = self.ask_ollama(prompt)
        self.chat_area.append(f"<b>Bot:</b> {reply}")
        self.speak(reply)

    def ask_ollama(self, prompt):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                headers={"Content-Type": "application/json"},
                data=json.dumps({
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                })
            )
            if response.status_code == 200:
                return response.json().get("response", "").strip()
            else:
                return f"[HTTP {response.status_code}] {response.text}"
        except Exception as e:
            return f"[Connection Error]: {str(e)}"

    def speak(self, text):
        self.tts_thread = TTSWorker(text, self.voice_id)
        self.tts_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MiniVoiceChatBot()
    window.show()
    sys.exit(app.exec_())
