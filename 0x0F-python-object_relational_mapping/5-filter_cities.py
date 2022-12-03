#!/usr/bin/ python3
"""
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
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
    arg = argv[4]
    cur = db.cursor()
    """cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.id=states.id\
            ORDER BY cities.id")"""

    cur.execute("SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name LIKE BINARY '{:s}' ORDER BY cities.id ASC".format(argv[4],)
                )
    # cur.execute(f"SELECT * FROM states WHERE id = {sys.argv[4]}")

    states = cur.fetchall()
    print(",".join(city[0] for city in states))

    """for city in states:
        if states is not None:
            print(",".join[city])"""

    cur.close()
    db.close()
