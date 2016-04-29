"""
Created on Tue Apr 26 11:52:57 2016

@author: greg.simpson
# -*- coding: utf-8 -*-
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
    print "\n\n%s %-10s %s" % (col_names[0], col_names[1], col_names[2])
    rows = cur.fetchall()
    for row in rows:
        print "%2s %-10s %s" % row

#11
print("#11")
import sqlite3 as lite
import csv
f = open('Downloads/edureka/sample-storedata.csv')
input = csv.reader(f)
conn = lite.connect('mytestdb')
curse = conn.cursor()
curse.execute("DROP TABLE IF EXISTS store")
curse.execute('CREATE TABLE store (Lat REAL(15), Long REAL(15), Phone VARCHAR(20), Address VARCHAR(60))')
for item in input:
    #print item
    curse.execute('INSERT INTO store VALUES (?,?,?,?)',item)
    print(item[0], item[1],item[2],item[3])
conn.commit()
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
    print row[0]


#word counter
print("\n\nWord Counter")
def word_count(string):
    print("Counting words in : " + string)
    my_string = string.lower().split()
    my_dict = {}
    for item in my_string:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1
    print(my_dict)

target_string="I am that I am"
word_count(target_string)
word_count(target_string)
target_string="once upon a time in an island far away"

#anagram 2
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        print (alist1[pos] )
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
            print ("\n" + str(pos))
            #print (alist1[pos] + ":" + alist2[pos])
        else:
            matches = False

    return matches

print("anagram2 " + str(anagramSolution2('abcde','edcba')) )
print("anagram2 " + str(anagramSolution2('lmnop','ploxym')) )


# anagram finder
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):        
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
        print ("\n" + str(pos))

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

#print("anagram4 " + str(anagramSolution4('apple','pleap')))
#print("anagram4 " + str(anagramSolution4('bubba','stopsign')))


# file word count
#!/usr/bin/python
print ("\n\nWord Count")
file=open("SampleTextFile.txt","r+")
wordcount={}
gjs_totalwords = 0
for word in file.read().lower().split():
    gjs_totalwords += 1
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
file.close()
#for item in wordcount.items(): print("GJS {}\t{}".format(*item))
print("Words read : " + str(gjs_totalwords) )
 
#wordcount.sort()
#for k,v in wordcount.items():
#    print k, v

import collections
from collections import OrderedDict
from collections import Counter
words_count = collections.Counter(wordcount) #Count the occurrence of each word

#print("words_count: " + str(words_count.most_common()))    
#print("words_count: " + str(words_count))    
#print("words_count: " + str(OrderedDict(words_count.most_common() )))

z = OrderedDict( words_count.most_common() )
#for item in z.items()[::-1]:
   ## operate on item
    ##print(item)
    #print("GJS2 !!! {}\t{}".format(*item))
print ("\nNumber of distinct words_count : " + str(len(words_count) ))
#print ("XXXX Number of distinct wordcount : " + str(len(wordcount) ))
print("Total words : " + str( sum (z.values() )) )
#print("Mean word occurance : " + str( (sum(z.values() ))/len(words_count) )) 
print("Mean word occurance : " + str( (sum(z.values() ))/float(len(words_count) )) )

#print("Mean word occurance : " + str( sum(z.values()) /  len(z.keys())))


#http://stackoverflow.com/questions/29198530/displaying-both-modes-in-a-bimodal-distribution
#from collections import Counter
from itertools import takewhile
counter = Counter(wordcount)
if counter:
    mostCommon = counter.most_common()
    maxCount = mostCommon[0][1]
    modes = [t[0] for t in takewhile(lambda x: x[1] == maxCount, mostCommon)]
print ("Mode(s) is/are : " + str(modes))
    
    
    


#count number of sentences
print ("\n\nSentence Counting")
file=open("SampleTextFile.txt","r+")
sentenceCount=0
for word in file.read().split('.'):

    if (word <> ''):
        sentenceCount +=1
        #print("\n\nsentence: " + word)
print ("sentenceCount : " + str(sentenceCount))
file.close()


# change to return
print ("\n\nMaking Change")
#amount=int(input("Please enter the change to be given"))
amount=83
endAmount=amount

coins=[50,25,10,5,1]
listOfCoins=["fifty" ,"twenty five", "ten", "five",  "one"]
change = []

for coin in coins:
    holdingAmount=amount
    amount=amount//coin
    change.append(amount)
    amount=holdingAmount%coin

print("The minimum coinage to return from " ,endAmount, " is as follows")
for i in range(len(coins)):
  print("There's " , change[i] ,"....",  listOfCoins[i] , " pieces in your change" )

# another version of making change - single line output
#amount = int(input( "Please enter amount in pence" ))
amount=72
# math floor of 50
fifty = amount // 50
# mod of 50 and floor of 20
twenty = amount % 50 // 20
# mod of 50 and 20 and floor of 10
ten = amount % 50 % 20 // 10
# mod of 50 , 20 and 10 and floor of 5
# mod of 50 , 20 , 10 and 5 and floor of 2
five = amount % 50 % 20 % 10 // 5
two = amount % 50 % 20 % 10 % 5 // 2
# mod of 50 , 20 , 10 , 5 and 2 and floor of 1
one = amount % 50 % 20 % 10 % 5 % 2 //1

print("50p>>> " , fifty , " 20p>>> " , twenty , " 10p>>> " , ten , " 5p>>> " , five , " 2p>>> " , two , " 1p>>> " , one )

