#!/usr/bin/ python3
"""
Ascript that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb
# db = MySQLdb.connect(mysql username=sys.argv[0],mysql
# password=sys.argv[1],database name=sys.argv[3],localhost=3306)
if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)

    cur = db.cursor()
   # cur.execute("SELECT * FROM states WHERE Name REGEXP '^[N].*$'")
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")

    states = cur.fetchall()

    for state in states:
        print(state)
        """ if state[1][0] == 'N':
            print(state)"""

    cur.close()
    db.close()
