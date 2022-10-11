#!/usr/bin/python3

"""
    script that lists all cities from the database hbtn_0e_4_usa
    script should take 3 arguments: <mysql username>
            <mysql password> <database name>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    sta_arg == argv[4]
    cur = dbase.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM cities c \
            JOIN states s ON s.id = state_id")
    cities = cur.fetchall()
    for city in cities:
        if (city[2] == sta_arg):
            print(city)
        else:
            print("kosise")
