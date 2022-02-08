import sqlite3

class Database():
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.connection = sqlite3.connect("C:/Users/amali/Downloads/sqlitestudio-3.3.3 (1)/SQLiteStudio/database")
        self.cur = self.connection.cursor()

    def setupUi(self):
