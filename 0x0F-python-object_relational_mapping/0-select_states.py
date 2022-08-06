#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb
db = MySQLdb.connect(
    host="localhost", port=3306, user=sys.argv[1],
    password=sys.argv[2], database=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM states;")
[print(state) for state in c.fetchall()]
