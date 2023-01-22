import sqlite3
from sqlite3 import connect, Error
from os import path, pardir

class Connection():
    db = None
    cursor = None

    def __init__(self):
        self.new_connection()

    def new_connection(self):
        newDB = False
        db_file = path.normpath("./database/KennelClub.db")
        if not path.exists(db_file):
            print("Database not found. Creating new database.")
            newDB = True
        else:
            print("Database found")

        try:
            print("Connecting...")
            self.db = connect(db_file)
            self.cursor = self.db.cursor()
            print("Connected")

            if newDB:
                self.fill_empty_db()

        except Error as e:
            print("Error connecting to database:")
            print(e)

    def fill_empty_db(self):
        sql_file = path.normpath("./database/scripts/create_db.sql")
        with open(sql_file) as f:
            script = f.read()

        self.cursor.executescript(script)
        self.push()

    def close_db(self):
        print("Disconnecting")
        self.db.close()

    def query(self, fromTable, select=[], where=None, additional=None):
        if len(select) == 0:
            columns = '*'
        else:
            columns = ', '.join(select)

        com = f"Select {columns} FROM {fromTable}"

        if where:
            com += f" WHERE {where}"

        if additional:
            com += f" {additional}"

        com += ";"
        print(com)

        self.cursor.execute(com)

        rows = self.cursor.fetchall()
        return(rows)

    def edit(self, update, where, set=[]):
        conditions = []
        for item in set:
            if int(item[1]):
                condition = f"{item[0]} = {item[1]}"
            else:
                condition = f"{item[0]} = '{item[1]}'"
            conditions.append(condition)

        condition = ', '.join(conditions)
        com = f"UPDATE {update} SET {condition} WHERE {where};"

        self.cursor.execute(com)
        self.push()
        print("Row(s) updated")

    def add(self, into, values=[]):
        columns = ', '.join(values)

        com = f"INSERT INTO {into} Values ({columns});"
        print(com)
        self.cursor.execute(com)
        self.push()
        print("Row(s) added")

    def remove(self, fromTable, where):
        com = f"DELETE FROM {fromTable} where {where}"
        self.cursor.execute(com)
        self.push()
        print("Row(s) deleted")

    def count(self, fromTable, select=None, where=None, count=None):
        if select == None:
            columns = ''
        elif len(select) == 0:
            columns = '*, '
        elif len(select) > 0:
            columns = ', '.join(select)
            columns += ', '


        com = f"SELECT {columns}COUNT({count}) FROM {fromTable}"

        if where:
            com += f" WHERE {where}"

        com += ";"
        print(com)

        self.cursor.execute(com)

        rows = self.cursor.fetchall()
        return(rows)

    def push(self):
        print("Updating Table")
        self.db.commit()
