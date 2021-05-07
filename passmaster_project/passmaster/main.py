import sys

from PyQt5.QtWidgets import QApplication

from .views import Window

def main():

    app = QApplication(sys.argv)
    # Create the main window
    win = Window()
    win.show()
    # Run the event loop

    # Sys module allows application termination
    sys.exit(app.exec())