#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
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

    query = "SELECT cities.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))

    data = cursor.fetchall()

    # Extract city names from the tuples and join them with commas
    city_names = ', '.join(row[0] for row in data)

    print(city_names)

    cursor.close()
    db.close()
