from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:password1234@localhost:5432/budzet')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)