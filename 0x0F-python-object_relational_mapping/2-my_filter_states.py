#!/usr/bin/python3
"""
this lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    connect = db.cursor()
    connect.execute("SELECT * FROM `states` ORDER BY `id`")
    states = connect.fetchall()
    [print(state) for state in states if state[1] == sys.argv[4]]
