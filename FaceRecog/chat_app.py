# chat_app.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import requests
import sys
import json

class ChatBotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TEXT ASSISTANT")
        self.setGeometry(100, 100, 600, 500)

        # Layout and widgets
        layout = QVBoxLayout()
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Ask me anything...")
        self.input_field.returnPressed.connect(self.handle_send)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.handle_send)

        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

    def handle_send(self):
        question = self.input_field.text().strip()
        if not question:
            return
        self.chat_area.append(f"You: {question}")
        self.input_field.clear()
        response = self.ask_llama3(question)
        self.chat_area.append(f"Bot: {response}\n")

    def ask_llama3(self, prompt):
        try:
            url = "http://localhost:11434/api/generate"
            headers = {"Content-Type": "application/json"}
            payload = {
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
            res = requests.post(url, headers=headers, data=json.dumps(payload))
            if res.status_code == 200:
                result = res.json()
                return result.get("response", "").strip()
            else:
                return f"[Error]: HTTP {res.status_code} — {res.text}"
        except Exception as e:
            return f"[Error]: {str(e)}"

# App start
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBotUI()
    window.show()
    sys.exit(app.exec_())