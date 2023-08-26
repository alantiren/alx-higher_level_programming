#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Take command-line arguments for MySQL username, password, database name, and state name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection and execute
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows and display the results
    cities = [row[0] for row in cursor.fetchall()]
    print(', '.join(cities))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
