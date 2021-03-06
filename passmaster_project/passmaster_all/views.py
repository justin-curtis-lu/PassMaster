from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    # Import all  PyQt classes
    # ----------------------

    # Table view policy
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    # Window classes
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    # Add, Delete, Clear All Buttons
    QPushButton,
    # Table view for password displaying
    QTableView,
    QVBoxLayout,
    # Widget class
    QWidget
)

# Image
from PyQt5.QtGui import QPixmap

from .model import PasswordsModel

# Application's main Window (Inherits from QMainWindow class)
class Window(QMainWindow):

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Pass Master")
        self.resize(550, 250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.PasswordsModel = PasswordsModel()
        self.setupUI()

    def setupUI(self):
        """GUI Setup."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.PasswordsModel.model)
        # Full row view
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons for Add, Delete, and Clear All
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deletePassword)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearPasswords)
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def clearPasswords(self):
        """Remove all passwords from the database."""
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove all your passwords?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.PasswordsModel.clearPasswords()

    def deletePassword(self):
        """Delete the selected password from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected password?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.PasswordsModel.deletePassword(row)

    def openAddDialog(self):
        """Open the Add Password dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.PasswordsModel.addPassword(dialog.data)
            self.table.resizeColumnsToContents()

class AddDialog(QDialog):
    """Add Password dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Password")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Password dialog's GUI."""
        # Create line edits for data fields
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.userField = QLineEdit()
        self.userField.setObjectName("User")
        self.passField = QLineEdit()
        self.passField.setObjectName("Pass")
        self.urlField = QLineEdit()
        self.urlField.setObjectName("URL")
        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Name:", self.nameField)
        layout.addRow("User:", self.userField)
        layout.addRow("Pass:", self.passField)
        layout.addRow("URL:", self.urlField)
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.userField, self.passField, self.urlField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide the {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()