#!/usr/bin/python3

"""
    script takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    script takes in 4 arguments <mysql username>,\
            <mysql password>,\
            <database name>\
            <state name searched>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn =  MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    nme = argv[4] 
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        if state[1] == nme:
            print(state)
