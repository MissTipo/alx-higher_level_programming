#!/usr/bin/ python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import sys
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306)
    #arg = argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id"
                )
    # cur.execute(f"SELECT * FROM states WHERE id = {sys.argv[4]}")

    states = cur.fetchall()
    #[print(city) for city in cur.fetchall()]

    for city in states:
        """if state[1] == sys.argv[4]:
            print(state)"""
        print(city)

    cur.close()
    db.close()
