#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute(
        "SELECT cities.id, cities.name, states.name \
            FROM cities INNER JOIN states ON cities.state_id = states.id;")
    [print(cities) for cities in c.fetchall()]
