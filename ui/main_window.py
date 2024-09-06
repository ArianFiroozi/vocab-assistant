from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDialog,
    QMessageBox
)

from ui.word_diplay_window import WordDisplayWindow
from ui.word_request_dialog import WordRequestDialog

from src.vocab import Vocab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vocab = self.load_vocab()

        self.setWindowTitle("Vocab Assistant")
        
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

        self.create_menu()

    def create_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        file_menu.addAction("Reset", self.reset_application)

    def load_vocab(self):
        vocab = Vocab()
        vocab.load()
        return vocab

    def show_new_words(self):
        self.show_word_request_dialog("New")

    def show_previous_words(self):
        self.show_word_request_dialog("Previous")

    def show_word_request_dialog(self, word_type):
        dialog = WordRequestDialog()
        if dialog.exec() == QDialog.Accepted:
            word_count, is_random = dialog.get_input()
            words = []
            if word_type == "New":
                words = self.vocab.get_new_words(word_count, is_random)
            else:
                words = self.vocab.get_read_words(word_count, is_random)
            self.display_words(words)

    def display_words(self, words):
        if len(words) <= 0:
            return

        self.word_display_window = WordDisplayWindow(words)
        self.word_display_window.show()

    def reset_application(self):
        reply = QMessageBox.question(self, 'Reset Application', 
                                     'Are you sure you want to reset the application?',
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.vocab.reset()

    def closeEvent(self, _):
        self.vocab.save()
