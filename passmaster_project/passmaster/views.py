from PyQt5.QtWidgets import (
    # Import PyQt classes
    QHBoxLayout,
    QMainWindow,
    QWidget,
)

# Application's main Window (Inherits from QMainWindow class)
class Window(QMainWindow):

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Password Master")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)