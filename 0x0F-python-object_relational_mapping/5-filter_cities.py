#!/usr/bin/python3
"""
this lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    connect = db.cursor()
    connect.execute("SELECT * FROM `cities` as city INNER JOIN `states` as\
            `state` ON city.state_id = state.id WHERE state.name = %s ORDER BY\
            city.id", (sys.argv[4],))
    cities = connect.fetchall()
    print(', '.join([city[2] for city in cities]))
