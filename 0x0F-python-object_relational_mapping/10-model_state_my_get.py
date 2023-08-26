#!/usr/bin/python3
"""
Prints the State object's id with the given name from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Take command-line arguments for MySQL username, password, database name, and state name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object's id with the provided state name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result or "Not found"
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close the session
    session.close()
