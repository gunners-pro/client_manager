from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSize, QPropertyAnimation, QEasingCurve
from ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manager Client")
        self.setMinimumSize(QSize(1024, 768))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.expanded = True

        self.animation = QPropertyAnimation(self.ui.sidebar, b"maximumWidth")
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.ui.toggleSidebar.clicked.connect(self.toggle_sidebar)

    def toggle_sidebar(self):
        if self.expanded:
            self.animation.setStartValue(self.ui.sidebar.width())
            self.animation.setEndValue(0)
        else:
            self.animation.setStartValue(self.ui.sidebar.width())
            self.animation.setEndValue(200)
        self.animation.start()
        self.expanded = not self.expanded