#!/usr/bin/python3

"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. Safe from SQL injection.
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

    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
