#!/usr/bin/ python3
"""
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""


import sys
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    arg = argv[4]
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC", (arg,))

    states = cur.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
        # print(state)

    cur.close()
    db.close()
