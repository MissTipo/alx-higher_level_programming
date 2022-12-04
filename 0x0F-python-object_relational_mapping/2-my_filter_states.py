#!/usr/bin/ python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
from sys import argv
import MySQLdb
# db = MySQLdb.connect(mysql username=sys.argv[0],mysql
# password=sys.argv[1],database name=sys.argv[3],localhost=3306)
if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)
    # staname = argv[4]
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{:s}' ORDER BY id ASC"
        .format(sys.argv[4]))
    # cur.execute(f"SELECT * FROM states WHERE id = {sys.argv[4]}")

    states = cur.fetchall()

    for state in states:
        """if state[1] == sys.argv[4]:
            print(state)"""
        print(state)

    cur.close()
    db.close()
