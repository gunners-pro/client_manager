from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manager Client")
        self.setMinimumSize(QSize(1024, 768))