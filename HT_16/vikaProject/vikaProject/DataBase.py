import sqlite3


class DataBase(object):
    db = sqlite3.connect("DB.db")
    cursor = db.cursor()

    def createTable(self, date):
        tableName = f"_{date[0]}_{date[1]}_{date[2]}"
        query = f"DROP TABLE IF EXISTS {tableName}"
        self.cursor.execute(query)
        self.db.commit()
        query = f"CREATE TABLE {tableName}(ID integer PRIMARY KEY AUTOINCREMENT NOT NULL, TITLE TEXT, NEWSDESCRIPTION TEXT, TAGS TEXT, URL TEXT)"
        self.cursor.execute(query)
        self.db.commit()

    def addData(self, date, newsTuple):
        tableName = f"_{date[0]}_{date[1]}_{date[2]}"
        query = f"INSERT INTO {tableName}(TITLE, NEWSDESCRIPTION, TAGS, URL) VALUES(?, ?, ?, ?)"
        self.cursor.execute(query, newsTuple)
        self.db.commit()

    def closeConnection(self):
        self.db.close()

# d = DataBase()
# d.createTable("17.01.1111")
# d.addData("17.01.1111", ("sfdsfds2dd", "d", "f", "dsg"))
