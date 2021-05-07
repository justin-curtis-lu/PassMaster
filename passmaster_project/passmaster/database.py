from PyQt5.QtWidgets import QMessageBox
# Import SQL modules to use with sql
from PyQt5.QtSql import QSqlDatabase, QSqlQuery



def _createContactsTable():
    """Create the contacts table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            user VARCHAR(40) NOT NULL,
            pass VARCHAR(50),
            URL VARCHAR(40) NOT NULL
        )
        """
    )

def createConnection(databaseName):
    """Create and open a database connection."""

    # Create connection using driver
    connection = QSqlDatabase.addDatabase("QSQLITE")

    # name data base
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    _createContactsTable()
    return True