#!/usr/bin/python3
"""
A  script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    query = """SELECT cities.name FROM cities
                WHERE cities.state_id=(SELECT states.id
                FROM states WHERE states.name LIKE %s)
                ORDER BY cities.id ASC"""
    cur.execute(query, (argv[4],))
    result = cur.fetchall()
    for index, row in enumerate(result):
        if index == len(result) - 1:
            print(row[0], end=" ")
        else:
            print(row[0], end=", ")
    print()
    cur.close()
    conn.close()
