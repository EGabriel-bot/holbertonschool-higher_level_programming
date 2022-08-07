#!/usr/bin/python3
"""Start link to table in database"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """create engine to execute queries"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State, City).filter(State.id == City.state_id).all()

    for row1, row2 in result:
        print(f"{row1.name}: ({row2.id}) {row2.name}")
