#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])

    name = sys.argv[4]
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE %s ORDER BY cities.id", (name,))

    fetch = c.fetchall()

    if not fetch:
        print()

    for i, cities in enumerate(fetch):
        if i == len(fetch) - 1:
            print("{}".format(str(cities[0])))
        else:
            print("{}, ".format(str(cities[0])), end="")
