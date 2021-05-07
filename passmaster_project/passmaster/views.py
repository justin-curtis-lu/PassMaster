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

from .model import ContactsModel

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
        self.contactsModel = ContactsModel()
        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        # Full row view
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        # Create buttons
        self.addButton = QPushButton("Add...")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        # Lay out the GUI
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def deleteContact(self):
        """Delete the selected contact from the database."""
        row = self.table.currentIndex().row()
        if row < 0:
            return

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)

    def openAddDialog(self):
        """Open the Add Contact dialog."""
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addPassword(dialog.data)
            self.table.resizeColumnsToContents()

class AddDialog(QDialog):
    """Add Contact dialog."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Password")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI."""
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
                    f"You must provide a entry's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()