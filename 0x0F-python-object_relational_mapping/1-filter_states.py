#!/usr/bin/python3
"""lists all states with a name starting with N"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for state in c.fetchall():
        if state[1][0] == 'N':
            print(state)
