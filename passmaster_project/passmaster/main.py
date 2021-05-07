import sys

from PyQt5.QtWidgets import QApplication

# Database handling
from .database import createConnection
# GUI handling
from .views import Window

def main():

    app = QApplication(sys.argv)

    # Create database ( exit if not successful )
    if not createConnection("passwords.sqlite"):
        sys.exit(1)

    # Create the main window
    win = Window()
    win.show()
    # Run the event loop

    # Sys module allows application termination
    sys.exit(app.exec())