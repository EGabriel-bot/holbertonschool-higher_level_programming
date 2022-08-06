#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
 where name matches the argument"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        password=sys.argv[2], database=sys.argv[3])
    name = sys.argv[4]
    c = db.cursor()
    query = f"SELECT * FROM states WHERE name LIKE '{name}%'\
         ORDER BY id ASC"
    c.execute(query)
    for state in c.fetchall():
        print(state)
