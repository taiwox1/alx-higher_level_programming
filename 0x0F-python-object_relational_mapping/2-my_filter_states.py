#!/usr/bin/python3

"""
    This script displays values in state all value in states table of
    hbtn_0e_0_usa where name matches the argument.

    script thakes 4 arguments: <mysql username>, <mysql password>,
    <database name> and <state name searched>
"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    search_name = argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states_guery = cur.fetchall()
    for state in states_guery:
        if state[1] == search_name:
            print(state)
    cur.close()
    db.close()
