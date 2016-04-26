# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:52:57 2016

@author: greg.simpson
"""

#1
import sqlite3
con = sqlite3.connect('test.db')
with con:
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data

#2
import sqlite3
con = sqlite3.connect('new_db')
with con:
    cur = con.cursor()
    #cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")
    print "The last Id of the inserted row is %d" % cur.lastrowid

#3
import os
import sqlite3
db_filename = 'todo.db'
db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
if db_is_new:
    print 'Need to create schema'
    print 'Creating database'
else:
    print 'Database exists, assume schema does, too.'
conn.close()

#4
import sqlite3 as lite 
import sys
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    #cur.execute("SELECT * FROM Cars")
    #for colinfo in cur.description:
    #    print colinfo


#5
import sqlite3 as lite
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127), 
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000), 
    (6, 'Hummer', 41400), 
    (7, 'Volkswagen', 21600)
)
con = lite.connect('test.db') 
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)") 
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)

#6
import sqlite3 as lite
con = lite.connect('test.db') 
with con:
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars") 
    rows = cur.fetchall()
    for row in rows:
        print row

#7
import sqlite3 as lite
con = lite.connect('test.db')
with con:
    con.row_factory = lite.Row
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars") 
    rows = cur.fetchall()
    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

#8
import sqlite3 as lite 
import sys
uId = 1
uPrice = 62300
con = lite.connect('test.db') 
with con:
    cur = con.cursor()
    cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId)) 
    con.commit()
    print "Number of rows updated: %d" % cur.rowcount

#9
import sqlite3 as lite
con = lite.connect('test.db') 
with con:
    cur = con.cursor() 
    cur.execute("PRAGMA table_info(Cars)")
    data = cur.fetchall()
    
    for d in data:
        print d[0], d[1], d[2]

#10
import sqlite3 as lite
con = lite.connect('test.db') 
with con:
    cur = con.cursor()
    cur.execute('SELECT * FROM Cars')
    col_names = [cn[0] for cn in cur.description] 
    rows = cur.fetchall()
    print "\n\n%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    for row in rows:
        print "%2s %-10s %s" % row

#11
import sqlite3 as lite
import csv
f = open('Downloads/sample-storedata.csv')
input = csv.reader(f)
conn = lite.connect('mytestdb')
curse = conn.cursor()
curse.execute("DROP TABLE IF EXISTS store")
curse.execute('CREATE TABLE store (Lat REAL(15), Long REAL(15), Phone VARCHAR(20), Address VARCHAR(60))')
for item in input:
    print item
    curse.execute('INSERT INTO store VALUES (?,?,?,?)',item)
curse.close()

    
#12 fetch all of the new rows
print("#12")
import sqlite3 as lite
conn = lite.connect('mytestdb')
curse = conn.cursor() 
curse.execute('SELECT * FROM store;') 
rows = curse.fetchall()
for row in rows:
    print row


#13. Fetch the column names of the store table created. Solution
print("#13")
import sqlite3 as lite
conn = lite.connect('mytestdb')
curse = conn.cursor() 
curse.execute('SELECT * FROM store;') 
rows = curse.description
for row in rows:
    print row


