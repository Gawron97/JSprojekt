

from database import Base, engine

def database_config():
    Base.metadata.create_all(engine)