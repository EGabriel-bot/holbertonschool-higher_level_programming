#!/usr/bin/python3
"""safe from MySQL injections!"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    name = sys.argv[4]
    c = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC;", (name,)
    if type(name) is not str:
        raise TypeError('state name needs to be a string')
    c.execute(query)
    for state in c.fetchall():
        if state[1] == name:
            print(state)
    db.close()
