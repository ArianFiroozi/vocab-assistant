from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
)

from src.word import Word

class WordDisplayWindow(QWidget):
    def __init__(self, words):
        super().__init__()
        self.setWindowTitle("Words Display")
        
        self.layout = QVBoxLayout(self)
        
        for word in words:
            word_layout = QHBoxLayout()
            word_label = QLabel(word.text)
            word_layout.addWidget(word_label)
            
            do_not_show_button = QPushButton()
            do_not_show_button.setIcon(QIcon("ui/icons/do_not_show.png"))
            do_not_show_button.setToolTip("Do Not Show Again")
            
            add_meaning_button = QPushButton()
            add_meaning_button.setIcon(QIcon("ui/icons/add_meaning.png"))
            add_meaning_button.setToolTip("Add Meaning")
            
            show_meaning_button = QPushButton()
            show_meaning_button.setIcon(QIcon("ui/icons/show_meaning.png"))
            show_meaning_button.setToolTip("Show Meaning")

            do_not_show_button.clicked.connect(word.do_not_show)
            do_not_show_button.clicked.connect(word.do_not_show)
            
            word_layout.addWidget(do_not_show_button)
            word_layout.addWidget(add_meaning_button)
            word_layout.addWidget(show_meaning_button)
            
            self.layout.addLayout(word_layout)
