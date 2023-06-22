#!/usr/bin/python3
"""
Get a state
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    state_name = argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name == state_name)
    records = query.all()

    if records:
        for record in records:
            print(record.id)
    else:
        print("Not found")
