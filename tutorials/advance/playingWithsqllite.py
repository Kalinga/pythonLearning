import sqlite3

import os.path

class SqliteExample(object):
    @staticmethod
    def dbPath():
        return os.getcwd() + "/example.db"

    @classmethod
    def getConn(cls):
        print cls.dbPath()
        # sqlite3.connect(":memory:") #RAMM based data base
        return sqlite3.connect(cls.dbPath())

if __name__ == "__main__":
    dbConn = SqliteExample.getConn()
    cur = dbConn.cursor()
    print "cur: ", type(cur)

    table_creation = "CREATE TABLE if NOT EXISTS TestTable(id INTEGER PRIMARY KEY, name TEXT, phone NUMBER, email TEXT, password TEXT)"
    #table_drop = " DROP TABLE TestTable"
    table_insert = "insert into TestTable(id, name, phone) values(?,?,?)"

    cur.execute(table_creation)
    cur.executemany (table_insert, [(101, "Kalinga", 6676754654), (102, "Sonali", 6611122254)])

    # cur.execute(table_drop)

    table_fetch = "select * from TestTable"

    if cur.execute(table_fetch):
        print "Run successfully"
        for i in cur:
            print i

    cur.close()
    dbConn.commit()
    dbConn.close()