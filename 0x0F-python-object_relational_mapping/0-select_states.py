#!/usr/bin/python3

# List all states from the database htn_0e_0_usa
# Usage: ./0-select_staes.py (username, password, name)

#import sys
import MySQLdb
#if __name__ == "__main__":
#    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
#   cur = conn.cursor()

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
