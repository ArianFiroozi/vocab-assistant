from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDialog,
)

from word_diplay_window import WordDisplayWindow
from word_request_dialog import WordRequestDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Manager")
        
        self.layout = QVBoxLayout()
        
        self.show_new_words_button = QPushButton("Show New Words", self)
        self.show_new_words_button.clicked.connect(self.show_new_words)
        self.layout.addWidget(self.show_new_words_button)
        
        self.show_previous_words_button = QPushButton("Show Previous Words", self)
        self.show_previous_words_button.clicked.connect(self.show_previous_words)
        self.layout.addWidget(self.show_previous_words_button)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def show_new_words(self):
        self.show_word_request_dialog("New")

    def show_previous_words(self):
        self.show_word_request_dialog("Previous")

    def show_word_request_dialog(self, word_type):
        dialog = WordRequestDialog()
        if dialog.exec() == QDialog.Accepted:
            word_count, is_random = dialog.get_input()
            words = [f"{word_type} Word {i+1}" for i in range(int(word_count))]
            self.display_words(words)

    def display_words(self, words):
        self.word_display_window = WordDisplayWindow(words)
        self.word_display_window.show()
