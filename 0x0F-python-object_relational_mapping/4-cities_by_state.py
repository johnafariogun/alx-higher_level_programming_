#!/usr/bin/python3
"""
this lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    connect = db.cursor()
    connect.execute("SELECT city.id, city.name, state.name FROM `cities` as\
            city INNER JOIN `states` as\
            `state` ON city.state_id = state.id ORDER BY city.id")
    cities = connect.fetchall()
    [print(city) for city in cities]
