#!/usr/bin/python3

# List all states from the database htn_0e_0_usa
# Usage: ./0-select_staes.py (username, password, name)

import sys
import MySQLdb
if __name__ == "__main__":
conn = db.MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.arg[3])
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
states = cur.fetchall()
for state in states:
    print(state)
cur.close()
conn.close()
