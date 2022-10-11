#!/usr/bin/python3

"""
    script that lists all cities from the database hbtn_0e_4_usa
    script should take 3 arguments: <mysql username>\
            <mysql password>\ <database name>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    dbase = MySQLdb.connect(user=argv[1], passwd=argv[2], db= argv[3])
    cur= dbase.cursor()
    cur.execute("SELECT c.id, c.name, c.name\
            FROM states s\
            JOIN cities c\
            ON s.id = state_id")
    cities = cur.fetchall()
    for city in cities:
        print(city)

    """ cur.iexecute(SELECT s.id, s.name, c.name
            FROM states c\
            JOIN cities s\
            ON c.id = state_id)
    """
