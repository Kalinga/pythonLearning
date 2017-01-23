#!/usr/bin/python
# coding=UTF-8

import sqlite3
import os

from  project.styleformat import heading

# Fetch the the version number of sqlite3
heading("Module 5 Assignments: 1")
print ("sqlite3.version: "), sqlite3.version
print ("sqlite3.version_info: "), sqlite3.version_info
print ("sqlite3.sqlite_version: "), sqlite3.sqlite_version
print ("sqlite3.sqlite_version_info: "), sqlite3.sqlite_version_info

heading("Module 5 Assignments: 2")
con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    table_exists = """select count(*) from sqlite_master WHERE type='table' and name='Friends'"""
    cur.execute(table_exists)
    if not cur.fetchone():
        cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
        print "The last Id of the inserted row is %d" % cur.lastrowid
    else:
        print "'Friends' Table alrady exists"

heading("Module 5 Assignments: 3")
db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print 'Need to create schema'
    print 'Creating database'
else:
    print 'Database exists, assume schema does, too.'
conn.close()


heading("Module 5 Assignments: 4")
con = sqlite3.connect('test.db')
table_exists = """select count(*) from sqlite_master WHERE type='table' and name='Cars'"""
table_create_str = """select sql from sqlite_master where tbl_name='Cars' and type='table'"""
table_info = """PRAGMA table_info(Cars)"""

with con:
    cur = con.cursor()
    cur.execute(table_exists)

    if cur.fetchone()[0]:
        cur.execute("SELECT * FROM Cars")

        for colinfo in cur.description:
            print colinfo
    else:
        cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY, Name TEXT, Price FLOAT )")
        cur.execute("INSERT INTO Cars(Name, Price) VALUES ('Benz', 100250)")
        cur.execute("INSERT INTO Cars(Name, Price) VALUES ('BMW', 134540)")
        cur.execute("INSERT INTO Cars(Name, Price) VALUES ('VW', 14640)")

    print "Query used to create Cars: ", cur.execute(table_create_str).fetchone()
    table_col_info = cur.execute(table_info).fetchall()
    print "PRAGMA Info Cars: ", table_col_info
    for col in table_col_info:
        print col[1]

    con.commit()

heading("Module 5 Assignments: 5")
cars = (
(1, 'Audi', 52642),
(2, 'Mercedes', 57127),
(3, 'Skoda', 9000),
(4, 'Volvo', 29000),
(5, 'Bentley', 350000),
(6, 'Hummer', 41400),
(7, 'Volkswagen', 21600)
)
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    print "%s Records insertion successful" % (cur.rowcount)

heading("Module 5 Assignments: 6 [Fetch inserted Records]")
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print row

heading("Module 5 Assignments: 7 [Using sqlite3 Row factory]")
con = sqlite3.connect('test.db')
with con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])


heading("Module 5 Assignments: 8")
import sys
uId = 1
uPrice = 62300
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (45678, 6))
    con.commit()
    print "Number of rows updated: %d" % cur.rowcount


heading("Module 5 Assignments: 9 [Meta data about Table]")
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute("PRAGMA table_info(Cars)")
    data = cur.fetchall()
    print data

    for d in data:
        print d[0], d[1], d[2]

heading("Module 5 Assignments: 10 [Meta data about Table]")
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description]
    rows = cur.fetchall()
    print "%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    for row in rows:
        print "%2s %-10s %s" % row

heading("Module 5 Assignments: 11 [sample csv to db]")
heading("Module 5 Assignments: 12 [Fetch all from db and display]")
heading("Module 5 Assignments: 13 [Fetch col names from db created]")