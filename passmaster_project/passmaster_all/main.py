import sys

from PyQt5.QtWidgets import QApplication

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

# Database handling
from .database import createConnection
# GUI handling
from .views import Window

def main():

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))

    app.setStyle("Fusion")

    # Dark mode Palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    app.setApplicationName("Pass Master")

    # Create database ( exit if not successful )
    if not createConnection("passwords.sqlite"):
        sys.exit(1)

    # Create the main window
    win = Window()

    win.show()
    # Run the event loop

    # Sys module allows application termination
    sys.exit(app.exec())