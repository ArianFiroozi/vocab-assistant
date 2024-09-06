from PySide6.QtWidgets import (
    QDialog,
    QLineEdit,
    QCheckBox,
    QFormLayout,
    QDialogButtonBox,
)

class WordRequestDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Request")
        
        self.layout = QFormLayout(self)
        
        self.word_count_input = QLineEdit(self)
        self.layout.addRow("Number of Words:", self.word_count_input)
        
        self.random_checkbox = QCheckBox("Random Words", self)
        self.layout.addRow(self.random_checkbox)
        
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)
        
        self.layout.addRow(self.button_box)

    def get_input(self):
        return int(self.word_count_input.text()), self.random_checkbox.isChecked()
