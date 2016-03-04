#!/usr/bin/env python3
#author   :  Pavani Krishna Goutham Baru(paba6303@colorado.edu)
#name     :  file1.py
#purpose  :  To take an abbreviation as an argument and print the planet name
#date     :  2015.11.10
#version  :  3.4.3
import sqlite3
import os
import sys
if(len(sys.argv)!=2):#Checks for the number of arguments
    print("Please enter the correct number of arguments")
    sys.exit()
if(not(os.path.isfile(sys.argv[0]))):#checks for the file
    print("File not found")
    sys.exit()
if(not(os.path.isfile('statedb.sql3'))):#checks for the database file
    print("NO such database")
    sys.exit()

else:
    
    db = sqlite3.connect('statedb.sql3')
    db.row_factory=sqlite3.Row
def insert(db,Id,State,abbr):#function for inserting values
    query="insert into Cars4(Id,State,abbr)values(?,?,?)"
    t=(Id,State,abbr,)
    cursor=db.cursor()
    cursor.execute(query,t)
    db.commit()
def queryresults(db,abbr):#function for checking the abbreviation and printin the state name
    try:
        query="select Id,State,abbr from Cars4 where abbr=?"
        t=(abbr,)
        cursor=db.cursor()
        cursor.execute(query,t)
        rows=cursor.fetchall()
        if(not rows):
            print("No such state")
            sys.exit()
        for row in rows:
            print("The name of the state is"+str(" ")+row[1])
    except sqlite3.OperationalError:
        print("No such table")
queryresults(db,(sys.argv[1]).upper())

