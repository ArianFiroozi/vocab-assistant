import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from src.vocab import Vocab 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
