#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states table
where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=database,
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
