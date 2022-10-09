#!/usr/bin/python3

"""
    this  list all the state with a name starng with N from the
    database hbtn_0e_0_usa
    the module takes 3 arguments <mysql username>, <mysql password>
    <database name>
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = dbase.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^[N]'")
    query_table = cur.fetchall()
    for state in query_table:
        print(state)
