from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QScrollArea
)

from src.word import Word

class WordDisplayWindow(QWidget):
    def __init__(self, words):
        super().__init__()
        self.setWindowTitle("Words Display")

        self.words = words
        self.layout = QVBoxLayout(self)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        self.word_meanings = []
        self.word_meaning_boxes = []

        for i, word in enumerate(words):
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
            
            self.word_meanings.append(QLabel(word.meaning))
            self.word_meaning_boxes.append(QLineEdit())
            self.word_meanings[i].setVisible(False) 
            self.word_meaning_boxes[i].setVisible(False)
            self.word_meaning_boxes[i].setPlaceholderText("type new meaning")

            do_not_show_button.clicked.connect(word.do_not_show)
            show_meaning_button.clicked.connect(lambda _, index=i: self.toggle_meaning(index))
            add_meaning_button.clicked.connect(lambda _, index=i: self.toggle_meaning_box(index))
            self.word_meaning_boxes[i].textChanged.connect(lambda text, index=i: self.edit_meaning(text, index))

            word_layout.addWidget(do_not_show_button)
            word_layout.addWidget(add_meaning_button)
            word_layout.addWidget(show_meaning_button)
            
            self.scroll_layout.addLayout(word_layout)
            self.scroll_layout.addWidget(self.word_meanings[i])
            self.scroll_layout.addWidget(self.word_meaning_boxes[i])

    def toggle_meaning(self, word_index):
        self.word_meanings[word_index].setVisible(not self.word_meanings[word_index].isVisible())

    def toggle_meaning_box(self, word_index):
        self.word_meaning_boxes[word_index].setVisible(not self.word_meaning_boxes[word_index].isVisible())

    def edit_meaning(self, new_meaning, word_index):
        self.word_meanings[word_index].setText(new_meaning)
        self.words[word_index].set_meaning(new_meaning)
